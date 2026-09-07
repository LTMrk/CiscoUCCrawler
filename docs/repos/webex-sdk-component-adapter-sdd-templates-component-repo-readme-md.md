---
doc_id: webex-sdk-component-adapter-sdd-templates-component-repo-readme-md
source_url: https://github.com/webex/sdk-component-adapter/blob/master/.sdd/templates/component-repo/README.md
repo: webex/sdk-component-adapter
ruta: .sdd/templates/component-repo/README.md
licencia: MIT
retrieved_at: 2026-09-07T10:28:46.630180+00:00
---

# sdk-component-adapter — .sdd/templates/component-repo/README.md

Repositorio: webex/sdk-component-adapter
Descripcion del repositorio: JS SDK Adapter implementation for Webex Components 🧩 (https://github.com/webex/components)

# Component Repository Templates

Standing documentation for one component repository. In a multi-repo product, these templates apply
inside each component repo; workspace-level documentation may link across repositories, but each
component repo still owns its local standing docs.

## Use This Folder

Use these templates when onboarding an existing repo or refreshing its standing SDD docs. The
generated docs help agents find the repo entry point, module specs, contracts, rules, and decisions
without scanning the whole codebase.

| Folder | Generates | Purpose |
|---|---|---|
| `standing-docs/` | Root `AGENTS.md` plus repo-level standing docs under `ai-docs/` by default | Navigation, architecture, contracts, security, service state, rules, and repo operation docs |
| `module-docs/` | Per-module specs | Canonical source-local module specs with responsibility, public surface, dependencies, requirements, data flow, sequence/class diagrams, use cases, failure paths, pitfalls, and module test strategy |
| `reference-docs/` | `ai-docs/patterns/`, `ai-docs/rules/`, `ai-docs/adr/` entries | Reference conventions, rules, and decisions |

---
> Fuente: https://github.com/webex/sdk-component-adapter/blob/master/.sdd/templates/component-repo/README.md (licencia MIT)
