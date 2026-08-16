---
doc_id: webex-admin-post-applications-applicationid-token
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: POST
path: /applications/{applicationId}/token
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.163223+00:00
---

# POST /applications/{applicationId}/token

**API:** Webex Admin
**Área:** Service Apps
**operationId:** `createServiceAppAccessToken`

## Resumen
Create Service App Access Token

## Descripción
Retrieves an organization specific token pair for an already authorized Service App. Service Apps use machine accounts to make API calls on behalf of an organization, independent of individual user life cycles.

This endpoint allows you to programmatically retrieve access and refresh tokens after a Full Admin has authorized your Service App in Control Hub.

To call this endpoint, you need an integration with the spark:applications_token scope.

## Parámetros
- `applicationId` [path] (string) **(requerido)**: The unique identifier of the Service App

## Cuerpo de la petición (application/json)
- `clientId` (string) **(requerido)**: The OAuth client ID of the Service App
- `clientSecret` (string) **(requerido)**: The OAuth client secret of the Service App
- `targetOrgId` (string) **(requerido)**: The organization ID for which the token will be created

## Respuestas
- **200**: Successfully created Service App access token
  - `access_token` (string): The OAuth 2.0 access token
  - `expires_in` (integer): Token expiration time in seconds
  - `refresh_token` (string): The OAuth 2.0 refresh token (if applicable)
  - `refresh_token_expires_in` (integer): Refresh token expiration time in seconds
  - `token_type` (string): The type of token issued
- **400**: Bad request - Invalid input parameters
- **401**: Unauthorized - Authentication required
- **403**: Forbidden - Insufficient permissions or Service App not authorized by Full Admin in Control Hub
- **404**: Service App not found

**Autenticación:** bearerAuth

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
