# Security Updates Monitor

*Last updated: 2025-08-14 16:20:01 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 13 |
| COMMIT | 5 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-f9f8-9pmf-xv68](https://github.com/advisories/GHSA-f9f8-9pmf-xv68): Helm May Panic Due To Incorrect YAML Content (GO/helm.sh/helm/v3) | MODERATE (CVSS: 6.5) | 2025-08-14 |
| GHSA | [GHSA-GHSA-9h84-qmv7-982p](https://github.com/advisories/GHSA-9h84-qmv7-982p): Helm Charts with Specific JSON Schema Values Can Cause Memory Exhaustion (GO/helm.sh/helm/v3) | MODERATE (CVSS: 6.5) | 2025-08-14 |
| GHSA | [GHSA-GHSA-r4mg-4433-c7g3](https://github.com/advisories/GHSA-r4mg-4433-c7g3): Active Storage allowed transformation methods that were potentially unsafe (RUBYGEMS/activestorage, RUBYGEMS/activestorage, RUBYGEMS/activestorage) | HIGH (CVSS: 0.0) | 2025-08-14 |
| GHSA | [GHSA-GHSA-7hfw-26vp-jp8m](https://github.com/advisories/GHSA-7hfw-26vp-jp8m): PyPDF's Manipulated FlateDecode streams can exhaust RAM (PIP/pypdf) | MODERATE (CVSS: 0.0) | 2025-08-13 |
| GHSA | [GHSA-GHSA-fcxq-v2r3-cc8h](https://github.com/advisories/GHSA-fcxq-v2r3-cc8h): External Secrets Operator's Missing Namespace Restriction Allows Unauthorized Secret Access (GO/github.com/external-secrets/external-secrets) | HIGH (CVSS: 0.0) | 2025-08-13 |
| GHSA | [GHSA-GHSA-p3qf-84rg-jxfc](https://github.com/advisories/GHSA-p3qf-84rg-jxfc): OliveTin OS Command Injection vulnerability (GO/github.com/OliveTin/OliveTin) | HIGH (CVSS: 6.5) | 2025-08-13 |
| GHSA | [GHSA-GHSA-xvr7-p2c6-j83w](https://github.com/advisories/GHSA-xvr7-p2c6-j83w): swift-nio-http2 affected by HTTP/2 MadeYouReset vulnerability (SWIFT/github.com/apple/swift-nio-http2) | MODERATE (CVSS: 0.0) | 2025-08-13 |
| GHSA | [GHSA-GHSA-23hv-mwm6-g8jf](https://github.com/advisories/GHSA-23hv-mwm6-g8jf): Apache Tomcat Session Fixation vulnerability (MAVEN/org.apache.tomcat:tomcat-catalina, MAVEN/org.apache.tomcat:tomcat-catalina, MAVEN/org.apache.tomcat:tomcat-catalina) | MODERATE (CVSS: 6.5) | 2025-08-13 |
| GHSA | [GHSA-GHSA-m5c7-5gv3-hcpf](https://github.com/advisories/GHSA-m5c7-5gv3-hcpf): Liferay Portal 7.4.0 and Liferay DXP have a reflected cross-site scripting (XSS) vulnerability (MAVEN/com.liferay:com.liferay.frontend.taglib.clay, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom) | MODERATE (CVSS: 0.0) | 2025-08-12 |
| GHSA | [GHSA-GHSA-h45x-qhg2-q375](https://github.com/advisories/GHSA-h45x-qhg2-q375): OpenEXR Heap-Based Buffer Overflow in Deep Scanline Parsing via Forged Unpacked Size (PIP/OpenEXR) | HIGH (CVSS: 7.8) | 2025-07-31 |
| GHSA | [GHSA-GHSA-39p2-8hq9-fwj6](https://github.com/advisories/GHSA-39p2-8hq9-fwj6): GitProxy New Branch Approval Exploit (NPM/@finos/git-proxy) | HIGH (CVSS: 0.0) | 2025-07-30 |
| GHSA | [GHSA-GHSA-6xp3-p59p-q4fj](https://github.com/advisories/GHSA-6xp3-p59p-q4fj): go-pg SQL injection vulnerability via the component /types/append_value.go (GO/github.com/go-pg/pg/v10, GO/github.com/go-pg/pg, GO/github.com/go-pg/pg/v9) | MODERATE (CVSS: 6.5) | 2025-06-12 |
| GHSA | [GHSA-GHSA-mq69-4j5w-3qwp](https://github.com/advisories/GHSA-mq69-4j5w-3qwp): Capsule tenant owner with "patch namespace" permission can hijack system namespaces (GO/github.com/projectcapsule/capsule) | HIGH (CVSS: 8.5) | 2024-08-20 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [c28d28a](https://github.com/torvalds/linux/commit/c28d28a7b005dd6459a6059dc7eff684bf0b7464) | Merge tag 'pm-6.17-rc2' of git://git.kernel.org/pub/scm/linux/kernel/git/rafael/linux-pm | 2025-08-14 |
| torvalds/linux | [5302e2a](https://github.com/torvalds/linux/commit/5302e2a3886c830b803ae3390b9d41d35832f315) | Merge branches 'pm-cpuidle' and 'pm-cpufreq' | 2025-08-14 |
| chromium/chromium | [50a503e](https://github.com/chromium/chromium/commit/50a503e398c1ab58d003f447cb4da6336ad14d8d) | Enforcing DiceWebSigninInterceptor not to listen to IM on Interception | 2025-08-14 |
| torvalds/linux | [87c6efc](https://github.com/torvalds/linux/commit/87c6efc5ce9c126ae4a781bc04504b83780e3650) | net/sched: ets: use old 'nbands' while purging unused classes | 2025-08-12 |
| torvalds/linux | [4faff70](https://github.com/torvalds/linux/commit/4faff70959d51078f9ee8372f8cff0d7045e4114) | net: usb: asix_devices: add phy_mask for ax88772 mdio bus | 2025-08-11 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28259](https://github.com/openssl/openssl/pull/28259) | Fix potential null pointer dereference in pkey_dh_derive | 2025-08-14 |

