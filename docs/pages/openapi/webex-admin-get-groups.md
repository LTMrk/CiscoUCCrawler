---
doc_id: webex-admin-get-groups
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: GET
path: /groups
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.149816+00:00
---

# GET /groups

**API:** Webex Admin
**Área:** Groups
**operationId:** `List and Search Groups`

## Resumen
List and Search Groups

## Descripción
List groups in your organization.

* Set the `includeMembers` parameter to `true` to return group members. The total number of members returned is limited to 500.

* Use the `startIndex` and `count` parameters to page through result set.

* To search for a specific group use the `filter` parameter.

* Use `sortBy` parameter to sort the responses by `id` or `displayName`.

## Parámetros
- `orgId` [query] (string): List groups in this organization. Only admin users of another organization (such as partners) may use this parameter.
- `filter` [query] (string): Searches the group by `displayName` with an operator and a value.  The available operators are `eq` (equal) and `sw` (starts with).  Only `displayName` can be used to filter results.
- `attributes` [query] (string): The attributes to return.
- `sortBy` [query] (string): Sort the results based by group `displayName`.
- `sortOrder` [query] (string): Sort results alphabetically by group display name, in ascending or descending order.
- `includeMembers` [query] (boolean): Optionally return group members in the response. The maximum number of members returned is 500.
- `startIndex` [query] (number): The index to start for group pagination.
- `count` [query] (number): Specifies the desired number of search results per page.

## Respuestas
- **200**: OK
  - `totalResults` (number): Total number of groups returned in the response.
  - `startIndex` (number):
  - `itemsPerPage` (number):
  - `groups` (array): An array of group objects.
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
