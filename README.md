# Security Updates Monitor

*Last updated: 2025-07-02 10:16:30 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 20 |
| COMMIT | 3 |
| PR | 13 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-m43g-m425-p68x](https://github.com/advisories/GHSA-m43g-m425-p68x): junit-platform-reporting can leak Git credentials through its OpenTestReportGeneratingListener  (MAVEN/org.junit.platform:junit-platform-reporting) | MODERATE (CVSS: 5.8) | 2025-07-01 |
| GHSA | [GHSA-GHSA-hc55-p739-j48w](https://github.com/advisories/GHSA-hc55-p739-j48w): @modelcontextprotocol/server-filesystem vulnerability allows for path validation bypass via colliding path prefix (NPM/@modelcontextprotocol/server-filesystem, NPM/@modelcontextprotocol/server-filesystem) | HIGH (CVSS: 0.0) | 2025-07-01 |
| GHSA | [GHSA-GHSA-q66q-fx2p-7w4m](https://github.com/advisories/GHSA-q66q-fx2p-7w4m): @modelcontextprotocol/server-filesystem allows for path validation bypass via prefix matching and symlink handling (NPM/@modelcontextprotocol/server-filesystem, NPM/@modelcontextprotocol/server-filesystem) | HIGH (CVSS: 0.0) | 2025-07-01 |
| GHSA | [GHSA-GHSA-h34r-jxqm-qgpr](https://github.com/advisories/GHSA-h34r-jxqm-qgpr): juju/utils leaks private key in certs (GO/github.com/juju/utils/v4/cert) | MODERATE (CVSS: 6.5) | 2025-07-01 |
| GHSA | [GHSA-GHSA-xg8h-j46f-w952](https://github.com/advisories/GHSA-xg8h-j46f-w952): Pillow vulnerability can cause write buffer overflow on BCn encoding (PIP/pillow) | HIGH (CVSS: 7.1) | 2025-07-01 |
| GHSA | [GHSA-GHSA-3q26-f695-pp76](https://github.com/advisories/GHSA-3q26-f695-pp76): @cyanheads/git-mcp-server vulnerable to command injection in several tools (NPM/@cyanheads/git-mcp-server) | HIGH (CVSS: 7.5) | 2025-06-30 |
| GHSA | [GHSA-GHSA-5vhg-9xg4-cv9m](https://github.com/advisories/GHSA-5vhg-9xg4-cv9m): tiny-secp256k1 allows for verify() bypass when running in bundled environment (NPM/tiny-secp256k1) | HIGH (CVSS: 0.0) | 2025-06-30 |
| GHSA | [GHSA-GHSA-7mc2-6phr-23xc](https://github.com/advisories/GHSA-7mc2-6phr-23xc): tiny-secp256k1 vulnerable to private key extraction when signing a malicious JSON-stringifyable message in bundled environment (NPM/tiny-secp256k1) | HIGH (CVSS: 0.0) | 2025-06-30 |
| GHSA | [GHSA-GHSA-6r2x-8pq8-9489](https://github.com/advisories/GHSA-6r2x-8pq8-9489): Electron vulnerable to Heap Buffer Overflow in NativeImage (NPM/electron, NPM/electron, NPM/electron) | MODERATE (CVSS: 0.0) | 2025-06-30 |
| GHSA | [GHSA-GHSA-373j-mhpf-84wg](https://github.com/advisories/GHSA-373j-mhpf-84wg): Janssen Config API returns results without scope verification (MAVEN/io.jans:jans-config-api-server) | HIGH (CVSS: 0.0) | 2025-06-30 |
| GHSA | [GHSA-GHSA-xw5q-g62x-2qjc](https://github.com/advisories/GHSA-xw5q-g62x-2qjc): electron ASAR Integrity bypass by just modifying the content (NPM/electron, NPM/electron) | HIGH (CVSS: 7.8) | 2025-06-30 |
| GHSA | [GHSA-GHSA-cqm8-rg2p-jfcf](https://github.com/advisories/GHSA-cqm8-rg2p-jfcf): Infinispan CLI vulnerable to Generation of Error Message Containing Sensitive Information (MAVEN/org.infinispan:infinispan-cli-client) | MODERATE (CVSS: 6.2) | 2025-06-27 |
| GHSA | [GHSA-GHSA-65gg-3w2w-hr4h](https://github.com/advisories/GHSA-65gg-3w2w-hr4h): Podman Improper Certificate Validation; machine missing TLS verification (GO/github.com/containers/podman/v4, GO/github.com/containers/podman/v5) | HIGH (CVSS: 8.4) | 2025-06-25 |
| GHSA | [GHSA-GHSA-mjvf-4h88-6xm3](https://github.com/advisories/GHSA-mjvf-4h88-6xm3): Improper Authentication vulnerability in Apache Solr (MAVEN/org.apache.solr:solr, MAVEN/org.apache.solr:solr) | CRITICAL (CVSS: 9.8) | 2024-10-16 |
| GHSA | [GHSA-GHSA-5h6x-m52p-23ph](https://github.com/advisories/GHSA-5h6x-m52p-23ph): Withdrawn Advisory: Improper Certificate Validation in Apache Qpid Proton (MAVEN/org.apache.qpid:proton-j) | HIGH (CVSS: 7.4) | 2022-05-24 |
| GHSA | [GHSA-GHSA-gpqc-4pp7-5954](https://github.com/advisories/GHSA-gpqc-4pp7-5954): Duplicate Advisory: Authentication Bypass by CSRF Weakness (RUBYGEMS/spree_auth_devise) | CRITICAL (CVSS: 9.3) | 2021-11-18 |
| GHSA | [GHSA-GHSA-6mqr-q86q-6gwr](https://github.com/advisories/GHSA-6mqr-q86q-6gwr): Duplicate Advisory: Authentication Bypass by CSRF Weakness (RUBYGEMS/spree_auth_devise) | CRITICAL (CVSS: 9.3) | 2021-11-18 |
| GHSA | [GHSA-GHSA-8xfw-5q82-3652](https://github.com/advisories/GHSA-8xfw-5q82-3652): Duplicate Advisory: Authentication Bypass by CSRF Weakness (RUBYGEMS/spree_auth_devise) | CRITICAL (CVSS: 9.3) | 2021-11-18 |
| GHSA | [GHSA-GHSA-26xx-m4q2-xhq8](https://github.com/advisories/GHSA-26xx-m4q2-xhq8): Spree Auth Devise vulnerability allows for authentication bypass through CSRF weakness (RUBYGEMS/spree_auth_devise, RUBYGEMS/spree_auth_devise, RUBYGEMS/spree_auth_devise) | CRITICAL (CVSS: 9.3) | 2021-11-18 |
| GHSA | [GHSA-GHSA-v6w3-2prq-h95f](https://github.com/advisories/GHSA-v6w3-2prq-h95f): Improper Input Validation in Jakarta Expression Language (MAVEN/org.glassfish:javax.el, MAVEN/org.glassfish:jakarta.el, MAVEN/com.sun.el:el-ri) | MODERATE (CVSS: 5.3) | 2021-10-06 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [19d744a](https://github.com/chromium/chromium/commit/19d744a1813c9a302546d3da3147a69e3ee0a5d3) | [bedrock] Move HistoryClustersSidePanelCoordinator to | 2025-07-01 |
| chromium/chromium | [98acd5f](https://github.com/chromium/chromium/commit/98acd5f5491652ed1fa85177b74c3c81b9950da6) | Roll V8 from 08af66db4e0f to b18b99c0f050 (42 revisions) | 2025-07-01 |
| openssl/openssl | [efa2d85](https://github.com/openssl/openssl/commit/efa2d85571a50c5a697677e3568007eb0d8dcbe7) | test/quic-openssl-docker/hq-interop/quic-hq-interop.c: Add check for OPENSSL_zalloc() | 2025-06-26 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [#241](https://github.com/chromium/chromium/pull/241) | fix(deps): follow-redirects' Proxy-Authorization header kept across hosts | 2025-07-02 |
| chromium/chromium | [#253](https://github.com/chromium/chromium/pull/253) | Bump cookie and express in /tools/android/dependency_analysis/js | 2025-07-02 |
| chromium/chromium | [#254](https://github.com/chromium/chromium/pull/254) | Bump serve-static and express in /tools/android/dependency_analysis/js | 2025-07-02 |
| chromium/chromium | [#256](https://github.com/chromium/chromium/pull/256) | Bump body-parser and express in /tools/android/dependency_analysis/js | 2025-07-02 |
| chromium/chromium | [#255](https://github.com/chromium/chromium/pull/255) | Bump express from 4.18.2 to 4.21.2 in /tools/android/dependency_analysis/js | 2025-07-02 |
| chromium/chromium | [#257](https://github.com/chromium/chromium/pull/257) | Bump send and express in /tools/android/dependency_analysis/js | 2025-07-02 |
| chromium/chromium | [#158](https://github.com/chromium/chromium/pull/158) | Bump webpack from 5.75.0 to 5.76.0 in /tools/android/dependency_analysis/js | 2025-07-02 |
| chromium/chromium | [#258](https://github.com/chromium/chromium/pull/258) | Bump webpack from 5.75.0 to 5.97.1 in /tools/android/dependency_analysis/js | 2025-07-02 |
| chromium/chromium | [#259](https://github.com/chromium/chromium/pull/259) | Bump vue from 2.7.14 to 3.0.0 in /tools/android/dependency_analysis/js | 2025-07-02 |
| chromium/chromium | [#261](https://github.com/chromium/chromium/pull/261) | Bump nanoid from 3.3.4 to 3.3.8 in /tools/android/dependency_analysis/js | 2025-07-02 |
| chromium/chromium | [#264](https://github.com/chromium/chromium/pull/264) | Bump jinja2 from 2.10 to 3.1.5 in /tools/code_coverage | 2025-07-02 |
| chromium/chromium | [#267](https://github.com/chromium/chromium/pull/267) | Fix: Improve robustness and security in `AwContentsIoThreadClientImpl | 2025-07-02 |
| openssl/openssl | [#27915](https://github.com/openssl/openssl/pull/27915) | test/quic-openssl-docker/hq-interop/quic-hq-interop.c: Add check for … | 2025-07-01 |

