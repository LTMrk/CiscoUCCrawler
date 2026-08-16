---
doc_id: webex-device-get-telephony-config-devices-deviceid-members
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
method: GET
path: /telephony/config/devices/{deviceId}/members
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.124523+00:00
---

# GET /telephony/config/devices/{deviceId}/members

**API:** Webex Device
**Área:** Device Call Settings
**operationId:** `getDeviceMembers`

## Resumen
Get Device Members

## Descripción
Get the list of all the members of the device including primary and secondary users.

A device member can be either a person or a workspace. An admin can access the list of member details, modify member details and
search for available members on a device.

Retrieving this list requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `deviceId` [path] (string) **(requerido)**: Unique identifier for the device.
- `orgId` [query] (string): Retrieves the list of all members of the device in this organization.

## Respuestas
- **200**: OK
  - `model` (string) **(requerido)**: Model type of the device.
  - `members` (array): List of members that appear on the device.
    - `id` (string) **(requerido)**: Unique identifier for the member.
    - `firstName` (string): First name of a person or workspace.
    - `lastName` (string): Last name of a person or workspace.
    - `phoneNumber` (string): Phone Number of a person or workspace. In some regions phone numbers are not returned in E.164 format. This will be supported in a future update.
    - `extension` (string): Extension of a person or workspace.
    - `routingPrefix` (string): Routing prefix of location.
    - `esn` (string): Routing prefix + extension of a person or workspace.
    - `primaryOwner` (boolean) **(requerido)**: This field indicates whether the person or the workspace is the owner of the device, and points to a primary Line/Port of the device.
    - `port` (number) **(requerido)**: Port number assigned to person or workspace.
    - `t38FaxCompressionEnabled` (boolean): T.38 Fax Compression setting and is available only for ATA Devices. Choose T.38 fax compression if the device requires this option. This will override user level compression options.
    - `lineType` (string) **(requerido)**: * `PRIMARY` - Primary line for the member.  * `SHARED_CALL_APPEARANCE` - Shared line for the member. A shared line allows users to receive and place calls to and from another user's extension, using their own device. Valores: PRIMARY, SHARED_CALL_APPEARANCE.
    - `lineWeight` (number) **(requerido)**: Number of lines that have been configured for the person on the device.
    - `hostIP` (string): Registration Host IP address for the line port.
    - `remoteIP` (string): Registration Remote IP address for the line port.
    - `hotlineEnabled` (boolean) **(requerido)**: Enable Hotline. Configure this line to automatically call a predefined number whenever taken off-hook. Once enabled, the line can only make calls to the predefined number set in hotlineDestination.
    - `hotlineDestination` (string) **(requerido)**: The preconfigured number for Hotline. Required only if `hotlineEnabled` is set to true.
    - `allowCallDeclineEnabled` (boolean) **(requerido)**: Set how a person's device behaves when a call is declined. When set to true, a call decline request is extended to all the endpoints on the device. When set to false, a call decline request only declines the current endpoint.
    - `lineLabel` (string): Device line label.
    - `linePort` (string): SIP username used in SIP signaling, for example, in registration.
    - `memberType` (string) **(requerido)**: * `PEOPLE` - Indicates the associated member is a person.  * `PLACE` - Indicates the associated member is a workspace.  * `VIRTUAL_LINE` - Indicates the associated member is a virtual line. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
    - `location` (object):
      - `id` (string) **(requerido)**: Location identifier associated with the members.
      - `name` (string) **(requerido)**: Location name associated with the member.
  - `maxLineCount` (number) **(requerido)**: Maximum number of lines available for the device.
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
