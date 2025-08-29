# Security Updates Monitor

*Last updated: 2025-08-29 19:10:48 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 11 |
| COMMIT | 9 |
| PR | 4 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-26rv-h2hf-3fw4](https://github.com/advisories/GHSA-26rv-h2hf-3fw4): Payload's SQLite adapter Session Fixation vulnerability (NPM/@payloadcms/graphql, NPM/@payloadcms/next, NPM/payload) | MODERATE (CVSS: 0.0) | 2025-08-29 |
| GHSA | [GHSA-GHSA-5v66-m237-hwf7](https://github.com/advisories/GHSA-5v66-m237-hwf7): Payload does not invalidate JWTs after log out (NPM/@payloadcms/graphql, NPM/@payloadcms/next, NPM/payload) | MODERATE (CVSS: 0.0) | 2025-08-29 |
| GHSA | [GHSA-GHSA-w469-hj2f-jpr5](https://github.com/advisories/GHSA-w469-hj2f-jpr5): Harness Allows Arbitrary File Write in Gitness LFS server (GO/github.com/harness/gitness, GO/github.com/harness/gitness) | HIGH (CVSS: 8.8) | 2025-08-29 |
| GHSA | [GHSA-GHSA-v2ch-c8v8-fgr7](https://github.com/advisories/GHSA-v2ch-c8v8-fgr7): Versity panic induced by AWS chunked data sent to port (GO/github.com/versity/versitygw) | HIGH (CVSS: 0.0) | 2025-08-29 |
| GHSA | [GHSA-GHSA-m54q-mm9w-fp6g](https://github.com/advisories/GHSA-m54q-mm9w-fp6g): Exiv2 has quadratic performance in ICC profile parsing in JpegBase::readMetadata (PIP/Exiv2) | LOW (CVSS: 0.0) | 2025-08-29 |
| GHSA | [GHSA-GHSA-496f-x7cq-cq39](https://github.com/advisories/GHSA-496f-x7cq-cq39): Exiv2 Segmentation Faults in Exiv2::EpsImage::writeMetadata() via crafted EPS file (PIP/Exiv2) | LOW (CVSS: 0.0) | 2025-08-29 |
| GHSA | [GHSA-GHSA-8f82-53h8-2p34](https://github.com/advisories/GHSA-8f82-53h8-2p34): HashiCorp Vault Community Edition Denial of Service Though Complex JSON Payloads (GO/github.com/hashicorp/vault) | HIGH (CVSS: 7.5) | 2025-08-28 |
| GHSA | [GHSA-GHSA-jc7w-c686-c4v9](https://github.com/advisories/GHSA-jc7w-c686-c4v9): github.com/ulikunitz/xz leaks memory when decoding a corrupted multiple LZMA archives (GO/github.com/ulikunitz/xz) | MODERATE (CVSS: 5.3) | 2025-08-28 |
| GHSA | [GHSA-GHSA-3rw9-wmc8-8948](https://github.com/advisories/GHSA-3rw9-wmc8-8948): Coder accepts an APIKey beyond the linked OIDC expiry if there is no refresh token (GO/github.com/coder/coder/v2) | LOW (CVSS: 0.0) | 2025-08-28 |
| GHSA | [GHSA-GHSA-cxm3-wv7p-598c](https://github.com/advisories/GHSA-cxm3-wv7p-598c): Malicious versions of Nx were published (NPM/@nx/workspace, NPM/@nx/js, NPM/@nx/devkit) | CRITICAL (CVSS: 0.0) | 2025-08-27 |
| GHSA | [GHSA-GHSA-rh8q-vjgf-gf74](https://github.com/advisories/GHSA-rh8q-vjgf-gf74): Improper Limitation of a Pathname to a Restricted Directory in Apache Tomcat (MAVEN/org.apache.tomcat:tomcat, MAVEN/org.apache.tomcat:tomcat, MAVEN/org.apache.tomcat:tomcat) | MODERATE (CVSS: 5.3) | 2022-05-14 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [fb679c8](https://github.com/torvalds/linux/commit/fb679c832b6497f19fffb8274c419783909c0912) | Merge tag 'efi-fixes-for-v6.17-1' of git://git.kernel.org/pub/scm/linux/kernel/git/efi/efi | 2025-08-29 |
| torvalds/linux | [02d6eee](https://github.com/torvalds/linux/commit/02d6eeedbc36d4b309d5518778071a749ef79c4e) | Merge tag 'hid-for-linus-2025082901' of git://git.kernel.org/pub/scm/linux/kernel/git/hid/hid | 2025-08-29 |
| torvalds/linux | [9c736ac](https://github.com/torvalds/linux/commit/9c736ace0666efe68efd53fcdfa2c6653c3e0e72) | Merge tag 'net-6.17-rc4' of git://git.kernel.org/pub/scm/linux/kernel/git/netdev/net | 2025-08-29 |
| postgres/postgres | [da9f9f7](https://github.com/postgres/postgres/commit/da9f9f75e5ce27a45878ffa262156d18f0046188) | Fix possible use after free in expand_partitioned_rtentry() | 2025-08-29 |
| chromium/chromium | [f65f524](https://github.com/chromium/chromium/commit/f65f524a6128bc57d1fb69e996c3ac9eb66897ef) | window management api: fix DisplayTopology null pointer exception | 2025-08-29 |
| chromium/chromium | [79d87ae](https://github.com/chromium/chromium/commit/79d87ae3a2839473ac244ec344a63b7de10bc4ae) | Fix OOB issue in DNSServerIterator | 2025-08-29 |
| chromium/chromium | [72f6aaa](https://github.com/chromium/chromium/commit/72f6aaa905cd2fe6fb41f25a0545179eb996aeeb) | Fix UAF in LoginStateChecker and related browser tests | 2025-08-29 |
| chromium/chromium | [237384f](https://github.com/chromium/chromium/commit/237384fc5991fdba6f1c90bf2683daedbbe44434) | Pass AttachmentDelegate to GlicInstance constructor | 2025-08-28 |
| openssl/openssl | [a8d02c5](https://github.com/openssl/openssl/commit/a8d02c5ca706384c53c941b3041c326c62a6f09e) | crypto/bio/bio_print.c: avoid integer overflow when reading width/precision | 2025-08-05 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28379](https://github.com/openssl/openssl/pull/28379) | Avoid signed integer overflow in RAND_load_file | 2025-08-29 |
| openssl/openssl | [#22285](https://github.com/openssl/openssl/pull/22285) | PKCS7/CMS: fix doc on signer/chain certs | 2025-08-29 |
| wazuh/wazuh | [#31571](https://github.com/wazuh/wazuh/pull/31571) | Refactor add support for Amazon Inspector v2 | 2025-08-29 |
| wazuh/wazuh | [#31599](https://github.com/wazuh/wazuh/pull/31599) | Improve and fix `dpkg` algorithm in version compare | 2025-08-29 |

