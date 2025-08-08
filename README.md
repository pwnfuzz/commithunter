# Security Updates Monitor

*Last updated: 2025-08-08 05:24:54 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 11 |
| COMMIT | 2 |
| PR | 5 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-8qf3-x8v5-2pj8](https://github.com/advisories/GHSA-8qf3-x8v5-2pj8): uv allows ZIP payload obfuscation through parsing differentials (PIP/uv) | MODERATE (CVSS: 0.0) | 2025-08-07 |
| GHSA | [GHSA-GHSA-93jv-pvg8-hf3v](https://github.com/advisories/GHSA-93jv-pvg8-hf3v): Ollama allows deletion of arbitrary files (GO/github.com/ollama/ollama) | MODERATE (CVSS: 6.6) | 2025-08-07 |
| GHSA | [GHSA-GHSA-c7p4-hx26-pr73](https://github.com/advisories/GHSA-c7p4-hx26-pr73): JWE is missing AES-GCM authentication tag validation in encrypted JWE (RUBYGEMS/jwe) | CRITICAL (CVSS: 9.1) | 2025-08-07 |
| GHSA | [GHSA-GHSA-m3hh-f9gh-74c2](https://github.com/advisories/GHSA-m3hh-f9gh-74c2): quiche connection ID retirement can trigger an infinite loop (RUST/quiche) | HIGH (CVSS: 0.0) | 2025-08-07 |
| GHSA | [GHSA-GHSA-378x-6p4f-8jgm](https://github.com/advisories/GHSA-378x-6p4f-8jgm): SKOPS Card.get_model happily allows arbitrary code execution (PIP/skops) | HIGH (CVSS: 8.4) | 2025-08-07 |
| GHSA | [GHSA-GHSA-cq8c-xv66-36gw](https://github.com/advisories/GHSA-cq8c-xv66-36gw): Astros's duplicate trailing slash feature leads to an open redirection security issue (NPM/astro) | MODERATE (CVSS: 0.0) | 2025-08-07 |
| GHSA | [GHSA-GHSA-8q6v-474h-whgg](https://github.com/advisories/GHSA-8q6v-474h-whgg): The Thinbus Javascript Secure Remote Password (SRP) Client Generates Fewer Bits of Entropy Than Intended (NPM/thinbus-srp) | MODERATE (CVSS: 0.0) | 2025-08-06 |
| GHSA | [GHSA-GHSA-q82r-2j7m-9rv4](https://github.com/advisories/GHSA-q82r-2j7m-9rv4): github.com/go-acme/lego/v4/acme/api does not enforce HTTPS (GO/github.com/go-acme/lego/v4, GO/github.com/go-acme/lego/v3, GO/github.com/go-acme/lego) | LOW (CVSS: 0.0) | 2025-08-06 |
| GHSA | [GHSA-GHSA-52f5-9888-hmc6](https://github.com/advisories/GHSA-52f5-9888-hmc6): tmp allows arbitrary temporary file / directory write via symbolic link `dir` parameter (NPM/tmp) | LOW (CVSS: 2.5) | 2025-08-06 |
| GHSA | [GHSA-GHSA-6v92-r5mx-h5fx](https://github.com/advisories/GHSA-6v92-r5mx-h5fx): smolagents has Sandbox Escape Vulnerability in the local_python_executor.py Module (PIP/smolagents) | CRITICAL (CVSS: 9.9) | 2025-07-27 |
| GHSA | [GHSA-GHSA-37mw-44qp-f5jm](https://github.com/advisories/GHSA-37mw-44qp-f5jm): Transformers is vulnerable to ReDoS attack through its DonutProcessor class (PIP/transformers) | MODERATE (CVSS: 5.3) | 2025-07-11 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [d61639d](https://github.com/chromium/chromium/commit/d61639d0fda4bf39eefd4e7d9dffb9dde09e029b) | Destroy device bound SessionService in ~URLRequestContext | 2025-08-07 |
| chromium/chromium | [52f3b74](https://github.com/chromium/chromium/commit/52f3b7419bc8892f011643006a1a075b5a7a9c82) | Reset DragDrop window observator to avoid UAF | 2025-08-07 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28184](https://github.com/openssl/openssl/pull/28184) | Fix integer overflow in date_to_julian() call | 2025-08-08 |
| openssl/openssl | [#28059](https://github.com/openssl/openssl/pull/28059) | Add array memory allocation routines | 2025-08-07 |
| erlang/otp | [#9967](https://github.com/erlang/otp/pull/9967) | chore(deps): update dependency microsoft/stl to v17.14 (maint-28) | 2025-08-07 |
| erlang/otp | [#9918](https://github.com/erlang/otp/pull/9918) | chore(deps): update dependency microsoft/stl to v17.14 (master) | 2025-08-07 |
| erlang/otp | [#9946](https://github.com/erlang/otp/pull/9946) | chore(deps): update dependency microsoft/stl to v17.14 (maint) | 2025-08-07 |

