---
doc_id: webex-meeting-get-admin-meeting-userconfig-trackingcodes
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /admin/meeting/userconfig/trackingCodes
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.400609+00:00
---

# GET /admin/meeting/userconfig/trackingCodes

**API:** Webex Meetings
**Área:** Tracking Codes
**operationId:** `Get User Tracking Codes`

## Resumen
Get User Tracking Codes

## Descripción
Lists user's tracking codes by an admin user.

* At least one parameter, either `personId`, or `email` is required. `personId` must come before `email` if both are specified. Please note that `email` is specified in the request header.

* If `siteUrl` is specified, the tracking codes of the specified site will be listed; otherwise, the tracking codes of a user's preferred site are listed. All available Webex sites and preferred sites of a user can be retrieved by the [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API. Please note that the user here is the admin user who invokes the API, not the user specified by `personId` or email.

* Admins can switch any Control Hub managed site from using classic tracking codes to mapped tracking codes in Control Hub, this is a one-time irreversible operation. Once the tracking codes are mapped to custom or user profile attributes, the response returns the user's mapped tracking codes.

#### Request Header

* `email`: Email address for the user whose tracking codes are being retrieved. The admin users can specify the email of a user on a site they manage and the API returns details for the user's tracking codes. At least one parameter of `personId` or `email` is required.

## Parámetros
- `siteUrl` [query] (string): URL of the Webex site from which the API retrieves the tracking code. If not specified, the API retrieves the tracking code from the user's preferred site. All available Webex sites and preferred sites of a user can be retrieved by the [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.
- `personId` [query] (string): Unique identifier for the user whose tracking codes are being retrieved. The admin user can specify the `personId` of a user on a site they manage and the API returns details for the user's tracking codes. At least one parameter of `personId` or `email` is required.
- `email` [header] (string): e.g. john.andersen@example.com

## Respuestas
- **200**: OK
  - `siteUrl` (string) **(requerido)**: Site URL for the tracking code.
  - `personId` (string): Unique identifier for the user.
  - `email` (string): Email address for the user.
  - `trackingCodes` (array): Tracking code information.
    - `id` (string) **(requerido)**: Unique identifier for tracking code.
    - `name` (string) **(requerido)**: Name for tracking code.
    - `value` (string) **(requerido)**: Value for tracking code.
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found
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
