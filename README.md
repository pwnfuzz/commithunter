# Security Updates Monitor

*Last updated: 2025-08-30 04:16:01 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 39 |
| COMMIT | 7 |
| PR | 4 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-xwfj-jgwm-7wp5](https://github.com/advisories/GHSA-xwfj-jgwm-7wp5):  Tracing logging user input may result in poisoning logs with ANSI escape sequences (RUST/tracing-subscriber) | LOW (CVSS: 0.0) | 2025-08-29 |
| GHSA | [GHSA-GHSA-w469-hj2f-jpr5](https://github.com/advisories/GHSA-w469-hj2f-jpr5): Harness Allows Arbitrary File Write in Gitness LFS server (GO/github.com/harness/gitness, GO/github.com/harness/gitness) | HIGH (CVSS: 8.8) | 2025-08-29 |
| GHSA | [GHSA-GHSA-m54q-mm9w-fp6g](https://github.com/advisories/GHSA-m54q-mm9w-fp6g): Exiv2 has quadratic performance in ICC profile parsing in JpegBase::readMetadata (PIP/Exiv2) | LOW (CVSS: 0.0) | 2025-08-29 |
| GHSA | [GHSA-GHSA-496f-x7cq-cq39](https://github.com/advisories/GHSA-496f-x7cq-cq39): Exiv2 Segmentation Faults in Exiv2::EpsImage::writeMetadata() via crafted EPS file (PIP/Exiv2) | LOW (CVSS: 0.0) | 2025-08-29 |
| GHSA | [GHSA-GHSA-6h9x-9j5v-7w9h](https://github.com/advisories/GHSA-6h9x-9j5v-7w9h): Rancher Fleet Helm Values are stored inside BundleDeployment in plain text (GO/github.com/rancher/fleet, GO/github.com/rancher/fleet, GO/github.com/rancher/fleet) | HIGH (CVSS: 7.7) | 2025-08-29 |
| GHSA | [GHSA-GHSA-9q78-27f3-2jmh](https://github.com/advisories/GHSA-9q78-27f3-2jmh): webp crate may expose memory contents when encoding an image (RUST/webp) | MODERATE (CVSS: 0.0) | 2025-08-29 |
| GHSA | [GHSA-GHSA-82ff-hg59-8x73](https://github.com/advisories/GHSA-82ff-hg59-8x73): github.com/gorilla/csrf improperly validates TrustedOrigins allowing CSRF attacks (GO/github.com/gorilla/csrf) | MODERATE (CVSS: 0.0) | 2025-08-29 |
| GHSA | [GHSA-GHSA-9fvj-xqr2-xwg8](https://github.com/advisories/GHSA-9fvj-xqr2-xwg8): gnark affected by denial of service when computing scalar multiplication using fake-GLV algorithm (GO/github.com/consensys/gnark) | HIGH (CVSS: 7.5) | 2025-08-29 |
| GHSA | [GHSA-GHSA-26rv-h2hf-3fw4](https://github.com/advisories/GHSA-26rv-h2hf-3fw4): Payload's SQLite adapter Session Fixation vulnerability (NPM/@payloadcms/graphql, NPM/@payloadcms/next, NPM/payload) | MODERATE (CVSS: 0.0) | 2025-08-29 |
| GHSA | [GHSA-GHSA-5v66-m237-hwf7](https://github.com/advisories/GHSA-5v66-m237-hwf7): Payload does not invalidate JWTs after log out (NPM/@payloadcms/graphql, NPM/@payloadcms/next, NPM/payload) | MODERATE (CVSS: 0.0) | 2025-08-29 |
| GHSA | [GHSA-GHSA-v2ch-c8v8-fgr7](https://github.com/advisories/GHSA-v2ch-c8v8-fgr7): Versity panic induced by AWS chunked data sent to port (GO/github.com/versity/versitygw) | HIGH (CVSS: 0.0) | 2025-08-29 |
| GHSA | [GHSA-GHSA-jc7w-c686-c4v9](https://github.com/advisories/GHSA-jc7w-c686-c4v9): github.com/ulikunitz/xz leaks memory when decoding a corrupted multiple LZMA archives (GO/github.com/ulikunitz/xz) | MODERATE (CVSS: 5.3) | 2025-08-28 |
| GHSA | [GHSA-GHSA-8f82-53h8-2p34](https://github.com/advisories/GHSA-8f82-53h8-2p34): HashiCorp Vault Community Edition Denial of Service Though Complex JSON Payloads (GO/github.com/hashicorp/vault) | HIGH (CVSS: 7.5) | 2025-08-28 |
| GHSA | [GHSA-GHSA-cxm3-wv7p-598c](https://github.com/advisories/GHSA-cxm3-wv7p-598c): Malicious versions of Nx were published (NPM/@nx/workspace, NPM/@nx/js, NPM/@nx/devkit) | CRITICAL (CVSS: 0.0) | 2025-08-27 |
| GHSA | [GHSA-GHSA-27r7-3m9x-r533](https://github.com/advisories/GHSA-27r7-3m9x-r533): traQ Allows Insertion of Sensitive Information into Log File (GO/github.com/traPtitech/traQ) | MODERATE (CVSS: 5.9) | 2025-08-26 |
| GHSA | [GHSA-GHSA-rx7m-68vc-ppxh](https://github.com/advisories/GHSA-rx7m-68vc-ppxh): PhpSpreadsheet vulnerable to SSRF when reading and displaying a processed HTML document in the browser (COMPOSER/phpoffice/phpspreadsheet, COMPOSER/phpoffice/phpspreadsheet, COMPOSER/phpoffice/phpspreadsheet) | HIGH (CVSS: 0.0) | 2025-08-25 |
| GHSA | [GHSA-GHSA-95v9-hv42-pwrj](https://github.com/advisories/GHSA-95v9-hv42-pwrj): gnark is vulnerable to signature malleability in EdDSA and ECDSA due to missing scalar checks (GO/github.com/consensys/gnark) | HIGH (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-gcqf-pxgg-gw8q](https://github.com/advisories/GHSA-gcqf-pxgg-gw8q): Dpanel has an arbitrary file read vulnerability (GO/github.com/donknap/dpanel) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-h469-4fcf-p23h](https://github.com/advisories/GHSA-h469-4fcf-p23h): Mattermost has Potential Server Crash due to Unvalidated Import Data (GO/github.com/mattermost/mattermost-server/v6, GO/github.com/mattermost/mattermost-server/v5, GO/github.com/mattermost/mattermost-server) | MODERATE (CVSS: 4.9) | 2025-08-21 |
| GHSA | [GHSA-GHSA-pj6f-rc94-gw53](https://github.com/advisories/GHSA-pj6f-rc94-gw53): Mattermost Fails to Sanitize File Names (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost-server) | MODERATE (CVSS: 4.3) | 2025-08-21 |
| GHSA | [GHSA-GHSA-x67c-v8jr-p29r](https://github.com/advisories/GHSA-x67c-v8jr-p29r): Mattermost Fails to Sanitize Path Traversal Sequences (GO/github.com/mattermost/mattermost-server/v6, GO/github.com/mattermost/mattermost-server/v5, GO/github.com/mattermost/mattermost/server/v8) | MODERATE (CVSS: 6.8) | 2025-08-21 |
| GHSA | [GHSA-GHSA-q453-638c-h4mr](https://github.com/advisories/GHSA-q453-638c-h4mr): Mattermost Fails to Validate Remote Cluster Upload Sessions (GO/github.com/mattermost/mattermost-server/v6, GO/github.com/mattermost/mattermost-server/v5, GO/github.com/mattermost/mattermost/server/v8) | MODERATE (CVSS: 6.8) | 2025-08-21 |
| GHSA | [GHSA-GHSA-4276-cm8c-788h](https://github.com/advisories/GHSA-4276-cm8c-788h): Mattermost Fails to Properly Validate Team Role Modification (GO/github.com/mattermost/mattermost-server/v6, GO/github.com/mattermost/mattermost-server/v5, GO/github.com/mattermost/mattermost/server/v8) | LOW (CVSS: 3.8) | 2025-08-21 |
| GHSA | [GHSA-GHSA-pwvr-grqg-7vp2](https://github.com/advisories/GHSA-pwvr-grqg-7vp2): Mattermost Lack of Access Control Validation (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server) | LOW (CVSS: 3.5) | 2025-08-21 |
| GHSA | [GHSA-GHSA-qj47-w9f2-qg44](https://github.com/advisories/GHSA-qj47-w9f2-qg44): Mattermost Does Not Sanitize the Team Invite ID (GO/github.com/mattermost/mattermost-server/v6, GO/github.com/mattermost/mattermost-server/v5, GO/github.com/mattermost/mattermost/server/v8) | MODERATE (CVSS: 4.3) | 2025-08-21 |
| GHSA | [GHSA-GHSA-vqwh-5jhh-vc9p](https://github.com/advisories/GHSA-vqwh-5jhh-vc9p): Mattermost Server SSRF Vulnerability via the Agents Plugin (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server) | LOW (CVSS: 3.5) | 2025-08-21 |
| GHSA | [GHSA-GHSA-gq3r-5833-5532](https://github.com/advisories/GHSA-gq3r-5833-5532): Mattermost Fails to Validate File Paths (GO/github.com/mattermost/mattermost-server/v6, GO/github.com/mattermost/mattermost-server/v5, GO/github.com/mattermost/mattermost/server/v8) | MODERATE (CVSS: 6.8) | 2025-08-21 |
| GHSA | [GHSA-GHSA-2464-8j7c-4cjm](https://github.com/advisories/GHSA-2464-8j7c-4cjm): go-viper's mapstructure May Leak Sensitive Information in Logs When Processing Malformed Data (GO/github.com/go-viper/mapstructure/v2) | MODERATE (CVSS: 5.3) | 2025-08-21 |
| GHSA | [GHSA-GHSA-8f93-j3fx-72f3](https://github.com/advisories/GHSA-8f93-j3fx-72f3): CRI-O has Potential High Memory Consumption from File Read (GO/github.com/cri-o/cri-o) | MODERATE (CVSS: 5.7) | 2025-08-20 |
| GHSA | [GHSA-GHSA-pr72-8fxw-xx22](https://github.com/advisories/GHSA-pr72-8fxw-xx22): Default Credentials in nginx-defender Configuration Files (GO/github.com/Anipaleja/nginx-defender) | MODERATE (CVSS: 6.5) | 2025-08-19 |
| GHSA | [GHSA-GHSA-qp7j-x725-g67f](https://github.com/advisories/GHSA-qp7j-x725-g67f): HydrAIDE Authentication Bypass Vulnerability (GO/github.com/hydraide/hydraide, GO/github.com/hydraide/hydraide) | CRITICAL (CVSS: 10.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-mgh9-4mwp-fg55](https://github.com/advisories/GHSA-mgh9-4mwp-fg55): OpenFGA Authorization Bypass  (GO/github.com/openfga/openfga) | MODERATE (CVSS: 0.0) | 2025-08-18 |
| GHSA | [GHSA-GHSA-fcpm-6mxq-m5vv](https://github.com/advisories/GHSA-fcpm-6mxq-m5vv): Capsule tenant owners with "patch namespace" permission can hijack system namespaces label (GO/github.com/projectcapsule/capsule) | CRITICAL (CVSS: 9.1) | 2025-08-18 |
| GHSA | [GHSA-GHSA-wjrx-6529-hcj3](https://github.com/advisories/GHSA-wjrx-6529-hcj3): HashiCorp go-getter Vulnerable to Symlink Attacks (GO/github.com/hashicorp/go-getter) | HIGH (CVSS: 7.5) | 2025-08-15 |
| GHSA | [GHSA-GHSA-5j3w-5pcr-f8hg](https://github.com/advisories/GHSA-5j3w-5pcr-f8hg): Symfony UX allows unsanitized HTML attribute injection via ComponentAttributes (COMPOSER/symfony/ux-live-component, COMPOSER/symfony/ux-twig-component) | MODERATE (CVSS: 6.1) | 2025-05-19 |
| GHSA | [GHSA-GHSA-428q-q3vv-3fq3](https://github.com/advisories/GHSA-428q-q3vv-3fq3): GraphQL grant on a property might be cached with different objects (COMPOSER/api-platform/graphql, COMPOSER/api-platform/core, COMPOSER/api-platform/core) | HIGH (CVSS: 7.5) | 2025-04-04 |
| GHSA | [GHSA-GHSA-cg3c-245w-728m](https://github.com/advisories/GHSA-cg3c-245w-728m): GraphQL query operations security can be bypassed (COMPOSER/api-platform/core, COMPOSER/api-platform/graphql, COMPOSER/api-platform/core) | HIGH (CVSS: 7.5) | 2025-04-04 |
| GHSA | [GHSA-GHSA-6fx8-h7jm-663j](https://github.com/advisories/GHSA-6fx8-h7jm-663j): parse-uri Regular expression Denial of Service (ReDoS) (NPM/parseuri, NPM/parse-uri) | MODERATE (CVSS: 0.0) | 2025-01-16 |
| GHSA | [GHSA-GHSA-7mj4-2984-955f](https://github.com/advisories/GHSA-7mj4-2984-955f): Withdrawn Advisory: AlchemyCMS is vulnerable to stored XSS via the /admin/pictures image field (RUBYGEMS/alchemy_cms) | MODERATE (CVSS: 5.9) | 2022-05-14 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [fb679c8](https://github.com/torvalds/linux/commit/fb679c832b6497f19fffb8274c419783909c0912) | Merge tag 'efi-fixes-for-v6.17-1' of git://git.kernel.org/pub/scm/linux/kernel/git/efi/efi | 2025-08-29 |
| torvalds/linux | [02d6eee](https://github.com/torvalds/linux/commit/02d6eeedbc36d4b309d5518778071a749ef79c4e) | Merge tag 'hid-for-linus-2025082901' of git://git.kernel.org/pub/scm/linux/kernel/git/hid/hid | 2025-08-29 |
| postgres/postgres | [da9f9f7](https://github.com/postgres/postgres/commit/da9f9f75e5ce27a45878ffa262156d18f0046188) | Fix possible use after free in expand_partitioned_rtentry() | 2025-08-29 |
| chromium/chromium | [f65f524](https://github.com/chromium/chromium/commit/f65f524a6128bc57d1fb69e996c3ac9eb66897ef) | window management api: fix DisplayTopology null pointer exception | 2025-08-29 |
| chromium/chromium | [79d87ae](https://github.com/chromium/chromium/commit/79d87ae3a2839473ac244ec344a63b7de10bc4ae) | Fix OOB issue in DNSServerIterator | 2025-08-29 |
| chromium/chromium | [72f6aaa](https://github.com/chromium/chromium/commit/72f6aaa905cd2fe6fb41f25a0545179eb996aeeb) | Fix UAF in LoginStateChecker and related browser tests | 2025-08-29 |
| openssl/openssl | [a8d02c5](https://github.com/openssl/openssl/commit/a8d02c5ca706384c53c941b3041c326c62a6f09e) | crypto/bio/bio_print.c: avoid integer overflow when reading width/precision | 2025-08-05 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28379](https://github.com/openssl/openssl/pull/28379) | Avoid signed integer overflow in RAND_load_file | 2025-08-29 |
| openssl/openssl | [#22285](https://github.com/openssl/openssl/pull/22285) | PKCS7/CMS: fix doc on signer/chain certs | 2025-08-29 |
| wazuh/wazuh | [#31571](https://github.com/wazuh/wazuh/pull/31571) | Refactor add support for Amazon Inspector v2 | 2025-08-29 |
| wazuh/wazuh | [#31599](https://github.com/wazuh/wazuh/pull/31599) | Improve and fix `dpkg` algorithm in version compare | 2025-08-29 |

