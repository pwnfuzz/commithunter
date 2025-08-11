# Security Updates Monitor

*Last updated: 2025-08-11 14:17:29 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 14 |
| COMMIT | 2 |
| PR | 4 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-rrgf-hcr9-jq6h](https://github.com/advisories/GHSA-rrgf-hcr9-jq6h): TinyScientist has Path Traversal Vulnerability in PDF Review Function (CWE-22) (PIP/tiny-scientist) | MODERATE (CVSS: 0.0) | 2025-08-11 |
| GHSA | [GHSA-GHSA-v3gr-w9gf-23cx](https://github.com/advisories/GHSA-v3gr-w9gf-23cx): The AuthKit Remix Library renders sensitive auth data in HTML (NPM/@workos-inc/authkit-remix) | HIGH (CVSS: 7.1) | 2025-08-08 |
| GHSA | [GHSA-GHSA-vqvc-9q8x-vmq6](https://github.com/advisories/GHSA-vqvc-9q8x-vmq6): The AuthKit React Router Library rendered sensitive auth data in HTML (NPM/@workos-inc/authkit-react-router) | HIGH (CVSS: 7.1) | 2025-08-08 |
| GHSA | [GHSA-GHSA-rxp7-9q75-vj3p](https://github.com/advisories/GHSA-rxp7-9q75-vj3p): OpenBao Login MFA Bypass of Rate Limiting and TOTP Token Reuse (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | MODERATE (CVSS: 5.7) | 2025-08-08 |
| GHSA | [GHSA-GHSA-2q8q-8fgw-9p6p](https://github.com/advisories/GHSA-2q8q-8fgw-9p6p): OpenBao LDAP MFA Enforcement Bypass When Using Username As Alias (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | MODERATE (CVSS: 6.5) | 2025-08-08 |
| GHSA | [GHSA-GHSA-f7c3-mhj2-9pvg](https://github.com/advisories/GHSA-f7c3-mhj2-9pvg): OpenBao TOTP Secrets Engine Code Reuse (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | MODERATE (CVSS: 6.5) | 2025-08-08 |
| GHSA | [GHSA-GHSA-hh28-h22f-8357](https://github.com/advisories/GHSA-hh28-h22f-8357): OpenBao has a Timing Side-Channel in the Userpass Auth Method (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | LOW (CVSS: 3.7) | 2025-08-08 |
| GHSA | [GHSA-GHSA-j3xv-7fxp-gfhx](https://github.com/advisories/GHSA-j3xv-7fxp-gfhx): OpenBao Userpass and LDAP User Lockout Bypass (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | MODERATE (CVSS: 5.3) | 2025-08-08 |
| GHSA | [GHSA-GHSA-xp75-r577-cvhp](https://github.com/advisories/GHSA-xp75-r577-cvhp): Privileged OpenBao Operator May Execute Code on the Underlying Host (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | CRITICAL (CVSS: 9.1) | 2025-08-08 |
| GHSA | [GHSA-GHSA-vf84-mxrq-crqc](https://github.com/advisories/GHSA-vf84-mxrq-crqc): OpenBao Root Namespace Operator May Elevate Token Privileges (GO/github.com/openbao/openbao, GO/github.com/openbao/openbao) | HIGH (CVSS: 7.2) | 2025-08-08 |
| GHSA | [GHSA-GHSA-6jcc-xgcr-q3h4](https://github.com/advisories/GHSA-6jcc-xgcr-q3h4): @fedify/fedify has Improper Authentication and Incorrect Authorization (NPM/@fedify/fedify, NPM/@fedify/fedify, NPM/@fedify/fedify) | HIGH (CVSS: 0.0) | 2025-08-08 |
| GHSA | [GHSA-GHSA-2vcf-qxv3-2mgw](https://github.com/advisories/GHSA-2vcf-qxv3-2mgw): Craft CMS has a theoretical bypass for CVE-2025-23209 (COMPOSER/craftcms/cms, COMPOSER/craftcms/cms) | MODERATE (CVSS: 0.0) | 2025-08-08 |
| GHSA | [GHSA-GHSA-75jv-vfxf-3865](https://github.com/advisories/GHSA-75jv-vfxf-3865): Assemblyline 4 service client vulnerable to Arbitrary Write through path traversal in Client code  (PIP/assemblyline-service-client, PIP/assemblyline-service-client) | CRITICAL (CVSS: 10.0) | 2025-07-25 |
| GHSA | [GHSA-GHSA-h4h6-vccr-44h2](https://github.com/advisories/GHSA-h4h6-vccr-44h2): uptrace pgdriver SQL injection vulnerability (GO/github.com/uptrace/bun/driver/pgdriver) | MODERATE (CVSS: 6.5) | 2025-06-12 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| postgres/postgres | [71ea0d6](https://github.com/postgres/postgres/commit/71ea0d6795438f95f4ee6e35867058c44b270d51) | Restrict psql meta-commands in plain-text dumps. | 2025-08-11 |
| postgres/postgres | [2242495](https://github.com/postgres/postgres/commit/22424953cded3f83f0382383773eaf36eb1abda9) | Fix security checks in selectivity estimation functions. | 2025-08-11 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28221](https://github.com/openssl/openssl/pull/28221) | Add missing NULL check in i2r_HASH | 2025-08-11 |
| erlang/otp | [#9946](https://github.com/erlang/otp/pull/9946) | chore(deps): update dependency microsoft/stl to v17.14 (maint) | 2025-08-11 |
| erlang/otp | [#9967](https://github.com/erlang/otp/pull/9967) | chore(deps): update dependency microsoft/stl to v17.14 (maint-28) | 2025-08-11 |
| erlang/otp | [#9918](https://github.com/erlang/otp/pull/9918) | chore(deps): update dependency microsoft/stl to v17.14 (master) | 2025-08-11 |

