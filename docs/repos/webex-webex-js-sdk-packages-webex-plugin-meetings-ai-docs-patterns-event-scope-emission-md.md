---
doc_id: webex-webex-js-sdk-packages-webex-plugin-meetings-ai-docs-patterns-event-scope-emission-md
source_url: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/plugin-meetings/ai-docs/patterns/event-scope-emission.md
repo: webex/webex-js-sdk
ruta: packages/@webex/plugin-meetings/ai-docs/patterns/event-scope-emission.md
licencia: NOASSERTION
retrieved_at: 2026-09-27T10:51:25.675500+00:00
---

# webex-js-sdk — packages/@webex/plugin-meetings/ai-docs/patterns/event-scope-emission.md

Repositorio: webex/webex-js-sdk
Descripcion del repositorio: JavaScript SDK for Webex

<!-- sdd-generated-metadata
doc_kind: reference-doc
generated_from: pattern@0.2.2
generator_plugin: repo-annotation@1.0.5+codex.20260818094939
generated_by: codex
approved_by: repository user
updated_at: 2026-08-18T15:33:39Z
validation_status: not-run
-->
# Pattern: Event-scope emission

> Root [`AGENTS.md`](../../AGENTS.md) · router [`SPEC_INDEX.md`](../SPEC_INDEX.md).

## When to use

**When to use:** When a module exposes a meeting/media/realtime state change to parent modules or consumers.

## Correct

```ts
// from src/meeting/connectionStateHandler.ts
this.emit(
  {file: 'connectionStateHandler', function: 'handleConnectionStateChange'},
  ConnectionStateEvent.stateChanged,
  {state: this.mediaConnectionState}
);
```

Extend/use `EventsScope`, emit the declared event constant only after the normalized state changes, and supply the expected payload.

## Incorrect

```ts
consumer.emit('connection-changed', rawPeerConnection);
```

**Why wrong:** It invents an event name, bypasses scoped logging, exposes an internal object, and can emit without a real state transition.

## Where it appears

- `src/locus-info/index.ts`, `src/meeting/connectionStateHandler.ts`, `src/multistream/receiveSlot.ts`, `src/multistream/remoteMedia.ts`, `src/reachability/index.ts`

## Edge cases / exceptions

- Behavioral telemetry uses metrics helpers rather than `EventsScope`.
- Remote Mercury/data-channel events must be parsed and mapped before consumer emission; do not relay arbitrary service payloads.

---
> Fuente: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/plugin-meetings/ai-docs/patterns/event-scope-emission.md (licencia NOASSERTION)
