# Security Updates Monitor

*Last updated: 2025-08-19 20:16:10 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 9 |
| COMMIT | 4 |
| PR | 5 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-xf8x-j4p2-f749](https://github.com/advisories/GHSA-xf8x-j4p2-f749): Astro allows unauthorized third-party images in _image endpoint (NPM/astro, NPM/@astrojs/node, NPM/astro) | MODERATE (CVSS: 0.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-hfmv-hhh3-43f2](https://github.com/advisories/GHSA-hfmv-hhh3-43f2): Stored XSS in n8n Form Trigger allows Account Takeover via injected iframe and video/source (NPM/n8n) | HIGH (CVSS: 8.7) | 2025-08-19 |
| GHSA | [GHSA-GHSA-qp7j-x725-g67f](https://github.com/advisories/GHSA-qp7j-x725-g67f): HydrAIDE Authentication Bypass Vulnerability (GO/github.com/hydraide/hydraide, GO/github.com/hydraide/hydraide) | CRITICAL (CVSS: 10.0) | 2025-08-19 |
| GHSA | [GHSA-GHSA-xfp8-x3j6-h67v](https://github.com/advisories/GHSA-xfp8-x3j6-h67v): ExpressGateway Cross-Site Scripting Vulnerability in lib/rest/routes/apps.js (NPM/express-gateway) | LOW (CVSS: 3.5) | 2025-08-18 |
| GHSA | [GHSA-GHSA-q4rg-7cjj-5r86](https://github.com/advisories/GHSA-q4rg-7cjj-5r86): ExpressGateway Cross-Site Scripting Vulnerability in lib/rest/routes/users.js (NPM/express-gateway) | LOW (CVSS: 3.5) | 2025-08-18 |
| GHSA | [GHSA-GHSA-3p2m-574v-v257](https://github.com/advisories/GHSA-3p2m-574v-v257): Liferay Portal Vulnerable to Cross-Site Scripting (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-18 |
| GHSA | [GHSA-GHSA-g4wg-mpfg-x2q6](https://github.com/advisories/GHSA-g4wg-mpfg-x2q6): Liferay Portal Login Bypass Vulnerability (MAVEN/com.liferay.portal:release.portal.bom) | LOW (CVSS: 0.0) | 2025-08-18 |
| GHSA | [GHSA-GHSA-v6xr-v2qg-h22h](https://github.com/advisories/GHSA-v6xr-v2qg-h22h): Liferay Portal Vulnerable to Insecure Direct Object Reference (MAVEN/com.liferay:com.liferay.roles.selector.web) | MODERATE (CVSS: 0.0) | 2025-08-18 |
| GHSA | [GHSA-GHSA-qppj-fm5r-hxr3](https://github.com/advisories/GHSA-qppj-fm5r-hxr3): HTTP/2 Stream Cancellation Attack (MAVEN/org.apache.tomcat:tomcat-coyote, MAVEN/org.apache.tomcat:tomcat-coyote, MAVEN/org.apache.tomcat:tomcat-coyote) | MODERATE (CVSS: 5.3) | 2023-10-10 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [055f213](https://github.com/torvalds/linux/commit/055f213075fbfa8e950bed8f2c50d01ac71bbf37) | Merge tag 'vfs-6.17-rc3.fixes' of git://git.kernel.org/pub/scm/linux/kernel/git/vfs/vfs | 2025-08-19 |
| postgres/postgres | [24225ad](https://github.com/postgres/postgres/commit/24225ad9aafc576295e210026d8ffa9f50d61145) | Pathify RHS unique-ification for semijoin planning | 2025-08-19 |
| chromium/chromium | [33c91c7](https://github.com/chromium/chromium/commit/33c91c7255da81d81a8df067cb9d1ede7bf12a82) | Roll src/third_party/sqlite/src/ cc08c7962..7d348fc79 (45 commits) | 2025-08-19 |
| torvalds/linux | [7375f22](https://github.com/torvalds/linux/commit/7375f22495e7cd1c5b3b5af9dcc4f6dffe34ce49) | fs/buffer: fix use-after-free when call bh_read() helper | 2025-08-11 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#27868](https://github.com/openssl/openssl/pull/27868) | fuzz/provider.c: Add check for OPENSSL_malloc() to avoid potential NU… | 2025-08-19 |
| openssl/openssl | [#28290](https://github.com/openssl/openssl/pull/28290) | Fix double free when reusing PSK sessions | 2025-08-19 |
| erlang/otp | [#10110](https://github.com/erlang/otp/pull/10110) | security: Update OTP version | 2025-08-19 |
| erlang/otp | [#10095](https://github.com/erlang/otp/pull/10095) | Fix for httpd CGI scripts | 2025-08-19 |
| langflow-ai/langflow | [#9441](https://github.com/langflow-ai/langflow/pull/9441) | fix: update CORS configuration and add env vars to allow for user control | 2025-08-19 |

