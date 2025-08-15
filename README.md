# Security Updates Monitor

*Last updated: 2025-08-15 08:20:13 UTC*

## Summary
| Type | Count |
|------|-------|
| ADVISORY | 16 |
| COMMIT | 4 |
| PR | 2 |

---

## Security Advisories

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| GHSA | [GHSA-GHSA-r4mg-4433-c7g3](https://github.com/advisories/GHSA-r4mg-4433-c7g3): Active Storage allowed transformation methods that were potentially unsafe (RUBYGEMS/activestorage, RUBYGEMS/activestorage, RUBYGEMS/activestorage) | HIGH (CVSS: 0.0) | 2025-08-14 |
| GHSA | [GHSA-GHSA-mhpq-m962-mg92](https://github.com/advisories/GHSA-mhpq-m962-mg92): Apache Superset allows authenticated users to discover metadata about datasources they don't have permission to access (PIP/apache-superset) | MODERATE (CVSS: 0.0) | 2025-08-14 |
| GHSA | [GHSA-GHSA-9g5x-mm39-wg9r](https://github.com/advisories/GHSA-9g5x-mm39-wg9r): Apache Superset data query improperly discloses database schema information to low-privileged guest user (PIP/apache-superset) | MODERATE (CVSS: 0.0) | 2025-08-14 |
| GHSA | [GHSA-GHSA-fxgf-3xh6-m2pp](https://github.com/advisories/GHSA-fxgf-3xh6-m2pp): Apache Superset has bypass of `DISALLOWED_SQL_FUNCTIONS` that allows execution of blocked SQL functions (PIP/apache-superset) | MODERATE (CVSS: 0.0) | 2025-08-14 |
| GHSA | [GHSA-GHSA-fj97-2v9x-w5m4](https://github.com/advisories/GHSA-fj97-2v9x-w5m4): Apache Superset's chart visualization has a stored Cross-Site Scripting (XSS) vulnerability (PIP/apache-superset) | MODERATE (CVSS: 0.0) | 2025-08-14 |
| GHSA | [GHSA-GHSA-2vv2-3x8x-4gv7](https://github.com/advisories/GHSA-2vv2-3x8x-4gv7): Flowise OS command remote code execution (NPM/flowise) | CRITICAL (CVSS: 9.8) | 2025-08-14 |
| GHSA | [GHSA-GHSA-f9f8-9pmf-xv68](https://github.com/advisories/GHSA-f9f8-9pmf-xv68): Helm May Panic Due To Incorrect YAML Content (GO/helm.sh/helm/v3) | MODERATE (CVSS: 6.5) | 2025-08-14 |
| GHSA | [GHSA-GHSA-9h84-qmv7-982p](https://github.com/advisories/GHSA-9h84-qmv7-982p): Helm Charts with Specific JSON Schema Values Can Cause Memory Exhaustion (GO/helm.sh/helm/v3) | MODERATE (CVSS: 6.5) | 2025-08-14 |
| GHSA | [GHSA-GHSA-7hfw-26vp-jp8m](https://github.com/advisories/GHSA-7hfw-26vp-jp8m): PyPDF's Manipulated FlateDecode streams can exhaust RAM (PIP/pypdf) | MODERATE (CVSS: 0.0) | 2025-08-13 |
| GHSA | [GHSA-GHSA-fcxq-v2r3-cc8h](https://github.com/advisories/GHSA-fcxq-v2r3-cc8h): External Secrets Operator's Missing Namespace Restriction Allows Unauthorized Secret Access (GO/github.com/external-secrets/external-secrets) | HIGH (CVSS: 0.0) | 2025-08-13 |
| GHSA | [GHSA-GHSA-m5c7-5gv3-hcpf](https://github.com/advisories/GHSA-m5c7-5gv3-hcpf): Liferay Portal 7.4.0 and Liferay DXP have a reflected cross-site scripting (XSS) vulnerability (MAVEN/com.liferay:com.liferay.frontend.taglib.clay, MAVEN/com.liferay.portal:release.dxp.bom, MAVEN/com.liferay.portal:release.dxp.bom) | MODERATE (CVSS: 0.0) | 2025-08-12 |
| GHSA | [GHSA-GHSA-6xp3-p59p-q4fj](https://github.com/advisories/GHSA-6xp3-p59p-q4fj): go-pg SQL injection vulnerability via the component /types/append_value.go (GO/github.com/go-pg/pg/v10, GO/github.com/go-pg/pg, GO/github.com/go-pg/pg/v9) | MODERATE (CVSS: 6.5) | 2025-06-12 |
| GHSA | [GHSA-GHSA-8cj5-5rvv-wf4v](https://github.com/advisories/GHSA-8cj5-5rvv-wf4v): tar-fs can extract outside the specified dir with a specific tarball (NPM/tar-fs, NPM/tar-fs, NPM/tar-fs) | HIGH (CVSS: 0.0) | 2025-06-03 |
| GHSA | [GHSA-GHSA-ww33-jppq-qfrp](https://github.com/advisories/GHSA-ww33-jppq-qfrp): phpMyFAQ Vulnerable to Stored HTML Injection at FAQ (COMPOSER/thorsten/phpmyfaq, COMPOSER/phpmyfaq/phpmyfaq) | MODERATE (CVSS: 5.2) | 2025-01-02 |
| GHSA | [GHSA-GHSA-mq69-4j5w-3qwp](https://github.com/advisories/GHSA-mq69-4j5w-3qwp): Capsule tenant owner with "patch namespace" permission can hijack system namespaces (GO/github.com/projectcapsule/capsule) | HIGH (CVSS: 8.5) | 2024-08-20 |
| GHSA | [GHSA-GHSA-j2h2-cvwh-cr64](https://github.com/advisories/GHSA-j2h2-cvwh-cr64): Mattermost Server Sensitive Data Exposure (GO/github.com/mattermost/mattermost-server/v5) | MODERATE (CVSS: 5.3) | 2022-05-24 |

## Code Commits

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| torvalds/linux | [c28d28a](https://github.com/torvalds/linux/commit/c28d28a7b005dd6459a6059dc7eff684bf0b7464) | Merge tag 'pm-6.17-rc2' of git://git.kernel.org/pub/scm/linux/kernel/git/rafael/linux-pm | 2025-08-14 |
| torvalds/linux | [5302e2a](https://github.com/torvalds/linux/commit/5302e2a3886c830b803ae3390b9d41d35832f315) | Merge branches 'pm-cpuidle' and 'pm-cpufreq' | 2025-08-14 |
| chromium/chromium | [928ff08](https://github.com/chromium/chromium/commit/928ff086a481355b352e2a029984d9a6447170d2) | Refactor HTMLDetailsElement::MainSummary to return a reference | 2025-08-14 |
| chromium/chromium | [0721e8a](https://github.com/chromium/chromium/commit/0721e8a75ddb72282881ba2953c9d783f2c796fe) | Import wpt@16d773f3a2e63d0e72d6db01553db82efe2d49b4 | 2025-08-14 |

## Pull Requests

| Source | Title | Severity | Date |
|--------|-------|----------|------|
| openssl/openssl | [#28184](https://github.com/openssl/openssl/pull/28184) | Fix integer overflow in date_to_julian() call | 2025-08-15 |
| openssl/openssl | [#28259](https://github.com/openssl/openssl/pull/28259) | Fix potential null pointer dereference in pkey_dh_derive | 2025-08-14 |

