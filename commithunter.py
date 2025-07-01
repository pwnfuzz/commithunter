import os
import re
import sys
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import List, Dict, Any

import requests

# --------------------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------------------

REPOSITORIES = [
    "torvalds/linux",
    "openssl/openssl",
    "postgres/postgres",
    "chromium/chromium",
    "erlang/otp",
    "wazuh/wazuh",
    "roundcube/roundcubemail",
    "langflow/langflow",
    "simplehelp/simplehelp",
    "hibernate/hibernate-validator"
]

SECURITY_KEYWORDS = [
    # CVEs and advisories (strict patterns)
    r"CVE-\d{4}-\d+",  
    r"GHSA-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}",  # GitHub Advisory IDs
    r"\bsecurity advisory\b",
    
    # Exploits and vulnerabilities
    r"\bexploit(?:ation)?\b",
    r"\bvulnerability\b",
    r"\bvuln(?:erability)?\b",  
    r"\binsecure\b",
    r"\bsecurity (?:fix|patch|update)\b",
    
    # Memory corruption
    r"\b(?:buffer|heap|stack|integer)[- ]?overflow\b",
    r"\buse[- ]?after[- ]?free\b",
    r"\buaf\b",
    r"\bdouble[- ]?free\b",
    r"\bmemory[- ]?(?:corruption|violation)\b",
    r"\bnull[- ]?pointer\b",
    r"\buninitialized (?:memory|access)\b",
    
    # Code execution
    r"\b(?:arbitrary|remote)[- ]?code[- ]?execution\b",
    r"\brce\b",
    r"\bcommand[- ]?injection\b",
    
    # Web vulnerabilities
    r"\b(?:xss|csrf|ssrf|sql(?:i| injection))\b",
    r"\b(?:cross[- ]?site|server[- ]?side)[- ]?(?:scripting|request[- ]?forgery)\b",
    r"\bxxe\b",
    
    # Privilege escalation
    r"\bprivilege[- ]?escalation\b",
    r"\bpriv[- ]?esc\b",
    r"\b(?:auth(?:entication|orization)|auth[zn])[- ]?bypass\b",
    
    # Info leaks
    r"\binformation[- ]?leak\b",
    r"\binfo[- ]?disclosure\b",
    r"\b(?:sensitive|secret)[- ]?exposure\b",
    
    # Access violations
    r"\b(?:read|write)[- ]?beyond[- ]?bounds\b",
    r"\boob\b",
    r"\baccess[- ]?violation\b",
    
    # Denial of Service
    r"\b(?:dos|denial[- ]?of[- ]?service)\b",
    r"\bcrash(?:ing)?[- ]?(?:bug|vuln)\b",
    
    # Secure coding fixes
    r"\b(?:sanitize|validate|escape)[- ]?(?:input|output)\b",
    r"\b(?:bound|range)[- ]?check\b",
    
    # Commit message conventions
    r"^fix(?:\(security\)|:.*security)",  # Conventional Commits
    r"^security:",  
    r"\[security\]",  # GitHub-style tags
]

KEYWORD_PATTERN = re.compile(r"|".join(SECURITY_KEYWORDS), re.IGNORECASE)

OUTPUT_ROOT = Path("output")
LOOKBACK_HOURS = int(os.getenv("LOOKBACK_HOURS", "24"))

GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {
    "Accept": "application/vnd.github+json",
    **({"Authorization": f"Bearer {GITHUB_TOKEN}"} if GITHUB_TOKEN else {})
}

# Minimum EPSS score for GHSA advisories
MIN_EPSS_SCORE = 0.1    

# --------------------------------------------------------------------------------------
# GitHub API Helpers
# --------------------------------------------------------------------------------------

def github_request(url: str, params: Dict[str, Any] | None = None) -> Any:
    response = requests.get(url, headers=HEADERS, params=params, timeout=30)
    response.raise_for_status()
    return response.json()

