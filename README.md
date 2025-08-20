# Security Updates Monitor

*Last updated: 2025-08-20 03:04:54 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 11 |
| COMMIT | 3 |
| PR | 5 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-pr72-8fxw-xx22](https://github.com/advisories/GHSA-pr72-8fxw-xx22): Default Credentials in nginx-defender Configuration Files (GO/github.com/Anipaleja/nginx-defender) | MODERATE (CVSS: 6.5) | 2025-08-19 |
| GHSA | [GHSA-GHSA-cwgh-r52j-xh6c](https://github.com/advisories/GHSA-cwgh-r52j-xh6c): Liferay Portal Reflected Cross-Site Scripting Vulnerability in displayType Parameter (MAVEN/com.liferay:com.liferay.expando.web) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-7mxq-h2r7-h449](https://github.com/advisories/GHSA-7mxq-h2r7-h449): Liferay Portal Email Modification Vulnerability via Calendar Portlet (MAVEN/com.liferay:com.liferay.calendar.service) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-22jp-w3cg-gvmm](https://github.com/advisories/GHSA-22jp-w3cg-gvmm): Liferay Portal has Stored Cross-Site Scripting Vulnerability via Message Boards Feature (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-35c5-67fm-cpcp](https://github.com/advisories/GHSA-35c5-67fm-cpcp): WP Crontrol Authenticated (Administrator+) plugin vulnerable to Blind Server-Side Request Forgery (COMPOSER/johnbillion/wp-crontrol) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-gjx4-2c7g-fm94](https://github.com/advisories/GHSA-gjx4-2c7g-fm94): screenshot-desktop vulnerable to command Injection via `format` option (NPM/screenshot-desktop) | CRITICAL (CVSS: 9.8) | 2025-08-19 |
| GHSA | [GHSA-GHSA-7rqq-prvp-x9jh](https://github.com/advisories/GHSA-7rqq-prvp-x9jh): Mermaid improperly sanitizes sequence diagram labels leading to XSS (NPM/mermaid) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-8gwm-58g9-j8pw](https://github.com/advisories/GHSA-8gwm-58g9-j8pw): Mermaid does not properly sanitize architecture diagram iconText leading to XSS (NPM/mermaid) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-3xw7-v6cj-5q8h](https://github.com/advisories/GHSA-3xw7-v6cj-5q8h): Copier's safe template has arbitrary filesystem read/write access (PIP/copier) | HIGH (CVSS: 0.0) | 2025-08-18 |
| GHSA | [GHSA-GHSA-p7q8-grrj-3m8w](https://github.com/advisories/GHSA-p7q8-grrj-3m8w): Copier's safe template has filesystem write access outside destination path (PIP/copier) | MODERATE (CVSS: 0.0) | 2025-08-18 |
| GHSA | [GHSA-GHSA-v6cf-mv9h-c8mc](https://github.com/advisories/GHSA-v6cf-mv9h-c8mc): Bouncy Castle for Java Uncontrolled Resource Consumption Vulnerability (MAVEN/org.bouncycastle:bc-fips) | LOW (CVSS: 0.0) | 2025-08-16 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [490ef25](https://github.com/chromium/chromium/commit/490ef25b449c5c0f8ff07bcc73ef88e6d3ae23e2) | [Fix] Use WeakPtr in NavigationWaiter to prevent crash | 2025-08-19 |
| openssl/openssl | [257ac12](https://github.com/openssl/openssl/commit/257ac1279877f05a997c76f58fc0c7af08e02718) | test/stack_test.c: check sk_sint_push result in test_int_stack | 2025-08-12 |
| openssl/openssl | [2b76895](https://github.com/openssl/openssl/commit/2b76895152fe7c7bcd11b9ae6e712c0437aee8c3) | test/mem_alloc_test.c: avoid referencing potentially freed old_ret | 2025-08-12 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28259](https://github.com/openssl/openssl/pull/28259) | Fix potential null pointer dereference in pkey_dh_derive | 2025-08-20 |
| openssl/openssl | [#28184](https://github.com/openssl/openssl/pull/28184) | Fix integer overflow in date_to_julian() call | 2025-08-20 |
| openssl/openssl | [#28300](https://github.com/openssl/openssl/pull/28300) | Avoid doublefree of OCSP_SINGLERESP | 2025-08-19 |
| erlang/otp | [#9790](https://github.com/erlang/otp/pull/9790) | otp scan PRs for vulnerabilities | 2025-08-19 |
| wazuh/wazuh | [#31433](https://github.com/wazuh/wazuh/pull/31433) | Fix Coverity defects in 4.13.0 RC3 | 2025-08-19 |

