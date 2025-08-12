# Security Updates Monitor

*Last updated: 2025-08-12 01:11:36 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 33 |
| COMMIT | 2 |
| PR | 4 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-r3v7-pc4g-7xp9](https://github.com/advisories/GHSA-r3v7-pc4g-7xp9): Oak Server has ReDoS in x-forwarded-proto and x-forwarded-for headers (NPM/@oakserver/oak) | MODERATE (CVSS: 5.3) | 2025-08-12 |
| GHSA | [GHSA-GHSA-9gvj-pp9x-gcfr](https://github.com/advisories/GHSA-9gvj-pp9x-gcfr): Picklescan has pickle parsing logic flaw that leads to malicious pickle file bypass (PIP/picklescan) | HIGH (CVSS: 0.0) | 2025-08-12 |
| GHSA | [GHSA-GHSA-pwh4-6r3m-j2rf](https://github.com/advisories/GHSA-pwh4-6r3m-j2rf): PyLoad vulnerable to SQL Injection via API /json/add_package in add_links parameter (PIP/pyload-ng) | HIGH (CVSS: 0.0) | 2025-08-12 |
| GHSA | [GHSA-GHSA-jhmr-57cj-q6g9](https://github.com/advisories/GHSA-jhmr-57cj-q6g9): Komari vulnerable to 2FA Authentication Bypass (GO/github.com/komari-monitor/komari) | HIGH (CVSS: 0.0) | 2025-08-12 |
| GHSA | [GHSA-GHSA-q355-h244-969h](https://github.com/advisories/GHSA-q355-h244-969h): Komari vulnerable to Cross-site WebSocket Hijacking (GO/github.com/komari-monitor/komari) | HIGH (CVSS: 0.0) | 2025-08-12 |
| GHSA | [GHSA-GHSA-xcxh-6cv4-q8p8](https://github.com/advisories/GHSA-xcxh-6cv4-q8p8): HFS user adding a "web link" in HFS is vulnerable to "target=_blank" exploit (NPM/hfs) | LOW (CVSS: 0.0) | 2025-08-12 |
| GHSA | [GHSA-GHSA-qpjq-c5hr-7925](https://github.com/advisories/GHSA-qpjq-c5hr-7925): Mattermost Confluence Plugin is Missing Authentication for Critical Function (GO/github.com/mattermost/mattermost-plugin-confluence) | HIGH (CVSS: 7.2) | 2025-08-11 |
| GHSA | [GHSA-GHSA-3cg3-3mmr-w8hj](https://github.com/advisories/GHSA-3cg3-3mmr-w8hj): Mattermost Confluence Plugin has Improper Validation of Specified Type of Input (GO/github.com/mattermost/mattermost-plugin-confluence) | HIGH (CVSS: 7.5) | 2025-08-11 |
| GHSA | [GHSA-GHSA-gjpm-6w34-ppvf](https://github.com/advisories/GHSA-gjpm-6w34-ppvf): Mattermost Confluence Plugin has Improper Check for Unusual or Exceptional Conditions (GO/github.com/mattermost/mattermost-plugin-confluence) | MODERATE (CVSS: 5.9) | 2025-08-11 |
| GHSA | [GHSA-GHSA-j66h-xhpr-7q5g](https://github.com/advisories/GHSA-j66h-xhpr-7q5g): Mattermost Confluence Plugin has Missing Authorization vulnerability (GO/github.com/mattermost/mattermost-plugin-confluence) | MODERATE (CVSS: 5.0) | 2025-08-11 |
| GHSA | [GHSA-GHSA-v6c8-g53h-mc2h](https://github.com/advisories/GHSA-v6c8-g53h-mc2h): Mattermost Confluence Plugin has Missing Authorization vulnerability (GO/github.com/mattermost/mattermost-plugin-confluence) | MODERATE (CVSS: 4.0) | 2025-08-11 |
| GHSA | [GHSA-GHSA-42m6-5vm7-fjv2](https://github.com/advisories/GHSA-42m6-5vm7-fjv2): Mattermost Confluence Plugin has Missing Authorization vulnerability (GO/github.com/mattermost/mattermost-plugin-confluence) | LOW (CVSS: 3.7) | 2025-08-11 |
| GHSA | [GHSA-GHSA-w92j-c6gr-hj8r](https://github.com/advisories/GHSA-w92j-c6gr-hj8r): Mattermost Confluence Plugin has Improper Check for Unusual or Exceptional Conditions (GO/github.com/mattermost/mattermost-plugin-confluence) | MODERATE (CVSS: 5.9) | 2025-08-11 |
| GHSA | [GHSA-GHSA-vc77-c2hx-h5x2](https://github.com/advisories/GHSA-vc77-c2hx-h5x2): Mattermost Confluence Plugin has Improper Check for Unusual or Exceptional Conditions (GO/github.com/mattermost/mattermost-plugin-confluence) | HIGH (CVSS: 7.5) | 2025-08-11 |
| GHSA | [GHSA-GHSA-qjrx-j8wm-xf83](https://github.com/advisories/GHSA-qjrx-j8wm-xf83): Mattermost Confluence Plugin has Missing Authorization vulnerability (GO/github.com/mattermost/mattermost-plugin-confluence) | MODERATE (CVSS: 4.0) | 2025-08-11 |
| GHSA | [GHSA-GHSA-rrgf-hcr9-jq6h](https://github.com/advisories/GHSA-rrgf-hcr9-jq6h): TinyScientist has Path Traversal Vulnerability in PDF Review Function (CWE-22) (PIP/tiny-scientist) | MODERATE (CVSS: 0.0) | 2025-08-11 |
| GHSA | [GHSA-GHSA-c6g5-g6r7-q4j6](https://github.com/advisories/GHSA-c6g5-g6r7-q4j6): Liferay Portal and Liferay DXP vulnerable to Server-Side Request Forgery (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom) | MODERATE (CVSS: 0.0) | 2025-08-09 |
| GHSA | [GHSA-GHSA-6v93-frf9-2rp8](https://github.com/advisories/GHSA-6v93-frf9-2rp8): Liferay Portal and Liferay DXP vulnerable to Server-Side Request Forgery (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom) | MODERATE (CVSS: 0.0) | 2025-08-09 |
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
| GHSA | [GHSA-GHSA-4j66-8f4r-3pjx](https://github.com/advisories/GHSA-4j66-8f4r-3pjx): Withdrawn Advisory: bun vulnerable to OS Command Injection (NPM/bun) | HIGH (CVSS: 8.8) | 2025-07-23 |
| GHSA | [GHSA-GHSA-h4h6-vccr-44h2](https://github.com/advisories/GHSA-h4h6-vccr-44h2): uptrace pgdriver SQL injection vulnerability (GO/github.com/uptrace/bun/driver/pgdriver) | MODERATE (CVSS: 6.5) | 2025-06-12 |
| GHSA | [GHSA-GHSA-m8p2-495h-ccmh](https://github.com/advisories/GHSA-m8p2-495h-ccmh): The SafeHtml annotation in Hibernate-Validator does not properly guard against XSS attacks (MAVEN/org.hibernate.validator:hibernate-validator, MAVEN/org.hibernate.validator:hibernate-validator) | MODERATE (CVSS: 6.5) | 2020-01-08 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| postgres/postgres | [71ea0d6](https://github.com/postgres/postgres/commit/71ea0d6795438f95f4ee6e35867058c44b270d51) | Restrict psql meta-commands in plain-text dumps. | 2025-08-11 |
| postgres/postgres | [2242495](https://github.com/postgres/postgres/commit/22424953cded3f83f0382383773eaf36eb1abda9) | Fix security checks in selectivity estimation functions. | 2025-08-11 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28221](https://github.com/openssl/openssl/pull/28221) | Add missing NULL check in i2r_HASH | 2025-08-12 |
| erlang/otp | [#9946](https://github.com/erlang/otp/pull/9946) | chore(deps): update dependency microsoft/stl to v17.14 (maint) | 2025-08-11 |
| erlang/otp | [#9967](https://github.com/erlang/otp/pull/9967) | chore(deps): update dependency microsoft/stl to v17.14 (maint-28) | 2025-08-11 |
| erlang/otp | [#9918](https://github.com/erlang/otp/pull/9918) | chore(deps): update dependency microsoft/stl to v17.14 (master) | 2025-08-11 |

