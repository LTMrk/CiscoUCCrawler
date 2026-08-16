---
doc_id: webex-contact-center-get-admin-v1-api-journey-actions-workspace-id-workspaceid-template-id-templateid-action-name-actionname
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /admin/v1/api/journey-actions/workspace-id/{workspaceId}/template-id/{templateId}/action-name/{actionName}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.973142+00:00
---

# GET /admin/v1/api/journey-actions/workspace-id/{workspaceId}/template-id/{templateId}/action-name/{actionName}

**API:** Webex Contact Center
**Área:** Journey - Trigger Actions API
**operationId:** `getJourneyActionDetailsByName`

## Resumen
Get specific Journey Action By Name

## Descripción
Get specific Journey Action By Name in JDS. 

Role and Scope:It requires id full admin or any role with cjp:config_read or cjp:config_write scope.

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Workspace ID
- `templateId` [path] (string) **(requerido)**: Template ID
- `actionName` [path] (string) **(requerido)**: Action Name

## Respuestas
- **200**: Success
  - `meta` (object): Meta information of the response
    - `organizationId` (string): Organization ID
  - `data` (object): Journey Action Configuration Response Model
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
    - `cooldownPeriodInMinutes` (integer): Cooldown Period In Minutes
    - `rules` (object): Configuration details of the Rules based on which the Action will be triggered
      - `type` (string): type
      - `childrenRules` (object): childrenRules
        - `type` (string): type
    - `actionTriggers` (array):
      - `type` (string) **(requerido)**: Type
- **404**: Not found
- **500**: Internal error

**Autenticación:** bearerAuth

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
