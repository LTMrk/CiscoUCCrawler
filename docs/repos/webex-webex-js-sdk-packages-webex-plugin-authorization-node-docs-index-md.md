---
doc_id: webex-webex-js-sdk-packages-webex-plugin-authorization-node-docs-index-md
source_url: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/plugin-authorization-node/docs/index.md
repo: webex/webex-js-sdk
ruta: packages/@webex/plugin-authorization-node/docs/index.md
licencia: NOASSERTION
retrieved_at: 2026-11-16T12:37:10.144479+00:00
---

# webex-js-sdk — packages/@webex/plugin-authorization-node/docs/index.md

Repositorio: webex/webex-js-sdk
Descripcion del repositorio: JavaScript SDK for Webex

---
okf_version: '0.1'
---
<!-- sdd-generated-metadata
doc_kind: standing-doc
generated_from: docs-index@0.3.0
generated_by: claude-code
approved_by: rarajes2@cisco.com
updated_at: 2026-11-11T09:32:15Z
validation_status: pass-with-warnings
-->

# @webex/plugin-authorization-node documentation

Doc map for developers and agents working on the Node authorization plugin.

## Start here

- [Getting started](getting-started.md)
- [Package architecture](architecture.md)

## Decisions

- [adr/](adr/index.md) — architectural decision records

## Specifications and contracts

- [architecture.md](architecture.md) — canonical package architecture and contract index
- [specs/README.md](specs/README.md) — manifest-backed module and contract registry
- [`src/docs/README.md`](../src/docs/README.md) — the Node authorization plugin specification beside
  its code
- [adr/](adr/index.md) — concrete architectural decisions; blank ADR templates remain under the
  monorepo root `.sdd/`

This package is a library, so there is no service specification and no OpenAPI document. Exact
contract details live in the native sources linked from the architecture index: `package.json` and
`src/index.js` for the package, and `src/authorization.js` for the plugin API.

## Related repository resources

- [`README.md`](../README.md) — retained npm usage page; context only, see
  [ADR-0001](adr/0001-keep-existing-docs-separate.md)
- [`NODE-OAUTH-FLOW-GUIDE.md`](../NODE-OAUTH-FLOW-GUIDE.md) — retained technical guide; context
  only, see [ADR-0001](adr/0001-keep-existing-docs-separate.md)
- [`AGENTS.md`](../AGENTS.md) — agent instructions for this package

---
> Fuente: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/plugin-authorization-node/docs/index.md (licencia NOASSERTION)
