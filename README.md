# Security Updates Monitor

*Last updated: 2025-07-08 18:20:52 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 11 |
| COMMIT | 3 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-3j8r-jf9w-5cmh](https://github.com/advisories/GHSA-3j8r-jf9w-5cmh): LlamaIndex vulnerability in its ObsidianReader class can lead to Path Traversal exploit (PIP/llama-index-readers-obsidian) | MODERATE (CVSS: 6.2) | 2025-07-07 |
| GHSA | [GHSA-GHSA-3wxx-q3gv-pvvv](https://github.com/advisories/GHSA-3wxx-q3gv-pvvv): LlamaIndex vulnerable to DoS attack through uncontrolled recursive JSON parsing (PIP/llama-index-core) | MODERATE (CVSS: 6.5) | 2025-07-07 |
| GHSA | [GHSA-GHSA-p7j4-jwjf-5x9w](https://github.com/advisories/GHSA-p7j4-jwjf-5x9w): LlamaIndex vulnerability in ArxivReader class can cause MD5 hash collisions (PIP/llama-index-readers-papers) | MODERATE (CVSS: 5.3) | 2025-07-07 |
| GHSA | [GHSA-GHSA-w42r-mrx7-c633](https://github.com/advisories/GHSA-w42r-mrx7-c633): LlamaIndex has an XML Entity Expansion vulnerability in its sitemap parser (PIP/llama-index-readers-papers) | HIGH (CVSS: 7.5) | 2025-07-07 |
| GHSA | [GHSA-GHSA-489j-g2vx-39wf](https://github.com/advisories/GHSA-489j-g2vx-39wf): Transformers vulnerable to ReDoS attack through its SETTING_RE variable (PIP/transformers) | MODERATE (CVSS: 5.3) | 2025-07-07 |
| GHSA | [GHSA-GHSA-j47q-rc62-w448](https://github.com/advisories/GHSA-j47q-rc62-w448): fastapi-guard is vulnerable to ReDoS through inefficient regex (PIP/fastapi-guard) | MODERATE (CVSS: 0.0) | 2025-07-07 |
| GHSA | [GHSA-GHSA-fmrf-6jv9-qjc7](https://github.com/advisories/GHSA-fmrf-6jv9-qjc7): LlamaIndex is vulnerable to Path Traversal attack through its ObsidianReader class (PIP/llama-index-readers-obsidian) | HIGH (CVSS: 7.5) | 2025-07-07 |
| GHSA | [GHSA-GHSA-36rg-gfq2-3h56](https://github.com/advisories/GHSA-36rg-gfq2-3h56): Better Auth Open Redirect Vulnerability in originCheck Middleware Affects Multiple Routes (NPM/better-auth) | LOW (CVSS: 0.0) | 2025-07-07 |
| GHSA | [GHSA-GHSA-rxf6-323f-44fc](https://github.com/advisories/GHSA-rxf6-323f-44fc): rust-protobuf crate is vulnerable to Uncontrolled Recursion, potentially leading to DoS (RUST/protobuf) | MODERATE (CVSS: 5.9) | 2025-07-05 |
| GHSA | [GHSA-GHSA-65gg-3w2w-hr4h](https://github.com/advisories/GHSA-65gg-3w2w-hr4h): Podman Improper Certificate Validation; machine missing TLS verification (GO/github.com/containers/podman/v4, GO/github.com/containers/podman/v5) | HIGH (CVSS: 8.4) | 2025-06-25 |
| GHSA | [GHSA-GHSA-wxcc-2f3q-4h58](https://github.com/advisories/GHSA-wxcc-2f3q-4h58): Grafana Alerting VictorOps integration could be exposed to users with Viewer permission (GO/github.com/grafana/grafana, GO/github.com/grafana/grafana, GO/github.com/grafana/grafana) | MODERATE (CVSS: 4.3) | 2025-01-31 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [d006330](https://github.com/torvalds/linux/commit/d006330be3f782ff3fb7c3ed51e617e01f29a465) | Merge tag 'sound-6.16-rc6' of git://git.kernel.org/pub/scm/linux/kernel/git/tiwai/sound | 2025-07-08 |
| chromium/chromium | [fca80ec](https://github.com/chromium/chromium/commit/fca80ec5b95c32a556049239427daa3a0cc41f80) | Roll V8 from 6604430bd769 to 7de1ea5c703b (11 revisions) | 2025-07-08 |
| chromium/chromium | [4186904](https://github.com/chromium/chromium/commit/4186904137f642a442c91ee87d50d6dff4e605e9) | Roll BoringSSL from 913c14be725d to 3fd8220e3c88 (1 revision) | 2025-07-07 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#27920](https://github.com/openssl/openssl/pull/27920) | fuzz/cmp.c: Correct the usages of BIO_new() | 2025-07-08 |

