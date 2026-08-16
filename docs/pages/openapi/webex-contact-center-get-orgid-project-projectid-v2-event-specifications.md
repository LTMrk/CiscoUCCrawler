---
doc_id: webex-contact-center-get-orgid-project-projectid-v2-event-specifications
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /{orgId}/project/{projectId}/v2/event-specifications
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.965914+00:00
---

# GET /{orgId}/project/{projectId}/v2/event-specifications

**API:** Webex Contact Center
**Área:** Events
**operationId:** `listEventSpecifications`

## Resumen
List Event Specifications

## Descripción
List the event types available for use in `event_flows[]`. Each entry describes the event name, payload schema, and any contextual metadata bound when the event fires.

Scope: `cjp:config_read`

## Parámetros
- `orgId` [path] (string) **(requerido)**: Organization ID.
- `projectId` [path] (string) **(requerido)**: Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.

## Respuestas
- **200**: Available event specifications, plus ready-to-paste quick-start snippets.
  - `specifications` (array): The available event specifications.
    - `eventSpecificationName` (string): Event specification name. Must be used verbatim as `FlowV2EventFlow.event`.
    - `eventSourceName` (string): Name of the event source the specification belongs to.
    - `eventClassificationName` (string): Name of the event classification the specification belongs to.
  - `quick_start` (object): Ready-to-paste start-node and global-error snippets. The backend resolves IDs from the supplied names.
- **401**: Unauthorized.
- **403**: Forbidden.
- **404**: Not Found.
- **429**: Too Many Requests.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
