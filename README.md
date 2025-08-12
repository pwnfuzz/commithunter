# Security Updates Monitor

*Last updated: 2025-08-12 11:13:29 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 18 |
| COMMIT | 1 |
| PR | 4 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-6ff3-jgxh-vffj](https://github.com/advisories/GHSA-6ff3-jgxh-vffj): Mattermost Confluence Plugin is Missing Authentication for Critical Function (GO/github.com/mattermost/mattermost-plugin-confluence) | HIGH (CVSS: 7.2) | 2025-08-11 |
| GHSA | [GHSA-GHSA-pwq7-2gvj-vg9v](https://github.com/advisories/GHSA-pwq7-2gvj-vg9v): Keras safe mode bypass vulnerability (PIP/keras) | HIGH (CVSS: 0.0) | 2025-08-11 |
| GHSA | [GHSA-GHSA-674p-xv2x-rf3g](https://github.com/advisories/GHSA-674p-xv2x-rf3g): Litestar has potential log injection in exception logging (PIP/litestar) | LOW (CVSS: 3.7) | 2025-08-11 |
| GHSA | [GHSA-GHSA-cmpr-8prq-w5p5](https://github.com/advisories/GHSA-cmpr-8prq-w5p5): Mattermost Confluence Plugin has Missing Authorization vulnerability (GO/github.com/mattermost/mattermost-plugin-confluence) | MODERATE (CVSS: 6.4) | 2025-08-11 |
| GHSA | [GHSA-GHSA-rfg4-2m63-fw2q](https://github.com/advisories/GHSA-rfg4-2m63-fw2q): Mattermost Confluence Plugin has Missing Authorization vulnerability (GO/github.com/mattermost/mattermost-plugin-confluence) | LOW (CVSS: 3.7) | 2025-08-11 |
| GHSA | [GHSA-GHSA-vpcr-fqpc-386h](https://github.com/advisories/GHSA-vpcr-fqpc-386h): Mattermost Confluence Plugin has Missing Authorization vulnerability (GO/github.com/mattermost/mattermost-plugin-confluence) | MODERATE (CVSS: 4.0) | 2025-08-11 |
| GHSA | [GHSA-GHSA-qx2v-8332-m4fv](https://github.com/advisories/GHSA-qx2v-8332-m4fv): slab allows out-of-bounds access in `get_disjoint_mut` due to incorrect bounds check (RUST/slab) | MODERATE (CVSS: 0.0) | 2025-08-11 |
| GHSA | [GHSA-GHSA-xwmg-2g98-w7v9](https://github.com/advisories/GHSA-xwmg-2g98-w7v9): Nimbus JOSE + JWT is vulnerable to DoS attacks when processing deeply nested JSON (MAVEN/com.nimbusds:nimbus-jose-jwt, MAVEN/com.nimbusds:nimbus-jose-jwt) | MODERATE (CVSS: 5.8) | 2025-07-11 |
| GHSA | [GHSA-GHSA-w5mx-334j-6fwv](https://github.com/advisories/GHSA-w5mx-334j-6fwv): Bagist Cross-site Scripting vulnerability (COMPOSER/bagisto/bagisto) | MODERATE (CVSS: 6.5) | 2024-03-01 |
| GHSA | [GHSA-GHSA-v642-mh27-8j6m](https://github.com/advisories/GHSA-v642-mh27-8j6m): MantisBT may disclose project names to unauthorized users  (COMPOSER/mantisbt/mantisbt) | MODERATE (CVSS: 4.3) | 2023-10-17 |
| GHSA | [GHSA-GHSA-29mw-wpgm-hmr9](https://github.com/advisories/GHSA-29mw-wpgm-hmr9): Regular Expression Denial of Service (ReDoS) in lodash (RUBYGEMS/lodash-rails, NPM/lodash.trim, NPM/lodash.trimend) | MODERATE (CVSS: 5.3) | 2022-01-06 |
| GHSA | [GHSA-GHSA-35jh-r3h4-6jhm](https://github.com/advisories/GHSA-35jh-r3h4-6jhm): Command Injection in lodash (RUBYGEMS/lodash-rails, NPM/lodash-template, NPM/lodash.template) | HIGH (CVSS: 7.2) | 2021-05-06 |
| GHSA | [GHSA-GHSA-p6mc-m468-83gw](https://github.com/advisories/GHSA-p6mc-m468-83gw): Prototype Pollution in lodash (RUBYGEMS/lodash-rails, NPM/lodash.updatewith, NPM/lodash.update) | HIGH (CVSS: 7.4) | 2020-07-15 |
| GHSA | [GHSA-GHSA-x5rq-j2xg-h7qm](https://github.com/advisories/GHSA-x5rq-j2xg-h7qm): Regular Expression Denial of Service (ReDoS) in lodash (RUBYGEMS/lodash-rails, NPM/lodash-amd, NPM/lodash-es) | MODERATE (CVSS: 0.0) | 2019-07-19 |
| GHSA | [GHSA-GHSA-jf85-cpcp-j695](https://github.com/advisories/GHSA-jf85-cpcp-j695): Prototype Pollution in lodash (RUBYGEMS/lodash-rails, NPM/lodash.defaultsdeep, NPM/lodash-amd) | CRITICAL (CVSS: 9.1) | 2019-07-10 |
| GHSA | [GHSA-GHSA-4xc9-xhrj-v574](https://github.com/advisories/GHSA-4xc9-xhrj-v574): Prototype Pollution in lodash (RUBYGEMS/lodash-rails, NPM/lodash) | HIGH (CVSS: 0.0) | 2019-02-07 |
| GHSA | [GHSA-GHSA-4q53-fqhc-cr46](https://github.com/advisories/GHSA-4q53-fqhc-cr46): ember-source Cross-site Scripting vulnerability (RUBYGEMS/ember-source, RUBYGEMS/ember-source, RUBYGEMS/ember-source) | LOW (CVSS: 0.0) | 2018-08-28 |
| GHSA | [GHSA-GHSA-fvqr-27wr-82fm](https://github.com/advisories/GHSA-fvqr-27wr-82fm): Prototype Pollution in lodash (RUBYGEMS/lodash-rails, NPM/lodash) | MODERATE (CVSS: 6.5) | 2018-07-26 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| postgres/postgres | [70693c6](https://github.com/postgres/postgres/commit/70693c645f6e490b9ed450e8611e94ab7af3aad2) | Convert newlines to spaces in names written in v11+ pg_dump comments. | 2025-08-11 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28184](https://github.com/openssl/openssl/pull/28184) | Fix integer overflow in date_to_julian() call | 2025-08-12 |
| erlang/otp | [#9960](https://github.com/erlang/otp/pull/9960) | chore(deps): update github-actions (maint-26) | 2025-08-11 |
| erlang/otp | [#9958](https://github.com/erlang/otp/pull/9958) | chore(deps): update github-actions (maint-27) | 2025-08-11 |
| erlang/otp | [#9956](https://github.com/erlang/otp/pull/9956) | chore(deps): update github-actions (maint-28) | 2025-08-11 |

