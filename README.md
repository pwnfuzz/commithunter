# Security Updates Monitor

*Last updated: 2025-08-20 22:12:28 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 6 |
| COMMIT | 3 |
| PR | 4 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-vq9x-w82r-rhmc](https://github.com/advisories/GHSA-vq9x-w82r-rhmc): Soosyze CMS's /user/login endpoint missing rate-limiting and lockout mechanisms (COMPOSER/soosyze/soosyze) | HIGH (CVSS: 5.4) | 2025-08-13 |
| GHSA | [GHSA-GHSA-47ww-ff84-4jrg](https://github.com/advisories/GHSA-47ww-ff84-4jrg): Cosmos SDK: x/group can halt when erroring in EndBlocker (GO/github.com/cosmos/cosmos-sdk, GO/github.com/cosmos/cosmos-sdk) | HIGH (CVSS: 0.0) | 2025-03-12 |
| GHSA | [GHSA-GHSA-8vmr-h7h5-cqhg](https://github.com/advisories/GHSA-8vmr-h7h5-cqhg): matrix-media-repo (MMR) allows unauthenticated writes to the media repository, which may allow planting of problematic content (GO/github.com/t2bot/matrix-media-repo) | MODERATE (CVSS: 5.3) | 2025-01-16 |
| GHSA | [GHSA-GHSA-rcxc-wjgw-579r](https://github.com/advisories/GHSA-rcxc-wjgw-579r): Matrix Media Repo (MMR) allows untrusted file formats can be thumbnailed, invoking potentially further untrusted decoders (GO/github.com/t2bot/matrix-media-repo) | MODERATE (CVSS: 6.8) | 2025-01-16 |
| GHSA | [GHSA-GHSA-gp86-q8hg-fpxj](https://github.com/advisories/GHSA-gp86-q8hg-fpxj): matrix-media-repo (MMR) allows a denial of service through memory exhaustion (GO/github.com/t2bot/matrix-media-repo) | MODERATE (CVSS: 5.3) | 2025-01-16 |
| GHSA | [GHSA-GHSA-r6jg-jfv6-2fjv](https://github.com/advisories/GHSA-r6jg-jfv6-2fjv): Matrix Media Repo (MMR) allows Server-Side Request Forgery (SSRF) on redirects and federation (GO/github.com/t2bot/matrix-media-repo) | MODERATE (CVSS: 5.0) | 2025-01-16 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [0cbd506](https://github.com/chromium/chromium/commit/0cbd506a1712a02f9abad68492bf5aba8b7d54e8) | Fix use-after-free in StructuredMetricsServiceTest teardown. | 2025-08-20 |
| chromium/chromium | [d4f1458](https://github.com/chromium/chromium/commit/d4f145860ab27a0cf916180ebd405c93ce49a7ef) | Fix use-after-free in `OnRefreshTokenRevoked` | 2025-08-20 |
| chromium/chromium | [ec320a6](https://github.com/chromium/chromium/commit/ec320a6124801de351083c8e6d981e49a9ac574d) | [cpesuggest] Add CPE prefix for third_party/android_deps/autorolled/committed/libs/com_google_guava_guava/README.chromium. | 2025-08-20 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| erlang/otp | [#9790](https://github.com/erlang/otp/pull/9790) | otp scan PRs for vulnerabilities | 2025-08-20 |
| erlang/otp | [#10095](https://github.com/erlang/otp/pull/10095) | Fix for httpd CGI scripts | 2025-08-20 |
| erlang/otp | [#10110](https://github.com/erlang/otp/pull/10110) | security: Update OTP version | 2025-08-20 |
| langflow-ai/langflow | [#9441](https://github.com/langflow-ai/langflow/pull/9441) | fix: update CORS configuration and add env vars to allow for user control | 2025-08-20 |

