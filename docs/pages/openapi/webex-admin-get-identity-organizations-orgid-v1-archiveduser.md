---
doc_id: webex-admin-get-identity-organizations-orgid-v1-archiveduser
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /identity/organizations/{orgId}/v1/ArchivedUser
operation_id: queryArchiveUser
tags: Archive Users
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.561130+00:00
---

# GET /identity/organizations/{orgId}/v1/ArchivedUser

**API:** Webex Admin
**Área:** Archive Users
**operationId:** `queryArchiveUser`

## Resumen
Query Archive User

## Descripción
Retrieves archived user information for the specified organization. Supported attributes are `id`, which is the unique identifier of a user in the system, and `username`. It is assigned when the user is created and can be retrieved through **GET Users** API.<br/>

**Authorization**

OAuth token issued by the Identity Broker.

One of the following OAuth scopes is required:

- `identity:people_rw`.
- `identity:people_read`.

The following administrators can use this API:

- `Account in the specified organization with one of the following roles: id_full_admin, id_user_admin, id_readonly_admin`.
- `Proxy account managing the specified organization with one of the following roles: id_full_admin, id_user_admin, id_readonly_admin`.

<br/>

## Parámetros
- `orgId` [path] (string) (**requerido**): The unique identifier for the organization.
- `filter` [query] (string) (**requerido**): A SCIM-style filter expression used to search archived users. Supported attributes are `username` and `id`, and only the `eq` operator is supported.  Examples:  - `username eq "test_user_1@example.com"` - `id eq "40929cc6-2df2-4ab5-871c-ec8e38f07b93"`

## Ejemplo de invocación
```bash
curl -X GET '/identity/organizations/<orgId>/v1/ArchivedUser?filter=<filter>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `totalResults` (integer): Total number of archived user that match the query.
- `schemas` (array): An array of schema URNs that define the structure of the SCIM resource.
- `Resources` (array): A list of archived users matching the filter.
  - `userName` (string) (**requerido**): The unique identifier for the user. This must be set to the user's primary email address. The `userName` value must be unique across Webex and is used for authentication.
  - `emails` (array) (**requerido**): A list of the user's email addresses.
    - `value` (string): The email address.
    - `type` (string): The type of the email. Valores: work, home, room, other.
    - `display` (string): A human-readable description, primarily used for display purposes.
    - `primary` (boolean): Email status boolean value. If the type is work and primary is true, the value must equal `userName`.
  - `name` (object) (**requerido**): The components of the user's real name.
    - `givenName` (string): The given name of the user, or first name in most Western languages (e.g., "Sarah" given the full name "Ms. Sarah J Henderson, III").
    - `familyName` (string): The family name of the user, or last name in most Western languages (e.g., "Henderson" given the full name "Ms. Sarah J Henderson, III").
    - `middleName` (string): The middle name(s) of the user (e.g., "Jane" given the full name "Ms. Sarah J Henderson, III").
    - `honorificPrefix` (string): The honorific prefix(es) of the user, or title in most Western languages (e.g., "Ms." given the full name "Ms. Sarah J Henderson, III").
    - `honorificSuffix` (string): The honorific suffix(es) of the user, or suffix in most Western languages (e.g., "III" given the full name "Ms. Sarah J Henderson, III").
  - `organization` (string) (**requerido**): The unique identifier for the organization.
  - `id` (string) (**requerido**): The unique identifier for the user.
  - `displayName` (string): The display name of the user in Webex.
  - `meta` (object) (**requerido**): Response metadata.
    - `resourceType` (string):
    - `organizationID` (string):
    - `created` (string) (**requerido**): The date and time the group was created.
    - `lastModified` (string) (**requerido**): The date and time the group was last changed.
    - `version` (string) (**requerido**): The version of the user.
    - `location` (string) (**requerido**): The resource itself.

### Ejemplo — respuesta 200
```json
{
  "totalResults": "1",
  "schemas": [
    "urn:scim:schemas:core:1.0",
    "urn:scim:schemas:extension:cisco:commonidentity:1.0"
  ],
  "Resources": [
    {
      "userName": "test_user2@example.com",
      "emails": [
        {
          "primary": true,
          "type": "work",
          "value": "test_user2@example.com"
        }
      ],
      "name": {
        "givenName": "Mike",
        "familyName": "Tang"
      },
      "organization": "410139c6-3bff-4404-9782-09a456ba2cae",
      "id": "b96936c9-5b86-4a01-8969-e945c91b62f6",
      "meta": {
        "created": "2019-01-25T00:53:13.000Z",
        "lastModified": "2019-01-25T00:53:13.000Z",
        "location": "https://webexapis.com/identity/scim/410139c6-3bff-4404-9782-09a456ba2cae/v1/UserArchives/b96936c9-5b86-4a01-8969-e945c91b62f6",
        "deleted": "2019-01-25T00:53:13.001Z"
      },
      "displayName": "Mike Tang"
    }
  ]
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be processed. An accompanying error message explains the issue.
- **401**: Unauthorized: Authentication credentials were missing or invalid.
- **403**: Forbidden: The request was understood but access is denied.
- **404**: Not Found: The requested URI is invalid, or the resource (such as a user) does not exist. Also returned when the requested format is not supported for the method.
- **405**: Method Not Allowed: The request was made using an unsupported HTTP method.
- **409**: Conflict: The request could not be processed because it conflicts with an existing system rule. For example, a person may not be added to a room more than once.
- **410**: Gone: The requested resource is no longer available.
- **415**: Unsupported Media Type: The request was made without specifying a media type or used a media type that is not supported.
- **423**: Locked: The requested resource is temporarily unavailable. A Retry-After header may indicate how many seconds to wait before retrying.
- **428**: Precondition Required: File(s) cannot be scanned for malware and must be force-downloaded.
- **429**: Too Many Requests: Too many requests have been sent in a given time and the request has been rate limited. A Retry-After header indicates how many seconds to wait before retrying.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server. Try again later.
- **503**: Service Unavailable: The server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

## Contexto de la API
The Webex Admin APIs provide comprehensive programmatic access to administrative functions for managing Webex organizations, users, licenses, and settings. These APIs enable automation of user provisioning, license assignment, compliance management, and audit event retrieval. Administrators can integrate with enterprise identity systems, enforce security policies, monitor usage, and streamline onboarding/offboarding processes. The APIs support granular control over organizational resources, making them ideal for large-scale deployments and custom admin tooling.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs