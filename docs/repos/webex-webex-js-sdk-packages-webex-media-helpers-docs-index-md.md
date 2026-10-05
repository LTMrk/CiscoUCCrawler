---
doc_id: webex-webex-js-sdk-packages-webex-media-helpers-docs-index-md
source_url: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/media-helpers/docs/index.md
repo: webex/webex-js-sdk
ruta: packages/@webex/media-helpers/docs/index.md
licencia: NOASSERTION
retrieved_at: 2026-10-05T11:22:42.470211+00:00
---

# webex-js-sdk — packages/@webex/media-helpers/docs/index.md

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
updated_at: 2026-09-30T05:28:59Z
validation_status: pass
-->

# @webex/media-helpers documentation

Doc map for developers and agents working on the `@webex/media-helpers` package.

## Start here

- [Getting started](getting-started.md)
- [Repository architecture](architecture.md)
- Service specification — not applicable; this package is a published library, not a deployable
  service
- API specification — not applicable; the published surface is an SDK package, so its
  ecosystem-native artifact is authoritative rather than an OpenAPI document

## Decisions

- [adr/](adr/) — architectural decision records

## Specifications and contracts

- [architecture.md](architecture.md) — canonical repository-wide architecture
- [specs/README.md](specs/README.md) — manifest-backed module and contract registry
- [README.md](README.md) — the owning specification for the `src/` module
- [adr/](adr/) — concrete architectural decisions; blank ADR templates remain under `.sdd/`

Use the manifest-linked native source for exact contract details: for this package that is
`package.json` for the published package surface and `src/index.ts` for the exact export list.
Register and link those sources from the architecture index and owning module spec instead of
copying them into Markdown.

## Related repository resources

- [../README.md](../README.md) — the published npm landing page, with install and effect usage
  examples. It remains owner-authored and is not generated.
- The monorepo root owns contribution instructions, the changelog, the license, and CI workflows for
  this package; see the repository root of `webex-js-sdk`.

---
> Fuente: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/media-helpers/docs/index.md (licencia NOASSERTION)
