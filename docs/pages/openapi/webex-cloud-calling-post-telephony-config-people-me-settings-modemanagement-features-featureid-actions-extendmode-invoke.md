---
doc_id: webex-cloud-calling-post-telephony-config-people-me-settings-modemanagement-features-featureid-actions-extendmode-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/config/people/me/settings/modeManagement/features/{featureId}/actions/extendMode/invoke
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.575488+00:00
---

# POST /telephony/config/people/me/settings/modeManagement/features/{featureId}/actions/extendMode/invoke

**API:** Webex Cloud Calling
**Área:** Mode Management
**operationId:** `extendMode`

## Resumen
Extend Current Operating Mode Duration

## Descripción
Extends the duration of the current operating mode by adding additional time before it expires or reverts to scheduled operation. This API allows managers to prolong a temporary mode change without having to switch modes again.

Extension time can be specified in 30-minute increments up to 720 minutes (12 hours). If no extension time is provided, the mode is extended with a manual switchback exception, meaning it will remain active until manually changed.

This API requires a user auth token with the `spark:telephony_config_write` scope. The authenticated user must be a mode manager for the specified feature.

## Parámetros
- `featureId` [path] (string) **(requerido)**: Unique identifier for the feature.

## Cuerpo de la petición (application/json)
- `operatingModeId` (string) **(requerido)**: Unique identifier for the operating mode for which the extension is being configured.
- `extensionTime` (integer): Extension time in minutes (must be multiple of 30). If not sent, mode is extended with manual switch back exception

## Respuestas
- **204**: Mode extended successfully
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