def github_graphql_query(query: str, variables: Dict[str, Any] = {}) -> Any:
    url = "https://api.github.com/graphql"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    json_payload = {"query": query, "variables": variables}
    response = requests.post(url, headers=headers, json=json_payload, timeout=30)
    response.raise_for_status()
    return response.json()

# --------------------------------------------------------------------------------------
# Fetch commits updated since ISO time
# --------------------------------------------------------------------------------------

def fetch_recent_commits(repo: str, since_iso: str) -> List[Dict[str, Any]]:
    url = f"{GITHUB_API_URL}/repos/{repo}/commits"
    commits: List[Dict[str, Any]] = []
    page = 1
    while True:
        batch = github_request(url, params={"since": since_iso, "per_page": 100, "page": page})
        if not batch:
            break
        commits.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return commits

# --------------------------------------------------------------------------------------
# Fetch PRs updated since ISO time
# --------------------------------------------------------------------------------------

def fetch_recent_prs(repo: str, since_iso: str) -> List[Dict[str, Any]]:
    url = f"{GITHUB_API_URL}/repos/{repo}/pulls"
    prs: List[Dict[str, Any]] = []
    page = 1
    while True:
        batch = github_request(url, params={
            "state": "all",
            "sort": "updated",
            "direction": "desc",
            "per_page": 100,
            "page": page
        })
        if not batch:
            break
        # Filter PRs updated since `since_iso`
        filtered = [pr for pr in batch if pr.get("updated_at", "") >= since_iso]
        prs.extend(filtered)
        if len(batch) < 100 or len(filtered) < 100:
            break
        page += 1
    return prs

# --------------------------------------------------------------------------------------
# Fetch GHSA advisories for a repo via GraphQL (supports pagination)
# --------------------------------------------------------------------------------------

def fetch_ghsa_advisories(repo: str) -> List[Dict[str, Any]]:
    owner, name = repo.split("/")
    advisories = []
    after = None
    query = """
    query($owner: String!, $name: String!, $after: String) {
      repository(owner: $owner, name: $name) {
        vulnerabilityAlerts(first: 100, after: $after) {
          pageInfo {
            hasNextPage
            endCursor
          }
          nodes {
            securityVulnerability {
              advisory {
                ghsaId
                description
                severity
                publishedAt
                identifiers {
                  type
                  value
                }
                references {
                  url
                }
                cvss {
                  score
                }
                epss {
                  score
                }
                permalink
              }
            }
          }
        }
      }
    }
    """
    while True:
        variables = {"owner": owner, "name": name, "after": after}
        result = github_graphql_query(query, variables)
        repo_data = result.get("data", {}).get("repository")
        if not repo_data:
            break
        alerts = repo_data.get("vulnerabilityAlerts")
        if not alerts:
            break
        nodes = alerts.get("nodes", [])
        for node in nodes:
            vuln = node.get("securityVulnerability", {})
            advisory = vuln.get("advisory", {})
            advisories.append(advisory)
        pageInfo = alerts.get("pageInfo", {})
        if pageInfo.get("hasNextPage"):
            after = pageInfo.get("endCursor")
        else:
            break
    return advisories

# --------------------------------------------------------------------------------------
# Matching helpers
# --------------------------------------------------------------------------------------

def commit_matches(commit: Dict[str, Any]) -> bool:
    message = commit.get("commit", {}).get("message", "")
    return bool(KEYWORD_PATTERN.search(message))

def pr_matches(pr: Dict[str, Any]) -> bool:
    title = pr.get("title", "")
    body = pr.get("body", "") or ""
    return bool(KEYWORD_PATTERN.search(title)) or bool(KEYWORD_PATTERN.search(body))

def advisory_matches(advisory: Dict[str, Any]) -> bool:
    severity = advisory.get("severity", "").upper()
    epss_score = advisory.get("epss", {}).get("score") or 0.0
    if severity in ("HIGH", "CRITICAL") and epss_score >= MIN_EPSS_SCORE:
        return True
    return False

# --------------------------------------------------------------------------------------
# Summarization
# --------------------------------------------------------------------------------------

