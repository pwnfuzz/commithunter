# Security Updates Monitor

*Last updated: 2025-07-18 18:21:04 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 19 |
| COMMIT | 2 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-6v2p-p543-phr9](https://github.com/advisories/GHSA-6v2p-p543-phr9): golang.org/x/oauth2 Improper Validation of Syntactic Correctness of Input vulnerability (GO/golang.org/x/oauth2) | HIGH (CVSS: 7.5) | 2025-07-18 |
| GHSA | [GHSA-GHSA-76c9-3jph-rj3q](https://github.com/advisories/GHSA-76c9-3jph-rj3q): on-headers is vulnerable to http response header manipulation (NPM/on-headers) | LOW (CVSS: 3.4) | 2025-07-17 |
| GHSA | [GHSA-GHSA-9rcw-c2f9-2j55](https://github.com/advisories/GHSA-9rcw-c2f9-2j55): OpenZeppelin Contracts Bytes's lastIndexOf function with position argument performs out-of-bound memory access on empty buffers (NPM/@openzeppelin/contracts-upgradeable, NPM/@openzeppelin/contracts) | MODERATE (CVSS: 0.0) | 2025-07-17 |
| GHSA | [GHSA-GHSA-hfj7-542q-8fvv](https://github.com/advisories/GHSA-hfj7-542q-8fvv): DiracX-Web is vulnerable to attack through an Open Redirect on its login page (NPM/@dirac-grid/diracx-web-components) | MODERATE (CVSS: 4.7) | 2025-07-17 |
| GHSA | [GHSA-GHSA-f7h5-c625-3795](https://github.com/advisories/GHSA-f7h5-c625-3795): Eclipse GlassFish is vulnerable to Server Side Request Forgery attacks through specific endpoints (MAVEN/org.glassfish.main.admingui:console-common) | HIGH (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-mqxx-c43h-jj9v](https://github.com/advisories/GHSA-mqxx-c43h-jj9v): Eclipse GlassFish is vulnerable to Stored XSS attacks through its Administration Console (MAVEN/org.glassfish.main.admingui:console-common) | MODERATE (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-99f7-hp6j-v6q4](https://github.com/advisories/GHSA-99f7-hp6j-v6q4): Eclipse GlassFish is vulnerable to Login Brute Force attacks through unlimited failed login attempts (MAVEN/org.glassfish.main.admingui:console-common) | MODERATE (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-62g9-99m7-w8wv](https://github.com/advisories/GHSA-62g9-99m7-w8wv): Eclipse GlassFish is vulnerable to Stored XSS attacks through its Administration Console (MAVEN/org.glassfish.main.admingui:console-cluster-plugin) | MODERATE (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-hp97-5x6g-q538](https://github.com/advisories/GHSA-hp97-5x6g-q538): Eclipse GlassFish is vulnerable to Stored XSS attacks through configuration file modifications (MAVEN/org.glassfish.main.admingui:console-common) | MODERATE (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-vqrm-83g6-pfv4](https://github.com/advisories/GHSA-vqrm-83g6-pfv4): Eclipse GlassFish is vulnerable to Reflected XSS attacks through its Administration Console (MAVEN/org.glassfish.main.admingui:console-cluster-plugin, MAVEN/org.glassfish.main.admingui:console-common) | MODERATE (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-h5gc-rm8j-5gpr](https://github.com/advisories/GHSA-h5gc-rm8j-5gpr): LangChain Community SSRF vulnerability exists in RequestsToolkit component  (PIP/langchain-community) | HIGH (CVSS: 8.4) | 2025-06-23 |
| GHSA | [GHSA-GHSA-c6mx-3fj9-9j7q](https://github.com/advisories/GHSA-c6mx-3fj9-9j7q): PowerJob vulnerable to incorrect access control (MAVEN/tech.powerjob:powerjob) | CRITICAL (CVSS: 9.8) | 2023-04-21 |
| GHSA | [GHSA-GHSA-mpvf-6h9g-2hq2](https://github.com/advisories/GHSA-mpvf-6h9g-2hq2): PowerJob Incorrect Access Control vulnerability (MAVEN/tech.powerjob:powerjob) | MODERATE (CVSS: 5.3) | 2023-04-19 |
| GHSA | [GHSA-GHSA-c23v-vqw5-52c5](https://github.com/advisories/GHSA-c23v-vqw5-52c5): PowerJob vulnerable to Incorrect Access Control via the create user/save interface. (MAVEN/tech.powerjob:powerjob) | MODERATE (CVSS: 5.3) | 2023-04-19 |
| GHSA | [GHSA-GHSA-83w4-x5w9-hf4h](https://github.com/advisories/GHSA-83w4-x5w9-hf4h): XXL-JOB vulnerable to Server-Side Request Forgery (SSRF) (MAVEN/com.xuxueli:xxl-job-core) | HIGH (CVSS: 8.8) | 2022-11-17 |
| GHSA | [GHSA-GHSA-x6rc-54xp-ccxx](https://github.com/advisories/GHSA-x6rc-54xp-ccxx): Withdrawn Advisory: Improper Restriction of XML External Entity Reference in Apache ActiveMQ (MAVEN/org.apache.activemq:activemq-client) | CRITICAL (CVSS: 9.8) | 2022-05-14 |
| GHSA | [GHSA-GHSA-4gr7-qw2q-jxh6](https://github.com/advisories/GHSA-4gr7-qw2q-jxh6): Cross-site Scripting in Nacos (MAVEN/com.alibaba.nacos:nacos-common, MAVEN/com.alibaba.nacos:nacos-common) | MODERATE (CVSS: 6.1) | 2022-03-12 |
| GHSA | [GHSA-GHSA-6xx3-rg99-gc3p](https://github.com/advisories/GHSA-6xx3-rg99-gc3p): Timing based private key exposure in Bouncy Castle (NUGET/BouncyCastle, MAVEN/org.bouncycastle:bcprov-jdk16, MAVEN/org.bouncycastle:bcprov-jdk15to18) | MODERATE (CVSS: 5.1) | 2021-08-13 |
| GHSA | [GHSA-GHSA-72m5-fvvv-55m6](https://github.com/advisories/GHSA-72m5-fvvv-55m6): Observable Differences in Behavior to Error Inputs in Bouncy Castle (MAVEN/org.bouncycastle:bcprov-jdk15to18, MAVEN/org.bouncycastle:bcprov-jdk15on, MAVEN/org.bouncycastle:bcprov-ext-jdk16) | MODERATE (CVSS: 5.3) | 2021-04-22 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [eced63e](https://github.com/chromium/chromium/commit/eced63e3e85e6fab9f0545b7af943e271165d726) | Implement PictureInPictureInputProtector | 2025-07-18 |
| chromium/chromium | [b2e3af6](https://github.com/chromium/chromium/commit/b2e3af66b3d34e1414ef87bee0a9a11319f688b1) | Reland "Update video picture-in-picture window title animation" | 2025-07-17 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [#317](https://github.com/chromium/chromium/pull/317) | Bump on-headers and compression in /tools/android/dependency_analysis/js | 2025-07-17 |

