# Security Updates Monitor

*Last updated: 2025-07-25 20:16:51 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 10 |
| COMMIT | 9 |
| PR | 2 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-j63h-hmgw-x4j7](https://github.com/advisories/GHSA-j63h-hmgw-x4j7): Opencast still publishes global system account credentials  (MAVEN/org.opencastproject:opencast-publication-service-oaipmh-remote, MAVEN/org.opencastproject:opencast-kernel, MAVEN/org.opencastproject:opencast-ingest-service-impl) | MODERATE (CVSS: 6.5) | 2025-07-25 |
| GHSA | [GHSA-GHSA-9jr9-8ff3-m894](https://github.com/advisories/GHSA-9jr9-8ff3-m894): HAX CMS API Lacks Authorization Checks (COMPOSER/elmsln/haxcms, NPM/@haxtheweb/haxcms-nodejs) | HIGH (CVSS: 8.3) | 2025-07-25 |
| GHSA | [GHSA-GHSA-gq52-6phf-x2r6](https://github.com/advisories/GHSA-gq52-6phf-x2r6): tj-actions/branch-names has a Command Injection Vulnerability (ACTIONS/tj-actions/branch-names) | CRITICAL (CVSS: 9.1) | 2025-07-25 |
| GHSA | [GHSA-GHSA-4v6w-xpmh-gfgp](https://github.com/advisories/GHSA-4v6w-xpmh-gfgp): Skops may allow MethodNode to access unexpected object fields through dot notation, leading to arbitrary code execution at load time (PIP/skops) | HIGH (CVSS: 0.0) | 2025-07-25 |
| GHSA | [GHSA-GHSA-m7f4-hrc6-fwg3](https://github.com/advisories/GHSA-m7f4-hrc6-fwg3): Skops has Inconsistent Trusted Type Validation that Enables Hidden `operator` Methods Execution (PIP/skops) | HIGH (CVSS: 0.0) | 2025-07-25 |
| GHSA | [GHSA-GHSA-cmm8-gw4m-26cw](https://github.com/advisories/GHSA-cmm8-gw4m-26cw): JHipster allows privilege escalation via a modified authorities parameter (NPM/generator-jhipster) | HIGH (CVSS: 8.0) | 2025-07-25 |
| GHSA | [GHSA-GHSA-p9qm-p942-q3w5](https://github.com/advisories/GHSA-p9qm-p942-q3w5): XWiki Platform vulnerable to SQL injection through XWiki#searchDocuments API (MAVEN/org.xwiki.platform:xwiki-platform-oldcore, MAVEN/org.xwiki.platform:xwiki-platform-oldcore) | HIGH (CVSS: 0.0) | 2025-07-25 |
| GHSA | [GHSA-GHSA-m837-g268-mmv7](https://github.com/advisories/GHSA-m837-g268-mmv7): Node-SAML SAML Authentication Bypass (NPM/@node-saml/node-saml, NPM/node-saml) | CRITICAL (CVSS: 0.0) | 2025-07-25 |
| GHSA | [GHSA-GHSA-vr59-gm53-v7cq](https://github.com/advisories/GHSA-vr59-gm53-v7cq): XWiki Platform vulnerable to SQL injection through getdeleteddocuments.vm template sort parameter (MAVEN/org.xwiki.platform:xwiki-platform-distribution-war, MAVEN/org.xwiki.platform:xwiki-platform-distribution-war) | CRITICAL (CVSS: 0.0) | 2025-07-24 |
| GHSA | [GHSA-GHSA-vvpg-55p7-5h8w](https://github.com/advisories/GHSA-vvpg-55p7-5h8w): Mattermost did not properly restrict channel creation (GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost-server/v6, GO/github.com/mattermost/mattermost-server/v5) | LOW (CVSS: 3.8) | 2024-08-01 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [a4c579c](https://github.com/chromium/chromium/commit/a4c579c9a8e4e05f3b3ec012c40cb36c6ae89e11) | Make DesktopDragDropClientWin a Window observer to avoid UAF | 2025-07-25 |
| chromium/chromium | [0a31139](https://github.com/chromium/chromium/commit/0a3113975fca9105b496fb97ed95ef87fa77d687) | [cpesuggest] Add CPE prefix for third_party/brotli/README.chromium. | 2025-07-25 |
| chromium/chromium | [05ad470](https://github.com/chromium/chromium/commit/05ad470ae6440c4389d72f80b69c6f1e3d0f9010) | [cpesuggest] Add CPE prefix for third_party/android_deps/autorolled/committed/libs/com_google_protobuf_protobuf_javalite/README.chromium. | 2025-07-24 |
| chromium/chromium | [c852041](https://github.com/chromium/chromium/commit/c8520419ac179a19e85173122d7e9480dbcab7ef) | [cpesuggest] Add CPE prefix for third_party/android_deps/autorolled/committed/libs/io_grpc_grpc_stub/README.chromium. | 2025-07-24 |
| chromium/chromium | [c3c6042](https://github.com/chromium/chromium/commit/c3c6042011e50cd791e5e1523ca964b846fb7204) | [cpesuggest] Add CPE prefix for third_party/android_deps/autorolled/committed/libs/io_grpc_grpc_binder/README.chromium. | 2025-07-24 |
| chromium/chromium | [e79a1c3](https://github.com/chromium/chromium/commit/e79a1c3122465ee7881e8a91d738afd4f00cf6c6) | [cpesuggest] Add CPE prefix for third_party/boringssl/README.chromium. | 2025-07-24 |
| chromium/chromium | [936680b](https://github.com/chromium/chromium/commit/936680bb96fb3bc5063c63536be06978801321e2) | [cpesuggest] Add CPE prefix for third_party/android_deps/autorolled/committed/libs/com_google_code_gson_gson/README.chromium. | 2025-07-24 |
| chromium/chromium | [60b09cc](https://github.com/chromium/chromium/commit/60b09cc7f42f7a40685357c0ea403ebdc54ebefb) | [cpesuggest] Add CPE prefix for third_party/opus/README.chromium. | 2025-07-24 |
| chromium/chromium | [00584c1](https://github.com/chromium/chromium/commit/00584c1e32e016bc53729e8a527f78fe35391b9f) | [cpesuggest] Add CPE prefix for third_party/compiler-rt/README.chromium. | 2025-07-24 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28059](https://github.com/openssl/openssl/pull/28059) | Add array memory allocation routines | 2025-07-25 |
| openssl/openssl | [#28095](https://github.com/openssl/openssl/pull/28095) | crypto: evp: fix potential null pointer dereference in EVP_DigestSign in m_sigver.c | 2025-07-25 |

