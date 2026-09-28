---
doc_id: webex-webexplaybooks-playbooks-docusign-finesse-int-docs-upstream-overview-md
source_url: https://github.com/webex/WebexPlaybooks/blob/main/playbooks/docusign-finesse-int/docs/upstream-overview.md
repo: webex/WebexPlaybooks
ruta: playbooks/docusign-finesse-int/docs/upstream-overview.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:10:06.621511+00:00
---

# WebexPlaybooks — playbooks/docusign-finesse-int/docs/upstream-overview.md

Repositorio: webex/WebexPlaybooks

# Upstream sample notes

This playbook’s code is adapted from
[wxsd-sales/docusign-finesse-int](https://github.com/wxsd-sales/docusign-finesse-int)
(MIT).

- **Demo:** [Vidcast recording](https://app.vidcast.io/share/87b7eb3d-c806-4d31-91f1-c6798f4c6453).
- **Contact:** WXSD team at [wxsd@external.cisco.com](mailto:wxsd@external.cisco.com).

## Playbook-specific changes

- Application root for Node and webpack is `src/` under this playbook (paths and
  `env.template` updated accordingly).
- **xml2js** was added as an explicit dependency (used by the DocuSign webhook
  handler; it was missing from the upstream `package.json`).
- Hardcoded Finesse `JSESSIONID` was replaced with optional `FINESSE_SESSION_COOKIE`.
- TLS verification is no longer disabled by default; set
  `FINESSE_ALLOW_INSECURE_TLS=true` only for lab Finesse with self-signed certs.

Pin the upstream commit when comparing behavior: clone the repo and run
`git rev-parse HEAD` on the revision you used.

---
> Fuente: https://github.com/webex/WebexPlaybooks/blob/main/playbooks/docusign-finesse-int/docs/upstream-overview.md (licencia NOASSERTION)
