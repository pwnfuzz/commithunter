# Security Updates Monitor

*Last updated: 2025-07-09 13:29:49 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 11 |
| COMMIT | 4 |
| PR | 3 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-gjv4-ghm7-q58q](https://github.com/advisories/GHSA-gjv4-ghm7-q58q): MCP Server Kubernetes vulnerable to command injection in several tools (NPM/mcp-server-kubernetes) | HIGH (CVSS: 7.5) | 2025-07-08 |
| GHSA | [GHSA-GHSA-rj53-j6jw-7f7g](https://github.com/advisories/GHSA-rj53-j6jw-7f7g): Babylon vulnerable to chain halt when a message modifies the validator set at the epoch boundary (GO/github.com/babylonlabs-io/babylon/v2) | HIGH (CVSS: 0.0) | 2025-07-08 |
| GHSA | [GHSA-GHSA-4pfg-2mw5-f8jx](https://github.com/advisories/GHSA-4pfg-2mw5-f8jx): Cloudflare Vite plugin exposes secrets over the built-in dev server (NPM/@cloudflare/vite-plugin) | MODERATE (CVSS: 0.0) | 2025-07-08 |
| GHSA | [GHSA-GHSA-5w57-2ccq-8w95](https://github.com/advisories/GHSA-5w57-2ccq-8w95): Node.js Sandbox MCP Server vulnerability can lead to Sandbox Escape via Command Injection (NPM/node-code-sandbox-mcp) | HIGH (CVSS: 7.5) | 2025-07-08 |
| GHSA | [GHSA-GHSA-q93c-p2mw-p23f](https://github.com/advisories/GHSA-q93c-p2mw-p23f): Dagster vulnerable to Path Traversal attack through its /logs endpoint (PIP/dagster) | MODERATE (CVSS: 7.5) | 2025-07-07 |
| GHSA | [GHSA-GHSA-2rhq-96q8-4vjq](https://github.com/advisories/GHSA-2rhq-96q8-4vjq): LlamaIndex vulnerable to Path Traversal attack through its encode_image function (PIP/llama-index-core) | HIGH (CVSS: 7.5) | 2025-07-07 |
| GHSA | [GHSA-GHSA-j5pr-vrjj-9v4h](https://github.com/advisories/GHSA-j5pr-vrjj-9v4h): Lord of Large Language Models vulnerable to Observable Discrepancy attack via authenticate_user function (PIP/lollms) | HIGH (CVSS: 7.5) | 2025-07-07 |
| GHSA | [GHSA-GHSA-phhr-52qp-3mj4](https://github.com/advisories/GHSA-phhr-52qp-3mj4): Transformers's Improper Input Validation vulnerability can be exploited through username injection (PIP/transformers) | LOW (CVSS: 3.5) | 2025-07-07 |
| GHSA | [GHSA-GHSA-jjph-296x-mrcr](https://github.com/advisories/GHSA-jjph-296x-mrcr): Transformers vulnerable to ReDoS attack through its get_imports() function (PIP/transformers) | MODERATE (CVSS: 5.3) | 2025-07-07 |
| GHSA | [GHSA-GHSA-q2wp-rjmx-x6x9](https://github.com/advisories/GHSA-q2wp-rjmx-x6x9): Transformers's ReDoS vulnerability in get_configuration_file can lead to catastrophic backtracking (PIP/transformers) | MODERATE (CVSS: 5.3) | 2025-07-07 |
| GHSA | [GHSA-GHSA-567v-6hmg-6qg7](https://github.com/advisories/GHSA-567v-6hmg-6qg7): ZITADEL "ignoring unknown usernames" vulnerability (GO/github.com/zitadel/zitadel, GO/github.com/zitadel/zitadel, GO/github.com/zitadel/zitadel) | MODERATE (CVSS: 5.3) | 2024-07-31 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [fceb315](https://github.com/chromium/chromium/commit/fceb3154f98dd80df7c2cd632b04791f584e0da2) | [iOS]Add a delegate to sync encryption view | 2025-07-08 |
| chromium/chromium | [02f3d31](https://github.com/chromium/chromium/commit/02f3d31560b9449471da8aaa77f3c69eb89c0793) | Enable stricter checks for DistilledPagePrefs observer lifetime. | 2025-07-08 |
| torvalds/linux | [70b9c0c](https://github.com/torvalds/linux/commit/70b9c0c11e55167b9552ef395bc00f4920299177) | uapi: bitops: use UAPI-safe variant of BITS_PER_LONG again (2) | 2025-06-30 |
| torvalds/linux | [570db4b](https://github.com/torvalds/linux/commit/570db4b39f535a8bb722adb8be0280d09e34ca99) | module: Make sure relocations are applied to the per-CPU section | 2025-06-10 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#27994](https://github.com/openssl/openssl/pull/27994) | test/evp_extra_test.c: Add check for BIO_new() | 2025-07-08 |
| openssl/openssl | [#27993](https://github.com/openssl/openssl/pull/27993) | test/bio_base64_test.c: Add check for BIO_new() | 2025-07-08 |
| wazuh/wazuh | [#30675](https://github.com/wazuh/wazuh/pull/30675) | Remove wazuh-analysisd and wazuh-dbd | 2025-07-08 |

