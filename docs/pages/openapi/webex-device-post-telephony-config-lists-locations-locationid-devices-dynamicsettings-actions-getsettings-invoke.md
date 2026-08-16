---
doc_id: webex-device-post-telephony-config-lists-locations-locationid-devices-dynamicsettings-actions-getsettings-invoke
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
method: POST
path: /telephony/config/lists/locations/{locationId}/devices/dynamicSettings/actions/getSettings/invoke
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.132388+00:00
---

# POST /telephony/config/lists/locations/{locationId}/devices/dynamicSettings/actions/getSettings/invoke

**API:** Webex Device
**Área:** Device Call Settings With Device Dynamic Settings
**operationId:** `getLocationDeviceDynamicSettings`

## Resumen
Get Location Device Dynamic Settings

## Descripción
Retrieve dynamic settings for specific device tags at the specified location level, allowing filters by `familyOrModelDisplayName` and `tag` identifier.

This API lets you request the values of multiple `Device Settings` at once by specifying a list of `familyOrModelDisplayName` and tag combinations for a specific location.

This requires a full, device, or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Unique identifier for the `location`.
- `orgId` [query] (string): Unique identifier for the `organization` to which this location belongs.
- `familyOrModelDisplayName` [query] (string) **(requerido)**: The family or model name for the device. If no tag is specified, all tags related to `familyOrModelDisplayName` are returned.

## Cuerpo de la petición (application/json)
- `tags` (array): Optional array of device tag identifiers to request settings for. Each identifier must have a length between 1 and 64 characters.

### Ejemplo de petición
```json
{
  "tags": [
    "%G711U_ORDER%",
    "%ENABLE_BLUETOOTH%",
    "%DO_UI_MENU_BACKGROUND%"
  ]
}
```

## Respuestas
- **200**: OK.
  - `tags` (array): Array of device setting values matching the requested tags.
    - `familyOrModelDisplayName` (string): The `familyOrModelDisplayName` of the device.
    - `tag` (string): The unique identifier for the setting.
    - `value` (string): The current value of the setting at `LOCATION` level. If the tag value is not set at the `LOCATION` level, this field will not be included in the response.
    - `parentValue` (string): The value inherited from the immediate parent level above `LOCATION`. It can be `SYSTEM_DEFAULT`, `REGIONAL_DEFAULT`, `ORGANIZATION`, or `LOCATION`, depending on which level the setting is actually configured at. If there is no parent level for this tag, this field will not be included in the response.
    - `parentLevel` (string): The level from which the tag's parent value is inherited. If there is no parent level for this tag, this field will not be included in the response. Valores: SYSTEM_DEFAULT, REGIONAL_DEFAULT, ORGANIZATION, LOCATION.
  - `lastUpdateTime` (integer): Timestamp of the last update to these settings.
  - `updateInProgress` (boolean): Flag indicating if an update to these settings is currently in progress.
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **410**: Gone: The requested resource is no longer available.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **423**: Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **428**: Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
