---
doc_id: webex-admin-post-identity-scim-orgid-v2-groups
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: POST
path: /identity/scim/{orgId}/v2/Groups
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.159419+00:00
---

# POST /identity/scim/{orgId}/v2/Groups

**API:** Webex Admin
**Área:** SCIM 2 Groups
**operationId:** `Create a group`

## Resumen
Create a group

## Descripción
Create a new group for a given organization. The group may optionally be created with group members.

<br/>

**Authorization**

OAuth token returned by Identity Broker.

<br/>

One of the following OAuth scopes is required:

- `identity:people_rw`

<br/>

The following administrators can use this API:

- `id_full_admin`

- `id_group_admin`

<br/>

**Usage**:

1. The input JSON must conform to one of the following schemas:
    - `urn:ietf:params:scim:schemas:core:2.0:Group`
    - `urn:scim:schemas:extension:cisco:webexidentity:2.0:Group`

1. Unrecognized schemas (ID/section) are ignored.

1. Read-only attributes provided as input values are ignored.

## Parámetros
- `orgId` [path] (string) **(requerido)**: The ID of the organization to which this group belongs. If not specified, the organization ID from the OAuth token is used.

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
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group",
    "urn:scim:schemas:extension:cisco:webexidentity:2.0:Group"
  ],
  "displayName": "group1@example.com",
  "externalId": "test",
  "members": [
    {
      "value": "c5349664-9f3d-410b-8bd3-6c31f181f13d",
      "type": "user"
    }
  ],
  "urn:scim:schemas:extension:cisco:webexidentity:2.0:Group": {
    "usage": "policy",
    "inheritances": [
      {
        "type": "role",
        "value": "id_full_admin",
        "nested": false,
        "scope": [
          "user"
        ]
      },
      {
        "type": "location_role",
        "value": "location_full_admin",
        "nested": false,
        "locationId": "72e22cec-cc28-45b7-b3dc-eafe0f44a2bd",
        "scope": [
          "user"
        ]
      }
    ],
    "owners": [
      {
        "value": "c5349664-9f3d-410b-8bd3-6c31f181f13d"
      }
    ],
    "managedBy": [
      {
        "orgId": "d1349664-9f3d-410b-8bd3-6c31f181f14e",
        "type": "user",
        "id": "c5349664-9f3d-410b-8bd3-6c31f181f13d",
        "role": "location_full_admin"
      }
    ]
  }
}
```

## Respuestas
- **201**: Created
  - `schemas` (array) **(requerido)**: Input JSON schemas.
  - `displayName` (string) **(requerido)**: A human-readable name for the group.
  - `id` (string) **(requerido)**: A unique identifier for the group.
  - `externalId` (string): An identifier for the resource as defined by the provisioning client.
  - `members` (array): A list of members of this group.
    - `type` (string): A label indicating the type of resource, for example user, machine, or group.
    - `value` (string): The identifier of the member of this Group.
    - `display` (string): A human-readable name for the group member.
    - `$ref` (string): The URI corresponding to a SCIM resource that is a member of this Group.
  - `meta` (object) **(requerido)**: Response metadata.
    - `resourceType` (string):
    - `organizationID` (string):
    - `created` (string) **(requerido)**: The date and time the group was created.
    - `lastModified` (string) **(requerido)**: The date and time the group was last changed.
    - `version` (string) **(requerido)**: The version of the user.
    - `location` (string) **(requerido)**: The resource itself.
  - `urn:scim:schemas:extension:cisco:webexidentity:2.0:Group` (object): The Cisco extention of SCIM 2
    - `usage` (string) **(requerido)**: The identifier of this group.
    - `owners` (array): The owners of this group.
      - `value` (string): The identifier of the owner of this Group.
    - `managedBy` (array): A list of delegates of this group.
      - `orgId` (string): The Organization identifier of the resource.
      - `type` (string): The resource type.
      - `id` (string): The identifier of the resource.
      - `role` (string): The delegated role.
    - `provisionSource` (string) **(requerido)**: The identifier of the source.
    - `inheritances` (array): An array of inheritances
      - `type` (string): Type of inheritance. Currently, `role` and `location_role` type is supported. Only `policy` usage supports inheritance. Valores: role, location_role.
      - `value` (string): The value of the inheritance. For the role type, this can be role names such as `id_full_admin`, `id_user_admin`, etc. For the location_role type, the value should be `location_full_admin`.
      - `nested` (boolean): Indicates whether this inheritance is nested.
      - `locationId` (string): The ID of the location group.
      - `scope` (array): Indicates which types of entities can inherit this property.
    - `meta` (object) **(requerido)**: Response metadata.
      - `organizationID` (string) **(requerido)**: The ID of the organization to which this group belongs.
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
