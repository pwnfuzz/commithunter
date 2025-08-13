# Security Updates Monitor

*Last updated: 2025-08-13 04:25:50 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 15 |
| COMMIT | 3 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-xcxh-6cv4-q8p8](https://github.com/advisories/GHSA-xcxh-6cv4-q8p8): HFS user adding a "web link" in HFS is vulnerable to "target=_blank" exploit (NPM/hfs) | LOW (CVSS: 0.0) | 2025-08-12 |
| GHSA | [GHSA-GHSA-cg99-m88x-422c](https://github.com/advisories/GHSA-cg99-m88x-422c): Liferay Portal and Liferay DXP have a Denial Of Service via File Upload (DOS) vulnerability (MAVEN/com.liferay:com.liferay.account.admin.web, MAVEN/com.liferay:com.liferay.users.admin.web, MAVEN/com.liferay:com.liferay.image.uploader.web) | MODERATE (CVSS: 0.0) | 2025-08-12 |
| GHSA | [GHSA-GHSA-67mf-3cr5-8w23](https://github.com/advisories/GHSA-67mf-3cr5-8w23): Bouncy Castle for Java on All (API modules) allows Excessive Allocation (MAVEN/org.bouncycastle:bc-fips, MAVEN/org.bouncycastle:bctls-jdk18on, MAVEN/org.bouncycastle:bctls-jdk15to18) | MODERATE (CVSS: 0.0) | 2025-08-12 |
| GHSA | [GHSA-GHSA-c9rc-mg46-23w3](https://github.com/advisories/GHSA-c9rc-mg46-23w3): Keras vulnerable to CVE-2025-1550 bypass via reuse of internal functionality (PIP/keras) | HIGH (CVSS: 8.8) | 2025-08-12 |
| GHSA | [GHSA-GHSA-w2cq-g8g3-gm83](https://github.com/advisories/GHSA-w2cq-g8g3-gm83): content-security-policy-parser Prototype Pollution Vulnerability May Lead to RCE (NPM/content-security-policy-parser) | HIGH (CVSS: 0.0) | 2025-08-12 |
| GHSA | [GHSA-GHSA-pwh4-6r3m-j2rf](https://github.com/advisories/GHSA-pwh4-6r3m-j2rf): PyLoad vulnerable to SQL Injection via API /json/add_package in add_links parameter (PIP/pyload-ng) | HIGH (CVSS: 0.0) | 2025-08-12 |
| GHSA | [GHSA-GHSA-75jv-vfxf-3865](https://github.com/advisories/GHSA-75jv-vfxf-3865): Assemblyline 4 service client vulnerable to Arbitrary Write through path traversal in Client code  (PIP/assemblyline-service-client, PIP/assemblyline-service-client) | MODERATE (CVSS: 4.2) | 2025-07-25 |
| GHSA | [GHSA-GHSA-xcj6-4355-2823](https://github.com/advisories/GHSA-xcj6-4355-2823): Jenkins Mattermost Notification Plugin contains unencrypted storage of secret token (MAVEN/org.jenkins-ci.plugins:mattermost) | MODERATE (CVSS: 6.5) | 2022-05-24 |
| GHSA | [GHSA-GHSA-29mw-wpgm-hmr9](https://github.com/advisories/GHSA-29mw-wpgm-hmr9): Regular Expression Denial of Service (ReDoS) in lodash (RUBYGEMS/lodash-rails, NPM/lodash.trim, NPM/lodash.trimend) | MODERATE (CVSS: 5.3) | 2022-01-06 |
| GHSA | [GHSA-GHSA-35jh-r3h4-6jhm](https://github.com/advisories/GHSA-35jh-r3h4-6jhm): Command Injection in lodash (RUBYGEMS/lodash-rails, NPM/lodash-template, NPM/lodash.template) | HIGH (CVSS: 7.2) | 2021-05-06 |
| GHSA | [GHSA-GHSA-p6mc-m468-83gw](https://github.com/advisories/GHSA-p6mc-m468-83gw): Prototype Pollution in lodash (RUBYGEMS/lodash-rails, NPM/lodash.updatewith, NPM/lodash.update) | HIGH (CVSS: 7.4) | 2020-07-15 |
| GHSA | [GHSA-GHSA-x5rq-j2xg-h7qm](https://github.com/advisories/GHSA-x5rq-j2xg-h7qm): Regular Expression Denial of Service (ReDoS) in lodash (RUBYGEMS/lodash-rails, NPM/lodash-amd, NPM/lodash-es) | MODERATE (CVSS: 0.0) | 2019-07-19 |
| GHSA | [GHSA-GHSA-jf85-cpcp-j695](https://github.com/advisories/GHSA-jf85-cpcp-j695): Prototype Pollution in lodash (RUBYGEMS/lodash-rails, NPM/lodash.defaultsdeep, NPM/lodash-amd) | CRITICAL (CVSS: 9.1) | 2019-07-10 |
| GHSA | [GHSA-GHSA-4xc9-xhrj-v574](https://github.com/advisories/GHSA-4xc9-xhrj-v574): Prototype Pollution in lodash (RUBYGEMS/lodash-rails, NPM/lodash) | HIGH (CVSS: 0.0) | 2019-02-07 |
| GHSA | [GHSA-GHSA-fvqr-27wr-82fm](https://github.com/advisories/GHSA-fvqr-27wr-82fm): Prototype Pollution in lodash (RUBYGEMS/lodash-rails, NPM/lodash) | MODERATE (CVSS: 6.5) | 2018-07-26 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [8742b2d](https://github.com/torvalds/linux/commit/8742b2d8935f476449ef37e263bc4da3295c7b58) | Merge tag 'pull-fixes' of git://git.kernel.org/pub/scm/linux/kernel/git/viro/vfs | 2025-08-12 |
| torvalds/linux | [20e0d85](https://github.com/torvalds/linux/commit/20e0d8576484c60c8c0c9d5d6665541c37dee327) | Merge tag 'snp_cache_coherency' of git://git.kernel.org/pub/scm/linux/kernel/git/tip/tip | 2025-08-12 |
| chromium/chromium | [2478573](https://github.com/chromium/chromium/commit/2478573045176f22c8997baf386c1ff3c4b9cf76) | a11y: Use ScopedObservation for SettingsWithTtsPreviewHandler | 2025-08-12 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28221](https://github.com/openssl/openssl/pull/28221) | Add missing NULL check in i2r_HASH | 2025-08-12 |

