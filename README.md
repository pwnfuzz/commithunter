# Security Updates Monitor

*Last updated: 2025-07-11 22:14:28 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 14 |
| COMMIT | 6 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-xrrq-rrgq-h89w](https://github.com/advisories/GHSA-xrrq-rrgq-h89w): static-alloc vulnerability leads to uninitialized read after allocating MemBump (RUST/static-alloc) | LOW (CVSS: 0.0) | 2025-07-11 |
| GHSA | [GHSA-GHSA-37mw-44qp-f5jm](https://github.com/advisories/GHSA-37mw-44qp-f5jm): Transformers is vulnerable to ReDoS attack through its DonutProcessor class (PIP/transformers) | MODERATE (CVSS: 5.3) | 2025-07-11 |
| GHSA | [GHSA-GHSA-275g-g844-73jh](https://github.com/advisories/GHSA-275g-g844-73jh): Matrix Rust SDK vulnerable to SQL Injection through its EventCache implementation (RUST/matrix-sdk-sqlite, RUST/matrix-sdk) | MODERATE (CVSS: 0.0) | 2025-07-10 |
| GHSA | [GHSA-GHSA-25xr-qj8w-c4vf](https://github.com/advisories/GHSA-25xr-qj8w-c4vf): Apache Tomcat Coyote vulnerable to Denial of Service via excessive HTTP/2 streams (MAVEN/org.apache.tomcat:tomcat-coyote, MAVEN/org.apache.tomcat:tomcat-coyote, MAVEN/org.apache.tomcat:tomcat-coyote) | MODERATE (CVSS: 0.0) | 2025-07-10 |
| GHSA | [GHSA-GHSA-wr62-c79q-cv37](https://github.com/advisories/GHSA-wr62-c79q-cv37): Apache Tomcat Catalina is vulnerable to DoS attack through bypassing of size limits (MAVEN/org.apache.tomcat:tomcat-catalina, MAVEN/org.apache.tomcat:tomcat-catalina, MAVEN/org.apache.tomcat:tomcat-catalina) | MODERATE (CVSS: 0.0) | 2025-07-10 |
| GHSA | [GHSA-GHSA-54xv-94qv-2gfg](https://github.com/advisories/GHSA-54xv-94qv-2gfg): @pdfme/common vulnerable to to XSS and Prototype Pollution through its expression evaluation (NPM/@pdfme/common) | MODERATE (CVSS: 6.1) | 2025-07-10 |
| GHSA | [GHSA-GHSA-3gv2-v3jx-r9fh](https://github.com/advisories/GHSA-3gv2-v3jx-r9fh): Chall-Manager is vulnerable to Path Traversal when extracting/decoding a zip archive (GO/github.com/ctfer-io/chall-manager) | HIGH (CVSS: 0.0) | 2025-07-10 |
| GHSA | [GHSA-GHSA-ggmv-j932-q89q](https://github.com/advisories/GHSA-ggmv-j932-q89q): Chall-Manager's HTTP Gateway is vulnerable to DoS due to missing header timeout (GO/github.com/ctfer-io/chall-manager) | HIGH (CVSS: 0.0) | 2025-07-10 |
| GHSA | [GHSA-GHSA-r7fm-3pqm-ww5w](https://github.com/advisories/GHSA-r7fm-3pqm-ww5w): Chall-Manager's scenario decoding process does not check for zip bombs (GO/github.com/ctfer-io/chall-manager) | HIGH (CVSS: 0.0) | 2025-07-10 |
| GHSA | [GHSA-GHSA-x5gf-qvw8-r2rm](https://github.com/advisories/GHSA-x5gf-qvw8-r2rm): pm2 Regular Expression Denial of Service vulnerability (NPM/pm2) | LOW (CVSS: 4.3) | 2025-06-09 |
| GHSA | [GHSA-GHSA-jqfv-jrvq-95jm](https://github.com/advisories/GHSA-jqfv-jrvq-95jm): Apache XML Graphics FOP XML External Entity Reference ('XXE') vulnerability (MAVEN/org.apache.xmlgraphics:fop-core) | MODERATE (CVSS: 5.3) | 2024-10-09 |
| GHSA | [GHSA-GHSA-r7pg-v2c8-mfg3](https://github.com/advisories/GHSA-r7pg-v2c8-mfg3): Apache Avro Java SDK: Arbitrary Code Execution when reading Avro Data (Java SDK) (MAVEN/org.apache.avro:avro) | CRITICAL (CVSS: 9.8) | 2024-10-03 |
| GHSA | [GHSA-GHSA-f5fw-25gw-5m92](https://github.com/advisories/GHSA-f5fw-25gw-5m92): Apache Hadoop: Temporary File Local Information Disclosure (MAVEN/org.apache.hadoop:hadoop-common) | LOW (CVSS: 3.3) | 2024-09-25 |
| GHSA | [GHSA-GHSA-6247-7862-q2pq](https://github.com/advisories/GHSA-6247-7862-q2pq): Apache Helix Front (UI) component contained a hard-coded secret (MAVEN/org.apache.helix:helix) | HIGH (CVSS: 7.5) | 2024-08-21 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [40f92e7](https://github.com/torvalds/linux/commit/40f92e79b0aabbf3575e371f9054657a421a3e79) | Merge tag 'block-6.16-20250710' of git://git.kernel.dk/linux | 2025-07-11 |
| torvalds/linux | [7ac5cc2](https://github.com/torvalds/linux/commit/7ac5cc2616257cf80d32a8814e44474f07efed62) | Merge tag 'wireless-2025-07-10' of https://git.kernel.org/pub/scm/linux/kernel/git/wireless/wireless | 2025-07-11 |
| chromium/chromium | [db40b07](https://github.com/chromium/chromium/commit/db40b0718a6a1a9a48451056850f615c58d920eb) | Use a WeakPtr for the Web Payment Handler progress bar. | 2025-07-11 |
| chromium/chromium | [94b9495](https://github.com/chromium/chromium/commit/94b949573d9e12e2c6fd97cf9986b7cbbc32dddf) | Avoid calling SetNeedsRedraw for each queue inside MarkTilesOOM. | 2025-07-11 |
| torvalds/linux | [eb41a26](https://github.com/torvalds/linux/commit/eb41a264a3a576dc040ee37c3d9d6b7e2d9be968) | net/mlx5e: Fix race between DIM disable and net_dim() | 2025-07-10 |
| chromium/chromium | [f0a1284](https://github.com/chromium/chromium/commit/f0a12849f29b89172b76361b74602454b07ef1ab) | Add 'URL:Google Internal' to template. | 2025-07-10 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| langflow-ai/langflow | [#9020](https://github.com/langflow-ai/langflow/pull/9020) | Feat/OAuth Single Sign-On Implementation with Google and Microsoft AD (Entra ID) | 2025-07-11 |

