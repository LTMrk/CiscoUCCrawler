---
doc_id: webex-cloud-calling-post-telephony-config-people-me-settings-modemanagement-features-featureid-actions-extendmode-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/people/me/settings/modeManagement/features/{featureId}/actions/extendMode/invoke
operation_id: extendMode
tags: Mode Management
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.170889+00:00
---

# POST /telephony/config/people/me/settings/modeManagement/features/{featureId}/actions/extendMode/invoke

**API:** Webex Cloud Calling
**Área:** Mode Management
**operationId:** `extendMode`
**Autenticación:** bearer-key

## Resumen
Extend Current Operating Mode Duration

## Descripción
Extends the duration of the current operating mode by adding additional time before it expires or reverts to scheduled operation. This API allows managers to prolong a temporary mode change without having to switch modes again.

Extension time can be specified in 30-minute increments up to 720 minutes (12 hours). If no extension time is provided, the mode is extended with a manual switchback exception, meaning it will remain active until manually changed.

This API requires a user auth token with the `spark:telephony_config_write` scope. The authenticated user must be a mode manager for the specified feature.

## Parámetros
- `featureId` [path] (string) (**requerido**): Unique identifier for the feature.

## Cuerpo de la petición (application/json)
- `operatingModeId` (string) (**requerido**): Unique identifier for the operating mode for which the extension is being configured.
- `extensionTime` (integer): Extension time in minutes (must be multiple of 30). If not sent, mode is extended with manual switch back exception

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/people/me/settings/modeManagement/features/<featureId>/actions/extendMode/invoke' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"operatingModeId": "<operatingModeId>"}'
```

## Respuestas correctas
**204**: Mode extended successfully

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served.
  Ejemplo:
```json
{
  "errors": [
    {
      "description": "Error processing request"
    }
  ],
  "trackingId": "NA_7b1234567-1234-1234-1234-123456789abc_1234"
}
```
- **401**: Unauthorized
  Ejemplo:
```json
{
  "errors": [
    {
      "description": "Error processing request"
    }
  ],
  "trackingId": "NA_7b1234567-1234-1234-1234-123456789abc_1234"
}
```
- **403**: Forbidden
  Ejemplo:
```json
{
  "errors": [
    {
      "description": "Error processing request"
    }
  ],
  "trackingId": "NA_7b1234567-1234-1234-1234-123456789abc_1234"
}
```
- **404**: Not Found
  Ejemplo:
```json
{
  "errors": [
    {
      "description": "Error processing request"
    }
  ],
  "trackingId": "NA_7b1234567-1234-1234-1234-123456789abc_1234"
}
```
- **405**: Method Not Allowed
  Ejemplo:
```json
{
  "errors": [
    {
      "description": "Error processing request"
    }
  ],
  "trackingId": "NA_7b1234567-1234-1234-1234-123456789abc_1234"
}
```
- **409**: Conflict
  Ejemplo:
```json
{
  "errors": [
    {
      "description": "Error processing request"
    }
  ],
  "trackingId": "NA_7b1234567-1234-1234-1234-123456789abc_1234"
}
```
- **410**: Gone
  Ejemplo:
```json
{
  "errors": [
    {
      "description": "Error processing request"
    }
  ],
  "trackingId": "NA_7b1234567-1234-1234-1234-123456789abc_1234"
}
```
- **415**: Unsupported Media Type
  Ejemplo:
```json
{
  "errors": [
    {
      "description": "Error processing request"
    }
  ],
  "trackingId": "NA_7b1234567-1234-1234-1234-123456789abc_1234"
}
```
- **423**: Locked
  Ejemplo:
```json
{
  "errors": [
    {
      "description": "Error processing request"
    }
  ],
  "trackingId": "NA_7b1234567-1234-1234-1234-123456789abc_1234"
}
```
- **428**: Precondition Required
  Ejemplo:
```json
{
  "errors": [
    {
      "description": "Error processing request"
    }
  ],
  "trackingId": "NA_7b1234567-1234-1234-1234-123456789abc_1234"
}
```
- **429**: Too Many Requests
  Ejemplo:
```json
{
  "errors": [
    {
      "description": "Error processing request"
    }
  ],
  "trackingId": "NA_7b1234567-1234-1234-1234-123456789abc_1234"
}
```
- **500**: Internal Server Error
  Ejemplo:
```json
{
  "errors": [
    {
      "description": "Error processing request"
    }
  ],
  "trackingId": "NA_7b1234567-1234-1234-1234-123456789abc_1234"
}
```
- **502**: Bad Gateway
  Ejemplo:
```json
{
  "errors": [
    {
      "description": "Error processing request"
    }
  ],
  "trackingId": "NA_7b1234567-1234-1234-1234-123456789abc_1234"
}
```
- **503**: Service Unavailable
  Ejemplo:
```json
{
  "errors": [
    {
      "description": "Error processing request"
    }
  ],
  "trackingId": "NA_7b1234567-1234-1234-1234-123456789abc_1234"
}
```
- **504**: Gateway Timeout
  Ejemplo:
```json
{
  "errors": [
    {
      "description": "Error processing request"
    }
  ],
  "trackingId": "NA_7b1234567-1234-1234-1234-123456789abc_1234"
}
```

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs