---
doc_id: webex-contact-center-put-admin-v1-api-profile-view-template-workspace-id-workspaceid-template-id-templateid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PUT
path: /admin/v1/api/profile-view-template/workspace-id/{workspaceId}/template-id/{templateId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.970801+00:00
---

# PUT /admin/v1/api/profile-view-template/workspace-id/{workspaceId}/template-id/{templateId}

**API:** Webex Contact Center
**Área:** Journey - Profile Creation & Insights API
**operationId:** `updateProfileViewTemplate`

## Resumen
Update existing ProfileViewTemplate

## Descripción
Update existing Profile View Template in JDS. 

Role and Scope: Requires id full admin or any role with cjp:config_write scope.

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Workspace ID
- `templateId` [path] (string) **(requerido)**: Template ID

## Cuerpo de la petición (application/json)
- `name` (string) **(requerido)**: Template Name
- `attributes` (array) **(requerido)**:
  - `displayName` (string) **(requerido)**: displayName
  - `version` (string) **(requerido)**: version
  - `event` (string) **(requerido)**: event
  - `metaDataType` (string) **(requerido)**: metaDataType
  - `metaData` (string) **(requerido)**: metaData
  - `limit` (integer) **(requerido)**: limit
  - `lookBackDurationType` (string) **(requerido)**: lookBackDurationType
  - `lookBackPeriod` (integer) **(requerido)**: lookBackPeriod
  - `aggregationMode` (string) **(requerido)**: aggregationMode
  - `verbose` (boolean) **(requerido)**: verbose
  - `widgetAttributes` (object): Create or Update WidgetAttributes
    - `type` (string): type
  - `rules` (object): Configuration details of the Rules
    - `logic` (string): logic
    - `args` (array): Arguments

## Respuestas
- **200**: Ok
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
- **400**: Bad Request
- **500**: Internal server error

**Autenticación:** bearerAuth

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