def summarize_entry(entry_type: str, repo: str, url: str, identifier: str, date_str: str) -> str:
    """Return markdown table row."""
    return f"| {date_str} | {entry_type} | [{identifier}]({url}) | {repo} |"

# --------------------------------------------------------------------------------------
# File helpers
# --------------------------------------------------------------------------------------

def ensure_output_path(now: datetime) -> Path:
    path = OUTPUT_ROOT / f"{now.year}" / f"{now.month:02d}"
    path.mkdir(parents=True, exist_ok=True)
    return path / "README.md"

# --------------------------------------------------------------------------------------
# Main logic
# --------------------------------------------------------------------------------------

def main() -> None:
    since_time = datetime.now(timezone.utc) - timedelta(hours=LOOKBACK_HOURS)
    since_iso = since_time.isoformat()

    findings: List[str] = []
    seen: set[str] = set()  # Track unique URLs to avoid duplicates

    for repo in REPOSITORIES:
        # Fetch commits
        try:
            commits = fetch_recent_commits(repo, since_iso)
        except requests.HTTPError as exc:
            print(f"Failed to fetch commits for {repo}: {exc}", file=sys.stderr)
            continue
        for commit in commits:
            if commit_matches(commit):
                sha = commit.get("sha", "")[:7]
                url = commit.get("html_url", "")
                date_str = commit.get("commit", {}).get("committer", {}).get("date", "")
                row = summarize_entry("Commit", repo, url, sha, date_str)
                if url not in seen:
                    seen.add(url)
                    findings.append(row)

        # Fetch PRs
        try:
            prs = fetch_recent_prs(repo, since_iso)
        except requests.HTTPError as exc:
            print(f"Failed to fetch PRs for {repo}: {exc}", file=sys.stderr)
            continue
        for pr in prs:
            if pr_matches(pr):
                pr_number = pr.get("number")
                url = pr.get("html_url")
                date_str = pr.get("updated_at", "")
                row = summarize_entry("PR", repo, url, f"#{pr_number}", date_str)
                if url not in seen:
                    seen.add(url)
                    findings.append(row)

        # Fetch GHSA advisories
        try:
            advisories = fetch_ghsa_advisories(repo)
        except requests.HTTPError as exc:
            print(f"Failed to fetch GHSA advisories for {repo}: {exc}", file=sys.stderr)
            continue
        for adv in advisories:
            if advisory_matches(adv):
                ghsa_id = adv.get("ghsaId", "UNKNOWN")
                permalink = adv.get("permalink", "")
                published_at = adv.get("publishedAt", "")
                row = summarize_entry("Advisory", repo, permalink, ghsa_id, published_at)
                if permalink not in seen:
                    seen.add(permalink)
                    findings.append(row)

    if not findings:
        print("No findings matched keywords or filters.")
        return

    now = datetime.now(timezone.utc)
    readme_path = ensure_output_path(now)

    header = (
        "# Security Relevant Updates\n\n"
        f"_Last updated: {now.strftime('%Y-%m-%d %H:%M UTC')}_\n\n"
        "| Date | Type | Identifier | Repository |\n"
        "| ---- | ---- | ---------- | ---------- |\n"
    )

    # Read existing content if exists to avoid duplication, else write header
    if readme_path.exists():
        with open(readme_path, "r", encoding="utf-8") as f:
            existing_lines = f.readlines()
    else:
        existing_lines = []

    existing_set = set(line.strip() for line in existing_lines if line.startswith("|"))
    new_lines = [line for line in findings if line not in existing_set]

    if not new_lines:
        print("No new findings to append.")
        return

    with open(readme_path, "a", encoding="utf-8") as f:
        if not existing_lines:
            f.write(header)
        f.write("\n".join(new_lines) + "\n")

    print(f"Appended {len(new_lines)} new findings to {readme_path}")

if __name__ == "__main__":
    if not GITHUB_TOKEN:
        print("Error: Please set GITHUB_TOKEN environment variable for authentication.", file=sys.stderr)
        sys.exit(1)
    main()
