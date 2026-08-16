---
doc_id: webex-admin-get-groups-groupid
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: GET
path: /groups/{groupId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.150065+00:00
---

# GET /groups/{groupId}

**API:** Webex Admin
**Área:** Groups
**operationId:** `Get Group Details`

## Resumen
Get Group Details

## Descripción
Get details for a group, by ID.

Optionally, the members may be retrieved with this request. The maximum number of members returned is 500.

## Parámetros
- `groupId` [path] (string) **(requerido)**: A unique identifier for the group.
- `includeMembers` [query] (boolean): Include the members as part of the response.

## Respuestas
- **200**: OK
  - `id` (string): A unique identifier for the group.
  - `displayName` (string): The name of the group.
  - `orgId` (string): The ID of the organization to which this group belongs.
  - `created` (string): The timestamp indicating creation date/time of group
  - `lastModified` (string): The timestamp indicating lastModification time of group
  - `memberSize` (number):
  - `members` (array): An array of members
    - `id` (string): Person ID of the group member.
    - `type` (string): Member type.
    - `displayName` (string):
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
