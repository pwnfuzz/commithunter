# Security Updates Monitor

*Last updated: 2025-07-30 08:21:34 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 25 |
| COMMIT | 5 |
| PR | 4 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-hfcf-79gh-f3jc](https://github.com/advisories/GHSA-hfcf-79gh-f3jc): Memos has Cross-Site Scripting (XSS) Vulnerability in Image URLs (GO/github.com/usememos/memos) | MODERATE (CVSS: 0.0) | 2025-07-29 |
| GHSA | [GHSA-GHSA-q78p-g86f-jg6q](https://github.com/advisories/GHSA-q78p-g86f-jg6q): Bugsink path traversal via event_id in ingestion (PIP/bugsink, PIP/bugsink, PIP/bugsink) | HIGH (CVSS: 0.0) | 2025-07-29 |
| GHSA | [GHSA-GHSA-w832-w3p8-cw29](https://github.com/advisories/GHSA-w832-w3p8-cw29): z-push/z-push-dev SQL Injection Vulnerability (COMPOSER/z-push/z-push-dev) | HIGH (CVSS: 9.1) | 2025-07-29 |
| GHSA | [GHSA-GHSA-4vq8-7jfc-9cvp](https://github.com/advisories/GHSA-4vq8-7jfc-9cvp): Moby firewalld reload removes bridge network isolation (GO/github.com/docker/docker) | LOW (CVSS: 3.3) | 2025-07-29 |
| GHSA | [GHSA-GHSA-x4rx-4gw3-53p4](https://github.com/advisories/GHSA-x4rx-4gw3-53p4): Moby firewalld reload makes published container ports accessible from remote hosts  (GO/github.com/docker/docker) | MODERATE (CVSS: 0.0) | 2025-07-29 |
| GHSA | [GHSA-GHSA-mrmq-3q62-6cc8](https://github.com/advisories/GHSA-mrmq-3q62-6cc8): BentoML SSRF Vulnerability in File Upload Processing   (PIP/bentoml) | CRITICAL (CVSS: 9.9) | 2025-07-29 |
| GHSA | [GHSA-GHSA-8xq3-w9fx-74rv](https://github.com/advisories/GHSA-8xq3-w9fx-74rv): webfinger.js Blind SSRF Vulnerability (NPM/webfinger.js) | MODERATE (CVSS: 0.0) | 2025-07-28 |
| GHSA | [GHSA-GHSA-rpcf-rmh6-42xr](https://github.com/advisories/GHSA-rpcf-rmh6-42xr): Netavark Has Possible DNS Resolve Confusion  (RUST/netavark) | LOW (CVSS: 3.7) | 2025-07-28 |
| GHSA | [GHSA-GHSA-m7f4-hrc6-fwg3](https://github.com/advisories/GHSA-m7f4-hrc6-fwg3): Skops has Inconsistent Trusted Type Validation that Enables Hidden `operator` Methods Execution (PIP/skops) | HIGH (CVSS: 0.0) | 2025-07-25 |
| GHSA | [GHSA-GHSA-mvw6-62qv-vmqf](https://github.com/advisories/GHSA-mvw6-62qv-vmqf): Duplicate Advisory: Koa Open Redirect via Referrer Header (User-Controlled) (NPM/koa) | LOW (CVSS: 3.5) | 2025-07-25 |
| GHSA | [GHSA-GHSA-49jm-g4m8-x53p](https://github.com/advisories/GHSA-49jm-g4m8-x53p): Withdrawn Advisory: CodeIgniter4 Cross-Site Scripting Vulnerability in debugbar_time Parameter (COMPOSER/codeigniter4/framework) | MODERATE (CVSS: 6.1) | 2025-07-25 |
| GHSA | [GHSA-GHSA-526j-mv3p-f4vv](https://github.com/advisories/GHSA-526j-mv3p-f4vv): eKuiper API endpoints handling SQL queries with user-controlled table names.  (GO/github.com/lf-edge/ekuiper, GO/github.com/lf-edge/ekuiper/v2) | HIGH (CVSS: 0.0) | 2025-07-24 |
| GHSA | [GHSA-GHSA-83j7-mhw9-388w](https://github.com/advisories/GHSA-83j7-mhw9-388w): Keycloak is vulnerable to bad actors escalating privileges through its Fine-Grained Admin Permissions (MAVEN/org.keycloak:keycloak-services) | MODERATE (CVSS: 6.5) | 2025-07-18 |
| GHSA | [GHSA-GHSA-7xqm-7738-642x](https://github.com/advisories/GHSA-7xqm-7738-642x): File Browser's Uncontrolled Memory Consumption vulnerability can enable DoS attack due to oversized file processing (GO/github.com/filebrowser/filebrowser/v2) | HIGH (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-7xwp-2cpp-p8r7](https://github.com/advisories/GHSA-7xwp-2cpp-p8r7): File Browser’s insecure JWT handling can lead to session replay attacks after logout (GO/github.com/filebrowser/filebrowser/v2, GO/github.com/filebrowser/filebrowser) | HIGH (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-56j4-446m-qrf6](https://github.com/advisories/GHSA-56j4-446m-qrf6): Babylon vulnerable to chain half when transaction has fees different than `ubbn` (GO/github.com/babylonlabs-io/babylon, GO/github.com/babylonlabs-io/babylon/v2) | HIGH (CVSS: 0.0) | 2025-06-30 |
| GHSA | [GHSA-GHSA-8f5r-8cmq-7fmq](https://github.com/advisories/GHSA-8f5r-8cmq-7fmq): OpenBao Inserts Sensitive Information into Log File when processing malformed data (GO/github.com/openbao/openbao/sdk/v2) | MODERATE (CVSS: 4.5) | 2025-06-26 |
| GHSA | [GHSA-GHSA-xh32-cx6c-cp4v](https://github.com/advisories/GHSA-xh32-cx6c-cp4v): Gogs XSS allowed by stored call in PDF renderer (GO/gogs.io/gogs, GO/github.com/gogs/gogs) | MODERATE (CVSS: 6.3) | 2025-06-26 |
| GHSA | [GHSA-GHSA-65p9-j6pg-72hj](https://github.com/advisories/GHSA-65p9-j6pg-72hj): billboard.js allows prototype pollution via the function generate (NPM/billboard.js) | CRITICAL (CVSS: 9.8) | 2025-06-04 |
| GHSA | [GHSA-GHSA-4585-28v2-8h46](https://github.com/advisories/GHSA-4585-28v2-8h46): Liferay Portal and Liferay DXP Information Disclosure Vulnerability in the Control Panel (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 4.3) | 2024-02-20 |
| GHSA | [GHSA-GHSA-qpgh-6v9w-vfv6](https://github.com/advisories/GHSA-qpgh-6v9w-vfv6): Liferay Portal and Liferay DXP Does Not Properly Restrict Membership to Child Site Based on Parent Site Options (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 5.4) | 2024-02-20 |
| GHSA | [GHSA-GHSA-3mrr-cw9q-727m](https://github.com/advisories/GHSA-3mrr-cw9q-727m): Liferay Vulnerable to Open Redirect via Adaptive Media Administration Page (MAVEN/com.liferay:com.liferay.adaptive.media.web, MAVEN/com.liferay:com.liferay.adaptive.media.web) | MODERATE (CVSS: 6.1) | 2024-02-20 |
| GHSA | [GHSA-GHSA-f3rf-cr7f-cwc4](https://github.com/advisories/GHSA-f3rf-cr7f-cwc4): Liferay Portal and Liferay DXP Vulnerable to Open Redirect in Countries Management's Edit Region Page (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 6.1) | 2024-02-20 |
| GHSA | [GHSA-GHSA-qp68-5v39-r869](https://github.com/advisories/GHSA-qp68-5v39-r869): Liferay Portal and Liferay DXP Vulnerable to XSS in the Commerce Module (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.commerce:com.liferay.commerce.address.content.web) | CRITICAL (CVSS: 9.7) | 2023-10-17 |
| GHSA | [GHSA-GHSA-hv45-r2f5-fmhj](https://github.com/advisories/GHSA-hv45-r2f5-fmhj): Liferay Portal and Liferay DXP Vulnerable to XSS in the Wiki Widget (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom) | CRITICAL (CVSS: 9.1) | 2023-10-17 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [854ff79](https://github.com/torvalds/linux/commit/854ff7923753009189a9e1f80d23ae9d407c2fb2) | Merge tag 'mmc-v6.17' of git://git.kernel.org/pub/scm/linux/kernel/git/ulfh/mmc | 2025-07-29 |
| torvalds/linux | [0ae982d](https://github.com/torvalds/linux/commit/0ae982df67760cd08affa935c0fe86c8a9311797) | Merge tag 'i2c-for-6.17-rc1' of git://git.kernel.org/pub/scm/linux/kernel/git/wsa/linux | 2025-07-29 |
| chromium/chromium | [71c9f77](https://github.com/chromium/chromium/commit/71c9f77f9d079c316eef0d86a0bc6e68e58f6b22) | Revert "Roll src/third_party/fontconfig/src/ 8f169b6a9..09ee17b85 (3 commits)" | 2025-07-29 |
| chromium/chromium | [d44fb92](https://github.com/chromium/chromium/commit/d44fb92ddf97a649de1e24eb2b216d7ccb0cb3e5) | Roll src/third_party/fontconfig/src/ 8f169b6a9..09ee17b85 (3 commits) | 2025-07-29 |
| chromium/chromium | [10556e3](https://github.com/chromium/chromium/commit/10556e396b434a59079a5fb585cfe600968df450) | Fix use-after-free in TailoredSecurityConsentedModal | 2025-07-29 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#18504](https://github.com/openssl/openssl/pull/18504) | crypto/bn: Fix a null pointer dereference | 2025-07-30 |
| roundcube/roundcubemail | [#9707](https://github.com/roundcube/roundcubemail/pull/9707) | Bump eslint from 8.57.1 to 9.15.0 | 2025-07-30 |
| roundcube/roundcubemail | [#9698](https://github.com/roundcube/roundcubemail/pull/9698) | Bump openpgp from 5.11.2 to 6.0.0 | 2025-07-30 |
| openssl/openssl | [#28095](https://github.com/openssl/openssl/pull/28095) | crypto: evp: fix potential null pointer dereference in EVP_DigestSign in m_sigver.c | 2025-07-29 |

