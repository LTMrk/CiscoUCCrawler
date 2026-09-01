---
doc_id: webex-contact-center-get-v1-api-events-stream-workspace-id-workspaceid-identity-identity
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /v1/api/events/stream/workspace-id/{workspaceId}/identity/{identity}
operation_id: streamEventsByIdentity
tags: Journey - Profile Creation & Insights API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.769984+00:00
---

# GET /v1/api/events/stream/workspace-id/{workspaceId}/identity/{identity}

**API:** Webex Contact Center
**Área:** Journey - Profile Creation & Insights API
**operationId:** `streamEventsByIdentity`
**Autenticación:** bearerAuth

## Resumen
Stream Events By Identity

## Descripción
Real-time streaming enables API consumers to listen for events as it arrives as part of the Journey; these may be transformed, value-added/enriched, and ready to be consumed or forwarded to another destination. Optionally accepts filter and data parameters slice/dice further. 

Role and Scope: Requires id full admin role with cjds:admin_org_write or cjds:admin_org_read scope. Or requires any role with cjp:user, cjp:config_write or cjp:config_read scope.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Workspace ID
- `identity` [path] (string) (**requerido**): Person Identity.    In case the identity contains non-uri-encodable characters, eg: '+', '>' etc, you can URL-encode the same and then pass it as parameter.
- `filter` [query] (string): Optional filter which can be applied to the elements to be fetched.  This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see [this reference](https://developer.here.com/documentation/data-client-library/dev_guide/client/rsql.html). For a list of supported operators, see this  [syntax guide](https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference).
- `data` [query] (string): Optional filter on data filed which can be applied to the elements to be fetched.  This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see [this reference](https://developer.here.com/documentation/data-client-library/dev_guide/client/rsql.html). For a list of supported operators, see this [syntax guide](https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference).

## Ejemplo de invocación
```bash
curl -X GET '/v1/api/events/stream/workspace-id/<workspaceId>/identity/<identity>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Ok
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