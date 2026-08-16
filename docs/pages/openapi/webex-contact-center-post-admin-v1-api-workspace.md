---
doc_id: webex-contact-center-post-admin-v1-api-workspace
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /admin/v1/api/workspace
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.974004+00:00
---

# POST /admin/v1/api/workspace

**API:** Webex Contact Center
**Área:** Journey - Workspace management API
**operationId:** `createWorkspace`

## Resumen
Create Workspace

## Descripción
Create Workspace in JDS. Use the cjp scope if you have a contact center license; otherwise, use the cjds scope.It requires the appropriate cjds:admin_org_write or cjp:config_write scopes

## Cuerpo de la petición (application/json)
- `name` (string) **(requerido)**: Workspace Name
- `description` (string) **(requerido)**: Workspace Description

## Respuestas
- **200**: Ok
  - `meta` (object): Meta information of the response
    - `organizationId` (string): Organization ID
  - `data` (object): Organization Response Model
    - `createdAt` (string): Created Timestamp
    - `createdBy` (string): Created By
    - `updatedAt` (string): Updated Timestamp
    - `updatedBy` (string): Updated By
    - `organizationId` (string): Organization ID
    - `name` (string): Organization Name
    - `isActive` (boolean): Is An Organization Active
    - `workspaces` (array): Workspaces
      - `id` (string): Workspace ID
      - `name` (string): Workspace Name
      - `description` (string): Workspace Description
      - `wxccSubscriptionIds` (array): List of Wxcc Subscription Ids
    - `enabledFeatureIds` (array): Enabled Feature Ids
    - `settings` (object): Create Or Update Organization Settings
      - `general` (object): Create Or Update Organization General Settings
        - `dataRetentionDays` (integer): Data Retention Days
      - `webex` (object): Create Or Update Organization Webex Settings
        - `env` (string): Webex Environment Name
- **404**: Resource not found
- **409**: Resource already exists
- **429**: Too many requests
- **500**: Internal server error

**Autenticación:** bearerAuth

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
