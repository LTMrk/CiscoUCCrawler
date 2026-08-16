---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-modemanagement-features-featureid-normaloperationmode
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/modeManagement/features/{featureId}/normalOperationMode
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.575019+00:00
---

# GET /telephony/config/people/me/settings/modeManagement/features/{featureId}/normalOperationMode

**API:** Webex Cloud Calling
**Área:** Mode Management
**operationId:** `getNormalOperationMode`

## Resumen
Get Normal Operation Mode

## Descripción
Retrieves the current normal operating mode that the feature is scheduled to be in based on its time schedules. This represents the mode the feature would be in if no manual exceptions or overrides were active.

The normal operation mode is determined by the feature's configured schedules and may differ from the actual current operating mode if a manual exception has been applied. This API helps managers understand what the scheduled behavior is versus the actual current state.

This API requires a user auth token with the `spark:telephony_config_read` scope. The authenticated user must be a mode manager for the specified feature.

## Parámetros
- `featureId` [path] (string) **(requerido)**: Unique identifier for the feature.

## Respuestas
- **200**: Normal operation mode retrieved successfully
  - `operatingModeId` (string) **(requerido)**: Unique identifier for the scheduled operating mode.
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
