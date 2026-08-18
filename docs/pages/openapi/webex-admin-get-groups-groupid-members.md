---
doc_id: webex-admin-get-groups-groupid-members
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /groups/{groupId}/members
operation_id: Get Group Members
tags: Groups
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.564856+00:00
---

# GET /groups/{groupId}/members

**API:** Webex Admin
**Área:** Groups
**operationId:** `Get Group Members`

## Resumen
Get Group Members

## Descripción
Gets the members of a group.

* The default maximum members returned is 500.

* Control parameters is available to page through the members and to control the size of the results.

## Parámetros
- `groupId` [path] (string) (**requerido**): A unique identifier for the group.
- `startIndex` [query] (number): The index to start for group pagination.
- `count` [query] (number): Non-negative integer that specifies the desired number of search results per page. Maximum value for the count is 500.

## Ejemplo de invocación
```bash
curl -X GET '/groups/<groupId>/members' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
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

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1NDSU1fR1JPVVAvMjUxMDRiZTAtZjg3NC00MzQzLTk2MDctZGYwMmRmMzdiNWMxOjM0OGFkYjgxLTI4ZjktNGFiNS1iMmQ2LWU5YjQ5NGU3MmEwNg",
  "displayName": "Sales Group",
  "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8zNDhhZGI4MS0yOGY5LTRhYjUtYjJkNi1lOWI0OTRlNzJhMDY",
  "created": "2022-02-17T02:13:29.706Z",
  "lastModified": "2022-02-17T02:13:29.706Z",
  "memberSize": 1,
  "members": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xOTUzOTdhMi03MTU5LTRjNTgtYTBiOC00NmQ2ZWZlZTdkMTM",
      "type": "user",
      "displayName": "Jane Smith"
    }
  ]
}
```

## Respuestas de error
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

## Contexto de la API
The Webex Admin APIs provide comprehensive programmatic access to administrative functions for managing Webex organizations, users, licenses, and settings. These APIs enable automation of user provisioning, license assignment, compliance management, and audit event retrieval. Administrators can integrate with enterprise identity systems, enforce security policies, monitor usage, and streamline onboarding/offboarding processes. The APIs support granular control over organizational resources, making them ideal for large-scale deployments and custom admin tooling.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs