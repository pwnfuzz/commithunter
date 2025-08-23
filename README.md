# Security Updates Monitor

*Last updated: 2025-08-23 11:10:40 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 5 |
| COMMIT | 3 |
| PR | 3 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-655h-hg88-5qmf](https://github.com/advisories/GHSA-655h-hg88-5qmf): Rust XCB `xcb::Connection::connect_to_fd*` functions violate I/O safety (RUST/xcb) | LOW (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-h469-4fcf-p23h](https://github.com/advisories/GHSA-h469-4fcf-p23h): Mattermost has Potential Server Crash due to Unvalidated Import Data (GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server) | MODERATE (CVSS: 4.9) | 2025-08-21 |
| GHSA | [GHSA-GHSA-w2wj-hw98-233h](https://github.com/advisories/GHSA-w2wj-hw98-233h): Keycloak Potential Variable Reference in Model Storage Services (MAVEN/org.keycloak:keycloak-model-storage-services) | MODERATE (CVSS: 4.9) | 2025-08-21 |
| GHSA | [GHSA-GHSA-9gjj-6gj7-c4wj](https://github.com/advisories/GHSA-9gjj-6gj7-c4wj): Denial-of-Service attack in pyLoad CNL Blueprint using dukpy.evaljs (PIP/pyload-ng) | HIGH (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-xqrq-4mgf-ff32](https://github.com/advisories/GHSA-xqrq-4mgf-ff32): Python-Future Module Arbitrary Code Execution via Unintended Import of test.py (PIP/future) | HIGH (CVSS: 0.0) | 2025-08-14 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [edeee68](https://github.com/torvalds/linux/commit/edeee68c42747c9d9b237f06fbc4cd1a2348fefb) | Merge tag 'scsi-fixes' of git://git.kernel.org/pub/scm/linux/kernel/git/jejb/scsi | 2025-08-22 |
| torvalds/linux | [c37d2bc](https://github.com/torvalds/linux/commit/c37d2bc92b90ef4df898d1aa7a3ffed34e4043b8) | Merge tag 'iommu-fixes-v6.17-rc2' of git://git.kernel.org/pub/scm/linux/kernel/git/iommu/linux | 2025-08-22 |
| openssl/openssl | [fc84d46](https://github.com/openssl/openssl/commit/fc84d46d7227886152be00618889a521e9132ef3) | Fix null pointer check in pkey_dh_derive to ensure both keys are set | 2025-08-13 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28259](https://github.com/openssl/openssl/pull/28259) | Fix potential null pointer dereference in pkey_dh_derive | 2025-08-22 |
| wazuh/wazuh | [#31511](https://github.com/wazuh/wazuh/pull/31511) | Fix literal parser dangling std::string_view capture, and add regression test | 2025-08-22 |
| hibernate/hibernate-validator | [#1682](https://github.com/hibernate/hibernate-validator/pull/1682) | Bump org.glassfish:jakarta.el from 3.0.3 to 3.0.4 in /performance | 2025-08-22 |

