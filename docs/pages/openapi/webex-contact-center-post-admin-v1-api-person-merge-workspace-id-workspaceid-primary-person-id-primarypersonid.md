---
doc_id: webex-contact-center-post-admin-v1-api-person-merge-workspace-id-workspaceid-primary-person-id-primarypersonid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /admin/v1/api/person/merge/workspace-id/{workspaceId}/primary-person-id/{primaryPersonId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.970164+00:00
---

# POST /admin/v1/api/person/merge/workspace-id/{workspaceId}/primary-person-id/{primaryPersonId}

**API:** Webex Contact Center
**Área:** Journey - Customer Identification API
**operationId:** `mergeAliases`

## Resumen
Merges Identities to a Primary Identity

## Descripción
Merges one/more Identities to a **Primary** Individual in JDS. 

Role and Scope: Requires id full admin role with cjp:config_write scope.

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Workspace ID
- `primaryPersonId` [path] (string) **(requerido)**: Primary Person ID

## Cuerpo de la petición (application/json)
- `personIdsToMerge` (array) **(requerido)**: List of Person Ids to merge

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
