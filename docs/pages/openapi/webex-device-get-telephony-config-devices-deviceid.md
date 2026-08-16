---
doc_id: webex-device-get-telephony-config-devices-deviceid
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
method: GET
path: /telephony/config/devices/{deviceId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.126561+00:00
---

# GET /telephony/config/devices/{deviceId}

**API:** Webex Device
**Área:** Device Call Settings
**operationId:** `getWebexCallingDeviceDetails`

## Resumen
Get Webex Calling Device Details

## Descripción
<div><Callout type="warning">Not supported for Webex for Government (FedRAMP)</Callout></div>

Retrieves Webex Calling device details that include information needed for third-party device management.

Webex calling devices are associated with a specific user Workspace or Virtual Line. Webex Calling devices share the location with the entity that owns them.

Person or workspace to which the device is assigned. Its fields point to a primary line/port of the device.

Requires a full, location, user, or read-only admin auth token with the scope of `spark-admin:telephony_config_read`.

## Parámetros
- `deviceId` [path] (string) **(requerido)**: Unique identifier for the device.
- `orgId` [query] (string): ID of the organization in which the device resides.

## Respuestas
- **200**: OK
  - `manufacturer` (string) **(requerido)**: Manufacturer of the device.
  - `managedBy` (string) **(requerido)**: Device manager(s).
  - `id` (string) **(requerido)**: A unique identifier for the device.
  - `ip` (string) **(requerido)**: The current IP address of the device.
  - `mac` (string): The unique address for the network adapter.
  - `model` (string) **(requerido)**: A model type of the device.
  - `activationState` (string): * `activating` - Device is activating using an activation code.  * `activated` - Device has been activated using an activation code.  * `deactivated` - Device has not been activated using an activation code. Valores: activating, activated, deactivated.
  - `description` (array): Comma-separated array of tags used to describe the device.
  - `upgradeChannelEnabled` (boolean) **(requerido)**: Enabled / disabled status of the upgrade channel.
  - `owner` (object):
    - `sipUserName` (string) **(requerido)**: SIP authentication user name for the owner of the device.
    - `linePort` (string): Identifies a device endpoint in standalone mode or a SIP URI public identity in IMS mode.
  - `proxy` (object):
    - `outboundProxy` (string): Outgoing server which the phone should use for all SIP requests. Not set if the response has no body.
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
