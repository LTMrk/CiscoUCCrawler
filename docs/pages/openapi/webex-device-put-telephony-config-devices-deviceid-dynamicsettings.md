---
doc_id: webex-device-put-telephony-config-devices-deviceid-dynamicsettings
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
method: PUT
path: /telephony/config/devices/{deviceId}/dynamicSettings
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.132713+00:00
---

# PUT /telephony/config/devices/{deviceId}/dynamicSettings

**API:** Webex Device
**Área:** Device Call Settings With Device Dynamic Settings
**operationId:** `updateSpecifiedSettingsForTheDevice`

## Resumen
Update Device Dynamic Settings

## Descripción
Modify dynamic settings for a specified device.

This API updates device settings based on the specified `tags`. If the `tags` field is empty, the request has no effect.

This requires a full, device, or read-only administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `deviceId` [path] (string) **(requerido)**: Device for which to update settings.
- `orgId` [query] (string): Organization to which the device belongs.

## Cuerpo de la petición (application/json)
- `tags` (array): Optional array of `tag` identifiers representing specific settings to update. If omitted or provided as an empty array, the request will have no effect.
  - `tag` (string) **(requerido)**: The unique identifier for the setting to be updated.
  - `action` (string) **(requerido)**: The action to perform on the setting. When action is `SET`, `tag` is updated to specified value. When action is `CLEAR`, the `tag` value at device level is removed, and the device will inherit the value from the parent level, if it exists. Valores: SET, CLEAR.
  - `value` (string): The new value to set for the setting. This field is required when `action` is `SET` and ignored otherwise.

### Ejemplo de petición
```json
{
  "tags": [
    {
      "action": "CLEAR",
      "tag": "%G711A_ORDER%"
    },
    {
      "action": "SET",
      "tag": "%ENABLE_BLUETOOTH%",
      "value": "0"
    }
  ]
}
```

## Respuestas
- **204**: No Content
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
