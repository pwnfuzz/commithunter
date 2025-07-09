# Security Updates Monitor

*Last updated: 2025-07-09 06:22:33 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 13 |
| COMMIT | 3 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-x698-5hjm-w2m5](https://github.com/advisories/GHSA-x698-5hjm-w2m5): pyLoad is vulnerable to attacks that bypass localhost restrictions, enabling the creation of arbitrary packages (PIP/pyload-ng) | HIGH (CVSS: 7.5) | 2025-07-08 |
| GHSA | [GHSA-GHSA-2wcm-vx67-3x4q](https://github.com/advisories/GHSA-2wcm-vx67-3x4q): Duplicate Advisory: GHSA-x698-5hjm-w2m5 (PIP/pyload-ng) | HIGH (CVSS: 0.0) | 2025-07-08 |
| GHSA | [GHSA-GHSA-p22h-3m2v-cmgh](https://github.com/advisories/GHSA-p22h-3m2v-cmgh): Cosmos SDK's Integer Overflow vulnerability in its Validator Rewards pool can cause a chain halt (GO/github.com/cosmos/cosmos-sdk, GO/github.com/cosmos/cosmos-sdk) | HIGH (CVSS: 0.0) | 2025-07-08 |
| GHSA | [GHSA-GHSA-557j-xg8c-q2mm](https://github.com/advisories/GHSA-557j-xg8c-q2mm): Helm vulnerable to Code Injection through malicious chart.yaml content (GO/helm.sh/helm/v3) | HIGH (CVSS: 8.5) | 2025-07-08 |
| GHSA | [GHSA-GHSA-3j8r-jf9w-5cmh](https://github.com/advisories/GHSA-3j8r-jf9w-5cmh): LlamaIndex vulnerability in its ObsidianReader class can lead to Path Traversal exploit (PIP/llama-index-readers-obsidian) | MODERATE (CVSS: 6.2) | 2025-07-07 |
| GHSA | [GHSA-GHSA-3wxx-q3gv-pvvv](https://github.com/advisories/GHSA-3wxx-q3gv-pvvv): LlamaIndex vulnerable to DoS attack through uncontrolled recursive JSON parsing (PIP/llama-index-core) | MODERATE (CVSS: 6.5) | 2025-07-07 |
| GHSA | [GHSA-GHSA-65gg-3w2w-hr4h](https://github.com/advisories/GHSA-65gg-3w2w-hr4h): Podman Improper Certificate Validation; machine missing TLS verification (GO/github.com/containers/podman/v4, GO/github.com/containers/podman/v5) | HIGH (CVSS: 8.4) | 2025-06-25 |
| GHSA | [GHSA-GHSA-rpfv-46xj-5984](https://github.com/advisories/GHSA-rpfv-46xj-5984): Upsonic has vulnerability in Pickle Handler component that can lead to deserialization (PIP/upsonic) | LOW (CVSS: 5.5) | 2025-06-19 |
| GHSA | [GHSA-GHSA-8jf4-fcjr-68c2](https://github.com/advisories/GHSA-8jf4-fcjr-68c2): Upsonic is vulnerable to Path Traversal attack through its os.path.join function (PIP/upsonic) | LOW (CVSS: 5.5) | 2025-06-19 |
| GHSA | [GHSA-GHSA-wxcc-2f3q-4h58](https://github.com/advisories/GHSA-wxcc-2f3q-4h58): Grafana Alerting VictorOps integration could be exposed to users with Viewer permission (GO/github.com/grafana/grafana, GO/github.com/grafana/grafana, GO/github.com/grafana/grafana) | MODERATE (CVSS: 4.3) | 2025-01-31 |
| GHSA | [GHSA-GHSA-hfrg-4jwr-jfpj](https://github.com/advisories/GHSA-hfrg-4jwr-jfpj): Improper HTML sanitization in ZITADEL (GO/github.com/zitadel/zitadel, GO/github.com/zitadel/zitadel, GO/github.com/zitadel/zitadel) | HIGH (CVSS: 8.1) | 2024-03-18 |
| GHSA | [GHSA-GHSA-xr7p-8q82-878q](https://github.com/advisories/GHSA-xr7p-8q82-878q): teler dashboard vulnerable to DOM-based cross-site scripting (XSS) (GO/teler.app, GO/teler.app, GO/teler.app) | LOW (CVSS: 3.1) | 2022-12-06 |
| GHSA | [GHSA-GHSA-77rm-9x9h-xj3g](https://github.com/advisories/GHSA-77rm-9x9h-xj3g): NULL Pointer Dereference in Protocol Buffers (GO/github.com/protocolbuffers/protobuf, GO/github.com/protocolbuffers/protobuf, MAVEN/com.google.protobuf:protobuf-java) | HIGH (CVSS: 7.5) | 2022-01-27 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [c545ffc](https://github.com/chromium/chromium/commit/c545ffce17a6aba55825a9512db922b064b10dd6) | Adding to third_party update. | 2025-07-09 |
| chromium/chromium | [fb8fe36](https://github.com/chromium/chromium/commit/fb8fe36758c107d2638908e36a86625cada621d3) | RenderDocument: Fix touch-stale-node-crash.html test. | 2025-07-09 |
| torvalds/linux | [d006330](https://github.com/torvalds/linux/commit/d006330be3f782ff3fb7c3ed51e617e01f29a465) | Merge tag 'sound-6.16-rc6' of git://git.kernel.org/pub/scm/linux/kernel/git/tiwai/sound | 2025-07-08 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#27920](https://github.com/openssl/openssl/pull/27920) | fuzz/cmp.c: Correct the usages of BIO_new() | 2025-07-08 |

