# Security Updates Monitor

*Last updated: 2025-08-21 09:15:27 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 23 |
| COMMIT | 2 |
| PR | 2 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-ggjm-f3g4-rwmm](https://github.com/advisories/GHSA-ggjm-f3g4-rwmm): n8n symlink traversal vulnerability in "Read/Write File" node allows access to restricted files (NPM/n8n) | MODERATE (CVSS: 6.5) | 2025-08-20 |
| GHSA | [GHSA-GHSA-mmxm-8w33-wc4h](https://github.com/advisories/GHSA-mmxm-8w33-wc4h): Eclipse Jetty affected by MadeYouReset HTTP/2 vulnerability (MAVEN/org.eclipse.jetty.http2:jetty-http2-common, MAVEN/org.eclipse.jetty.http2:jetty-http2-common, MAVEN/org.eclipse.jetty.http2:http2-common) | HIGH (CVSS: 7.5) | 2025-08-20 |
| GHSA | [GHSA-GHSA-3j63-5h8p-gf7c](https://github.com/advisories/GHSA-3j63-5h8p-gf7c): x402 SDK vulnerable in outdated versions in resource servers for builders (NPM/x402-hono, NPM/x402-express, NPM/x402-next) | HIGH (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-p9gc-59hf-x48p](https://github.com/advisories/GHSA-p9gc-59hf-x48p): Liferay Portal Vulnerable to Cross-Site Request Forgery (MAVEN/com.liferay.portal:release.portal.bom) | HIGH (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-f9qj-4c5x-cpcw](https://github.com/advisories/GHSA-f9qj-4c5x-cpcw): elysia-cors Origin Validation Error (NPM/@elysiajs/cors) | MODERATE (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-5fx5-cff6-f3fp](https://github.com/advisories/GHSA-5fx5-cff6-f3fp): Liferay Portal Unauthenticated File Access via URL (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-56qj-wp5r-mvhj](https://github.com/advisories/GHSA-56qj-wp5r-mvhj): Liferay Portal Unvalidated File Upload (MAVEN/com.liferay:com.liferay.dynamic.data.mapping.form.web) | MODERATE (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-j6p8-g3rj-ghpm](https://github.com/advisories/GHSA-j6p8-g3rj-ghpm): Liferay Portal Vulnerable to Cross-Site Scripting via assetTagNames Parameter (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-3fp2-6mwq-4q3j](https://github.com/advisories/GHSA-3fp2-6mwq-4q3j): Liferay Portal Vulnerable to Cross-Site Scripting through URLs (MAVEN/com.liferay:com.liferay.layout.type.controller.display.page) | MODERATE (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-8f93-j3fx-72f3](https://github.com/advisories/GHSA-8f93-j3fx-72f3): CRI-O has Potential High Memory Consumption from File Read (GO/github.com/cri-o/cri-o) | MODERATE (CVSS: 5.7) | 2025-08-20 |
| GHSA | [GHSA-GHSA-hf86-8x8v-h7vc](https://github.com/advisories/GHSA-hf86-8x8v-h7vc): Apache EventMesh Vulnerable to Server-Side Request Forgery in WebhookUtil.java (MAVEN/org.apache.eventmesh:eventmesh-runtime) | MODERATE (CVSS: 6.3) | 2025-08-20 |
| GHSA | [GHSA-GHSA-mv33-9f6j-pfmc](https://github.com/advisories/GHSA-mv33-9f6j-pfmc): Directus allows unauthenticated file upload and file modification due to lacking input sanitization (NPM/@directus/api, NPM/directus) | CRITICAL (CVSS: 9.3) | 2025-08-20 |
| GHSA | [GHSA-GHSA-m49p-6cjp-x2h3](https://github.com/advisories/GHSA-m49p-6cjp-x2h3): Liferay Portal Vulnerable to Cross-Site Scripting via DDM Structure Field Labels (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-8gwm-58g9-j8pw](https://github.com/advisories/GHSA-8gwm-58g9-j8pw): Mermaid does not properly sanitize architecture diagram iconText leading to XSS (NPM/mermaid) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-g4vp-4gqr-7v8c](https://github.com/advisories/GHSA-g4vp-4gqr-7v8c): Liferay Portal Enumeration Discrepancy in Calendars (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-vjwr-cqwf-6q96](https://github.com/advisories/GHSA-vjwr-cqwf-6q96): Liferay Portal Vulnerable to Cross-Site Scripting via backURL Paramter (MAVEN/com.liferay:com.liferay.journal.web) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-7q33-gwcm-r6cj](https://github.com/advisories/GHSA-7q33-gwcm-r6cj): Liferay Portal CSRF Vulnerability via Endpoint Parameter (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-rh9f-gr6q-mpc4](https://github.com/advisories/GHSA-rh9f-gr6q-mpc4): moonshine Stored Cross-Site Scripting Vulnerability in Create Admin (COMPOSER/moonshine/moonshine) | MODERATE (CVSS: 4.9) | 2025-08-19 |
| GHSA | [GHSA-GHSA-p632-58pp-c9xg](https://github.com/advisories/GHSA-p632-58pp-c9xg): moonshine Stored Cross-Site Scripting Vulnerability in Create Article (COMPOSER/moonshine/moonshine) | MODERATE (CVSS: 4.5) | 2025-08-19 |
| GHSA | [GHSA-GHSA-9g9j-3w64-3cjh](https://github.com/advisories/GHSA-9g9j-3w64-3cjh): MoonShine SQL Injection Vulnerability (COMPOSER/moonshine/moonshine) | MODERATE (CVSS: 4.9) | 2025-08-19 |
| GHSA | [GHSA-GHSA-8xfq-7f6m-mpmf](https://github.com/advisories/GHSA-8xfq-7f6m-mpmf): MoonShine Arbitrary File Upload Vulnerability (COMPOSER/moonshine/moonshine) | MODERATE (CVSS: 4.5) | 2025-08-19 |
| GHSA | [GHSA-GHSA-4gg5-vx3j-xwc7](https://github.com/advisories/GHSA-4gg5-vx3j-xwc7): Protobuf Java vulnerable to Uncontrolled Resource Consumption (MAVEN/com.google.protobuf:protobuf-java, MAVEN/com.google.protobuf:protobuf-javalite, MAVEN/com.google.protobuf:protobuf-javalite) | HIGH (CVSS: 7.5) | 2022-12-12 |
| GHSA | [GHSA-GHSA-g5ww-5jh7-63cx](https://github.com/advisories/GHSA-g5ww-5jh7-63cx): Protobuf Java vulnerable to Uncontrolled Resource Consumption (MAVEN/com.google.protobuf:protobuf-java, MAVEN/com.google.protobuf:protobuf-javalite, MAVEN/com.google.protobuf:protobuf-javalite) | HIGH (CVSS: 7.5) | 2022-12-12 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [41cd3fd](https://github.com/torvalds/linux/commit/41cd3fd152634250fdd09a52a35352b3f323800d) | Merge tag 'pci-v6.17-fixes-2' of git://git.kernel.org/pub/scm/linux/kernel/git/pci/pci | 2025-08-20 |
| openssl/openssl | [eaacf56](https://github.com/openssl/openssl/commit/eaacf56ba97e8089344bc85f8a50b00932cd3416) | Avoid doublefree of OCSP_SINGLERESP | 2025-08-19 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28300](https://github.com/openssl/openssl/pull/28300) | Avoid doublefree of OCSP_SINGLERESP | 2025-08-20 |
| openssl/openssl | [#28184](https://github.com/openssl/openssl/pull/28184) | Fix integer overflow in date_to_julian() call | 2025-08-20 |

