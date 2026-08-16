---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-features-hotdesking-availablemembers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/{personId}/features/hotDesking/availableMembers
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.655067+00:00
---

# GET /telephony/config/people/{personId}/features/hotDesking/availableMembers

**API:** Webex Cloud Calling
**Área:** Features: Hot Desking Members, User Call Settings (3/3)
**operationId:** `searchAvailableHotDeskingMembers`

## Resumen
Search Available Hot Desking Members

## Descripción
Retrieve members available for assignment to a person's hot desking guest profile.

Available members can include people, workspaces, and virtual lines that can be added as shared lines on the hot desking profile.

This API requires a full, user, device, read-only, or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `personId` [path] (string) **(requerido)**: Unique identifier for the person.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization, such as partners, may use this parameter. If not specified, the organization from the OAuth token is used.
- `locationId` [query] (string): Return only available members in this location.
- `max` [query] (integer): Maximum number of records to return.
- `start` [query] (integer): Offset from the first result to fetch.
- `memberName` [query] (string): Search for available members by name.
- `phoneNumber` [query] (string): Search for available members by phone number.
- `extension` [query] (string): Search for available members by extension.
- `order` [query] (array): Sort order for the available member list. Multiple order values may be provided.

## Respuestas
- **200**: OK
  - `members` (array) **(requerido)**: List of members that can be assigned to the person's hot desking guest profile.
    - `id` (string) **(requerido)**: Unique identifier for the available member.
    - `firstName` (string): First name of the available member.
    - `lastName` (string): Last name of the available member.
    - `phoneNumber` (string): Phone number of the available member.
    - `extension` (string): Extension of the available member.
    - `routingPrefix` (string): Routing prefix of the member's location.
    - `esn` (string): Enterprise significant number for the available member.
    - `lineType` (string) **(requerido)**: Line type for the hot desking guest profile member.  * `HOTDESKING_GUEST` - Primary hot desking guest profile line.  * `SHARED_CALL_APPEARANCE` - Shared line assigned to the hot desking guest profile.  * `PRIMARY` - Primary line.  * `MOBILITY` - Mobility line. Valores: HOTDESKING_GUEST, SHARED_CALL_APPEARANCE, PRIMARY, MOBILITY.
    - `memberType` (string) **(requerido)**: Type of assigned or available member.  * `PEOPLE` - The member is a person.  * `PLACE` - The member is a workspace.  * `VIRTUAL_LINE` - The member is a virtual line. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
    - `location` (object): Location associated with the hot desking member.
      - `id` (string) **(requerido)**: Unique identifier for the location.
      - `name` (string) **(requerido)**: Name of the location.
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
