---
doc_id: webex-contact-center-delete-admin-v1-api-workspace-workspace-id-workspaceid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: DELETE
path: /admin/v1/api/workspace/workspace-id/{workspaceId}
operation_id: deleteWorkspaceById
tags: Journey - Workspace management API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.215628+00:00
---

# DELETE /admin/v1/api/workspace/workspace-id/{workspaceId}

**API:** Webex Contact Center
**Área:** Journey - Workspace management API
**operationId:** `deleteWorkspaceById`
**Autenticación:** bearerAuth

## Resumen
Delete Workspace

## Descripción
Delete Workspace By Id. Use the cjp scope if you have a contact center license; otherwise, use the cjds scope. It requires the appropriate cjds:admin_org_write or cjp:config_write scopes

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Workspace ID

## Ejemplo de invocación
```bash
curl -X DELETE '/admin/v1/api/workspace/workspace-id/<workspaceId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Ok
- `meta` (object): Meta information of the response
  - `organizationId` (string): Organization ID
- `data` (object): Workspace under an organization
  - `id` (string): Workspace ID
  - `name` (string): Workspace Name
  - `description` (string): Workspace Description
  - `wxccSubscriptionIds` (array): List of Wxcc Subscription Ids

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