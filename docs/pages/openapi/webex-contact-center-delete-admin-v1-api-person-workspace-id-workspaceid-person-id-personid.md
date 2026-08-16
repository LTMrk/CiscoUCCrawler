---
doc_id: webex-contact-center-delete-admin-v1-api-person-workspace-id-workspaceid-person-id-personid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: DELETE
path: /admin/v1/api/person/workspace-id/{workspaceId}/person-id/{personId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.969428+00:00
---

# DELETE /admin/v1/api/person/workspace-id/{workspaceId}/person-id/{personId}

**API:** Webex Contact Center
**Área:** Journey - Customer Identification API
**operationId:** `deletePersonbyId`

## Resumen
Delete specific Person by id

## Descripción
Delete Person Details searched by Person id in JDS. 

Role and Scope: Requires id full admin or any role with cjp:config_write scope

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Workspace ID
- `personId` [path] (string) **(requerido)**: Person ID

## Respuestas
- **200**: Success
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
- **404**: Not found
- **500**: Internal error

**Autenticación:** bearerAuth

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
