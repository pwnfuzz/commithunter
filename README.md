# Security Updates Monitor

*Last updated: 2025-08-08 15:16:32 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 14 |
| COMMIT | 3 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-rxp7-9q75-vj3p](https://github.com/advisories/GHSA-rxp7-9q75-vj3p): OpenBao Login MFA Bypass of Rate Limiting and TOTP Token Reuse (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | MODERATE (CVSS: 5.7) | 2025-08-08 |
| GHSA | [GHSA-GHSA-f7c3-mhj2-9pvg](https://github.com/advisories/GHSA-f7c3-mhj2-9pvg): OpenBao TOTP Secrets Engine Code Reuse (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | MODERATE (CVSS: 6.5) | 2025-08-08 |
| GHSA | [GHSA-GHSA-hh28-h22f-8357](https://github.com/advisories/GHSA-hh28-h22f-8357): OpenBao has a Timing Side-Channel in the Userpass Auth Method (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | LOW (CVSS: 3.7) | 2025-08-08 |
| GHSA | [GHSA-GHSA-j3xv-7fxp-gfhx](https://github.com/advisories/GHSA-j3xv-7fxp-gfhx): OpenBao Userpass and LDAP User Lockout Bypass (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | MODERATE (CVSS: 5.3) | 2025-08-08 |
| GHSA | [GHSA-GHSA-xp75-r577-cvhp](https://github.com/advisories/GHSA-xp75-r577-cvhp): Privileged OpenBao Operator May Execute Code on the Underlying Host (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | CRITICAL (CVSS: 9.1) | 2025-08-08 |
| GHSA | [GHSA-GHSA-vf84-mxrq-crqc](https://github.com/advisories/GHSA-vf84-mxrq-crqc): OpenBao Root Namespace Operator May Elevate Token Privileges (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | HIGH (CVSS: 7.2) | 2025-08-08 |
| GHSA | [GHSA-GHSA-6jcc-xgcr-q3h4](https://github.com/advisories/GHSA-6jcc-xgcr-q3h4): @fedify/fedify has Improper Authentication and Incorrect Authorization (NPM/@fedify/fedify, NPM/@fedify/fedify, NPM/@fedify/fedify) | HIGH (CVSS: 0.0) | 2025-08-08 |
| GHSA | [GHSA-GHSA-8qf3-x8v5-2pj8](https://github.com/advisories/GHSA-8qf3-x8v5-2pj8): uv allows ZIP payload obfuscation through parsing differentials (PIP/uv) | MODERATE (CVSS: 0.0) | 2025-08-07 |
| GHSA | [GHSA-GHSA-93jv-pvg8-hf3v](https://github.com/advisories/GHSA-93jv-pvg8-hf3v): Ollama allows deletion of arbitrary files (GO/github.com/ollama/ollama) | MODERATE (CVSS: 6.6) | 2025-08-07 |
| GHSA | [GHSA-GHSA-c7p4-hx26-pr73](https://github.com/advisories/GHSA-c7p4-hx26-pr73): JWE is missing AES-GCM authentication tag validation in encrypted JWE (RUBYGEMS/jwe) | CRITICAL (CVSS: 9.1) | 2025-08-07 |
| GHSA | [GHSA-GHSA-m3hh-f9gh-74c2](https://github.com/advisories/GHSA-m3hh-f9gh-74c2): quiche connection ID retirement can trigger an infinite loop (RUST/quiche) | HIGH (CVSS: 0.0) | 2025-08-07 |
| GHSA | [GHSA-GHSA-378x-6p4f-8jgm](https://github.com/advisories/GHSA-378x-6p4f-8jgm): SKOPS Card.get_model happily allows arbitrary code execution (PIP/skops) | HIGH (CVSS: 8.4) | 2025-08-07 |
| GHSA | [GHSA-GHSA-cq8c-xv66-36gw](https://github.com/advisories/GHSA-cq8c-xv66-36gw): Astros's duplicate trailing slash feature leads to an open redirection security issue (NPM/astro) | MODERATE (CVSS: 0.0) | 2025-08-07 |
| GHSA | [GHSA-GHSA-4mxg-3p6v-xgq3](https://github.com/advisories/GHSA-4mxg-3p6v-xgq3): Node-SAML SAML Signature Verification Vulnerability (NPM/@node-saml/passport-saml, NPM/passport-saml, NPM/@node-saml/node-saml) | CRITICAL (CVSS: 10.0) | 2025-07-28 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| postgres/postgres | [fd2ab03](https://github.com/postgres/postgres/commit/fd2ab03fea23ad6183fe694e750c901c6ff38479) | Fix incorrect lack of Datum conversion in _int_matchsel() | 2025-08-08 |
| chromium/chromium | [d61639d](https://github.com/chromium/chromium/commit/d61639d0fda4bf39eefd4e7d9dffb9dde09e029b) | Destroy device bound SessionService in ~URLRequestContext | 2025-08-07 |
| chromium/chromium | [52f3b74](https://github.com/chromium/chromium/commit/52f3b7419bc8892f011643006a1a075b5a7a9c82) | Reset DragDrop window observator to avoid UAF | 2025-08-07 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28184](https://github.com/openssl/openssl/pull/28184) | Fix integer overflow in date_to_julian() call | 2025-08-08 |

