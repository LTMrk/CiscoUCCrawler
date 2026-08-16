---
doc_id: webex-cloud-calling-get-telephony-config-supporteddevices
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/supportedDevices
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.583794+00:00
---

# GET /telephony/config/supportedDevices

**API:** Webex Cloud Calling
**Área:** Device Call Settings With Device Dynamic Settings
**operationId:** `readTheListOfSupportedDevices`

## Resumen
Read the List of Supported Devices

## Descripción
Gets the list of supported devices for an organization.

Retrieving this list requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): List supported devices for an organization.
- `allowConfigureLayoutEnabled` [query] (boolean): List supported devices that allow the user to configure the layout.
- `type` [query] (string): List supported devices of a specific type. To excluded device types from a request or query, add `type=not:DEVICE_TYPE`. For example, `type=not:MPP`.

## Respuestas
- **200**: OK
  - `upgradeChannelList` (array) **(requerido)**: List of available upgrade channels.  * `STABLE` - These are standard stable releases.  * `STABLE_DELAY` - These are delayed stable releases.  * `PREVIEW` - These are Preview/pre-release versions.  * `BETA` - These are Beta testing versions.  * `TESTING` - These are testing versions.
  - `devices` (array) **(requerido)**: List of supported devices.
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
