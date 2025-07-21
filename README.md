# Security Updates Monitor

*Last updated: 2025-07-21 22:15:36 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 17 |
| COMMIT | 3 |
| PR | 2 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-xqpg-92fq-grfg](https://github.com/advisories/GHSA-xqpg-92fq-grfg): `pyLoad` has Path Traversal Vulnerability in `json/upload` Endpoint that allows Arbitrary File Write (PIP/pyload-ng) | HIGH (CVSS: 7.5) | 2025-07-21 |
| GHSA | [GHSA-GHSA-5fpv-5qvh-7cf3](https://github.com/advisories/GHSA-5fpv-5qvh-7cf3): NodeJS version of the HAX CMS application is distributed with Default Secrets (NPM/@haxtheweb/haxcms-nodejs) | HIGH (CVSS: 7.3) | 2025-07-21 |
| GHSA | [GHSA-GHSA-pjj3-j5j6-qj27](https://github.com/advisories/GHSA-pjj3-j5j6-qj27): HAX CMS NodeJS Application Has Improper Error Handling That Leads to Denial of Service (NPM/@haxtheweb/haxcms-nodejs) | HIGH (CVSS: 0.0) | 2025-07-21 |
| GHSA | [GHSA-GHSA-59g8-h59f-8hjp](https://github.com/advisories/GHSA-59g8-h59f-8hjp): NodeJS version of HAX CMS Has Disabled Content Security Policy That Enables Cross-Site Scripting (NPM/@haxtheweb/haxcms-nodejs) | HIGH (CVSS: 0.0) | 2025-07-21 |
| GHSA | [GHSA-GHSA-f38f-jvqj-mfg6](https://github.com/advisories/GHSA-f38f-jvqj-mfg6): NodeJS version of HAX CMS Has Insecure Default Configuration That Leads to Unauthenticated Access (NPM/@haxtheweb/haxcms-nodejs) | CRITICAL (CVSS: 0.0) | 2025-07-21 |
| GHSA | [GHSA-GHSA-xg9p-p463-3qjp](https://github.com/advisories/GHSA-xg9p-p463-3qjp): Apache Jena doesn't validate file access paths in configuration files uploaded by users with administrator access (MAVEN/org.apache.jena:jena) | HIGH (CVSS: 7.2) | 2025-07-21 |
| GHSA | [GHSA-GHSA-jq2c-m8gg-mqcm](https://github.com/advisories/GHSA-jq2c-m8gg-mqcm): Apache Jena allows users with administrator access to create databases files outside the files area of the Fuseki server (MAVEN/org.apache.jena:jena-fuseki) | MODERATE (CVSS: 4.9) | 2025-07-21 |
| GHSA | [GHSA-GHSA-353f-x4gh-cqq8](https://github.com/advisories/GHSA-353f-x4gh-cqq8): Nokogiri patches vendored libxml2 to resolve multiple CVEs (RUBYGEMS/nokogiri) | CRITICAL (CVSS: 0.0) | 2025-07-21 |
| GHSA | [GHSA-GHSA-2c2j-9gv5-cj73](https://github.com/advisories/GHSA-2c2j-9gv5-cj73): Starlette has possible denial-of-service vector when parsing large files in multipart forms (PIP/starlette) | MODERATE (CVSS: 5.3) | 2025-07-21 |
| GHSA | [GHSA-GHSA-49xw-hw94-fmv2](https://github.com/advisories/GHSA-49xw-hw94-fmv2): Dolibarr has Remote Code Execution Vulnerability (Bypass) (COMPOSER/dolibarr/dolibarr) | HIGH (CVSS: 8.8) | 2025-07-21 |
| GHSA | [GHSA-GHSA-c5qx-p38x-qf5w](https://github.com/advisories/GHSA-c5qx-p38x-qf5w): RageAgainstThePixel/setup-steamcmd leaked authentication token in job output logs (ACTIONS/RageAgainstThePixel/setup-steamcmd) | HIGH (CVSS: 0.0) | 2025-07-21 |
| GHSA | [GHSA-GHSA-xj5p-8h7g-76m7](https://github.com/advisories/GHSA-xj5p-8h7g-76m7): @translated/lara-mcp vulnerable to command injection in import_tmx tool (NPM/@translated/lara-mcp) | HIGH (CVSS: 7.5) | 2025-07-21 |
| GHSA | [GHSA-GHSA-2gxp-6r36-m97r](https://github.com/advisories/GHSA-2gxp-6r36-m97r): Cadwyn vulnerable to XSS on the docs page (PIP/cadwyn) | LOW (CVSS: 0.0) | 2025-07-21 |
| GHSA | [GHSA-GHSA-mqcp-p2hv-vw6x](https://github.com/advisories/GHSA-mqcp-p2hv-vw6x): Thor can construct an unsafe shell command from library input. (RUBYGEMS/thor) | LOW (CVSS: 2.8) | 2025-07-20 |
| GHSA | [GHSA-GHSA-fm79-3f68-h2fc](https://github.com/advisories/GHSA-fm79-3f68-h2fc): Wasmtime CLI  is vulnerable to host panic through its fd_renumber function (RUST/wasmtime, RUST/wasmtime, RUST/wasmtime) | LOW (CVSS: 3.5) | 2025-07-18 |
| GHSA | [GHSA-GHSA-f8vw-8vgh-22r9](https://github.com/advisories/GHSA-f8vw-8vgh-22r9): XXL-JOB is vulnerable to SSRF attacks (MAVEN/com.xuxueli:xxl-job-core) | LOW (CVSS: 6.3) | 2025-07-18 |
| GHSA | [GHSA-GHSA-83j7-mhw9-388w](https://github.com/advisories/GHSA-83j7-mhw9-388w): Keycloak is vulnerable to bad actors escalating privileges through its Fine-Grained Admin Permissions (MAVEN/org.keycloak:keycloak-services) | MODERATE (CVSS: 6.5) | 2025-07-18 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [9972b6d](https://github.com/chromium/chromium/commit/9972b6ddee575dcaab70eeec6b4062113214d1cc) | Fix use after free | 2025-07-21 |
| chromium/chromium | [ad62a2e](https://github.com/chromium/chromium/commit/ad62a2e4564fd423f622a676c93f80ce26f0f473) | [bedrock] Ensure ProfileMenuViewBase bubbles do not outlive Browser | 2025-07-21 |
| chromium/chromium | [0d60e42](https://github.com/chromium/chromium/commit/0d60e4275f217ba99588c9b8f3d9490a4bdfa2da) | Roll V8 from dc15bd462b4e to 923aca0ee805 (8 revisions) | 2025-07-21 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28059](https://github.com/openssl/openssl/pull/28059) | Add array memory allocation routines | 2025-07-21 |
| openssl/openssl | [#27044](https://github.com/openssl/openssl/pull/27044) | fix potential null pointer dereference in cms_main function in apps/cms.c #26941 | 2025-07-21 |

