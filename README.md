# Security Updates Monitor

*Last updated: 2025-08-06 09:23:00 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 10 |
| COMMIT | 1 |
| PR | 3 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-57q2-6cp4-9mq3](https://github.com/advisories/GHSA-57q2-6cp4-9mq3): XWiki exposes passwords and emails stored in fields not named password/email in xml.vm (MAVEN/org.xwiki.platform:xwiki-platform-legacy-oldcore, MAVEN/org.xwiki.platform:xwiki-platform-legacy-oldcore, MAVEN/org.xwiki.platform:xwiki-platform-legacy-oldcore) | HIGH (CVSS: 0.0) | 2025-08-05 |
| GHSA | [GHSA-GHSA-r38m-cgpg-qj69](https://github.com/advisories/GHSA-r38m-cgpg-qj69): XWiki leaks password hashes and other accessible password properties (MAVEN/org.xwiki.platform:xwiki-platform-legacy-oldcore, MAVEN/org.xwiki.platform:xwiki-platform-legacy-oldcore, MAVEN/org.xwiki.platform:xwiki-platform-legacy-oldcore) | HIGH (CVSS: 0.0) | 2025-08-05 |
| GHSA | [GHSA-GHSA-h5rc-j5f5-3gcm](https://github.com/advisories/GHSA-h5rc-j5f5-3gcm): russh is missing overflow checks during channel windows adjust (RUST/russh) | MODERATE (CVSS: 6.5) | 2025-08-04 |
| GHSA | [GHSA-GHSA-x56v-x2h6-7j34](https://github.com/advisories/GHSA-x56v-x2h6-7j34): Claude Code echo command allowed bypass of user approval prompt for command execution (NPM/@anthropic-ai/claude-code) | HIGH (CVSS: 0.0) | 2025-08-04 |
| GHSA | [GHSA-GHSA-pmw4-pwvc-3hx2](https://github.com/advisories/GHSA-pmw4-pwvc-3hx2): Claude Code Research Preview has a Path Restriction Bypass which could allow unauthorized file access (NPM/@anthropic-ai/claude-code) | HIGH (CVSS: 0.0) | 2025-08-04 |
| GHSA | [GHSA-GHSA-mm3p-j368-7jcr](https://github.com/advisories/GHSA-mm3p-j368-7jcr): IPX Allows Path Traversal via Prefix Matching Bypass (NPM/ipx, NPM/ipx, NPM/ipx) | MODERATE (CVSS: 0.0) | 2025-08-04 |
| GHSA | [GHSA-GHSA-vf2r-cxg9-p7rf](https://github.com/advisories/GHSA-vf2r-cxg9-p7rf): The ADOdb sqlite3 driver allows SQL injection (COMPOSER/adodb/adodb-php) | CRITICAL (CVSS: 10.0) | 2025-08-04 |
| GHSA | [GHSA-GHSA-mqcp-p2hv-vw6x](https://github.com/advisories/GHSA-mqcp-p2hv-vw6x): Thor can construct an unsafe shell command from library input. (RUBYGEMS/thor) | HIGH (CVSS: 7.9) | 2025-07-20 |
| GHSA | [GHSA-GHSA-969w-gqqr-g6j3](https://github.com/advisories/GHSA-969w-gqqr-g6j3): MLflow Cross-Site Request Forgery (CSRF) vulnerability (PIP/mlflow) | MODERATE (CVSS: 5.4) | 2025-03-20 |
| GHSA | [GHSA-GHSA-9j5q-479x-43g2](https://github.com/advisories/GHSA-9j5q-479x-43g2): @stryker-mutator/util vulnerable to Prototype Pollution (NPM/@stryker-mutator/util) | HIGH (CVSS: 7.5) | 2025-02-06 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| wazuh/wazuh | [caf800a](https://github.com/wazuh/wazuh/commit/caf800aa065489cd3c9ed89b92c030dbe04c561a) | Merge pull request #31221 from wazuh/enhancement/30932-complete-python-vuln-scans | 2025-08-05 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28059](https://github.com/openssl/openssl/pull/28059) | Add array memory allocation routines | 2025-08-06 |
| openssl/openssl | [#28184](https://github.com/openssl/openssl/pull/28184) | Fix integer overflow in date_to_julian() call | 2025-08-06 |
| wazuh/wazuh | [#31221](https://github.com/wazuh/wazuh/pull/31221) | Add embedded Python and its builtins to vulnerability checks - Implementation | 2025-08-05 |

