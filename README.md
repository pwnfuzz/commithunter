# Security Updates Monitor

*Last updated: 2025-07-09 21:13:54 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 17 |
| COMMIT | 3 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-884f-p57j-f258](https://github.com/advisories/GHSA-884f-p57j-f258): Jenkins ReadyAPI Functional Testing Plugin vulnerability stores unencrypted authentication credentials (MAVEN/org.jenkins-ci.plugins:soapui-pro-functional-testing) | MODERATE (CVSS: 4.3) | 2025-07-09 |
| GHSA | [GHSA-GHSA-26x3-7jw5-7mg4](https://github.com/advisories/GHSA-26x3-7jw5-7mg4): Jenkins Statistics Gatherer Plugin does not mask AWS Secret Key (MAVEN/org.jenkins.plugins.statistics.gatherer:statistics-gatherer) | MODERATE (CVSS: 4.3) | 2025-07-09 |
| GHSA | [GHSA-GHSA-962q-84v8-hxhj](https://github.com/advisories/GHSA-962q-84v8-hxhj): Jenkins QMetry Test Management Plugin vulnerability exposes API keys (MAVEN/org.jenkins-ci.plugins:qmetry-test-management) | MODERATE (CVSS: 4.3) | 2025-07-09 |
| GHSA | [GHSA-GHSA-3c9f-c64m-h4wc](https://github.com/advisories/GHSA-3c9f-c64m-h4wc): Jenkins Statistics Gatherer Plugin vulnerability exposes AWS Secret Key (MAVEN/org.jenkins.plugins.statistics.gatherer:statistics-gatherer) | MODERATE (CVSS: 4.3) | 2025-07-09 |
| GHSA | [GHSA-GHSA-3wgg-3j4j-3f69](https://github.com/advisories/GHSA-3wgg-3j4j-3f69): Jenkins Aqua Security Scanner Plugin vulnerability exposes scanner tokens (MAVEN/org.jenkins-ci.plugins:aqua-security-scanner) | MODERATE (CVSS: 4.3) | 2025-07-09 |
| GHSA | [GHSA-GHSA-qcj2-99cg-mppf](https://github.com/advisories/GHSA-qcj2-99cg-mppf): Jenkins Git Parameter Plugin vulnerable to code injection due to inexhaustive parameter check (MAVEN/org.jenkins-ci.tools:git-parameter) | MODERATE (CVSS: 5.4) | 2025-07-09 |
| GHSA | [GHSA-GHSA-367v-5ppj-2hrx](https://github.com/advisories/GHSA-367v-5ppj-2hrx): Jenkins HTML Publisher Plugin vulnerability displays controller file system information in its logs (MAVEN/org.jenkins-ci.plugins:htmlpublisher) | MODERATE (CVSS: 4.3) | 2025-07-09 |
| GHSA | [GHSA-GHSA-9768-hprv-crj5](https://github.com/advisories/GHSA-9768-hprv-crj5): Jenkins Credentials Binding Plugin vulnerability can expose sensitive information in logger messages (MAVEN/org.jenkins-ci.plugins:credentials-binding) | MODERATE (CVSS: 4.3) | 2025-07-09 |
| GHSA | [GHSA-GHSA-gjv4-ghm7-q58q](https://github.com/advisories/GHSA-gjv4-ghm7-q58q): MCP Server Kubernetes vulnerable to command injection in several tools (NPM/mcp-server-kubernetes) | HIGH (CVSS: 7.5) | 2025-07-08 |
| GHSA | [GHSA-GHSA-7f8r-222p-6f5g](https://github.com/advisories/GHSA-7f8r-222p-6f5g): MCP Inspector proxy server lacks authentication between the Inspector client and proxy (NPM/@modelcontextprotocol/inspector) | CRITICAL (CVSS: 0.0) | 2025-06-13 |
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

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#27994](https://github.com/openssl/openssl/pull/27994) | test/evp_extra_test.c: Add check for BIO_new() | 2025-07-08 |

