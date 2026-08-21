---
doc_id: webex-contact-center-patch-admin-v1-api-person-workspace-id-workspaceid-person-id-personid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PATCH
path: /admin/v1/api/person/workspace-id/{workspaceId}/person-id/{personId}
operation_id: addRemoveAliases
tags: Journey - Customer Identification API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.812460+00:00
---

# PATCH /admin/v1/api/person/workspace-id/{workspaceId}/person-id/{personId}

**API:** Webex Contact Center
**Área:** Journey - Customer Identification API
**operationId:** `addRemoveAliases`
**Autenticación:** bearerAuth

## Resumen
Add/Remove/Replace details of a Person

## Descripción
The Patch Api can be used to add/remove identities(email, phone, customerId) or replace firstName and lastName of an Individual. We support only add, replace and remove operations. 

For a more information on Patch Requests, see this  [JSON PATCH guide](https://jsonpatch.com). 

Role and Scope: Requires id full admin role with cjp:config_write or any role with cjp:user or cjp:config_write scope.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Workspace ID
- `personId` [path] (string) (**requerido**): Person ID

## Cuerpo de la petición (application/json-patch+json)
- (array de:)
  - `op` (string) (**requerido**): The operation to be performed Valores: add, update, remove.
  - `path` (string) (**requerido**): A JSON-Pointer
  - `value` (string): The value to be used within the operations.

## Ejemplo de invocación
```bash
curl -X PATCH '/admin/v1/api/person/workspace-id/<workspaceId>/person-id/<personId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**202**: Accepted
- `meta` (object): Meta information of the response
  - `organizationId` (string): Organization ID
- `data` (object): Person Response Model
  - `id` (string): Profile View Template Id
  - `firstName` (string): firstName
  - `lastName` (string): lastName
  - `phone` (array): Phone Number
  - `email` (array): Email
  - `temporaryId` (array): Temporary Id
  - `customerId` (array): Customer Id
  - `aliases` (array): Aliases

## Respuestas de error
- **400**: Bad Request
- **404**: Not found
- **500**: Internal error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs