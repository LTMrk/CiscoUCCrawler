---
doc_id: webex-admin-get-schemas-scim2-user
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: GET
path: /Schemas/SCIM2/User
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.160760+00:00
---

# GET /Schemas/SCIM2/User

**API:** Webex Admin
**Área:** SCIM 2 Schemas
**operationId:** `Get User Schema`

## Resumen
Get User Schema

## Descripción
This API allows the service client to get all the `User` schemas information from CI.

**Authorization:**

OAuth token rendered by Identity Broker.

One of the following OAuth scopes is required:

- `identity:people_rw`

- `identity:organizations_rw`

The following administrators can use this API:

- `id_full_admin`

- `id_user_admin`

- `id_readonly_admin`

- `id_device_admin`

## Respuestas
- **200**: OK
  - `urn:scim:schemas:extension:cisco:webexidentity:2.0:User` (object): The Cisco extension of SCIM 2.
    - `id` (string) **(requerido)**: A unique identifier for the user.
    - `name` (string) **(requerido)**: The name of the user.
    - `description` (string) **(requerido)**: Description of the user.
    - `attributes` (array): A list of attributes of this user.
      - `name` (string): The name of the user.
      - `type` (string): The type of the user.
      - `referenceTypes` (string) **(requerido)**: * `external` - Represents a reference to entities or resources that exist outside the current system or organization.  * `Group` - Refers to a reference type that identifies a collection of users or entities within a system.  * `User` - Denotes a reference to an individual who interacts with the system.  * `Machine` - Indicates a reference to a computing device or automated system. Valores: external, Group, User, Machine.
      - `multiValued` (boolean): A boolean value for the user.
      - `description` (string): Description of the user.
      - `required` (boolean): A boolean value for the user.
      - `caseExact` (boolean): A boolean value for the user.
      - `mutability` (string): Mutability of the user.
      - `returned` (string): Returned value of the user.
      - `canonicalValues` (array): A list of canonical values of this user.
      - `uniqueness` (string): Uniqueness of the user.
      - `subAttributes` (array): A list of sub-attributes of this user.
        - `name` (string): The name of the group.
        - `type` (string): The type of the group.
        - `referenceTypes` (array): An array of additional information about reference types of the group.
        - `multiValued` (boolean): A boolean value for the group.
        - `description` (string): Description of the group.
        - `required` (boolean): A boolean value for the group.
        - `caseExact` (boolean): A boolean value for the group.
        - `mutability` (string): Mutability of the group.
        - `returned` (string): Returned value of the group.
        - `uniqueness` (string): Uniqueness of the group.
        - `canonicalValues` (array): A list of canonical values of this group.
      - `size` (number): This refers to the measurement or magnitude of an object, entity, or dataset, quantified as 50.
      - `length` (number): This describes the extent or measurement of something from end to end, quantified as 128.
  - `urn:ietf:params:scim:schemas:core:2.0:User` (object): The core extension of SCIM 2.
    - `id` (string) **(requerido)**: A unique identifier for the user.
    - `name` (string) **(requerido)**: The name of the user.
    - `description` (string) **(requerido)**: Description of the user.
    - `attributes` (array): A list of attributes of this user.
      - `name` (string): The name of the user.
      - `type` (string): The type of the user.
      - `referenceTypes` (string) **(requerido)**: * `external` - Represents a reference to entities or resources that exist outside the current system or organization.  * `Group` - Refers to a reference type that identifies a collection of users or entities within a system.  * `User` - Denotes a reference to an individual who interacts with the system.  * `Machine` - Indicates a reference to a computing device or automated system. Valores: external, Group, User, Machine.
      - `multiValued` (boolean): A boolean value for the user.
      - `description` (string): Description of the user.
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
