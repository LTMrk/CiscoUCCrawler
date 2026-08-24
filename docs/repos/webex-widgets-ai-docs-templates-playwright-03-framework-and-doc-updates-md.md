---
doc_id: webex-widgets-ai-docs-templates-playwright-03-framework-and-doc-updates-md
source_url: https://github.com/webex/widgets/blob/next/ai-docs/templates/playwright/03-framework-and-doc-updates.md
repo: webex/widgets
ruta: ai-docs/templates/playwright/03-framework-and-doc-updates.md
licencia: sin declarar
retrieved_at: 2026-08-24T09:09:10.983926+00:00
---

# widgets — ai-docs/templates/playwright/03-framework-and-doc-updates.md

Repositorio: webex/widgets
Descripcion del repositorio: Embed the power of Webex in your web applications ✨

# Playwright Framework and Docs Updates

## Purpose

Apply shared framework updates and keep Playwright docs aligned in the same task.

---

## Framework Files

Update these as needed for reusable behavior changes:

- `playwright/Utils/*.ts`
- `playwright/test-manager.ts`
- `playwright/constants.ts`
- `playwright/global.setup.ts`
- `playwright.config.ts`

---

## Doc Files (Required Alignment)

- `playwright/ai-docs/AGENTS.md`
- `playwright/ai-docs/ARCHITECTURE.md`

`playwright/ai-docs/ARCHITECTURE.md` is the single source of truth for framework internals and scenario-level technical reference.

If a task adds/changes suites, tests, sets, setup flows, runtime flags, or stability constraints, doc updates are mandatory.

---

## Checklist

- [ ] Shared changes are reusable and not test-case specific
- [ ] Existing tests remain backward compatible or intentionally migrated
- [ ] AGENTS baseline reflects current suites/sets/workflow
- [ ] ARCHITECTURE topology/mapping/runtime sections match current code
- [ ] No references to non-existent files/suites/sets

---

_Last Updated: 2026-03-05_

---
> Fuente: https://github.com/webex/widgets/blob/next/ai-docs/templates/playwright/03-framework-and-doc-updates.md (licencia sin declarar)
