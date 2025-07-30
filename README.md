# Security Updates Monitor

*Last updated: 2025-07-30 13:36:41 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 12 |
| COMMIT | 5 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-rxmq-m78w-7wmc](https://github.com/advisories/GHSA-rxmq-m78w-7wmc): SixLabors ImageSharp Has Infinite Loop in GIF Decoder When Skipping Malformed Comment Extension Blocks (NUGET/SixLabors.ImageSharp, NUGET/SixLabors.ImageSharp) | MODERATE (CVSS: 5.3) | 2025-07-30 |
| GHSA | [GHSA-GHSA-rrqh-93c8-j966](https://github.com/advisories/GHSA-rrqh-93c8-j966): Ruby SAML DOS vulnerability with large SAML response (RUBYGEMS/ruby-saml) | MODERATE (CVSS: 0.0) | 2025-07-30 |
| GHSA | [GHSA-GHSA-3wwm-hjv7-23r3](https://github.com/advisories/GHSA-3wwm-hjv7-23r3): Pyload log Injection via API /json/add_package in add_name parameter (PIP/pyload-ng) | MODERATE (CVSS: 4.3) | 2025-07-30 |
| GHSA | [GHSA-GHSA-27gp-8389-hm4w](https://github.com/advisories/GHSA-27gp-8389-hm4w): Keycloak Privilege Escalation Vulnerability in Admin Console (FGAPv2 Enabled) (MAVEN/org.keycloak:keycloak-services) | MODERATE (CVSS: 6.5) | 2025-07-30 |
| GHSA | [GHSA-GHSA-xhpr-465j-7p9q](https://github.com/advisories/GHSA-xhpr-465j-7p9q): Keycloak phishing attack via email verification step in first login flow (MAVEN/org.keycloak:keycloak-services, MAVEN/org.keycloak:keycloak-services) | MODERATE (CVSS: 5.4) | 2025-07-30 |
| GHSA | [GHSA-GHSA-hq25-vp56-qr86](https://github.com/advisories/GHSA-hq25-vp56-qr86): Bacula-web SQL Injection Vulnerability (COMPOSER/bacula-web/bacula-web) | HIGH (CVSS: 8.1) | 2025-07-29 |
| GHSA | [GHSA-GHSA-jgmv-j7ww-jx2x](https://github.com/advisories/GHSA-jgmv-j7ww-jx2x): Koa Open Redirect via Referrer Header (User-Controlled) (NPM/koa) | LOW (CVSS: 3.5) | 2025-07-29 |
| GHSA | [GHSA-GHSA-75vq-qvhr-7ffr](https://github.com/advisories/GHSA-75vq-qvhr-7ffr): Umbraco Delivery API allows for cached requests to be returned with an invalid API key (NUGET/Umbraco.Cms.Api.Delivery, NUGET/Umbraco.Cms.Api.Delivery, NUGET/Umbraco.Cms.Api.Delivery) | MODERATE (CVSS: 5.3) | 2025-07-29 |
| GHSA | [GHSA-GHSA-4mxg-3p6v-xgq3](https://github.com/advisories/GHSA-4mxg-3p6v-xgq3): Node-SAML SAML Signature Verification Vulnerability (NPM/@node-saml/node-saml) | CRITICAL (CVSS: 10.0) | 2025-07-28 |
| GHSA | [GHSA-GHSA-95jq-xph2-cx9h](https://github.com/advisories/GHSA-95jq-xph2-cx9h): Linkify Allows Prototype Pollution & HTML Attribute Injection (XSS) (NPM/linkifyjs) | HIGH (CVSS: 0.0) | 2025-07-26 |
| GHSA | [GHSA-GHSA-83j7-mhw9-388w](https://github.com/advisories/GHSA-83j7-mhw9-388w): Duplicate Advisory: Keycloak Privilege Escalation Vulnerability in Admin Console (FGAPv2 Enabled) (MAVEN/org.keycloak:keycloak-services) | MODERATE (CVSS: 6.5) | 2025-07-18 |
| GHSA | [GHSA-GHSA-gj52-35xm-gxjh](https://github.com/advisories/GHSA-gj52-35xm-gxjh): Duplicate Advisory: Keycloak phishing attack via email verification step in first login flow (MAVEN/org.keycloak:keycloak-services) | MODERATE (CVSS: 5.4) | 2025-07-10 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [a26321e](https://github.com/torvalds/linux/commit/a26321ee4c935a63c29ed6518f27e38826b36e68) | Merge tag 'hardening-v6.17-rc1-fix1' of git://git.kernel.org/pub/scm/linux/kernel/git/kees/linux | 2025-07-30 |
| torvalds/linux | [94fd446](https://github.com/torvalds/linux/commit/94fd44648dae2a5b6149a41faa0b07928c3e1963) | fortify: Fix incorrect reporting of read buffer size | 2025-07-29 |
| torvalds/linux | [4eee152](https://github.com/torvalds/linux/commit/4eee1520ea845a6d6d82e85498d9412419560871) | Merge tag 'usb-6.17-rc1' of git://git.kernel.org/pub/scm/linux/kernel/git/gregkh/usb | 2025-07-29 |
| chromium/chromium | [27f85dd](https://github.com/chromium/chromium/commit/27f85ddbff8fb2a79a2bc7f0616d0051c1b7052c) | [cpesuggest] Add CPE prefix for third_party/maven/3pp/3pp.pb. | 2025-07-29 |
| openssl/openssl | [daa004d](https://github.com/openssl/openssl/commit/daa004d48438d67241b58592d43c3214dd3a903f) | crypto: evp: fix potential null pointer dereference in EVP_DigestSignUpdate in m_sigver.c | 2025-07-25 |

