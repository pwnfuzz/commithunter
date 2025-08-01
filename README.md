# Security Updates Monitor

*Last updated: 2025-08-01 23:15:32 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 18 |
| COMMIT | 4 |
| PR | 2 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-6c5r-4wfc-3mcx](https://github.com/advisories/GHSA-6c5r-4wfc-3mcx): Hashicorp Vault has Incorrect Validation for Non-CA Certificates (GO/github.com/hashicorp/vault) | MODERATE (CVSS: 6.8) | 2025-08-01 |
| GHSA | [GHSA-GHSA-v6r4-35f9-9rpw](https://github.com/advisories/GHSA-v6r4-35f9-9rpw): Hashicorp Vault has Login MFA Rate Limit Bypass Vulnerability (GO/github.com/hashicorp/vault) | MODERATE (CVSS: 5.7) | 2025-08-01 |
| GHSA | [GHSA-GHSA-qv3p-fmv3-9hww](https://github.com/advisories/GHSA-qv3p-fmv3-9hww): Hashicorp Vault's TOTP Secrets Engine Susceptible to Code Reuse  (GO/github.com/hashicorp/vault) | MODERATE (CVSS: 6.5) | 2025-08-01 |
| GHSA | [GHSA-GHSA-mwgr-84fv-3jh9](https://github.com/advisories/GHSA-mwgr-84fv-3jh9): Hashicorp Vault has an Observable Discrepancy on Existing and Non-Existing Users (GO/github.com/hashicorp/vault) | LOW (CVSS: 3.7) | 2025-08-01 |
| GHSA | [GHSA-GHSA-qgj7-fmq2-6cc4](https://github.com/advisories/GHSA-qgj7-fmq2-6cc4): Hashicorp Vault has Lockout Feature Authentication Bypass (GO/github.com/hashicorp/vault) | MODERATE (CVSS: 5.3) | 2025-08-01 |
| GHSA | [GHSA-GHSA-6h4p-m86h-hhgh](https://github.com/advisories/GHSA-6h4p-m86h-hhgh): Hashicorp Vault has Privilege Escalation Vulnerability (GO/github.com/hashicorp/vault) | HIGH (CVSS: 7.2) | 2025-08-01 |
| GHSA | [GHSA-GHSA-mr4h-qf9j-f665](https://github.com/advisories/GHSA-mr4h-qf9j-f665): Hashicorp Vault has Code Execution Vulnerability via Plugin Configuration (GO/github.com/hashicorp/vault) | CRITICAL (CVSS: 9.1) | 2025-08-01 |
| GHSA | [GHSA-GHSA-2x2j-3c2v-g3c2](https://github.com/advisories/GHSA-2x2j-3c2v-g3c2): Microweber XSS Vulnerability in the homepage Endpoint  (COMPOSER/microweber/microweber) | MODERATE (CVSS: 0.0) | 2025-08-01 |
| GHSA | [GHSA-GHSA-mvj3-hc7j-vp74](https://github.com/advisories/GHSA-mvj3-hc7j-vp74): Microweber has Reflected XSS Vulnerability in the layout Parameter (COMPOSER/microweber/microweber) | MODERATE (CVSS: 6.1) | 2025-08-01 |
| GHSA | [GHSA-GHSA-8357-fjvx-xrm8](https://github.com/advisories/GHSA-8357-fjvx-xrm8): Microweber has Reflected XSS Vulnerability in the id Parameter (COMPOSER/microweber/microweber) | MODERATE (CVSS: 6.1) | 2025-08-01 |
| GHSA | [GHSA-GHSA-85cg-cmq5-qjm7](https://github.com/advisories/GHSA-85cg-cmq5-qjm7): @nestjs/devtools-integration: CSRF to Sandbox Escape Allows for RCE against JS Developers (NPM/@nestjs/devtools-integration) | CRITICAL (CVSS: 0.0) | 2025-08-01 |
| GHSA | [GHSA-GHSA-7qw8-3vmf-gj32](https://github.com/advisories/GHSA-7qw8-3vmf-gj32): MaterialX Null Pointer Dereference in MaterialXCore Shader Generation due to Unchecked implGraphOutput (PIP/MaterialX) | LOW (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-3jhf-gxhr-q4cx](https://github.com/advisories/GHSA-3jhf-gxhr-q4cx): MaterialX Null Pointer Dereference in getShaderNodes due to Unchecked nodeGraph->getOutput return (PIP/MaterialX) | LOW (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-h45x-qhg2-q375](https://github.com/advisories/GHSA-h45x-qhg2-q375): OpenEXR Heap-Based Buffer Overflow in Deep Scanline Parsing via Forged Unpacked Size (PIP/OpenEXR) | HIGH (CVSS: 0.0) | 2025-07-31 |
| GHSA | [GHSA-GHSA-xxmh-rf63-qwjv](https://github.com/advisories/GHSA-xxmh-rf63-qwjv): GitProxy Backfile Parsing Exploit (NPM/@finos/git-proxy) | HIGH (CVSS: 0.0) | 2025-07-30 |
| GHSA | [GHSA-GHSA-qr93-8wwf-22g4](https://github.com/advisories/GHSA-qr93-8wwf-22g4): GitProxy Approval Bypass When Pushing Multiple Branches (NPM/@finos/git-proxy) | HIGH (CVSS: 0.0) | 2025-07-30 |
| GHSA | [GHSA-GHSA-8xq3-w9fx-74rv](https://github.com/advisories/GHSA-8xq3-w9fx-74rv): webfinger.js Blind SSRF Vulnerability (NPM/webfinger.js) | MODERATE (CVSS: 0.0) | 2025-07-28 |
| GHSA | [GHSA-GHSA-w596-4wvx-j9j6](https://github.com/advisories/GHSA-w596-4wvx-j9j6): Withdrawn Advisory: ReDoS in py library when used with subversion  (PIP/py) | HIGH (CVSS: 7.5) | 2022-10-16 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [b80a75c](https://github.com/torvalds/linux/commit/b80a75cf6999fb79971b41eaec7af2bb4b514714) | Merge tag 'hid-for-linus-2025073101' of git://git.kernel.org/pub/scm/linux/kernel/git/hid/hid | 2025-08-01 |
| chromium/chromium | [a1f090c](https://github.com/chromium/chromium/commit/a1f090cfa63df356946367734ffed310be11bf98) | Notify GeolocationSystemPermissionManager observers before destruction | 2025-08-01 |
| chromium/chromium | [44f483d](https://github.com/chromium/chromium/commit/44f483d46d950995bf76f4fa1a7ced6f013136ef) | Roll Dawn from ae947216dca9 to 24eec2f88310 (10 revisions) | 2025-08-01 |
| chromium/chromium | [41905e4](https://github.com/chromium/chromium/commit/41905e418351fe5fa6266f14d109834ada25a78f) | base: Add integer overflow checks in File::Read/Write | 2025-08-01 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| wazuh/wazuh | [#31187](https://github.com/wazuh/wazuh/pull/31187) | Fix authd.pass ACL permissions to match client.keys security level | 2025-08-01 |
| wazuh/wazuh | [#31163](https://github.com/wazuh/wazuh/pull/31163) | Add support for Inspector v2. | 2025-08-01 |

