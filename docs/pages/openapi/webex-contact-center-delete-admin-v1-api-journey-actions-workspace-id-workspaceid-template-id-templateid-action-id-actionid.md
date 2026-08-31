---
doc_id: webex-contact-center-delete-admin-v1-api-journey-actions-workspace-id-workspaceid-template-id-templateid-action-id-actionid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: DELETE
path: /admin/v1/api/journey-actions/workspace-id/{workspaceId}/template-id/{templateId}/action-id/{actionId}
operation_id: deleteJourneyActionById
tags: Journey - Trigger Actions API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.215118+00:00
---

# DELETE /admin/v1/api/journey-actions/workspace-id/{workspaceId}/template-id/{templateId}/action-id/{actionId}

**API:** Webex Contact Center
**Área:** Journey - Trigger Actions API
**operationId:** `deleteJourneyActionById`
**Autenticación:** bearerAuth

## Resumen
Delete Journey Action configuration By ActionId

## Descripción
Delete Journey Action configuration By ActionId in JDS. 

Role and Scope: It requires id full admin role with cjp:config_write scope.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Workspace ID
- `templateId` [path] (string) (**requerido**): Template ID
- `actionId` [path] (string) (**requerido**): Action ID

## Ejemplo de invocación
```bash
curl -X DELETE '/admin/v1/api/journey-actions/workspace-id/<workspaceId>/template-id/<templateId>/action-id/<actionId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Success
- `createdAt` (string): Created Timestamp
- `createdBy` (string): Created By
- `updatedAt` (string): Updated Timestamp
- `updatedBy` (string): Updated By
- `id` (string): Journey Action Id
- `name` (string): Journey Action Name
- `organizationId` (string): Organization Id
- `workspaceId` (string): Workspace Id
- `isActive` (boolean): Is Journey Action Configuration Active
- `templateId` (string): Profile View Template ID
- `cooldownPeriodInMinutes` (integer/int32): Cooldown Period In Minutes
- `rules` (object): Configuration details of the Rules based on which the Action will be triggered
  - `type` (string): type
  - `childrenRules` (object): childrenRules
    - `type` (string): type
- `actionTriggers` (array):
  - `type` (string) (**requerido**): Type

## Respuestas de error
- **404**: Not found
- **500**: Internal error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs