---
doc_id: webex-admin-get-identity-scim-orgid-v2-users
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /identity/scim/{orgId}/v2/Users
operation_id: Search users
tags: SCIM 2 Users
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.586704+00:00
---

# GET /identity/scim/{orgId}/v2/Users

**API:** Webex Admin
**Área:** SCIM 2 Users
**operationId:** `Search users`

## Resumen
Search users

## Descripción
<br/>

**Authorization**

OAuth token rendered by Identity Broker.

<br/>

One of the following OAuth scopes is required:

- `identity:people_rw`

- `identity:people_read`

<br/>

The following administrators can use this API:

- `id_full_admin`

- `id_user_admin`

- `id_readonly_admin`

- `id_device_admin`

<br/>

## Parámetros
- `orgId` [path] (string) (**requerido**): Webex Identity assigned organization identifier for user's organization.
- `filter` [query] (string): The URL encoded filter. If the value is empty, the API will return all users under the organization.  The examples below show some search filters:  - `userName` eq "user1@example.com"  - `userName` sw "user1@example"  - `userName` ew "example"  - `phoneNumbers` [ type eq "mobile" and value eq "14170120"]  - `urn:scim:schemas:extension:cisco:webexidentity:2.0:User:meta.organizationId` eq "0ae87ade-8c8a-4952-af08-318798958d0c"  - For more filter patterns, please check [filtering](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2).  | **Attributes** | **Operators** | |-----|-----| | **SCIM Core** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | ---- | | `id` | eq | | `userName` | eq sw ew | | `name.familyName` | eq sw ew | | `name.givenName` | eq sw | | `name.middleName` | eq sw | | `name.formatted` | eq sw | | `displayName` | eq sw ew | | `nickName` | eq sw ew | | `emails.display` | eq sw ew | | `emails.value` | eq sw ew | | `phoneNumbers.value` | eq sw ew | | `phoneNumbers.display` | eq sw ew | | **Enterprise Extensions** | ---- | | `employeeNumber` | eq sw ew | | `costCenter` | eq sw ew | | `organization` | eq sw ew | | `division` | eq sw ew | | `department` | eq sw ew | | `manager.value` | eq | | `manager.displayName` | eq sw ew |
- `attributes` [query] (string): A multi-valued list of string names for resource attributes to return in the response, like 'userName,department,emails'. It supports the SCIM id 'urn:ietf:params:scim:schemas:extension:enterprise:2.0:User,userName'. The default is empty, all attributes will be returned
- `excludedAttributes` [query] (string): A multi-valued list of strings names for resource attributes to be removed from the default set of attributes to return. The default is empty, all attributes will be returned
- `sortBy` [query] (string): A string for the attribute whose value can be used to order the returned responses. Now we only allow `userName`, `id`, `meta.lastModified` to sort.
- `sortOrder` [query] (string): A string for the order in which the 'sortBy' parameter is applied. Allowed values are 'ascending' and 'descending'.
- `startIndex` [query] (string): An integer for the 1-based index of the first query result. The default is 1.
- `count` [query] (string): An integer for the maximum number of query results per page.  The default is 100.
- `returnGroups` [query] (string): Define whether the group information needs to be returned.  The default is false.
- `includeGroupDetails` [query] (string): Define whether the group information with details needs to be returned. The default is false.
- `groupUsageTypes` [query] (string): Returns groups with details of the specified group type.

## Ejemplo de invocación
```bash
curl -X GET '/identity/scim/<orgId>/v2/Users' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `schemas` (array) (**requerido**): Input JSON schemas.
- `totalResults` (number): Total number of users in search results.
- `itemsPerPage` (number): The total number of items in a paged result.
- `startIndex` (number): Start at the one-based offset in the list of matching users.
- `Resources` (array): A list of users with details.
  - `schemas` (array) (**requerido**): Input JSON schemas.
  - `id` (string) (**requerido**): Webex Identity assigned user identifier.
  - `userName` (string) (**requerido**): A unique identifier for the user and authenticates the user in Webex.  This must be set to the user's primary email address.  No other user in Webex may have the same `userName` value and thus is required to be unique within Webex.
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
  - `preferredLanguage` (string): User's preferred language. Acceptable values are based on the [ISO-696](http://www.loc.gov/standards/iso639-2/php/code_list.php) and [ISO-3166](https://www.iso.org/obp/ui/#search) with the 2 letter language code followed by an _ and then the 2 letter country code.  Examples are:                                      en_US : for United States English or fr_FR for Parisian French.
  - `locale` (string): The user's locale which represents the user's currency, time format, and numerical representations.  Acceptable values are based on the [ISO-696](http://www.loc.gov/standards/iso639-2/php/code_list.php) and [ISO-3166](https://www.iso.org/obp/ui/#search) with the 2 letter language code followed by an _ and then the 2 letter country code.  Examples are:                           en_US : for United States English or fr_FR for Parisian French.
  - `externalId` (string): User identifier provided by an external provisioning source.
  - `timezone` (string): The user's time zone specified in the [IANA timezone](https://nodatime.org/timezones) timezone format, for example, "America/Los_Angeles".
  - `phoneNumbers` (array): A list of user's phone numbers.
    - `value` (string): phone number.
    - `type` (string): We support the following phone number types: 'mobile', 'work', 'fax', 'work_extension', 'alternate1', 'alternate2'.  Alternate 1 and Alternate 2 are types inherited from Webex meeting sites. Valores: work, home, mobile, work_extension, fax, pager, other.
    - `display` (string): A human-readable name, primarily used for display purposes.
    - `primary` (boolean): A Boolean value for phone number's primary status.
  - `groups` (array): A list of group details returned only when `includeGroupDetails` or `returnGroups` request parameters are set to true.
    - `value` (string): A unique identifier for the group.
    - `display` (string): Display name of the group.
    - `$ref` (string): The URI corresponding to a group.
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