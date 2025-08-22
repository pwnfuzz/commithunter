# Security Updates Monitor

*Last updated: 2025-08-22 06:21:50 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 13 |
| COMMIT | 2 |
| PR | 5 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-9gjj-6gj7-c4wj](https://github.com/advisories/GHSA-9gjj-6gj7-c4wj): Denial-of-Service attack in pyLoad CNL Blueprint using dukpy.evaljs (PIP/pyload-ng) | HIGH (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-x67c-v8jr-p29r](https://github.com/advisories/GHSA-x67c-v8jr-p29r): Mattermost Fails to Sanitize Path Traversal Sequences (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost-server) | MODERATE (CVSS: 6.8) | 2025-08-21 |
| GHSA | [GHSA-GHSA-q453-638c-h4mr](https://github.com/advisories/GHSA-q453-638c-h4mr): Mattermost Fails to Validate Remote Cluster Upload Sessions (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost-server) | MODERATE (CVSS: 6.8) | 2025-08-21 |
| GHSA | [GHSA-GHSA-4276-cm8c-788h](https://github.com/advisories/GHSA-4276-cm8c-788h): Mattermost Fails to Properly Validate Team Role Modification (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost-server) | LOW (CVSS: 3.8) | 2025-08-21 |
| GHSA | [GHSA-GHSA-pwvr-grqg-7vp2](https://github.com/advisories/GHSA-pwvr-grqg-7vp2): Mattermost Lack of Access Control Validation (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server) | LOW (CVSS: 3.5) | 2025-08-21 |
| GHSA | [GHSA-GHSA-qj47-w9f2-qg44](https://github.com/advisories/GHSA-qj47-w9f2-qg44): Mattermost Does Not Sanitize the Team Invite ID (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost-server) | MODERATE (CVSS: 4.3) | 2025-08-21 |
| GHSA | [GHSA-GHSA-vqwh-5jhh-vc9p](https://github.com/advisories/GHSA-vqwh-5jhh-vc9p): Mattermost Server SSRF Vulnerability via the Agents Plugin (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server) | LOW (CVSS: 3.5) | 2025-08-21 |
| GHSA | [GHSA-GHSA-r4mg-4433-c7g3](https://github.com/advisories/GHSA-r4mg-4433-c7g3): Active Storage allowed transformation methods that were potentially unsafe (RUBYGEMS/activestorage, RUBYGEMS/activestorage, RUBYGEMS/activestorage) | CRITICAL (CVSS: 0.0) | 2025-08-14 |
| GHSA | [GHSA-GHSA-76r7-hhxj-r776](https://github.com/advisories/GHSA-76r7-hhxj-r776): Active Record logging vulnerable to ANSI escape injection (RUBYGEMS/activerecord, RUBYGEMS/activerecord, RUBYGEMS/activerecord) | MODERATE (CVSS: 0.0) | 2025-08-13 |
| GHSA | [GHSA-GHSA-7h24-c332-p48c](https://github.com/advisories/GHSA-7h24-c332-p48c): vproxy Divide by Zero DoS Vulnerability (RUST/vproxy) | HIGH (CVSS: 7.5) | 2025-07-30 |
| GHSA | [GHSA-GHSA-8fxg-mr34-jqr8](https://github.com/advisories/GHSA-8fxg-mr34-jqr8): NocoDB SQL Injection vulnerability (NPM/nocodb) | MODERATE (CVSS: 6.5) | 2024-05-13 |
| GHSA | [GHSA-GHSA-qg73-g3cf-vhhh](https://github.com/advisories/GHSA-qg73-g3cf-vhhh): NocoDB Allows Preview of Files with Dangerous Content (NPM/nocodb) | MODERATE (CVSS: 5.7) | 2024-05-13 |
| GHSA | [GHSA-GHSA-h6r4-xvw6-jc5h](https://github.com/advisories/GHSA-h6r4-xvw6-jc5h): NocoDB Vulnerable to Stored Cross-Site Scripting in Formula.vue (NPM/nocodb) | HIGH (CVSS: 7.3) | 2024-05-13 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [b15ce2e](https://github.com/chromium/chromium/commit/b15ce2eb31488788a1fd40e1ae75f2551dfdeb05) | Roll V8 from 7a52429bd26c to fcbc1059cb18 (26 revisions) | 2025-08-22 |
| torvalds/linux | [eb4a099](https://github.com/torvalds/linux/commit/eb4a0992ddae04ad5b402029a430b2fa06c81647) | Merge tag '6.17-rc2-ksmbd-server-fixes' of git://git.samba.org/ksmbd | 2025-08-21 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| langflow-ai/langflow | [#9491](https://github.com/langflow-ai/langflow/pull/9491) | build(deps): bump sha.js from 2.4.11 to 2.4.12 in /docs | 2025-08-22 |
| erlang/otp | [#9956](https://github.com/erlang/otp/pull/9956) | chore(deps): update github-actions (maint-28) | 2025-08-21 |
| erlang/otp | [#9790](https://github.com/erlang/otp/pull/9790) | otp scan PRs for vulnerabilities | 2025-08-21 |
| erlang/otp | [#10095](https://github.com/erlang/otp/pull/10095) | Fix for httpd CGI scripts | 2025-08-21 |
| langflow-ai/langflow | [#9441](https://github.com/langflow-ai/langflow/pull/9441) | fix: update CORS configuration and add env vars to allow for user control | 2025-08-21 |

