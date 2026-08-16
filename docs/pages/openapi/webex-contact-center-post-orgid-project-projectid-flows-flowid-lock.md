---
doc_id: webex-contact-center-post-orgid-project-projectid-flows-flowid-lock
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /{orgId}/project/{projectId}/flows/{flowId}:lock
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.966592+00:00
---

# POST /{orgId}/project/{projectId}/flows/{flowId}:lock

**API:** Webex Contact Center
**Área:** Flows
**operationId:** `lockFlowUsingPOST`

## Resumen
Lock a Flow or Subflow

## Descripción
Lock a flow to prevent concurrent edits by other users. Locks expire after 15 minutes of inactivity.

Scope: `cjp:config_write`. Roles: [`Organizational Full Admin`, `Contact Center Service Admin`]

## Parámetros
- `flowId` [path] (string) **(requerido)**: Flow ID.
- `orgId` [path] (string) **(requerido)**: Organization ID.
- `projectId` [path] (string) **(requerido)**: Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.
- `flowType` [query] (string): Either of 'FLOW' or 'SUBFLOW'.

## Respuestas
- **200**: Lock confirmation with expiry information.
- **401**: Unauthorized.
- **403**: Forbidden.
- **404**: Not Found.
- **409**: Conflict — the flow is already locked by another user.
- **429**: Too Many Requests.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
