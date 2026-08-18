---
doc_id: webex-admin-patch-identity-scim-orgid-v2-users-userid
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: PATCH
path: /identity/scim/{orgId}/v2/Users/{userId}
operation_id: Update a user with PATCH
tags: SCIM 2 Users
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.587945+00:00
---

# PATCH /identity/scim/{orgId}/v2/Users/{userId}

**API:** Webex Admin
**Área:** SCIM 2 Users
**operationId:** `Update a user with PATCH`

## Resumen
Update a user with PATCH

## Descripción
<br/>

**Authorization**

OAuth token rendered by Identity Broker.

<br/>

One of the following OAuth scopes is required:

- `identity:people_rw`

<br/>

The following administrators can use this API:

- `id_full_admin`

- `id_user_admin`

<br/>

**Usage**:

1. The PATCH API replaces individual attributes and roles of the user's data in the request body.
   The PATCH API supports `add`, `remove`, and `replace` operations on any individual
   attribute or role allowing only specific attributes of the user's object to be modified.

2. Each operation against an attribute must be compatible with the attribute's mutability.

3. Each PATCH operation represents a single action to be applied to the
   same SCIM resource specified by the request URI.  Operations are
   applied sequentially in the order they appear in the array.  Each
   operation in the sequence is applied to the target resource; the
   resulting resource becomes the target of the next operation.
   Evaluation continues until all operations are successfully applied or
   until an error condition is encountered.

<br/>

**Add operations**:

The `add` operation adds a new attribute value to an existing resource.
The operation must contain a `value` member whose content specifies the value to be added.
The value may be a quoted value, or it may be a JSON object containing the sub-attributes of the complex attribute specified in the operation's `path`.
The result of the add operation depends upon the target `path` reference locations:

<br/>

- If omitted, the target location is assumed to be the resource itself.  The `value` parameter contains a set of attributes to be added to the resource.

- If the target location does not exist, the attribute and value are added.

- If the target location specifies a complex attribute, a set of sub-attributes shall be specified in the `value` parameter.

- If the target location specifies a multi-valued attribute, a new value is added to the attribute.

- If the target location specifies a single-valued attribute, the existing value is replaced.

- If the target location specifies an attribute that does not exist (has no value), the attribute is added with the new value.

- If the target location exists, the value is replaced.

- If the target location already contains the value specified, no changes should be made to the resource.

<br/>

**Replace operations**:

The `replace` operation replaces the value at the target location specified by the `path`.
The operation performs the following functions, depending on the target location specified by `path`:

<br/>

- If the `path` parameter is omitted, the target is assumed to be the resource itself.  In this case, the `value` attribute shall contain a list of one or more attributes to be replaced.

- If the target location is a single-value attribute, the value of the attribute is replaced.

- If the target location is a multi-valued attribute and no filter is specified, the attribute and all values are replaced.

- If the target location path specifies an attribute that does not exist, the service provider shall treat the operation as an "add".

- If the target location specifies a complex attribute, a set of sub-attributes SHALL be specified in the `value` parameter, which replaces any existing values or adds where an attribute did not previously exist.  Sub-attributes not specified in the `value` parameters are left unchanged.

- If the target location is a multi-valued attribute and a value selection ("valuePath") filter is specified that matches one or more values of the multi-valued attribute, then all matching record values will be replaced.

- If the target location is a complex multi-valued attribute with a value selection filter ("valuePath") and a specific sub-attribute (e.g., "addresses[type eq "work"].streetAddress"), the matching sub-attribute of all matching records is replaced.

- If the target location is a multi-valued attribute for which a value selection filter ("valuePath") has been supplied and no record match was made, the service provider will return failure as HTTP status code 400 and a `scimType` error code of "noTarget".

<br/>

**Remove operations**:

The `remove` operation removes the value at the target location specified by the required attribute `path`.  The operation performs the following functions, depending on the target location specified by `path`:

<br/>

- If `path` is unspecified, the operation fails with HTTP status code 400 and a "scimType" error code of "noTarget".

- If the target location is a single-value attribute, the attribute and its associated value is removed, and the attribute will be considered unassigned.

- If the target location is a multi-valued attribute and no filter is specified, the attribute and all values are removed, and the attribute SHALL be considered unassigned.

- If the target location is a multi-valued attribute and a complex filter is specified comparing a `value`, the values matched by the filter are removed.  If no other values remain after the removal of the selected values, the multi-valued attribute will be considered unassigned.

