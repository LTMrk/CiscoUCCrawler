---
doc_id: webex-sdk-component-adapter-ai-docs-patterns-structured-adapter-logging-md
source_url: https://github.com/webex/sdk-component-adapter/blob/master/ai-docs/patterns/structured-adapter-logging.md
repo: webex/sdk-component-adapter
ruta: ai-docs/patterns/structured-adapter-logging.md
licencia: MIT
retrieved_at: 2026-09-07T10:28:57.214585+00:00
---

# sdk-component-adapter — ai-docs/patterns/structured-adapter-logging.md

Repositorio: webex/sdk-component-adapter
Descripcion del repositorio: JS SDK Adapter implementation for Webex Components 🧩 (https://github.com/webex/components)

<!-- ───────────────────────────────
  Template:     Pattern
  Template-ID:  pattern-structured-logger
  Description:  Structured logger usage with domain tags and entity IDs.
  Generates:    ai-docs/patterns/structured-adapter-logging.md
  Library ver:  0.2.2
  Last updated: 2026-08-05
─────────────────────────────── -->

# Pattern: Structured adapter logging

Observed in: `src/WebexSDKAdapter.js`, `src/MeetingsSDKAdapter.js`, `src/RoomsSDKAdapter.js`, `src/ActivitiesSDKAdapter.js`

## Intent

Consistent debug/error logs with domain tag and entity ID. **Target:** avoid secrets and minimize PII in logs. **Current code:** some adapters still pass full `{activity}` / `{person}` objects at debug/error — documented as accepted brownfield gap in [`RULES.md`](../RULES.md).

## Correct

```javascript
import logger from './logger';

const LOG_ARGS = ['SDK', `${name}-${version}`];
logger.debug(...LOG_ARGS, 'connect()', 'calling sdk.internal.mercury.connect()');
logger.error('ROOM', ID, 'createRoom()', ['Unable to create room', {room}], err);
```

Evidence: `src/WebexSDKAdapter.js`, `src/logger.js`, `src/RoomsSDKAdapter.js`

## Incorrect

```javascript
console.log('connecting', sdk.credentials); // Leaks secrets, no level control
console.error(err); // No domain context
```

## Verification

- Logger level configurable via `window.webexSDKAdapterSetLogLevel` in browser builds.

---
> Fuente: https://github.com/webex/sdk-component-adapter/blob/master/ai-docs/patterns/structured-adapter-logging.md (licencia MIT)
