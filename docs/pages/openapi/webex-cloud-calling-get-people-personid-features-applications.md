---
doc_id: webex-cloud-calling-get-people-personid-features-applications
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /people/{personId}/features/applications
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.636559+00:00
---

# GET /people/{personId}/features/applications

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `getPersonsAppServicesSettingsNew`

## Resumen
Retrieve a person's Application Services Settings New

## Descripción
Gets mobile and PC applications settings for a user.

Application services let you determine the ringing behavior for calls made to people in certain scenarios. You can also specify which devices can download the Webex Calling app.

Requires a full, user, or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `personId` [path] (string) **(requerido)**: Unique identifier for the person.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Respuestas
- **200**: OK
  - `ringDevicesForClickToDialCallsEnabled` (boolean) **(requerido)**: When `true`, indicates to ring devices for outbound Click to Dial calls.
  - `ringDevicesForGroupPageEnabled` (boolean) **(requerido)**: When `true`, indicates to ring devices for inbound Group Pages.
  - `ringDevicesForCallParkEnabled` (boolean) **(requerido)**: When `true`, indicates to ring devices for Call Park recalled.
  - `browserClientEnabled` (boolean) **(requerido)**: Indicates that the browser Webex Calling application is enabled for use.
  - `browserClientId` (string): Device ID of WebRTC client. Returns only if `browserClientEnabled` is true.
  - `desktopClientEnabled` (boolean) **(requerido)**: Indicates that the desktop Webex Calling application is enabled for use.
  - `desktopClientId` (string): Device ID of Desktop client. Returns only if `desktopClientEnabled` is true.
  - `tabletClientEnabled` (boolean) **(requerido)**: Indicates that the tablet Webex Calling application is enabled for use.
  - `tabletClientId` (string): Device ID of Tablet client. Returns only if `tabletClientEnabled` is true.
  - `mobileClientEnabled` (boolean) **(requerido)**: Indicates that the mobile Webex Calling application is enabled for use.
  - `mobileClientId` (string): Device ID of Mobile client. Returns only if `mobileClientEnabled` is true.
  - `availableLineCount` (number) **(requerido)**: Number of available device licenses for assigning devices/apps.
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
