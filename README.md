# Security Updates Monitor

*Last updated: 2025-08-01 06:25:55 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 15 |
| COMMIT | 4 |
| PR | 2 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-fm6c-f59h-7mmg](https://github.com/advisories/GHSA-fm6c-f59h-7mmg): MS SWIFT Remote Code Execution via unsafe PyYAML deserialization (PIP/ms-swift) | LOW (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-qc2h-74x3-4v3w](https://github.com/advisories/GHSA-qc2h-74x3-4v3w): MaterialX Lack of MTLX Import Depth Limit Leads to DoS (Denial-Of-Service) Via Stack Exhaustion (PIP/MaterialX) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-wx6g-fm6f-w822](https://github.com/advisories/GHSA-wx6g-fm6f-w822): MaterialX Stack Overflow via Lack of MTLX XML Parsing Recursion Limit  (PIP/MaterialX) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-jxr6-qrxx-2ph2](https://github.com/advisories/GHSA-jxr6-qrxx-2ph2): num2words subjected to phishing attack, two versions published containing malware (PIP/num2words) | CRITICAL (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-9qm3-6qrr-c76m](https://github.com/advisories/GHSA-9qm3-6qrr-c76m): @nyariv/sandboxjs has Prototype Pollution vulnerability that may lead to RCE (NPM/@nyariv/sandboxjs) | HIGH (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-x22w-82jp-8rvf](https://github.com/advisories/GHSA-x22w-82jp-8rvf): OpenEXR Out-Of-Memory via Unbounded File Header Values (PIP/OpenEXR) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-qhpm-86v7-phmm](https://github.com/advisories/GHSA-qhpm-86v7-phmm): OpenEXR ScanLineProcess::run_fill NULL Pointer Write In "reduceMemory" Mode (PIP/OpenEXR) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-4r7w-q3jg-ff43](https://github.com/advisories/GHSA-4r7w-q3jg-ff43): OpenEXR Out of Bounds Heap Read due to Bad Pointer Arithmetic in LossyDctDecoder_execute (PIP/OpenEXR) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-8mx2-rjh8-q3jq](https://github.com/advisories/GHSA-8mx2-rjh8-q3jq): copyparty Reflected XSS via Filter Parameter (PIP/copyparty) | MODERATE (CVSS: 6.3) | 2025-07-31 |
| GHSA | [GHSA-GHSA-72ww-4rcw-mc62](https://github.com/advisories/GHSA-72ww-4rcw-mc62): Apache JSPWiki Cross-Site Scripting (XSS) Vulnerability in the Image Plugin (MAVEN/org.apache.jspwiki:jspwiki-main) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-rrff-chj9-w4c7](https://github.com/advisories/GHSA-rrff-chj9-w4c7): Apache JSPWiki Cross-Site Scripting (XSS) Vulnerability via Header Link Rendering (MAVEN/org.apache.jspwiki:jspwiki-markdown, MAVEN/org.apache.jspwiki:jspwiki-main) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-7c78-rm87-5673](https://github.com/advisories/GHSA-7c78-rm87-5673): MS SWIFT WEB-UI RCE Vulnerability (PIP/ms-swift) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-r54c-2xmf-2cf3](https://github.com/advisories/GHSA-r54c-2xmf-2cf3): MS SWIFT Deserialization RCE Vulnerability (PIP/ms-swift) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-7rh7-c77v-6434](https://github.com/advisories/GHSA-7rh7-c77v-6434): OAuth2-Proxy has authentication bypass in oauth2-proxy skip_auth_routes due to Query Parameter inclusion (GO/github.com/oauth2-proxy/oauth2-proxy/v7) | CRITICAL (CVSS: 9.1) | 2025-07-30 |
| GHSA | [GHSA-GHSA-8xq3-w9fx-74rv](https://github.com/advisories/GHSA-8xq3-w9fx-74rv): webfinger.js Blind SSRF Vulnerability (NPM/webfinger.js) | MODERATE (CVSS: 0.0) | 2025-07-28 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [c93529a](https://github.com/torvalds/linux/commit/c93529ad4fa8d8d8cb21649e70a46991a1dda0f8) | Merge tag 'for-linus-iommufd' of git://git.kernel.org/pub/scm/linux/kernel/git/jgg/iommufd | 2025-07-31 |
| torvalds/linux | [2c8c9aa](https://github.com/torvalds/linux/commit/2c8c9aae4492f813b9b9ae95f0931945a693100e) | Merge tag 'scsi-misc' of git://git.kernel.org/pub/scm/linux/kernel/git/jejb/scsi | 2025-07-31 |
| torvalds/linux | [440e6d7](https://github.com/torvalds/linux/commit/440e6d7e1435bb1e1948eeae34ca8bef6c7c5f82) | Merge tag 'jfs-6.17' of github.com:kleikamp/linux-shaggy | 2025-07-31 |
| chromium/chromium | [66dd91f](https://github.com/chromium/chromium/commit/66dd91fa5bf90d651709f138ff40c3bcb9de0afb) | [ios] Fix possible use-after-free in data sharing code | 2025-07-31 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28059](https://github.com/openssl/openssl/pull/28059) | Add array memory allocation routines | 2025-08-01 |
| langflow-ai/langflow | [#9264](https://github.com/langflow-ai/langflow/pull/9264) | ⚡️ Speed up function `_get_core_dependencies` by 51% in PR #9198 (`cz/pkt-man`) | 2025-07-31 |

