# Security Updates Monitor

*Last updated: 2025-08-25 21:13:04 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 16 |
| COMMIT | 1 |
| PR | 4 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-63cx-g855-hvv4](https://github.com/advisories/GHSA-63cx-g855-hvv4): mitmproxy binaries embed a vulnerable python-hyper/h2 dependency (PIP/mitmproxy) | MODERATE (CVSS: 0.0) | 2025-08-25 |
| GHSA | [GHSA-GHSA-847f-9342-265h](https://github.com/advisories/GHSA-847f-9342-265h): h2 allows HTTP Request Smuggling due to illegal characters in headers (PIP/h2) | MODERATE (CVSS: 0.0) | 2025-08-25 |
| GHSA | [GHSA-GHSA-5cmr-4px5-23pc](https://github.com/advisories/GHSA-5cmr-4px5-23pc): XGrammar affected by Denial of Service by infinite recursion grammars (PIP/xgrammar) | HIGH (CVSS: 0.0) | 2025-08-25 |
| GHSA | [GHSA-GHSA-crcq-738g-pqvc](https://github.com/advisories/GHSA-crcq-738g-pqvc): Craft CMS Potential Remote Code Execution via Twig SSTI (COMPOSER/craftcms/cms, COMPOSER/craftcms/cms) | MODERATE (CVSS: 0.0) | 2025-08-25 |
| GHSA | [GHSA-GHSA-6hgw-6x87-578x](https://github.com/advisories/GHSA-6hgw-6x87-578x): ImageMagick has Undefined Behavior (function-type-mismatch) in CloneSplayTree (NUGET/Magick.NET-Q8-x86, NUGET/Magick.NET-Q8-x64, NUGET/Magick.NET-Q8-arm64) | MODERATE (CVSS: 6.1) | 2025-08-25 |
| GHSA | [GHSA-GHSA-qp29-wxp5-wh82](https://github.com/advisories/GHSA-qp29-wxp5-wh82): imagemagick: integer overflows in MNG magnification (NUGET/Magick.NET-Q16-AnyCPU, NUGET/Magick.NET-Q16-HDRI-AnyCPU, NUGET/Magick.NET-Q16-HDRI-OpenMP-arm64) | HIGH (CVSS: 8.8) | 2025-08-25 |
| GHSA | [GHSA-GHSA-4gv9-mp8m-592r](https://github.com/advisories/GHSA-4gv9-mp8m-592r): Langflow Vulnerable to Privilege Escalation via CLI Superuser Creation (Post-RCE) (PIP/langflow-base, PIP/langflow) | HIGH (CVSS: 8.8) | 2025-08-25 |
| GHSA | [GHSA-GHSA-rx7m-68vc-ppxh](https://github.com/advisories/GHSA-rx7m-68vc-ppxh): PhpSpreadsheet vulnerable to SSRF when reading and displaying a processed HTML document in the browser (COMPOSER/phpoffice/phpspreadsheet, COMPOSER/phpoffice/phpspreadsheet, COMPOSER/phpoffice/phpspreadsheet) | HIGH (CVSS: 0.0) | 2025-08-25 |
| GHSA | [GHSA-GHSA-mf9q-87xx-jgvv](https://github.com/advisories/GHSA-mf9q-87xx-jgvv): Liferay Portal allows unrestricted upload of file in the style books component (MAVEN/com.liferay:com.liferay.style.book.web) | MODERATE (CVSS: 0.0) | 2025-08-23 |
| GHSA | [GHSA-GHSA-h8gx-4hhm-w45v](https://github.com/advisories/GHSA-h8gx-4hhm-w45v): Liferay Portal stored cross-site scripting in text field of the web content structure (MAVEN/com.liferay:com.liferay.journal.service) | MODERATE (CVSS: 0.0) | 2025-08-23 |
| GHSA | [GHSA-GHSA-23w4-rpc6-wpcc](https://github.com/advisories/GHSA-23w4-rpc6-wpcc): Liferay Portal ReDoS with Role Name search in KaleoDesignerPortlet (MAVEN/com.liferay:com.liferay.portal.workflow.kaleo.designer.web) | MODERATE (CVSS: 0.0) | 2025-08-23 |
| GHSA | [GHSA-GHSA-6hj4-v2qp-cqr2](https://github.com/advisories/GHSA-6hj4-v2qp-cqr2): Liferay Portal allows open redirect in /c/portal/edit_info_item parameter redirect (MAVEN/com.liferay:com.liferay.info.impl) | MODERATE (CVSS: 0.0) | 2025-08-23 |
| GHSA | [GHSA-GHSA-rvmf-jw8g-r35r](https://github.com/advisories/GHSA-rvmf-jw8g-r35r): Liferay Portal vulnerable to Stored XSS in Components portlet (MAVEN/com.liferay:com.liferay.plugins.admin.web) | MODERATE (CVSS: 0.0) | 2025-08-23 |
| GHSA | [GHSA-GHSA-cv9j-mg9w-v7wm](https://github.com/advisories/GHSA-cv9j-mg9w-v7wm): Liferay Portal JSONWS API endpoint shares sensitive information (MAVEN/com.liferay.portal:com.liferay.portal.impl) | MODERATE (CVSS: 0.0) | 2025-08-23 |
| GHSA | [GHSA-GHSA-h4m4-xp33-37mj](https://github.com/advisories/GHSA-h4m4-xp33-37mj): Liferay Portal vulnerable to Reflected XSS with the referer and forward parameter (MAVEN/com.liferay.portal:com.liferay.portal.kernel) | MODERATE (CVSS: 0.0) | 2025-08-23 |
| GHSA | [GHSA-GHSA-3h7r-4xxj-3mfm](https://github.com/advisories/GHSA-3h7r-4xxj-3mfm): Liferay Portal Reflected XSS in CKeditor 4.21.0 endpoint (NPM/liferay-ckeditor, MAVEN/com.liferay:com.liferay.frontend.js.dependencies.web, MAVEN/com.liferay:com.liferay.frontend.editor.ckeditor.web) | MODERATE (CVSS: 0.0) | 2025-08-22 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [dc3fe74](https://github.com/chromium/chromium/commit/dc3fe7400a8b1c45d7e3ff2cd43d945c188602ab) | Reapply "Roll protobuf to v32." | 2025-08-25 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| erlang/otp | [#9790](https://github.com/erlang/otp/pull/9790) | otp scan PRs for vulnerabilities | 2025-08-25 |
| wazuh/wazuh | [#31517](https://github.com/wazuh/wazuh/pull/31517) | Fix literal parser dangling std::string_view capture, and add regression test in 6.0.0 | 2025-08-25 |
| wazuh/wazuh | [#31511](https://github.com/wazuh/wazuh/pull/31511) | Fix literal parser dangling std::string_view capture, and add regression test | 2025-08-25 |
| langflow-ai/langflow | [#9474](https://github.com/langflow-ai/langflow/pull/9474) | docs: troubleshooting backlog items | 2025-08-25 |

