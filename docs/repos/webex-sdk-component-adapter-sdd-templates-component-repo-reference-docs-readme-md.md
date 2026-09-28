---
doc_id: webex-sdk-component-adapter-sdd-templates-component-repo-reference-docs-readme-md
source_url: https://github.com/webex/sdk-component-adapter/blob/master/.sdd/templates/component-repo/reference-docs/README.md
repo: webex/sdk-component-adapter
ruta: .sdd/templates/component-repo/reference-docs/README.md
licencia: MIT
retrieved_at: 2026-09-07T10:28:47.600462+00:00
---

# sdk-component-adapter — .sdd/templates/component-repo/reference-docs/README.md

Repositorio: webex/sdk-component-adapter
Descripcion del repositorio: JS SDK Adapter implementation for Webex Components 🧩 (https://github.com/webex/components)

# Reference Documentation Templates

Repeatable reference docs for a component repository. These are copied or instantiated under
`ai-docs/` when a repo needs durable conventions, enforceable rules, or architecture decisions that
future agents should load on demand.

## Use This Folder

Use these templates after the standing docs and module specs identify repeatable knowledge worth
promoting out of a one-off change or run record.

| Folder | Generates | Purpose |
|---|---|---|
| `patterns/` | `ai-docs/patterns/<name>.md` | Code-grounded conventions that are visible in real source but not fully enforced by tooling. |
| `rules/` | `ai-docs/rules/<name>.md` | Deeper rule pages for repo-specific constraints that need rationale, examples, and enforcement detail. |
| `adr/` | `ai-docs/adr/NNNN-<title>.md` | Append-only architecture decisions with context, rejected alternatives, consequences, and supersession. |

Promote only durable knowledge here. Temporary notes, questionnaire output, validation reports, and
investigation transcripts stay under `.generated/`.

Conventions (metadata header, navigation pointer, context-efficiency, `Include if:` handling, and
Capture/Avoid/Example guidance) are described in `../../README.md`.

---
> Fuente: https://github.com/webex/sdk-component-adapter/blob/master/.sdd/templates/component-repo/reference-docs/README.md (licencia MIT)
