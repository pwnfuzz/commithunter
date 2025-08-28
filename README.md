# Security Updates Monitor

*Last updated: 2025-08-28 20:15:44 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 9 |
| COMMIT | 3 |
| PR | 7 |

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
| GHSA | [GHSA-GHSA-hp87-p4gw-j4gq](https://github.com/advisories/GHSA-hp87-p4gw-j4gq): gopkg.in/yaml.v3 Denial of Service (GO/gopkg.in/yaml.v3) | HIGH (CVSS: 7.5) | 2022-05-20 |
| GHSA | [GHSA-GHSA-rh8q-vjgf-gf74](https://github.com/advisories/GHSA-rh8q-vjgf-gf74): Improper Limitation of a Pathname to a Restricted Directory in Apache Tomcat (MAVEN/org.apache.tomcat:tomcat, MAVEN/org.apache.tomcat:tomcat, MAVEN/org.apache.tomcat:tomcat) | MODERATE (CVSS: 5.3) | 2022-05-14 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [56e98b6](https://github.com/chromium/chromium/commit/56e98b6f2927086a6913620753e744555f505ddf) | window management api: fix DisplayTopology null pointer exception | 2025-08-28 |
| chromium/chromium | [747e8c8](https://github.com/chromium/chromium/commit/747e8c8f36453eb7cf97a55f53a5937121365208) | Reland "[overscroll] Reapply "Store elastic_overscroll on ScrollTree."" | 2025-08-28 |
| chromium/chromium | [07c4905](https://github.com/chromium/chromium/commit/07c4905bf0336552c7d8a06d9be49cd7721f349e) | Revert "[overscroll] Reapply "Store elastic_overscroll on ScrollTree."" | 2025-08-28 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#22285](https://github.com/openssl/openssl/pull/22285) | PKCS7/CMS: fix doc on signer/chain certs | 2025-08-28 |
| openssl/openssl | [#11600](https://github.com/openssl/openssl/pull/11600) | WIP: Additional tests for CVE-2020-1967 | 2025-08-28 |
| wazuh/wazuh | [#31599](https://github.com/wazuh/wazuh/pull/31599) | Improve and fix `dpkg` algorithm in version compare | 2025-08-28 |
| wazuh/wazuh | [#31571](https://github.com/wazuh/wazuh/pull/31571) | Refactor add support for Amazon Inspector v2 | 2025-08-28 |
| langflow-ai/langflow | [#9584](https://github.com/langflow-ai/langflow/pull/9584) | docs: CVE advisory and patch release 1.5.1 | 2025-08-28 |
| langflow-ai/langflow | [#9474](https://github.com/langflow-ai/langflow/pull/9474) | docs: troubleshooting backlog items | 2025-08-28 |
| langflow-ai/langflow | [#9542](https://github.com/langflow-ai/langflow/pull/9542) | fix: superuser credential handling and AUTO_LOGIN security | 2025-08-28 |

