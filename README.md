# Security Updates Monitor

*Last updated: 2025-07-03 01:12:49 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 8 |
| COMMIT | 2 |
| PR | 12 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-hc55-p739-j48w](https://github.com/advisories/GHSA-hc55-p739-j48w): @modelcontextprotocol/server-filesystem vulnerability allows for path validation bypass via colliding path prefix (NPM/@modelcontextprotocol/server-filesystem, NPM/@modelcontextprotocol/server-filesystem) | HIGH (CVSS: 0.0) | 2025-07-01 |
| GHSA | [GHSA-GHSA-q66q-fx2p-7w4m](https://github.com/advisories/GHSA-q66q-fx2p-7w4m): @modelcontextprotocol/server-filesystem allows for path validation bypass via prefix matching and symlink handling (NPM/@modelcontextprotocol/server-filesystem, NPM/@modelcontextprotocol/server-filesystem) | HIGH (CVSS: 0.0) | 2025-07-01 |
| GHSA | [GHSA-GHSA-xg8h-j46f-w952](https://github.com/advisories/GHSA-xg8h-j46f-w952): Pillow vulnerability can cause write buffer overflow on BCn encoding (PIP/pillow) | HIGH (CVSS: 7.1) | 2025-07-01 |
| GHSA | [GHSA-GHSA-65gg-3w2w-hr4h](https://github.com/advisories/GHSA-65gg-3w2w-hr4h): Podman Improper Certificate Validation; machine missing TLS verification (GO/github.com/containers/podman/v4, GO/github.com/containers/podman/v5) | HIGH (CVSS: 8.4) | 2025-06-25 |
| GHSA | [GHSA-GHSA-rp38-pj7h-r8q2](https://github.com/advisories/GHSA-rp38-pj7h-r8q2): python-a2a has a path traversal in the create_workflow function (PIP/python-a2a) | MODERATE (CVSS: 5.5) | 2025-06-17 |
| GHSA | [GHSA-GHSA-fj44-h6xw-896g](https://github.com/advisories/GHSA-fj44-h6xw-896g): react-native-keys insecurely stores encryption cipher and Base64 chunks (NPM/react-native-keys) | HIGH (CVSS: 7.5) | 2025-06-09 |
| GHSA | [GHSA-GHSA-jffq-528j-mp6c](https://github.com/advisories/GHSA-jffq-528j-mp6c): Withdrawn Advisory: Improper Restriction of XML External Entity Reference in Mulesoft APIkit (MAVEN/org.mule.modules:mule-apikit-module) | CRITICAL (CVSS: 9.8) | 2022-05-24 |
| GHSA | [GHSA-GHSA-cqqj-4p63-rrmm](https://github.com/advisories/GHSA-cqqj-4p63-rrmm): HTTP Request Smuggling in Netty (MAVEN/io.netty:netty-codec-http, MAVEN/io.netty:netty, MAVEN/org.jboss.netty:netty) | CRITICAL (CVSS: 9.1) | 2020-02-21 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| postgres/postgres | [fe05430](https://github.com/postgres/postgres/commit/fe05430ace8e0b3c945cf581564458a5983a07b6) | Correctly copy the target host identification in PQcancelCreate. | 2025-07-02 |
| chromium/chromium | [f465913](https://github.com/chromium/chromium/commit/f465913b2fdd284b8598b0ec110833a6faa4e3d7) | Use a weak pointer for Content Filter observers in tests | 2025-07-02 |

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

