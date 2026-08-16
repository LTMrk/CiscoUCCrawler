---
doc_id: webex-contact-center-get-admin-v1-api-profile-view-template-workspace-id-workspaceid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /admin/v1/api/profile-view-template/workspace-id/{workspaceId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.971065+00:00
---

# GET /admin/v1/api/profile-view-template/workspace-id/{workspaceId}

**API:** Webex Contact Center
**Área:** Journey - Profile Creation & Insights API
**operationId:** `getAllTemplates`

## Resumen
Get All Template Details

## Descripción
Get Template details by Organization Id and workspaceId in JDS. 

Role and Scope: Requires id full admin role with cjp:config_write or cjp:config_read scope. Or requires any role with cjp:user, cjp:config_write or cjp:config_read scope.

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Workspace ID
- `filter` [query] (string): Optional filter which can be applied to the elements to be fetched.   This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see [this reference](https://developer.here.com/documentation/data-client-library/dev_guide/client/rsql.html). For a list of supported operators, see this [syntax guide](https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference).
- `sort` [query] (string): Sort direction
- `sortBy` [query] (string): Sort By Field
- `page` [query] (integer): Index of the page of results to be fetched.  Results are returned in blocks of pageSize elements. This parameter specifies which page number to retrieve.The page numbering starts with 0.
- `pageSize` [query] (integer): Number of items to be displayed on a page.

## Respuestas
- **200**: Success
  - `meta` (object): Meta information of the response
    - `organizationId` (string): Organization ID
  - `data` (array): Data part of the response
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
