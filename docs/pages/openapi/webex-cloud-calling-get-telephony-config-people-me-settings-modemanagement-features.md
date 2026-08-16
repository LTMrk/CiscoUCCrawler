---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-modemanagement-features
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/modeManagement/features
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.574604+00:00
---

# GET /telephony/config/people/me/settings/modeManagement/features

**API:** Webex Cloud Calling
**Área:** Mode Management
**operationId:** `getModeManagementFeatures`

## Resumen
Get Mode Management Features

## Descripción
Retrieves a list of all mode management features (Auto Attendants, Call Queues, and Hunt Groups) for which the authenticated user has been designated as a mode manager. This API returns basic information about each feature including its ID, name, and type.

Mode Management allows designated managers to switch features between different operational configurations based on time schedules or manual triggers. This is useful for managing business hours, holidays, and emergency scenarios.

This API requires a user auth token with the `spark:telephony_config_read` scope. The authenticated user must be configured as a mode manager for at least one feature to receive results.

## Respuestas
- **200**: Mode management features retrieved successfully
  - `features` (array) **(requerido)**: List of mode management features. Returns all items in a single response.
    - `id` (string) **(requerido)**: Unique identifier for the auto attendant, call queue, or hunt group.
    - `name` (string) **(requerido)**: Display name of the auto attendant, call queue, or hunt group.
    - `type` (string) **(requerido)**: * `AUTO_ATTENDANT` - Auto Attendant feature.  * `CALL_QUEUE` - Call Queue feature (includes customer assist queues).  * `HUNT_GROUP` - Hunt Group feature. Valores: AUTO_ATTENDANT, CALL_QUEUE, HUNT_GROUP.
    - `phoneNumber` (string): Phone number of the feature
    - `extension` (string): Extension of the feature
    - `modeBasedForwardingEnabled` (boolean) **(requerido)**: Whether mode based forwarding is enabled for the feature
    - `location` (object): Location information for the feature
      - `id` (string) **(requerido)**: Unique identifier for the location.
      - `name` (string) **(requerido)**: Display name of the location.
    - `forwardDestination` (string): Current forward destination
    - `currentOperatingModeName` (string): Name of the current operating mode
    - `currentOperatingModeId` (string): ID of the current operating mode
    - `exceptionType` (string): Type of exception indicating how the feature will switch back from the current mode. This field is not present when the feature is in normal operation.   * `AUTOMATIC_SWITCH_BACK_EARLY_START` - Automatic switchback with early start.  * `AUTOMATIC_SWITCH_BACK_EXTENSION` - Automatic switchback with extension.  * `MANUAL_SWITCH_BACK` - Manual switchback required.  * `AUTOMATIC_SWITCH_BACK_STANDARD` - Standard automatic switchback. Valores: AUTOMATIC_SWITCH_BACK_EARLY_START, AUTOMATIC_SWITCH_BACK_EXTENSION, MANUAL_SWITCH_BACK, AUTOMATIC_SWITCH_BACK_STANDARD.
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
