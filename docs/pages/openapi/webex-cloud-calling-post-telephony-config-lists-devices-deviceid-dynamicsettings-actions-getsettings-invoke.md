---
doc_id: webex-cloud-calling-post-telephony-config-lists-devices-deviceid-dynamicsettings-actions-getsettings-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/config/lists/devices/{deviceId}/dynamicSettings/actions/getSettings/invoke
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.588941+00:00
---

# POST /telephony/config/lists/devices/{deviceId}/dynamicSettings/actions/getSettings/invoke

**API:** Webex Cloud Calling
**Área:** Device Call Settings With Device Dynamic Settings
**operationId:** `getDeviceDynamicSettings`

## Resumen
Get Device Dynamic Settings

## Descripción
Retrieve settings for a specified device.

This API retrieves device settings based on the specified `tags`; if the `tags` field is empty or missing, all settings for the device are returned.

This requires a full, device, or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `deviceId` [path] (string) **(requerido)**: Device for which to retrieve settings.
- `orgId` [query] (string): Organization to which the `device` belongs.

## Cuerpo de la petición (application/json)
- `tags` (array): Optional array of tag identifiers representing specific settings to fetch. If omitted or provided as an empty array, all settings for the device will be returned.

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
- **200**: OK
  - `tags` (array) **(requerido)**: Array of device setting values matching the requested tags.
    - `familyOrModelDisplayName` (string) **(requerido)**: The display name of the device family or model associated with the returned tag.
    - `tag` (string) **(requerido)**: The unique identifier for the device setting.
    - `value` (string): The current value of the setting at device level. If the tag value is not set at the device level, this field will not be included in the response.
    - `parentValue` (string): The setting value at the next available `parentLevel`. It is used if `value` is not set and is omitted when no parent level exists for the tag.
    - `parentLevel` (string): The level from which the tag's parent value is inherited. If there is no parent level for this tag, this field will not be included in the response. Valores: SYSTEM_DEFAULT, REGIONAL_DEFAULT, ORGANIZATION, LOCATION.
  - `lastUpdateTime` (integer): Timestamp of the last update to these settings.
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
