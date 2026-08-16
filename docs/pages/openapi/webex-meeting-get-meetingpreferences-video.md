---
doc_id: webex-meeting-get-meetingpreferences-video
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /meetingPreferences/video
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.388544+00:00
---

# GET /meetingPreferences/video

**API:** Webex Meetings
**Área:** Preferences
**operationId:** `Get Video Options`

## Resumen
Get Video Options

## Descripción
Retrieves video options for the authenticated user.

## Parámetros
- `userEmail` [query] (string): Email address for the user. This parameter is only used if the user or application calling the API has the [admin-level scopes](/docs/meetings#adminorganization-level-authentication-and-scopes). If set, the admin may specify the email of a user in a site they manage and the API will return details of the video options for that user.
- `siteUrl` [query] (string): URL of the Webex site to query. For individual use, if `siteUrl` is not specified, the query will use the default site of the user. For admin use, if `siteUrl` is not specified, the query will use the default site for the admin's authorization token used to make the call. In the case where the user belongs to a site different than the admin’s default site, the admin can set the site to query using the `siteUrl` parameter. All available Webex sites and default site of a user can be retrieved using [Get Site List](/docs/api/v1/meeting-preferences/get-site-list).

## Respuestas
- **200**: OK
  - `videoDevices` (array) **(requerido)**: Array of video devices. This attribute can be modified with the [Update Video Options](/docs/api/v1/meeting-preferences/update-video-options) API.
    - `deviceName` (string) **(requerido)**: Video system name. It cannot be empty. This attribute can be modified with the [Update Video Options](/docs/api/v1/meeting-preferences/update-video-options) API.
    - `deviceAddress` (string) **(requerido)**: Video address. It cannot be empty and must be in valid email format. This attribute can be modified with the [Update Video Options](/docs/api/v1/meeting-preferences/update-video-options) API.
    - `isDefault` (boolean) **(requerido)**: Flag identifying the device as the default video device. If user's video device list is not empty, one and only one device must be set as default. This attribute can be modified with the [Update Video Options](/docs/api/v1/meeting-preferences/update-video-options) API.
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden
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
