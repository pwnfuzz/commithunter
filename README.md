# Security Updates Monitor

*Last updated: 2025-07-10 22:14:04 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 16 |
| COMMIT | 2 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-ggmv-j932-q89q](https://github.com/advisories/GHSA-ggmv-j932-q89q): Chall-Manager's HTTP Gateway is vulnerable to DoS due to missing header timeout (GO/github.com/ctfer-io/chall-manager) | HIGH (CVSS: 0.0) | 2025-07-10 |
| GHSA | [GHSA-GHSA-r7fm-3pqm-ww5w](https://github.com/advisories/GHSA-r7fm-3pqm-ww5w): Chall-Manager's scenario decoding process does not check for zip bombs (GO/github.com/ctfer-io/chall-manager) | HIGH (CVSS: 0.0) | 2025-07-10 |
| GHSA | [GHSA-GHSA-3gv2-v3jx-r9fh](https://github.com/advisories/GHSA-3gv2-v3jx-r9fh): Chall-Manager is vulnerable to Path Traversal when extracting/decoding a zip archive (GO/github.com/ctfer-io/chall-manager) | HIGH (CVSS: 0.0) | 2025-07-10 |
| GHSA | [GHSA-GHSA-54xv-94qv-2gfg](https://github.com/advisories/GHSA-54xv-94qv-2gfg): @pdfme/common vulnerable to to XSS and Prototype Pollution through its expression evaluation (NPM/@pdfme/common) | MODERATE (CVSS: 6.1) | 2025-07-10 |
| GHSA | [GHSA-GHSA-275g-g844-73jh](https://github.com/advisories/GHSA-275g-g844-73jh): Matrix Rust SDK vulnerable to SQL Injection through its EventCache implementation (RUST/matrix-sdk) | MODERATE (CVSS: 0.0) | 2025-07-10 |
| GHSA | [GHSA-GHSA-q8p4-vw42-66gh](https://github.com/advisories/GHSA-q8p4-vw42-66gh): Jenkins Apica Loadtest Plugin vulnerability exposes authentication tokens (MAVEN/com.apica:ApicaLoadtest) | MODERATE (CVSS: 4.3) | 2025-07-09 |
| GHSA | [GHSA-GHSA-28j3-hphh-cjr8](https://github.com/advisories/GHSA-28j3-hphh-cjr8): Jenkins Apica Loadtest Plugin vulnerability exposes authentication tokens (MAVEN/com.apica:ApicaLoadtest) | MODERATE (CVSS: 4.3) | 2025-07-09 |
| GHSA | [GHSA-GHSA-pgrx-5f8q-r5mq](https://github.com/advisories/GHSA-pgrx-5f8q-r5mq): Jenkins IBM Cloud DevOps Plugin vulnerability exposes SonarQube authentication tokens (MAVEN/com.ibm.devops:ibm-cloud-devops) | MODERATE (CVSS: 4.3) | 2025-07-09 |
| GHSA | [GHSA-GHSA-jxwj-qccf-4896](https://github.com/advisories/GHSA-jxwj-qccf-4896): Jenkins IFTTT Build Notifier Plugin vulnerability exposes IFTTT Maker Channel Keys (MAVEN/org.jenkins-ci.plugins:ifttt-build-notifier) | MODERATE (CVSS: 4.3) | 2025-07-09 |
| GHSA | [GHSA-GHSA-qr9h-j6xg-2j72](https://github.com/advisories/GHSA-qr9h-j6xg-2j72): Qwik's unhandled exception vulnerabilty can cause server crashes from malicious requests (NPM/@builder.io/qwik-city) | CRITICAL (CVSS: 0.0) | 2025-07-09 |
| GHSA | [GHSA-GHSA-557j-xg8c-q2mm](https://github.com/advisories/GHSA-557j-xg8c-q2mm): Helm vulnerable to Code Injection through malicious chart.yaml content (GO/helm.sh/helm/v3) | HIGH (CVSS: 8.5) | 2025-07-08 |
| GHSA | [GHSA-GHSA-gq57-v332-7666](https://github.com/advisories/GHSA-gq57-v332-7666): n8n is vulnerable to Improper Authorization through its `/stop` endpoint (NPM/n8n) | MODERATE (CVSS: 4.3) | 2025-07-03 |
| GHSA | [GHSA-GHSA-r26v-98qj-48q9](https://github.com/advisories/GHSA-r26v-98qj-48q9): XXL SSO is vulnerable to an Open Redirect through malicious manipulation of the redirect_url argument  (MAVEN/com.xuxueli:xxl-sso) | LOW (CVSS: 3.5) | 2025-06-26 |
| GHSA | [GHSA-GHSA-79vf-hf9f-j9q8](https://github.com/advisories/GHSA-79vf-hf9f-j9q8): @vue/cli-plugin-pwa Regular Expression Denial of Service vulnerability (NPM/@vue/cli-plugin-pwa) | MODERATE (CVSS: 4.3) | 2025-06-09 |
| GHSA | [GHSA-GHSA-f5xg-cfpj-2mw6](https://github.com/advisories/GHSA-f5xg-cfpj-2mw6): taro-css-to-react-native Regular Expression Denial of Service vulnerability (NPM/taro-css-to-react-native) | MODERATE (CVSS: 4.3) | 2025-06-09 |
| GHSA | [GHSA-GHSA-x5gf-qvw8-r2rm](https://github.com/advisories/GHSA-x5gf-qvw8-r2rm): pm2 Regular Expression Denial of Service vulnerability (NPM/pm2) | LOW (CVSS: 4.3) | 2025-06-09 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [532e92c](https://github.com/chromium/chromium/commit/532e92cca81b0e3fd50ba504d938b68897dccd50) | Prevent origin updates in same-document navigations | 2025-07-10 |
| chromium/chromium | [04faffc](https://github.com/chromium/chromium/commit/04faffcf5d149501c43c3f0c92b2709df5d819e3) | Roll src/third_party/libwebp/src/ 2af6c034a..4fa219123 (54 commits) | 2025-07-10 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| wazuh/wazuh | [#30804](https://github.com/wazuh/wazuh/pull/30804) | Fixed error in database feed manager when wazuh is shutting down | 2025-07-10 |

