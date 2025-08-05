# Security Updates Monitor

*Last updated: 2025-08-05 19:18:05 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 22 |
| COMMIT | 2 |
| PR | 2 |

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
| GHSA | [GHSA-GHSA-fm3m-jrgm-5ppg](https://github.com/advisories/GHSA-fm3m-jrgm-5ppg): RatPanel can perform remote command execution without authorization (GO/github.com/tnborg/panel, GO/github.com/tnborg/panel) | HIGH (CVSS: 0.0) | 2025-08-04 |
| GHSA | [GHSA-GHSA-3c93-92r7-j934](https://github.com/advisories/GHSA-3c93-92r7-j934): Grafana Infinity Datasource Plugin SSRF Vulnerability (GO/github.com/grafana/grafana-infinity-datasource) | MODERATE (CVSS: 5.0) | 2025-08-04 |
| GHSA | [GHSA-GHSA-jgmv-j7ww-jx2x](https://github.com/advisories/GHSA-jgmv-j7ww-jx2x): Koa Open Redirect via Referrer Header (User-Controlled) (NPM/koa, NPM/koa) | LOW (CVSS: 3.5) | 2025-07-29 |
| GHSA | [GHSA-GHSA-cmm8-gw4m-26cw](https://github.com/advisories/GHSA-cmm8-gw4m-26cw): Withdrawn Advisory: JHipster allows privilege escalation via a modified authorities parameter (NPM/generator-jhipster) | LOW (CVSS: 2.9) | 2025-07-25 |
| GHSA | [GHSA-GHSA-w7qc-6grj-w7r8](https://github.com/advisories/GHSA-w7qc-6grj-w7r8): File Browser vulnerable to command execution allowlist bypass (GO/github.com/filebrowser/filebrowser, GO/github.com/filebrowser/filebrowser/v2) | HIGH (CVSS: 8.1) | 2025-06-30 |
| GHSA | [GHSA-GHSA-hc8f-m8g5-8362](https://github.com/advisories/GHSA-hc8f-m8g5-8362): File Browser: Command Execution not Limited to Scope (GO/github.com/filebrowser/filebrowser, GO/github.com/filebrowser/filebrowser/v2) | HIGH (CVSS: 8.1) | 2025-06-30 |
| GHSA | [GHSA-GHSA-4wx8-5gm2-2j97](https://github.com/advisories/GHSA-4wx8-5gm2-2j97): filebrowser allows Stored Cross-Site Scripting through the Markdown preview function (GO/github.com/filebrowser/filebrowser, GO/github.com/filebrowser/filebrowser/v2) | HIGH (CVSS: 7.6) | 2025-06-27 |
| GHSA | [GHSA-GHSA-jj2r-455p-5gvf](https://github.com/advisories/GHSA-jj2r-455p-5gvf): filebrowser Sets Insecure File Permissions (GO/github.com/filebrowser/filebrowser, GO/github.com/filebrowser/filebrowser/v2) | MODERATE (CVSS: 5.5) | 2025-06-27 |
| GHSA | [GHSA-GHSA-3q2w-42mv-cph4](https://github.com/advisories/GHSA-3q2w-42mv-cph4): filebrowser Allows Shell Commands to Spawn Other Commands (GO/github.com/filebrowser/filebrowser, GO/github.com/filebrowser/filebrowser/v2) | HIGH (CVSS: 8.1) | 2025-06-27 |
| GHSA | [GHSA-GHSA-969w-gqqr-g6j3](https://github.com/advisories/GHSA-969w-gqqr-g6j3): MLflow Cross-Site Request Forgery (CSRF) vulnerability (PIP/mlflow) | MODERATE (CVSS: 5.4) | 2025-03-20 |
| GHSA | [GHSA-GHSA-9j5q-479x-43g2](https://github.com/advisories/GHSA-9j5q-479x-43g2): @stryker-mutator/util vulnerable to Prototype Pollution (NPM/@stryker-mutator/util) | HIGH (CVSS: 7.5) | 2025-02-06 |
| GHSA | [GHSA-GHSA-g233-2p4r-3q7v](https://github.com/advisories/GHSA-g233-2p4r-3q7v): Hashicorp Vault vulnerable to denial of service through memory exhaustion (GO/github.com/openbao/openbao, GO/github.com/hashicorp/vault) | HIGH (CVSS: 7.5) | 2024-10-31 |
| GHSA | [GHSA-GHSA-rr8j-7w34-xp5j](https://github.com/advisories/GHSA-rr8j-7w34-xp5j): Vault Community Edition privilege escalation vulnerability (GO/github.com/openbao/openbao, GO/github.com/hashicorp/vault) | HIGH (CVSS: 7.2) | 2024-10-10 |
| GHSA | [GHSA-GHSA-jg74-mwgw-v6x3](https://github.com/advisories/GHSA-jg74-mwgw-v6x3): Vault SSH Secrets Engine Configuration Did Not Restrict Valid Principals By Default (GO/github.com/openbao/openbao, GO/github.com/hashicorp/vault) | HIGH (CVSS: 7.5) | 2024-09-26 |
| GHSA | [GHSA-GHSA-8554-jxcw-454q](https://github.com/advisories/GHSA-8554-jxcw-454q): Webargs mishandles concurrent JSON parsing (PIP/webargs) | HIGH (CVSS: 8.1) | 2019-03-12 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| wazuh/wazuh | [caf800a](https://github.com/wazuh/wazuh/commit/caf800aa065489cd3c9ed89b92c030dbe04c561a) | Merge pull request #31221 from wazuh/enhancement/30932-complete-python-vuln-scans | 2025-08-05 |
| chromium/chromium | [4eceb31](https://github.com/chromium/chromium/commit/4eceb31b729158d2fa7519b43bf3475eb32c2302) | [UAF] avoid early close of animation session | 2025-08-04 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28059](https://github.com/openssl/openssl/pull/28059) | Add array memory allocation routines | 2025-08-05 |
| wazuh/wazuh | [#31221](https://github.com/wazuh/wazuh/pull/31221) | Add embedded Python and its builtins to vulnerability checks - Implementation | 2025-08-05 |

