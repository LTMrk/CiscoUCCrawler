---
doc_id: webex-cloud-calling-get-telephony-config-virtuallines-virtuallineid-devices
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/virtualLines/{virtualLineId}/devices
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.656822+00:00
---

# GET /telephony/config/virtualLines/{virtualLineId}/devices

**API:** Webex Cloud Calling
**Área:** Virtual Line Call Settings
**operationId:** `Get List of Devices Assigned for a Virtual Line`

## Resumen
Get List of Devices Assigned for a Virtual Line

## Descripción
Retrieve Device details assigned for a virtual line.

Virtual line is a capability in Webex Calling that allows administrators to configure multiple lines to Webex Calling users.

Retrieving the assigned device detials for a virtual line requires a full, user, or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `virtualLineId` [path] (string) **(requerido)**: Retrieve settings for a virtual line with the matching ID.
- `orgId` [query] (string): Retrieve virtual line settings from this organization.

## Respuestas
- **200**: OK
  - `devices` (array): List of devices assigned to a virtual line.
    - `id` (string) **(requerido)**: Unique identifier for a device.
    - `description` (array): Comma separated array of tags used to describe device.
    - `model` (string) **(requerido)**: Identifier for device model.
    - `mac` (string): MAC address of device.
    - `primaryOwner` (boolean) **(requerido)**: Indicates whether the person or the workspace is the owner of the device and points to a primary Line/Port of the device.
    - `type` (string) **(requerido)**: * `PRIMARY` - Primary line for the member.  * `SHARED_CALL_APPEARANCE` - Shared line for the member. A shared line allows users to receive and place calls to and from another user's extension, using their own device. Valores: PRIMARY, SHARED_CALL_APPEARANCE.
    - `owner` (object) **(requerido)**:
      - `id` (string) **(requerido)**: Unique identifier of a person or a workspace.
      - `type` (string) **(requerido)**: * `PEOPLE` - Indicates the associated member is a person.  * `PLACE` - Indicates the associated member is a workspace. Valores: PEOPLE, PLACE.
      - `firstName` (string): The first name of the device owner.
      - `lastName` (string): The last name of the device owner.
    - `activationState` (string) **(requerido)**: * `ACTIVATING` - Indicates a device is activating.  * `ACTIVATED` - Indicates a device is activated.  * `DEACTIVATED` - Indicates a device is deactivated. Valores: ACTIVATING, ACTIVATED, DEACTIVATED.
    - `location` (object) **(requerido)**: Location details of virtual line.
      - `id` (string) **(requerido)**: ID of location associated with virtual line.
      - `name` (string) **(requerido)**: Name of location associated with virtual line.
  - `availableEndpointType` (string) **(requerido)**: * `PRIMARY` - Primary line for the member.  * `SHARED_CALL_APPEARANCE` - Shared line for the member. A shared line allows users to receive and place calls to and from another user's extension, using their own device. Valores: PRIMARY, SHARED_CALL_APPEARANCE.
  - `maxDeviceCount` (number) **(requerido)**: Maximum number of devices a virtual line can be assigned to.
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
