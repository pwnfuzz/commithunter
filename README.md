# Security Updates Monitor

*Last updated: 2025-08-22 21:12:42 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 26 |
| COMMIT | 1 |
| PR | 2 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-fvqv-593q-qp8r](https://github.com/advisories/GHSA-fvqv-593q-qp8r): Liferay Portal Reflected Cross-Site Scripting Vulnerability via PortalUtil.escapeRedirect (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-74rg-6f92-g6wx](https://github.com/advisories/GHSA-74rg-6f92-g6wx): UnoPim has CSV Injection on Quick Export feature (COMPOSER/unopim/unopim) | LOW (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-xwc5-q44v-p6gg](https://github.com/advisories/GHSA-xwc5-q44v-p6gg): Liferay Portal User Enumeration Vulnerability via the Create Account Page (MAVEN/com.liferay:com.liferay.login.web) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-8p2f-fx4q-75cx](https://github.com/advisories/GHSA-8p2f-fx4q-75cx): UnoPim has Broken Access Control (COMPOSER/unopim/unopim) | HIGH (CVSS: 8.1) | 2025-08-22 |
| GHSA | [GHSA-GHSA-gcqf-pxgg-gw8q](https://github.com/advisories/GHSA-gcqf-pxgg-gw8q): Dpanel has an arbitrary file read vulnerability (GO/github.com/donknap/dpanel) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-95v9-hv42-pwrj](https://github.com/advisories/GHSA-95v9-hv42-pwrj): gnark is vulnerable to signature malleability in EdDSA and ECDSA due to missing scalar checks (GO/github.com/consensys/gnark) | HIGH (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-gj8w-ffq9-6828](https://github.com/advisories/GHSA-gj8w-ffq9-6828): JeecgBoot SQL Injection Vulnerability (MAVEN/org.jeecgframework.boot:jeecg-boot-base-core) | MODERATE (CVSS: 6.5) | 2025-08-22 |
| GHSA | [GHSA-GHSA-jfcv-jv9g-2vx2](https://github.com/advisories/GHSA-jfcv-jv9g-2vx2): Bouncy Castle for Java has Uncontrolled Resource Consumption Vulnerability (MAVEN/org.bouncycastle:bctls-fips, MAVEN/org.bouncycastle:bc-fips) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-g6rx-6wfx-gj74](https://github.com/advisories/GHSA-g6rx-6wfx-gj74): Bouncy Castle for Java has Out-of-Bounds Write Vulnerability (MAVEN/org.bouncycastle:bc-fips) | LOW (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-vv6j-3g6g-2pvj](https://github.com/advisories/GHSA-vv6j-3g6g-2pvj): Picklescan missing detection when calling pytorch function torch.utils._config_module.load_config (PIP/picklescan) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-vr7h-p6mm-wpmh](https://github.com/advisories/GHSA-vr7h-p6mm-wpmh): Picklescan missing detection when calling pytorch function torch.jit.unsupported_tensor_ops.execWrapper (PIP/picklescan) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-h3qp-7fh3-f8h4](https://github.com/advisories/GHSA-h3qp-7fh3-f8h4): Picklescan missing detection when calling pytorch function torch.utils.data.datapipes.utils.decoder.basichandlers (PIP/picklescan) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-f745-w6jp-hpxx](https://github.com/advisories/GHSA-f745-w6jp-hpxx): Picklescan missing detection when calling pytorch function torch.utils.collect_env.run (PIP/picklescan) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-f4x7-rfwp-v3xw](https://github.com/advisories/GHSA-f4x7-rfwp-v3xw): Picklescan missing detection when calling pytorch function torch.fx.experimental.symbolic_shapes.ShapeEnv.evaluate_guards_expression (PIP/picklescan) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-86cj-95qr-2p4f](https://github.com/advisories/GHSA-86cj-95qr-2p4f): Picklescan missing detection when calling pytorch function torch._dynamo.guards.GuardBuilder.get (PIP/picklescan) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-4r9r-ch6f-vxmx](https://github.com/advisories/GHSA-4r9r-ch6f-vxmx): Picklescan missing detection when calling pytorch function torch.utils.bottleneck.__main__.run_cprofile (PIP/picklescan) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-r367-q549-pgr5](https://github.com/advisories/GHSA-r367-q549-pgr5): Liferay Portal Reflected Cross-Site Scripting Vulnerability via Form Container (MAVEN/com.liferay:com.liferay.layout.taglib) | LOW (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-qpp6-f3qj-rggq](https://github.com/advisories/GHSA-qpp6-f3qj-rggq): Liferay Portal's Unlimited File Upload Could Result in DoS (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-48cg-9c55-j2q7](https://github.com/advisories/GHSA-48cg-9c55-j2q7): hippo4j Includes Hard Coded Secret Key in JWT Creation (MAVEN/cn.hippo4j:hippo4j-core) | HIGH (CVSS: 8.8) | 2025-08-21 |
| GHSA | [GHSA-GHSA-pj6f-rc94-gw53](https://github.com/advisories/GHSA-pj6f-rc94-gw53): Mattermost Fails to Sanitize File Names (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost-server) | MODERATE (CVSS: 4.3) | 2025-08-21 |
| GHSA | [GHSA-GHSA-58cq-8wm2-6m87](https://github.com/advisories/GHSA-58cq-8wm2-6m87): Liferay Portal Stored Cross-Site Scripting Vulnerability via GroupPagesPortlet_type Parameter (MAVEN/com.liferay:com.liferay.layout.admin.web) | MODERATE (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-q2gv-w583-f2vq](https://github.com/advisories/GHSA-q2gv-w583-f2vq): Liferay Portal Reflected Cross-Site Scripting Vulnerability via snippet Parameter (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-x7p4-v8mj-6fxx](https://github.com/advisories/GHSA-x7p4-v8mj-6fxx): Liferay Portal Username Enumeration Vulnerability (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-gqp3-2cvr-x8m3](https://github.com/advisories/GHSA-gqp3-2cvr-x8m3): Apache Tomcat Improper Resource Shutdown or Release vulnerability (MAVEN/org.apache.tomcat.embed:tomcat-embed-core, MAVEN/org.apache.tomcat.embed:tomcat-embed-core, MAVEN/org.apache.tomcat.embed:tomcat-embed-core) | HIGH (CVSS: 7.5) | 2025-08-13 |
| GHSA | [GHSA-GHSA-hfcf-79gh-f3jc](https://github.com/advisories/GHSA-hfcf-79gh-f3jc): Memos has Cross-Site Scripting (XSS) Vulnerability in Image URLs (GO/github.com/usememos/memos) | MODERATE (CVSS: 0.0) | 2025-07-29 |
| GHSA | [GHSA-GHSA-4jq9-2xhw-jpx7](https://github.com/advisories/GHSA-4jq9-2xhw-jpx7): Java: DoS Vulnerability in JSON-JAVA (MAVEN/org.json:json) | HIGH (CVSS: 7.5) | 2023-11-14 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [cf6fc5e](https://github.com/torvalds/linux/commit/cf6fc5eefc5bbbbff92a085039ff74cdbd065c29) | Merge tag 's390-6.17-3' of git://git.kernel.org/pub/scm/linux/kernel/git/s390/linux | 2025-08-22 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| wazuh/wazuh | [#31514](https://github.com/wazuh/wazuh/pull/31514) | Fix literal parser dangling std::string_view capture, and add regression test in 6.0.0 | 2025-08-22 |
| langflow-ai/langflow | [#9474](https://github.com/langflow-ai/langflow/pull/9474) | docs: troubleshooting backlog items | 2025-08-22 |

