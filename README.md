# Security Updates Monitor

*Last updated: 2025-07-09 18:21:01 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 28 |
| COMMIT | 3 |
| PR | 1 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-qr9h-j6xg-2j72](https://github.com/advisories/GHSA-qr9h-j6xg-2j72): Qwik's unhandled exception vulnerabilty can cause server crashes from malicious requests (NPM/@builder.io/qwik-city) | CRITICAL (CVSS: 0.0) | 2025-07-09 |
| GHSA | [GHSA-GHSA-6xpm-ggf7-wc3p](https://github.com/advisories/GHSA-6xpm-ggf7-wc3p): mcp-remote exposed to OS command injection via untrusted MCP server connections (NPM/mcp-remote) | CRITICAL (CVSS: 9.7) | 2025-07-09 |
| GHSA | [GHSA-GHSA-9mp4-77wg-rwx9](https://github.com/advisories/GHSA-9mp4-77wg-rwx9): @clerk/backend Performs Insufficient Verification of Data Authenticity (NPM/@clerk/tanstack-react-start, NPM/@clerk/remix, NPM/@clerk/react-router) | HIGH (CVSS: 7.5) | 2025-07-09 |
| GHSA | [GHSA-GHSA-phhq-63jg-fp7r](https://github.com/advisories/GHSA-phhq-63jg-fp7r): Contrast vulnerability allows arbitrary host data Injection into container VOLUME mount points (GO/github.com/edgelesssys/contrast) | LOW (CVSS: 3.5) | 2025-07-09 |
| GHSA | [GHSA-GHSA-4vc8-wvhw-m5gv](https://github.com/advisories/GHSA-4vc8-wvhw-m5gv): Juju allows arbitrary executable uploads via authenticated endpoint without authorization (GO/github.com/juju/juju) | HIGH (CVSS: 8.8) | 2025-07-09 |
| GHSA | [GHSA-GHSA-r64v-82fh-xc63](https://github.com/advisories/GHSA-r64v-82fh-xc63): Juju vulnerable to sensitive log retrieval via authenticated endpoint without authorization (GO/github.com/juju/juju) | MODERATE (CVSS: 6.5) | 2025-07-09 |
| GHSA | [GHSA-GHSA-24ch-w38v-xmh8](https://github.com/advisories/GHSA-24ch-w38v-xmh8): Juju zip slip vulnerability via authenticated endpoint (GO/github.com/juju/juju) | HIGH (CVSS: 8.8) | 2025-07-09 |
| GHSA | [GHSA-GHSA-557j-xg8c-q2mm](https://github.com/advisories/GHSA-557j-xg8c-q2mm): Helm vulnerable to Code Injection through malicious chart.yaml content (GO/helm.sh/helm/v3) | HIGH (CVSS: 8.5) | 2025-07-08 |
| GHSA | [GHSA-GHSA-x698-5hjm-w2m5](https://github.com/advisories/GHSA-x698-5hjm-w2m5): pyLoad is vulnerable to attacks that bypass localhost restrictions, enabling the creation of arbitrary packages (PIP/pyload-ng) | HIGH (CVSS: 7.5) | 2025-07-08 |
| GHSA | [GHSA-GHSA-2wcm-vx67-3x4q](https://github.com/advisories/GHSA-2wcm-vx67-3x4q): Duplicate Advisory: GHSA-x698-5hjm-w2m5 (PIP/pyload-ng) | HIGH (CVSS: 0.0) | 2025-07-08 |
| GHSA | [GHSA-GHSA-p22h-3m2v-cmgh](https://github.com/advisories/GHSA-p22h-3m2v-cmgh): Cosmos SDK's Integer Overflow vulnerability in its Validator Rewards pool can cause a chain halt (GO/github.com/cosmos/cosmos-sdk, GO/github.com/cosmos/cosmos-sdk) | HIGH (CVSS: 0.0) | 2025-07-08 |
| GHSA | [GHSA-GHSA-65gg-3w2w-hr4h](https://github.com/advisories/GHSA-65gg-3w2w-hr4h): Podman Improper Certificate Validation; machine missing TLS verification (GO/github.com/containers/podman/v4, GO/github.com/containers/podman/v5) | HIGH (CVSS: 8.4) | 2025-06-25 |
| GHSA | [GHSA-GHSA-rpfv-46xj-5984](https://github.com/advisories/GHSA-rpfv-46xj-5984): Upsonic has vulnerability in Pickle Handler component that can lead to deserialization (PIP/upsonic) | LOW (CVSS: 5.5) | 2025-06-19 |
| GHSA | [GHSA-GHSA-8jf4-fcjr-68c2](https://github.com/advisories/GHSA-8jf4-fcjr-68c2): Upsonic is vulnerable to Path Traversal attack through its os.path.join function (PIP/upsonic) | LOW (CVSS: 5.5) | 2025-06-19 |
| GHSA | [GHSA-GHSA-vv7r-c36w-3prj](https://github.com/advisories/GHSA-vv7r-c36w-3prj): Apache Commons FileUpload, Apache Commons FileUpload: FileUpload DoS via part headers (MAVEN/commons-fileupload:commons-fileupload, MAVEN/org.apache.commons:commons-fileupload2-core) | HIGH (CVSS: 0.0) | 2025-06-16 |
| GHSA | [GHSA-GHSA-mx2j-7cmv-353c](https://github.com/advisories/GHSA-mx2j-7cmv-353c): wasmvm: Malicious smart contract can slow down block production (GO/github.com/CosmWasm/wasmvm/v2, GO/github.com/CosmWasm/wasmvm, GO/github.com/CosmWasm/wasmvm/v2) | MODERATE (CVSS: 0.0) | 2025-02-04 |
| GHSA | [GHSA-GHSA-6cf5-w9h3-4rqv](https://github.com/advisories/GHSA-6cf5-w9h3-4rqv): Denied Host Validation Bypass in Zitadel Actions (GO/github.com/zitadel/zitadel, GO/github.com/zitadel/zitadel, GO/github.com/zitadel/zitadel) | MODERATE (CVSS: 5.9) | 2024-10-25 |
| GHSA | [GHSA-GHSA-hh8p-374f-qgr5](https://github.com/advisories/GHSA-hh8p-374f-qgr5): Grafana plugin data sources vulnerable to access control bypass (GO/github.com/grafana/grafana, GO/github.com/grafana/grafana, GO/github.com/grafana/grafana) | MODERATE (CVSS: 4.4) | 2024-08-20 |
| GHSA | [GHSA-GHSA-vg67-chm7-8m3j](https://github.com/advisories/GHSA-vg67-chm7-8m3j): Mattermost allows remote actor to create/update/delete posts in arbitrary channels (GO/github.com/mattermost/mattermost, GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost/server/v8) | HIGH (CVSS: 5.5) | 2024-08-01 |
| GHSA | [GHSA-GHSA-jr9x-3x7m-4j75](https://github.com/advisories/GHSA-jr9x-3x7m-4j75): Mattermost allows a remote actor to make an arbitrary local channel read-only (GO/github.com/mattermost/mattermost, GO/github.com/mattermost/mattermost/server/v8, GO/github.com/mattermost/mattermost/server/v8) | MODERATE (CVSS: 4.1) | 2024-08-01 |
| GHSA | [GHSA-GHSA-hfrg-4jwr-jfpj](https://github.com/advisories/GHSA-hfrg-4jwr-jfpj): Improper HTML sanitization in ZITADEL (GO/github.com/zitadel/zitadel, GO/github.com/zitadel/zitadel, GO/github.com/zitadel/zitadel) | HIGH (CVSS: 8.1) | 2024-03-18 |
| GHSA | [GHSA-GHSA-r6cc-7wj7-gfx2](https://github.com/advisories/GHSA-r6cc-7wj7-gfx2): Kubernetes csi-proxy vulnerable to privilege escalation due to improper input validation (GO/github.com/kubernetes-csi/csi-proxy, GO/github.com/kubernetes-csi/csi-proxy, GO/github.com/kubernetes-csi/csi-proxy) | HIGH (CVSS: 8.8) | 2023-11-03 |
| GHSA | [GHSA-GHSA-j7hp-h8jx-5ppr](https://github.com/advisories/GHSA-j7hp-h8jx-5ppr): libwebp: OOB write in BuildHuffmanTable (GO/github.com/chai2010/webp, GO/github.com/chai2010/webp, GO/github.com/chai2010/webp) | HIGH (CVSS: 8.8) | 2023-09-12 |
| GHSA | [GHSA-GHSA-3wq5-3f56-v5xc](https://github.com/advisories/GHSA-3wq5-3f56-v5xc): Mattermost vulnerable to information disclosure (GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost-server, GO/github.com/mattermost/mattermost-server) | MODERATE (CVSS: 5.3) | 2023-03-31 |
| GHSA | [GHSA-GHSA-xr7p-8q82-878q](https://github.com/advisories/GHSA-xr7p-8q82-878q): teler dashboard vulnerable to DOM-based cross-site scripting (XSS) (GO/teler.app, GO/teler.app, GO/teler.app) | LOW (CVSS: 3.1) | 2022-12-06 |
| GHSA | [GHSA-GHSA-4whx-7p29-mq22](https://github.com/advisories/GHSA-4whx-7p29-mq22): TiDB authentication bypass vulnerability (GO/github.com/pingcap/tidb, GO/github.com/pingcap/tidb, GO/github.com/pingcap/tidb) | HIGH (CVSS: 7.8) | 2022-06-06 |
| GHSA | [GHSA-GHSA-f2wr-c4c4-xjg7](https://github.com/advisories/GHSA-f2wr-c4c4-xjg7): Apache Traffic Control vulnerable to Slowloris-style Denial of Service attack (GO/github.com/apache/trafficcontrol, GO/github.com/apache/trafficcontrol, GO/github.com/apache/trafficcontrol) | HIGH (CVSS: 7.5) | 2022-05-13 |
| GHSA | [GHSA-GHSA-77rm-9x9h-xj3g](https://github.com/advisories/GHSA-77rm-9x9h-xj3g): NULL Pointer Dereference in Protocol Buffers (GO/github.com/protocolbuffers/protobuf, GO/github.com/protocolbuffers/protobuf, MAVEN/com.google.protobuf:protobuf-java) | HIGH (CVSS: 7.5) | 2022-01-27 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| chromium/chromium | [9aded5b](https://github.com/chromium/chromium/commit/9aded5b262a1d365a1ae660a4f7ca4a33ba71eda) | Reland "Create proactive password recovery suggestion" | 2025-07-09 |
| chromium/chromium | [c545ffc](https://github.com/chromium/chromium/commit/c545ffce17a6aba55825a9512db922b064b10dd6) | Adding to third_party update. | 2025-07-09 |
| chromium/chromium | [fb8fe36](https://github.com/chromium/chromium/commit/fb8fe36758c107d2638908e36a86625cada621d3) | RenderDocument: Fix touch-stale-node-crash.html test. | 2025-07-09 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| wazuh/wazuh | [#30804](https://github.com/wazuh/wazuh/pull/30804) | Fixed error in database feed manager when wazuh is shutting down | 2025-07-09 |

