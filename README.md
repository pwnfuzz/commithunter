# Security Updates Monitor

*Last updated: 2025-09-05 19:11:25 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 11 |
| COMMIT | 6 |
| PR | 2 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-fghv-69vj-qj49](https://github.com/advisories/GHSA-fghv-69vj-qj49): Netty vulnerable to request smuggling due to incorrect parsing of chunk extensions (MAVEN/io.netty:netty-codec-http, MAVEN/io.netty:netty-codec-http) | LOW (CVSS: 0.0) | 2025-09-04 |
| GHSA | [GHSA-GHSA-qpr4-c339-7vq8](https://github.com/advisories/GHSA-qpr4-c339-7vq8): Server-Side Request Forgery via /_image endpoint in Astro Cloudflare adapter (NPM/@astrojs/cloudflare) | HIGH (CVSS: 7.2) | 2025-09-04 |
| GHSA | [GHSA-GHSA-786q-9hcg-v9ff](https://github.com/advisories/GHSA-786q-9hcg-v9ff): Argo CD's Project API Token Exposes Repository Credentials (GO/github.com/argoproj/argo-cd/v3, GO/github.com/argoproj/argo-cd/v3, GO/github.com/argoproj/argo-cd/v2) | CRITICAL (CVSS: 10.0) | 2025-09-04 |
| GHSA | [GHSA-GHSA-wp3j-xq48-xpjw](https://github.com/advisories/GHSA-wp3j-xq48-xpjw): podman kube play symlink traversal vulnerability (GO/github.com/containers/podman/v4, GO/github.com/containers/podman/v5) | HIGH (CVSS: 8.1) | 2025-09-04 |
| GHSA | [GHSA-GHSA-8xx5-h6m3-jr33](https://github.com/advisories/GHSA-8xx5-h6m3-jr33): Presta Shop vulnerable to email enumeration  (COMPOSER/prestashop/prestashop) | MODERATE (CVSS: 4.2) | 2025-09-04 |
| GHSA | [GHSA-GHSA-x2jc-989c-47q4](https://github.com/advisories/GHSA-x2jc-989c-47q4): Hexo `include_code` has a path traversal (NPM/hexo) | HIGH (CVSS: 7.5) | 2023-09-08 |
| GHSA | [GHSA-GHSA-hw56-7xj4-7gx6](https://github.com/advisories/GHSA-hw56-7xj4-7gx6): Liferay Portal and Liferay DXP Vulnerable to SQL Injection via Friendly URL Module (MAVEN/com.liferay:com.liferay.friendly.url.service, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.portal.bom) | CRITICAL (CVSS: 9.8) | 2022-11-15 |
| GHSA | [GHSA-GHSA-r5fj-j449-vqw2](https://github.com/advisories/GHSA-r5fj-j449-vqw2): Liferay Portal and Liferay DXP Vulnerable to SQL Injection via the Fragment Module (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay:com.liferay.fragment.service) | CRITICAL (CVSS: 9.8) | 2022-11-15 |
| GHSA | [GHSA-GHSA-gxxj-fhmr-37j9](https://github.com/advisories/GHSA-gxxj-fhmr-37j9): Liferay Portal and Liferay DXP Vulnerable to SQL Injection via the Layout Module (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay:com.liferay.layout.page.template.service) | HIGH (CVSS: 8.8) | 2022-11-15 |
| GHSA | [GHSA-GHSA-vjj4-qwcm-552h](https://github.com/advisories/GHSA-vjj4-qwcm-552h): Inefficient Regular Expression Complexity in Liferay Portal  (MAVEN/com.liferay.portal:release.portal.bom) | HIGH (CVSS: 7.5) | 2022-11-15 |
| GHSA | [GHSA-GHSA-hffx-r282-w2g9](https://github.com/advisories/GHSA-hffx-r282-w2g9): Path Traversal in Liferay Portal (MAVEN/com.liferay.portal:release.portal.bom) | HIGH (CVSS: 7.5) | 2022-11-15 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [4e47e46](https://github.com/torvalds/linux/commit/4e47e46718c466d90f7a452579f9ed1a7c250553) | Merge tag 'pcmcia-6.18' of git://git.kernel.org/pub/scm/linux/kernel/git/brodo/linux | 2025-09-05 |
| erlang/otp | [ae81b2f](https://github.com/erlang/otp/commit/ae81b2f6ff2d541c01242f12cdbd5238aa4b26bd) | Merge pull request #10168 from kikofernandez/kiko/create-automatic-vendor-vulnerability-issue/OTP-19763 | 2025-09-05 |
| chromium/chromium | [3ddf9a1](https://github.com/chromium/chromium/commit/3ddf9a18f5ec781b7ad1c71568333ee052a5ec18) | Roll Dawn from 0567736dfb04 to 95122946d574 (25 revisions) | 2025-09-04 |
| chromium/chromium | [beec7dd](https://github.com/chromium/chromium/commit/beec7dd467c2bf58f0b98719c7da70610a51f823) | Roll src/third_party/libvpx/source/libvpx/ b122dc093..8d00aca60 (5 commits) | 2025-09-04 |
| wazuh/wazuh | [81cc44c](https://github.com/wazuh/wazuh/commit/81cc44c6908c680d2419087ca73ff6d5fcc47fcb) | fix: adjust indentation for policy loading in SecurityConfigurationAssessment::Run() | 2025-09-04 |
| wazuh/wazuh | [f742908](https://github.com/wazuh/wazuh/commit/f742908cc7864ceeee50c0a129e1da98d5163c40) | fix: correct scan logic in SecurityConfigurationAssessment::Run() | 2025-09-03 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| erlang/otp | [#9956](https://github.com/erlang/otp/pull/9956) | chore(deps): update github-actions (maint-28) | 2025-09-05 |
| wazuh/wazuh | [#31599](https://github.com/wazuh/wazuh/pull/31599) | Improve and fix `dpkg` algorithm in version compare | 2025-09-05 |

