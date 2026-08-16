---
doc_id: webex-meeting-put-admin-meeting-userconfig-trackingcodes
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: PUT
path: /admin/meeting/userconfig/trackingCodes
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.400748+00:00
---

# PUT /admin/meeting/userconfig/trackingCodes

**API:** Webex Meetings
**Área:** Tracking Codes
**operationId:** `Update User Tracking Codes`

## Resumen
Update User Tracking Codes

## Descripción
Updates tracking codes for a specified user by an admin user.

* The `siteUrl` is required. The operation updates a user's tracking code on the specified site. All a user's available Webex sites can be retrieved by the [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API. Please note that the user here is the admin user who invokes the API, not the user specified by `personId` or `email`.

* A name that is not found in the site-level tracking codes cannot be set for a user's tracking codes. All available site-level tracking codes for a site can be retrieved by the [List Tracking Codes](/docs/api/v1/tracking-codes/list-tracking-codes) API.

* If the `inputMode` of a user's tracking code is `select` or `hostProfileSelect`, its value must be one of the site-level options of that tracking code. All available site-level tracking codes for a site can be retrieved by the [List Tracking Codes](/docs/api/v1/tracking-codes/list-tracking-codes) API.

* Admins can switch any Control Hub managed site from using classic tracking codes to mapped tracking codes in Control Hub, this is a one-time irreversible operation. Once the tracking codes are mapped to custom or user profile attributes, they cannot update user's tracking codes when the mapping process is in progress or the mapping process is completed.

## Cuerpo de la petición (application/json)
- `siteUrl` (string) **(requerido)**: Site URL for the tracking code.
- `personId` (string): Unique identifier for the user. At least one parameter of `personId` or `email` is required. `personId` must precede `email` if both are specified.
- `email` (string): Email address for the user. At least one parameter of `personId` or `email` is required. `personId` must precede `email` if both are specified.
- `trackingCodes` (array): Tracking code information for updates.
  - `name` (string) **(requerido)**: Name for tracking code. The name cannot be empty and the maximum size is 120 characters.
  - `value` (string) **(requerido)**: Value for tracking code. `value` cannot be empty and the maximum size is 120 characters.

### Ejemplo de petición
```json
{
  "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xOGJiOWNjMC0zMWM2LTQ3MzYtYmE4OC0wMDk5ZmQzNDNmODE",
  "email": "john.andersen@example.com",
  "siteUrl": "example.webex.com",
  "trackingCodes": [
    {
      "name": "Department",
      "value": "Sales"
    },
    {
      "name": "Division",
      "value": "Part-time"
    }
  ]
}
```

## Respuestas
- **200**: OK
  - `siteUrl` (string) **(requerido)**: Site URL for the tracking code.
  - `personId` (string): Unique identifier for the user.
  - `email` (string): Email address for the user.
  - `trackingCodes` (array): Tracking code information.
    - `id` (string) **(requerido)**: Unique identifier for tracking code.
    - `name` (string) **(requerido)**: Name for tracking code.
    - `value` (string) **(requerido)**: Value for tracking code.
- **400**: Bad Request
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
