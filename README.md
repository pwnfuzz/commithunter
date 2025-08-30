# Security Updates Monitor

*Last updated: 2025-08-30 20:13:36 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 34 |
| COMMIT | 1 |

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
| GHSA | [GHSA-GHSA-jc7w-c686-c4v9](https://github.com/advisories/GHSA-jc7w-c686-c4v9): github.com/ulikunitz/xz leaks memory when decoding a corrupted multiple LZMA archives (GO/github.com/ulikunitz/xz) | MODERATE (CVSS: 5.3) | 2025-08-28 |
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
| chromium/chromium | [8d0428d](https://github.com/chromium/chromium/commit/8d0428d5211aff5f38e7d51c36726bbb9ab952b8) | Roll compiler-rt from 781f4e850a9e to 361e87916c9c (6 revisions) | 2025-08-30 |

