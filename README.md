# Security Updates Monitor

*Last updated: 2025-09-03 18:19:28 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 21 |
| COMMIT | 2 |
| PR | 4 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-rrpj-r8h7-rm7r](https://github.com/advisories/GHSA-rrpj-r8h7-rm7r): Apache DolphinScheduler Incorrect Default Permissions Vulnerability (MAVEN/org.apache.dolphinscheduler:dolphinscheduler) | LOW (CVSS: 0.0) | 2025-09-03 |
| GHSA | [GHSA-GHSA-ph6w-f82w-28w6](https://github.com/advisories/GHSA-ph6w-f82w-28w6): Claude Code Vulnerable to Arbitrary Code Execution Due to Insufficient Startup Warning (NPM/@anthropic-ai/claude-code) | HIGH (CVSS: 0.0) | 2025-09-03 |
| GHSA | [GHSA-GHSA-x9gp-vjh6-3wv6](https://github.com/advisories/GHSA-x9gp-vjh6-3wv6): CKEditor 5 cross-site scripting (XSS) vulnerability in the clipboard package (NPM/@ckeditor/ckeditor5-clipboard, NPM/ckeditor5, NPM/@ckeditor/ckeditor5-clipboard) | LOW (CVSS: 0.0) | 2025-09-03 |
| GHSA | [GHSA-GHSA-3p8m-j85q-pgmj](https://github.com/advisories/GHSA-3p8m-j85q-pgmj): Netty's decoders vulnerable to DoS via zip bomb style attack (MAVEN/io.netty:netty-codec, MAVEN/io.netty:netty-codec-compression) | MODERATE (CVSS: 0.0) | 2025-09-03 |
| GHSA | [GHSA-GHSA-m63c-3rmg-r2cf](https://github.com/advisories/GHSA-m63c-3rmg-r2cf): XWiki configuration files can be accessed through jsx and sx endpoints (MAVEN/org.xwiki.platform:xwiki-platform-skin-skinx) | CRITICAL (CVSS: 0.0) | 2025-09-03 |
| GHSA | [GHSA-GHSA-qww7-89xh-x7m7](https://github.com/advisories/GHSA-qww7-89xh-x7m7): XWiki configuration files can be accessed through the webjars API (MAVEN/org.xwiki.platform:xwiki-platform-webjars-api) | CRITICAL (CVSS: 0.0) | 2025-09-03 |
| GHSA | [GHSA-GHSA-95h4-w6j8-2rp8](https://github.com/advisories/GHSA-95h4-w6j8-2rp8): Undertow MadeYouReset HTTP/2 DDoS Vulnerability (MAVEN/io.undertow:undertow-core) | HIGH (CVSS: 7.5) | 2025-09-02 |
| GHSA | [GHSA-GHSA-cv2m-5pfp-f245](https://github.com/advisories/GHSA-cv2m-5pfp-f245): Silverpeas Core Username Enumeration Vulnerability (MAVEN/org.silverpeas.core:silverpeas-core) | MODERATE (CVSS: 0.0) | 2025-09-02 |
| GHSA | [GHSA-GHSA-67mf-3cr5-8w23](https://github.com/advisories/GHSA-67mf-3cr5-8w23): Bouncy Castle for Java on All (API modules) allows Excessive Allocation (MAVEN/org.bouncycastle:bc-fips, MAVEN/org.bouncycastle:bc-fips, MAVEN/org.bouncycastle:bctls-jdk18on) | MODERATE (CVSS: 0.0) | 2025-08-12 |
| GHSA | [GHSA-GHSA-7qgg-vw88-cc99](https://github.com/advisories/GHSA-7qgg-vw88-cc99): utils-extend Prototype Pollution (NPM/utils-extend) | CRITICAL (CVSS: 9.1) | 2025-02-06 |
| GHSA | [GHSA-GHSA-mgfv-m47x-4wqp](https://github.com/advisories/GHSA-mgfv-m47x-4wqp): useragent Regular Expression Denial of Service vulnerability (NPM/useragent) | MODERATE (CVSS: 7.5) | 2024-10-26 |
| GHSA | [GHSA-GHSA-cqfh-c4c5-c2hg](https://github.com/advisories/GHSA-cqfh-c4c5-c2hg): domain-suffix RegEx Denial of Service (NPM/domain-suffix) | HIGH (CVSS: 7.5) | 2024-03-28 |
| GHSA | [GHSA-GHSA-9h6g-pr28-7cqp](https://github.com/advisories/GHSA-9h6g-pr28-7cqp): nodemailer ReDoS when trying to send a specially crafted email (NPM/nodemailer) | MODERATE (CVSS: 5.3) | 2024-01-31 |
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
| openssl/openssl | [eb851cc](https://github.com/openssl/openssl/commit/eb851cc1fb985edfcbeb5710bd671ab6db49bc2d) | apps/enc.c: avoid signed integer overflow on bufsize assignment | 2025-09-01 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| wazuh/wazuh | [#31674](https://github.com/wazuh/wazuh/pull/31674) | Remove deprecated VD tests | 2025-09-03 |
| wazuh/wazuh | [#31631](https://github.com/wazuh/wazuh/pull/31631) | Update cluster configuration | 2025-09-03 |
| langflow-ai/langflow | [#9441](https://github.com/langflow-ai/langflow/pull/9441) | fix: update CORS configuration and add env vars to allow for user control | 2025-09-03 |
| langflow-ai/langflow | [#9542](https://github.com/langflow-ai/langflow/pull/9542) | fix: superuser credential handling and AUTO_LOGIN security | 2025-09-02 |

