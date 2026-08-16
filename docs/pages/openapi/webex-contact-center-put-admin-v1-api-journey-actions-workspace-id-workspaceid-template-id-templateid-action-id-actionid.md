---
doc_id: webex-contact-center-put-admin-v1-api-journey-actions-workspace-id-workspaceid-template-id-templateid-action-id-actionid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PUT
path: /admin/v1/api/journey-actions/workspace-id/{workspaceId}/template-id/{templateId}/action-id/{actionId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.973376+00:00
---

# PUT /admin/v1/api/journey-actions/workspace-id/{workspaceId}/template-id/{templateId}/action-id/{actionId}

**API:** Webex Contact Center
**Área:** Journey - Trigger Actions API
**operationId:** `updateJourneyActionConfiguration`

## Resumen
Update existing Journey Action

## Descripción
Update existing Journey Action in JDS. 

Role and Scope: It requires id full admin or any role with cjp:config_write scope.

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Workspace ID
- `templateId` [path] (string) **(requerido)**: Template ID
- `actionId` [path] (string) **(requerido)**: Action ID

## Cuerpo de la petición (application/json)
- `name` (string) **(requerido)**: Name
- `cooldownPeriodInMinutes` (integer): Cooldown Period In Minutes
- `rules` (object) **(requerido)**: Configuration details of the Rules
  - `logic` (string): logic
  - `args` (array): Arguments
- `actionTriggers` (array):
  - `type` (string) **(requerido)**: Type
- `isActive` (boolean): Is Journey Action Configuration Active

## Respuestas
- **201**: Accepted
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
- **400**: Bad Request
- **500**: Internal server error

**Autenticación:** bearerAuth

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
