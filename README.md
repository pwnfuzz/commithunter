# Security Updates Monitor

*Last updated: 2025-08-29 04:17:44 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 10 |
| COMMIT | 2 |
| PR | 2 |
| ZDI | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-w48j-pp7j-fj55](https://github.com/advisories/GHSA-w48j-pp7j-fj55): Valtimo scripting engine can be used to gain access to sensitive data or resources (MAVEN/com.ritense.valtimo:core, MAVEN/com.ritense.valtimo:core) | CRITICAL (CVSS: 9.1) | 2025-08-28 |
| GHSA | [GHSA-GHSA-9m7c-m33f-3429](https://github.com/advisories/GHSA-9m7c-m33f-3429): XWiki PDF export jobs store sensitive cookies unencrypted in job statuses (MAVEN/org.xwiki.platform:xwiki-platform-export-pdf-api, MAVEN/org.xwiki.platform:xwiki-platform-export-pdf-api, MAVEN/org.xwiki.platform:xwiki-platform-export-pdf-api) | MODERATE (CVSS: 5.8) | 2025-08-28 |
| GHSA | [GHSA-GHSA-qqfq-7cpp-hcqj](https://github.com/advisories/GHSA-qqfq-7cpp-hcqj): Contao does not properly manage privileges for page and article fields (COMPOSER/contao/contao, COMPOSER/contao/contao, COMPOSER/contao/core-bundle) | MODERATE (CVSS: 4.3) | 2025-08-28 |
| GHSA | [GHSA-GHSA-7m47-r75r-cx8v](https://github.com/advisories/GHSA-7m47-r75r-cx8v): Contao applies improper access control in the back end voters (COMPOSER/contao/contao, COMPOSER/contao/contao, COMPOSER/contao/core-bundle) | MODERATE (CVSS: 4.3) | 2025-08-28 |
| GHSA | [GHSA-GHSA-w53m-gxvg-vx7p](https://github.com/advisories/GHSA-w53m-gxvg-vx7p): Contao can disclose sensitive information in the news module (COMPOSER/contao/contao, COMPOSER/contao/contao, COMPOSER/contao/core-bundle) | MODERATE (CVSS: 5.3) | 2025-08-28 |
| GHSA | [GHSA-GHSA-2xmj-8wmq-7475](https://github.com/advisories/GHSA-2xmj-8wmq-7475): Contao discloses sensitive information in the front end search index (COMPOSER/contao/contao, COMPOSER/contao/contao, COMPOSER/contao/core-bundle) | MODERATE (CVSS: 5.3) | 2025-08-28 |
| GHSA | [GHSA-GHSA-4fxf-xgrm-8fcj](https://github.com/advisories/GHSA-4fxf-xgrm-8fcj): FormCms avatar upload feature has a stored cross-site scripting (XSS) vulnerability (NUGET/FormCMS) | MODERATE (CVSS: 0.0) | 2025-08-28 |
| GHSA | [GHSA-GHSA-vxg3-w9rv-rhr2](https://github.com/advisories/GHSA-vxg3-w9rv-rhr2): Contrast leaks workload secrets to logs on INFO level (GO/github.com/edgelesssys/contrast) | HIGH (CVSS: 7.3) | 2025-08-28 |
| GHSA | [GHSA-GHSA-65rg-554r-9j5x](https://github.com/advisories/GHSA-65rg-554r-9j5x): lychee link checking action affected by arbitrary code injection in composite action (ACTIONS/lycheeverse/lychee-action) | MODERATE (CVSS: 0.0) | 2025-08-28 |
| GHSA | [GHSA-GHSA-6qr6-x7jm-x2q6](https://github.com/advisories/GHSA-6qr6-x7jm-x2q6): Improper Limitation of a Pathname to a Restricted Directory in Apache Tomcat (MAVEN/org.apache.tomcat:tomcat, MAVEN/org.apache.tomcat:tomcat, MAVEN/org.apache.tomcat:tomcat) | MODERATE (CVSS: 4.3) | 2022-05-14 |

## ZDI Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| ZDI | [ZDI-25-873: ZDI-25-873: Linux Kernel perf Subsystem AUX Buffers Use-After-Free Local Privilege Escalation Vulnerability](http://www.zerodayinitiative.com/advisories/ZDI-25-873/) | - | 2025-08-28 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [bce7492](https://github.com/chromium/chromium/commit/bce7492c0e8c0d16db6aa98146ac64190e754465) | ios: Enable PartitionAlloc BackupRefPtr by default on iOS | 2025-08-28 |
| langflow-ai/langflow | [59d64f0](https://github.com/langflow-ai/langflow/commit/59d64f0cf513591a1edb1f06eac29fdc122c8204) | docs: CVE advisory and patch release 1.5.1 (#9584) | 2025-08-28 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28376](https://github.com/openssl/openssl/pull/28376) | make PCT on key import a transient error state not a permanent one | 2025-08-29 |
| openssl/openssl | [#6017](https://github.com/openssl/openssl/pull/6017) | Fix fibre stack to prevent memory corruption if stack overflows. | 2025-08-28 |

