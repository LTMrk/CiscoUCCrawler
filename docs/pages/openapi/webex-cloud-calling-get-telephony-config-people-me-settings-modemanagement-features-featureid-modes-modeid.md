---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-modemanagement-features-featureid-modes-modeid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/modeManagement/features/{featureId}/modes/{modeId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.575179+00:00
---

# GET /telephony/config/people/me/settings/modeManagement/features/{featureId}/modes/{modeId}

**API:** Webex Cloud Calling
**Área:** Mode Management
**operationId:** `getOperatingMode`

## Resumen
Get Operating Mode

## Descripción
Retrieves detailed information about a specific operating mode for a feature, including the mode's ID and name. This API allows managers to get the details of any operating mode configured for a feature.

Operating modes define different configurations for how a feature behaves (e.g., business hours routing vs. after-hours routing). Each mode has a unique ID and a descriptive name that helps managers identify its purpose.

This API requires a user auth token with the `spark:telephony_config_read` scope. The authenticated user must be a mode manager for the specified feature.

## Parámetros
- `featureId` [path] (string) **(requerido)**: Unique identifier for the feature.
- `modeId` [path] (string) **(requerido)**: Unique identifier for the operating mode.

## Respuestas
- **200**: Operating mode retrieved successfully
  - `operatingModeId` (string) **(requerido)**: Unique identifier for the operating mode.
  - `name` (string) **(requerido)**: Display name of the operating mode.
  - `type` (string) **(requerido)**: * `NONE` - No schedule defined.  * `SAME_HOURS_DAILY` - Same hours apply for weekdays (Monday-Friday) and weekends (Saturday-Sunday).  * `DIFFERENT_HOURS_DAILY` - Different hours for each day of the week.  * `HOLIDAY` - Holiday-based schedule. Valores: NONE, SAME_HOURS_DAILY, DIFFERENT_HOURS_DAILY, HOLIDAY.
  - `level` (string) **(requerido)**: * `LOCATION` - Operating mode is defined at the location level.  * `ORGANIZATION` - Operating mode is defined at the organization level. Valores: LOCATION, ORGANIZATION.
  - `locationName` (string): Location name
  - `sameHoursDaily` (object): Schedule configuration when same hours apply for weekdays and weekends
    - `mondayToFriday` (object):
      - `enabled` (boolean) **(requerido)**: Whether schedule is enabled for Monday to Friday
      - `allDayEnabled` (boolean) **(requerido)**: Whether all day is enabled
      - `startTime` (string): Start time in HH:mm format. This field is not present when allDayEnabled is true.
      - `endTime` (string): End time in HH:mm format. This field is not present when allDayEnabled is true.
    - `saturdayToSunday` (object):
      - `enabled` (boolean) **(requerido)**: Whether schedule is enabled for Saturday to Sunday
      - `allDayEnabled` (boolean) **(requerido)**: Whether all day is enabled
      - `startTime` (string): Start time in HH:mm format. This field is not present when allDayEnabled is true.
      - `endTime` (string): End time in HH:mm format. This field is not present when allDayEnabled is true.
  - `differentHoursDaily` (object): Schedule configuration when different hours apply for each day
    - `sunday` (object):
      - `enabled` (boolean) **(requerido)**: Whether schedule is enabled for Sunday.
      - `allDayEnabled` (boolean) **(requerido)**: Whether all day is enabled.
      - `startTime` (string): Start time in HH:mm format. This field is not present when allDayEnabled is true.
      - `endTime` (string): End time in HH:mm format. This field is not present when allDayEnabled is true.
    - `monday` (object):
      - `enabled` (boolean) **(requerido)**: Whether schedule is enabled for Monday.
      - `allDayEnabled` (boolean) **(requerido)**: Whether all day is enabled.
      - `startTime` (string): Start time in HH:mm format. This field is not present when allDayEnabled is true.
      - `endTime` (string): End time in HH:mm format. This field is not present when allDayEnabled is true.
    - `tuesday` (object):
      - `enabled` (boolean) **(requerido)**: Whether schedule is enabled for Tuesday.
      - `allDayEnabled` (boolean) **(requerido)**: Whether all day is enabled.
      - `startTime` (string): Start time in HH:mm format. This field is not present when allDayEnabled is true.
      - `endTime` (string): End time in HH:mm format. This field is not present when allDayEnabled is true.
    - `wednesday` (object):
      - `enabled` (boolean) **(requerido)**: Whether schedule is enabled for Wednesday.
      - `allDayEnabled` (boolean) **(requerido)**: Whether all day is enabled.
      - `startTime` (string): Start time in HH:mm format. This field is not present when allDayEnabled is true.
      - `endTime` (string): End time in HH:mm format. This field is not present when allDayEnabled is true.
    - `thursday` (object):
      - `enabled` (boolean) **(requerido)**: Whether schedule is enabled for Thursday.
      - `allDayEnabled` (boolean) **(requerido)**: Whether all day is enabled.
- **400**: Bad Request: The request was invalid or cannot be otherwise served.
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **405**: Method Not Allowed
- **409**: Conflict
- **410**: Gone
- **415**: Unsupported Media Type
- **423**: Locked
- **428**: Precondition Required
- **429**: Too Many Requests
- **500**: Internal Server Error
- **502**: Bad Gateway
- **503**: Service Unavailable
- **504**: Gateway Timeout

**Autenticación:** bearer-key

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
