# Security Updates Monitor

*Last updated: 2025-07-16 15:16:43 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 19 |
| COMMIT | 2 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-7xqm-7738-642x](https://github.com/advisories/GHSA-7xqm-7738-642x): File Browser's Uncontrolled Memory Consumption vulnerability can enable DoS attack due to oversized file processing (GO/github.com/filebrowser/filebrowser, GO/github.com/filebrowser/filebrowser) | HIGH (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-7mcq-f592-pf7v](https://github.com/advisories/GHSA-7mcq-f592-pf7v): Slice Ring Buffer and Slice Deque contains four unique double-free vulnerabilities triggered through safe APIs (RUST/slice-ring-buffer, RUST/slice-deque) | HIGH (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-36wv-v2qp-v4g4](https://github.com/advisories/GHSA-36wv-v2qp-v4g4): Apache CXF is vulnerable to DoS attacks as entire files are read into memory and logged (MAVEN/org.apache.cxf:cxf-core, MAVEN/org.apache.cxf:cxf-core, MAVEN/org.apache.cxf:cxf-core) | MODERATE (CVSS: 5.6) | 2025-07-15 |
| GHSA | [GHSA-GHSA-xh69-987w-hrp8](https://github.com/advisories/GHSA-xh69-987w-hrp8): resolv vulnerable to DoS via insufficient DNS domain name length validation (RUBYGEMS/resolv, RUBYGEMS/resolv, RUBYGEMS/resolv) | MODERATE (CVSS: 5.3) | 2025-07-15 |
| GHSA | [GHSA-GHSA-6jx8-rcjx-vmwf](https://github.com/advisories/GHSA-6jx8-rcjx-vmwf): GitHub Kanban MCP Server vulnerable to Command Injection (NPM/@sunwood-ai-labs/github-kanban-mcp-server) | HIGH (CVSS: 0.0) | 2025-07-15 |
| GHSA | [GHSA-GHSA-rcqj-3fmp-5cqx](https://github.com/advisories/GHSA-rcqj-3fmp-5cqx): Apache Pulsar Kafka Connector Logs Sensitive Information in Application Logs (MAVEN/org.apache.pulsar:pulsar-io-kafka, MAVEN/org.apache.pulsar:pulsar-io-kafka, MAVEN/org.apache.pulsar:pulsar-io-kafka) | MODERATE (CVSS: 6.5) | 2025-04-09 |
| GHSA | [GHSA-GHSA-43mq-6xmg-29vm](https://github.com/advisories/GHSA-43mq-6xmg-29vm): Apache Struts file upload logic is flawed (MAVEN/org.apache.struts:struts2-core) | CRITICAL (CVSS: 9.8) | 2024-12-11 |
| GHSA | [GHSA-GHSA-92qf-8gh3-gwcm](https://github.com/advisories/GHSA-92qf-8gh3-gwcm): Apache Superset: Improper SQL authorisation, parse not checking for specific postgres functions (PIP/apache-superset) | LOW (CVSS: 9.8) | 2024-12-09 |
| GHSA | [GHSA-GHSA-cf3q-vg8w-mw84](https://github.com/advisories/GHSA-cf3q-vg8w-mw84): Apache StreamPipes: Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG) in Recovery Token Generation (MAVEN/org.apache.streampipes:streampipes-resource-management) | CRITICAL (CVSS: 9.1) | 2024-06-24 |
| GHSA | [GHSA-GHSA-j5gv-w838-mmcx](https://github.com/advisories/GHSA-j5gv-w838-mmcx): Liferay Portal and Liferay DXP Vulnerable to XSS via the Page Tree Menu (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay:com.liferay.layout.impl) | CRITICAL (CVSS: 9.1) | 2023-10-17 |
| GHSA | [GHSA-GHSA-49gm-5685-8fxv](https://github.com/advisories/GHSA-49gm-5685-8fxv): Liferay Portal and Liferay DXP Vulnerable to XSS via the OAuth2ProviderApplicationRedirect Class (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay:com.liferay.oauth2.provider.rest) | CRITICAL (CVSS: 9.7) | 2023-10-17 |
| GHSA | [GHSA-GHSA-r5fj-j449-vqw2](https://github.com/advisories/GHSA-r5fj-j449-vqw2): Liferay Portal and Liferay DXP Vulnerable to SQL Injection via the Fragment Module (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay:com.liferay.fragment.service) | CRITICAL (CVSS: 9.8) | 2022-11-15 |
| GHSA | [GHSA-GHSA-wffm-j7m8-93g4](https://github.com/advisories/GHSA-wffm-j7m8-93g4): Liferay Portal and Liferay DXP Vulnerable to XSS via Tag Name (MAVEN/com.liferay:com.liferay.asset.taglib) | MODERATE (CVSS: 6.1) | 2022-09-23 |
| GHSA | [GHSA-GHSA-5j86-vmpx-42pc](https://github.com/advisories/GHSA-5j86-vmpx-42pc): Liferay Portal Path Traversal Vulnerability via the Hypermedia REST APIs Module (MAVEN/com.liferay:com.liferay.headless.discovery.web) | HIGH (CVSS: 7.5) | 2022-09-23 |
| GHSA | [GHSA-GHSA-8mp9-w7gr-pvj3](https://github.com/advisories/GHSA-8mp9-w7gr-pvj3): Liferay Portal and Liferay DXP Vulnerable to XSS via the filter_ Prefix (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay:com.liferay.fragment.renderer.collection.filter.impl) | MODERATE (CVSS: 6.1) | 2022-09-23 |
| GHSA | [GHSA-GHSA-7m65-hmvg-rxpc](https://github.com/advisories/GHSA-7m65-hmvg-rxpc): Liferay Portal and Liferay DXP Vulnerable to XSS in the Site Module (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom) | MODERATE (CVSS: 5.4) | 2022-09-23 |
| GHSA | [GHSA-GHSA-w397-9p2j-6x23](https://github.com/advisories/GHSA-w397-9p2j-6x23): Liferay Portal and Liferay DXP HtmlUtil.escapeRedirect Can Be Circumvented (MAVEN/com.liferay.portal:com.liferay.util.java, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom) | MODERATE (CVSS: 6.1) | 2022-09-23 |
| GHSA | [GHSA-GHSA-ghw5-998m-vw4w](https://github.com/advisories/GHSA-ghw5-998m-vw4w): Liferay Portal and Liferay DXP fails to check origin of event messages (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay:com.liferay.remote.app.web) | MODERATE (CVSS: 5.3) | 2022-03-04 |
| GHSA | [GHSA-GHSA-ffmm-5ww2-g3q4](https://github.com/advisories/GHSA-ffmm-5ww2-g3q4): Liferay Portal and Liferay DXP cross-site scripting (XSS) vulnerability via the script console (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay:com.liferay.server.admin.web) | MODERATE (CVSS: 6.1) | 2022-03-04 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [c9ed5b6](https://github.com/chromium/chromium/commit/c9ed5b66f2369599d278280878dfd0b186c4233c) | Revert "Update video picture-in-picture window title animation" | 2025-07-16 |
| chromium/chromium | [247cd02](https://github.com/chromium/chromium/commit/247cd023ec889ccb73f505a32099cece5d6f1afb) | Update video picture-in-picture window title animation | 2025-07-15 |

