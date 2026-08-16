---
doc_id: webex-cloud-calling-get-telephony-config-paging
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/paging
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.617818+00:00
---

# GET /telephony/config/paging

**API:** Webex Cloud Calling
**Área:** Features:  Paging Group
**operationId:** `Read the List of Paging Groups`

## Resumen
Read the List of Paging Groups

## Descripción
List all Paging Groups for the organization.

Group Paging allows a person to place a one-way call or group page to up to 75 people and/or workspaces by
dialing a number or extension assigned to a specific paging group. The Group Paging service makes a simultaneous call to all the assigned targets.

Retrieving this list requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): List paging groups for this organization.
- `max` [query] (number): Limit the number of objects returned to this maximum count. Default is 2000
- `start` [query] (number): Start at the zero-based offset in the list of matching objects. Default is 0
- `locationId` [query] (string): Return only paging groups with matching location ID. Default is all locations
- `name` [query] (string): Return only paging groups with the matching name.
- `phoneNumber` [query] (string): Return only paging groups with matching primary phone number or extension.

## Respuestas
- **200**: OK
  - `locationPaging` (array) **(requerido)**: Array of paging groups.
    - `id` (string) **(requerido)**: A unique identifier for the paging group.
    - `name` (string) **(requerido)**: Unique name for the paging group. Minimum length is 1. Maximum length is 30.
    - `phoneNumber` (string): Paging group phone number. Minimum length is 1. Maximum length is 23. Either `phoneNumber` or `extension` is mandatory.
    - `extension` (string): Paging group extension. Minimum length is 2. Maximum length is 10. Either `phoneNumber` or `extension` is mandatory.
    - `routingPrefix` (string): Routing prefix of location.
    - `esn` (string): Routing prefix + extension of a person or workspace.
    - `locationName` (string) **(requerido)**: Name of location for paging group.
    - `locationId` (string) **(requerido)**: Id of location for paging group.
    - `tollFreeNumber` (boolean) **(requerido)**: Flag to indicate toll free number.
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
