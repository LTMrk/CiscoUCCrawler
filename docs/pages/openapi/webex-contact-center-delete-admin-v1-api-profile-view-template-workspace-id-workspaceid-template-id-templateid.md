---
doc_id: webex-contact-center-delete-admin-v1-api-profile-view-template-workspace-id-workspaceid-template-id-templateid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: DELETE
path: /admin/v1/api/profile-view-template/workspace-id/{workspaceId}/template-id/{templateId}
operation_id: deleteTemplatebyId
tags: Journey - Profile Creation & Insights API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.210983+00:00
---

# DELETE /admin/v1/api/profile-view-template/workspace-id/{workspaceId}/template-id/{templateId}

**API:** Webex Contact Center
**Área:** Journey - Profile Creation & Insights API
**operationId:** `deleteTemplatebyId`
**Autenticación:** bearerAuth

## Resumen
Delete Template by template Id

## Descripción
Delete Template By template id in JDS. 

Role and Scope: Requires id full admin or any role with cjp:config_write scope.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Workspace ID
- `templateId` [path] (string) (**requerido**): Template ID

## Ejemplo de invocación
```bash
curl -X DELETE '/admin/v1/api/profile-view-template/workspace-id/<workspaceId>/template-id/<templateId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Success
- `createdAt` (string): Created Timestamp
- `createdBy` (string): Created By
- `updatedAt` (string): Updated Timestamp
- `updatedBy` (string): Updated By
- `id` (string): Profile View Template Id
- `name` (string): Template Name
- `workspaceId` (string): Workspace Id
- `organizationId` (string): Organization Id
- `attributes` (array):
  - `displayName` (string): displayName
  - `version` (string): version
  - `event` (string): event
  - `metaDataType` (string): metaDataType
  - `metaData` (string): metaData
  - `limit` (integer/int32): limit
  - `lookBackDurationType` (string): lookBackDurationType
  - `lookBackPeriod` (integer/int32): lookBackPeriod
  - `aggregationMode` (string): aggregationMode
  - `verbose` (boolean): verbose
  - `widgetAttributes` (object): WidgetAttributes
    - `type` (string): type
  - `rules` (object): Configuration details of the Rules based on which the Action will be triggered
    - `type` (string): type
    - `childrenRules` (object): childrenRules
      - `type` (string): type

## Respuestas de error
- **404**: Not found
- **500**: Internal error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs