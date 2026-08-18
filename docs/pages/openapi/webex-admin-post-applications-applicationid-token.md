---
doc_id: webex-admin-post-applications-applicationid-token
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: POST
path: /applications/{applicationId}/token
operation_id: createServiceAppAccessToken
tags: Service Apps
deprecated: false
scopes: spark:applications_token
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.589734+00:00
---

# POST /applications/{applicationId}/token

**API:** Webex Admin
**Área:** Service Apps
**operationId:** `createServiceAppAccessToken`
**Scopes requeridos:** `spark:applications_token`

## Resumen
Create Service App Access Token

## Descripción
Retrieves an organization specific token pair for an already authorized Service App. Service Apps use machine accounts to make API calls on behalf of an organization, independent of individual user life cycles.

This endpoint allows you to programmatically retrieve access and refresh tokens after a Full Admin has authorized your Service App in Control Hub.

To call this endpoint, you need an integration with the spark:applications_token scope.

## Parámetros
- `applicationId` [path] (string) (**requerido**): The unique identifier of the Service App

## Cuerpo de la petición (application/json)
- `clientId` (string) (**requerido**): The OAuth client ID of the Service App
- `clientSecret` (string/password) (**requerido**): The OAuth client secret of the Service App
- `targetOrgId` (string) (**requerido**): The organization ID for which the token will be created

## Ejemplo de invocación
```bash
curl -X POST '/applications/<applicationId>/token' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"clientId": "<clientId>", "clientSecret": "<clientSecret>", "targetOrgId": "<targetOrgId>"}'
```

## Respuestas correctas
**200**: Successfully created Service App access token
- `access_token` (string): The OAuth 2.0 access token
- `expires_in` (integer/int64): Token expiration time in seconds
- `refresh_token` (string): The OAuth 2.0 refresh token (if applicable)
- `refresh_token_expires_in` (integer): Refresh token expiration time in seconds
- `token_type` (string): The type of token issued

### Ejemplo — respuesta 200
```json
{
  "access_token": "ZmFrZVRva2VuRm9yRXhhbXBsZVB1cnBvc2VzT25seQ...",
  "expires_in": 3600,
  "refresh_token": "ZmFrZVJlZnJlc2hUb2tlbkZvckV4YW1wbGVPbmx5...",
  "refresh_token_expires_in": 7776000,
  "token_type": "Bearer"
}
```

## Respuestas de error
- **400**: Bad request - Invalid input parameters
  Ejemplo:
```json
{
  "message": "Invalid client credentials",
  "trackingId": "ROUTER_1234567890ABCDEF",
  "errors": [
    {
      "description": "The provided clientSecret is invalid"
    }
  ]
}
```
- **401**: Unauthorized - Authentication required
  Ejemplo:
```json
{
  "message": "Invalid client credentials",
  "trackingId": "ROUTER_1234567890ABCDEF",
  "errors": [
    {
      "description": "The provided clientSecret is invalid"
    }
  ]
}
```
- **403**: Forbidden - Insufficient permissions or Service App not authorized by Full Admin in Control Hub
  Ejemplo:
```json
{
  "message": "Invalid client credentials",
  "trackingId": "ROUTER_1234567890ABCDEF",
  "errors": [
    {
      "description": "The provided clientSecret is invalid"
    }
  ]
}
```
- **404**: Service App not found
  Ejemplo:
```json
{
  "message": "Invalid client credentials",
  "trackingId": "ROUTER_1234567890ABCDEF",
  "errors": [
    {
      "description": "The provided clientSecret is invalid"
    }
  ]
}
```

## Contexto de la API
The Webex Admin APIs provide comprehensive programmatic access to administrative functions for managing Webex organizations, users, licenses, and settings. These APIs enable automation of user provisioning, license assignment, compliance management, and audit event retrieval. Administrators can integrate with enterprise identity systems, enforce security policies, monitor usage, and streamline onboarding/offboarding processes. The APIs support granular control over organizational resources, making them ideal for large-scale deployments and custom admin tooling.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs