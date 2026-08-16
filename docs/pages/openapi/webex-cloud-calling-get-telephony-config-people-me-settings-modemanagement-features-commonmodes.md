---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-modemanagement-features-commonmodes
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/modeManagement/features/commonModes
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.574706+00:00
---

# GET /telephony/config/people/me/settings/modeManagement/features/commonModes

**API:** Webex Cloud Calling
**Área:** Mode Management
**operationId:** `getCommonModes`

## Resumen
Get Common Modes

## Descripción
Retrieves a list of common operating mode names that are shared across multiple specified features. This API accepts a list of feature IDs and returns only the mode names that exist in all of the specified features, allowing managers to switch multiple features to the same mode simultaneously.

Common modes are useful when you need to coordinate operational changes across multiple features. For example, switching an entire office to "Holiday" mode across all Auto Attendants and Call Queues at once.

This API requires a user auth token with the `spark:telephony_config_read` scope. The authenticated user must be a mode manager for the specified features.

## Parámetros
- `featureIds` [query] (array) **(requerido)**: List of feature IDs (comma-separated) for auto attendants, call queues, or hunt groups

## Respuestas
- **200**: Common modes retrieved successfully
  - `commonModeNames` (array) **(requerido)**: Array of operating mode names
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
