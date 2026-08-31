---
doc_id: webex-contact-center-get-admin-v1-api-person-workspace-id-workspaceid-aliases-aliases
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /admin/v1/api/person/workspace-id/{workspaceId}/aliases/{aliases}
operation_id: getPersonbyAliases
tags: Journey - Customer Identification API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.210132+00:00
---

# GET /admin/v1/api/person/workspace-id/{workspaceId}/aliases/{aliases}

**API:** Webex Contact Center
**Área:** Journey - Customer Identification API
**operationId:** `getPersonbyAliases`
**Autenticación:** bearerAuth

## Resumen
Search for an Identity via aliases

## Descripción
Get one or more Person Details searched by aliases in JDS. Multiple aliases should be separated by a comma.

Role and Scope: Requires id full admin role with cjp:config_write or cjp:config_read scope. Or it requires any role with cjp:user, cjp:config_write  or cjp:config_read scope.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Workspace ID
- `aliases` [path] (string) (**requerido**): Aliases to search for. Multiple aliases should be separated by a comma.    In case the alias(es) contain(s) non-uri-encodable characters, eg: '+', '>' etc, you can URL-encode the same and then pass it as parameter.
- `sortBy` [query] (string): Sort By Field
- `sort` [query] (string): Sort direction
- `page` [query] (integer): Index of the page of results to be fetched.  Results are returned in blocks of pageSize elements. This parameter specifies which page number to retrieve.The page numbering starts with 0.
- `pageSize` [query] (integer): Number of items to be displayed on a page.

## Ejemplo de invocación
```bash
curl -X GET '/admin/v1/api/person/workspace-id/<workspaceId>/aliases/<aliases>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Success
- `meta` (object): Meta information of the response
  - `organizationId` (string): Organization ID
- `data` (array): Data part of the response
  - `id` (string): Profile View Template Id
  - `firstName` (string): firstName
  - `lastName` (string): lastName
  - `phone` (array): Phone Number
  - `email` (array): Email
  - `temporaryId` (array): Temporary Id
  - `customerId` (array): Customer Id
  - `aliases` (array): Aliases

## Respuestas de error
- **404**: Not found
- **500**: Internal error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs