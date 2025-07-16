# Security Updates Monitor

*Last updated: 2025-07-16 18:21:42 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 11 |
| COMMIT | 3 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-7xwp-2cpp-p8r7](https://github.com/advisories/GHSA-7xwp-2cpp-p8r7): File Browser’s insecure JWT handling can lead to session replay attacks after logout (GO/github.com/filebrowser/filebrowser) | HIGH (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-6qjf-g333-pv38](https://github.com/advisories/GHSA-6qjf-g333-pv38): Job Iteration API is vulnerable to OS Command Injection attack through its CsvEnumerator class (RUBYGEMS/job-iteration) | HIGH (CVSS: 0.0) | 2025-07-14 |
| GHSA | [GHSA-GHSA-f43m-hhj4-q3jg](https://github.com/advisories/GHSA-f43m-hhj4-q3jg): Liferay Portal and Liferay DXP Includes LDAP Credentials in the Page URL (MAVEN/com.liferay:com.liferay.portal.settings.authentication.ldap.web, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom) | MODERATE (CVSS: 5.9) | 2022-11-15 |
| GHSA | [GHSA-GHSA-hw56-7xj4-7gx6](https://github.com/advisories/GHSA-hw56-7xj4-7gx6): Liferay Portal and Liferay DXP Vulnerable to SQL Injection via Friendly URL Module (MAVEN/com.liferay:com.liferay.friendly.url.service, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.portal.bom) | CRITICAL (CVSS: 9.8) | 2022-11-15 |
| GHSA | [GHSA-GHSA-r32w-v775-5952](https://github.com/advisories/GHSA-r32w-v775-5952): Liferay Portal and Liferay DXP Vulnerable to XSS via the Document Library Module (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay:com.liferay.document.library.web) | MODERATE (CVSS: 6.1) | 2022-10-19 |
| GHSA | [GHSA-GHSA-cmrw-cgfc-v6x2](https://github.com/advisories/GHSA-cmrw-cgfc-v6x2): Liferay Portal and Liferay DXP Vulnerable to XSS via the Role Module (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay:com.liferay.roles.admin.web) | MODERATE (CVSS: 5.4) | 2022-10-19 |
| GHSA | [GHSA-GHSA-9427-7f65-88c8](https://github.com/advisories/GHSA-9427-7f65-88c8): Liferay Portal Insecure Default Configuration in auth.login.prompt.enabled (MAVEN/com.liferay.portal:com.liferay.portal.impl, MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 5.3) | 2022-10-07 |
| GHSA | [GHSA-GHSA-h9ww-wjg4-jvvg](https://github.com/advisories/GHSA-h9ww-wjg4-jvvg): Liferay Portal and Liferay DXP Fails to Check Permissions in Translation Module (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay:com.liferay.translation.web) | MODERATE (CVSS: 6.5) | 2022-09-23 |
| GHSA | [GHSA-GHSA-2ggw-8gmc-r2gq](https://github.com/advisories/GHSA-2ggw-8gmc-r2gq): Liferay Portal XSS vulnerability via movie parameter in the /html/portal/flash.jsp page (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 6.1) | 2022-05-14 |
| GHSA | [GHSA-GHSA-rpj9-pc39-h8j8](https://github.com/advisories/GHSA-rpj9-pc39-h8j8): Liferay Portal vulnerable to arbitrary command injection (MAVEN/com.liferay.portal:portal-service) | MODERATE (CVSS: 0.0) | 2022-05-13 |
| GHSA | [GHSA-GHSA-v588-qcp3-jv46](https://github.com/advisories/GHSA-v588-qcp3-jv46): Path Traversal in serve (NPM/serve) | HIGH (CVSS: 7.5) | 2019-03-25 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [54788bf](https://github.com/chromium/chromium/commit/54788bf20c04579648d93dfbe0deb1840fb819ca) | Fix UAF in InputInjector | 2025-07-16 |
| chromium/chromium | [5b24b0a](https://github.com/chromium/chromium/commit/5b24b0a6090a3937ed9b2b6fb975a1dd02522024) | Glic actor: Allow initially insecure HTTP URLs with navigate tool | 2025-07-15 |
| chromium/chromium | [4c51ea1](https://github.com/chromium/chromium/commit/4c51ea1e26b5738f8b57ec12ccf639cf402d2bd7) | [minizip] Fix potential OOB in unicode path extra field parsing | 2025-07-15 |

