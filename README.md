# Security Updates Monitor

*Last updated: 2025-07-19 01:14:06 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 26 |
| COMMIT | 2 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-5662-cv6m-63wh](https://github.com/advisories/GHSA-5662-cv6m-63wh): melange's world-writable permissions expose SBOM files to potential image tampering (GO/chainguard.dev/melange) | MODERATE (CVSS: 4.4) | 2025-07-18 |
| GHSA | [GHSA-GHSA-x6ph-r535-3vjw](https://github.com/advisories/GHSA-x6ph-r535-3vjw): apko is vulnerable to attack through incorrect permissions in /etc/ld.so.cache and other files (GO/chainguard.dev/apko) | HIGH (CVSS: 7.0) | 2025-07-18 |
| GHSA | [GHSA-GHSA-fm79-3f68-h2fc](https://github.com/advisories/GHSA-fm79-3f68-h2fc): Wasmtime CLI  is vulnerable to host panic through its fd_renumber function (RUST/wasmtime-wasi, RUST/wasmtime-wasi, RUST/wasmtime-wasi) | LOW (CVSS: 3.5) | 2025-07-18 |
| GHSA | [GHSA-GHSA-6v2p-p543-phr9](https://github.com/advisories/GHSA-6v2p-p543-phr9): golang.org/x/oauth2 Improper Validation of Syntactic Correctness of Input vulnerability (GO/golang.org/x/oauth2) | HIGH (CVSS: 7.5) | 2025-07-18 |
| GHSA | [GHSA-GHSA-76c9-3jph-rj3q](https://github.com/advisories/GHSA-76c9-3jph-rj3q): on-headers is vulnerable to http response header manipulation (NPM/on-headers) | LOW (CVSS: 3.4) | 2025-07-17 |
| GHSA | [GHSA-GHSA-f7h5-c625-3795](https://github.com/advisories/GHSA-f7h5-c625-3795): Eclipse GlassFish is vulnerable to Server Side Request Forgery attacks through specific endpoints (MAVEN/org.glassfish.main.admingui:console-common) | HIGH (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-mqxx-c43h-jj9v](https://github.com/advisories/GHSA-mqxx-c43h-jj9v): Eclipse GlassFish is vulnerable to Stored XSS attacks through its Administration Console (MAVEN/org.glassfish.main.admingui:console-common) | MODERATE (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-99f7-hp6j-v6q4](https://github.com/advisories/GHSA-99f7-hp6j-v6q4): Eclipse GlassFish is vulnerable to Login Brute Force attacks through unlimited failed login attempts (MAVEN/org.glassfish.main.admingui:console-common) | MODERATE (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-62g9-99m7-w8wv](https://github.com/advisories/GHSA-62g9-99m7-w8wv): Eclipse GlassFish is vulnerable to Stored XSS attacks through its Administration Console (MAVEN/org.glassfish.main.admingui:console-cluster-plugin) | MODERATE (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-hp97-5x6g-q538](https://github.com/advisories/GHSA-hp97-5x6g-q538): Eclipse GlassFish is vulnerable to Stored XSS attacks through configuration file modifications (MAVEN/org.glassfish.main.admingui:console-common) | MODERATE (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-vqrm-83g6-pfv4](https://github.com/advisories/GHSA-vqrm-83g6-pfv4): Eclipse GlassFish is vulnerable to Reflected XSS attacks through its Administration Console (MAVEN/org.glassfish.main.admingui:console-cluster-plugin, MAVEN/org.glassfish.main.admingui:console-common) | MODERATE (CVSS: 0.0) | 2025-07-16 |
| GHSA | [GHSA-GHSA-c6mx-3fj9-9j7q](https://github.com/advisories/GHSA-c6mx-3fj9-9j7q): PowerJob vulnerable to incorrect access control (MAVEN/tech.powerjob:powerjob) | CRITICAL (CVSS: 9.8) | 2023-04-21 |
| GHSA | [GHSA-GHSA-mpvf-6h9g-2hq2](https://github.com/advisories/GHSA-mpvf-6h9g-2hq2): PowerJob Incorrect Access Control vulnerability (MAVEN/tech.powerjob:powerjob) | MODERATE (CVSS: 5.3) | 2023-04-19 |
| GHSA | [GHSA-GHSA-c23v-vqw5-52c5](https://github.com/advisories/GHSA-c23v-vqw5-52c5): PowerJob vulnerable to Incorrect Access Control via the create user/save interface. (MAVEN/tech.powerjob:powerjob) | MODERATE (CVSS: 5.3) | 2023-04-19 |
| GHSA | [GHSA-GHSA-4j2x-v3mr-467m](https://github.com/advisories/GHSA-4j2x-v3mr-467m): Jeecg-boot vulnerable to SQL injection via updateNullByEmptyString (MAVEN/org.jeecgframework.boot:jeecg-module-system) | CRITICAL (CVSS: 9.8) | 2022-11-25 |
| GHSA | [GHSA-GHSA-25gv-mvm7-5h3h](https://github.com/advisories/GHSA-25gv-mvm7-5h3h): Jeecg-boot vulnerable to SQL injection via /sys/user/putRecycleBin (MAVEN/org.jeecgframework.boot:jeecg-module-system) | MODERATE (CVSS: 4.3) | 2022-11-25 |
| GHSA | [GHSA-GHSA-83w4-x5w9-hf4h](https://github.com/advisories/GHSA-83w4-x5w9-hf4h): XXL-JOB vulnerable to Server-Side Request Forgery (SSRF) (MAVEN/com.xuxueli:xxl-job-core) | HIGH (CVSS: 8.8) | 2022-11-17 |
| GHSA | [GHSA-GHSA-7r3w-wggm-pjwf](https://github.com/advisories/GHSA-7r3w-wggm-pjwf): Liferay Portal and Liferay DXP Vulnerable to XSS in the Portal Search Module (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay:com.liferay.portal.search.web) | MODERATE (CVSS: 6.1) | 2022-09-23 |
| GHSA | [GHSA-GHSA-8gqf-26xw-x3gx](https://github.com/advisories/GHSA-8gqf-26xw-x3gx): Liferay Portal XSS Vulnerability  (MAVEN/com.liferay:com.liferay.login.web, MAVEN/com.liferay:com.liferay.login.authentication.openid.connect.web, MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 6.1) | 2022-05-17 |
| GHSA | [GHSA-GHSA-cm99-x97g-9qx8](https://github.com/advisories/GHSA-cm99-x97g-9qx8): Liferay Portal XSS Vulnerability (MAVEN/com.liferay:com.liferay.frontend.taglib, MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 6.1) | 2022-05-17 |
| GHSA | [GHSA-GHSA-x6rc-54xp-ccxx](https://github.com/advisories/GHSA-x6rc-54xp-ccxx): Withdrawn Advisory: Improper Restriction of XML External Entity Reference in Apache ActiveMQ (MAVEN/org.apache.activemq:activemq-client) | CRITICAL (CVSS: 9.8) | 2022-05-14 |
| GHSA | [GHSA-GHSA-w7f2-6896-6mm2](https://github.com/advisories/GHSA-w7f2-6896-6mm2): Liferay Portal and Liferay DXP allows arbitrary injection via web content template names (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom) | MODERATE (CVSS: 6.1) | 2022-04-26 |
| GHSA | [GHSA-GHSA-4gr7-qw2q-jxh6](https://github.com/advisories/GHSA-4gr7-qw2q-jxh6): Cross-site Scripting in Nacos (MAVEN/com.alibaba.nacos:nacos-common, MAVEN/com.alibaba.nacos:nacos-common) | MODERATE (CVSS: 6.1) | 2022-03-12 |
| GHSA | [GHSA-GHSA-2m53-83f3-562j](https://github.com/advisories/GHSA-2m53-83f3-562j): Prototype pollution in min-dash (MAVEN/org.webjars.npm:min-dash, NPM/min-dash) | HIGH (CVSS: 7.5) | 2022-02-01 |
| GHSA | [GHSA-GHSA-fm93-fhh2-cg2c](https://github.com/advisories/GHSA-fm93-fhh2-cg2c): Duplicate Advisory: Prototype Pollution in min-dash (NPM/min-dash) | HIGH (CVSS: 7.5) | 2022-01-27 |
| GHSA | [GHSA-GHSA-4r97-78gf-q24v](https://github.com/advisories/GHSA-4r97-78gf-q24v): Duplicate Advisory: Prototype Pollution in klona (NPM/klona) | HIGH (CVSS: 0.0) | 2020-09-04 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [4adb825](https://github.com/chromium/chromium/commit/4adb82512af566927fcda8574504324c27653f58) | Implement media playback trust check for the video PiP overlay window | 2025-07-18 |
| chromium/chromium | [eced63e](https://github.com/chromium/chromium/commit/eced63e3e85e6fab9f0545b7af943e271165d726) | Implement PictureInPictureInputProtector | 2025-07-18 |

