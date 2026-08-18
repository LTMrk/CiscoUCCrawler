---
doc_id: webex-device-patch-devices-deviceid
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
api_version: 1.0.0
method: PATCH
path: /devices/{deviceId}
operation_id: Modify Device Tags
tags: Devices
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.206990+00:00
---

# PATCH /devices/{deviceId}

**API:** Webex Device
**Área:** Devices
**operationId:** `Modify Device Tags`

## Resumen
Modify Device Tags

## Descripción
Create, delete or update tags on a device. For your own device, this requires an auth token with the `spark:devices_write` scope. An auth token with the `spark-admin:devices_write` scope is required to operate on other devices within the organization.

Specify the device ID in the `deviceId` parameter in the URI.

Include only the tag array in the request body, no other device attributes can be changed. This action will overwrite any previous tags. A common approach is to first [GET the devices's details](/docs/api/v1/devices/get-device-details), make changes to the `tags` array, and then PATCH the new complete array with this endpoint.

## Parámetros
- `deviceId` [path] (string) (**requerido**): Unique identifier for the device.
- `orgId` [query] (string): The organization associated with the device. If left empty, the organization associated with the caller will be used.

## Cuerpo de la petición (application/json-patch+json)
- `op` (string): * `add` - Add all specified tags to the existing device tags list.  * `remove` - Remove all tags that the device currently has.  * `replace` - Replace the tags currently on the device with the specified list. Valores: add, remove, replace.
- `path` (string): Only the tags path is supported to patch.
- `value` (array):

### Ejemplo — petición
```json
[
  {
    "op": "replace",
    "path": "tags",
    "value": [
      "First Tag",
      "Second Tag"
    ]
  }
]
```

## Ejemplo de invocación
```bash
curl -X PATCH '/devices/<deviceId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- `id` (string): A unique identifier for the device.
- `displayName` (string): A friendly name for the device.
- `placeId` (string): The `placeId` field has been deprecated. Please use `workspaceId` instead.
- `workspaceId` (string): The workspace associated with the device.
- `personId` (string): The person associated with the device.
- `orgId` (string): The organization associated with the device.
- `capabilities` (array): The capabilities of the device.
- `permissions` (array): The permissions the user has for this device. For example, `xapi` means this user is entitled to using the `xapi` against this device.
- `connectionStatus` (string): The connection status of the device. Valores: connected, disconnected, connected_with_issues, offline_expired, activating, pending, unknown, offline_deep_sleep.
- `product` (string): The product name. A display friendly version of the device's `model`.
- `type` (string): The product type.
- `tags` (array): Tags assigned to the device.
- `ip` (string): The current IP address of the device.
- `activeInterface` (string): The current network connectivity for the device. Valores: wired.
- `mac` (string): The unique address for the network adapter.
- `primarySipUrl` (string): The primary SIP address to dial this device.
- `sipUrls` (array): All SIP addresses to dial this device.
- `serial` (string): Serial number for the device.
- `software` (string): The operating system name data and version tag.
- `upgradeChannel` (string): The upgrade channel the device is assigned to.
- `created` (string) (**requerido**): The date and time that the device was registered, in ISO8601 format.
- `locationId` (string): The location associated with the device.
- `workspaceLocationId` (string): The workspace location associated with the device. Deprecated, prefer `locationId`.
- `errorCodes` (array): Error codes coming from the device.
- `firstSeen` (string): Timestamp of the first time device sent a status post.
- `lastSeen` (string): Timestamp of the last time device sent a status post.
- `managedBy` (string): Entity managing the device configuration. Valores: CISCO, CUSTOMER, PARTNER.
- `devicePlatform` (string): Device platform Valores: cisco, microsoftTeamsRoom.
- `plannedMaintenance` (object): The planned maintenance for the device.
  - `mode` (string): The planned maintenance mode for the device Valores: off, on, upcoming.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMV9pbnQxMy9ERVZJQ0UvNTEwMUIwN0ItNEY4Ri00RUY3LUI1NjUtREIxOUM3QjcyM0Y3",
  "callingDeviceId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMV9pbnQxMy9DQUxMSU5HX0RFVklDRS81MTAxQjA3Qi00RjhGLTRFRjctQjU2NS1EQjE5QzdCNzIzRjc=",
  "webexDeviceId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMV9pbnQxMy9ERVZJQ0UvNTEwMUIwN0ItNEY4Ri00RUY3LUI1NjUtREIxOUM3QjcyM0Y3",
  "deviceId": "Y2lzY29zcGFyazovL29yZ0lkPTk2YWJjMmFhLTNkY2MtMTFlNS1hMTUyLWZlMzQ4MTljZGM5YS9ERVZJQ0VfSUQvNTEwMWIwN2ItNGY4Zi00ZWY3LWI1NjUtZGIxOWM3YjcyM2Y3",
  "displayName": "SFO12-3-PanHandle",
  "placeId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS83MTZlOWQxYy1jYTQ0LTRmZWQtOGZjYS05ZGY0YjRmNDE3ZjU",
  "workspaceId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS83MTZlOWQxYy1jYTQ0LTRmZWQtOGZjYS05ZGY0YjRmNDE3ZjU",
  "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS83MTZlOWQxYy1jYTQ0LTRmZWQtOGZjYS05ZGY0YjRmNDE3ZjU",
  "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
  "capabilities": [
    "xapi"
  ],
  "permissions": [
    "xapi:readonly"
  ],
  "connectionStatus": "connected",
  "product": "Cisco Webex DX80",
  "type": "roomdesk",
  "tags": [
    "First Tag",
    "Second Tag"
  ],
  "ip": "100.110.120.130",
  "activeInterface": "wired",
  "mac": "11:22:33:44:AA:FF",
  "primarySipUrl": "sample_device@sample_workspacename.orgname.org",
  "sipUrls": [
    "sample_device@sample_workspacename.orgname.org",
    "another_device@sample_workspacename.orgname.org"
  ],
  "serial"
  ... (truncado)
```

## Respuestas de error
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

## Contexto de la API
The Webex Device APIs provide endpoints for managing and monitoring Webex devices, including registration, configuration, status retrieval, workspace assignment, and firmware management. These APIs support automation of device onboarding, health monitoring, remote troubleshooting, and bulk configuration updates. Integration scenarios include custom device dashboards, proactive alerting, and seamless workspace management for meeting rooms and shared spaces. The APIs are essential for IT teams managing large fleets of Webex devices across distributed environments.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs