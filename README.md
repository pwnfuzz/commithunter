# Security Updates Monitor

*Last updated: 2025-08-19 19:11:14 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 10 |
| COMMIT | 3 |
| PR | 5 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-3xw7-v6cj-5q8h](https://github.com/advisories/GHSA-3xw7-v6cj-5q8h): Copier's safe template has arbitrary filesystem read/write access (PIP/copier) | HIGH (CVSS: 0.0) | 2025-08-18 |
| GHSA | [GHSA-GHSA-p7q8-grrj-3m8w](https://github.com/advisories/GHSA-p7q8-grrj-3m8w): Copier's safe template has filesystem write access outside destination path (PIP/copier) | MODERATE (CVSS: 0.0) | 2025-08-18 |
| GHSA | [GHSA-GHSA-mgh9-4mwp-fg55](https://github.com/advisories/GHSA-mgh9-4mwp-fg55): OpenFGA Authorization Bypass  (GO/github.com/openfga/openfga) | MODERATE (CVSS: 0.0) | 2025-08-18 |
| GHSA | [GHSA-GHSA-vhcr-hgc8-29qr](https://github.com/advisories/GHSA-vhcr-hgc8-29qr): Liferay Portal Vulnerable to Cross-Site Scripting  (MAVEN/com.liferay:com.liferay.layout.taglib) | LOW (CVSS: 0.0) | 2025-08-18 |
| GHSA | [GHSA-GHSA-r936-gwx5-v52f](https://github.com/advisories/GHSA-r936-gwx5-v52f): Spring Framework MVC Applications Path Traversal Vulnerability (MAVEN/org.springframework:spring-webmvc, MAVEN/org.springframework:spring-webmvc, MAVEN/org.springframework:spring-webmvc) | MODERATE (CVSS: 5.9) | 2025-08-18 |
| GHSA | [GHSA-GHSA-vxq6-8cwm-wj99](https://github.com/advisories/GHSA-vxq6-8cwm-wj99): LibreNMS allows stored XSS in Alert Template name field (COMPOSER/librenms/librenms) | MODERATE (CVSS: 5.5) | 2025-08-18 |
| GHSA | [GHSA-GHSA-fcpm-6mxq-m5vv](https://github.com/advisories/GHSA-fcpm-6mxq-m5vv): Capsule tenant owners with "patch namespace" permission can hijack system namespaces label (GO/github.com/projectcapsule/capsule) | CRITICAL (CVSS: 9.1) | 2025-08-18 |
| GHSA | [GHSA-GHSA-v6cf-mv9h-c8mc](https://github.com/advisories/GHSA-v6cf-mv9h-c8mc): Bouncy Castle for Java Uncontrolled Resource Consumption Vulnerability (MAVEN/org.bouncycastle:bc-fips) | LOW (CVSS: 0.0) | 2025-08-16 |
| GHSA | [GHSA-GHSA-2vv2-3x8x-4gv7](https://github.com/advisories/GHSA-2vv2-3x8x-4gv7): Flowise OS command remote code execution (NPM/flowise) | CRITICAL (CVSS: 9.8) | 2025-08-14 |
| GHSA | [GHSA-GHSA-fcxq-v2r3-cc8h](https://github.com/advisories/GHSA-fcxq-v2r3-cc8h): External Secrets Operator's Missing Namespace Restriction Allows Unauthorized Secret Access (GO/github.com/external-secrets/external-secrets) | HIGH (CVSS: 0.0) | 2025-08-13 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [490ef25](https://github.com/chromium/chromium/commit/490ef25b449c5c0f8ff07bcc73ef88e6d3ae23e2) | [Fix] Use WeakPtr in NavigationWaiter to prevent crash | 2025-08-19 |
| openssl/openssl | [257ac12](https://github.com/openssl/openssl/commit/257ac1279877f05a997c76f58fc0c7af08e02718) | test/stack_test.c: check sk_sint_push result in test_int_stack | 2025-08-12 |
| openssl/openssl | [2b76895](https://github.com/openssl/openssl/commit/2b76895152fe7c7bcd11b9ae6e712c0437aee8c3) | test/mem_alloc_test.c: avoid referencing potentially freed old_ret | 2025-08-12 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28300](https://github.com/openssl/openssl/pull/28300) | Avoid doublefree of OCSP_SINGLERESP | 2025-08-19 |
| openssl/openssl | [#28259](https://github.com/openssl/openssl/pull/28259) | Fix potential null pointer dereference in pkey_dh_derive | 2025-08-19 |
| erlang/otp | [#9790](https://github.com/erlang/otp/pull/9790) | otp scan PRs for vulnerabilities | 2025-08-19 |
| wazuh/wazuh | [#31433](https://github.com/wazuh/wazuh/pull/31433) | Fix Coverity defects in 4.13.0 RC3 | 2025-08-19 |
| openssl/openssl | [#28184](https://github.com/openssl/openssl/pull/28184) | Fix integer overflow in date_to_julian() call | 2025-08-18 |

