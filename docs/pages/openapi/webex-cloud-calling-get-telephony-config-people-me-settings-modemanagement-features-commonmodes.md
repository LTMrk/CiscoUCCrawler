---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-modemanagement-features-commonmodes
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/settings/modeManagement/features/commonModes
operation_id: getCommonModes
tags: Mode Management
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.598934+00:00
---

# GET /telephony/config/people/me/settings/modeManagement/features/commonModes

**API:** Webex Cloud Calling
**Área:** Mode Management
**operationId:** `getCommonModes`
**Autenticación:** bearer-key

## Resumen
Get Common Modes

## Descripción
Retrieves a list of common operating mode names that are shared across multiple specified features. This API accepts a list of feature IDs and returns only the mode names that exist in all of the specified features, allowing managers to switch multiple features to the same mode simultaneously.

Common modes are useful when you need to coordinate operational changes across multiple features. For example, switching an entire office to "Holiday" mode across all Auto Attendants and Call Queues at once.

This API requires a user auth token with the `spark:telephony_config_read` scope. The authenticated user must be a mode manager for the specified features.

## Parámetros
- `featureIds` [query] (array) (**requerido**): List of feature IDs (comma-separated) for auto attendants, call queues, or hunt groups

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/settings/modeManagement/features/commonModes?featureIds=<featureIds>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Common modes retrieved successfully
- `commonModeNames` (array) (**requerido**): Array of operating mode names

### Ejemplo — respuesta 200
```json
{
  "commonModeNames": [
    "Day1",
    "Holiday1",
    "Operating Mode Outage"
  ]
}
```

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