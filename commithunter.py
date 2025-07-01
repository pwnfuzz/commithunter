import os
import re
import sys
import json
import requests
import feedparser
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import List, Dict, Any

# -------------------------
# Configuration
# -------------------------

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
    r"CVE-\d{4}-\d+",
    r"GHSA-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}",
    r"\bsecurity advisory\b",
    r"\bexploit(?:ation)?\b",
    r"\bvulnerability\b",
    r"\bvuln(?:erability)?\b",
    r"\binsecure\b",
    r"\bsecurity (?:fix|patch|update)\b",
    r"\b(?:buffer|heap|stack|integer)[- ]?overflow\b",
    r"\buse[- ]?after[- ]?free\b",
    r"\buaf\b",
    r"\bdouble[- ]?free\b",
    r"\bmemory[- ]?(?:corruption|violation)\b",
    r"\bnull[- ]?pointer\b",
    r"\buninitialized (?:memory|access)\b",
    r"\b(?:arbitrary|remote)[- ]?code[- ]?execution\b",
    r"\brce\b",
    r"\bcommand[- ]?injection\b",
    r"\b(?:xss|csrf|ssrf|sql(?:i| injection))\b",
    r"\b(?:cross[- ]?site|server[- ]?side)[- ]?(?:scripting|request[- ]?forgery)\b",
    r"\bxxe\b",
    r"\bprivilege[- ]?escalation\b",
    r"\bpriv[- ]?esc\b",
    r"\b(?:auth(?:entication|orization)|auth[zn])[- ]?bypass\b",
    r"\binformation[- ]?leak\b",
    r"\binfo[- ]?disclosure\b",
    r"\b(?:sensitive|secret)[- ]?exposure\b",
    r"\b(?:read|write)[- ]?beyond[- ]?bounds\b",
    r"\boob\b",
    r"\baccess[- ]?violation\b",
    r"\b(?:dos|denial[- ]?of[- ]?service)\b",
    r"\bcrash(?:ing)?[- ]?(?:bug|vuln)\b",
    r"\b(?:sanitize|validate|escape)[- ]?(?:input|output)\b",
    r"\b(?:bound|range)[- ]?check\b",
    r"^fix(?:\(security\)|:.*security)",
    r"^security:",
    r"\[security\]",
]

KEYWORD_PATTERN = re.compile("|".join(SECURITY_KEYWORDS), re.IGNORECASE)

OUTPUT_ROOT = Path("output")
LOOKBACK_HOURS = int(os.getenv("LOOKBACK_HOURS", "24"))

GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {
    "Accept": "application/vnd.github+json",
    **({"Authorization": f"Bearer {GITHUB_TOKEN}"} if GITHUB_TOKEN else {})
}

MIN_EPSS_SCORE = 0.1

# Openwall OSS Security archive URL (last 3 days)
OPENWALL_OSS_URL = "https://www.openwall.com/lists/oss-security/atom/"

# ZDI RSS feed URL for published advisories in 2025
ZDI_RSS_URL = "https://www.zerodayinitiative.com/rss/published/2025/"

# -------------------------
# GitHub API Helpers
# -------------------------

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

# -------------------------
# Fetch GitHub commits, PRs, advisories
# -------------------------

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
        filtered = [pr for pr in batch if pr.get("updated_at", "") >= since_iso]
        prs.extend(filtered)
        if len(batch) < 100 or len(filtered) < 100:
            break
        page += 1
    return prs

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

# -------------------------
# Matching helpers
# -------------------------

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

# -------------------------
# Openwall OSS Security Feed (Atom)
# -------------------------

def fetch_openwall_oss_entries(since_time: datetime) -> List[Dict[str, Any]]:
    try:
        feed = feedparser.parse(OPENWALL_OSS_URL)
    except Exception as e:
        print(f"Failed to parse Openwall OSS feed: {e}", file=sys.stderr)
        return []

    entries = []
    for entry in feed.entries:
        # entry.published_parsed is a time.struct_time in UTC
        published_dt = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
        if published_dt < since_time:
            continue
        # Filter by keywords in title or summary
        text = f"{entry.title}\n{entry.summary}"
        if KEYWORD_PATTERN.search(text):
            entries.append({
                "title": entry.title,
                "link": entry.link,
                "published": published_dt.isoformat(),
                "summary": entry.summary
            })
    return entries

# -------------------------
# ZDI RSS Feed parsing
# -------------------------

def extract_severity_from_zdi_entry(entry) -> str:
    # Usually severity is in the summary or tags; check tags first
    severity = None
    if "tags" in entry:
        for tag in entry.tags:
            if "term" in tag and tag.term.lower() in ("critical", "high", "medium", "low"):
                severity = tag.term
                break
    if not severity:
        # Fallback: check summary for severity keyword
        summary = entry.get("summary", "").lower()
        for sev in ("critical", "high", "medium", "low"):
            if sev in summary:
                severity = sev
                break
    return severity or ""

def fetch_zdi_high_severity(since_time: datetime) -> List[Dict[str, Any]]:
    try:
        feed = feedparser.parse(ZDI_RSS_URL)
    except Exception as e:
        print(f"Failed to parse ZDI RSS feed: {e}", file=sys.stderr)
        return []

    entries = []
    for entry in feed.entries:
        published_dt = None
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            published_dt = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
        elif hasattr(entry, "updated_parsed") and entry.updated_parsed:
            published_dt = datetime(*entry.updated_parsed[:6], tzinfo=timezone.utc)
        else:
            continue
        if published_dt < since_time:
            continue
        severity = extract_severity_from_zdi_entry(entry).lower()
        if severity in ("high", "critical"):
            entries.append({
                "title": entry.title,
                "link": entry.link,
                "published": published_dt.isoformat(),
                "summary": entry.get("summary", "")
            })
    return entries

# -------------------------
# Format output as markdown
# -------------------------

def summarize_commit(commit: Dict[str, Any], repo: str) -> str:
    sha = commit.get("sha", "")[:7]
    url = commit.get("html_url") or f"https://github.com/{repo}/commit/{sha}"
    message = commit.get("commit", {}).get("message", "").splitlines()[0]
    date = commit.get("commit", {}).get("author", {}).get("date", "")
    return f"- [{repo} Commit {sha}]({url}) - {message} ({date})"

def summarize_pr(pr: Dict[str, Any], repo: str) -> str:
    num = pr.get("number")
    url = pr.get("html_url")
    title = pr.get("title")
    updated = pr.get("updated_at")
    return f"- [{repo} PR #{num}]({url}) - {title} ({updated})"

def summarize_advisory(advisory: Dict[str, Any], repo: str) -> str:
    ghsa_id = advisory.get("ghsaId", "N/A")
    url = advisory.get("permalink", "")
    desc = advisory.get("description", "").splitlines()[0]
    severity = advisory.get("severity", "N/A")
    epss_score = advisory.get("epss", {}).get("score", 0)
    published = advisory.get("publishedAt", "N/A")
    return f"- [{repo} GHSA {ghsa_id}]({url}) - {desc} (Severity: {severity}, EPSS: {epss_score}, Published: {published})"

def summarize_oss_entry(entry: Dict[str, Any]) -> str:
    title = entry.get("title", "")
    link = entry.get("link", "")
    published = entry.get("published", "")
    return f"- [OSS-Security]({link}) - {title} ({published})"

def summarize_zdi_entry(entry: Dict[str, Any]) -> str:
    title = entry.get("title", "")
    link = entry.get("link", "")
    published = entry.get("published", "")
    return f"- [ZDI Advisory]({link}) - {title} ({published})"

# -------------------------
# Main process
# -------------------------

def main():
    now = datetime.now(timezone.utc)
    since = now - timedelta(hours=LOOKBACK_HOURS)
    since_iso = since.isoformat()

    print(f"Fetching data since {since_iso}...")

    all_results = []

    # --- GitHub commits, PRs, advisories ---
    for repo in REPOSITORIES:
        print(f"Processing repo: {repo}")

        commits = fetch_recent_commits(repo, since_iso)
        filtered_commits = [c for c in commits if commit_matches(c)]

        prs = fetch_recent_prs(repo, since_iso)
        filtered_prs = [pr for pr in prs if pr_matches(pr)]

        advisories = fetch_ghsa_advisories(repo)
        filtered_advisories = [a for a in advisories if advisory_matches(a)]

        for c in filtered_commits:
            all_results.append(summarize_commit(c, repo))
        for pr in filtered_prs:
            all_results.append(summarize_pr(pr, repo))
        for adv in filtered_advisories:
            all_results.append(summarize_advisory(adv, repo))

    # --- OSS-Security mailing list ---
    oss_entries = fetch_openwall_oss_entries(since)
    for entry in oss_entries:
        all_results.append(summarize_oss_entry(entry))

    # --- ZDI RSS ---
    zdi_entries = fetch_zdi_high_severity(since)
    for entry in zdi_entries:
        all_results.append(summarize_zdi_entry(entry))

    if not all_results:
        print("No matching security-related items found in the timeframe.")
        return

    # Create output folder with date
    output_dir = OUTPUT_ROOT / now.strftime("%Y-%m-%d")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"security_updates_{now.strftime('%Y%m%d_%H%M%S')}.md"

    with output_file.open("w", encoding="utf-8") as f:
        f.write(f"# Security Updates Report - {now.strftime('%Y-%m-%d %H:%M:%S UTC')}\n\n")
        f.write(f"Updates collected from GitHub repos, OSS Security mailing list, and ZDI RSS feed for the past {LOOKBACK_HOURS} hours.\n\n")
        f.write("## Summary\n\n")
        for line in all_results:
            f.write(line + "\n")

    print(f"Report written to {output_file}")


if __name__ == "__main__":
    main()