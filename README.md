# Security Updates Monitor

*Last updated: 2025-08-22 11:12:00 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 20 |
| COMMIT | 2 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-8hmm-4crw-vm2c](https://github.com/advisories/GHSA-8hmm-4crw-vm2c): @musistudio/claude-code-router has improper CORS configuration (NPM/@musistudio/claude-code-router) | HIGH (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-pp7p-q8fx-2968](https://github.com/advisories/GHSA-pp7p-q8fx-2968): vite-plugin-static-copy files not included in `src` are possible to access with a crafted request (NPM/vite-plugin-static-copy, NPM/vite-plugin-static-copy) | MODERATE (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-287x-6r2h-f9mw](https://github.com/advisories/GHSA-287x-6r2h-f9mw): UnoPim vulnerable to CSRF on Product edit feature and creation of other types (COMPOSER/unopim/unopim) | MODERATE (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-v22v-xwh7-2vrm](https://github.com/advisories/GHSA-v22v-xwh7-2vrm): UnoPim vulnerable to remote code execution through Arbitrary File upload (COMPOSER/unopim/unopim) | HIGH (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-xr97-25v7-hc2q](https://github.com/advisories/GHSA-xr97-25v7-hc2q): UnoPim has Stored Cross-site Scripting vulnerability in user creation functionality (COMPOSER/unopim/unopim) | HIGH (CVSS: 8.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-rxc4-3w6r-4v47](https://github.com/advisories/GHSA-rxc4-3w6r-4v47): vllm API endpoints vulnerable to Denial of Service Attacks (PIP/vllm) | HIGH (CVSS: 7.5) | 2025-08-21 |
| GHSA | [GHSA-GHSA-gq3r-5833-5532](https://github.com/advisories/GHSA-gq3r-5833-5532): Mattermost Fails to Validate File Paths (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost-server) | MODERATE (CVSS: 6.8) | 2025-08-21 |
| GHSA | [GHSA-GHSA-p6rm-483j-37jf](https://github.com/advisories/GHSA-p6rm-483j-37jf): wong2 mcp-cli Command Injection Vulnerability (NPM/@wong2/mcp-cli) | LOW (CVSS: 5.6) | 2025-08-21 |
| GHSA | [GHSA-GHSA-95m3-7q98-8xr5](https://github.com/advisories/GHSA-95m3-7q98-8xr5): sha.js is missing type checks leading to hash rewind and passing on crafted data (NPM/sha.js) | CRITICAL (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-cpq7-6gpm-g9rc](https://github.com/advisories/GHSA-cpq7-6gpm-g9rc): cipher-base is missing type checks, leading to hash rewind and passing on crafted data (NPM/cipher-base) | CRITICAL (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-79j6-g2m3-jgfw](https://github.com/advisories/GHSA-79j6-g2m3-jgfw): vLLM has remote code execution vulnerability in the tool call parser for Qwen3-Coder (PIP/vllm) | HIGH (CVSS: 8.8) | 2025-08-21 |
| GHSA | [GHSA-GHSA-2464-8j7c-4cjm](https://github.com/advisories/GHSA-2464-8j7c-4cjm): go-viper's mapstructure May Leak Sensitive Information in Logs When Processing Malformed Data (GO/github.com/go-viper/mapstructure/v2) | MODERATE (CVSS: 5.3) | 2025-08-21 |
| GHSA | [GHSA-GHSA-p72g-pv48-7w9x](https://github.com/advisories/GHSA-p72g-pv48-7w9x): Apache Tika XXE Vulnerability via Crafted XFA File Inside a PDF (MAVEN/org.apache.tika:tika-parser-pdf-module) | CRITICAL (CVSS: 9.8) | 2025-08-20 |
| GHSA | [GHSA-GHSA-f9qj-4c5x-cpcw](https://github.com/advisories/GHSA-f9qj-4c5x-cpcw): elysia-cors Origin Validation Error (NPM/@elysiajs/cors) | MODERATE (CVSS: 6.5) | 2025-08-20 |
| GHSA | [GHSA-GHSA-xh9h-692f-mmg4](https://github.com/advisories/GHSA-xh9h-692f-mmg4): Microsoft Knack ReDoS Vulnerability in the Introspection Module (PIP/knack) | LOW (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-6fxp-p9mg-q64w](https://github.com/advisories/GHSA-6fxp-p9mg-q64w): Microsoft Knack ReDoS Vulnerability in the Introspection Module (PIP/knack) | LOW (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-62pf-hcwj-rcfc](https://github.com/advisories/GHSA-62pf-hcwj-rcfc): Liferay Portal Vulnerable to Cross-Site Scripting via DDMPortlet_definition Parameter (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-mpww-r37c-vxjw](https://github.com/advisories/GHSA-mpww-r37c-vxjw): Liferay Portal Vulnerable to Cross-Site Scripting in Dynamic Data Mapping (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-mmxm-8w33-wc4h](https://github.com/advisories/GHSA-mmxm-8w33-wc4h): Eclipse Jetty affected by MadeYouReset HTTP/2 vulnerability (MAVEN/org.eclipse.jetty.http2:jetty-http2-common, MAVEN/org.eclipse.jetty.http2:jetty-http2-common, MAVEN/org.eclipse.jetty.http2:http2-common) | HIGH (CVSS: 7.5) | 2025-08-20 |
| GHSA | [GHSA-GHSA-8xfq-7f6m-mpmf](https://github.com/advisories/GHSA-8xfq-7f6m-mpmf): MoonShine Arbitrary File Upload Vulnerability (COMPOSER/moonshine/moonshine) | MODERATE (CVSS: 4.5) | 2025-08-19 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [9a36b58](https://github.com/torvalds/linux/commit/9a36b58a88f62398dbd005e5f3648f257ae2b9b4) | Merge tag 'spi-fix-v6.17-rc2' of git://git.kernel.org/pub/scm/linux/kernel/git/broonie/spi | 2025-08-21 |
| chromium/chromium | [c144985](https://github.com/chromium/chromium/commit/c144985e3b0968266017ae8958dee6dd292f2081) | Revert "[Fix] Use WeakPtr in NavigationWaiter to prevent crash" | 2025-08-21 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| langflow-ai/langflow | [#9474](https://github.com/langflow-ai/langflow/pull/9474) | docs: troubleshooting backlog items | 2025-08-21 |

