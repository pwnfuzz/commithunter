# Security Updates Monitor

*Last updated: 2025-08-02 10:15:22 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 15 |
| COMMIT | 4 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-2rjv-cv85-xhgm](https://github.com/advisories/GHSA-2rjv-cv85-xhgm): OpenSearch unauthorized data access on fields protected by field level security if field is a member of an object (MAVEN/org.opensearch.plugin:opensearch-security) | MODERATE (CVSS: 5.7) | 2025-08-01 |
| GHSA | [GHSA-GHSA-rrmm-wq7q-h4v5](https://github.com/advisories/GHSA-rrmm-wq7q-h4v5): OpenSearch unauthorized data access on fields protected by field masking for fields of type ip, geo_point, geo_shape, xy_point, xy_shape (MAVEN/org.opensearch.plugin:opensearch-security) | MODERATE (CVSS: 5.7) | 2025-08-01 |
| GHSA | [GHSA-GHSA-8j63-96wh-wh3j](https://github.com/advisories/GHSA-8j63-96wh-wh3j): 1Panel agent certificate verification bypass leading to arbitrary command execution (GO/github.com/1Panel-dev/1Panel/core, GO/github.com/1Panel-dev/1Panel/core) | HIGH (CVSS: 8.1) | 2025-08-01 |
| GHSA | [GHSA-GHSA-q6gg-9f92-r9wg](https://github.com/advisories/GHSA-q6gg-9f92-r9wg): Traefik Client Plugin's Path Traversal Vulnerability Allows Arbitrary File Overwrite and Remote Code Execution (GO/github.com/traefik/traefik/v3, GO/github.com/traefik/traefik/v3, GO/github.com/traefik/traefik/v2) | HIGH (CVSS: 0.0) | 2025-08-01 |
| GHSA | [GHSA-GHSA-qc2h-74x3-4v3w](https://github.com/advisories/GHSA-qc2h-74x3-4v3w): MaterialX Lack of MTLX Import Depth Limit Leads to DoS (Denial-Of-Service) Via Stack Exhaustion (PIP/MaterialX) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-wx6g-fm6f-w822](https://github.com/advisories/GHSA-wx6g-fm6f-w822): MaterialX Stack Overflow via Lack of MTLX XML Parsing Recursion Limit  (PIP/MaterialX) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-x22w-82jp-8rvf](https://github.com/advisories/GHSA-x22w-82jp-8rvf): OpenEXR Out-Of-Memory via Unbounded File Header Values (PIP/OpenEXR) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-fm6c-f59h-7mmg](https://github.com/advisories/GHSA-fm6c-f59h-7mmg): MS SWIFT Remote Code Execution via unsafe PyYAML deserialization (PIP/ms-swift) | LOW (CVSS: 9.8) | 2025-07-31 |
| GHSA | [GHSA-GHSA-782f-gxj5-xvqc](https://github.com/advisories/GHSA-782f-gxj5-xvqc): Microweber Has Stored XSS Vulnerability in User Profile Fields (COMPOSER/microweber/microweber) | LOW (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-qhpm-86v7-phmm](https://github.com/advisories/GHSA-qhpm-86v7-phmm): OpenEXR ScanLineProcess::run_fill NULL Pointer Write In "reduceMemory" Mode (PIP/OpenEXR) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-4r7w-q3jg-ff43](https://github.com/advisories/GHSA-4r7w-q3jg-ff43): OpenEXR Out of Bounds Heap Read due to Bad Pointer Arithmetic in LossyDctDecoder_execute (PIP/OpenEXR) | MODERATE (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-rxf6-323f-44fc](https://github.com/advisories/GHSA-rxf6-323f-44fc): Duplicate Advisory: rust-protobuf crate is vulnerable to Uncontrolled Recursion, potentially leading to DoS (RUST/protobuf) | MODERATE (CVSS: 5.9) | 2025-07-05 |
| GHSA | [GHSA-GHSA-33p9-3p43-82vq](https://github.com/advisories/GHSA-33p9-3p43-82vq): Jupyter Core on Windows Has Uncontrolled Search Path Element Local Privilege Escalation Vulnerability (PIP/jupyter_core) | HIGH (CVSS: 7.3) | 2025-06-04 |
| GHSA | [GHSA-GHSA-2gh3-rmm4-6rq5](https://github.com/advisories/GHSA-2gh3-rmm4-6rq5): Crash due to uncontrolled recursion in protobuf crate (RUST/protobuf) | MODERATE (CVSS: 0.0) | 2025-03-07 |
| GHSA | [GHSA-GHSA-4fwr-mh5q-hchh](https://github.com/advisories/GHSA-4fwr-mh5q-hchh): io.quarkus:quarkus-resteasy: Memory Leak in Quarkus RESTEasy Classic When Client Requests Timeout (MAVEN/io.quarkus:quarkus-resteasy, MAVEN/io.quarkus:quarkus-resteasy, MAVEN/io.quarkus:quarkus-resteasy) | HIGH (CVSS: 7.5) | 2025-02-26 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [a6923c0](https://github.com/torvalds/linux/commit/a6923c06a3b2e2c534ae28c53a7531e76cc95cfa) | Merge tag 'bpf-fixes' of git://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf | 2025-08-02 |
| postgres/postgres | [3b3fa94](https://github.com/postgres/postgres/commit/3b3fa949009393541e552b8ae42cc2b03be25549) | Fix use-after-free with INSERT ON CONFLICT changes in reorderbuffer.c | 2025-08-02 |
| torvalds/linux | [821c9e5](https://github.com/torvalds/linux/commit/821c9e515db512904250e1d460109a1dc4c7ef6b) | Merge tag 'for_linus' of git://git.kernel.org/pub/scm/linux/kernel/git/mst/vhost | 2025-08-01 |
| torvalds/linux | [fac6b82](https://github.com/torvalds/linux/commit/fac6b82e0f3eaca33c8c67ec401681b21143ae17) | vsock/virtio: Move SKB allocation lower-bound check to callers | 2025-07-17 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28059](https://github.com/openssl/openssl/pull/28059) | Add array memory allocation routines | 2025-08-01 |

