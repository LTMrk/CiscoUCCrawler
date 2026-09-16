---
doc_id: webex-react-widgets-sdd-templates-component-repo-readme-md
source_url: https://github.com/webex/react-widgets/blob/master/.sdd/templates/component-repo/README.md
repo: webex/react-widgets
ruta: .sdd/templates/component-repo/README.md
licencia: MIT
retrieved_at: 2026-09-16T09:35:20.107984+00:00
---

# react-widgets — .sdd/templates/component-repo/README.md

Repositorio: webex/react-widgets
Descripcion del repositorio: React components and Redux modules for embedded Webex Teams

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
> Fuente: https://github.com/webex/react-widgets/blob/master/.sdd/templates/component-repo/README.md (licencia MIT)
