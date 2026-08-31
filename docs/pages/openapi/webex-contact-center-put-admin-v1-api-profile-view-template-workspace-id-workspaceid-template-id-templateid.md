---
doc_id: webex-contact-center-put-admin-v1-api-profile-view-template-workspace-id-workspaceid-template-id-templateid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PUT
path: /admin/v1/api/profile-view-template/workspace-id/{workspaceId}/template-id/{templateId}
operation_id: updateProfileViewTemplate
tags: Journey - Profile Creation & Insights API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.765781+00:00
---

# PUT /admin/v1/api/profile-view-template/workspace-id/{workspaceId}/template-id/{templateId}

**API:** Webex Contact Center
**Área:** Journey - Profile Creation & Insights API
**operationId:** `updateProfileViewTemplate`
**Autenticación:** bearerAuth

## Resumen
Update existing ProfileViewTemplate

## Descripción
Update existing Profile View Template in JDS. 

Role and Scope: Requires id full admin or any role with cjp:config_write scope.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Workspace ID
- `templateId` [path] (string) (**requerido**): Template ID

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Template Name
- `attributes` (array) (**requerido**):
  - `displayName` (string) (**requerido**): displayName
  - `version` (string) (**requerido**): version
  - `event` (string) (**requerido**): event
  - `metaDataType` (string) (**requerido**): metaDataType
  - `metaData` (string) (**requerido**): metaData
  - `limit` (integer/int32) (**requerido**): limit
  - `lookBackDurationType` (string) (**requerido**): lookBackDurationType
  - `lookBackPeriod` (integer/int32) (**requerido**): lookBackPeriod
  - `aggregationMode` (string) (**requerido**): aggregationMode
  - `verbose` (boolean) (**requerido**): verbose
  - `widgetAttributes` (object): Create or Update WidgetAttributes
    - `type` (string): type
  - `rules` (object): Configuration details of the Rules
    - `logic` (string): logic
    - `args` (array): Arguments

## Ejemplo de invocación
```bash
curl -X PUT '/admin/v1/api/profile-view-template/workspace-id/<workspaceId>/template-id/<templateId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"attributes": [], "name": "<name>"}'
```

## Respuestas correctas
**200**: Ok
- `meta` (object): Meta information of the response
  - `organizationId` (string): Organization ID
- `data` (object): Template Response Model
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
- **400**: Bad Request
- **500**: Internal server error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs