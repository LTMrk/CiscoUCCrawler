---
doc_id: webex-cloud-calling-post-telephony-config-people-me-settings-modemanagement-features-featureid-actions-switchmode-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/config/people/me/settings/modeManagement/features/{featureId}/actions/switchMode/invoke
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.575390+00:00
---

# POST /telephony/config/people/me/settings/modeManagement/features/{featureId}/actions/switchMode/invoke

**API:** Webex Cloud Calling
**Área:** Mode Management
**operationId:** `switchModeForFeature`

## Resumen
Switch Mode for Single Feature

## Descripción
Switches the operating mode for a single feature to a specified mode, either temporarily or with manual switchback. This API creates an exception to the feature's normal scheduled operation, allowing managers to manually control the feature's behavior.

You can configure whether the mode switch is temporary (automatically reverts based on schedule) or requires manual switchback. This is useful for handling unexpected situations like emergency closures, special events, or unscheduled breaks.

This API requires a user auth token with the `spark:telephony_config_write` scope. The authenticated user must be a mode manager for the specified feature.

## Parámetros
- `featureId` [path] (string) **(requerido)**: Unique identifier for the feature.

## Cuerpo de la petición (application/json)
- `operatingModeId` (string) **(requerido)**: Operating mode ID to switch to
- `isManualSwitchbackEnabled` (boolean): Determines if switch back will be manual (if true) or automatic (if false or omitted from request)

## Respuestas
- **204**: Mode switched successfully
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
