# Security Updates Monitor

*Last updated: 2025-07-16 16:19:52 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 13 |
| COMMIT | 3 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-7xwp-2cpp-p8r7](https://github.com/advisories/GHSA-7xwp-2cpp-p8r7): File Browser’s insecure JWT handling can lead to session replay attacks after logout (GO/github.com/filebrowser/filebrowser) | HIGH (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-29g5-m8v7-v564](https://github.com/advisories/GHSA-29g5-m8v7-v564): Measured is vulnerable to Path Traversal attacks during class initialization (RUBYGEMS/measured) | MODERATE (CVSS: 0.0) | 2025-07-15 |
| GHSA | [GHSA-GHSA-vhvx-8xgc-99wf](https://github.com/advisories/GHSA-vhvx-8xgc-99wf): DSpace is vulnerable to Path Traversal attacks when importing packages using Simple Archive Format (MAVEN/org.dspace:dspace-api, MAVEN/org.dspace:dspace-api, MAVEN/org.dspace:dspace-api) | MODERATE (CVSS: 5.2) | 2025-07-15 |
| GHSA | [GHSA-GHSA-jjwr-5cfh-7xwh](https://github.com/advisories/GHSA-jjwr-5cfh-7xwh): DSpace is vulnerable to XML External Entity injection during archive imports  (MAVEN/org.dspace:dspace-api, MAVEN/org.dspace:dspace-api, MAVEN/org.dspace:dspace-api) | MODERATE (CVSS: 6.9) | 2025-07-15 |
| GHSA | [GHSA-GHSA-6qjf-g333-pv38](https://github.com/advisories/GHSA-6qjf-g333-pv38): Job Iteration API is vulnerable to OS Command Injection attack through its CsvEnumerator class (RUBYGEMS/job-iteration) | HIGH (CVSS: 0.0) | 2025-07-14 |
| GHSA | [GHSA-GHSA-9427-7f65-88c8](https://github.com/advisories/GHSA-9427-7f65-88c8): Liferay Portal Insecure Default Configuration in auth.login.prompt.enabled (MAVEN/com.liferay.portal:com.liferay.portal.impl, MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 5.3) | 2022-10-07 |
| GHSA | [GHSA-GHSA-h9ww-wjg4-jvvg](https://github.com/advisories/GHSA-h9ww-wjg4-jvvg): Liferay Portal and Liferay DXP Fails to Check Permissions in Translation Module (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay:com.liferay.translation.web) | MODERATE (CVSS: 6.5) | 2022-09-23 |
| GHSA | [GHSA-GHSA-9h7f-5hc8-cj5f](https://github.com/advisories/GHSA-9h7f-5hc8-cj5f): Liferay Portal cross-site scripting (XSS) vulnerability in the Frontend Taglib module (MAVEN/com.liferay:com.liferay.frontend.taglib.clay, MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 6.1) | 2022-05-24 |
| GHSA | [GHSA-GHSA-2ggw-8gmc-r2gq](https://github.com/advisories/GHSA-2ggw-8gmc-r2gq): Liferay Portal XSS vulnerability via movie parameter in the /html/portal/flash.jsp page (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 6.1) | 2022-05-14 |
| GHSA | [GHSA-GHSA-rpj9-pc39-h8j8](https://github.com/advisories/GHSA-rpj9-pc39-h8j8): Liferay Portal vulnerable to arbitrary command injection (MAVEN/com.liferay.portal:portal-service) | MODERATE (CVSS: 0.0) | 2022-05-13 |
| GHSA | [GHSA-GHSA-9536-m86r-q297](https://github.com/advisories/GHSA-9536-m86r-q297): Liferay Portal vulnerable to cross-site scripting (XSS) via the keywords parameter (MAVEN/com.liferay:com.liferay.frontend.taglib.clay) | MODERATE (CVSS: 6.1) | 2022-03-04 |
| GHSA | [GHSA-GHSA-r39x-3qq4-gxmr](https://github.com/advisories/GHSA-r39x-3qq4-gxmr): Liferay Portal and Liferay DXP vulnerable to cross-site scripting (XSS) in edit blog entry page (MAVEN/com.liferay:com.liferay.frontend.js.web, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 5.4) | 2022-03-04 |
| GHSA | [GHSA-GHSA-v588-qcp3-jv46](https://github.com/advisories/GHSA-v588-qcp3-jv46): Path Traversal in serve (NPM/serve) | HIGH (CVSS: 7.5) | 2019-03-25 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [54788bf](https://github.com/chromium/chromium/commit/54788bf20c04579648d93dfbe0deb1840fb819ca) | Fix UAF in InputInjector | 2025-07-16 |
| chromium/chromium | [5b24b0a](https://github.com/chromium/chromium/commit/5b24b0a6090a3937ed9b2b6fb975a1dd02522024) | Glic actor: Allow initially insecure HTTP URLs with navigate tool | 2025-07-15 |
| chromium/chromium | [4c51ea1](https://github.com/chromium/chromium/commit/4c51ea1e26b5738f8b57ec12ccf639cf402d2bd7) | [minizip] Fix potential OOB in unicode path extra field parsing | 2025-07-15 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| langflow-ai/langflow | [#9057](https://github.com/langflow-ai/langflow/pull/9057) | docs: langflow 1.5 auto-login security doc | 2025-07-15 |

