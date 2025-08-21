# Security Updates Monitor

*Last updated: 2025-08-21 19:11:15 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 31 |
| COMMIT | 2 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-rxc4-3w6r-4v47](https://github.com/advisories/GHSA-rxc4-3w6r-4v47): vllm API endpoints vulnerable to Denial of Service Attacks (PIP/vllm) | HIGH (CVSS: 7.5) | 2025-08-21 |
| GHSA | [GHSA-GHSA-gq3r-5833-5532](https://github.com/advisories/GHSA-gq3r-5833-5532): Mattermost Fails to Validate File Paths (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost-server) | MODERATE (CVSS: 6.8) | 2025-08-21 |
| GHSA | [GHSA-GHSA-8hmm-4crw-vm2c](https://github.com/advisories/GHSA-8hmm-4crw-vm2c): @musistudio/claude-code-router has improper CORS configuration (NPM/@musistudio/claude-code-router) | LOW (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-pp7p-q8fx-2968](https://github.com/advisories/GHSA-pp7p-q8fx-2968): vite-plugin-static-copy files not included in `src` are possible to access with a crafted request (NPM/vite-plugin-static-copy, NPM/vite-plugin-static-copy) | MODERATE (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-p6rm-483j-37jf](https://github.com/advisories/GHSA-p6rm-483j-37jf): wong2 mcp-cli Command Injection Vulnerability (NPM/@wong2/mcp-cli) | LOW (CVSS: 5.6) | 2025-08-21 |
| GHSA | [GHSA-GHSA-95m3-7q98-8xr5](https://github.com/advisories/GHSA-95m3-7q98-8xr5): sha.js is missing type checks leading to hash rewind and passing on crafted data (NPM/sha.js) | CRITICAL (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-cpq7-6gpm-g9rc](https://github.com/advisories/GHSA-cpq7-6gpm-g9rc): cipher-base is missing type checks, leading to hash rewind and passing on crafted data (NPM/cipher-base) | CRITICAL (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-79j6-g2m3-jgfw](https://github.com/advisories/GHSA-79j6-g2m3-jgfw): vLLM has remote code execution vulnerability in the tool call parser for Qwen3-Coder (PIP/vllm) | HIGH (CVSS: 8.8) | 2025-08-21 |
| GHSA | [GHSA-GHSA-2464-8j7c-4cjm](https://github.com/advisories/GHSA-2464-8j7c-4cjm): go-viper's mapstructure May Leak Sensitive Information in Logs When Processing Malformed Data (GO/github.com/go-viper/mapstructure/v2) | MODERATE (CVSS: 5.3) | 2025-08-21 |
| GHSA | [GHSA-GHSA-287x-6r2h-f9mw](https://github.com/advisories/GHSA-287x-6r2h-f9mw): UnoPim vulnerable to CSRF on Product edit feature and creation of other types (COMPOSER/unopim/unopim) | MODERATE (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-v22v-xwh7-2vrm](https://github.com/advisories/GHSA-v22v-xwh7-2vrm): UnoPim vulnerable to remote code execution through Arbitrary File upload (COMPOSER/unopim/unopim) | HIGH (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-xr97-25v7-hc2q](https://github.com/advisories/GHSA-xr97-25v7-hc2q): UnoPim has Stored Cross-site Scripting vulnerability in user creation functionality (COMPOSER/unopim/unopim) | HIGH (CVSS: 8.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-p72g-pv48-7w9x](https://github.com/advisories/GHSA-p72g-pv48-7w9x): Apache Tika XXE Vulnerability via Crafted XFA File Inside a PDF (MAVEN/org.apache.tika:tika-parser-pdf-module) | CRITICAL (CVSS: 9.8) | 2025-08-20 |
| GHSA | [GHSA-GHSA-f9qj-4c5x-cpcw](https://github.com/advisories/GHSA-f9qj-4c5x-cpcw): elysia-cors Origin Validation Error (NPM/@elysiajs/cors) | MODERATE (CVSS: 6.5) | 2025-08-20 |
| GHSA | [GHSA-GHSA-xh9h-692f-mmg4](https://github.com/advisories/GHSA-xh9h-692f-mmg4): Microsoft Knack ReDoS Vulnerability in the Introspection Module (PIP/knack) | LOW (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-6fxp-p9mg-q64w](https://github.com/advisories/GHSA-6fxp-p9mg-q64w): Microsoft Knack ReDoS Vulnerability in the Introspection Module (PIP/knack) | LOW (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-62pf-hcwj-rcfc](https://github.com/advisories/GHSA-62pf-hcwj-rcfc): Liferay Portal Vulnerable to Cross-Site Scripting via DDMPortlet_definition Parameter (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-mpww-r37c-vxjw](https://github.com/advisories/GHSA-mpww-r37c-vxjw): Liferay Portal Vulnerable to Cross-Site Scripting in Dynamic Data Mapping (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-mmxm-8w33-wc4h](https://github.com/advisories/GHSA-mmxm-8w33-wc4h): Eclipse Jetty affected by MadeYouReset HTTP/2 vulnerability (MAVEN/org.eclipse.jetty.http2:jetty-http2-common, MAVEN/org.eclipse.jetty.http2:jetty-http2-common, MAVEN/org.eclipse.jetty.http2:http2-common) | HIGH (CVSS: 7.5) | 2025-08-20 |
| GHSA | [GHSA-GHSA-ggjm-f3g4-rwmm](https://github.com/advisories/GHSA-ggjm-f3g4-rwmm): n8n symlink traversal vulnerability in "Read/Write File" node allows access to restricted files (NPM/n8n) | MODERATE (CVSS: 6.5) | 2025-08-20 |
| GHSA | [GHSA-GHSA-3j63-5h8p-gf7c](https://github.com/advisories/GHSA-3j63-5h8p-gf7c): x402 SDK vulnerable in outdated versions in resource servers for builders (NPM/x402-hono, NPM/x402-express, NPM/x402-next) | HIGH (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-p9gc-59hf-x48p](https://github.com/advisories/GHSA-p9gc-59hf-x48p): Liferay Portal Vulnerable to Cross-Site Request Forgery (MAVEN/com.liferay.portal:release.portal.bom) | HIGH (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-5fx5-cff6-f3fp](https://github.com/advisories/GHSA-5fx5-cff6-f3fp): Liferay Portal Unauthenticated File Access via URL (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-56qj-wp5r-mvhj](https://github.com/advisories/GHSA-56qj-wp5r-mvhj): Liferay Portal Unvalidated File Upload (MAVEN/com.liferay:com.liferay.dynamic.data.mapping.form.web) | MODERATE (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-j6p8-g3rj-ghpm](https://github.com/advisories/GHSA-j6p8-g3rj-ghpm): Liferay Portal Vulnerable to Cross-Site Scripting via assetTagNames Parameter (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-3fp2-6mwq-4q3j](https://github.com/advisories/GHSA-3fp2-6mwq-4q3j): Liferay Portal Vulnerable to Cross-Site Scripting through URLs (MAVEN/com.liferay:com.liferay.layout.type.controller.display.page) | MODERATE (CVSS: 0.0) | 2025-08-20 |
| GHSA | [GHSA-GHSA-8xfq-7f6m-mpmf](https://github.com/advisories/GHSA-8xfq-7f6m-mpmf): MoonShine Arbitrary File Upload Vulnerability (COMPOSER/moonshine/moonshine) | MODERATE (CVSS: 4.5) | 2025-08-19 |
| GHSA | [GHSA-GHSA-m49p-6cjp-x2h3](https://github.com/advisories/GHSA-m49p-6cjp-x2h3): Liferay Portal Vulnerable to Cross-Site Scripting via DDM Structure Field Labels (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-8gwm-58g9-j8pw](https://github.com/advisories/GHSA-8gwm-58g9-j8pw): Mermaid does not properly sanitize architecture diagram iconText leading to XSS (NPM/mermaid) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-4gg5-vx3j-xwc7](https://github.com/advisories/GHSA-4gg5-vx3j-xwc7): Protobuf Java vulnerable to Uncontrolled Resource Consumption (MAVEN/com.google.protobuf:protobuf-java, MAVEN/com.google.protobuf:protobuf-javalite, MAVEN/com.google.protobuf:protobuf-javalite) | HIGH (CVSS: 7.5) | 2022-12-12 |
| GHSA | [GHSA-GHSA-g5ww-5jh7-63cx](https://github.com/advisories/GHSA-g5ww-5jh7-63cx): Protobuf Java vulnerable to Uncontrolled Resource Consumption (MAVEN/com.google.protobuf:protobuf-java, MAVEN/com.google.protobuf:protobuf-javalite, MAVEN/com.google.protobuf:protobuf-javalite) | HIGH (CVSS: 7.5) | 2022-12-12 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [c144985](https://github.com/chromium/chromium/commit/c144985e3b0968266017ae8958dee6dd292f2081) | Revert "[Fix] Use WeakPtr in NavigationWaiter to prevent crash" | 2025-08-21 |
| torvalds/linux | [41cd3fd](https://github.com/torvalds/linux/commit/41cd3fd152634250fdd09a52a35352b3f323800d) | Merge tag 'pci-v6.17-fixes-2' of git://git.kernel.org/pub/scm/linux/kernel/git/pci/pci | 2025-08-20 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| langflow-ai/langflow | [#9474](https://github.com/langflow-ai/langflow/pull/9474) | docs: troubleshooting backlog items | 2025-08-21 |

