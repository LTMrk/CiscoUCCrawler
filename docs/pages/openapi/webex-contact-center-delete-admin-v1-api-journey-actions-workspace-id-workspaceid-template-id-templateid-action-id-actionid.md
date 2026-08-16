---
doc_id: webex-contact-center-delete-admin-v1-api-journey-actions-workspace-id-workspaceid-template-id-templateid-action-id-actionid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: DELETE
path: /admin/v1/api/journey-actions/workspace-id/{workspaceId}/template-id/{templateId}/action-id/{actionId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.973483+00:00
---

# DELETE /admin/v1/api/journey-actions/workspace-id/{workspaceId}/template-id/{templateId}/action-id/{actionId}

**API:** Webex Contact Center
**Área:** Journey - Trigger Actions API
**operationId:** `deleteJourneyActionById`

## Resumen
Delete Journey Action configuration By ActionId

## Descripción
Delete Journey Action configuration By ActionId in JDS. 

Role and Scope: It requires id full admin role with cjp:config_write scope.

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Workspace ID
- `templateId` [path] (string) **(requerido)**: Template ID
- `actionId` [path] (string) **(requerido)**: Action ID

## Respuestas
- **200**: Success
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
