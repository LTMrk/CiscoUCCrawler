---
doc_id: webex-contact-center-post-publish-v1-api-event
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /publish/v1/api/event
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.970514+00:00
---

# POST /publish/v1/api/event

**API:** Webex Contact Center
**Área:** Journey - Data Ingestion API
**operationId:** `journeyEventPosting`

## Resumen
Journey Event Posting

## Descripción
Journey Event Posting API accepts events that describe what occurred, when, and by whom on every interaction across touch points and applications. Data Ingestion is based on Cloud Events specification for describing event data in a common way. API accepts data in the form of POST with support for Header based authorization. 

Role and Scope: Requires id full admin role with cjds:admin_org_write or any role with cjp:config_write scope.

## Parámetros
- `workspaceId` [query] (string) **(requerido)**: Workspace ID

## Cuerpo de la petición (application/json)
- `id` (string) **(requerido)**: Event ID
- `specversion` (string) **(requerido)**: Event Spec Version
- `type` (string) **(requerido)**: Event Type
- `source` (string) **(requerido)**: Event Source
- `time` (string): Event Time
- `identity` (string) **(requerido)**: Identity
- `identitytype` (string) **(requerido)**: Identity Type
- `previousidentity` (string): Previous Identity
- `datacontenttype` (string) **(requerido)**: Event Data Content Type
- `data` (object) **(requerido)**: Event Data
  - `agentId` (string): Agent Id
  - `destination` (string): destination
  - `profileType` (string): profileType
  - `currentState` (string): currentState
  - `idleCodeId` (string): idleCodeId
  - `createdTime` (string): createdTime

## Respuestas
- **200**: Ok
  - `meta` (object): Meta information of the response
    - `organizationId` (string): Organization ID
    - `workspaceId` (string): Workspace ID
  - `data` (object): Data part of the response
    - `message` (string): message
- **404**: Resource not found
- **409**: Resource already exists
- **429**: Too many requests
- **500**: Internal server error

**Autenticación:** bearerAuth

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
