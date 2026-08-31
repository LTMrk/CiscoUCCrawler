---
doc_id: webex-contact-center-get-admin-v1-api-journey-actions-workspace-id-workspaceid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /admin/v1/api/journey-actions/workspace-id/{workspaceId}
operation_id: getAllJourneyActions
tags: Journey - Trigger Actions API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.213995+00:00
---

# GET /admin/v1/api/journey-actions/workspace-id/{workspaceId}

**API:** Webex Contact Center
**Área:** Journey - Trigger Actions API
**operationId:** `getAllJourneyActions`
**Autenticación:** bearerAuth

## Resumen
Get all Journey Actions

## Descripción
Get all Journey Actions in JDS. 

Role and Scope: Requires id full admin or any role with cjp:config_write or cjp:config_read scope.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Workspace ID
- `sortBy` [query] (string): Sort By Field
- `sort` [query] (string): Sort direction
- `page` [query] (integer): Index of the page of results to be fetched.  Results are returned in blocks of pageSize elements. This parameter specifies which page number to retrieve. The page numbering starts with 0.
- `pageSize` [query] (integer): Number of items to be displayed on a page.

## Ejemplo de invocación
```bash
curl -X GET '/admin/v1/api/journey-actions/workspace-id/<workspaceId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Success
- `meta` (object): Meta information of the response
  - `organizationId` (string): Organization ID
- `data` (array): Data part of the response
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