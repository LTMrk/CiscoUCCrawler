---
doc_id: webex-contact-center-patch-admin-v1-api-person-add-identities-workspace-id-workspaceid-person-id-personid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PATCH
path: /admin/v1/api/person/add-identities/workspace-id/{workspaceId}/person-id/{personId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.969672+00:00
---

# PATCH /admin/v1/api/person/add-identities/workspace-id/{workspaceId}/person-id/{personId}

**API:** Webex Contact Center
**Área:** Journey - Customer Identification API
**operationId:** `addIdentitiesToPerson`

## Resumen
Add one/more Identities to a person

## Descripción
This Patch Api can be used to add identities(email, phone, customerId) to a person.

Role and Scope: Requires id full admin or any role with cjp:config_write scope.

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Workspace ID
- `personId` [path] (string) **(requerido)**: Person ID

## Cuerpo de la petición (application/json-patch+json)
- `phone` (array): Phone Number
- `email` (array): Email
- `temporaryId` (array): Temporary Id
- `customerId` (array): Customer Id

## Respuestas
- **200**: Ok
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
- **401**: UnAuthorized
- **404**: Resource not found
- **500**: Internal server error

**Autenticación:** bearerAuth

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
