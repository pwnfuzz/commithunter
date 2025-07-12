# Security Updates Monitor

*Last updated: 2025-07-12 10:14:44 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 9 |
| COMMIT | 5 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-j288-q9x7-2f5v](https://github.com/advisories/GHSA-j288-q9x7-2f5v): Apache Commons Lang is vulnerable to Uncontrolled Recursion when processing long inputs (MAVEN/commons-lang:commons-lang, MAVEN/org.apache.commons:commons-lang3) | MODERATE (CVSS: 6.5) | 2025-07-11 |
| GHSA | [GHSA-GHSA-xrrq-rrgq-h89w](https://github.com/advisories/GHSA-xrrq-rrgq-h89w): static-alloc vulnerability leads to uninitialized read after allocating MemBump (RUST/static-alloc) | LOW (CVSS: 0.0) | 2025-07-11 |
| GHSA | [GHSA-GHSA-37mw-44qp-f5jm](https://github.com/advisories/GHSA-37mw-44qp-f5jm): Transformers is vulnerable to ReDoS attack through its DonutProcessor class (PIP/transformers) | MODERATE (CVSS: 5.3) | 2025-07-11 |
| GHSA | [GHSA-GHSA-25xr-qj8w-c4vf](https://github.com/advisories/GHSA-25xr-qj8w-c4vf): Apache Tomcat Coyote vulnerable to Denial of Service via excessive HTTP/2 streams (MAVEN/org.apache.tomcat:tomcat-coyote, MAVEN/org.apache.tomcat:tomcat-coyote, MAVEN/org.apache.tomcat:tomcat-coyote) | MODERATE (CVSS: 7.5) | 2025-07-10 |
| GHSA | [GHSA-GHSA-wr62-c79q-cv37](https://github.com/advisories/GHSA-wr62-c79q-cv37): Apache Tomcat Catalina is vulnerable to DoS attack through bypassing of size limits (MAVEN/org.apache.tomcat:tomcat-catalina, MAVEN/org.apache.tomcat:tomcat-catalina, MAVEN/org.apache.tomcat:tomcat-catalina) | MODERATE (CVSS: 7.5) | 2025-07-10 |
| GHSA | [GHSA-GHSA-275g-g844-73jh](https://github.com/advisories/GHSA-275g-g844-73jh): Matrix Rust SDK vulnerable to SQL Injection through its EventCache implementation (RUST/matrix-sdk-sqlite, RUST/matrix-sdk) | MODERATE (CVSS: 0.0) | 2025-07-10 |
| GHSA | [GHSA-GHSA-x5gf-qvw8-r2rm](https://github.com/advisories/GHSA-x5gf-qvw8-r2rm): pm2 Regular Expression Denial of Service vulnerability (NPM/pm2) | LOW (CVSS: 4.3) | 2025-06-09 |
| GHSA | [GHSA-GHSA-gp98-hfvm-2r4x](https://github.com/advisories/GHSA-gp98-hfvm-2r4x): Apache IoTDB JDBC Driver Discloses Sensitive Information via Log Files (MAVEN/org.apache.iotdb:iotdb-jdbc, MAVEN/org.apache.iotdb:iotdb-jdbc) | MODERATE (CVSS: 7.5) | 2025-05-14 |
| GHSA | [GHSA-GHSA-fpwp-69xv-c67f](https://github.com/advisories/GHSA-fpwp-69xv-c67f): aiohttp-session Session Fixation vulnerability (PIP/aiohttp-session) | HIGH (CVSS: 6.5) | 2018-09-13 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [2323efd](https://github.com/chromium/chromium/commit/2323efdd56bec882a440296f3a1999614a25fe2c) | [Multiple Requests] Fix issue in virtual card enrollment. | 2025-07-12 |
| torvalds/linux | [40f92e7](https://github.com/torvalds/linux/commit/40f92e79b0aabbf3575e371f9054657a421a3e79) | Merge tag 'block-6.16-20250710' of git://git.kernel.dk/linux | 2025-07-11 |
| chromium/chromium | [db40b07](https://github.com/chromium/chromium/commit/db40b0718a6a1a9a48451056850f615c58d920eb) | Use a WeakPtr for the Web Payment Handler progress bar. | 2025-07-11 |
| chromium/chromium | [94b9495](https://github.com/chromium/chromium/commit/94b949573d9e12e2c6fd97cf9986b7cbbc32dddf) | Avoid calling SetNeedsRedraw for each queue inside MarkTilesOOM. | 2025-07-11 |
| torvalds/linux | [eb41a26](https://github.com/torvalds/linux/commit/eb41a264a3a576dc040ee37c3d9d6b7e2d9be968) | net/mlx5e: Fix race between DIM disable and net_dim() | 2025-07-10 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| langflow-ai/langflow | [#9020](https://github.com/langflow-ai/langflow/pull/9020) | Feat/OAuth Single Sign-On Implementation with Google and Microsoft AD (Entra ID) | 2025-07-11 |

