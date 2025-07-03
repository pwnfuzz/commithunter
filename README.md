# Security Updates Monitor

*Last updated: 2025-07-03 17:15:06 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 11 |
| COMMIT | 5 |
| PR | 4 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-q43x-79jr-cq98](https://github.com/advisories/GHSA-q43x-79jr-cq98): tarteaucitron.js vulnerable to DOM Clobbering via document.currentScript (NPM/tarteaucitronjs) | MODERATE (CVSS: 4.2) | 2025-07-03 |
| GHSA | [GHSA-GHSA-gj54-gwj9-x2c6](https://github.com/advisories/GHSA-gj54-gwj9-x2c6): eKuiper /config/uploads API arbitrary file writing may lead to RCE (GO/github.com/lf-edge/ekuiper, GO/github.com/lf-edge/ekuiper/v2) | HIGH (CVSS: 0.0) | 2025-07-03 |
| GHSA | [GHSA-GHSA-fv2p-qj5p-wqq4](https://github.com/advisories/GHSA-fv2p-qj5p-wqq4): LF Edge eKuiper vulnerable to File Path Traversal leading to file replacement (GO/github.com/lf-edge/ekuiper, GO/github.com/lf-edge/ekuiper/v2) | HIGH (CVSS: 8.5) | 2025-07-03 |
| GHSA | [GHSA-GHSA-hqp6-mjw3-f586](https://github.com/advisories/GHSA-hqp6-mjw3-f586): HashiCorp Vagrant has code injection vulnerability through default synced folders (RUBYGEMS/vagrant) | MODERATE (CVSS: 0.0) | 2025-07-02 |
| GHSA | [GHSA-GHSA-j64v-xh5w-8hqj](https://github.com/advisories/GHSA-j64v-xh5w-8hqj): Microweber CMS API has authenticated local file inclusion vulnerability (COMPOSER/microweber/microweber) | MODERATE (CVSS: 0.0) | 2025-07-02 |
| GHSA | [GHSA-GHSA-3w94-vq2x-v5wr](https://github.com/advisories/GHSA-3w94-vq2x-v5wr): ethereum does not check transaction malleability for EIP-2930, EIP-1559 and EIP-7702 transactions (RUST/ethereum) | MODERATE (CVSS: 0.0) | 2025-07-02 |
| GHSA | [GHSA-GHSA-3m86-c9x3-vwm9](https://github.com/advisories/GHSA-3m86-c9x3-vwm9): Graylog vulnerable to privilege escalation through API tokens (MAVEN/org.graylog2:graylog2-server, MAVEN/org.graylog2:graylog2-server) | HIGH (CVSS: 0.0) | 2025-06-30 |
| GHSA | [GHSA-GHSA-8vxj-4cph-c596](https://github.com/advisories/GHSA-8vxj-4cph-c596): Deno has --allow-read / --allow-write permission bypass in `node:sqlite` (RUST/deno_node, RUST/deno) | MODERATE (CVSS: 9.1) | 2025-06-04 |
| GHSA | [GHSA-GHSA-7w8p-chxq-2789](https://github.com/advisories/GHSA-7w8p-chxq-2789): Deno.env.toObject() ignores the variables listed in --deny-env and returns all environment variables (RUST/deno_runtime, RUST/deno, RUST/deno) | MODERATE (CVSS: 5.3) | 2025-06-04 |
| GHSA | [GHSA-GHSA-xqxc-x6p3-w683](https://github.com/advisories/GHSA-xqxc-x6p3-w683): Deno run with --allow-read and --deny-read flags results in allowed (RUST/deno_runtime, RUST/deno, RUST/deno) | MODERATE (CVSS: 5.3) | 2025-06-04 |
| GHSA | [GHSA-GHSA-p7c9-8xx8-h74f](https://github.com/advisories/GHSA-p7c9-8xx8-h74f): Apache Kafka's SCRAM implementation Incorrectly Implements Authentication Algorithm (MAVEN/org.apache.kafka:kafka_2.10, MAVEN/org.apache.kafka:kafka_2.11, MAVEN/org.apache.kafka:kafka_2.12) | LOW (CVSS: 5.3) | 2024-12-18 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [d32e907](https://github.com/torvalds/linux/commit/d32e907d15f7257f69d38b4c829f87a79ecf8b7f) | Merge tag 'xfs-fixes-6.16-rc5' of git://git.kernel.org/pub/scm/fs/xfs/xfs-linux | 2025-07-03 |
| postgres/postgres | [fd7d7b7](https://github.com/postgres/postgres/commit/fd7d7b719137b5c427681a50c0a0ac2d745b68bd) | Improve checks for GUC recovery_target_timeline | 2025-07-03 |
| chromium/chromium | [c91fda0](https://github.com/chromium/chromium/commit/c91fda09bebc27f023570330dc856551325e15c6) | Fix memory heap-use-after-free on linux_chromium_asan_rel_ng in test | 2025-07-03 |
| chromium/chromium | [09db6e4](https://github.com/chromium/chromium/commit/09db6e4822a2755e3b8b32d33ac1d7583cf29c36) | FitText: Fix a null pointer dereference in GetSvgFragmentData() | 2025-07-03 |
| torvalds/linux | [103406b](https://github.com/torvalds/linux/commit/103406b38c600fec1fe375a77b27d87e314aea09) | net/sched: Always pass notifications when child class becomes empty | 2025-06-30 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#27955](https://github.com/openssl/openssl/pull/27955) | Fix: Private Key Found Directly in Code Files in apps/ca-key.pem | 2025-07-03 |
| openssl/openssl | [#27954](https://github.com/openssl/openssl/pull/27954) | Fix: GitHub Actions Workflow Vulnerable to Code Injection Attacks in .github/workflows/coveralls.yml | 2025-07-03 |
| openssl/openssl | [#27953](https://github.com/openssl/openssl/pull/27953) | Fix: Unsafe Text Processing Function Could Corrupt Data in apps/rehash.c | 2025-07-03 |
| openssl/openssl | [#27952](https://github.com/openssl/openssl/pull/27952) | Fix: Unsafe Text Processing Function Could Corrupt Data in apps/rehash.c | 2025-07-03 |

