---
doc_id: webex-cloud-calling-get-devices
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /devices
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.589891+00:00
---

# GET /devices

**API:** Webex Cloud Calling
**Área:** Devices
**operationId:** `List Devices`

## Resumen
List Devices

## Descripción
Lists all active Webex devices associated with the authenticated user, such as devices activated in personal mode. This requires the `spark:devices_read` scope. Administrators can list all devices within their organization. This requires an administrator auth token with the `spark-admin:devices_read` scope.

## Parámetros
- `max` [query] (number): Limit the maximum number of devices in the response.
- `start` [query] (number): Offset. Default is 0.
- `displayName` [query] (string): List devices with this display name.
- `personId` [query] (string): List devices by person ID.
- `workspaceId` [query] (string): List devices by workspace ID.
- `orgId` [query] (string): List devices in this organization. Only admin users of another organization (such as partners) may use this parameter.
- `connectionStatus` [query] (string): List devices with this connection status.
- `product` [query] (string): List devices with this product name.
- `type` [query] (string): List devices with this type.
- `serial` [query] (string): List devices with this serial number.
- `tag` [query] (string): List devices which have a tag. Searching for multiple tags (logical AND) can be done by comma separating the `tag` values or adding several `tag` parameters.
- `software` [query] (string): List devices with this software version.
- `upgradeChannel` [query] (string): List devices with this upgrade channel.
- `errorCode` [query] (string): List devices with this error code.
- `capability` [query] (string): List devices with this capability.
- `permission` [query] (string): List devices with this permission.
- `locationId` [query] (string): List devices by location ID.
- `workspaceLocationId` [query] (string): List devices by workspace location ID. Deprecated, prefer `locationId`.
- `mac` [query] (string): List devices with this MAC address.
- `devicePlatform` [query] (string): List devices with this device platform.
- `plannedMaintenance` [query] (string): List devices with this planned maintenance.

## Respuestas
- **200**: OK
  - `items` (array):
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
    - `created` (string) **(requerido)**: The date and time that the device was registered, in ISO8601 format.
    - `locationId` (string): The location associated with the device.
    - `workspaceLocationId` (string): The workspace location associated with the device. Deprecated, prefer `locationId`.
    - `errorCodes` (array): Error codes coming from the device.
    - `firstSeen` (string): Timestamp of the first time device sent a status post.
    - `lastSeen` (string): Timestamp of the last time device sent a status post.
    - `managedBy` (string): Entity managing the device configuration. Valores: CISCO, CUSTOMER, PARTNER.
    - `devicePlatform` (string): Device platform Valores: cisco, microsoftTeamsRoom.
    - `plannedMaintenance` (object): The planned maintenance for the device.
      - `mode` (string): The planned maintenance mode for the device Valores: off, on, upcoming.
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
