---
doc_id: webex-contact-center-delete-admin-v1-api-profile-view-template-workspace-id-workspaceid-template-id-templateid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: DELETE
path: /admin/v1/api/profile-view-template/workspace-id/{workspaceId}/template-id/{templateId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.970947+00:00
---

# DELETE /admin/v1/api/profile-view-template/workspace-id/{workspaceId}/template-id/{templateId}

**API:** Webex Contact Center
**Área:** Journey - Profile Creation & Insights API
**operationId:** `deleteTemplatebyId`

## Resumen
Delete Template by template Id

## Descripción
Delete Template By template id in JDS. 

Role and Scope: Requires id full admin or any role with cjp:config_write scope.

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Workspace ID
- `templateId` [path] (string) **(requerido)**: Template ID

## Respuestas
- **200**: Success
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
