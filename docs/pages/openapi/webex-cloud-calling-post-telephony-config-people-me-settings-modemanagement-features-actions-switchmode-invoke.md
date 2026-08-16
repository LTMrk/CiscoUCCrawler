---
doc_id: webex-cloud-calling-post-telephony-config-people-me-settings-modemanagement-features-actions-switchmode-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/config/people/me/settings/modeManagement/features/actions/switchMode/invoke
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.574801+00:00
---

# POST /telephony/config/people/me/settings/modeManagement/features/actions/switchMode/invoke

**API:** Webex Cloud Calling
**Área:** Mode Management
**operationId:** `switchModeMultipleFeatures`

## Resumen
Switch Mode for Multiple Features

## Descripción
Switches the operating mode for multiple features simultaneously by specifying a common mode name. This API accepts a list of feature IDs and sets all of them to the specified operating mode, provided that mode exists for all features.

This bulk operation is particularly useful for coordinating operational changes across an organization, such as activating holiday modes, emergency procedures, or after-hours configurations across multiple Auto Attendants, Call Queues, and Hunt Groups at once.

This API requires a user auth token with the `spark:telephony_config_write` scope. The authenticated user must be a mode manager for all specified features.

## Cuerpo de la petición (application/json)
- `featureIds` (array) **(requerido)**: List of feature IDs to switch mode
- `operatingModeName` (string) **(requerido)**: Name of the common operating mode to be set as current operating mode

## Respuestas
- **204**: Mode switched successfully for multiple features
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
