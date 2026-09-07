---
doc_id: webex-sdk-component-adapter-ai-docs-patterns-rxjs-entity-observable-cache-md
source_url: https://github.com/webex/sdk-component-adapter/blob/master/ai-docs/patterns/rxjs-entity-observable-cache.md
repo: webex/sdk-component-adapter
ruta: ai-docs/patterns/rxjs-entity-observable-cache.md
licencia: MIT
retrieved_at: 2026-09-07T10:28:56.945179+00:00
---

# sdk-component-adapter — ai-docs/patterns/rxjs-entity-observable-cache.md

Repositorio: webex/sdk-component-adapter
Descripcion del repositorio: JS SDK Adapter implementation for Webex Components 🧩 (https://github.com/webex/components)

<!-- ───────────────────────────────
  Template:     Pattern
  Template-ID:  pattern-rxjs-entity-cache
  Description:  RxJS per-entity observable cache pattern used by domain adapters.
  Generates:    ai-docs/patterns/rxjs-entity-observable-cache.md
  Library ver:  0.2.2
  Last updated: 2026-08-05
─────────────────────────────── -->

# Pattern: RxJS entity observable cache

Observed in: `src/ActivitiesSDKAdapter.js`, `src/RoomsSDKAdapter.js`, `src/PeopleSDKAdapter.js`, `src/OrganizationsSDKAdapter.js`

## Intent

Reuse one hot observable per entity ID so multiple subscribers share SDK fetch + live updates.

## Correct

```javascript
// Create ReplaySubject(1) on first getActivity(ID) call; store in this.activityObservables[ID]
// Subsequent callers subscribe to the same subject
getActivity(ID) {
  if (!this.activityObservables[ID]) {
    this.activityObservables[ID] = new ReplaySubject(1);
    this.fetchActivity(ID).then(/* next */, /* error on subject */);
  }
  return this.activityObservables[ID].asObservable();
}
```

Evidence: `src/ActivitiesSDKAdapter.js`, `src/RoomsSDKAdapter.js`, `src/PeopleSDKAdapter.js`

## Incorrect

```javascript
// Anti-pattern: new Observable per call — duplicate SDK fetches and divergent state
getActivity(ID) {
  return new Observable((subscriber) => {
    this.fetchActivity(ID).then(subscriber.next);
  });
}
```

## Verification

- Unit tests assert single fetch for duplicate subscriptions (`ActivitiesSDKAdapter.test.js`).

---
> Fuente: https://github.com/webex/sdk-component-adapter/blob/master/ai-docs/patterns/rxjs-entity-observable-cache.md (licencia MIT)
