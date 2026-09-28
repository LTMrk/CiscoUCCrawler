---
doc_id: webex-webex-js-sdk-packages-calling-ai-docs-patterns-readme-md
source_url: https://github.com/webex/webex-js-sdk/blob/next/packages/calling/ai-docs/patterns/README.md
repo: webex/webex-js-sdk
ruta: packages/calling/ai-docs/patterns/README.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:07:51.220295+00:00
---

# webex-js-sdk — packages/calling/ai-docs/patterns/README.md

Repositorio: webex/webex-js-sdk
Descripcion del repositorio: JavaScript SDK for Webex

# ai-docs/patterns/ — repo conventions (correct vs incorrect)

Conventions the linter doesn't catch (naming intent, error-enrichment style, event idioms), extracted
from **real source** (a convention seen in 3+ files) — never invented.

## Use Patterns For

Use patterns when a convention is visible in real code but not enforced by tooling. A pattern should
show correct and incorrect examples so future agents can follow the local style.

- **Fill-in shape:** `_pattern-example.md` (When to use · Correct · Incorrect · Where it appears · Edge cases).
- **Routing:** generic patterns live directly in `ai-docs/patterns/`; language-specific ones in
  `ai-docs/patterns/<language>/`.
- **Defer to the linter:** if a tool already enforces it, point to the tool instead of writing a pattern.

Each pattern file carries the standard metadata header, a navigation pointer, and Capture/Avoid/Example
guidance. See `../README.md` for this reference-docs area and `../../../README.md` for global
conventions.

---
> Fuente: https://github.com/webex/webex-js-sdk/blob/next/packages/calling/ai-docs/patterns/README.md (licencia NOASSERTION)
