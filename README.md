# Security Updates Monitor

*Last updated: 2025-07-14 23:15:03 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 6 |
| COMMIT | 2 |
| PR | 3 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-x8c6-gj59-6rx8](https://github.com/advisories/GHSA-x8c6-gj59-6rx8): py-libp2p is vulnerable to DoS attacks through use of large RSA keys (PIP/libp2p) | MODERATE (CVSS: 4.3) | 2025-07-14 |
| GHSA | [GHSA-GHSA-qxh9-qmf2-rhwc](https://github.com/advisories/GHSA-qxh9-qmf2-rhwc): Roundup is vulnerable to XSS through interactions between URLs and issue tracker templates (PIP/roundup) | MODERATE (CVSS: 6.4) | 2025-07-13 |
| GHSA | [GHSA-GHSA-7pgf-ppxw-8624](https://github.com/advisories/GHSA-7pgf-ppxw-8624): Apache Zeppelin exposes server resources to unauthenticated attackers (MAVEN/org.apache.zeppelin:zeppelin-server, MAVEN/org.apache.zeppelin:zeppelin-interpreter) | HIGH (CVSS: 7.5) | 2025-07-12 |
| GHSA | [GHSA-GHSA-wg4x-hf94-fj5v](https://github.com/advisories/GHSA-wg4x-hf94-fj5v): Liferay Portal and Liferay DXP vulnerable to email spam via lack of flagging rate (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom) | MODERATE (CVSS: 4.3) | 2022-05-24 |
| GHSA | [GHSA-GHSA-822f-jfpg-hg7h](https://github.com/advisories/GHSA-822f-jfpg-hg7h): Liferay Portal and Liferay DXP fails to check permissions to view sites/groups (MAVEN/com.liferay.portal:com.liferay.portal.impl, MAVEN/com.liferay:com.liferay.site.browser.web, MAVEN/com.liferay.portal:release.dxp.bom) | MODERATE (CVSS: 4.3) | 2022-04-20 |
| GHSA | [GHSA-GHSA-jp3m-vh3g-6ggp](https://github.com/advisories/GHSA-jp3m-vh3g-6ggp): Liferay Portal and Liferay DXP fails to properly import users from LDAP (MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay:com.liferay.portal.security.ldap.impl) | HIGH (CVSS: 7.5) | 2022-03-04 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [ae198fc](https://github.com/chromium/chromium/commit/ae198fc44c04b9574a8fdef16a39b1b4d13018f9) | Fix use-after-free crash in ChromeOS notification handling | 2025-07-14 |
| chromium/chromium | [09bc93a](https://github.com/chromium/chromium/commit/09bc93a2c04f61ce4e9ed27c05084c16d6260cc4) | Fix read of uninitialized memory in MemoryConsumerTraitsTest.OutOfRange | 2025-07-14 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| langflow-ai/langflow | [#8363](https://github.com/langflow-ai/langflow/pull/8363) | Updated .github/actions/install-playwright/action.yml to fix security vulnerability [yaml.github-actions.security.run-shell-injection.run-shell-injection] | 2025-07-14 |
| langflow-ai/langflow | [#8530](https://github.com/langflow-ai/langflow/pull/8530) | build(deps): bump brace-expansion from 1.1.11 to 1.1.12 in /scripts/aws | 2025-07-14 |
| langflow-ai/langflow | [#9020](https://github.com/langflow-ai/langflow/pull/9020) | Feat/OAuth Single Sign-On Implementation with Google and Microsoft AD (Entra ID) | 2025-07-14 |

