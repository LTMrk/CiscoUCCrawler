---
doc_id: webex-contact-center-get-orgid-project-projectid-v2-flows-flowid-validate
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /{orgId}/project/{projectId}/v2/flows/{flowId}:validate
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.967540+00:00
---

# GET /{orgId}/project/{projectId}/v2/flows/{flowId}:validate

**API:** Webex Contact Center
**Área:** Flows
**operationId:** `validateExistingFlowV2`

## Resumen
Validate an Existing Flow Draft

## Descripción
Validate the current draft of an existing flow (read-only operation).

Scope: `cjp:config_read`

## Parámetros
- `orgId` [path] (string) **(requerido)**: Organization ID.
- `projectId` [path] (string) **(requerido)**: Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.
- `flowId` [path] (string) **(requerido)**: Flow ID.
- `versionId` [query] (string): Version to validate. Use 'draft' for the current draft, or a specific version ObjectId.
- `flowType` [query] (string): Either of 'FLOW' or 'SUBFLOW'.

## Respuestas
- **200**: Validation result.
  - `valid` (boolean): True if the draft passed validation.
  - `results` (array): Per-issue results.
    - `code` (string): Stable result code.
    - `docLink` (string): Link to documentation about this result. May be empty.
    - `hint` (string): Additional hint about the result, when available.
    - `message` (string): Human-readable explanation of the result.
    - `severity` (string): Severity of the result. Valores: ERROR, WARNING, RECOMMENDATION.
    - `activityLabel` (string): Label of the activity the result relates to. May be empty.
- **401**: Unauthorized.
- **403**: Forbidden.
- **404**: Not Found.
- **429**: Too Many Requests.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
