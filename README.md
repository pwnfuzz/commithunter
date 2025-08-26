# Security Updates Monitor

*Last updated: 2025-08-26 20:15:51 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 18 |
| COMMIT | 2 |
| PR | 2 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-cfmv-h8fx-85m7](https://github.com/advisories/GHSA-cfmv-h8fx-85m7): xml2rfc has an arbitrary file read vulnerability (PIP/xml2rfc) | HIGH (CVSS: 0.0) | 2025-08-26 |
| GHSA | [GHSA-GHSA-7753-xrfw-ch36](https://github.com/advisories/GHSA-7753-xrfw-ch36): LlamaIndex affected by a Denial of Service (DOS) in JSONReader (PIP/llama-index-core) | HIGH (CVSS: 8.6) | 2025-08-26 |
| GHSA | [GHSA-GHSA-mxvv-97wh-cfmm](https://github.com/advisories/GHSA-mxvv-97wh-cfmm): ImageMagick (WriteBMPImage): 32-bit integer overflow when writing BMP scanline stride → heap buffer overflow (NUGET/Magick.NET-Q8-x86, NUGET/Magick.NET-Q8-AnyCPU, NUGET/Magick.NET-Q16-x86) | HIGH (CVSS: 7.5) | 2025-08-26 |
| GHSA | [GHSA-GHSA-9ccg-6pjw-x645](https://github.com/advisories/GHSA-9ccg-6pjw-x645): ImageMagick has a Format String Bug in InterpretImageFilename leads to arbitrary code execution (NUGET/Magick.NET-Q8-x86, NUGET/Magick.NET-Q8-x64, NUGET/Magick.NET-Q8-arm64) | HIGH (CVSS: 7.5) | 2025-08-26 |
| GHSA | [GHSA-GHSA-fh55-q5pj-pxgw](https://github.com/advisories/GHSA-fh55-q5pj-pxgw): ImageMagick affected by divide-by-zero in ThumbnailImage via montage -geometry ":" leads to crash (NUGET/Magick.NET-Q8-x86, NUGET/Magick.NET-Q8-x64, NUGET/Magick.NET-Q8-arm64) | LOW (CVSS: 3.7) | 2025-08-26 |
| GHSA | [GHSA-GHSA-pw25-c82r-75mm](https://github.com/advisories/GHSA-pw25-c82r-75mm): request-filtering-agent SSRF Bypass via HTTPS Requests to 127.0.0.1 (NPM/request-filtering-agent) | MODERATE (CVSS: 0.0) | 2025-08-25 |
| GHSA | [GHSA-GHSA-rx7m-68vc-ppxh](https://github.com/advisories/GHSA-rx7m-68vc-ppxh): PhpSpreadsheet vulnerable to SSRF when reading and displaying a processed HTML document in the browser (COMPOSER/phpoffice/phpspreadsheet, COMPOSER/phpoffice/phpspreadsheet, COMPOSER/phpoffice/phpspreadsheet) | HIGH (CVSS: 0.0) | 2025-08-25 |
| GHSA | [GHSA-GHSA-mqh4-2mm8-g7w9](https://github.com/advisories/GHSA-mqh4-2mm8-g7w9): Adminer PHP Object Injection issue leads to Denial of Service (COMPOSER/vrana/adminer) | HIGH (CVSS: 8.6) | 2025-08-25 |
| GHSA | [GHSA-GHSA-5c4f-pxmx-xcm4](https://github.com/advisories/GHSA-5c4f-pxmx-xcm4): Apache Cassandra: User with MODIFY permission on ALL KEYSPACES can escalate privileges to superuser via unsafe actions (4.0.16 only) (MAVEN/org.apache.cassandra:cassandra-all) | HIGH (CVSS: 8.8) | 2025-08-25 |
| GHSA | [GHSA-GHSA-95v9-hv42-pwrj](https://github.com/advisories/GHSA-95v9-hv42-pwrj): gnark is vulnerable to signature malleability in EdDSA and ECDSA due to missing scalar checks (GO/github.com/consensys/gnark) | HIGH (CVSS: 0.0) | 2025-08-22 |
| GHSA | [GHSA-GHSA-cpq7-6gpm-g9rc](https://github.com/advisories/GHSA-cpq7-6gpm-g9rc): cipher-base is missing type checks, leading to hash rewind and passing on crafted data (NPM/cipher-base) | CRITICAL (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-95m3-7q98-8xr5](https://github.com/advisories/GHSA-95m3-7q98-8xr5): sha.js is missing type checks leading to hash rewind and passing on crafted data (NPM/sha.js) | CRITICAL (CVSS: 0.0) | 2025-08-21 |
| GHSA | [GHSA-GHSA-xr97-25v7-hc2q](https://github.com/advisories/GHSA-xr97-25v7-hc2q): UnoPim has Stored Cross-site Scripting vulnerability in user creation functionality (COMPOSER/unopim/unopim) | MODERATE (CVSS: 6.8) | 2025-08-21 |
| GHSA | [GHSA-GHSA-4xg4-54hm-9j77](https://github.com/advisories/GHSA-4xg4-54hm-9j77): Gokapi has stored XSS vulnerability in friendly name for API keys (GO/github.com/forceu/gokapi, GO/github.com/forceu/gokapi) | MODERATE (CVSS: 5.4) | 2025-06-03 |
| GHSA | [GHSA-GHSA-95rc-wc32-gm53](https://github.com/advisories/GHSA-95rc-wc32-gm53): Gokapi vulnerable to stored XSS via uploading file with malicious file name (GO/github.com/forceu/gokapi, GO/github.com/forceu/gokapi) | MODERATE (CVSS: 0.0) | 2025-06-03 |
| GHSA | [GHSA-GHSA-wf6c-hrhf-86cw](https://github.com/advisories/GHSA-wf6c-hrhf-86cw): NocoDB Vulnerable to Reflected Cross-Site Scripting on Reset Password Page (NPM/nocodb) | MODERATE (CVSS: 6.1) | 2025-03-06 |
| GHSA | [GHSA-GHSA-jh6x-7xfg-9cq2](https://github.com/advisories/GHSA-jh6x-7xfg-9cq2): Searching Opencast may cause a denial of service (MAVEN/org.opencastproject:opencast-elasticsearch-impl, MAVEN/org.opencastproject:opencast-elasticsearch-impl, MAVEN/org.opencastproject:opencast-elasticsearch-impl) | MODERATE (CVSS: 6.5) | 2024-11-20 |
| GHSA | [GHSA-GHSA-phh4-3hmm-24rx](https://github.com/advisories/GHSA-phh4-3hmm-24rx): Duplicate Advisory: Juju makes Use of Weak Credentials (GO/github.com/juju/juju) | HIGH (CVSS: 8.7) | 2024-10-02 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [01838f0](https://github.com/chromium/chromium/commit/01838f0d7ef96de9d8b25579ab45de9c7af34aed) | Remove insecure HTTP prefixed cookies from DB | 2025-08-26 |
| erlang/otp | [d848fbc](https://github.com/erlang/otp/commit/d848fbc1dab75d5369284a6472baf0eea54c2c5d) | Merge pull request #9790 from kikofernandez/add-vendor-vulnerability-analysis/OTP-19652 | 2025-08-26 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| erlang/otp | [#10095](https://github.com/erlang/otp/pull/10095) | Fix for httpd CGI scripts | 2025-08-26 |
| wazuh/wazuh | [#31571](https://github.com/wazuh/wazuh/pull/31571) | Refactor add support for Amazon Inspector v2 | 2025-08-26 |

