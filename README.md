# Security Updates Monitor

*Last updated: 2025-08-20 19:11:26 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 19 |
| COMMIT | 1 |
| PR | 3 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-8f93-j3fx-72f3](https://github.com/advisories/GHSA-8f93-j3fx-72f3): CRI-O has Potential High Memory Consumption from File Read (GO/github.com/cri-o/cri-o) | MODERATE (CVSS: 5.7) | 2025-08-20 |
| GHSA | [GHSA-GHSA-ggjm-f3g4-rwmm](https://github.com/advisories/GHSA-ggjm-f3g4-rwmm): n8n symlink traversal vulnerability in "Read/Write File" node allows access to restricted files (NPM/n8n) | MODERATE (CVSS: 6.5) | 2025-08-20 |
| GHSA | [GHSA-GHSA-hf86-8x8v-h7vc](https://github.com/advisories/GHSA-hf86-8x8v-h7vc): Apache EventMesh Vulnerable to Server-Side Request Forgery in WebhookUtil.java (MAVEN/org.apache.eventmesh:eventmesh-runtime) | MODERATE (CVSS: 6.3) | 2025-08-20 |
| GHSA | [GHSA-GHSA-mv33-9f6j-pfmc](https://github.com/advisories/GHSA-mv33-9f6j-pfmc): Directus allows unauthenticated file upload and file modification due to lacking input sanitization (NPM/@directus/api, NPM/directus) | CRITICAL (CVSS: 9.3) | 2025-08-20 |
| GHSA | [GHSA-GHSA-g4vp-4gqr-7v8c](https://github.com/advisories/GHSA-g4vp-4gqr-7v8c): Liferay Portal Enumeration Discrepancy in Calendars (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-vjwr-cqwf-6q96](https://github.com/advisories/GHSA-vjwr-cqwf-6q96): Liferay Portal Vulnerable to Cross-Site Scripting via backURL Paramter (MAVEN/com.liferay:com.liferay.journal.web) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-7q33-gwcm-r6cj](https://github.com/advisories/GHSA-7q33-gwcm-r6cj): Liferay Portal CSRF Vulnerability via Endpoint Parameter (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-rh9f-gr6q-mpc4](https://github.com/advisories/GHSA-rh9f-gr6q-mpc4): moonshine Stored Cross-Site Scripting Vulnerability in Create Admin (COMPOSER/moonshine/moonshine) | MODERATE (CVSS: 4.9) | 2025-08-19 |
| GHSA | [GHSA-GHSA-p632-58pp-c9xg](https://github.com/advisories/GHSA-p632-58pp-c9xg): moonshine Stored Cross-Site Scripting Vulnerability in Create Article (COMPOSER/moonshine/moonshine) | MODERATE (CVSS: 4.5) | 2025-08-19 |
| GHSA | [GHSA-GHSA-9g9j-3w64-3cjh](https://github.com/advisories/GHSA-9g9j-3w64-3cjh): MoonShine SQL Injection Vulnerability (COMPOSER/moonshine/moonshine) | MODERATE (CVSS: 4.9) | 2025-08-19 |
| GHSA | [GHSA-GHSA-8xfq-7f6m-mpmf](https://github.com/advisories/GHSA-8xfq-7f6m-mpmf): MoonShine Arbitrary File Upload Vulnerability (COMPOSER/moonshine/moonshine) | MODERATE (CVSS: 4.5) | 2025-08-19 |
| GHSA | [GHSA-GHSA-pr72-8fxw-xx22](https://github.com/advisories/GHSA-pr72-8fxw-xx22): Default Credentials in nginx-defender Configuration Files (GO/github.com/Anipaleja/nginx-defender) | MODERATE (CVSS: 6.5) | 2025-08-19 |
| GHSA | [GHSA-GHSA-cwgh-r52j-xh6c](https://github.com/advisories/GHSA-cwgh-r52j-xh6c): Liferay Portal Reflected Cross-Site Scripting Vulnerability in displayType Parameter (MAVEN/com.liferay:com.liferay.expando.web) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-7mxq-h2r7-h449](https://github.com/advisories/GHSA-7mxq-h2r7-h449): Liferay Portal Email Modification Vulnerability via Calendar Portlet (MAVEN/com.liferay:com.liferay.calendar.service) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-22jp-w3cg-gvmm](https://github.com/advisories/GHSA-22jp-w3cg-gvmm): Liferay Portal has Stored Cross-Site Scripting Vulnerability via Message Boards Feature (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-35c5-67fm-cpcp](https://github.com/advisories/GHSA-35c5-67fm-cpcp): WP Crontrol Authenticated (Administrator+) plugin vulnerable to Blind Server-Side Request Forgery (COMPOSER/johnbillion/wp-crontrol) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-gjx4-2c7g-fm94](https://github.com/advisories/GHSA-gjx4-2c7g-fm94): screenshot-desktop vulnerable to command Injection via `format` option (NPM/screenshot-desktop) | CRITICAL (CVSS: 9.8) | 2025-08-19 |
| GHSA | [GHSA-GHSA-7rqq-prvp-x9jh](https://github.com/advisories/GHSA-7rqq-prvp-x9jh): Mermaid improperly sanitizes sequence diagram labels leading to XSS (NPM/mermaid) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-8gwm-58g9-j8pw](https://github.com/advisories/GHSA-8gwm-58g9-j8pw): Mermaid does not properly sanitize architecture diagram iconText leading to XSS (NPM/mermaid) | MODERATE (CVSS: 0.0) | 2025-08-19 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [eaacf56](https://github.com/openssl/openssl/commit/eaacf56ba97e8089344bc85f8a50b00932cd3416) | Avoid doublefree of OCSP_SINGLERESP | 2025-08-19 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28300](https://github.com/openssl/openssl/pull/28300) | Avoid doublefree of OCSP_SINGLERESP | 2025-08-20 |
| openssl/openssl | [#28184](https://github.com/openssl/openssl/pull/28184) | Fix integer overflow in date_to_julian() call | 2025-08-20 |
| openssl/openssl | [#28259](https://github.com/openssl/openssl/pull/28259) | Fix potential null pointer dereference in pkey_dh_derive | 2025-08-20 |

