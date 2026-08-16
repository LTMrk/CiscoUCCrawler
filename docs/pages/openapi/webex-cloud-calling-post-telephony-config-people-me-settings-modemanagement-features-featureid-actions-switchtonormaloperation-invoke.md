---
doc_id: webex-cloud-calling-post-telephony-config-people-me-settings-modemanagement-features-featureid-actions-switchtonormaloperation-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/config/people/me/settings/modeManagement/features/{featureId}/actions/switchToNormalOperation/invoke
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.575275+00:00
---

# POST /telephony/config/people/me/settings/modeManagement/features/{featureId}/actions/switchToNormalOperation/invoke

**API:** Webex Cloud Calling
**Área:** Mode Management
**operationId:** `switchToNormalOperation`

## Resumen
Switch to Normal Operation

## Descripción
Switches the feature back to its normal scheduled operation mode, removing any manual exceptions or overrides that may be active. This returns the feature to operating according to its configured time schedules.

This operation is useful when a temporary manual mode change (exception) is no longer needed and you want to restore automatic schedule-based operation. It effectively cancels any active manual mode switches.

This API requires a user auth token with the `spark:telephony_config_write` scope. The authenticated user must be a mode manager for the specified feature.

## Parámetros
- `featureId` [path] (string) **(requerido)**: Unique identifier for the feature.

## Respuestas
- **204**: Switched to normal operation successfully
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
