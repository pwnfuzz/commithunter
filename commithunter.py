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
    # Kernels
    "torvalds/linux",
    "microsoft/WSL2-Linux-Kernel",

    # Cryptography
    "openssl/openssl",
    "libressl-portable/portable",

    # Runtimes
    "python/cpython",
    "nodejs/node",
    "openjdk/jdk",
    "dotnet/runtime",

    # Browsers
    "chromium/chromium",
    "mozilla/gecko-dev",
    "webkit/WebKit",

    # Web Servers
    "nginx/nginx",
    "apache/httpd",
    "haproxy/haproxy",

    # Databases
    "redis/redis",
    "postgres/postgres",
    "mongodb/mongo",

    # Security Tools
    "radareorg/radare2",
    "ghidra/ghidra",
    "zaproxy/zaproxy",

    # Virtualization
    "qemu/qemu",
    "containerd/containerd",
]

KEYWORDS = [
    r"security",
    r"vuln",
    r"vulnerab(le|ility)",
    r"exploit",
    r"overflow",
    r"buffer[- ]?overflow",
    r"stack[- ]?overflow",
    r"heap[- ]?overflow",
    r"integer[- ]?overflow",
    r"out[- ]?of[- ]?bounds",
    r"oob",
    r"use[- ]?after[- ]?free",
    r"uaf",
    r"double[- ]?free",
    r"null[- ]?pointer",
    r"uninitialized",
    r"memory[- ]?corruption",
    r"arbitrary code",
    r"code[- ]?execution",
    r"race[- ]?condition",
    r"information leak",
    r"info[- ]?leak",
    r"leak",
    r"read[- ]?beyond",
    r"write[- ]?beyond",
    r"privilege[- ]?escalation",
    r"priv[- ]?esc",
    r"overflow",
    r"assertion failure",
    r"segfault",
    r"segmentation fault",
    r"bounds?[- ]?check",
    r"invalid[- ]?access",
    r"invalid[- ]?pointer",
    r"use[- ]?of[- ]?freed",
    r"access violation",
    r"memory[- ]?violation",
    r"cve[-:]?\d{4}-\d+",
    r"patch",
    r"fix(ing)?[- ]?(bug|vuln|issue|sec|cve)",
]

KEYWORD_PATTERN = re.compile(r"|".join(KEYWORDS), re.IGNORECASE)

OUTPUT_ROOT = Path("output")
LOOKBACK_HOURS = int(os.getenv("LOOKBACK_HOURS", "24"))


# --------------------------------------------------------------------------------------
# GitHub API Helpers
# --------------------------------------------------------------------------------------

def github_request(url: str, params: Dict[str, Any] | None = None) -> Any:
    headers = {"Accept": "application/vnd.github+json"}
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    response = requests.get(url, headers=headers, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def fetch_recent_commits(repo: str, since_iso: str) -> List[Dict[str, Any]]:
    url = f"https://api.github.com/repos/{repo}/commits"
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
# Core Logic
# --------------------------------------------------------------------------------------

def commit_matches(commit: Dict[str, Any]) -> bool:
    message = commit.get("commit", {}).get("message", "")
    return bool(KEYWORD_PATTERN.search(message))


def summarize_commit(repo: str, commit: Dict[str, Any]) -> tuple[str, str, str, str]:
    """Return (row_str, repo, sha, date_iso) for markdown table."""
    sha_full = commit.get("sha", "")
    sha = sha_full[:7]
    html_url = commit.get("html_url", "")
    date_str = commit.get("commit", {}).get("committer", {}).get("date", "")

    # Build markdown table row
    row = f"| {date_str} | [{sha}]({html_url}) | {repo} |"
    return row, repo, sha_full, date_str


def ensure_output_path(now: datetime) -> Path:
    path = OUTPUT_ROOT / f"{now.year}" / f"{now.month:02d}"
    path.mkdir(parents=True, exist_ok=True)
    return path / "README.md"


def main() -> None:
    since_time = datetime.now(timezone.utc) - timedelta(hours=LOOKBACK_HOURS)
    since_iso = since_time.isoformat()

    findings: List[str] = []
    seen: set[tuple[str, str]] = set()  # (repo, sha)

    for repo in REPOSITORIES:
        try:
            commits = fetch_recent_commits(repo, since_iso)
        except requests.HTTPError as exc:
            print(f"Failed to fetch commits for {repo}: {exc}", file=sys.stderr)
            continue
        for commit in commits:
            if commit_matches(commit):
                row, _repo, _sha, _ = summarize_commit(repo, commit)
                if (_repo, _sha) not in seen:
                    seen.add((_repo, _sha))
                    findings.append(row)

    # After processing all repositories
    now = datetime.now(timezone.utc)
    output_file = ensure_output_path(now)

        # Build sets of existing rows and SHAs to prevent duplicates across runs or formats
    existing_rows: set[str] = set()
    existing_shas: set[str] = set()
    header_present = False
    if output_file.exists():
        with output_file.open("r", encoding="utf-8") as fp:
            for l in fp:
                line = l.rstrip("\n")
                if line.startswith("| ") and line.count("|") >= 3:
                    existing_rows.add(line)
                if line.strip() == "| Date | Commit | Repo |":
                    header_present = True
                # Collect commit SHAs (7-40 hex chars) from links or code formatting
                for m in re.finditer(r"\b[0-9a-f]{7,40}\b", line):
                    existing_shas.add(m.group(0))

    # Filter out rows whose SHA already present, or duplicate full row
    new_rows: List[str] = []
    for row in findings:
        sha_match = re.search(r"\[([0-9a-f]{7,40})\]", row)
        sha = sha_match.group(1) if sha_match else ""
        if row in existing_rows or sha in existing_shas:
            continue
        existing_rows.add(row)
        existing_shas.add(sha)
        new_rows.append(row)

    if not new_rows:
        print("No new matching commits found in the specified window.")
        return

    header_lines = (
        "| Date | Commit | Repo |\n|------|--------|------|\n"
    )

    with output_file.open("a", encoding="utf-8") as fp:
        if not header_present:
            fp.write("\n\n" + header_lines)
        for line in new_rows:
            fp.write(line + "\n")

    print(f"Wrote {len(new_rows)} new findings to {output_file}")


if __name__ == "__main__":
    main()
