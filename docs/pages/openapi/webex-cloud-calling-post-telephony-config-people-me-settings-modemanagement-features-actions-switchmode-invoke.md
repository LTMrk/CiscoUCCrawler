---
doc_id: webex-cloud-calling-post-telephony-config-people-me-settings-modemanagement-features-actions-switchmode-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/people/me/settings/modeManagement/features/actions/switchMode/invoke
operation_id: switchModeMultipleFeatures
tags: Mode Management
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.599301+00:00
---

# POST /telephony/config/people/me/settings/modeManagement/features/actions/switchMode/invoke

**API:** Webex Cloud Calling
**Área:** Mode Management
**operationId:** `switchModeMultipleFeatures`
**Autenticación:** bearer-key

## Resumen
Switch Mode for Multiple Features

## Descripción
Switches the operating mode for multiple features simultaneously by specifying a common mode name. This API accepts a list of feature IDs and sets all of them to the specified operating mode, provided that mode exists for all features.

This bulk operation is particularly useful for coordinating operational changes across an organization, such as activating holiday modes, emergency procedures, or after-hours configurations across multiple Auto Attendants, Call Queues, and Hunt Groups at once.

This API requires a user auth token with the `spark:telephony_config_write` scope. The authenticated user must be a mode manager for all specified features.

## Cuerpo de la petición (application/json)
- `featureIds` (array) (**requerido**): List of feature IDs to switch mode
- `operatingModeName` (string) (**requerido**): Name of the common operating mode to be set as current operating mode

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/people/me/settings/modeManagement/features/actions/switchMode/invoke' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"featureIds": [], "operatingModeName": "<operatingModeName>"}'
```

## Respuestas correctas
**204**: Mode switched successfully for multiple features

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