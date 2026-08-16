---
doc_id: webex-contact-center-get-admin-v1-api-profile-view-template-workspace-id-workspaceid-template-name-templatename
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /admin/v1/api/profile-view-template/workspace-id/{workspaceId}/template-name/{templateName}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.971324+00:00
---

# GET /admin/v1/api/profile-view-template/workspace-id/{workspaceId}/template-name/{templateName}

**API:** Webex Contact Center
**Área:** Journey - Profile Creation & Insights API
**operationId:** `getTemplatebyName`

## Resumen
Get A specific Template searched by template name

## Descripción
Get Template details by template Name in JDS. 

Role and Scope: Requires id full admin role with cjp:config_write or cjp:config_read scope. Or requires any role with cjp:user, cjp:config_write or cjp:config_read scope.

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Workspace ID
- `templateName` [path] (string) **(requerido)**: Template Name

## Respuestas
- **200**: Success
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
      - `limit` (integer): limit
      - `lookBackDurationType` (string): lookBackDurationType
      - `lookBackPeriod` (integer): lookBackPeriod
      - `aggregationMode` (string): aggregationMode
      - `verbose` (boolean): verbose
      - `widgetAttributes` (object): WidgetAttributes
        - `type` (string): type
      - `rules` (object): Configuration details of the Rules based on which the Action will be triggered
        - `type` (string): type
        - `childrenRules` (object): childrenRules
          - `type` (string): type
- **404**: Not found
- **500**: Internal error

**Autenticación:** bearerAuth

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
