---
doc_id: webex-contact-center-post-publish-v1-api-event
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /publish/v1/api/event
operation_id: journeyEventPosting
tags: Journey - Data Ingestion API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.864334+00:00
---

# POST /publish/v1/api/event

**API:** Webex Contact Center
**Área:** Journey - Data Ingestion API
**operationId:** `journeyEventPosting`
**Autenticación:** bearerAuth

## Resumen
Journey Event Posting

## Descripción
Journey Event Posting API accepts events that describe what occurred, when, and by whom on every interaction across touch points and applications. Data Ingestion is based on Cloud Events specification for describing event data in a common way. API accepts data in the form of POST with support for Header based authorization. 

Role and Scope: Requires id full admin role with cjds:admin_org_write or any role with cjp:config_write scope.

## Parámetros
- `workspaceId` [query] (string) (**requerido**): Workspace ID

## Cuerpo de la petición (application/json)
- `id` (string) (**requerido**): Event ID
- `specversion` (string) (**requerido**): Event Spec Version
- `type` (string) (**requerido**): Event Type
- `source` (string) (**requerido**): Event Source
- `time` (string): Event Time
- `identity` (string) (**requerido**): Identity
- `identitytype` (string) (**requerido**): Identity Type
- `previousidentity` (string): Previous Identity
- `datacontenttype` (string) (**requerido**): Event Data Content Type
- `data` (object) (**requerido**): Event Data
  - `agentId` (string): Agent Id
  - `destination` (string): destination
  - `profileType` (string): profileType
  - `currentState` (string): currentState
  - `idleCodeId` (string): idleCodeId
  - `createdTime` (string): createdTime

## Ejemplo de invocación
```bash
curl -X POST '/publish/v1/api/event?workspaceId=<workspaceId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"data": {}, "datacontenttype": "<datacontenttype>", "id": "<id>", "identity": "<identity>", "identitytype": "<identitytype>", "source": "<source>"}'
```

## Respuestas correctas
**200**: Ok
- `meta` (object): Meta information of the response
  - `organizationId` (string): Organization ID
  - `workspaceId` (string): Workspace ID
- `data` (object): Data part of the response
  - `message` (string): message

## Respuestas de error
- **404**: Resource not found
- **409**: Resource already exists
- **429**: Too many requests
- **500**: Internal server error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs