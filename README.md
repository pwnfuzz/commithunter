# Security Updates Monitor

*Last updated: 2025-08-08 19:12:39 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 38 |
| COMMIT | 1 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-v3gr-w9gf-23cx](https://github.com/advisories/GHSA-v3gr-w9gf-23cx): The AuthKit Remix Library renders sensitive auth data in HTML (NPM/@workos-inc/authkit-remix) | HIGH (CVSS: 7.1) | 2025-08-08 |
| GHSA | [GHSA-GHSA-vqvc-9q8x-vmq6](https://github.com/advisories/GHSA-vqvc-9q8x-vmq6): The AuthKit React Router Library rendered sensitive auth data in HTML (NPM/@workos-inc/authkit-react-router) | HIGH (CVSS: 7.1) | 2025-08-08 |
| GHSA | [GHSA-GHSA-33r8-vrx9-rmcv](https://github.com/advisories/GHSA-33r8-vrx9-rmcv): ExecuTorch integer overflow vulnerability leads to code execution (PIP/executorch) | MODERATE (CVSS: 0.0) | 2025-08-08 |
| GHSA | [GHSA-GHSA-g358-g2pq-c46j](https://github.com/advisories/GHSA-g358-g2pq-c46j): Apache Seata: Deserialization of untrusted Data in Apache Seata Server (MAVEN/org.apache.seata:seata-serializer-fury) | HIGH (CVSS: 0.0) | 2025-08-08 |
| GHSA | [GHSA-GHSA-g4px-6qhm-hqjm](https://github.com/advisories/GHSA-g4px-6qhm-hqjm): Apache CXF: Untrusted JMS configuration can lead to RCE (MAVEN/org.apache.cxf:cxf-rt-transports-jms, MAVEN/org.apache.cxf:cxf-rt-transports-jms, MAVEN/org.apache.cxf:cxf-rt-transports-jms) | MODERATE (CVSS: 0.0) | 2025-08-08 |
| GHSA | [GHSA-GHSA-rxp7-9q75-vj3p](https://github.com/advisories/GHSA-rxp7-9q75-vj3p): OpenBao Login MFA Bypass of Rate Limiting and TOTP Token Reuse (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | MODERATE (CVSS: 5.7) | 2025-08-08 |
| GHSA | [GHSA-GHSA-f7c3-mhj2-9pvg](https://github.com/advisories/GHSA-f7c3-mhj2-9pvg): OpenBao TOTP Secrets Engine Code Reuse (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | MODERATE (CVSS: 6.5) | 2025-08-08 |
| GHSA | [GHSA-GHSA-hh28-h22f-8357](https://github.com/advisories/GHSA-hh28-h22f-8357): OpenBao has a Timing Side-Channel in the Userpass Auth Method (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | LOW (CVSS: 3.7) | 2025-08-08 |
| GHSA | [GHSA-GHSA-j3xv-7fxp-gfhx](https://github.com/advisories/GHSA-j3xv-7fxp-gfhx): OpenBao Userpass and LDAP User Lockout Bypass (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | MODERATE (CVSS: 5.3) | 2025-08-08 |
| GHSA | [GHSA-GHSA-xp75-r577-cvhp](https://github.com/advisories/GHSA-xp75-r577-cvhp): Privileged OpenBao Operator May Execute Code on the Underlying Host (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | CRITICAL (CVSS: 9.1) | 2025-08-08 |
| GHSA | [GHSA-GHSA-vf84-mxrq-crqc](https://github.com/advisories/GHSA-vf84-mxrq-crqc): OpenBao Root Namespace Operator May Elevate Token Privileges (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | HIGH (CVSS: 7.2) | 2025-08-08 |
| GHSA | [GHSA-GHSA-6jcc-xgcr-q3h4](https://github.com/advisories/GHSA-6jcc-xgcr-q3h4): @fedify/fedify has Improper Authentication and Incorrect Authorization (NPM/@fedify/fedify, NPM/@fedify/fedify, NPM/@fedify/fedify) | HIGH (CVSS: 0.0) | 2025-08-08 |
| GHSA | [GHSA-GHSA-c7p4-hx26-pr73](https://github.com/advisories/GHSA-c7p4-hx26-pr73): JWE is missing AES-GCM authentication tag validation in encrypted JWE (RUBYGEMS/jwe) | CRITICAL (CVSS: 9.1) | 2025-08-07 |
| GHSA | [GHSA-GHSA-378x-6p4f-8jgm](https://github.com/advisories/GHSA-378x-6p4f-8jgm): SKOPS Card.get_model happily allows arbitrary code execution (PIP/skops) | HIGH (CVSS: 8.4) | 2025-08-07 |
| GHSA | [GHSA-GHSA-cq8c-xv66-36gw](https://github.com/advisories/GHSA-cq8c-xv66-36gw): Astros's duplicate trailing slash feature leads to an open redirection security issue (NPM/astro) | MODERATE (CVSS: 0.0) | 2025-08-07 |
| GHSA | [GHSA-GHSA-8qf3-x8v5-2pj8](https://github.com/advisories/GHSA-8qf3-x8v5-2pj8): uv allows ZIP payload obfuscation through parsing differentials (PIP/uv) | MODERATE (CVSS: 0.0) | 2025-08-07 |
| GHSA | [GHSA-GHSA-93jv-pvg8-hf3v](https://github.com/advisories/GHSA-93jv-pvg8-hf3v): Ollama allows deletion of arbitrary files (GO/github.com/ollama/ollama) | MODERATE (CVSS: 6.6) | 2025-08-07 |
| GHSA | [GHSA-GHSA-m3hh-f9gh-74c2](https://github.com/advisories/GHSA-m3hh-f9gh-74c2): quiche connection ID retirement can trigger an infinite loop (RUST/quiche) | HIGH (CVSS: 0.0) | 2025-08-07 |
| GHSA | [GHSA-GHSA-4mxg-3p6v-xgq3](https://github.com/advisories/GHSA-4mxg-3p6v-xgq3): Node-SAML SAML Signature Verification Vulnerability (NPM/@node-saml/passport-saml, NPM/passport-saml, NPM/@node-saml/node-saml) | CRITICAL (CVSS: 10.0) | 2025-07-28 |
| GHSA | [GHSA-GHSA-25xr-qj8w-c4vf](https://github.com/advisories/GHSA-25xr-qj8w-c4vf): Apache Tomcat Coyote vulnerable to Denial of Service via excessive HTTP/2 streams (MAVEN/org.apache.tomcat:tomcat-coyote, MAVEN/org.apache.tomcat:tomcat-coyote, MAVEN/org.apache.tomcat:tomcat-coyote) | MODERATE (CVSS: 7.5) | 2025-07-10 |
| GHSA | [GHSA-GHSA-wr62-c79q-cv37](https://github.com/advisories/GHSA-wr62-c79q-cv37): Apache Tomcat Catalina is vulnerable to DoS attack through bypassing of size limits (MAVEN/org.apache.tomcat:tomcat-catalina, MAVEN/org.apache.tomcat:tomcat-catalina, MAVEN/org.apache.tomcat:tomcat-catalina) | MODERATE (CVSS: 7.5) | 2025-07-10 |
| GHSA | [GHSA-GHSA-4j3c-42xv-3f84](https://github.com/advisories/GHSA-4j3c-42xv-3f84): Apache Tomcat Utilities is vulnerable to resource exhaustion when using the APR/Native connector (MAVEN/org.apache.tomcat:tomcat-util, MAVEN/org.apache.tomcat:tomcat-util) | MODERATE (CVSS: 7.5) | 2025-07-10 |
| GHSA | [GHSA-GHSA-wc4r-xq3c-5cf3](https://github.com/advisories/GHSA-wc4r-xq3c-5cf3): Apache Tomcat - Security constraint bypass for pre/post-resources (MAVEN/org.apache.tomcat.embed:tomcat-embed-core, MAVEN/org.apache.tomcat:tomcat-catalina, MAVEN/org.apache.tomcat.embed:tomcat-embed-core) | MODERATE (CVSS: 0.0) | 2025-06-16 |
| GHSA | [GHSA-GHSA-h3gc-qfqq-6h8f](https://github.com/advisories/GHSA-h3gc-qfqq-6h8f): Apache Tomcat - DoS in multipart upload (MAVEN/org.apache.tomcat.embed:tomcat-embed-core, MAVEN/org.apache.tomcat:tomcat-catalina, MAVEN/org.apache.tomcat.embed:tomcat-embed-core) | HIGH (CVSS: 7.5) | 2025-06-16 |
| GHSA | [GHSA-GHSA-h2fw-rfh5-95r3](https://github.com/advisories/GHSA-h2fw-rfh5-95r3): Apache Tomcat - CGI security constraint bypass (MAVEN/org.apache.tomcat.embed:tomcat-embed-core, MAVEN/org.apache.tomcat:tomcat-catalina, MAVEN/org.apache.tomcat.embed:tomcat-embed-core) | LOW (CVSS: 0.0) | 2025-05-29 |
| GHSA | [GHSA-GHSA-ff77-26x5-69cr](https://github.com/advisories/GHSA-ff77-26x5-69cr): Apache Tomcat Rewrite rule bypass (MAVEN/org.apache.tomcat.embed:tomcat-embed-core, MAVEN/org.apache.tomcat:tomcat-catalina, MAVEN/org.apache.tomcat.embed:tomcat-embed-core) | LOW (CVSS: 0.0) | 2025-04-28 |
| GHSA | [GHSA-GHSA-3p2h-wqq4-wf4h](https://github.com/advisories/GHSA-3p2h-wqq4-wf4h): Apache Tomcat Denial of Service via invalid HTTP priority header (MAVEN/org.apache.tomcat.embed:tomcat-embed-core, MAVEN/org.apache.tomcat:tomcat-coyote, MAVEN/org.apache.tomcat.embed:tomcat-embed-core) | MODERATE (CVSS: 0.0) | 2025-04-28 |
| GHSA | [GHSA-GHSA-83qj-6fr2-vhqg](https://github.com/advisories/GHSA-83qj-6fr2-vhqg): Apache Tomcat: Potential RCE and/or information disclosure and/or information corruption with partial PUT (MAVEN/org.apache.tomcat.embed:tomcat-embed-core, MAVEN/org.apache.tomcat:tomcat-catalina, MAVEN/org.apache.tomcat.embed:tomcat-embed-core) | CRITICAL (CVSS: 9.8) | 2025-03-10 |
| GHSA | [GHSA-GHSA-653p-vg55-5652](https://github.com/advisories/GHSA-653p-vg55-5652): Apache Tomcat Uncontrolled Resource Consumption vulnerability (MAVEN/org.apache.tomcat:tomcat-catalina, MAVEN/org.apache.tomcat:tomcat-catalina, MAVEN/org.apache.tomcat:tomcat-catalina) | MODERATE (CVSS: 5.3) | 2024-12-17 |
| GHSA | [GHSA-GHSA-5j33-cvvr-w245](https://github.com/advisories/GHSA-5j33-cvvr-w245): Apache Tomcat Time-of-check Time-of-use (TOCTOU) Race Condition vulnerability (MAVEN/org.apache.tomcat.embed:tomcat-embed-core, MAVEN/org.apache.tomcat:tomcat-catalina, MAVEN/org.apache.tomcat.embed:tomcat-embed-core) | HIGH (CVSS: 9.8) | 2024-12-17 |
| GHSA | [GHSA-GHSA-xcpr-7mr4-h4xq](https://github.com/advisories/GHSA-xcpr-7mr4-h4xq): Apache Tomcat - Authentication Bypass (MAVEN/org.apache.tomcat:tomcat-catalina, MAVEN/org.apache.tomcat:tomcat-catalina, MAVEN/org.apache.tomcat:tomcat-catalina) | CRITICAL (CVSS: 9.8) | 2024-11-18 |
| GHSA | [GHSA-GHSA-7jqf-v358-p8g7](https://github.com/advisories/GHSA-7jqf-v358-p8g7): Apache Tomcat Allocation of Resources Without Limits or Throttling vulnerability (MAVEN/org.apache.tomcat:tomcat-util, MAVEN/org.apache.tomcat:tomcat-util, MAVEN/org.apache.tomcat:tomcat-util) | HIGH (CVSS: 8.6) | 2024-11-07 |
| GHSA | [GHSA-GHSA-wm9w-rjj3-j356](https://github.com/advisories/GHSA-wm9w-rjj3-j356): Apache Tomcat - Denial of Service (MAVEN/org.apache.tomcat.embed:tomcat-embed-core, MAVEN/org.apache.tomcat:tomcat-coyote, MAVEN/org.apache.tomcat:tomcat-coyote) | HIGH (CVSS: 7.5) | 2024-07-03 |
| GHSA | [GHSA-GHSA-v682-8vv8-vpwr](https://github.com/advisories/GHSA-v682-8vv8-vpwr): Denial of Service via incomplete cleanup vulnerability in Apache Tomcat (MAVEN/org.apache.tomcat.embed:tomcat-embed-websocket, MAVEN/org.apache.tomcat.embed:tomcat-embed-websocket, MAVEN/org.apache.tomcat.embed:tomcat-embed-websocket) | MODERATE (CVSS: 6.3) | 2024-03-13 |
| GHSA | [GHSA-GHSA-fccv-jmmp-qg76](https://github.com/advisories/GHSA-fccv-jmmp-qg76): Apache Tomcat Improper Input Validation vulnerability (MAVEN/org.apache.tomcat.embed:tomcat-embed-core, MAVEN/org.apache.tomcat.embed:tomcat-embed-core, MAVEN/org.apache.tomcat.embed:tomcat-embed-core) | HIGH (CVSS: 7.5) | 2023-11-28 |
| GHSA | [GHSA-GHSA-r6j3-px5g-cq3x](https://github.com/advisories/GHSA-r6j3-px5g-cq3x): Apache Tomcat Improper Input Validation vulnerability (MAVEN/org.apache.tomcat.embed:tomcat-embed-core, MAVEN/org.apache.tomcat.embed:tomcat-embed-core, MAVEN/org.apache.tomcat.embed:tomcat-embed-core) | MODERATE (CVSS: 5.3) | 2023-10-10 |
| GHSA | [GHSA-GHSA-g8pj-r55q-5c2v](https://github.com/advisories/GHSA-g8pj-r55q-5c2v): Apache Tomcat Incomplete Cleanup vulnerability (MAVEN/org.apache.tomcat:tomcat-coyote, MAVEN/org.apache.tomcat:tomcat-coyote, MAVEN/org.apache.tomcat.embed:tomcat-embed-core) | MODERATE (CVSS: 5.3) | 2023-10-10 |
| GHSA | [GHSA-GHSA-q3mw-pvr8-9ggc](https://github.com/advisories/GHSA-q3mw-pvr8-9ggc): Apache Tomcat Open Redirect vulnerability (MAVEN/org.apache.tomcat.embed:tomcat-embed-core, MAVEN/org.apache.tomcat.embed:tomcat-embed-core, MAVEN/org.apache.tomcat.embed:tomcat-embed-core) | MODERATE (CVSS: 6.1) | 2023-08-25 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| postgres/postgres | [fd2ab03](https://github.com/postgres/postgres/commit/fd2ab03fea23ad6183fe694e750c901c6ff38479) | Fix incorrect lack of Datum conversion in _int_matchsel() | 2025-08-08 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28184](https://github.com/openssl/openssl/pull/28184) | Fix integer overflow in date_to_julian() call | 2025-08-08 |

