---
doc_id: webex-contact-center-get-v1-api-progressive-profile-view-workspace-id-workspaceid-person-id-personid-template-id-templateid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /v1/api/progressive-profile-view/workspace-id/{workspaceId}/person-id/{personId}/template-id/{templateId}
operation_id: getProgressiveProfileView
tags: Journey - Profile Creation & Insights API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.815921+00:00
---

# GET /v1/api/progressive-profile-view/workspace-id/{workspaceId}/person-id/{personId}/template-id/{templateId}

**API:** Webex Contact Center
**Área:** Journey - Profile Creation & Insights API
**operationId:** `getProgressiveProfileView`
**Autenticación:** bearerAuth

## Resumen
Historic Progressive Profile View

## Descripción
Get Historic Progressive Profile View in JDS. 

Role and Scope: Requires id full admin role with cjds:admin_org_write or cjds:admin_org_read scope. Or requires any role with cjp:user, cjp:config_write or cjp:config_read scope.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Workspace ID
- `personId` [path] (string) (**requerido**): Person ID
- `templateId` [path] (string) (**requerido**): Template ID

## Ejemplo de invocación
```bash
curl -X GET '/v1/api/progressive-profile-view/workspace-id/<workspaceId>/person-id/<personId>/template-id/<templateId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Ok
- `meta` (object):
  - `organizationId` (string): Organization ID
  - `workspaceId` (string): Workspace ID
  - `personId` (string): personId
  - `templateId` (string): templateId
- `data` (array):
  - `workspaceId` (string) (**requerido**): Workspace ID
  - `organizationId` (string) (**requerido**): Organization ID
  - `personId` (string) (**requerido**): Person ID
  - `templateId` (string) (**requerido**): Template ID
  - `searchFilter` (string): search Filter
  - `attributes` (array): Attributes
    - `queryTemplate` (object): Attributes under an ProfileViewTemplate
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
    - `result` (string): Result Object
    - `error` (string): Error data
    - `journeyEvents` (array): Journey Events
  - `systemMetdata` (object): ProfileViewSystemMetdata
    - `journeyActionTriggerHistories` (array):
      - `actionId` (string) (**requerido**): Action Id
      - `triggeredAt` (string/date-time) (**requerido**): Triggered Date
      - `doNotDisturbPeriod` (string) (**requerido**): Do Not Disturb Period
  - `timestamp` (string): TimeStamp

## Respuestas de error
- **400**: Bad Request
- **404**: Not Found
- **500**: Internal server error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs