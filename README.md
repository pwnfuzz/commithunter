# Security Updates Monitor

*Last updated: 2025-07-29 06:24:15 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 29 |
| COMMIT | 3 |
| PR | 2 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-9952-gv64-x94c](https://github.com/advisories/GHSA-9952-gv64-x94c): CodeIgniter4's ImageMagick Handler has Command Injection Vulnerability (COMPOSER/codeigniter4/framework) | CRITICAL (CVSS: 9.8) | 2025-07-28 |
| GHSA | [GHSA-GHSA-q5h2-xq96-6gmc](https://github.com/advisories/GHSA-q5h2-xq96-6gmc): Duplicate Advisory: buffered-reader vulnerable to out-of-bounds array access leading to panic (RUST/buffered-reader, RUST/buffered-reader) | LOW (CVSS: 2.9) | 2025-07-28 |
| GHSA | [GHSA-GHSA-286m-6pg9-v42v](https://github.com/advisories/GHSA-286m-6pg9-v42v): Duplicate Advisory: Multiple issues involving quote API in shlex (RUST/shlex) | LOW (CVSS: 3.2) | 2025-07-28 |
| GHSA | [GHSA-GHSA-97f8-h76h-f297](https://github.com/advisories/GHSA-97f8-h76h-f297): Duplicate Advisory: Unauthenticated Nonce Increment in snow (RUST/snow) | LOW (CVSS: 3.1) | 2025-07-28 |
| GHSA | [GHSA-GHSA-rfx3-ffrp-6875](https://github.com/advisories/GHSA-rfx3-ffrp-6875): Duplicate Advisory: sequoia-openpgp vulnerable to out-of-bounds array access leading to panic (RUST/sequoia-openpgp, RUST/sequoia-openpgp, RUST/sequoia-openpgp) | LOW (CVSS: 2.9) | 2025-07-28 |
| GHSA | [GHSA-GHSA-gw89-822v-8v8g](https://github.com/advisories/GHSA-gw89-822v-8v8g): Duplicate Advisory: `openssl` `X509VerifyParamRef::set_host` buffer over-read (RUST/openssl) | MODERATE (CVSS: 4.5) | 2025-07-28 |
| GHSA | [GHSA-GHSA-g693-v3jr-8hcr](https://github.com/advisories/GHSA-g693-v3jr-8hcr): Duplicate Advisory: `ed25519-dalek` Double Public Key Signing Function Oracle Attack (RUST/ed25519-dalek) | MODERATE (CVSS: 5.9) | 2025-07-28 |
| GHSA | [GHSA-GHSA-5c5j-jmhx-q2gr](https://github.com/advisories/GHSA-5c5j-jmhx-q2gr): Duplicate Advisory: gix-transport code execution vulnerability (RUST/gix-transport) | MODERATE (CVSS: 4.1) | 2025-07-28 |
| GHSA | [GHSA-GHSA-j87p-gjr6-m4pv](https://github.com/advisories/GHSA-j87p-gjr6-m4pv): Duplicate Advisory: serde-json-wasm stack overflow during recursive JSON parsing (RUST/serde-json-wasm, RUST/serde-json-wasm) | LOW (CVSS: 3.2) | 2025-07-27 |
| GHSA | [GHSA-GHSA-p444-p2rm-hvrw](https://github.com/advisories/GHSA-p444-p2rm-hvrw): Duplicate Advisory: transpose: Buffer overflow due to integer overflow (RUST/transpose) | MODERATE (CVSS: 4.5) | 2025-07-27 |
| GHSA | [GHSA-GHSA-rm83-pxjx-pr5j](https://github.com/advisories/GHSA-rm83-pxjx-pr5j): Duplicate Advisory: CosmWasm affected by arithmetic overflows (RUST/cosmwasm-std, RUST/cosmwasm-std) | LOW (CVSS: 3.7) | 2025-07-27 |
| GHSA | [GHSA-GHSA-4hff-hh47-7788](https://github.com/advisories/GHSA-4hff-hh47-7788): Duplicate Advisory: curve25519-dalek has timing variability in `curve25519-dalek`'s `Scalar29::sub`/`Scalar52::sub` (RUST/curve25519-dalek) | LOW (CVSS: 2.9) | 2025-07-27 |
| GHSA | [GHSA-GHSA-g97w-mw7g-v3jv](https://github.com/advisories/GHSA-g97w-mw7g-v3jv): Duplicate Advisory: Low severity (DoS) vulnerability in sequoia-openpgp (RUST/sequoia-openpgp) | LOW (CVSS: 2.9) | 2025-07-27 |
| GHSA | [GHSA-GHSA-mvw6-62qv-vmqf](https://github.com/advisories/GHSA-mvw6-62qv-vmqf): Koa Open Redirect Vulnerability (NPM/koa) | LOW (CVSS: 3.5) | 2025-07-25 |
| GHSA | [GHSA-GHSA-49jm-g4m8-x53p](https://github.com/advisories/GHSA-49jm-g4m8-x53p): CodeIgniter4 Cross-Site Scripting Vulnerability in debugbar_time Parameter (COMPOSER/codeigniter4/framework) | MODERATE (CVSS: 6.1) | 2025-07-25 |
| GHSA | [GHSA-GHSA-xffm-g5w8-qvg7](https://github.com/advisories/GHSA-xffm-g5w8-qvg7): @eslint/plugin-kit is vulnerable to Regular Expression Denial of Service attacks through ConfigCommentParser (NPM/@eslint/plugin-kit) | LOW (CVSS: 0.0) | 2025-07-18 |
| GHSA | [GHSA-GHSA-9344-p847-qm5c](https://github.com/advisories/GHSA-9344-p847-qm5c): Low severity (DoS) vulnerability in sequoia-openpgp (RUST/sequoia-openpgp) | LOW (CVSS: 2.9) | 2024-06-26 |
| GHSA | [GHSA-GHSA-x4gp-pqpj-f43q](https://github.com/advisories/GHSA-x4gp-pqpj-f43q): curve25519-dalek has timing variability in `curve25519-dalek`'s `Scalar29::sub`/`Scalar52::sub` (RUST/curve25519-dalek) | MODERATE (CVSS: 0.0) | 2024-06-18 |
| GHSA | [GHSA-GHSA-8724-5xmm-w5xq](https://github.com/advisories/GHSA-8724-5xmm-w5xq): CosmWasm affected by arithmetic overflows (RUST/cosmwasm-std, RUST/cosmwasm-std, RUST/cosmwasm-std) | LOW (CVSS: 3.7) | 2024-04-24 |
| GHSA | [GHSA-GHSA-5gmm-6m36-r7jh](https://github.com/advisories/GHSA-5gmm-6m36-r7jh): transpose: Buffer overflow due to integer overflow (RUST/transpose) | MODERATE (CVSS: 4.5) | 2024-04-05 |
| GHSA | [GHSA-GHSA-rr69-rxr6-8qwf](https://github.com/advisories/GHSA-rr69-rxr6-8qwf): serde-json-wasm stack overflow during recursive JSON parsing (RUST/serde-json-wasm, RUST/serde-json-wasm) | HIGH (CVSS: 7.5) | 2024-02-09 |
| GHSA | [GHSA-GHSA-7g9j-g5jg-3vv3](https://github.com/advisories/GHSA-7g9j-g5jg-3vv3): Unauthenticated Nonce Increment in snow (RUST/snow) | LOW (CVSS: 3.1) | 2024-01-24 |
| GHSA | [GHSA-GHSA-r7qv-8r2h-pg27](https://github.com/advisories/GHSA-r7qv-8r2h-pg27): Multiple issues involving quote API in shlex (RUST/shlex) | LOW (CVSS: 3.2) | 2024-01-22 |
| GHSA | [GHSA-GHSA-rrjw-j4m2-mf34](https://github.com/advisories/GHSA-rrjw-j4m2-mf34): gix-transport code execution vulnerability (RUST/gix-transport) | MODERATE (CVSS: 4.1) | 2023-09-25 |
| GHSA | [GHSA-GHSA-w5vr-6qhr-36cc](https://github.com/advisories/GHSA-w5vr-6qhr-36cc): `ed25519-dalek` Double Public Key Signing Function Oracle Attack (RUST/ed25519-dalek) | MODERATE (CVSS: 5.9) | 2023-08-14 |
| GHSA | [GHSA-GHSA-xcf7-rvmh-g6q4](https://github.com/advisories/GHSA-xcf7-rvmh-g6q4): `openssl` `X509VerifyParamRef::set_host` buffer over-read (RUST/openssl) | MODERATE (CVSS: 4.5) | 2023-06-21 |
| GHSA | [GHSA-GHSA-29mf-62xx-28jq](https://github.com/advisories/GHSA-29mf-62xx-28jq): buffered-reader vulnerable to out-of-bounds array access leading to panic (RUST/buffered-reader, RUST/buffered-reader) | LOW (CVSS: 2.9) | 2023-06-06 |
| GHSA | [GHSA-GHSA-25mx-8f3v-8wh7](https://github.com/advisories/GHSA-25mx-8f3v-8wh7): sequoia-openpgp vulnerable to out-of-bounds array access leading to panic (RUST/sequoia-openpgp, RUST/sequoia-openpgp, RUST/sequoia-openpgp) | LOW (CVSS: 2.9) | 2023-06-06 |
| GHSA | [GHSA-GHSA-h47j-hc6x-h3qq](https://github.com/advisories/GHSA-h47j-hc6x-h3qq): Remote Code Execution Vulnerability in NPM mongo-express (NPM/mongo-express) | CRITICAL (CVSS: 10.0) | 2019-12-30 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [e5cf61f](https://github.com/torvalds/linux/commit/e5cf61fa6e2fb9ae6339eaa892612488c966baaf) | Merge tag 'v6.17-rc-smb3-server-fixes' of git://git.samba.org/ksmbd | 2025-07-28 |
| torvalds/linux | [f70d24c](https://github.com/torvalds/linux/commit/f70d24c230bcaa1e95f66252133068a98c895200) | Merge tag 'vfs-6.17-rc1.nsfs' of git://git.kernel.org/pub/scm/linux/kernel/git/vfs/vfs | 2025-07-28 |
| torvalds/linux | [ce3f5bb](https://github.com/torvalds/linux/commit/ce3f5bb7504ca802efa710280a4601a06545bd2e) | Merge tag 'nfsd-6.17' of git://git.kernel.org/pub/scm/linux/kernel/git/cel/linux | 2025-07-28 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28095](https://github.com/openssl/openssl/pull/28095) | crypto: evp: fix potential null pointer dereference in EVP_DigestSign in m_sigver.c | 2025-07-28 |
| openssl/openssl | [#28059](https://github.com/openssl/openssl/pull/28059) | Add array memory allocation routines | 2025-07-28 |

