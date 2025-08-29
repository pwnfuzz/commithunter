# Security Updates Monitor

*Last updated: 2025-08-29 09:15:00 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 8 |
| COMMIT | 4 |
| PR | 8 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-jc7w-c686-c4v9](https://github.com/advisories/GHSA-jc7w-c686-c4v9): github.com/ulikunitz/xz leaks memory when decoding a corrupted multiple LZMA archives (GO/github.com/ulikunitz/xz) | MODERATE (CVSS: 5.3) | 2025-08-28 |
| GHSA | [GHSA-GHSA-3rw9-wmc8-8948](https://github.com/advisories/GHSA-3rw9-wmc8-8948): Coder accepts an APIKey beyond the linked OIDC expiry if there is no refresh token (GO/github.com/coder/coder/v2) | LOW (CVSS: 0.0) | 2025-08-28 |
| GHSA | [GHSA-GHSA-xjhf-7833-3pm5](https://github.com/advisories/GHSA-xjhf-7833-3pm5): Volto affected by possible DoS by invoking specific URL by anonymous user (NPM/@plone/volto, NPM/@plone/volto, NPM/@plone/volto) | HIGH (CVSS: 7.5) | 2025-08-28 |
| GHSA | [GHSA-GHSA-8pxw-9c75-6w56](https://github.com/advisories/GHSA-8pxw-9c75-6w56): NeuVector admin account has insecure default password (GO/github.com/neuvector/neuvector) | CRITICAL (CVSS: 9.8) | 2025-08-28 |
| GHSA | [GHSA-GHSA-w54x-xfxg-4gxq](https://github.com/advisories/GHSA-w54x-xfxg-4gxq): NeuVector process with sensitive arguments lead to leakage (GO/github.com/neuvector/neuvector) | MODERATE (CVSS: 5.3) | 2025-08-28 |
| GHSA | [GHSA-GHSA-8ff6-pc43-jwv3](https://github.com/advisories/GHSA-8ff6-pc43-jwv3): NeuVector has an  insecure password storage vulnerable to rainbow attack (GO/github.com/neuvector/neuvector) | MODERATE (CVSS: 5.3) | 2025-08-28 |
| GHSA | [GHSA-GHSA-cxm3-wv7p-598c](https://github.com/advisories/GHSA-cxm3-wv7p-598c): Malicious versions of Nx were published (NPM/@nx/workspace, NPM/@nx/js, NPM/@nx/devkit) | CRITICAL (CVSS: 0.0) | 2025-08-27 |
| GHSA | [GHSA-GHSA-rh8q-vjgf-gf74](https://github.com/advisories/GHSA-rh8q-vjgf-gf74): Improper Limitation of a Pathname to a Restricted Directory in Apache Tomcat (MAVEN/org.apache.tomcat:tomcat, MAVEN/org.apache.tomcat:tomcat, MAVEN/org.apache.tomcat:tomcat) | MODERATE (CVSS: 5.3) | 2022-05-14 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [79d87ae](https://github.com/chromium/chromium/commit/79d87ae3a2839473ac244ec344a63b7de10bc4ae) | Fix OOB issue in DNSServerIterator | 2025-08-29 |
| chromium/chromium | [72f6aaa](https://github.com/chromium/chromium/commit/72f6aaa905cd2fe6fb41f25a0545179eb996aeeb) | Fix UAF in LoginStateChecker and related browser tests | 2025-08-29 |
| chromium/chromium | [237384f](https://github.com/chromium/chromium/commit/237384fc5991fdba6f1c90bf2683daedbbe44434) | Pass AttachmentDelegate to GlicInstance constructor | 2025-08-28 |
| chromium/chromium | [56e98b6](https://github.com/chromium/chromium/commit/56e98b6f2927086a6913620753e744555f505ddf) | window management api: fix DisplayTopology null pointer exception | 2025-08-28 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28379](https://github.com/openssl/openssl/pull/28379) | Avoid signed integer overflow in RAND_load_file | 2025-08-29 |
| openssl/openssl | [#22285](https://github.com/openssl/openssl/pull/22285) | PKCS7/CMS: fix doc on signer/chain certs | 2025-08-29 |
| wazuh/wazuh | [#31571](https://github.com/wazuh/wazuh/pull/31571) | Refactor add support for Amazon Inspector v2 | 2025-08-29 |
| openssl/openssl | [#11600](https://github.com/openssl/openssl/pull/11600) | WIP: Additional tests for CVE-2020-1967 | 2025-08-28 |
| wazuh/wazuh | [#31599](https://github.com/wazuh/wazuh/pull/31599) | Improve and fix `dpkg` algorithm in version compare | 2025-08-28 |
| langflow-ai/langflow | [#9584](https://github.com/langflow-ai/langflow/pull/9584) | docs: CVE advisory and patch release 1.5.1 | 2025-08-28 |
| langflow-ai/langflow | [#9474](https://github.com/langflow-ai/langflow/pull/9474) | docs: troubleshooting backlog items | 2025-08-28 |
| langflow-ai/langflow | [#9542](https://github.com/langflow-ai/langflow/pull/9542) | fix: superuser credential handling and AUTO_LOGIN security | 2025-08-28 |

