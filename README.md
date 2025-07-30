# Security Updates Monitor

*Last updated: 2025-07-30 22:15:30 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 19 |
| COMMIT | 3 |
| PR | 4 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-cx25-xg7c-xfm5](https://github.com/advisories/GHSA-cx25-xg7c-xfm5): Apache Struts Extras Before 2 has an Improper Output Neutralization for Logs Vulnerability (MAVEN/org.apache.struts:struts-extras) | MODERATE (CVSS: 6.5) | 2025-07-30 |
| GHSA | [GHSA-GHSA-7rh7-c77v-6434](https://github.com/advisories/GHSA-7rh7-c77v-6434): OAuth2-Proxy has authentication bypass in oauth2-proxy skip_auth_routes due to Query Parameter inclusion (GO/github.com/oauth2-proxy/oauth2-proxy/v7) | CRITICAL (CVSS: 9.1) | 2025-07-30 |
| GHSA | [GHSA-GHSA-q78p-g86f-jg6q](https://github.com/advisories/GHSA-q78p-g86f-jg6q): Bugsink path traversal via event_id in ingestion (PIP/bugsink, PIP/bugsink, PIP/bugsink) | HIGH (CVSS: 0.0) | 2025-07-29 |
| GHSA | [GHSA-GHSA-4vq8-7jfc-9cvp](https://github.com/advisories/GHSA-4vq8-7jfc-9cvp): Moby firewalld reload removes bridge network isolation (GO/github.com/docker/docker) | LOW (CVSS: 3.3) | 2025-07-29 |
| GHSA | [GHSA-GHSA-x4rx-4gw3-53p4](https://github.com/advisories/GHSA-x4rx-4gw3-53p4): Moby firewalld reload makes published container ports accessible from remote hosts  (GO/github.com/docker/docker) | MODERATE (CVSS: 0.0) | 2025-07-29 |
| GHSA | [GHSA-GHSA-mrmq-3q62-6cc8](https://github.com/advisories/GHSA-mrmq-3q62-6cc8): BentoML SSRF Vulnerability in File Upload Processing   (PIP/bentoml) | CRITICAL (CVSS: 9.9) | 2025-07-29 |
| GHSA | [GHSA-GHSA-8xq3-w9fx-74rv](https://github.com/advisories/GHSA-8xq3-w9fx-74rv): webfinger.js Blind SSRF Vulnerability (NPM/webfinger.js) | MODERATE (CVSS: 0.0) | 2025-07-28 |
| GHSA | [GHSA-GHSA-m7f4-hrc6-fwg3](https://github.com/advisories/GHSA-m7f4-hrc6-fwg3): Skops has Inconsistent Trusted Type Validation that Enables Hidden `operator` Methods Execution (PIP/skops) | HIGH (CVSS: 0.0) | 2025-07-25 |
| GHSA | [GHSA-GHSA-526j-mv3p-f4vv](https://github.com/advisories/GHSA-526j-mv3p-f4vv): eKuiper API endpoints handling SQL queries with user-controlled table names.  (GO/github.com/lf-edge/ekuiper, GO/github.com/lf-edge/ekuiper/v2) | HIGH (CVSS: 0.0) | 2025-07-24 |
| GHSA | [GHSA-GHSA-7xqm-7738-642x](https://github.com/advisories/GHSA-7xqm-7738-642x): File Browser's Uncontrolled Memory Consumption vulnerability can enable DoS attack due to oversized file processing (GO/github.com/filebrowser/filebrowser/v2) | HIGH (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-7xwp-2cpp-p8r7](https://github.com/advisories/GHSA-7xwp-2cpp-p8r7): File Browser’s insecure JWT handling can lead to session replay attacks after logout (GO/github.com/filebrowser/filebrowser/v2, GO/github.com/filebrowser/filebrowser) | HIGH (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-56j4-446m-qrf6](https://github.com/advisories/GHSA-56j4-446m-qrf6): Babylon vulnerable to chain half when transaction has fees different than `ubbn` (GO/github.com/babylonlabs-io/babylon, GO/github.com/babylonlabs-io/babylon/v2) | HIGH (CVSS: 0.0) | 2025-06-30 |
| GHSA | [GHSA-GHSA-xh32-cx6c-cp4v](https://github.com/advisories/GHSA-xh32-cx6c-cp4v): Gogs XSS allowed by stored call in PDF renderer (GO/gogs.io/gogs, GO/github.com/gogs/gogs) | MODERATE (CVSS: 6.3) | 2025-06-26 |
| GHSA | [GHSA-GHSA-65gg-3w2w-hr4h](https://github.com/advisories/GHSA-65gg-3w2w-hr4h): Podman Improper Certificate Validation; machine missing TLS verification (GO/github.com/containers/podman/v4, GO/github.com/containers/podman/v5) | HIGH (CVSS: 8.4) | 2025-06-25 |
| GHSA | [GHSA-GHSA-ggwg-cmwp-46r5](https://github.com/advisories/GHSA-ggwg-cmwp-46r5): yiisoft/yii2 Mishandles the Attaching of Behavior Defined by a `__class` Array Key (COMPOSER/yiisoft/yii2) | CRITICAL (CVSS: 9.1) | 2025-04-10 |
| GHSA | [GHSA-GHSA-f2jm-rw3h-6phg](https://github.com/advisories/GHSA-f2jm-rw3h-6phg): LangChain pickle deserialization of untrusted data (PIP/langchain-community) | HIGH (CVSS: 5.2) | 2024-09-17 |
| GHSA | [GHSA-GHSA-wj6h-64fc-37mp](https://github.com/advisories/GHSA-wj6h-64fc-37mp): Minerva timing attack on P-256 in python-ecdsa (PIP/ecdsa) | HIGH (CVSS: 7.4) | 2024-01-22 |
| GHSA | [GHSA-GHSA-6pm2-j2v8-h3cj](https://github.com/advisories/GHSA-6pm2-j2v8-h3cj): Withdrawn: Fortra GoAnywhere MFT Deserialization of Untrusted Data vulnerability affects metasploit-framework (RUBYGEMS/metasploit-framework) | HIGH (CVSS: 7.2) | 2023-02-06 |
| GHSA | [GHSA-GHSA-4x9r-j582-cgr8](https://github.com/advisories/GHSA-4x9r-j582-cgr8): Apache Spark UI can allow impersonation if ACLs enabled (PIP/pyspark, MAVEN/org.apache.spark:spark-parent_2.12, MAVEN/org.apache.spark:spark-parent_2.12) | HIGH (CVSS: 8.8) | 2022-07-19 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [9774163](https://github.com/chromium/chromium/commit/9774163885c12368e96af61346e6712e614894f3) | Roll PDFium from 864375abbcd3 to ea66420dc6fb (2 revisions) | 2025-07-30 |
| chromium/chromium | [71c9f77](https://github.com/chromium/chromium/commit/71c9f77f9d079c316eef0d86a0bc6e68e58f6b22) | Revert "Roll src/third_party/fontconfig/src/ 8f169b6a9..09ee17b85 (3 commits)" | 2025-07-29 |
| chromium/chromium | [d44fb92](https://github.com/chromium/chromium/commit/d44fb92ddf97a649de1e24eb2b216d7ccb0cb3e5) | Roll src/third_party/fontconfig/src/ 8f169b6a9..09ee17b85 (3 commits) | 2025-07-29 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#18504](https://github.com/openssl/openssl/pull/18504) | crypto/bn: Fix a null pointer dereference | 2025-07-30 |
| roundcube/roundcubemail | [#9707](https://github.com/roundcube/roundcubemail/pull/9707) | Bump eslint from 8.57.1 to 9.15.0 | 2025-07-30 |
| roundcube/roundcubemail | [#9698](https://github.com/roundcube/roundcubemail/pull/9698) | Bump openpgp from 5.11.2 to 6.0.0 | 2025-07-30 |
| openssl/openssl | [#28095](https://github.com/openssl/openssl/pull/28095) | crypto: evp: fix potential null pointer dereference in EVP_DigestSign in m_sigver.c | 2025-07-29 |