- If the target location is a complex multi-valued attribute and a complex filter is specified based on the attribute's sub-attributes, the matching records are removed.  Sub-attributes whose values have been removed will be considered unassigned.  If the complex multi-valued attribute has no remaining records, the attribute will be considered unassigned.

 The following roles cannot be assigned to a user:

1. Location Admin

2. Webex Site Admin 

<br/>

**NOTE**:

Once a user's role or managed roles are changed, all tokens associated with that user will be invalidated.

## Parámetros
- `orgId` [path] (string) (**requerido**): Webex Identity assigned organization identifier for user's organization.
- `userId` [path] (string) (**requerido**): Webex Identity assigned user identifier.

## Cuerpo de la petición (application/json)
- `schemas` (array) (**requerido**): Input JSON schemas.
- `Operations` (array) (**requerido**): A list of patch operations.
  - `op` (string) (**requerido**): The operation to perform. Valores: add, replace, remove.
  - `path` (string): A string containing an attribute path describing the target of the operation.
  - `value` (array): New value.
    - `value` (string): CI Role
    - `type` (string): name
    - `display` (string): A human-readable name, primarily used for display purposes.

### Ejemplo — petición
```json
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations": [
    {
      "op": "add",
      "path": "roles",
      "value": [
        {
          "value": "id_user_admin",
          "type": "cirole",
          "display": "Full Administrator."
        }
      ]
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X PATCH '/identity/scim/<orgId>/v2/Users/<userId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"schemas": [], "Operations": []}'
```

## Respuestas correctas
**200**: OK
- `schemas` (array) (**requerido**): Input JSON schemas.
- `id` (string) (**requerido**): Webex Identity assigned user identifier.
- `userName` (string) (**requerido**): A unique identifier for the user and authenticates the user in Webex.  This must be set to the user's primary email address.  No other user in Webex may have the same `userName` value and thus this value is required to be unique within Webex.
- `active` (boolean): A boolean value of "true" or "false" indicating whether the user is allowed to login in Webex.
- `roles` (array): List of roles assigned to the user.
  - `value` (string): CI Role
  - `type` (string): name
  - `display` (string): A human-readable name, primarily used for display purposes.
- `name` (object): The components of the user's real name.
  - `givenName` (string): The given name of the user, or first name in most Western languages (e.g., "Sarah" given the full name "Ms. Sarah J Henderson, III").
  - `familyName` (string): The family name of the user, or last name in most Western languages (e.g., "Henderson" given the full name "Ms. Sarah J Henderson, III").
  - `middleName` (string): The middle name(s) of the user (e.g., "Jane" given the full name "Ms. Sarah J Henderson, III").
  - `honorificPrefix` (string): The honorific prefix(es) of the user, or title in most Western languages (e.g., "Ms." given the full name "Ms. Sarah J Henderson, III").
  - `honorificSuffix` (string): The honorific suffix(es) of the user, or suffix in most Western languages (e.g., "III" given the full name "Ms. Sarah J Henderson, III").
- `displayName` (string): The name displayed for the user in Webex.
- `nickName` (string): A casual name of the user. For example, Bob when the user's formal name is Robert.
- `emails` (array): A list of the user's email addresses, including primary and alternative emails. The primary work email address must match the value of the user's username.
  - `value` (string): The email address.
  - `type` (string): The type of the email. Valores: work, home, room, other.
  - `display` (string): A human-readable description, primarily used for display purposes.
  - `primary` (boolean): Email status boolean value. If the type is work and primary is true, the value must equal `userName`.
