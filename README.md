# Security Updates Monitor

*Last updated: 2025-09-03 06:20:27 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 15 |
| COMMIT | 1 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-95h4-w6j8-2rp8](https://github.com/advisories/GHSA-95h4-w6j8-2rp8): Undertow MadeYouReset HTTP/2 DDoS Vulnerability (MAVEN/io.undertow:undertow-core) | HIGH (CVSS: 7.5) | 2025-09-02 |
| GHSA | [GHSA-GHSA-cv2m-5pfp-f245](https://github.com/advisories/GHSA-cv2m-5pfp-f245): Silverpeas Core Username Enumeration Vulnerability (MAVEN/org.silverpeas.core:silverpeas-core) | MODERATE (CVSS: 0.0) | 2025-09-02 |
| GHSA | [GHSA-GHSA-fqqv-56h5-f57g](https://github.com/advisories/GHSA-fqqv-56h5-f57g): PocketMine-MP `ResourcePackDataInfoPacket` amplification vulnerability due to lack of resource pack sequence status checking (COMPOSER/pocketmine/pocketmine-mp) | HIGH (CVSS: 0.0) | 2025-09-02 |
| GHSA | [GHSA-GHSA-mxh2-ccgj-8635](https://github.com/advisories/GHSA-mxh2-ccgj-8635): ESP-IDF web_server basic auth bypass using empty or incomplete Authorization header (PIP/esphome) | HIGH (CVSS: 8.1) | 2025-09-02 |
| GHSA | [GHSA-GHSA-4h8c-qrcq-cv5c](https://github.com/advisories/GHSA-4h8c-qrcq-cv5c): Local Deep Research's API keys are stored in plain text (PIP/local-deep-research) | MODERATE (CVSS: 0.0) | 2025-09-02 |
| GHSA | [GHSA-GHSA-67mf-3cr5-8w23](https://github.com/advisories/GHSA-67mf-3cr5-8w23): Bouncy Castle for Java on All (API modules) allows Excessive Allocation (MAVEN/org.bouncycastle:bc-fips, MAVEN/org.bouncycastle:bc-fips, MAVEN/org.bouncycastle:bctls-jdk18on) | MODERATE (CVSS: 0.0) | 2025-08-12 |
| GHSA | [GHSA-GHSA-735f-pc8j-v9w8](https://github.com/advisories/GHSA-735f-pc8j-v9w8): protobuf-java has potential Denial of Service issue (MAVEN/com.google.protobuf:protobuf-java, MAVEN/com.google.protobuf:protobuf-java, MAVEN/com.google.protobuf:protobuf-javalite) | HIGH (CVSS: 7.5) | 2024-09-19 |
| GHSA | [GHSA-GHSA-vp98-w2p3-mv35](https://github.com/advisories/GHSA-vp98-w2p3-mv35): Apache Log4j 1.x (EOL) allows Denial of Service (DoS) (MAVEN/log4j:log4j, MAVEN/org.apache.logging.log4j:log4j-core) | HIGH (CVSS: 7.5) | 2023-03-10 |
| GHSA | [GHSA-GHSA-rpjm-422r-95mh](https://github.com/advisories/GHSA-rpjm-422r-95mh): Regular expression denial of service in apache tika (MAVEN/org.apache.tika:tika-core, MAVEN/org.apache.tika:tika-core) | MODERATE (CVSS: 5.5) | 2022-05-17 |
| GHSA | [GHSA-GHSA-xjgh-84hx-56c5](https://github.com/advisories/GHSA-xjgh-84hx-56c5): Unrestricted Upload of File with Dangerous Type Apache Tomcat (MAVEN/org.apache.tomcat.embed:tomcat-embed-core, MAVEN/org.apache.tomcat.embed:tomcat-embed-core, MAVEN/org.apache.tomcat.embed:tomcat-embed-core) | HIGH (CVSS: 8.1) | 2022-05-14 |
| GHSA | [GHSA-GHSA-w3j5-q8f2-3cqq](https://github.com/advisories/GHSA-w3j5-q8f2-3cqq): Concurrent Execution using Shared Resource with Improper Synchronization in Apache Tomcat (MAVEN/org.apache.tomcat:tomcat-util, MAVEN/org.apache.tomcat:tomcat-util, MAVEN/org.apache.tomcat:tomcat-util) | HIGH (CVSS: 7.5) | 2022-05-14 |
| GHSA | [GHSA-GHSA-jwwr-fjgh-cv2x](https://github.com/advisories/GHSA-jwwr-fjgh-cv2x): Improper Restriction of XML External Entity Reference in Castor (MAVEN/org.castor:castor, MAVEN/org.codehaus.castor:castor) | MODERATE (CVSS: 0.0) | 2022-05-13 |
| GHSA | [GHSA-GHSA-cr3q-pqgq-m8c2](https://github.com/advisories/GHSA-cr3q-pqgq-m8c2): Spoofing attack in swagger-ui (MAVEN/org.webjars:swagger-ui, NPM/swagger-ui) | MODERATE (CVSS: 4.3) | 2022-03-12 |
| GHSA | [GHSA-GHSA-qcj7-g2j5-g7r3](https://github.com/advisories/GHSA-qcj7-g2j5-g7r3): In Bouncy Castle JCE Provider ECDSA does not fully validate ASN.1 encoding of signature on verification (MAVEN/org.bouncycastle:bcprov-jdk15on, MAVEN/org.bouncycastle:bcprov-jdk15, MAVEN/org.bouncycastle:bcprov-jdk14) | HIGH (CVSS: 7.5) | 2018-10-17 |
| GHSA | [GHSA-GHSA-mhpp-875w-9cpv](https://github.com/advisories/GHSA-mhpp-875w-9cpv): Denial of Service in jquery (MAVEN/org.webjars.npm:jquery, RUBYGEMS/jquery-rails, NUGET/jQuery) | HIGH (CVSS: 7.5) | 2018-01-22 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [8026aed](https://github.com/torvalds/linux/commit/8026aed072e1221f0a61e5acc48c64546341bd4d) | Merge tag 'mm-hotfixes-stable-2025-09-01-17-20' of git://git.kernel.org/pub/scm/linux/kernel/git/akpm/mm | 2025-09-02 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| langflow-ai/langflow | [#9542](https://github.com/langflow-ai/langflow/pull/9542) | fix: superuser credential handling and AUTO_LOGIN security | 2025-09-02 |

