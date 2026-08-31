---
doc_id: webex-contact-center-get-admin-v1-api-profile-view-template-workspace-id-workspaceid-template-name-templatename
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /admin/v1/api/profile-view-template/workspace-id/{workspaceId}/template-name/{templateName}
operation_id: getTemplatebyName
tags: Journey - Profile Creation & Insights API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.211644+00:00
---

# GET /admin/v1/api/profile-view-template/workspace-id/{workspaceId}/template-name/{templateName}

**API:** Webex Contact Center
**Área:** Journey - Profile Creation & Insights API
**operationId:** `getTemplatebyName`
**Autenticación:** bearerAuth

## Resumen
Get A specific Template searched by template name

## Descripción
Get Template details by template Name in JDS. 

Role and Scope: Requires id full admin role with cjp:config_write or cjp:config_read scope. Or requires any role with cjp:user, cjp:config_write or cjp:config_read scope.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Workspace ID
- `templateName` [path] (string) (**requerido**): Template Name

## Ejemplo de invocación
```bash
curl -X GET '/admin/v1/api/profile-view-template/workspace-id/<workspaceId>/template-name/<templateName>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Success
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
- **404**: Not found
- **500**: Internal error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs