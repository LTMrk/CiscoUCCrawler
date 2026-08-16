---
doc_id: webex-admin-get-identity-organizations-orgid
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: GET
path: /identity/organizations/{orgId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.148690+00:00
---

# GET /identity/organizations/{orgId}

**API:** Webex Admin
**Área:** Identity Organization
**operationId:** `Get an organization`

## Resumen
Get an organization

## Descripción
<br/>

**Authorization**

OAuth token rendered by identity broker.

<br/>

One of the following OAuth scopes is required:

- `identity:organizations_rw`

- `identity:organizations_read`

<br/>

## Parámetros
- `orgId` [path] (string) **(requerido)**: Webex Identity assigned organization identifier.

## Respuestas
- **200**: OK
  - `schemas` (array) **(requerido)**: Output JSON schemas.
  - `id` (string) **(requerido)**: Webex Identity assigned organization identifier.
  - `displayName` (string) **(requerido)**: Full name of the organization.
  - `preferredLanguage` (string): It is the default preferredLanguage for user creation in this org. It is set in ISO639 format.
  - `meta` (object):
    - `created` (string) **(requerido)**: The date and time the organization was created.
    - `lastModified` (string) **(requerido)**: The last modification time of the organization.
    - `version` (string) **(requerido)**: The version information of the organization.
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
