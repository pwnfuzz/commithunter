# Security Updates Monitor

*Last updated: 2025-08-12 20:16:56 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 22 |
| COMMIT | 3 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-cg99-m88x-422c](https://github.com/advisories/GHSA-cg99-m88x-422c): Liferay Portal and Liferay DXP have a Denial Of Service via File Upload (DOS) vulnerability (MAVEN/com.liferay:com.liferay.account.admin.web, MAVEN/com.liferay:com.liferay.users.admin.web, MAVEN/com.liferay:com.liferay.image.uploader.web) | MODERATE (CVSS: 0.0) | 2025-08-12 |
| GHSA | [GHSA-GHSA-67mf-3cr5-8w23](https://github.com/advisories/GHSA-67mf-3cr5-8w23): Bouncy Castle for Java on All (API modules) allows Excessive Allocation (MAVEN/org.bouncycastle:bc-fips, MAVEN/org.bouncycastle:bctls-jdk18on, MAVEN/org.bouncycastle:bctls-jdk15to18) | MODERATE (CVSS: 0.0) | 2025-08-12 |
| GHSA | [GHSA-GHSA-c9rc-mg46-23w3](https://github.com/advisories/GHSA-c9rc-mg46-23w3): Keras vulnerable to CVE-2025-1550 bypass via reuse of internal functionality (PIP/keras) | HIGH (CVSS: 8.8) | 2025-08-12 |
| GHSA | [GHSA-GHSA-w2cq-g8g3-gm83](https://github.com/advisories/GHSA-w2cq-g8g3-gm83): content-security-policy-parser Prototype Pollution Vulnerability May Lead to RCE (NPM/content-security-policy-parser) | HIGH (CVSS: 0.0) | 2025-08-12 |
| GHSA | [GHSA-GHSA-pwh4-6r3m-j2rf](https://github.com/advisories/GHSA-pwh4-6r3m-j2rf): PyLoad vulnerable to SQL Injection via API /json/add_package in add_links parameter (PIP/pyload-ng) | HIGH (CVSS: 0.0) | 2025-08-12 |
| GHSA | [GHSA-GHSA-r3v7-pc4g-7xp9](https://github.com/advisories/GHSA-r3v7-pc4g-7xp9): Oak Server has ReDoS in x-forwarded-proto and x-forwarded-for headers (NPM/@oakserver/oak) | MODERATE (CVSS: 5.3) | 2025-08-12 |
| GHSA | [GHSA-GHSA-9gvj-pp9x-gcfr](https://github.com/advisories/GHSA-9gvj-pp9x-gcfr): Picklescan has pickle parsing logic flaw that leads to malicious pickle file bypass (PIP/picklescan) | HIGH (CVSS: 0.0) | 2025-08-12 |
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
| GHSA | [GHSA-GHSA-c6g5-g6r7-q4j6](https://github.com/advisories/GHSA-c6g5-g6r7-q4j6): Liferay Portal and Liferay DXP vulnerable to Server-Side Request Forgery (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom) | MODERATE (CVSS: 0.0) | 2025-08-09 |
| GHSA | [GHSA-GHSA-75jv-vfxf-3865](https://github.com/advisories/GHSA-75jv-vfxf-3865): Assemblyline 4 service client vulnerable to Arbitrary Write through path traversal in Client code  (PIP/assemblyline-service-client, PIP/assemblyline-service-client) | MODERATE (CVSS: 4.2) | 2025-07-25 |
| GHSA | [GHSA-GHSA-4j66-8f4r-3pjx](https://github.com/advisories/GHSA-4j66-8f4r-3pjx): Withdrawn Advisory: bun vulnerable to OS Command Injection (NPM/bun) | HIGH (CVSS: 8.8) | 2025-07-23 |

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

