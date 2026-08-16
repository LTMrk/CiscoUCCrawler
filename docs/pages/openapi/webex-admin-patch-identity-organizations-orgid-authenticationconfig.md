---
doc_id: webex-admin-patch-identity-organizations-orgid-authenticationconfig
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: PATCH
path: /identity/organizations/{orgId}/authenticationConfig
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.148949+00:00
---

# PATCH /identity/organizations/{orgId}/authenticationConfig

**API:** Webex Admin
**Área:** Identity Organization
**operationId:** `Update Organization Authentication Configuration Settings`

## Resumen
Update Organization Authentication Configuration Settings

## Descripción
Update the authentication configuration details, by organizationID.
Specify the organization ID in the `orgId` parameter in the URI.

<br/>

**Authorization**

OAuth token rendered by identity broker.

<br/>

One of the following OAuth scopes is required:

- `identity:organizations_rw`

<br/>

The following administrators can use this API:

- `id_full_admin`

<br/>

**Usage**:

1. Input JSON must contain schema: "urn:cisco:codev:identity:idbroker:authnconfig:schemas:1.0".

## Parámetros
- `orgId` [path] (string) **(requerido)**: A unique identifier for the org.

## Cuerpo de la petición (application/json)
- `schemas` (array) **(requerido)**: Input JSON schemas. It should contain the following schema:   urn:cisco:codev:identity:idbroker:authnconfig:schemas:1.0
- `RememberMyLoginId` (boolean): Login Id set to true if it should be remembered.
- `RememberMyLoginIdDuration` (number): Specifies the number of days the user's login ID is remembered. Must be between 1 and 120 (inclusive).
- `mfaEnabled` (boolean): Enable/ Disable multi-factor authentication on an organization.

### Ejemplo de petición
```json
{
  "schemas": [
    "urn:cisco:codev:identity:idbroker:authnconfig:schemas:1.0"
  ],
  "RememberMyLoginId": true,
  "RememberMyLoginIdDuration": 30,
  "mfaEnabled": true
}
```

## Respuestas
- **200**: OK
  - `schemas` (array): Output JSON schemas.
  - `LockoutDuration` (number): The number of minutes that an account will be locked out.
  - `LockoutDurationMultiplier` (number): The multiplier of the LockoutDuration. Each subsequent lockout will be multiplied by this value.
  - `LockoutFailureCount` (number): Number of failed login attempts that will trigger account lockout.
  - `LockoutFailureDuration` (number): Number of minutes that a login failure will be recorded.
  - `RememberMyLoginId` (boolean): True to remember the user's Login Id.
  - `mfaEnabled` (boolean): True, if multi factor authentication is enabled on an organization.
  - `RememberMyLoginIdDuration` (number): Specifies the number of days the user's login ID is remembered. Must be between 1 and 120 (inclusive).
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
