# Security Updates Monitor

*Last updated: 2025-09-04 16:17:43 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 19 |
| COMMIT | 1 |
| PR | 4 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-j4fw-4mhr-hc45](https://github.com/advisories/GHSA-j4fw-4mhr-hc45): Liferay Portal Vulnerable to Denial of Service in Kaleo Forms Admin (MAVEN/com.liferay:com.liferay.portal.workflow.kaleo.forms.web) | HIGH (CVSS: 0.0) | 2025-09-04 |
| GHSA | [GHSA-GHSA-c7v7-rqfm-f44j](https://github.com/advisories/GHSA-c7v7-rqfm-f44j): Vaadin Platform possible file bypass via upload validation on the server-side (MAVEN/com.vaadin:vaadin, MAVEN/com.vaadin:vaadin, MAVEN/com.vaadin:vaadin) | MODERATE (CVSS: 0.0) | 2025-09-04 |
| GHSA | [GHSA-GHSA-94g8-xv23-7656](https://github.com/advisories/GHSA-94g8-xv23-7656): Vaadin Flow Components possible file bypass via upload validation on the server-side (MAVEN/com.vaadin:vaadin-upload-flow, MAVEN/com.vaadin:vaadin-upload-flow, MAVEN/com.vaadin:vaadin-upload-flow) | MODERATE (CVSS: 0.0) | 2025-09-04 |
| GHSA | [GHSA-GHSA-9gfh-4fwj-w3rj](https://github.com/advisories/GHSA-9gfh-4fwj-w3rj): Vaadin Framework possible file bypass via upload validation on the server-side (MAVEN/com.vaadin:vaadin-server, MAVEN/com.vaadin:vaadin-server) | MODERATE (CVSS: 0.0) | 2025-09-04 |
| GHSA | [GHSA-GHSA-vxmw-7h4f-hqxh](https://github.com/advisories/GHSA-vxmw-7h4f-hqxh): PyPI publish GitHub Action vulnerable to injectable expression expansions in action steps (ACTIONS/pypa/gh-action-pypi-publish) | LOW (CVSS: 0.0) | 2025-09-04 |
| GHSA | [GHSA-GHSA-377j-wj38-4728](https://github.com/advisories/GHSA-377j-wj38-4728): Weblate has a long session expiry when verifying second factor (PIP/Weblate) | LOW (CVSS: 0.0) | 2025-09-04 |
| GHSA | [GHSA-GHSA-mw26-5g2v-hqw3](https://github.com/advisories/GHSA-mw26-5g2v-hqw3): DeepDiff Class Pollution in Delta class leading to DoS, Remote Code Execution, and more (PIP/deepdiff) | CRITICAL (CVSS: 0.0) | 2025-09-03 |
| GHSA | [GHSA-GHSA-f696-867g-2759](https://github.com/advisories/GHSA-f696-867g-2759): Jenkins OpenTelemetry Plugin missing permission check allows capturing credentials (MAVEN/io.jenkins.plugins:opentelemetry) | MODERATE (CVSS: 4.2) | 2025-09-03 |
| GHSA | [GHSA-GHSA-gm8g-fh49-qq6v](https://github.com/advisories/GHSA-gm8g-fh49-qq6v): Jenkins global-build-stats Plugin missing permission check can result in graph IDs being enumerated (MAVEN/org.jenkins-ci.plugins:global-build-stats) | MODERATE (CVSS: 4.3) | 2025-09-03 |
| GHSA | [GHSA-GHSA-g2pq-9jr7-w6gv](https://github.com/advisories/GHSA-g2pq-9jr7-w6gv): Jenkins Git client Plugin file system information disclosure vulnerability (MAVEN/org.jenkins-ci.plugins:git-client) | MODERATE (CVSS: 4.3) | 2025-09-03 |
| GHSA | [GHSA-GHSA-3ggv-qwcp-j6xg](https://github.com/advisories/GHSA-3ggv-qwcp-j6xg): Mautic Vulnerable to User Enumeration via Response Timing (COMPOSER/mautic/core, COMPOSER/mautic/core, COMPOSER/mautic/core) | MODERATE (CVSS: 5.9) | 2025-09-03 |
| GHSA | [GHSA-GHSA-9v8p-m85m-f7mm](https://github.com/advisories/GHSA-9v8p-m85m-f7mm): Mautic vulnerable to reflected XSS in lead:addLeadTags - Quick Add (COMPOSER/mautic/core, COMPOSER/mautic/core, COMPOSER/mautic/core) | MODERATE (CVSS: 0.0) | 2025-09-03 |
| GHSA | [GHSA-GHSA-438m-6mhw-hq5w](https://github.com/advisories/GHSA-438m-6mhw-hq5w): Mautic vulnerable to secret data extraction via elfinder (COMPOSER/mautic/core, COMPOSER/mautic/core, COMPOSER/mautic/core) | MODERATE (CVSS: 5.5) | 2025-09-03 |
| GHSA | [GHSA-GHSA-45qj-4xq3-3c45](https://github.com/advisories/GHSA-45qj-4xq3-3c45): mcp-markdownify-server vulnerable to command injection in pptx-to-markdown tool (NPM/mcp-markdownify-server) | HIGH (CVSS: 7.5) | 2025-09-02 |
| GHSA | [GHSA-GHSA-33pr-m977-5w97](https://github.com/advisories/GHSA-33pr-m977-5w97): Soft Serve vulnerable to arbitrary file writing through SSH API (GO/github.com/charmbracelet/soft-serve) | HIGH (CVSS: 7.7) | 2025-09-02 |
| GHSA | [GHSA-GHSA-w2wj-hw98-233h](https://github.com/advisories/GHSA-w2wj-hw98-233h): Keycloak Potential Variable Reference in Model Storage Services (MAVEN/org.keycloak:keycloak-model-storage-services) | MODERATE (CVSS: 4.9) | 2025-08-21 |
| GHSA | [GHSA-GHSA-qj5r-2r5p-phc7](https://github.com/advisories/GHSA-qj5r-2r5p-phc7): Keycloak-services SMTP Inject Vulnerability (MAVEN/org.keycloak:keycloak-services) | MODERATE (CVSS: 6.5) | 2025-08-06 |
| GHSA | [GHSA-GHSA-hxgm-ghmv-xjjm](https://github.com/advisories/GHSA-hxgm-ghmv-xjjm): Directus incorrectly handles `_in` filter (NPM/directus) | HIGH (CVSS: 6.3) | 2024-07-08 |
| GHSA | [GHSA-GHSA-f54q-j679-p9hh](https://github.com/advisories/GHSA-f54q-j679-p9hh): copyparty vulnerable to reflected cross-site scripting via k304 parameter (PIP/copyparty) | MODERATE (CVSS: 6.3) | 2023-07-25 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| erlang/otp | [ac158e5](https://github.com/erlang/otp/commit/ac158e5fd4c465c470a62018e890386b42f0b4e5) | Merge pull request #10145 from kikofernandez/add-vendor-vulnerability-analysis | 2025-09-04 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| erlang/otp | [#10165](https://github.com/erlang/otp/pull/10165) | add openvex under_investigation pcre2 detected vulnerability | 2025-09-04 |
| erlang/otp | [#10145](https://github.com/erlang/otp/pull/10145) | Verification of GH Securities included in OpenVEX statements | 2025-09-04 |
| wazuh/wazuh | [#31599](https://github.com/wazuh/wazuh/pull/31599) | Improve and fix `dpkg` algorithm in version compare | 2025-09-04 |
| langflow-ai/langflow | [#9020](https://github.com/langflow-ai/langflow/pull/9020) | Feat/OAuth Single Sign-On Implementation with Google and Microsoft AD (Entra ID) | 2025-09-04 |

