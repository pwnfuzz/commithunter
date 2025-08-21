# Security Updates Monitor

*Last updated: 2025-08-21 18:20:57 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 9 |
| COMMIT | 2 |
| PR | 3 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-x67c-v8jr-p29r](https://github.com/advisories/GHSA-x67c-v8jr-p29r): Mattermost Fails to Sanitize Path Traversal Sequences (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost-server) | MODERATE (CVSS: 6.8) | 2025-08-21 |
| GHSA | [GHSA-GHSA-q453-638c-h4mr](https://github.com/advisories/GHSA-q453-638c-h4mr): Mattermost Fails to Validate Remote Cluster Upload Sessions (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost-server) | MODERATE (CVSS: 6.8) | 2025-08-21 |
| GHSA | [GHSA-GHSA-4276-cm8c-788h](https://github.com/advisories/GHSA-4276-cm8c-788h): Mattermost Fails to Properly Validate Team Role Modification (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost-server) | LOW (CVSS: 3.8) | 2025-08-21 |
| GHSA | [GHSA-GHSA-pwvr-grqg-7vp2](https://github.com/advisories/GHSA-pwvr-grqg-7vp2): Mattermost Lack of Access Control Validation (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server) | LOW (CVSS: 3.5) | 2025-08-21 |
| GHSA | [GHSA-GHSA-qj47-w9f2-qg44](https://github.com/advisories/GHSA-qj47-w9f2-qg44): Mattermost Does Not Sanitize the Team Invite ID (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost-server) | MODERATE (CVSS: 4.3) | 2025-08-21 |
| GHSA | [GHSA-GHSA-vqwh-5jhh-vc9p](https://github.com/advisories/GHSA-vqwh-5jhh-vc9p): Mattermost Server SSRF Vulnerability via the Agents Plugin (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server) | LOW (CVSS: 3.5) | 2025-08-21 |
| GHSA | [GHSA-GHSA-7h24-c332-p48c](https://github.com/advisories/GHSA-7h24-c332-p48c): vproxy Divide by Zero DoS Vulnerability (RUST/vproxy) | HIGH (CVSS: 7.5) | 2025-07-30 |
| GHSA | [GHSA-GHSA-6qjf-g333-pv38](https://github.com/advisories/GHSA-6qjf-g333-pv38): Job Iteration API is vulnerable to OS Command Injection attack through its CsvEnumerator class (RUBYGEMS/job-iteration) | CRITICAL (CVSS: 0.0) | 2025-07-14 |
| GHSA | [GHSA-GHSA-8vmr-h7h5-cqhg](https://github.com/advisories/GHSA-8vmr-h7h5-cqhg): matrix-media-repo (MMR) allows unauthenticated writes to the media repository, which may allow planting of problematic content (GO/github.com/t2bot/matrix-media-repo) | MODERATE (CVSS: 5.3) | 2025-01-16 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [eb4a099](https://github.com/torvalds/linux/commit/eb4a0992ddae04ad5b402029a430b2fa06c81647) | Merge tag '6.17-rc2-ksmbd-server-fixes' of git://git.samba.org/ksmbd | 2025-08-21 |
| chromium/chromium | [0cbd506](https://github.com/chromium/chromium/commit/0cbd506a1712a02f9abad68492bf5aba8b7d54e8) | Fix use-after-free in StructuredMetricsServiceTest teardown. | 2025-08-20 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#27044](https://github.com/openssl/openssl/pull/27044) | fix potential null pointer dereference in cms_main function in apps/cms.c #26941 | 2025-08-21 |
| erlang/otp | [#9790](https://github.com/erlang/otp/pull/9790) | otp scan PRs for vulnerabilities | 2025-08-21 |
| erlang/otp | [#10095](https://github.com/erlang/otp/pull/10095) | Fix for httpd CGI scripts | 2025-08-21 |

