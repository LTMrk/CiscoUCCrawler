---
doc_id: webex-react-widgets-sdd-templates-component-repo-module-docs-readme-md
source_url: https://github.com/webex/react-widgets/blob/master/.sdd/templates/component-repo/module-docs/README.md
repo: webex/react-widgets
ruta: .sdd/templates/component-repo/module-docs/README.md
licencia: MIT
retrieved_at: 2026-09-16T09:35:20.304936+00:00
---

# react-widgets — .sdd/templates/component-repo/module-docs/README.md

Repositorio: webex/react-widgets
Descripcion del repositorio: React components and Redux modules for embedded Webex Teams

# Per-module docs

Per-module docs for modules, packages, services, or components inside one repository. Each module that
warrants documentation gets one canonical spec:

## Use This Template

Use `module-spec.template.md` when a module needs an authoritative spec or a better Partial spec.
The generated file is what future engineering work reads before changing that module.

| Template | Generates | Purpose · when to use |
|---|---|---|
| `module-spec.template.md` | `<module-path>/ai-docs/<module-name>-spec.md` by default | Canonical module spec — orientation, requirements, data flow, sequence/class diagrams, use cases, business rules & invariants, concurrency, state machine, protocol/wire format, UI flow, data model, pitfalls, test approach, and coverage score metadata. Created per module during onboarding/backfill and read before modifying the module. |

- `<module-path>/ai-docs/<module-name>-spec.md` is the module documentation surface. State machine, protocol/wire format, UI
  flow, and data model details live as sections in that spec when they apply.
- `module-spec-quality.md` defines the completion check for generated module specs. It covers the
  universal sections, detailed design, data flow, sequence diagram(s), class/component relationships,
  use cases, pitfalls, error/failure paths, and module test strategy.
- Public-surface sections stay compact: summarize the endpoint/export/event, compatibility, and
  migration expectations, then link to the root `CONTRACTS.md` index row and the canonical schema or
  API detail source.
- Prefer `.yaml` for OpenAPI/AsyncAPI schemas unless the target repo already uses `.yml`; use `.proto`,
  `.graphql`, JSON Schema, or language-native SDK API outputs when those are the natural contract
  source.
- Module specs are **not** agent-entry files — the repository-level agent contract is `AGENTS.md`.

Conventions are described in `../../README.md`.

---
> Fuente: https://github.com/webex/react-widgets/blob/master/.sdd/templates/component-repo/module-docs/README.md (licencia MIT)
