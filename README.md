# Security Updates Monitor

*Last updated: 2025-07-15 18:22:27 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 30 |
| COMMIT | 5 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-29g5-m8v7-v564](https://github.com/advisories/GHSA-29g5-m8v7-v564): Measured is vulnerable to Path Traversal attacks during class initialization (RUBYGEMS/measured) | MODERATE (CVSS: 0.0) | 2025-07-15 |
| GHSA | [GHSA-GHSA-vhvx-8xgc-99wf](https://github.com/advisories/GHSA-vhvx-8xgc-99wf): DSpace is vulnerable to Path Traversal attacks when importing packages using Simple Archive Format (MAVEN/org.dspace:dspace-api, MAVEN/org.dspace:dspace-api, MAVEN/org.dspace:dspace-api) | MODERATE (CVSS: 5.2) | 2025-07-15 |
| GHSA | [GHSA-GHSA-jjwr-5cfh-7xwh](https://github.com/advisories/GHSA-jjwr-5cfh-7xwh): DSpace is vulnerable to XML External Entity injection during archive imports  (MAVEN/org.dspace:dspace-api, MAVEN/org.dspace:dspace-api, MAVEN/org.dspace:dspace-api) | MODERATE (CVSS: 6.9) | 2025-07-15 |
| GHSA | [GHSA-GHSA-8w3f-4r8f-pf53](https://github.com/advisories/GHSA-8w3f-4r8f-pf53): pyLoad vulnerable to XSS through insecure CAPTCHA  (PIP/pyload-ng) | CRITICAL (CVSS: 9.8) | 2025-07-15 |
| GHSA | [GHSA-GHSA-7cvf-pxgp-42fc](https://github.com/advisories/GHSA-7cvf-pxgp-42fc): Directus' insufficient permission checks can enable unauthenticated users to manually trigger Flows (NPM/directus) | MODERATE (CVSS: 6.5) | 2025-07-15 |
| GHSA | [GHSA-GHSA-rmjh-cf9q-pv7q](https://github.com/advisories/GHSA-rmjh-cf9q-pv7q): Directus' exact version number is exposed by the OpenAPI Spec (NPM/directus) | MODERATE (CVSS: 5.3) | 2025-07-15 |
| GHSA | [GHSA-GHSA-f24x-rm6g-3w5v](https://github.com/advisories/GHSA-f24x-rm6g-3w5v): Directus tokens are not redacted in flow logs, exposing session credentials to all admin (NPM/directus) | MODERATE (CVSS: 4.5) | 2025-07-15 |
| GHSA | [GHSA-GHSA-x3vm-88hf-gpxp](https://github.com/advisories/GHSA-x3vm-88hf-gpxp): Directus is vulnerable to sensitive data exposure as user data is not being redacted when logged (NPM/directus) | MODERATE (CVSS: 4.2) | 2025-07-15 |
| GHSA | [GHSA-GHSA-6qjf-g333-pv38](https://github.com/advisories/GHSA-6qjf-g333-pv38): Job Iteration API is vulnerable to OS Command Injection attack through its CsvEnumerator class (RUBYGEMS/job-iteration) | HIGH (CVSS: 0.0) | 2025-07-14 |
| GHSA | [GHSA-GHSA-32mf-57h2-64x9](https://github.com/advisories/GHSA-32mf-57h2-64x9): XWiki Rendering is vulnerable to RCE attacks when processing nested macros (MAVEN/org.xwiki.rendering:xwiki-rendering-transformation-macro, MAVEN/org.xwiki.rendering:xwiki-rendering-transformation-macro, MAVEN/org.xwiki.rendering:xwiki-rendering-transformation-macro) | CRITICAL (CVSS: 10.0) | 2025-07-14 |
| GHSA | [GHSA-GHSA-w3wh-g4m9-783p](https://github.com/advisories/GHSA-w3wh-g4m9-783p): XWiki Rendering is vulnerable to XSS attacks through insecure XHTML syntax (MAVEN/org.xwiki.rendering:xwiki-rendering-syntax-xhtml) | CRITICAL (CVSS: 9.1) | 2025-07-14 |
| GHSA | [GHSA-GHSA-jv7x-xhv2-p5v2](https://github.com/advisories/GHSA-jv7x-xhv2-p5v2): LaRecipe is vulnerable to Server-Side Template Injection attacks (COMPOSER/binarytorch/larecipe) | CRITICAL (CVSS: 10.0) | 2025-07-14 |
| GHSA | [GHSA-GHSA-9548-qrrj-x5pj](https://github.com/advisories/GHSA-9548-qrrj-x5pj):  AIOHTTP is vulnerable to HTTP Request/Response Smuggling through incorrect parsing of chunked trailer sections (PIP/aiohttp) | LOW (CVSS: 0.0) | 2025-07-14 |
| GHSA | [GHSA-GHSA-q28v-664f-q6wj](https://github.com/advisories/GHSA-q28v-664f-q6wj): Indico vulnerability allows attackers to bulk dump user details (PIP/indico) | MODERATE (CVSS: 0.0) | 2025-07-14 |
| GHSA | [GHSA-GHSA-44c3-38h8-9fh9](https://github.com/advisories/GHSA-44c3-38h8-9fh9): Apache Jackrabbit vulnerable to blind XXE attack due to insecure document build (MAVEN/org.apache.jackrabbit:jackrabbit-core, MAVEN/org.apache.jackrabbit:jackrabbit-core, MAVEN/org.apache.jackrabbit:jackrabbit-core) | HIGH (CVSS: 8.8) | 2025-07-14 |
| GHSA | [GHSA-GHSA-7pr5-w74r-jjj7](https://github.com/advisories/GHSA-7pr5-w74r-jjj7): Mezzanine CMS has a Stored Cross-Site Scripting (XSS) vulnerability in the displayable_links_js function (PIP/Mezzanine) | MODERATE (CVSS: 0.0) | 2025-06-17 |
| GHSA | [GHSA-GHSA-pm4j-p7pm-fpvx](https://github.com/advisories/GHSA-pm4j-p7pm-fpvx): Apache ActiveMQ Artemis Vulnerable to Insertion of Sensitive Information into Log File (MAVEN/org.apache.activemq:artemis-project) | MODERATE (CVSS: 6.5) | 2025-04-09 |
| GHSA | [GHSA-GHSA-3w85-5p9g-h334](https://github.com/advisories/GHSA-3w85-5p9g-h334): Apache ActiveMQ Artemis User Without Create Address Permissions can Modify Address Routing-Type (MAVEN/org.apache.activemq:artemis-server) | LOW (CVSS: 4.3) | 2025-04-01 |
| GHSA | [GHSA-GHSA-2xcr-p767-f3rv](https://github.com/advisories/GHSA-2xcr-p767-f3rv): Apache Druid vulnerable to Server-Side Request Forgery, Cross-site Scripting, Open Redirect (MAVEN/org.apache.druid:druid, MAVEN/org.apache.druid:druid) | MODERATE (CVSS: 5.4) | 2025-03-20 |
| GHSA | [GHSA-GHSA-8355-xj3p-hv6q](https://github.com/advisories/GHSA-8355-xj3p-hv6q): Apache Ignite: Possible RCE when deserializing incoming messages by the server node (MAVEN/org.apache.ignite:ignite-core) | CRITICAL (CVSS: 9.1) | 2025-02-14 |
| GHSA | [GHSA-GHSA-9h7f-5hc8-cj5f](https://github.com/advisories/GHSA-9h7f-5hc8-cj5f): Liferay Portal cross-site scripting (XSS) vulnerability in the Frontend Taglib module (MAVEN/com.liferay:com.liferay.frontend.taglib.clay, MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 6.1) | 2022-05-24 |
| GHSA | [GHSA-GHSA-hgjv-7wjr-qwqp](https://github.com/advisories/GHSA-hgjv-7wjr-qwqp): Liferay Portal and Liferay DXP Cross-site scripting (XSS) vulnerability in the Frontend JS module (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom) | MODERATE (CVSS: 6.1) | 2022-05-24 |
| GHSA | [GHSA-GHSA-3vww-jrmm-9vff](https://github.com/advisories/GHSA-3vww-jrmm-9vff): Liferay Portal and Liferay DXP allows arbitrary injection via the site name (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay:com.liferay.layout.seo.web) | MODERATE (CVSS: 6.1) | 2022-04-26 |
| GHSA | [GHSA-GHSA-q2rp-xfj8-r95h](https://github.com/advisories/GHSA-q2rp-xfj8-r95h): Liferay Portal and Liferay DXP allows arbitrary injection via the name of an asset category (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay:com.liferay.asset.taglib) | MODERATE (CVSS: 5.4) | 2022-04-20 |
| GHSA | [GHSA-GHSA-658f-xhv4-p978](https://github.com/advisories/GHSA-658f-xhv4-p978): Liferay Portal and Liferay DXP allows arbitrary injection via form field (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay:com.liferay.dynamic.data.mapping.form.field.type) | MODERATE (CVSS: 6.1) | 2022-04-16 |
| GHSA | [GHSA-GHSA-9536-m86r-q297](https://github.com/advisories/GHSA-9536-m86r-q297): Liferay Portal vulnerable to cross-site scripting (XSS) via the keywords parameter (MAVEN/com.liferay:com.liferay.frontend.taglib.clay) | MODERATE (CVSS: 6.1) | 2022-03-04 |
| GHSA | [GHSA-GHSA-r39x-3qq4-gxmr](https://github.com/advisories/GHSA-r39x-3qq4-gxmr): Liferay Portal and Liferay DXP vulnerable to cross-site scripting (XSS) in edit blog entry page (MAVEN/com.liferay:com.liferay.frontend.js.web, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 5.4) | 2022-03-04 |
| GHSA | [GHSA-GHSA-vw6g-gh6c-8qwp](https://github.com/advisories/GHSA-vw6g-gh6c-8qwp): Liferay Portal and Liferay DXP vulnerable to cross-site scripting (XSS) in the Gogo Shell module (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom) | MODERATE (CVSS: 5.4) | 2022-03-04 |
| GHSA | [GHSA-GHSA-3x83-whxw-pvmg](https://github.com/advisories/GHSA-3x83-whxw-pvmg): Liferay Portal and Liferay DXP vulnerable to cross-site scripting (XSS) (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay:com.liferay.layout.admin.web) | MODERATE (CVSS: 5.4) | 2022-03-04 |
| GHSA | [GHSA-GHSA-f855-2rvm-5j7h](https://github.com/advisories/GHSA-f855-2rvm-5j7h): Liferay Portal and Liferay DXP has incorrect default permissions for site members (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom) | MODERATE (CVSS: 6.5) | 2022-03-03 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [5e936ab](https://github.com/chromium/chromium/commit/5e936ab51409fc9ceba7e0863d1c175a36a9cea1) | [iOS] Fix ReaderModeJavaScriptFeatureTest heap-use-after-free failure. | 2025-07-15 |
| chromium/chromium | [451590f](https://github.com/chromium/chromium/commit/451590f266419b572b2058498877ecc357368e3e) | Fix: Add null safety to tab loading supplier | 2025-07-15 |
| chromium/chromium | [fb7843d](https://github.com/chromium/chromium/commit/fb7843d75d73d2a38ac996ce294f9433aee7c49b) | Enable graphite test for CI | 2025-07-15 |
| chromium/chromium | [4aa45ca](https://github.com/chromium/chromium/commit/4aa45caad96b2cfe2b70ebd710aa85a606b08ffe) | Roll compiler-rt from 52767bf1a36a to 7c9c0e004dbd (1 revision) | 2025-07-14 |
| chromium/chromium | [90d99dc](https://github.com/chromium/chromium/commit/90d99dcd83af2f13e0f917b5a9dc59eeee0204d0) | Fix potential UAF in MediaStreamTrackImpl | 2025-07-14 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| langflow-ai/langflow | [#9057](https://github.com/langflow-ai/langflow/pull/9057) | docs: langflow 1.5 auto-login security doc | 2025-07-15 |

