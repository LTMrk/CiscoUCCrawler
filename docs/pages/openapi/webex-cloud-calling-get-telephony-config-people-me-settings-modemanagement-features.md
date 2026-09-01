---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-modemanagement-features
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/settings/modeManagement/features
operation_id: getModeManagementFeatures
tags: Mode Management
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.598493+00:00
---

# GET /telephony/config/people/me/settings/modeManagement/features

**API:** Webex Cloud Calling
**Área:** Mode Management
**operationId:** `getModeManagementFeatures`
**Autenticación:** bearer-key

## Resumen
Get Mode Management Features

## Descripción
Retrieves a list of all mode management features (Auto Attendants, Call Queues, and Hunt Groups) for which the authenticated user has been designated as a mode manager. This API returns basic information about each feature including its ID, name, and type.

Mode Management allows designated managers to switch features between different operational configurations based on time schedules or manual triggers. This is useful for managing business hours, holidays, and emergency scenarios.

This API requires a user auth token with the `spark:telephony_config_read` scope. The authenticated user must be configured as a mode manager for at least one feature to receive results.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/settings/modeManagement/features' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Mode management features retrieved successfully
- `features` (array) (**requerido**): List of mode management features. Returns all items in a single response.
  - `id` (string) (**requerido**): Unique identifier for the auto attendant, call queue, or hunt group.
  - `name` (string) (**requerido**): Display name of the auto attendant, call queue, or hunt group.
  - `type` (string) (**requerido**): * `AUTO_ATTENDANT` - Auto Attendant feature.  * `CALL_QUEUE` - Call Queue feature (includes customer assist queues).  * `HUNT_GROUP` - Hunt Group feature. Valores: AUTO_ATTENDANT, CALL_QUEUE, HUNT_GROUP.
  - `phoneNumber` (string): Phone number of the feature
  - `extension` (string): Extension of the feature
  - `modeBasedForwardingEnabled` (boolean) (**requerido**): Whether mode based forwarding is enabled for the feature
  - `location` (object): Location information for the feature
    - `id` (string) (**requerido**): Unique identifier for the location.
    - `name` (string) (**requerido**): Display name of the location.
  - `forwardDestination` (string): Current forward destination
  - `currentOperatingModeName` (string): Name of the current operating mode
  - `currentOperatingModeId` (string): ID of the current operating mode
  - `exceptionType` (string): Type of exception indicating how the feature will switch back from the current mode. This field is not present when the feature is in normal operation.   * `AUTOMATIC_SWITCH_BACK_EARLY_START` - Automatic switchback with early start.  * `AUTOMATIC_SWITCH_BACK_EXTENSION` - Automatic switchback with extension.  * `MANUAL_SWITCH_BACK` - Manual switchback required.  * `AUTOMATIC_SWITCH_BACK_STANDARD` - Standard automatic switchback. Valores: AUTOMATIC_SWITCH_BACK_EARLY_START, AUTOMATIC_SWITCH_BACK_EXTENSION, MANUAL_SWITCH_BACK, AUTOMATIC_SWITCH_BACK_STANDARD.

### Ejemplo — respuesta 200
```json
{
  "features": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0ZFQVRVUkUvYjQzMmI2NmQtM2VkYy00ZGNkLTg4ODctNDZlOGU2NWQwYzIw",
      "name": "Main Reception",
      "type": "AUTO_ATTENDANT",
      "phoneNumber": "+14085551234",
      "extension": "1234",
      "modeBasedForwardingEnabled": true,
      "location": {
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzEyMzQ1Njc4LTkwYWItY2RlZi0xMjM0LTU2Nzg5MGFiY2RlZg==",
        "name": "San Jose Office"
      },
      "forwardDestination": "+14085555678",
      "currentOperatingModeName": "Business Hours",
      "currentOperatingModeId": "Y2lzY29zcGFyazovL3VzL09QRVJBVElOR19NT0RFLzAyZjZlMmI4LTFjZDktNWI3ZS1jOTVjLTczYzZkYzk1MTZjMg==",
      "exceptionType": "MANUAL_SWITCH_BACK"
    }
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