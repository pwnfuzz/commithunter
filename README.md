# Security Updates Monitor

*Last updated: 2025-07-22 18:22:11 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 18 |
| COMMIT | 1 |
| PR | 2 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-pjj3-j5j6-qj27](https://github.com/advisories/GHSA-pjj3-j5j6-qj27): HAX CMS NodeJS Application Has Improper Error Handling That Leads to Denial of Service (NPM/@haxtheweb/haxcms-nodejs) | HIGH (CVSS: 0.0) | 2025-07-21 |
| GHSA | [GHSA-GHSA-59g8-h59f-8hjp](https://github.com/advisories/GHSA-59g8-h59f-8hjp): NodeJS version of HAX CMS Has Disabled Content Security Policy That Enables Cross-Site Scripting (NPM/@haxtheweb/haxcms-nodejs) | HIGH (CVSS: 0.0) | 2025-07-21 |
| GHSA | [GHSA-GHSA-f38f-jvqj-mfg6](https://github.com/advisories/GHSA-f38f-jvqj-mfg6): NodeJS version of HAX CMS Has Insecure Default Configuration That Leads to Unauthenticated Access (NPM/@haxtheweb/haxcms-nodejs) | CRITICAL (CVSS: 0.0) | 2025-07-21 |
| GHSA | [GHSA-GHSA-xj5p-8h7g-76m7](https://github.com/advisories/GHSA-xj5p-8h7g-76m7): @translated/lara-mcp vulnerable to command injection in import_tmx tool (NPM/@translated/lara-mcp) | HIGH (CVSS: 7.5) | 2025-07-21 |
| GHSA | [GHSA-GHSA-2gxp-6r36-m97r](https://github.com/advisories/GHSA-2gxp-6r36-m97r): Cadwyn vulnerable to XSS on the docs page (PIP/cadwyn) | LOW (CVSS: 7.6) | 2025-07-21 |
| GHSA | [GHSA-GHSA-2c2j-9gv5-cj73](https://github.com/advisories/GHSA-2c2j-9gv5-cj73): Starlette has possible denial-of-service vector when parsing large files in multipart forms (PIP/starlette) | MODERATE (CVSS: 5.3) | 2025-07-21 |
| GHSA | [GHSA-GHSA-xqpg-92fq-grfg](https://github.com/advisories/GHSA-xqpg-92fq-grfg): `pyLoad` has Path Traversal Vulnerability in `json/upload` Endpoint that allows Arbitrary File Write (PIP/pyload-ng) | HIGH (CVSS: 7.5) | 2025-07-21 |
| GHSA | [GHSA-GHSA-5fpv-5qvh-7cf3](https://github.com/advisories/GHSA-5fpv-5qvh-7cf3): NodeJS version of the HAX CMS application is distributed with Default Secrets (NPM/@haxtheweb/haxcms-nodejs) | HIGH (CVSS: 7.3) | 2025-07-21 |
| GHSA | [GHSA-GHSA-xg9p-p463-3qjp](https://github.com/advisories/GHSA-xg9p-p463-3qjp): Apache Jena doesn't validate file access paths in configuration files uploaded by users with administrator access (MAVEN/org.apache.jena:jena) | HIGH (CVSS: 7.2) | 2025-07-21 |
| GHSA | [GHSA-GHSA-jq2c-m8gg-mqcm](https://github.com/advisories/GHSA-jq2c-m8gg-mqcm): Apache Jena allows users with administrator access to create databases files outside the files area of the Fuseki server (MAVEN/org.apache.jena:jena-fuseki) | MODERATE (CVSS: 4.9) | 2025-07-21 |
| GHSA | [GHSA-GHSA-353f-x4gh-cqq8](https://github.com/advisories/GHSA-353f-x4gh-cqq8): Nokogiri patches vendored libxml2 to resolve multiple CVEs (RUBYGEMS/nokogiri) | CRITICAL (CVSS: 0.0) | 2025-07-21 |
| GHSA | [GHSA-GHSA-49xw-hw94-fmv2](https://github.com/advisories/GHSA-49xw-hw94-fmv2): Dolibarr has Remote Code Execution Vulnerability (Bypass) (COMPOSER/dolibarr/dolibarr) | HIGH (CVSS: 8.8) | 2025-07-21 |
| GHSA | [GHSA-GHSA-c5qx-p38x-qf5w](https://github.com/advisories/GHSA-c5qx-p38x-qf5w): RageAgainstThePixel/setup-steamcmd leaked authentication token in job output logs (ACTIONS/RageAgainstThePixel/setup-steamcmd) | HIGH (CVSS: 0.0) | 2025-07-21 |
| GHSA | [GHSA-GHSA-mqcp-p2hv-vw6x](https://github.com/advisories/GHSA-mqcp-p2hv-vw6x): Thor can construct an unsafe shell command from library input. (RUBYGEMS/thor) | LOW (CVSS: 2.8) | 2025-07-20 |
| GHSA | [GHSA-GHSA-r67m-mf7v-qp7j](https://github.com/advisories/GHSA-r67m-mf7v-qp7j): Mattermost password hash disclosure vulnerability (GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost-server/v5, GO/github.com/mattermost/mattermost-server/v6) | MODERATE (CVSS: 4.9) | 2023-11-06 |
| GHSA | [GHSA-GHSA-jg82-xh3w-rhxx](https://github.com/advisories/GHSA-jg82-xh3w-rhxx): Synchrony deobfuscator prototype pollution vulnerability leading to arbitrary code execution (NPM/deobfuscator) | HIGH (CVSS: 7.8) | 2023-10-18 |
| GHSA | [GHSA-GHSA-c23v-vqw5-52c5](https://github.com/advisories/GHSA-c23v-vqw5-52c5): PowerJob vulnerable to Incorrect Access Control via the create user/save interface. (MAVEN/tech.powerjob:powerjob) | MODERATE (CVSS: 5.3) | 2023-04-19 |
| GHSA | [GHSA-GHSA-627p-rr78-99rj](https://github.com/advisories/GHSA-627p-rr78-99rj): GitLab auth uses full name instead of username as user ID, allowing impersonation (GO/github.com/concourse/concourse, GO/github.com/concourse/dex, GO/github.com/concourse/concourse) | HIGH (CVSS: 7.5) | 2021-12-20 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [9972b6d](https://github.com/chromium/chromium/commit/9972b6ddee575dcaab70eeec6b4062113214d1cc) | Fix use after free | 2025-07-21 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| erlang/otp | [#9946](https://github.com/erlang/otp/pull/9946) | chore(deps): update dependency microsoft/stl to v17.14 (maint) | 2025-07-21 |
| erlang/otp | [#9918](https://github.com/erlang/otp/pull/9918) | chore(deps): update dependency microsoft/stl to v17.14 (master) | 2025-07-21 |

