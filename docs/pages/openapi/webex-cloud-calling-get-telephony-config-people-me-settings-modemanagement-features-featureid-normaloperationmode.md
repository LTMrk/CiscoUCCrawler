---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-modemanagement-features-featureid-normaloperationmode
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/settings/modeManagement/features/{featureId}/normalOperationMode
operation_id: getNormalOperationMode
tags: Mode Management
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.600193+00:00
---

# GET /telephony/config/people/me/settings/modeManagement/features/{featureId}/normalOperationMode

**API:** Webex Cloud Calling
**Área:** Mode Management
**operationId:** `getNormalOperationMode`
**Autenticación:** bearer-key

## Resumen
Get Normal Operation Mode

## Descripción
Retrieves the current normal operating mode that the feature is scheduled to be in based on its time schedules. This represents the mode the feature would be in if no manual exceptions or overrides were active.

The normal operation mode is determined by the feature's configured schedules and may differ from the actual current operating mode if a manual exception has been applied. This API helps managers understand what the scheduled behavior is versus the actual current state.

This API requires a user auth token with the `spark:telephony_config_read` scope. The authenticated user must be a mode manager for the specified feature.

## Parámetros
- `featureId` [path] (string) (**requerido**): Unique identifier for the feature.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/settings/modeManagement/features/<featureId>/normalOperationMode' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Normal operation mode retrieved successfully
- `operatingModeId` (string) (**requerido**): Unique identifier for the scheduled operating mode.

### Ejemplo — respuesta 200
```json
{
  "operatingModeId": "Y2lzY29zcGFyazovL3VzL09QRVJBVElOR19NT0RFLzAyZjZlMmI4LTFjZDktNWI3ZS1jOTVjLTczYzZkYzk1MTZjMg=="
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