- `userType` (string) (**requerido**):  Valores: user, room, external_calling, calling_service.
- `profileUrl` (string): A fully qualified URL pointing to a page representing the user's online profile.
- `title` (string): The user's business title.  Examples of a title is "Business Manager". "Senior Accountant", "Engineer" etc.
- `preferredLanguage` (string): User's preferred language. Acceptable values for this field are based on the [ISO-696](http://www.loc.gov/standards/iso639-2/php/code_list.php) and [ISO-3166](https://www.iso.org/obp/ui/#search) with the 2 letter language code followed by an _ and then the 2 letter country code.  Examples are:                                      en_US : for United States English or fr_FR for Parisian French.
- `locale` (string): The user's locale which represents the user's currency, time format, and numerical representations.  Acceptable values for this field are based on the [ISO-696](http://www.loc.gov/standards/iso639-2/php/code_list.php) and [ISO-3166](https://www.iso.org/obp/ui/#search) with the 2 letter language code followed by an _ and then the 2 letter country code.  Examples are:                           en_US : for United States English or fr_FR for Parisian French.
- `externalId` (string): User identifier provided by an external provisioning source.
- `timezone` (string): The user's time zone specified in the [IANA timezone](https://nodatime.org/timezones) timezone format, for example, "America/Los_Angeles".
- `phoneNumbers` (array): A list of user's phone numbers.
  - `value` (string): phone number.
  - `type` (string): We support the following phone number types: 'mobile', 'work', 'fax', 'work_extension', 'alternate1', 'alternate2'.  Alternate 1 and Alternate 2 are types inherited from Webex meeting sites. Valores: work, home, mobile, work_extension, fax, pager, other.
  - `display` (string): A human-readable name, primarily used for display purposes.
  - `primary` (boolean): A Boolean value for phone number's primary status.
- `photos` (array): A list of photo objects for the user.
  - `value` (string): photo link.
  - `type` (string): The type of the photo Valores: photo, thumbnail, resizable.
  - `display` (string): A human-readable description, primarily used for display purposes.
  - `primary` (boolean): A Boolean value for the photo usage status.
- `addresses` (array): User's physical mailing address.
  - `type` (string): The type of the address.
  - `streetAddress` (string): The full street address component, which may include house number, street name, P.O. box, and multi-line extended street address information. This attribute MAY contain newlines.
  - `locality` (string): The city or locality component.
  - `region` (string): The state or region component.
  - `postalCode` (string): The zip code or postal code component.
  - `country` (string): The country name component.
- `urn:ietf:params:scim:schemas:extension:enterprise:2.0:User` (object): SCIM2 enterprise extension
  - `costCenter` (string): Name of a cost center.
  - `organization` (string): Name of an organization.
  - `division` (string): Name of a division.
  - `department` (string): Name of a department.
  - `employeeNumber` (string): Numeric or alphanumeric identifier assigned to a person, typically based on the order of hire or association with an organization.
  - `manager` (object): The user's manager.
    - `value` (string) (**requerido**): Webex Identity assigned user identifier of the user's manager. The manager must belong to the same org as the user.
    - `displayName` (string): The name displayed for the manager in Webex.
    - `$ref` (string): The URI corresponding to a SCIM user that is the manager.
- `urn:scim:schemas:extension:cisco:webexidentity:2.0:User` (object): The Cisco extension of SCIM 2.
  - `accountStatus` (string) (**requerido**): An array of additional information about a user's status. Valores: active, pending, transient, disabled, fraud, fraud_transient, compliance_transient, pending_transient.
  - `sipAddresses` (array): `sipAddress` values for the user.
    - `value` (string) (**requerido**): The `sipAddress` value.
    - `type` (string): `sipAddress` type. Valores: enterprise.

### Ejemplo — respuesta 200
```json
{
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User",
    "urn:scim:schemas:extension:cisco:webexidentity:2.0:User",
    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
  ],
  "id": "3426a8e3-d414-4bf0-a493-4f6787632a13",
  "userName": "user1Changed@example.com",
  "active": true,
  "roles": [
    {
      "value": "id_full_admin",
      "type": "cirole",
      "display": "Full administrator"
    }
  ],
  "name": {
    "familyName": "Joestar",
    "givenName": "Jonathan",
    "middleName": "Jane",
    "honorificPrefix": "Mr.",
    "honorificSuffix": "III"
  },
  "displayName": "new displayName value",
  "nickName": "JoJo",
  "emails": [
    {
      "value": "user1@example.home.com",
      "type": "home",
      "display": "home email description"
    },
    {
      "value": "user1Changed@example.com",
      "type": "work",
      "primary": true
    }
  ],
  "userType": "user",
  "profileUrl": "https://jojowiki.com/Jonathan_Joestar",
  "title": "Sales manager",
  "preferredLanguage": "en_US",
  "locale": "en_US",
  "externalId": "externalIdNewValue",
  "timezone": "America/Los_Angeles",
  "phoneNumbers": [
    {
      "value": "400 123 1234",
      "type": "work",
      "primary": true,
      "display": "work phone number"
    }
  ],
  "photos": [
    {
      "value": "https://photos.example.com/profilephoto/72930000000Ccne/F",
      "type": "photo",
      "primary": true,
      "display": "photo description"
    }
  ],
  "addresses": [
    {
      "typ
  ... (truncado)
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