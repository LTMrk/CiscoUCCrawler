---
doc_id: webex-contact-center-put-admin-v1-api-workspace-workspace-id-workspaceid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PUT
path: /admin/v1/api/workspace/workspace-id/{workspaceId}
operation_id: updateWorkspaceById
tags: Journey - Workspace management API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.770810+00:00
---

# PUT /admin/v1/api/workspace/workspace-id/{workspaceId}

**API:** Webex Contact Center
**Área:** Journey - Workspace management API
**operationId:** `updateWorkspaceById`
**Autenticación:** bearerAuth

## Resumen
Update Workspace

## Descripción
Update workspace by Id. Use the cjp scope if you have a contact center license; otherwise, use the cjds scope. It requires the appropriate cjds:admin_org_write or cjp:config_write scopes

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Workspace ID

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Workspace Name
- `description` (string) (**requerido**): Workspace Description

## Ejemplo de invocación
```bash
curl -X PUT '/admin/v1/api/workspace/workspace-id/<workspaceId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"description": "<description>", "name": "<name>"}'
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