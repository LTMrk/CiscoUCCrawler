---
doc_id: webex-admin-patch-identity-scim-orgid-v2-groups-groupid
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: PATCH
path: /identity/scim/{orgId}/v2/Groups/{groupId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.160165+00:00
---

# PATCH /identity/scim/{orgId}/v2/Groups/{groupId}

**API:** Webex Admin
**Área:** SCIM 2 Groups
**operationId:** `Update a group with PATCH`

## Resumen
Update a group with PATCH

## Descripción
Update group attributes with PATCH.

Specify the group ID in the `groupId` parameter in the URI.

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

1. Each operation on an attribute must be compatible with the attribute's mutability.

1. Each PATCH operation represents a single action to be applied to the
   same SCIM resource specified by the request URI. Operations are
   applied sequentially in the order they appear in the array. Each
   operation in the sequence is applied to the target resource; the
   resulting resource becomes the target of the next operation.
   Evaluation continues until all operations are successfully applied or
   until an error condition is encountered.

<br/>

**Add operations**:

The `add` operation is used to add a new attribute value to an existing resource. The operation must contain a `value` member whose content specifies the value to be added. The value may be a quoted value, or it may be a JSON object containing the sub-attributes of the complex attribute specified in the operation's `path`. The result of the add operation depends upon the target location indicated by `path` references:

<br/>

- If omitted, the target location is assumed to be the resource itself. The `value` parameter contains a set of attributes to be added to the resource.

- If the target location does not exist, the attribute and value are added.

- If the target location specifies a complex attribute, a set of sub-attributes shall be specified in the `value` parameter.

- If the target location specifies a multi-valued attribute, a new value is added to the attribute.

- If the target location specifies a single-valued attribute, the existing value is replaced.

- If the target location specifies an attribute that does not exist (has no value), the attribute is added with the new value.

- If the target location exists, the value is replaced.

- If the target location already contains the value specified, no changes should be made to the resource.

<br/>

**Replace operations**:

The `replace` operation replaces the value at the target location specified by the `path`. The operation performs the following functions, depending on the target location specified by `path`:

<br/>

- If the `path` parameter is omitted, the target is assumed to be the resource itself. In this case, the `value` attribute shall contain a list of one or more attributes that are to be replaced.

- If the target location is a single-value attribute, the value of the attribute is replaced.

- If the target location is a multi-valued attribute and no filter is specified, the attribute and all values are replaced.

- If the target location path specifies an attribute that does not exist, the service provider shall treat the operation as an "add".

- If the target location specifies a complex attribute, a set of sub-attributes SHALL be specified in the `value` parameter, which replaces any existing values or adds where an attribute did not previously exist. Sub-attributes that are not specified in the `value` parameters are left unchanged.

- If the target location is a multi-valued attribute and a value selection ("valuePath") filter is specified that matches one or more values of the multi-valued attribute, then all matching record values will be replaced.

- If the target location is a complex multi-valued attribute with a value selection filter ("valuePath") and a specific sub-attribute (e.g., "addresses[type eq "work"].streetAddress"), the matching sub-attribute of all matching records is replaced.

- If the target location is a multi-valued attribute for which a value selection filter ("valuePath") has been supplied and no record match was made, the service provider will indicate the failure by returning HTTP status code 400 and a `scimType` error code of `noTarget`.

<br/>

**Remove operations**:

The `remove` operation removes the value at the target location specified by the required attribute `path`. The operation performs the following functions, depending on the target location specified by `path`:

<br/>

- If `path` is unspecified, the operation fails with HTTP status code 400 and a "scimType" error code of "noTarget".

- If the target location is a single-value attribute, the attribute and its associated value is removed, and the attribute will be considered unassigned.

- If the target location is a multi-valued attribute and no filter is specified, the attribute and all values are removed, and the attribute SHALL be considered unassigned.

- If the target location is a multi-valued attribute and a complex filter is specified comparing a `value`, the values matched by the filter are removed. If no other values remain after the removal of the selected values, the multi-valued attribute will be considered unassigned.

- If the target location is a complex multi-valued attribute and a complex filter is specified based on the attribute`s sub-attributes, the matching records are removed. Sub-attributes whose values have been removed will be considered unassigned. If the complex multi-valued attribute has no remaining records, the attribute will be considered unassigned.

## Parámetros
- `orgId` [path] (string) **(requerido)**: The ID of the organization to which this group belongs. If not specified, the organization ID from the OAuth token is used.
- `groupId` [path] (string) **(requerido)**: A unique identifier for the group.

## Cuerpo de la petición (application/json)
- `schemas` (array) **(requerido)**: Input JSON schemas.
- `Operations` (array) **(requerido)**: A list of patch operations.
  - `op` (string) **(requerido)**: The operation to perform. Valores: add, replace, remove.
  - `path` (string): A string containing an attribute path describing the target of the operation.
  - `value` (array): New value.
    - `type` (string): Type of inheritance. Currently, `role` and `location_role` type is supported. Only `policy` usage supports inheritance. Valores: role, location_role.
    - `value` (string): The value of the inheritance. For the role type, this can be role names such as `id_full_admin`, `id_user_admin`, etc. For the location_role type, the value should be `location_full_admin`.
    - `nested` (boolean): Indicates whether this inheritance is nested.
    - `locationId` (string): The ID of the location group.
    - `scope` (array): Indicates which types of entities can inherit this property.

### Ejemplo de petición
```json
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations": [
    {
      "op": "add",
      "path": "urn:scim:schemas:extension:cisco:webexidentity:2.0:Group.inheritances",
      "value": [
        {
          "type": "location_role",
          "value": "location_full_admin",
          "nested": false,
          "locationId": "72e22cec-cc28-45b7-b3dc-eafe0f44a2bd",
          "scope": [
            "user"
          ]
        }
      ]
    }
  ]
}
```

## Respuestas
- **200**: OK
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
