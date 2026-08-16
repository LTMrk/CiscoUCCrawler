---
doc_id: webex-admin-post-groups
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: POST
path: /groups
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.149671+00:00
---

# POST /groups

**API:** Webex Admin
**Área:** Groups
**operationId:** `Create a Group`

## Resumen
Create a Group

## Descripción
Create a new group for a given organization. The group may optionally be created with group members.

## Cuerpo de la petición (application/json)
- `schemas` (array) **(requerido)**: Input JSON schemas.
- `displayName` (string) **(requerido)**: A human-readable name for the Group.
- `externalId` (string): An identifier for the resource as defined by the provisioning client.
- `members` (array): A list of members of this group.
  - `value` (string): The identifier of the member of this Group.
  - `type` (string): A label indicating the type of resource, for example user, machine, or group.
- `urn:scim:schemas:extension:cisco:webexidentity:2.0:Group` (object): The Cisco extension of SCIM 2.
  - `usage` (string): The identifier of this Group.
  - `owners` (array): The owners of this group.
    - `value` (string): The identifier of the owner of this group.
  - `inheritances` (array): An array of inheritances
    - `type` (string): Type of inheritance. Currently, `role` and `location_role` type is supported. Only `policy` usage supports inheritance. Valores: role, location_role.
    - `value` (string): The value of the inheritance. For the role type, this can be role names such as `id_full_admin`, `id_user_admin`, etc. For the location_role type, the value should be `location_full_admin`.
    - `nested` (boolean): Indicates whether this inheritance is nested.
    - `locationId` (string): The ID of the location group.
    - `scope` (array): Indicates which types of entities can inherit this property.
  - `managedBy` (array): A list of delegates of this group.
    - `orgId` (string): The Organization identifier of the resource.
    - `type` (string): The resource type.
    - `id` (string): The identifier of the resource.
    - `role` (string): The delegated role.

### Ejemplo de petición
```json
{
  "displayName": "Sales Group",
  "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8zNDhhZGI4MS0yOGY5LTRhYjUtYjJkNi1lOWI0OTRlNzJhMDY",
  "description": "Salas Group in San Jose",
  "members": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xOTUzOTdhMi03MTU5LTRjNTgtYTBiOC00NmQ2ZWZlZTdkMTM"
    }
  ]
}
```

## Respuestas
- **201**: Created
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
