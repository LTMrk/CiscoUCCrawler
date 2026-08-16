---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-devices
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/{personId}/devices
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.583289+00:00
---

# GET /telephony/config/people/{personId}/devices

**API:** Webex Cloud Calling
**Área:** Device Call Settings
**operationId:** `getPersonDevices`

## Resumen
Get Person Devices

## Descripción
Get all devices for a person.

This requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `personId` [path] (string) **(requerido)**: Person for whom to retrieve devices.
- `orgId` [query] (string): Organization to which the person belongs.

## Respuestas
- **200**: OK
  - `devices` (array) **(requerido)**: Array of devices available to person.
    - `id` (string) **(requerido)**: Unique identifier for a device.
    - `description` (array): Comma separated array of tags used to describe device.
    - `model` (string) **(requerido)**: Identifier for device model.
    - `modelType` (string): * `DEVICE` - The endpoint is a device.  * `APPLICATION` - The endpoint is a application. Valores: DEVICE, APPLICATION.
    - `mac` (string): MAC address of device.
    - `ipAddress` (string): IP address of device.
    - `primaryOwner` (boolean) **(requerido)**: Indicates whether the person or the workspace is the owner of the device, and points to a primary Line/Port of the device.
    - `type` (string) **(requerido)**: * `PRIMARY` - Primary line for the member.  * `SHARED_CALL_APPEARANCE` - Shared line for the member. A shared line allows users to receive and place calls to and from another user's extension, using their own device.  * `MOBILITY` - Device is a shared line.  * `HOTDESKING_GUEST` - Device is a hotdesking guest. Valores: PRIMARY, SHARED_CALL_APPEARANCE, MOBILITY, HOTDESKING_GUEST.
    - `hoteling` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: Enable/Disable hoteling Host. Enabling the device for hoteling means that a guest(end user) can log into this host(workspace device) and use this device  as if it were their own. This is useful when traveling to a remote office but still needing to place/receive calls with their telephone number and access features normally available to them on their office phone.
      - `limitGuestUse` (boolean): Enable limiting the time a guest can use the device. The time limit is configured via `guestHoursLimit`.
      - `guestHoursLimit` (number): Time Limit in hours until hoteling is enabled. Mandatory if `limitGuestUse` is enabled.
    - `owner` (object) **(requerido)**:
      - `id` (string) **(requerido)**: Unique identifier of a person or a workspace.
      - `type` (string) **(requerido)**: * `PEOPLE` - Indicates the associated member is a person.  * `PLACE` - Indicates the associated member is a workspace. Valores: PEOPLE, PLACE.
      - `firstName` (string): The first name of the device owner.
      - `lastName` (string): The last name of the device owner.
    - `activationState` (string) **(requerido)**: * `activating` - Device is activating using an activation code.  * `activated` - Device has been activated using an activation code.  * `deactivated` - Device has not been activated using an activation code. Valores: activating, activated, deactivated.
  - `maxDeviceCount` (number) **(requerido)**: Maximum number of devices a person can be assigned to.
  - `maxOwnedDeviceCount` (number) **(requerido)**: Maximum number of devices a person can own.
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
