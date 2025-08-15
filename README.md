# Security Updates Monitor

*Last updated: 2025-08-15 19:11:41 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 15 |
| COMMIT | 5 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-3x3q-ghcp-whf7](https://github.com/advisories/GHSA-3x3q-ghcp-whf7): Template Secret leakage in logs in Scaffolder when using `fetch:template` (NPM/@backstage/plugin-scaffolder-backend) | LOW (CVSS: 2.6) | 2025-08-15 |
| GHSA | [GHSA-GHSA-9x9c-ghc5-jhw9](https://github.com/advisories/GHSA-9x9c-ghc5-jhw9): @astrojs/node's trailing slash handling causes open redirect issue (NPM/@astrojs/node) | MODERATE (CVSS: 0.0) | 2025-08-15 |
| GHSA | [GHSA-GHSA-77h3-w9rx-hj3q](https://github.com/advisories/GHSA-77h3-w9rx-hj3q): User-defined implementations of the safe trait scratchpad::Tracking can cause heap buffer overflows (RUST/scratchpad) | MODERATE (CVSS: 0.0) | 2025-08-14 |
| GHSA | [GHSA-GHSA-xqrq-4mgf-ff32](https://github.com/advisories/GHSA-xqrq-4mgf-ff32): Python-Future Module Arbitrary Code Execution via Unintended Import of test.py (PIP/future) | HIGH (CVSS: 0.0) | 2025-08-14 |
| GHSA | [GHSA-GHSA-wm7x-ww72-r77q](https://github.com/advisories/GHSA-wm7x-ww72-r77q): Information Disclosure in Amazon ECS Container Agent (GO/github.com/aws/amazon-ecs-agent) | MODERATE (CVSS: 4.3) | 2025-08-14 |
| GHSA | [GHSA-GHSA-j26p-6wx7-f3pw](https://github.com/advisories/GHSA-j26p-6wx7-f3pw): Youki: If /proc and /sys in the rootfs are symbolic links, they can potentially be exploited to gain access to the host root filesystem. (RUST/youki) | HIGH (CVSS: 7.0) | 2025-08-14 |
| GHSA | [GHSA-GHSA-76r7-hhxj-r776](https://github.com/advisories/GHSA-76r7-hhxj-r776): Active Record logging vulnerable to ANSI escape injection (RUBYGEMS/activerecord, RUBYGEMS/activerecord, RUBYGEMS/activerecord) | MODERATE (CVSS: 0.0) | 2025-08-13 |
| GHSA | [GHSA-GHSA-ggmv-j932-q89q](https://github.com/advisories/GHSA-ggmv-j932-q89q): Chall-Manager's HTTP Gateway is vulnerable to DoS due to missing header timeout (GO/github.com/ctfer-io/chall-manager) | HIGH (CVSS: 7.5) | 2025-07-10 |
| GHSA | [GHSA-GHSA-3gv2-v3jx-r9fh](https://github.com/advisories/GHSA-3gv2-v3jx-r9fh): Chall-Manager is vulnerable to Path Traversal when extracting/decoding a zip archive (GO/github.com/ctfer-io/chall-manager) | HIGH (CVSS: 9.1) | 2025-07-10 |
| GHSA | [GHSA-GHSA-m3r7-8gw7-qwvc](https://github.com/advisories/GHSA-m3r7-8gw7-qwvc): thorsten/phpmyfaq Unintended File Download Triggered by Embedded Frames (COMPOSER/thorsten/phpmyfaq) | MODERATE (CVSS: 4.9) | 2024-12-13 |
| GHSA | [GHSA-GHSA-mrr8-v49w-3333](https://github.com/advisories/GHSA-mrr8-v49w-3333): sweetalert2 contains potentially undesirable behavior (NPM/sweetalert2) | LOW (CVSS: 0.0) | 2023-07-10 |
| GHSA | [GHSA-GHSA-xg68-chx2-253g](https://github.com/advisories/GHSA-xg68-chx2-253g): Prototype Pollution in jquery-deparam (NPM/jquery-deparam) | HIGH (CVSS: 8.8) | 2021-05-24 |
| GHSA | [GHSA-GHSA-95q3-8gr9-gm8w](https://github.com/advisories/GHSA-95q3-8gr9-gm8w): Pillow Denial of Service by Uncontrolled Resource Consumption (PIP/pillow) | HIGH (CVSS: 7.5) | 2021-03-18 |
| GHSA | [GHSA-GHSA-f4w8-cv6p-x6r5](https://github.com/advisories/GHSA-f4w8-cv6p-x6r5): Pillow Denial of Service by Uncontrolled Resource Consumption (PIP/Pillow) | HIGH (CVSS: 7.5) | 2021-03-18 |
| GHSA | [GHSA-GHSA-3wvg-mj6g-m9cv](https://github.com/advisories/GHSA-3wvg-mj6g-m9cv): Pillow Uncontrolled Resource Consumption (PIP/pillow) | HIGH (CVSS: 7.5) | 2021-03-18 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [9cee804](https://github.com/chromium/chromium/commit/9cee804e398ba5b88ea9abf8116e5708cfabce1b) | Reland "Use base::ByteCount in base::SysInfo." | 2025-08-15 |
| chromium/chromium | [c4ec5fb](https://github.com/chromium/chromium/commit/c4ec5fb6abaf159001b9d260d10140b09880bbe3) | Close CollaborationControllerDelegateDesktop dialogs on browser exit | 2025-08-15 |
| chromium/chromium | [504f886](https://github.com/chromium/chromium/commit/504f886b69dfcf169c02f089104c60ee376312c6) | Roll src/third_party/readability/src/ 04fd32f72..1f0ec4268 (6 commits) | 2025-08-15 |
| chromium/chromium | [3bc5890](https://github.com/chromium/chromium/commit/3bc5890e1fd9ba0e25038cf3b75c801dc7e98674) | Roll src/third_party/ffmpeg/ d2d06b12c..9e751092c (470 commits) | 2025-08-14 |
| chromium/chromium | [01ef69c](https://github.com/chromium/chromium/commit/01ef69c2f4a4f9c9415c4eea8786884eb199ff75) | [bedrock] Address UAF issues in ExtensionsMenuCoordinator | 2025-08-14 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| erlang/otp | [#9790](https://github.com/erlang/otp/pull/9790) | otp scan PRs for vulnerabilities | 2025-08-15 |

