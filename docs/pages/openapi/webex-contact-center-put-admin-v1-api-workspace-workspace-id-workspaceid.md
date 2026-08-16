---
doc_id: webex-contact-center-put-admin-v1-api-workspace-workspace-id-workspaceid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PUT
path: /admin/v1/api/workspace/workspace-id/{workspaceId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.973701+00:00
---

# PUT /admin/v1/api/workspace/workspace-id/{workspaceId}

**API:** Webex Contact Center
**Área:** Journey - Workspace management API
**operationId:** `updateWorkspaceById`

## Resumen
Update Workspace

## Descripción
Update workspace by Id. Use the cjp scope if you have a contact center license; otherwise, use the cjds scope. It requires the appropriate cjds:admin_org_write or cjp:config_write scopes

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Workspace ID

## Cuerpo de la petición (application/json)
- `name` (string) **(requerido)**: Workspace Name
- `description` (string) **(requerido)**: Workspace Description

## Respuestas
- **200**: Ok
  - `meta` (object): Meta information of the response
    - `organizationId` (string): Organization ID
  - `data` (object): Workspace under an organization
    - `id` (string): Workspace ID
    - `name` (string): Workspace Name
    - `description` (string): Workspace Description
    - `wxccSubscriptionIds` (array): List of Wxcc Subscription Ids
- **404**: Resource not found
- **409**: Resource already exists
- **429**: Too many requests
- **500**: Internal server error

**Autenticación:** bearerAuth

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
