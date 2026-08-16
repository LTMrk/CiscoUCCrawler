---
doc_id: webex-contact-center-get-admin-v1-api-wxcc-subscription-workspace-id-workspaceid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /admin/v1/api/wxcc-subscription/workspace-id/{workspaceId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.972467+00:00
---

# GET /admin/v1/api/wxcc-subscription/workspace-id/{workspaceId}

**API:** Webex Contact Center
**Área:** Journey - Subscription API
**operationId:** `getWXCCSubscription`

## Resumen
Get WXCC Subscription

## Descripción
Get WXCC Subscription in JDS. Use the cjp scope if you have a contact center license; otherwise, use the cjds scope. It requires the appropriate cjds:admin_org_read or cjds:admin_org_write scopes or cjp:config_read or cjp:config_write scopes

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Workspace ID

## Respuestas
- **200**: Ok
  - `meta` (object): Meta information of the response
    - `organizationId` (string): Organization ID
  - `data` (array): Data part of the response
    - `id` (string) **(requerido)**: Subscription ID
    - `name` (string) **(requerido)**: Subscription Name
    - `description` (string) **(requerido)**: Subscription Description
    - `eventTypes` (array) **(requerido)**: Event Types to be subscribed
    - `destinationUrl` (string) **(requerido)**: Destination URL
    - `createdTime` (integer) **(requerido)**: Created Time
    - `status` (string) **(requerido)**: Status
    - `lastUpdatedTime` (integer) **(requerido)**: Last Updated Time
- **404**: Resource not found
- **409**: Resource already exists
- **429**: Too many requests
- **500**: Internal server error

**Autenticación:** bearerAuth

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
