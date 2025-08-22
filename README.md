# Security Updates Monitor

*Last updated: 2025-08-22 19:11:19 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 21 |
| COMMIT | 2 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-vv6j-3g6g-2pvj](https://github.com/advisories/GHSA-vv6j-3g6g-2pvj): Picklescan missing detection when calling pytorch function torch.utils._config_module.load_config (PIP/picklescan) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-vr7h-p6mm-wpmh](https://github.com/advisories/GHSA-vr7h-p6mm-wpmh): Picklescan missing detection when calling pytorch function torch.jit.unsupported_tensor_ops.execWrapper (PIP/picklescan) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-h3qp-7fh3-f8h4](https://github.com/advisories/GHSA-h3qp-7fh3-f8h4): Picklescan missing detection when calling pytorch function torch.utils.data.datapipes.utils.decoder.basichandlers (PIP/picklescan) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-f745-w6jp-hpxx](https://github.com/advisories/GHSA-f745-w6jp-hpxx): Picklescan missing detection when calling pytorch function torch.utils.collect_env.run (PIP/picklescan) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-f4x7-rfwp-v3xw](https://github.com/advisories/GHSA-f4x7-rfwp-v3xw): Picklescan missing detection when calling pytorch function torch.fx.experimental.symbolic_shapes.ShapeEnv.evaluate_guards_expression (PIP/picklescan) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-86cj-95qr-2p4f](https://github.com/advisories/GHSA-86cj-95qr-2p4f): Picklescan missing detection when calling pytorch function torch._dynamo.guards.GuardBuilder.get (PIP/picklescan) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-4r9r-ch6f-vxmx](https://github.com/advisories/GHSA-4r9r-ch6f-vxmx): Picklescan missing detection when calling pytorch function torch.utils.bottleneck.__main__.run_cprofile (PIP/picklescan) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-r367-q549-pgr5](https://github.com/advisories/GHSA-r367-q549-pgr5): Liferay Portal Reflected Cross-Site Scripting Vulnerability via Form Container (MAVEN/com.liferay:com.liferay.layout.taglib) | LOW (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-qpp6-f3qj-rggq](https://github.com/advisories/GHSA-qpp6-f3qj-rggq): Liferay Portal's Unlimited File Upload Could Result in DoS (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-74rg-6f92-g6wx](https://github.com/advisories/GHSA-74rg-6f92-g6wx): UnoPim has CSV Injection on Quick Export feature (COMPOSER/unopim/unopim) | HIGH (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-8p2f-fx4q-75cx](https://github.com/advisories/GHSA-8p2f-fx4q-75cx): UnoPim has Broken Access Control (COMPOSER/unopim/unopim) | HIGH (CVSS: 8.1) | 2025-08-22 |
| GHSA | [GHSA-GHSA-gcqf-pxgg-gw8q](https://github.com/advisories/GHSA-gcqf-pxgg-gw8q): Dpanel has an arbitrary file read vulnerability (GO/github.com/donknap/dpanel) | MODERATE (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-pj6f-rc94-gw53](https://github.com/advisories/GHSA-pj6f-rc94-gw53): Mattermost Fails to Sanitize File Names (GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost-server) | MODERATE (CVSS: 4.3) | 2025-08-21 |
| GHSA | [GHSA-GHSA-58cq-8wm2-6m87](https://github.com/advisories/GHSA-58cq-8wm2-6m87): Liferay Portal Stored Cross-Site Scripting Vulnerability via GroupPagesPortlet_type Parameter (MAVEN/com.liferay:com.liferay.layout.admin.web) | MODERATE (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-q2gv-w583-f2vq](https://github.com/advisories/GHSA-q2gv-w583-f2vq): Liferay Portal Reflected Cross-Site Scripting Vulnerability via snippet Parameter (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-x7p4-v8mj-6fxx](https://github.com/advisories/GHSA-x7p4-v8mj-6fxx): Liferay Portal Username Enumeration Vulnerability (MAVEN/com.liferay.portal:release.portal.bom) | MODERATE (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-8hmm-4crw-vm2c](https://github.com/advisories/GHSA-8hmm-4crw-vm2c): @musistudio/claude-code-router has improper CORS configuration (NPM/@musistudio/claude-code-router) | HIGH (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-pp7p-q8fx-2968](https://github.com/advisories/GHSA-pp7p-q8fx-2968): vite-plugin-static-copy files not included in `src` are possible to access with a crafted request (NPM/vite-plugin-static-copy, NPM/vite-plugin-static-copy) | MODERATE (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-287x-6r2h-f9mw](https://github.com/advisories/GHSA-287x-6r2h-f9mw): UnoPim vulnerable to CSRF on Product edit feature and creation of other types (COMPOSER/unopim/unopim) | MODERATE (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-v22v-xwh7-2vrm](https://github.com/advisories/GHSA-v22v-xwh7-2vrm): UnoPim vulnerable to remote code execution through Arbitrary File upload (COMPOSER/unopim/unopim) | HIGH (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-xr97-25v7-hc2q](https://github.com/advisories/GHSA-xr97-25v7-hc2q): UnoPim has Stored Cross-site Scripting vulnerability in user creation functionality (COMPOSER/unopim/unopim) | HIGH (CVSS: 8.0) | 2025-08-21 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [cf6fc5e](https://github.com/torvalds/linux/commit/cf6fc5eefc5bbbbff92a085039ff74cdbd065c29) | Merge tag 's390-6.17-3' of git://git.kernel.org/pub/scm/linux/kernel/git/s390/linux | 2025-08-22 |
| torvalds/linux | [9a36b58](https://github.com/torvalds/linux/commit/9a36b58a88f62398dbd005e5f3648f257ae2b9b4) | Merge tag 'spi-fix-v6.17-rc2' of git://git.kernel.org/pub/scm/linux/kernel/git/broonie/spi | 2025-08-21 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| langflow-ai/langflow | [#9474](https://github.com/langflow-ai/langflow/pull/9474) | docs: troubleshooting backlog items | 2025-08-22 |

