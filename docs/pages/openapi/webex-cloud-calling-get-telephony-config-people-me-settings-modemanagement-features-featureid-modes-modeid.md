---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-modemanagement-features-featureid-modes-modeid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/settings/modeManagement/features/{featureId}/modes/{modeId}
operation_id: getOperatingMode
tags: Mode Management
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.381599+00:00
---

# GET /telephony/config/people/me/settings/modeManagement/features/{featureId}/modes/{modeId}

**API:** Webex Cloud Calling
**Área:** Mode Management
**operationId:** `getOperatingMode`
**Autenticación:** bearer-key

## Resumen
Get Operating Mode

## Descripción
Retrieves detailed information about a specific operating mode for a feature, including the mode's ID and name. This API allows managers to get the details of any operating mode configured for a feature.

Operating modes define different configurations for how a feature behaves (e.g., business hours routing vs. after-hours routing). Each mode has a unique ID and a descriptive name that helps managers identify its purpose.

This API requires a user auth token with the `spark:telephony_config_read` scope. The authenticated user must be a mode manager for the specified feature.

## Parámetros
- `featureId` [path] (string) (**requerido**): Unique identifier for the feature.
- `modeId` [path] (string) (**requerido**): Unique identifier for the operating mode.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/settings/modeManagement/features/<featureId>/modes/<modeId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Operating mode retrieved successfully
- `operatingModeId` (string) (**requerido**): Unique identifier for the operating mode.
- `name` (string) (**requerido**): Display name of the operating mode.
- `type` (string) (**requerido**): * `NONE` - No schedule defined.  * `SAME_HOURS_DAILY` - Same hours apply for weekdays (Monday-Friday) and weekends (Saturday-Sunday).  * `DIFFERENT_HOURS_DAILY` - Different hours for each day of the week.  * `HOLIDAY` - Holiday-based schedule. Valores: NONE, SAME_HOURS_DAILY, DIFFERENT_HOURS_DAILY, HOLIDAY.
- `level` (string) (**requerido**): * `LOCATION` - Operating mode is defined at the location level.  * `ORGANIZATION` - Operating mode is defined at the organization level. Valores: LOCATION, ORGANIZATION.
- `locationName` (string): Location name
- `sameHoursDaily` (object): Schedule configuration when same hours apply for weekdays and weekends
  - `mondayToFriday` (object):
    - `enabled` (boolean) (**requerido**): Whether schedule is enabled for Monday to Friday
    - `allDayEnabled` (boolean) (**requerido**): Whether all day is enabled
    - `startTime` (string): Start time in HH:mm format. This field is not present when allDayEnabled is true.
    - `endTime` (string): End time in HH:mm format. This field is not present when allDayEnabled is true.
  - `saturdayToSunday` (object):
    - `enabled` (boolean) (**requerido**): Whether schedule is enabled for Saturday to Sunday
    - `allDayEnabled` (boolean) (**requerido**): Whether all day is enabled
    - `startTime` (string): Start time in HH:mm format. This field is not present when allDayEnabled is true.
    - `endTime` (string): End time in HH:mm format. This field is not present when allDayEnabled is true.
- `differentHoursDaily` (object): Schedule configuration when different hours apply for each day
  - `sunday` (object):
    - `enabled` (boolean) (**requerido**): Whether schedule is enabled for Sunday.
    - `allDayEnabled` (boolean) (**requerido**): Whether all day is enabled.
    - `startTime` (string): Start time in HH:mm format. This field is not present when allDayEnabled is true.
    - `endTime` (string): End time in HH:mm format. This field is not present when allDayEnabled is true.
  - `monday` (object):
    - `enabled` (boolean) (**requerido**): Whether schedule is enabled for Monday.
    - `allDayEnabled` (boolean) (**requerido**): Whether all day is enabled.
    - `startTime` (string): Start time in HH:mm format. This field is not present when allDayEnabled is true.
    - `endTime` (string): End time in HH:mm format. This field is not present when allDayEnabled is true.
  - `tuesday` (object):
    - `enabled` (boolean) (**requerido**): Whether schedule is enabled for Tuesday.
    - `allDayEnabled` (boolean) (**requerido**): Whether all day is enabled.
    - `startTime` (string): Start time in HH:mm format. This field is not present when allDayEnabled is true.
    - `endTime` (string): End time in HH:mm format. This field is not present when allDayEnabled is true.
  - `wednesday` (object):
    - `enabled` (boolean) (**requerido**): Whether schedule is enabled for Wednesday.
    - `allDayEnabled` (boolean) (**requerido**): Whether all day is enabled.
    - `startTime` (string): Start time in HH:mm format. This field is not present when allDayEnabled is true.
    - `endTime` (string): End time in HH:mm format. This field is not present when allDayEnabled is true.
  - `thursday` (object):
    - `enabled` (boolean) (**requerido**): Whether schedule is enabled for Thursday.
    - `allDayEnabled` (boolean) (**requerido**): Whether all day is enabled.
    - `startTime` (string): Start time in HH:mm format. This field is not present when allDayEnabled is true.
    - `endTime` (string): End time in HH:mm format. This field is not present when allDayEnabled is true.
  - `friday` (object):
    - `enabled` (boolean) (**requerido**): Whether schedule is enabled for Friday.
    - `allDayEnabled` (boolean) (**requerido**): Whether all day is enabled.
    - `startTime` (string): Start time in HH:mm format. This field is not present when allDayEnabled is true.
    - `endTime` (string): End time in HH:mm format. This field is not present when allDayEnabled is true.
  - `saturday` (object):
    - `enabled` (boolean) (**requerido**): Whether schedule is enabled for Saturday.
    - `allDayEnabled` (boolean) (**requerido**): Whether all day is enabled.
    - `startTime` (string): Start time in HH:mm format. This field is not present when allDayEnabled is true.
    - `endTime` (string): End time in HH:mm format. This field is not present when allDayEnabled is true.
- `holidays` (array): Array of holiday schedule events
  - `id` (string): Unique identifier for the holiday schedule event.
  - `name` (string): Holiday event name
  - `allDayEnabled` (boolean): Whether holiday is all day
  - `startDate` (string): Start date in YYYY-MM-DD format.
  - `endDate` (string): End date in YYYY-MM-DD format.
  - `startTime` (string): Start time in HH:mm format. This field is not present when allDayEnabled is true.
  - `endTime` (string): End time in HH:mm format. This field is not present when allDayEnabled is true.

### Ejemplo — respuesta 200
```json
{
  "operatingModeId": "Y2lzY29zcGFyazovL3VzL09QRVJBVElOR19NT0RFLzAyZjZlMmI4LTFjZDktNWI3ZS1jOTVjLTczYzZkYzk1MTZjMg==",
  "name": "Business Hours Mode",
  "type": "SAME_HOURS_DAILY",
  "level": "LOCATION",
  "locationName": "San Jose",
  "sameHoursDaily": {
    "mondayToFriday": {
      "enabled": true,
      "allDayEnabled": false,
      "startTime": "09:00",
      "endTime": "17:00"
    },
    "saturdayToSunday": {
      "enabled": false,
      "allDayEnabled": false,
      "startTime": "10:00",
      "endTime": "14:00"
    }
  },
  "forwardTo": {
    "enabled": true,
    "destination": "+14085551234",
    "sendToVoicemailEnabled": false
  }
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