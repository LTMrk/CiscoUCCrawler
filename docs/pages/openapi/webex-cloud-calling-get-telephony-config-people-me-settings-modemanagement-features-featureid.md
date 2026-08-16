---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-modemanagement-features-featureid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/modeManagement/features/{featureId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.574918+00:00
---

# GET /telephony/config/people/me/settings/modeManagement/features/{featureId}

**API:** Webex Cloud Calling
**Área:** Mode Management
**operationId:** `getModeManagementFeature`

## Resumen
Get Mode Management Feature

## Descripción
Retrieves detailed information about a specific mode management feature including its current operating mode and exception status. This API provides the feature's ID, name, type, current operating mode ID, and whether it is currently in an exception mode.

Exception mode indicates that the feature has been manually switched to a different mode than what its schedule dictates. This information is critical for mode managers to understand the current state of their features.

This API requires a user auth token with the `spark:telephony_config_read` scope. The authenticated user must be a mode manager for the specified feature.

## Parámetros
- `featureId` [path] (string) **(requerido)**: Unique identifier for the feature.

## Respuestas
- **200**: Mode management feature retrieved successfully
  - `modeBasedForwardingEnabled` (boolean) **(requerido)**: Whether mode based forwarding is enabled for the feature
  - `timezone` (string) **(requerido)**: Timezone for the feature
  - `phoneNumber` (string): Phone number of the feature
  - `extension` (string): Extension of the feature
  - `currentOperatingModeId` (string) **(requerido)**: Unique identifier for the current operating mode.
  - `currentOperatingModeEndTime` (string): The current operating mode's end time in 12-hour format showing hour and minute only (no date information). This field's presence and meaning depends on the operational state:  * Present during normal operation with the time at which the next mode change will occur.  * Not present for Manual Switch Back exceptions.  * For Automatic Switch Back (Early Start) exceptions it is when the exception ends and the feature automatically reverts to normal operation which is the mode's configured start time.  * For Automatic Switch Back (Extension) exceptions it is when the exception ends and the feature automatically reverts to normal operation which is the mode's configured end time when the exception started plus the extension time.  * For Automatic Switch Back (Standard) exceptions it is when the exception ends and the feature automatically reverts to normal operation which is the mode's configured end time.
  - `currentOperatingModeForwardDestination` (string): Forward destination for current operating mode
  - `exceptionType` (string): Type of exception indicating how the feature will switch back from the current mode. This field is not present when the feature is in normal operation.   * `AUTOMATIC_SWITCH_BACK_EARLY_START` - Automatic switchback with early start.  * `AUTOMATIC_SWITCH_BACK_EXTENSION` - Automatic switchback with extension.  * `MANUAL_SWITCH_BACK` - Manual switchback required.  * `AUTOMATIC_SWITCH_BACK_STANDARD` - Standard automatic switchback. Valores: AUTOMATIC_SWITCH_BACK_EARLY_START, AUTOMATIC_SWITCH_BACK_EXTENSION, MANUAL_SWITCH_BACK, AUTOMATIC_SWITCH_BACK_STANDARD.
  - `modes` (array) **(requerido)**: Array of operating modes configured for this feature
    - `id` (string) **(requerido)**: Unique identifier for the operating mode.
    - `name` (string) **(requerido)**: Display name of the operating mode.
    - `type` (string): * `NONE` - No schedule defined.  * `SAME_HOURS_DAILY` - Same hours for weekdays and weekends.  * `DIFFERENT_HOURS_DAILY` - Different hours for each day.  * `HOLIDAY` - Holiday-based schedule. Valores: NONE, SAME_HOURS_DAILY, DIFFERENT_HOURS_DAILY, HOLIDAY.
    - `level` (string): * `ORGANIZATION` - Organization level mode.  * `LOCATION` - Location level mode. Valores: ORGANIZATION, LOCATION.
    - `normalOperationEnabled` (boolean) **(requerido)**: Whether this mode is enabled for normal operation.
    - `forwardTo` (object): Forwarding configuration for this mode
      - `selection` (string): * `DO_NOT_FORWARD` - Do not forward calls.  * `FORWARD_TO_SPECIFIED_NUMBER` - Forward to a specified number.  * `FORWARD_TO_DEFAULT_NUMBER` - Use the mode's default forwarding setting (which may be to forward or not forward). Valores: DO_NOT_FORWARD, FORWARD_TO_SPECIFIED_NUMBER, FORWARD_TO_DEFAULT_NUMBER.
      - `phoneNumber` (string): Phone number to forward to when selection is FORWARD_TO_SPECIFIED_NUMBER.
      - `sendToVoicemailEnabled` (boolean) **(requerido)**: Whether to send to voicemail when selection is FORWARD_TO_SPECIFIED_NUMBER.
      - `defaultPhoneNumber` (string): Default phone number when selection is FORWARD_TO_DEFAULT_NUMBER. This field is not present if the mode's default is to not forward.
      - `defaultSendToVoicemailEnabled` (boolean) **(requerido)**: Whether default is to send to voicemail
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
