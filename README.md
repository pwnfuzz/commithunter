# Security Updates Monitor

*Last updated: 2025-07-03 07:15:19 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 16 |
| COMMIT | 3 |
| PR | 4 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-3w94-vq2x-v5wr](https://github.com/advisories/GHSA-3w94-vq2x-v5wr): ethereum does not check transaction malleability for EIP-2930, EIP-1559 and EIP-7702 transactions (RUST/ethereum) | MODERATE (CVSS: 0.0) | 2025-07-02 |
| GHSA | [GHSA-GHSA-3m86-c9x3-vwm9](https://github.com/advisories/GHSA-3m86-c9x3-vwm9): Graylog vulnerable to privilege escalation through API tokens (MAVEN/org.graylog2:graylog2-server, MAVEN/org.graylog2:graylog2-server) | HIGH (CVSS: 0.0) | 2025-06-30 |
| GHSA | [GHSA-GHSA-cm2r-rg7r-p7gg](https://github.com/advisories/GHSA-cm2r-rg7r-p7gg): File Browser vulnerable to insecure password handling (GO/github.com/filebrowser/filebrowser, GO/github.com/filebrowser/filebrowser/v2) | MODERATE (CVSS: 5.9) | 2025-06-30 |
| GHSA | [GHSA-GHSA-8vxj-4cph-c596](https://github.com/advisories/GHSA-8vxj-4cph-c596): Deno has --allow-read / --allow-write permission bypass in `node:sqlite` (RUST/deno_node, RUST/deno) | MODERATE (CVSS: 9.1) | 2025-06-04 |
| GHSA | [GHSA-GHSA-7w8p-chxq-2789](https://github.com/advisories/GHSA-7w8p-chxq-2789): Deno.env.toObject() ignores the variables listed in --deny-env and returns all environment variables (RUST/deno_runtime, RUST/deno, RUST/deno) | MODERATE (CVSS: 5.3) | 2025-06-04 |
| GHSA | [GHSA-GHSA-xqxc-x6p3-w683](https://github.com/advisories/GHSA-xqxc-x6p3-w683): Deno run with --allow-read and --deny-read flags results in allowed (RUST/deno_runtime, RUST/deno, RUST/deno) | MODERATE (CVSS: 5.3) | 2025-06-04 |
| GHSA | [GHSA-GHSA-5fc3-pqf2-57cx](https://github.com/advisories/GHSA-5fc3-pqf2-57cx): Apache IoTDB Discloses Sensitive Information via Log Files (PIP/apache-iotdb, PIP/apache-iotdb, MAVEN/org.apache.iotdb:node-commons) | MODERATE (CVSS: 0.0) | 2025-05-14 |
| GHSA | [GHSA-GHSA-f4rq-f4j9-f6rm](https://github.com/advisories/GHSA-f4rq-f4j9-f6rm): Apache IoTDB Vulnerable to Remote Code Execution (PIP/apache-iotdb, MAVEN/org.apache.iotdb:iotdb-core) | CRITICAL (CVSS: 9.8) | 2025-05-14 |
| GHSA | [GHSA-GHSA-x3m8-f7g5-qhm7](https://github.com/advisories/GHSA-x3m8-f7g5-qhm7): vLLM Allows Remote Code Execution via Mooncake Integration (PIP/vllm) | CRITICAL (CVSS: 9.1) | 2025-03-19 |
| GHSA | [GHSA-GHSA-rm76-4mrf-v9r8](https://github.com/advisories/GHSA-rm76-4mrf-v9r8): vLLM uses Python 3.12 built-in hash() which leads to predictable hash collisions in prefix cache (PIP/vllm) | LOW (CVSS: 2.6) | 2025-02-06 |
| GHSA | [GHSA-GHSA-p7c9-8xx8-h74f](https://github.com/advisories/GHSA-p7c9-8xx8-h74f): Apache Kafka's SCRAM implementation Incorrectly Implements Authentication Algorithm (MAVEN/org.apache.kafka:kafka_2.10, MAVEN/org.apache.kafka:kafka_2.11, MAVEN/org.apache.kafka:kafka_2.12) | LOW (CVSS: 5.3) | 2024-12-18 |
| GHSA | [GHSA-GHSA-jxw2-jvxf-5vrp](https://github.com/advisories/GHSA-jxw2-jvxf-5vrp): Databricks JDBC Driver Command Injection vulnerability (MAVEN/com.databricks:databricks-jdbc) | HIGH (CVSS: 7.3) | 2024-12-17 |
| GHSA | [GHSA-GHSA-7p9f-6x8j-gxxp](https://github.com/advisories/GHSA-7p9f-6x8j-gxxp): CRI-O: Maliciously structured checkpoint file can gain arbitrary node access (GO/github.com/cri-o/cri-o, GO/github.com/cri-o/cri-o, GO/github.com/cri-o/cri-o) | MODERATE (CVSS: 7.4) | 2024-11-26 |
| GHSA | [GHSA-GHSA-h7w9-c5vx-x7j3](https://github.com/advisories/GHSA-h7w9-c5vx-x7j3): Insecure Default Initialization of Resource vulnerability in Apache Solr (MAVEN/org.apache.solr:solr, MAVEN/org.apache.solr:solr) | HIGH (CVSS: 8.1) | 2024-10-16 |
| GHSA | [GHSA-GHSA-7rvp-xqj7-rxf2](https://github.com/advisories/GHSA-7rvp-xqj7-rxf2): Withdrawn Advisory: Daylight Studio FUEL-CMS SQLi Vulnerability (COMPOSER/codeigniter/framework) | HIGH (CVSS: 8.8) | 2023-08-11 |
| GHSA | [GHSA-GHSA-m8p2-495h-ccmh](https://github.com/advisories/GHSA-m8p2-495h-ccmh): The SafeHtml annotation in Hibernate-Validator does not properly guard against XSS attacks (MAVEN/org.hibernate.validator:hibernate-validator) | MODERATE (CVSS: 6.5) | 2020-01-08 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| postgres/postgres | [fd7d7b7](https://github.com/postgres/postgres/commit/fd7d7b719137b5c427681a50c0a0ac2d745b68bd) | Improve checks for GUC recovery_target_timeline | 2025-07-03 |
| chromium/chromium | [09db6e4](https://github.com/chromium/chromium/commit/09db6e4822a2755e3b8b32d33ac1d7583cf29c36) | FitText: Fix a null pointer dereference in GetSvgFragmentData() | 2025-07-03 |
| torvalds/linux | [b4911fb](https://github.com/torvalds/linux/commit/b4911fb0b060899e4eebca0151eb56deb86921ec) | Merge tag 'mmc-v6.16-rc1' of git://git.kernel.org/pub/scm/linux/kernel/git/ulfh/mmc | 2025-07-02 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#27955](https://github.com/openssl/openssl/pull/27955) | Fix: Private Key Found Directly in Code Files in apps/ca-key.pem | 2025-07-03 |
| openssl/openssl | [#27954](https://github.com/openssl/openssl/pull/27954) | Fix: GitHub Actions Workflow Vulnerable to Code Injection Attacks in .github/workflows/coveralls.yml | 2025-07-03 |
| openssl/openssl | [#27953](https://github.com/openssl/openssl/pull/27953) | Fix: Unsafe Text Processing Function Could Corrupt Data in apps/rehash.c | 2025-07-03 |
| openssl/openssl | [#27952](https://github.com/openssl/openssl/pull/27952) | Fix: Unsafe Text Processing Function Could Corrupt Data in apps/rehash.c | 2025-07-03 |

