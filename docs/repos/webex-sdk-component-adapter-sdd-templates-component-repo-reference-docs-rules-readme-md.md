---
doc_id: webex-sdk-component-adapter-sdd-templates-component-repo-reference-docs-rules-readme-md
source_url: https://github.com/webex/sdk-component-adapter/blob/master/.sdd/templates/component-repo/reference-docs/rules/README.md
repo: webex/sdk-component-adapter
ruta: .sdd/templates/component-repo/reference-docs/rules/README.md
licencia: MIT
retrieved_at: 2026-09-07T10:28:48.861179+00:00
---

# sdk-component-adapter — .sdd/templates/component-repo/reference-docs/rules/README.md

Repositorio: webex/sdk-component-adapter
Descripcion del repositorio: JS SDK Adapter implementation for Webex Components 🧩 (https://github.com/webex/components)

# ai-docs/rules/ — deeper repo rules

`AGENTS.md` carries the 5–10 **critical** rules; the repo-wide `RULES.md` is the digest; this folder
holds the **fuller, per-rule detail** an agent loads on demand.

## Use Rules For

Use rule files when a future change must consistently follow a repo-specific constraint. Keep the
short rule in `AGENTS.md` or `RULES.md`; put examples, rationale, and enforcement details here.

- **Fill-in shape:** `_rule-example.md` (Rule · Why · How to follow · Enforced by).
- **Routing:** generic rules live directly in `ai-docs/rules/`; language-specific ones in
  `ai-docs/rules/<language>/`.
- **Defer to tooling:** if a linter/CI already enforces a rule, the rule file points to that rather than
  restating it.

Each rule file carries the standard metadata header, a navigation pointer, and Capture/Avoid/Example
guidance. See `../README.md` for this reference-docs area and `../../../README.md` for global
conventions.

---
> Fuente: https://github.com/webex/sdk-component-adapter/blob/master/.sdd/templates/component-repo/reference-docs/rules/README.md (licencia MIT)
