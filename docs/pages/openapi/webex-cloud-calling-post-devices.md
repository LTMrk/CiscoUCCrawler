---
doc_id: webex-cloud-calling-post-devices
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /devices
operation_id: Create a Device by MAC Address
tags: Devices
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.006655+00:00
---

# POST /devices

**API:** Webex Cloud Calling
**Área:** Devices
**operationId:** `Create a Device by MAC Address`

## Resumen
Create a Device by MAC Address

## Descripción
Create a phone by its MAC address in a specific workspace or for a person.

Specify the `mac`, `model` and either `workspaceId` or `personId`.

* You can get the `model` from the [supported devices](/docs/api/v1/device-call-settings/read-the-list-of-supported-devices) API.

* Either `workspaceId` or `personId` should be provided. If both are supplied, the request will be invalid.

* The `password` field is only required for third party devices. You can obtain the required third party phone configuration from [here](/docs/api/v1/beta-device-call-settings-with-third-party-device-support/get-third-party-device).

<div><Callout type="warning">Adding a device to a person with a Webex Calling Standard license will disable Webex Calling across their Webex mobile, tablet, desktop, and browser applications.</Callout></div><br><div><Callout type="warning">When adding devices to a Webex Calling Professional licensed person or workspace, wait for each API call to finish before starting the next. This prevents race conditions that can cause errors when assigning primary versus secondary device status.</Callout></div>

## Parámetros
- `orgId` [query] (string): The organization associated with the device. If left empty, the organization associated with the caller will be used.

## Cuerpo de la petición (application/json)
- `mac` (string) (**requerido**): The MAC address of the device being created.
- `model` (string) (**requerido**): The model of the device being created. The corresponding device model display name sometimes called the product name, can also be used to specify the model.
- `workspaceId` (string): The ID of the workspace where the device will be created.
- `personId` (string): The ID of the person who will own the device once created.
- `password` (string): SIP password to be configured for the phone, only required with third party devices.

### Ejemplo — petición
```json
{
  "mac": "D82E3EEF4E5C",
  "model": "DMS Cisco 8865",
  "workspaceId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS83MTZlOWQxYy1jYTQ0LTRmZWQtOGZjYS05ZGY0YjRmNDE3ZjU"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/devices' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"mac": "<mac>", "model": "<model>"}'
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
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs