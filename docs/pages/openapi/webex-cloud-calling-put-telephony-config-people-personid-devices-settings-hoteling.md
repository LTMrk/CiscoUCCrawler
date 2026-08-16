---
doc_id: webex-cloud-calling-put-telephony-config-people-personid-devices-settings-hoteling
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/people/{personId}/devices/settings/hoteling
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.583406+00:00
---

# PUT /telephony/config/people/{personId}/devices/settings/hoteling

**API:** Webex Cloud Calling
**Área:** Device Call Settings
**operationId:** `modefyHotelingSettingsForPersonsPrimaryDevices`

## Resumen
Modify Hoteling Settings for a Person's Primary Devices

## Descripción
Modify hoteling login configuration on a person's Webex Calling Devices which are in effect when the device is the user's primary device and device type is PRIMARY. To view the current hoteling login settings, see the `hoteling` field in [Get Person Devices](/docs/api/v1/device-call-settings/get-person-devices).

Modifying devices for a person requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `personId` [path] (string) **(requerido)**: ID of the person associated with the device.
- `orgId` [query] (string): Organization to which the person belongs.

## Cuerpo de la petición (application/json)
- `hoteling` (object) **(requerido)**:
  - `enabled` (boolean) **(requerido)**: Enable/Disable hoteling Host. Enabling the device for hoteling means that a guest(end user) can log into this host(workspace device) and use this device  as if it were their own. This is useful when traveling to a remote office but still needing to place/receive calls with their telephone number and access features normally available to them on their office phone.
  - `limitGuestUse` (boolean): Enable limiting the time a guest can use the device. The time limit is configured via `guestHoursLimit`.
  - `guestHoursLimit` (number): Time Limit in hours until hoteling is enabled. Mandatory if `limitGuestUse` is enabled.

### Ejemplo de petición
```json
{
  "hoteling": {
    "enabled": true,
    "limitGuestUse": true,
    "guestHoursLimit": 5
  }
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
