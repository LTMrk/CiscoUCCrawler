---
doc_id: webex-contact-center-get-v1-api-events-workspace-id-workspaceid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /v1/api/events/workspace-id/{workspaceId}
operation_id: historicEvents
tags: Journey - Profile Creation & Insights API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.817081+00:00
---

# GET /v1/api/events/workspace-id/{workspaceId}

**API:** Webex Contact Center
**Área:** Journey - Profile Creation & Insights API
**operationId:** `historicEvents`
**Autenticación:** bearerAuth

## Resumen
Historic Journey Events

## Descripción
Getting Historic Customer Journey Events from Pinot. These events are append-only, immutable data ledger that can be queried to retrieve snapshot of latest events that moment in time or historically to play-back events as they occurred to understand or analyze Journeys using ML/AI models. 

Role and Scope: Requires id full admin role with cjds:admin_org_write or cjds:admin_org_read scope. Or requires any role with cjp:user, cjp:config_write or cjp:config_read scope.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Workspace ID
- `identity` [query] (string): Identity to search events for.    In case the identity contains non-uri-encodable characters, eg: '+', '>' etc, you can URL-encode the same and then pass it as parameter.
- `sortBy` [query] (string): sort By Field
- `sort` [query] (string): sort direction
- `filter` [query] (string): Optional filter which can be applied to the elements to be fetched.  This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see [this reference](https://developer.here.com/documentation/data-client-library/dev_guide/client/rsql.html). For a list of supported operators, see this  [syntax guide](https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference).
- `data` [query] (string): Optional filter on data filed which can be applied to the elements to be fetched.  This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see [this reference](https://developer.here.com/documentation/data-client-library/dev_guide/client/rsql.html). For a list of supported operators, see this  [syntax guide](https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference).
- `page` [query] (integer): Index of the page of results to be fetched.  Results are returned in blocks of pageSize elements. This parameter specifies which page number to retrieve.The page numbering starts with 0.
- `pageSize` [query] (integer): Number of items to be displayed on a page.

## Ejemplo de invocación
```bash
curl -X GET '/v1/api/events/workspace-id/<workspaceId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Ok
- `meta` (object):
  - `organizationId` (string): Organization ID
  - `workspaceId` (string): Workspace ID
  - `resultCount` (integer/int32): Result Count
  - `identity` (string): identity
- `data` (array):
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