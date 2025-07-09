# Security Updates Monitor

*Last updated: 2025-07-09 19:12:33 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 9 |
| COMMIT | 4 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-gjv4-ghm7-q58q](https://github.com/advisories/GHSA-gjv4-ghm7-q58q): MCP Server Kubernetes vulnerable to command injection in several tools (NPM/mcp-server-kubernetes) | HIGH (CVSS: 7.5) | 2025-07-08 |
| GHSA | [GHSA-GHSA-q93c-p2mw-p23f](https://github.com/advisories/GHSA-q93c-p2mw-p23f): Dagster vulnerable to Path Traversal attack through its /logs endpoint (PIP/dagster) | MODERATE (CVSS: 7.5) | 2025-07-07 |
| GHSA | [GHSA-GHSA-hcgh-r5gq-6qc2](https://github.com/advisories/GHSA-hcgh-r5gq-6qc2): Microweber vulnerable to XSS attack due to insure `group` component in its Settings handler (COMPOSER/microweber/microweber) | LOW (CVSS: 3.5) | 2025-03-12 |
| GHSA | [GHSA-GHSA-vm7w-2724-5m23](https://github.com/advisories/GHSA-vm7w-2724-5m23): Apache StreamPipes has improper privilege management in a REST interface (PIP/streampipes, MAVEN/org.apache.streampipes:streampipes-parent) | MODERATE (CVSS: 6.5) | 2025-03-03 |
| GHSA | [GHSA-GHSA-9fpw-c9x7-cv3j](https://github.com/advisories/GHSA-9fpw-c9x7-cv3j): Mattermost allows remote actor to set arbitrary RemoteId values for synced users (GO/github.com/mattermost/mattermost, GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost/server/v8) | MODERATE (CVSS: 2.7) | 2024-08-01 |
| GHSA | [GHSA-GHSA-v333-7h2p-5fhv](https://github.com/advisories/GHSA-v333-7h2p-5fhv): ZITADEL has improper HTML sanitization in emails and Console UI (GO/github.com/zitadel/zitadel, GO/github.com/zitadel/zitadel, GO/github.com/zitadel/zitadel) | MODERATE (CVSS: 4.3) | 2024-07-31 |
| GHSA | [GHSA-GHSA-q394-h7f5-7f44](https://github.com/advisories/GHSA-q394-h7f5-7f44): Generation of Error Message Containing Sensitive Information in Elasticsearch (MAVEN/org.elasticsearch.client:elasticsearch-rest-client) | MODERATE (CVSS: 6.5) | 2022-05-24 |
| GHSA | [GHSA-GHSA-w9p3-5cr8-m3jj](https://github.com/advisories/GHSA-w9p3-5cr8-m3jj): Deserialization of Untrusted Data in Log4j 1.x (MAVEN/org.zenframework.z8.dependencies.commons:log4j-1.2.17, MAVEN/log4j:log4j) | HIGH (CVSS: 8.8) | 2022-01-21 |
| GHSA | [GHSA-GHSA-86g5-2wh3-gc9j](https://github.com/advisories/GHSA-86g5-2wh3-gc9j): Path Traversal in Action View (RUBYGEMS/actionview, RUBYGEMS/actionview, RUBYGEMS/actionview) | HIGH (CVSS: 7.5) | 2019-03-13 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [8c2e52e](https://github.com/torvalds/linux/commit/8c2e52ebbe885c7eeaabd3b7ddcdc1246fc400d2) | eventpoll: don't decrement ep refcount while still holding the ep mutex | 2025-07-09 |
| chromium/chromium | [37e8c13](https://github.com/chromium/chromium/commit/37e8c13053405e9da98b8b472acfbaf7834472ba) | [bedrock] Null-check BrowserView in ~ChromeLabsBubbleView() | 2025-07-09 |
| chromium/chromium | [e50409c](https://github.com/chromium/chromium/commit/e50409cecb4837cb611707ab52792661d0549c0e) | Glic actor: Throttle navigations for safety checks | 2025-07-09 |
| chromium/chromium | [fceb315](https://github.com/chromium/chromium/commit/fceb3154f98dd80df7c2cd632b04791f584e0da2) | [iOS]Add a delegate to sync encryption view | 2025-07-08 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#27994](https://github.com/openssl/openssl/pull/27994) | test/evp_extra_test.c: Add check for BIO_new() | 2025-07-08 |

