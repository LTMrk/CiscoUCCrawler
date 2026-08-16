---
doc_id: webex-device-put-telephony-config-devices-deviceid-members
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
method: PUT
path: /telephony/config/devices/{deviceId}/members
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.124797+00:00
---

# PUT /telephony/config/devices/{deviceId}/members

**API:** Webex Device
**Área:** Device Call Settings
**operationId:** `updateMembersOnDevice`

## Resumen
Update Members on the device

## Descripción
Modify member details on the device.

A device member can be either a person, virtual line or a workspace. An admin can access the list of member details, modify member details and
search for available members on a device.

Modifying members on the device requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `deviceId` [path] (string) **(requerido)**: Unique identifier for the device.
- `orgId` [query] (string): Modify members on the device in this organization.

## Cuerpo de la petición (application/json)
- `members` (array): This specifies the new list of device members, completely replacing the existing device members. If the member's list is omitted then all the users are removed except the primary user.
  - `port` (number) **(requerido)**: Person's assigned port number.
  - `id` (string) **(requerido)**: Unique identifier for the member.
  - `t38FaxCompressionEnabled` (boolean): T.38 Fax Compression setting and is available only for ATA Devices. Choose T.38 fax compression if the device requires this option. This will override user level compression options.
  - `primaryOwner` (boolean) **(requerido)**: Whether the user is the owner of the device or not, and points to a primary Line/Port of device.
  - `lineType` (string) **(requerido)**: * `PRIMARY` - Primary line for the member.  * `SHARED_CALL_APPEARANCE` - Shared line for the member. A shared line allows users to receive and place calls to and from another user's extension, using their own device. Valores: PRIMARY, SHARED_CALL_APPEARANCE.
  - `lineWeight` (number) **(requerido)**: Number of lines that have been configured for the person on the device.
  - `hotlineEnabled` (boolean) **(requerido)**: Enable Hotline. Configure this line to automatically call a predefined number whenever taken off-hook. Once enabled, the line can only make calls to the predefined number set in hotlineDestination.
  - `hotlineDestination` (string) **(requerido)**: The preconfigured number for Hotline. Required only if `hotlineEnabled` is set to true.
  - `allowCallDeclineEnabled` (boolean) **(requerido)**: Set how a person's device behaves when a call is declined. When set to true, a call decline request is extended to all the endpoints on the device. When set to false, a call decline request only declines the current endpoint.
  - `lineLabel` (string): Device line label.

### Ejemplo de petición
```json
{
  "members": [
    {
      "port": 1,
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jODhiZGIwNC1jZjU5LTRjMjMtODQ4OC00NTNhOTE3ZDFlMjk",
      "t38FaxCompressionEnabled": false,
      "primaryOwner": true,
      "lineType": "SHARED_CALL_APPEARANCE",
      "lineWeight": 1,
      "allowCallDeclineEnabled": true,
      "hotlineDestination": "",
      "hotlineEnabled": false,
      "lineLabel": "share line label"
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
