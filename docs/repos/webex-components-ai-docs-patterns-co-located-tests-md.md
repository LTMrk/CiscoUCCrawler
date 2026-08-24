---
doc_id: webex-components-ai-docs-patterns-co-located-tests-md
source_url: https://github.com/webex/components/blob/master/ai-docs/patterns/co-located-tests.md
repo: webex/components
ruta: ai-docs/patterns/co-located-tests.md
licencia: MIT
retrieved_at: 2026-08-24T09:09:29.050667+00:00
---

# components — ai-docs/patterns/co-located-tests.md

Repositorio: webex/components
Descripcion del repositorio: Embed the power of Webex in your web applications, on your own terms 💪🏼

<!-- ───────────────────────────────
  Template:     Pattern (example)
  Template-ID:  pattern
  Generates:    ai-docs/patterns/co-located-tests.md
  Description:  A repo convention from real code — correct vs incorrect form, with where it appears.
  Library ver:  0.2.1
  Last updated: 2026-07-27
─────────────────────────────── -->

# Pattern: co-located component tests

> Router [`SPEC_INDEX.md`](../SPEC_INDEX.md) · [`RULES.md`](../RULES.md)

## When to use

When adding or modifying a React component under `src/components/`.

## Correct

```javascript
// from src/components/WebexMeeting/WebexMeeting.test.js
// Test file beside component; mock adapter context; snapshot or behavior assertions
```

Place `ComponentName.test.js` or `ComponentName.test.jsx` in the same folder as `ComponentName.jsx`.

## Incorrect

```javascript
// Centralized tests/ folder only, disconnected from component folder
```

**Why wrong:** This repo convention co-locates tests with source for discoverability and CONTRIBUTING compliance.

## Where it appears

- `src/components/WebexMeeting/WebexMeeting.test.js`
- `src/components/WebexDataProvider/WebexDataProvider.test.js`
- `src/components/hoc/withAdapter.test.jsx`
- `src/adapters/MeetingsJSONAdapter.test.js`

## Edge cases / exceptions

Storybook stories (`.stories.js`) supplement but do not replace unit tests per `CONTRIBUTING.md`.

---
> Fuente: https://github.com/webex/components/blob/master/ai-docs/patterns/co-located-tests.md (licencia MIT)
