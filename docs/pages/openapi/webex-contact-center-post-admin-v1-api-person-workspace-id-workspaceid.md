---
doc_id: webex-contact-center-post-admin-v1-api-person-workspace-id-workspaceid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /admin/v1/api/person/workspace-id/{workspaceId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.970051+00:00
---

# POST /admin/v1/api/person/workspace-id/{workspaceId}

**API:** Webex Contact Center
**Área:** Journey - Customer Identification API
**operationId:** `createPerson`

## Resumen
Create a Person

## Descripción
This API helps to create a Person in JDS.

Role and Scope: Requires id full admin OR any role with cjp:config_write scope.

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Workspace ID

## Cuerpo de la petición (application/json)
- `firstName` (string): firstName
- `lastName` (string): lastName
- `phone` (array): Phone Number
- `email` (array): Email
- `temporaryId` (array): Temporary Id
- `customerId` (array): Customer Id

## Respuestas
- **201**: Created
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
- **404**: Resource not found
- **500**: Internal server error

**Autenticación:** bearerAuth

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
