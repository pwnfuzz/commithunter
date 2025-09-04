# Security Updates Monitor

*Last updated: 2025-09-04 17:12:23 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 11 |
| COMMIT | 4 |
| PR | 2 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-x9gp-vjh6-3wv6](https://github.com/advisories/GHSA-x9gp-vjh6-3wv6): CKEditor 5 cross-site scripting (XSS) vulnerability in the clipboard package (NPM/@ckeditor/ckeditor5-clipboard, NPM/ckeditor5, NPM/@ckeditor/ckeditor5-clipboard) | LOW (CVSS: 0.0) | 2025-09-03 |
| GHSA | [GHSA-GHSA-3p8m-j85q-pgmj](https://github.com/advisories/GHSA-3p8m-j85q-pgmj): Netty's decoders vulnerable to DoS via zip bomb style attack (MAVEN/io.netty:netty-codec, MAVEN/io.netty:netty-codec-compression) | MODERATE (CVSS: 0.0) | 2025-09-03 |
| GHSA | [GHSA-GHSA-hj6f-7hp7-xg69](https://github.com/advisories/GHSA-hj6f-7hp7-xg69): Mautic vulnerable to SSRF via webhook function (COMPOSER/mautic/core, COMPOSER/mautic/core, COMPOSER/mautic/core) | LOW (CVSS: 2.7) | 2025-09-03 |
| GHSA | [GHSA-GHSA-9hp6-4448-45g2](https://github.com/advisories/GHSA-9hp6-4448-45g2): Hono's flaw in URL path parsing could cause path confusion (NPM/hono) | HIGH (CVSS: 7.5) | 2025-09-03 |
| GHSA | [GHSA-GHSA-wgq8-vr6r-mqxm](https://github.com/advisories/GHSA-wgq8-vr6r-mqxm): frost-core: refresh shares with smaller min_signers will reduce security of group (RUST/frost-core) | MODERATE (CVSS: 0.0) | 2025-09-03 |
| GHSA | [GHSA-GHSA-vmqv-hx8q-j7mg](https://github.com/advisories/GHSA-vmqv-hx8q-j7mg): Electron has ASAR Integrity Bypass via resource modification (NPM/electron, NPM/electron, NPM/electron) | MODERATE (CVSS: 6.1) | 2025-09-03 |
| GHSA | [GHSA-GHSA-rrpj-r8h7-rm7r](https://github.com/advisories/GHSA-rrpj-r8h7-rm7r): Apache DolphinScheduler Incorrect Default Permissions Vulnerability (MAVEN/org.apache.dolphinscheduler:dolphinscheduler) | LOW (CVSS: 0.0) | 2025-09-03 |
| GHSA | [GHSA-GHSA-ph6w-f82w-28w6](https://github.com/advisories/GHSA-ph6w-f82w-28w6): Claude Code Vulnerable to Arbitrary Code Execution Due to Insufficient Startup Warning (NPM/@anthropic-ai/claude-code) | HIGH (CVSS: 0.0) | 2025-09-03 |
| GHSA | [GHSA-GHSA-m63c-3rmg-r2cf](https://github.com/advisories/GHSA-m63c-3rmg-r2cf): XWiki configuration files can be accessed through jsx and sx endpoints (MAVEN/org.xwiki.platform:xwiki-platform-skin-skinx) | CRITICAL (CVSS: 0.0) | 2025-09-03 |
| GHSA | [GHSA-GHSA-qww7-89xh-x7m7](https://github.com/advisories/GHSA-qww7-89xh-x7m7): XWiki configuration files can be accessed through the webjars API (MAVEN/org.xwiki.platform:xwiki-platform-webjars-api) | CRITICAL (CVSS: 0.0) | 2025-09-03 |
| GHSA | [GHSA-GHSA-7rqq-prvp-x9jh](https://github.com/advisories/GHSA-7rqq-prvp-x9jh): Mermaid improperly sanitizes sequence diagram labels leading to XSS (NPM/mermaid, NPM/mermaid) | MODERATE (CVSS: 0.0) | 2025-08-19 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [8c4834b](https://github.com/chromium/chromium/commit/8c4834ba8b863301e20a7c1f5de4e482a0815913) | Fix potential memory corruption | 2025-09-04 |
| chromium/chromium | [541c195](https://github.com/chromium/chromium/commit/541c1958f03f5c4fcd142eda6b59b6ece12c343f) | Roll Depot Tools from 0f565fa8583d to f916887e129c (1 revision) | 2025-09-04 |
| erlang/otp | [ebc99ff](https://github.com/erlang/otp/commit/ebc99ffcd3e01d8c8aea3738b26ed2ccf1ceb22f) | Merge pull request #10165 from kikofernandez/kiko/add-possible-pcre2-vendor-vulnerability | 2025-09-04 |
| erlang/otp | [ea220cc](https://github.com/erlang/otp/commit/ea220cc25ed7ca2ae898b72ebde444e01155a8b2) | add openvex under_investigation pcre2 detected vulnerability | 2025-09-04 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| langflow-ai/langflow | [#9542](https://github.com/langflow-ai/langflow/pull/9542) | fix: superuser credential handling and AUTO_LOGIN security | 2025-09-04 |
| langflow-ai/langflow | [#9441](https://github.com/langflow-ai/langflow/pull/9441) | fix: update CORS configuration and add env vars to allow for user control | 2025-09-03 |

