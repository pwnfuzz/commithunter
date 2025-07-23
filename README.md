# Security Updates Monitor

*Last updated: 2025-07-23 20:17:12 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 19 |
| PR | 4 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-vmhh-8rxq-fp9g](https://github.com/advisories/GHSA-vmhh-8rxq-fp9g): ImageMagick has XMP profile write that triggers hang due to unbounded loop (NUGET/Magick.NET-Q16-HDRI-OpenMP-arm64, NUGET/Magick.NET-Q16-HDRI-OpenMP-x64, NUGET/Magick.NET-Q16-HDRI-x86) | HIGH (CVSS: 7.5) | 2025-07-23 |
| GHSA | [GHSA-GHSA-269j-37ww-cmh3](https://github.com/advisories/GHSA-269j-37ww-cmh3): Mezzanine CMS vulnerable to Cross-site Scripting (PIP/Mezzanine) | MODERATE (CVSS: 4.8) | 2025-07-23 |
| GHSA | [GHSA-GHSA-9h3q-32c7-r533](https://github.com/advisories/GHSA-9h3q-32c7-r533): private-ip vulnerable to Server-Side Request Forgery (NPM/private-ip) | HIGH (CVSS: 8.2) | 2025-07-23 |
| GHSA | [GHSA-GHSA-h27m-3qw8-3pw8](https://github.com/advisories/GHSA-h27m-3qw8-3pw8): Possible ORM Leak Vulnerability in the Harbor (GO/github.com/goharbor/harbor, GO/github.com/goharbor/harbor, GO/github.com/goharbor/harbor) | MODERATE (CVSS: 4.9) | 2025-07-23 |
| GHSA | [GHSA-GHSA-rrf6-pxg8-684g](https://github.com/advisories/GHSA-rrf6-pxg8-684g): FastAPI Guard has a regex bypass (PIP/fastapi-guard) | HIGH (CVSS: 0.0) | 2025-07-23 |
| GHSA | [GHSA-GHSA-x9hg-5q6g-q3jr](https://github.com/advisories/GHSA-x9hg-5q6g-q3jr): Ollama vulnerable to Cross-Domain Token Exposure (GO/github.com/ollama/ollama) | MODERATE (CVSS: 6.9) | 2025-07-22 |
| GHSA | [GHSA-GHSA-h7x8-jv97-fvvm](https://github.com/advisories/GHSA-h7x8-jv97-fvvm): Dagster Local File Inclusion vulnerability (PIP/dagster) | MODERATE (CVSS: 6.6) | 2025-07-22 |
| GHSA | [GHSA-GHSA-2gxp-6r36-m97r](https://github.com/advisories/GHSA-2gxp-6r36-m97r): Cadwyn vulnerable to XSS on the docs page (PIP/cadwyn) | HIGH (CVSS: 7.6) | 2025-07-21 |
| GHSA | [GHSA-GHSA-xqpg-92fq-grfg](https://github.com/advisories/GHSA-xqpg-92fq-grfg): `pyLoad` has Path Traversal Vulnerability in `json/upload` Endpoint that allows Arbitrary File Write (PIP/pyload-ng) | HIGH (CVSS: 7.5) | 2025-07-21 |
| GHSA | [GHSA-GHSA-54vw-f4xf-f92j](https://github.com/advisories/GHSA-54vw-f4xf-f92j): HAX CMS application pages vulnerable to clickjacking (COMPOSER/elmsln/haxcms, NPM/@haxtheweb/haxcms-nodejs) | MODERATE (CVSS: 4.3) | 2025-07-21 |
| GHSA | [GHSA-GHSA-gq96-8w38-hhj2](https://github.com/advisories/GHSA-gq96-8w38-hhj2): LibreNMS has Authenticated Remote File Inclusion in ajax_form.php that Allows RCE (COMPOSER/librenms/librenms) | HIGH (CVSS: 7.5) | 2025-07-21 |
| GHSA | [GHSA-GHSA-5fpv-5qvh-7cf3](https://github.com/advisories/GHSA-5fpv-5qvh-7cf3): NodeJS version of the HAX CMS application is distributed with Default Secrets (NPM/@haxtheweb/haxcms-nodejs) | HIGH (CVSS: 7.3) | 2025-07-21 |
| GHSA | [GHSA-GHSA-mqcp-p2hv-vw6x](https://github.com/advisories/GHSA-mqcp-p2hv-vw6x): Thor can construct an unsafe shell command from library input. (RUBYGEMS/thor) | LOW (CVSS: 2.8) | 2025-07-20 |
| GHSA | [GHSA-GHSA-m5hw-rhvr-f47c](https://github.com/advisories/GHSA-m5hw-rhvr-f47c): simogeo/filemanager arbitrary file upload vulnerability (COMPOSER/simogeo/filemanager) | CRITICAL (CVSS: 9.8) | 2025-07-18 |
| GHSA | [GHSA-GHSA-46m5-8hpj-p5p5](https://github.com/advisories/GHSA-46m5-8hpj-p5p5): Grafana's insecure DingDing Alert integration exposes sensitive information (GO/github.com/grafana/grafana) | MODERATE (CVSS: 4.3) | 2025-07-17 |
| GHSA | [GHSA-GHSA-65gg-3w2w-hr4h](https://github.com/advisories/GHSA-65gg-3w2w-hr4h): Podman Improper Certificate Validation; machine missing TLS verification (GO/github.com/containers/podman/v4, GO/github.com/containers/podman/v5) | HIGH (CVSS: 8.4) | 2025-06-25 |
| GHSA | [GHSA-GHSA-w69q-w4h4-2fx8](https://github.com/advisories/GHSA-w69q-w4h4-2fx8): Reverb use after free vulnerability (PIP/dm-reverb-nightly, PIP/dm-reverb) | MODERATE (CVSS: 6.0) | 2024-09-19 |
| GHSA | [GHSA-GHSA-qjvf-8748-9w7h](https://github.com/advisories/GHSA-qjvf-8748-9w7h): github.com/google/nftable IP addresses were encoded in the wrong byte order (GO/github.com/google/nftables) | MODERATE (CVSS: 5.6) | 2024-07-04 |
| GHSA | [GHSA-GHSA-rcm2-22f3-pqv3](https://github.com/advisories/GHSA-rcm2-22f3-pqv3): Firebase vulnerable to CRSF attack (NPM/firebase-tools) | LOW (CVSS: 2.6) | 2024-05-02 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [#1171](https://github.com/torvalds/linux/pull/1171) | Begin Rewrite in Java to be truly Enterprise:tm:-ready. | 2025-07-23 |
| wazuh/wazuh | [#31046](https://github.com/wazuh/wazuh/pull/31046) | Fix API secure headers | 2025-07-23 |
| wazuh/wazuh | [#30494](https://github.com/wazuh/wazuh/pull/30494) | Fix cluster restart race condition | 2025-07-23 |
| langflow-ai/langflow | [#9057](https://github.com/langflow-ai/langflow/pull/9057) | docs: langflow 1.5 auto-login security doc | 2025-07-23 |

