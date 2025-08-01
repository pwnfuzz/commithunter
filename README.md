# Security Updates Monitor

*Last updated: 2025-08-01 18:22:00 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 15 |
| COMMIT | 2 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-2rjv-cv85-xhgm](https://github.com/advisories/GHSA-2rjv-cv85-xhgm): OpenSearch unauthorized data access on fields protected by field level security if field is a member of an object (MAVEN/org.opensearch.plugin:opensearch-security) | MODERATE (CVSS: 5.7) | 2025-08-01 |
| GHSA | [GHSA-GHSA-rrmm-wq7q-h4v5](https://github.com/advisories/GHSA-rrmm-wq7q-h4v5): OpenSearch unauthorized data access on fields protected by field masking for fields of type ip, geo_point, geo_shape, xy_point, xy_shape (MAVEN/org.opensearch.plugin:opensearch-security) | MODERATE (CVSS: 5.7) | 2025-08-01 |
| GHSA | [GHSA-GHSA-8j63-96wh-wh3j](https://github.com/advisories/GHSA-8j63-96wh-wh3j): 1Panel agent certificate verification bypass leading to arbitrary command execution (GO/github.com/1Panel-dev/1Panel/core, GO/github.com/1Panel-dev/1Panel/core) | HIGH (CVSS: 8.1) | 2025-08-01 |
| GHSA | [GHSA-GHSA-q6gg-9f92-r9wg](https://github.com/advisories/GHSA-q6gg-9f92-r9wg): Traefik Client Plugin's Path Traversal Vulnerability Allows Arbitrary File Overwrite and Remote Code Execution (GO/github.com/traefik/traefik/v3, GO/github.com/traefik/traefik/v3, GO/github.com/traefik/traefik/v2) | HIGH (CVSS: 0.0) | 2025-08-01 |
| GHSA | [GHSA-GHSA-782f-gxj5-xvqc](https://github.com/advisories/GHSA-782f-gxj5-xvqc): Microweber Has Stored XSS Vulnerability in User Profile Fields (COMPOSER/microweber/microweber) | LOW (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-wx6g-fm6f-w822](https://github.com/advisories/GHSA-wx6g-fm6f-w822): MaterialX Stack Overflow via Lack of MTLX XML Parsing Recursion Limit  (PIP/MaterialX) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-qhpm-86v7-phmm](https://github.com/advisories/GHSA-qhpm-86v7-phmm): OpenEXR ScanLineProcess::run_fill NULL Pointer Write In "reduceMemory" Mode (PIP/OpenEXR) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-4r7w-q3jg-ff43](https://github.com/advisories/GHSA-4r7w-q3jg-ff43): OpenEXR Out of Bounds Heap Read due to Bad Pointer Arithmetic in LossyDctDecoder_execute (PIP/OpenEXR) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-7c78-rm87-5673](https://github.com/advisories/GHSA-7c78-rm87-5673): MS SWIFT WEB-UI RCE Vulnerability (PIP/ms-swift) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-r54c-2xmf-2cf3](https://github.com/advisories/GHSA-r54c-2xmf-2cf3): MS SWIFT Deserialization RCE Vulnerability (PIP/ms-swift) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-fm6c-f59h-7mmg](https://github.com/advisories/GHSA-fm6c-f59h-7mmg): MS SWIFT Remote Code Execution via unsafe PyYAML deserialization (PIP/ms-swift) | LOW (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-qc2h-74x3-4v3w](https://github.com/advisories/GHSA-qc2h-74x3-4v3w): MaterialX Lack of MTLX Import Depth Limit Leads to DoS (Denial-Of-Service) Via Stack Exhaustion (PIP/MaterialX) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-jxr6-qrxx-2ph2](https://github.com/advisories/GHSA-jxr6-qrxx-2ph2): num2words subjected to phishing attack, two versions published containing malware (PIP/num2words) | CRITICAL (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-9qm3-6qrr-c76m](https://github.com/advisories/GHSA-9qm3-6qrr-c76m): @nyariv/sandboxjs has Prototype Pollution vulnerability that may lead to RCE (NPM/@nyariv/sandboxjs) | HIGH (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-x22w-82jp-8rvf](https://github.com/advisories/GHSA-x22w-82jp-8rvf): OpenEXR Out-Of-Memory via Unbounded File Header Values (PIP/OpenEXR) | MODERATE (CVSS: 0.0) | 2025-07-31 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [c93529a](https://github.com/torvalds/linux/commit/c93529ad4fa8d8d8cb21649e70a46991a1dda0f8) | Merge tag 'for-linus-iommufd' of git://git.kernel.org/pub/scm/linux/kernel/git/jgg/iommufd | 2025-07-31 |
| torvalds/linux | [2c8c9aa](https://github.com/torvalds/linux/commit/2c8c9aae4492f813b9b9ae95f0931945a693100e) | Merge tag 'scsi-misc' of git://git.kernel.org/pub/scm/linux/kernel/git/jejb/scsi | 2025-07-31 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28059](https://github.com/openssl/openssl/pull/28059) | Add array memory allocation routines | 2025-08-01 |

