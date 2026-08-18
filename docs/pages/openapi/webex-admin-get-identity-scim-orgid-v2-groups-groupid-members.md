---
doc_id: webex-admin-get-identity-scim-orgid-v2-groups-groupid-members
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /identity/scim/{orgId}/v2/Groups/{groupId}/Members
operation_id: Get Group Members
tags: SCIM 2 Groups
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.582125+00:00
---

# GET /identity/scim/{orgId}/v2/Groups/{groupId}/Members

**API:** Webex Admin
**Área:** SCIM 2 Groups
**operationId:** `Get Group Members`

## Resumen
Get Group Members

## Descripción
Returns the members of a group.

- The default maximum number of members returned is 500.

- Control parameters are available to page through the members and to control the size of the results.

- Long result sets are split into [pages](/docs/basics#pagination).

**Note**
Location groups are different from SCIM groups. You cannot search for identities in a location via groups.

<br/>

**Authorization**

OAuth token returned by the Identity Broker.

<br/>

One of the following OAuth scopes is required:

- `identity:people_rw`

- `identity:people_read`

<br/>

The following administrators can use this API:

- `id_full_admin`

- `id_group_admin`

- `id_readonly_admin`

- `id_device_admin`

## Parámetros
- `orgId` [path] (string) (**requerido**): The ID of the organization to which this group belongs. If not specified, the organization ID from the OAuth token is used.
- `groupId` [path] (string) (**requerido**): A unique identifier for the group.
- `startIndex` [query] (number): The index to start for group pagination.
- `count` [query] (number): Non-negative integer that specifies the desired number of search results per page. The maximum value for the count is 500.
- `memberType` [query] (string): Filter the members by member type. Sample data: `user`, `machine`, `group`.

## Ejemplo de invocación
```bash
curl -X GET '/identity/scim/<orgId>/v2/Groups/<groupId>/Members' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `schemas` (array) (**requerido**): Input JSON schemas.
- `displayName` (string) (**requerido**): A human-readable name for the group.
- `totalResults` (number): Total number of groups in search results.
- `itemsPerPage` (number): The total number of items in a paged result.
- `startIndex` (number): Start at the one-based offset in the list of matching groups.
- `members` (array): A list of members of this group.
  - `type` (string): A label indicating the type of resource, for example user, machine, or group.
  - `value` (string): The identifier of the member of this Group.
  - `display` (string): A human-readable name for the group member.

### Ejemplo — respuesta 200
```json
{
  "schemas": [
    "urn:scim:schemas:extension:cisco:webexidentity:2.0:GroupMembers"
  ],
  "memberSize": 2,
  "displayName": "group_name",
  "itemsPerPage": 2,
  "startIndex": 1,
  "members": [
    {
      "value": "c5349664-9f3d-410b-8bd3-6c31f181f13d",
      "type": "user",
      "display": "A user"
    },
    {
      "value": "ffd2164c-b938-46dd-8b2f-def6c33b45d0",
      "type": "group",
      "display": "A nested group"
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