---
doc_id: webex-contact-center-patch-orgid-project-projectid-v2-flows-flowid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PATCH
path: /{orgId}/project/{projectId}/v2/flows/{flowId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.967441+00:00
---

# PATCH /{orgId}/project/{projectId}/v2/flows/{flowId}

**API:** Webex Contact Center
**Área:** Flows
**operationId:** `patchFlowV2Draft`

## Resumen
Patch a Flow Draft

## Descripción
Apply partial updates to an existing flow draft without replacing the entire document. The patch body is a Patch Draft Contract — server-side merge, idempotent, and re-validated after the merge. The patch is rejected if the merged document fails validation, so the draft is never left in a broken state. The body may also include top-level overrides such as `name` and `description`.

Pass `expectedVersion` as a query parameter to enable optimistic locking; the request fails with `409 Conflict` if the server-side version does not match. Omit `expectedVersion` to skip the check.

Scope: `cjp:config_write`

## Parámetros
- `orgId` [path] (string) **(requerido)**: Organization ID.
- `projectId` [path] (string) **(requerido)**: Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.
- `flowId` [path] (string) **(requerido)**: Flow ID.
- `expectedVersion` [query] (integer): Expected current draft version for optimistic locking. The request fails with 409 Conflict if the server-side version does not match. Omit to skip the check.
- `flowType` [query] (string): Either of 'FLOW' or 'SUBFLOW'.

## Cuerpo de la petición (application/json)
- `upsert_nodes` (array): Nodes to insert or replace. Matched by `name`. If a node with the same name exists, it is fully replaced; otherwise a new node is created.
- `upsert_edges` (array): Edges to insert or replace, matched by `id`.
- `remove_node_names` (array): Names of nodes to remove. Edges referencing a removed node must also be removed in the same patch, or the merged document will fail validation.
- `remove_edge_keys` (array): Identifiers of edges to remove.

## Respuestas
- **200**: Updated flow metadata, including the new `version`.
  - `flow` (object): The persisted flow document, including the server-assigned `id`.
  - `preflightWarnings` (array): Non-blocking warnings raised while persisting the flow (for example, references that resolve but are flagged for review). Empty when there are none.
  - `preflightWarningsCount` (integer): Number of entries in `preflightWarnings`.
- **400**: Bad Request.
- **401**: Unauthorized.
- **403**: Forbidden.
- **404**: Not Found.
- **409**: Conflict — `expectedVersion` does not match the current draft version.
- **422**: Unprocessable Entity — merged flow document failed validation.
- **429**: Too Many Requests.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
