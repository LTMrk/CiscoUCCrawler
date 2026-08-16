---
doc_id: webex-contact-center-patch-admin-v1-api-person-workspace-id-workspaceid-person-id-personid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PATCH
path: /admin/v1/api/person/workspace-id/{workspaceId}/person-id/{personId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.969537+00:00
---

# PATCH /admin/v1/api/person/workspace-id/{workspaceId}/person-id/{personId}

**API:** Webex Contact Center
**Área:** Journey - Customer Identification API
**operationId:** `addRemoveAliases`

## Resumen
Add/Remove/Replace details of a Person

## Descripción
The Patch Api can be used to add/remove identities(email, phone, customerId) or replace firstName and lastName of an Individual. We support only add, replace and remove operations. 

For a more information on Patch Requests, see this  [JSON PATCH guide](https://jsonpatch.com). 

Role and Scope: Requires id full admin role with cjp:config_write or any role with cjp:user or cjp:config_write scope.

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Workspace ID
- `personId` [path] (string) **(requerido)**: Person ID

## Cuerpo de la petición (application/json-patch+json)
- (array de:)
  - `op` (string) **(requerido)**: The operation to be performed Valores: add, update, remove.
  - `path` (string) **(requerido)**: A JSON-Pointer
  - `value` (string): The value to be used within the operations.

## Respuestas
- **202**: Accepted
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
- **400**: Bad Request
- **404**: Not found
- **500**: Internal error

**Autenticación:** bearerAuth

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
