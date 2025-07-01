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
    "langflow-ai/langflow",
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

def fetch_ghsa_advisories(since: datetime) -> List[Dict[str, Any]]:
    print("Fetching recent GitHub Security Advisories...")
    advisories = []
    after = None
    query = """
    query($after: String, $since: DateTime!) {
      securityAdvisories(
        first: 100,
        after: $after,
        orderBy: {field: UPDATED_AT, direction: DESC},
        updatedSince: $since
      ) {
        pageInfo {
          hasNextPage
          endCursor
        }
        nodes {
          ghsaId
          summary
          description
          severity
          publishedAt
          updatedAt
          identifiers {
            type
            value
          }
          references {
            url
          }
          vulnerabilities(first: 10) {
            nodes {
              package {
                name
                ecosystem
              }
              vulnerableVersionRange
            }
          }
          cvss {
            score
            vectorString
          }
          permalink
        }
      }
    }
    """
    while True:
        variables = {
            "after": after,
            "since": since.isoformat()
        }
        result = github_graphql_query(query, variables)
        data = result.get("data", {}).get("securityAdvisories", {})
        if not data:
            break
            
        nodes = data.get("nodes", [])
        advisories.extend(nodes)
        
        page_info = data.get("pageInfo", {})
        if not page_info.get("hasNextPage"):
            break
            
        after = page_info.get("endCursor")
        
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
    print(f"Fetching recent Openwall OSS entries...")
    try:
        feed = feedparser.parse(OPENWALL_OSS_URL)
    except Exception as e:
        print(f"Failed to parse Openwall OSS feed: {e}", file=sys.stderr)
        return []

    entries = []
    for entry in feed.entries[:20]:  # Only check most recent 20 entries
        try:
            published_dt = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
            if published_dt < since_time:
                continue
                
            entries.append({
                "title": entry.title,
                "link": entry.link,
                "published": published_dt.isoformat(),
                "summary": entry.get("summary", ""),
                "type": "oss-security"
            })
        except Exception as e:
            print(f"Error processing OSS entry: {e}", file=sys.stderr)
            continue
            
    return entries

# -------------------------
# ZDI RSS Feed parsing
# -------------------------

def extract_severity_from_zdi_entry(entry) -> str:
    print(f"Extracting severity from ZDI entry: {entry.title}")
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

def summarize_commit(commit: Dict[str, Any], repo: str) -> tuple[str, str, str, str, str]:
    sha = commit.get("sha", "")[:7]
    url = commit.get("html_url") or f"https://github.com/{repo}/commit/{sha}"
    message = commit.get("commit", {}).get("message", "").splitlines()[0]
    date = commit.get("commit", {}).get("author", {}).get("date", "")[:10]  # YYYY-MM-DD
    return ("commit", repo, f"[{sha[:7]}]({url})", message, date)

def summarize_pr(pr: Dict[str, Any], repo: str) -> tuple[str, str, str, str, str]:
    num = pr.get("number")
    url = pr.get("html_url")
    title = pr.get("title", "")
    updated = pr.get("updated_at", "")[:10]  # YYYY-MM-DD
    return ("pr", repo, f"[#{num}]({url})", title, updated)

def summarize_advisory(advisory: Dict[str, Any], _: str = "") -> tuple[str, str, str, str, str]:
    ghsa_id = advisory.get("ghsaId", "N/A")
    url = advisory.get("permalink", "")
    description = advisory.get("description", "")
    summary = advisory.get("summary", description.splitlines()[0] if description else "")
    severity = advisory.get("severity", "N/A")
    cvss_score = advisory.get("cvss", {}).get("score", "N/A")
    published = advisory.get("publishedAt", "")[:10]  # YYYY-MM-DD
    
    # Get affected packages
    vulns = advisory.get("vulnerabilities", {}).get("nodes", [])
    packages = []
    for v in vulns[:3]:  # Limit to first 3 packages
        pkg = v.get("package", {})
        if pkg:
            pkg_str = f"{pkg.get('ecosystem', '')}/{pkg.get('name', '')}"
            if pkg_str.strip('/'):
                packages.append(pkg_str)
    
    pkg_info = f" ({', '.join(packages)})" if packages else ""
    title = f"[GHSA-{ghsa_id}]({url}): {summary}{pkg_info}"
    return ("advisory", "GHSA", title, f"{severity} (CVSS: {cvss_score})", published)

def summarize_oss_entry(entry: Dict[str, Any]) -> tuple[str, str, str, str, str]:
    title = entry.get("title", "").strip()
    link = entry.get("link", "")
    published = entry.get("published", "")[:10]  # YYYY-MM-DD
    
    # Try to extract CVE ID if present in title
    cve_match = re.search(r'CVE-\d+-\d+', title.upper())
    if cve_match:
        title = f"{cve_match.group(0)}: {title}"
    
    return ("oss", "OSS-Security", f"[{title}]({link})", "", published)

def summarize_zdi_entry(entry: Dict[str, Any]) -> tuple[str, str, str, str, str]:
    title = entry.get("title", "").strip()
    link = entry.get("link", "")
    published = entry.get("published", "")[:10]  # YYYY-MM-DD
    
    # Extract ZDI ID if present (e.g., ZDI-25-XXX)
    zdi_match = re.search(r'ZDI-\d{2,4}-\d{3,4}', title)
    if zdi_match:
        title = f"{zdi_match.group(0)}: {title}"
    
    return ("zdi", "ZDI", f"[{title}]({link})", "", published)

# -------------------------
# Main process
# -------------------------

def load_existing_entries(output_file: Path) -> set[str]:
    if not output_file.exists():
        return set()
    
    seen = set()
    with output_file.open('r', encoding='utf-8') as f:
        content = f.read()
        # Extract all markdown links [text](url)
        for match in re.finditer(r'\[(.*?)\]\((.*?)\)', content):
            url = match.group(2)
            if '://' in url:  # Only add actual URLs, not anchor links
                seen.add(url)
    return seen

def write_markdown_table(entries: List[tuple], output_file: Path, now: datetime):
    # Sort entries by date (newest first)
    entries.sort(key=lambda x: x[4], reverse=True)
    
    with output_file.open('w', encoding='utf-8') as f:
        # Write header
        f.write("# Security Updates Monitor\n\n")
        f.write(f"*Last updated: {now.strftime('%Y-%m-%d %H:%M:%S UTC')}*\n\n")
        
        # Write summary
        f.write("## Summary\n")
        f.write("| Type | Count |\n")
        f.write("|------|-------|\n")
        from collections import defaultdict
        counts = defaultdict(int)
        for entry in entries:
            counts[entry[0]] += 1
        for entry_type, count in sorted(counts.items()):
            f.write(f"| {entry_type.upper()} | {count} |\n")
        f.write("\n---\n\n")
        
        # Write entries by type
        entry_types = {
            'advisory': 'Security Advisories',
            'oss': 'OSS-Security',
            'zdi': 'ZDI Advisories',
            'commit': 'Code Commits',
            'pr': 'Pull Requests'
        }
        
        for entry_type, display_name in entry_types.items():
            type_entries = [e for e in entries if e[0] == entry_type]
            if not type_entries:
                continue
                
            f.write(f"## {display_name}\n\n")
            f.write("| Source | Title | Severity | Date |\n")
            f.write("|--------|-------|----------|------|\n")
            
            for entry in type_entries:
                _, source, title, severity, date = entry
                f.write(f"| {source} | {title} | {severity or '-'} | {date} |\n")
            
            f.write("\n")

def main():
    now = datetime.now(timezone.utc)
    since = now - timedelta(hours=LOOKBACK_HOURS)
    since_iso = since.isoformat()
    
    # Ensure output directory exists
    output_dir = Path(".")  # Root directory for README.md
    output_file = output_dir / "README.md"
    
    # Load existing entries to avoid duplicates
    seen_entries = load_existing_entries(output_file)
    all_entries = []

    print(f"Fetching data since {since_iso}...")

    # --- GitHub Security Advisories (global) ---
    print("Fetching GitHub Security Advisories...")
    ghsa_advisories = fetch_ghsa_advisories(since)
    for advisory in ghsa_advisories:
        entry = summarize_advisory(advisory, "GHSA")
        url = advisory.get("permalink", "")
        if url and url not in seen_entries:
            all_entries.append(entry)
            seen_entries.add(url)

    # --- OSS-Security mailing list ---
    print("Fetching OSS-Security updates...")
    oss_entries = fetch_openwall_oss_entries(since)
    for entry in oss_entries:
        entry_data = summarize_oss_entry(entry)
        url = entry.get("link", "")
        if url and url not in seen_entries:
            all_entries.append(entry_data)
            seen_entries.add(url)

    # --- Process repository-specific data ---
    for repo in REPOSITORIES:
        print(f"Processing repo: {repo}")
        
        # Process commits
        try:
            commits = fetch_recent_commits(repo, since_iso)
            for commit in commits:
                if commit_matches(commit):
                    entry = summarize_commit(commit, repo)
                    url = commit.get("html_url", "")
                    if url and url not in seen_entries:
                        all_entries.append(entry)
                        seen_entries.add(url)
        except Exception as e:
            print(f"Error processing {repo} commits: {e}", file=sys.stderr)
            
        # Process PRs
        try:
            prs = fetch_recent_prs(repo, since_iso)
            for pr in prs:
                if pr_matches(pr):
                    entry = summarize_pr(pr, repo)
                    url = pr.get("html_url", "")
                    if url and url not in seen_entries:
                        all_entries.append(entry)
                        seen_entries.add(url)
        except Exception as e:
            print(f"Error processing {repo} PRs: {e}", file=sys.stderr)

    # --- ZDI RSS ---
    print("Fetching ZDI advisories...")
    zdi_entries = fetch_zdi_high_severity(since)
    for entry in zdi_entries:
        entry_data = summarize_zdi_entry(entry)
        url = entry.get("link", "")
        if url and url not in seen_entries:
            all_entries.append(entry_data)
            seen_entries.add(url)

    if not all_entries:
        print("No new security-related items found in the timeframe.")
        return

    # Write the complete markdown file
    write_markdown_table(all_entries, output_file, now)
    print(f"Updated {output_file} with {len(all_entries)} entries")
    print(f"Report written to {output_file}")


if __name__ == "__main__":
    main()