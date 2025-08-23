# Security Updates Monitor

*Last updated: 2025-08-23 15:12:17 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 4 |
| COMMIT | 3 |
| PR | 3 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-655h-hg88-5qmf](https://github.com/advisories/GHSA-655h-hg88-5qmf): Rust XCB `xcb::Connection::connect_to_fd*` functions violate I/O safety (RUST/xcb) | LOW (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-h469-4fcf-p23h](https://github.com/advisories/GHSA-h469-4fcf-p23h): Mattermost has Potential Server Crash due to Unvalidated Import Data (GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server) | MODERATE (CVSS: 4.9) | 2025-08-21 |
| GHSA | [GHSA-GHSA-w2wj-hw98-233h](https://github.com/advisories/GHSA-w2wj-hw98-233h): Keycloak Potential Variable Reference in Model Storage Services (MAVEN/org.keycloak:keycloak-model-storage-services) | MODERATE (CVSS: 4.9) | 2025-08-21 |
| GHSA | [GHSA-GHSA-xqrq-4mgf-ff32](https://github.com/advisories/GHSA-xqrq-4mgf-ff32): Python-Future Module Arbitrary Code Execution via Unintended Import of test.py (PIP/future) | HIGH (CVSS: 0.0) | 2025-08-14 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [e1d8f9c](https://github.com/torvalds/linux/commit/e1d8f9ccb24ecd969fb1062886b20200acc60009) | Merge tag 'trace-v6.17-rc2-2' of git://git.kernel.org/pub/scm/linux/kernel/git/trace/linux-trace | 2025-08-23 |
| torvalds/linux | [bfb336c](https://github.com/torvalds/linux/commit/bfb336cf97df7b37b2b2edec0f69773e06d11955) | ftrace: Also allocate and copy hash for reading of filter files | 2025-08-22 |
| openssl/openssl | [fc84d46](https://github.com/openssl/openssl/commit/fc84d46d7227886152be00618889a521e9132ef3) | Fix null pointer check in pkey_dh_derive to ensure both keys are set | 2025-08-13 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28259](https://github.com/openssl/openssl/pull/28259) | Fix potential null pointer dereference in pkey_dh_derive | 2025-08-22 |
| wazuh/wazuh | [#31511](https://github.com/wazuh/wazuh/pull/31511) | Fix literal parser dangling std::string_view capture, and add regression test | 2025-08-22 |
| hibernate/hibernate-validator | [#1682](https://github.com/hibernate/hibernate-validator/pull/1682) | Bump org.glassfish:jakarta.el from 3.0.3 to 3.0.4 in /performance | 2025-08-22 |

