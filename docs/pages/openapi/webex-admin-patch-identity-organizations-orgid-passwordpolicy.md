---
doc_id: webex-admin-patch-identity-organizations-orgid-passwordpolicy
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: PATCH
path: /identity/organizations/{orgId}/passwordPolicy
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.149100+00:00
---

# PATCH /identity/organizations/{orgId}/passwordPolicy

**API:** Webex Admin
**Área:** Identity Organization
**operationId:** `Update Organization Password Policy`

## Resumen
Update Organization Password Policy

## Descripción
Update Organization Password Policy, by organizationID.
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

1. Input JSON must contain schema: "urn:cisco:codev:identity:idbroker:pwdpolicy:schemas:1.0".

## Parámetros
- `orgId` [path] (string) **(requerido)**: A unique identifier for the org.

## Cuerpo de la petición (application/json)
- `schemas` (array) **(requerido)**: Input JSON schemas. It should contain the following schema:   urn:cisco:codev:identity:idbroker:pwdpolicy:schemas:1.0
- `minimumNumeric` (string) **(requerido)**: Minimum number of numeric characters in password
- `minimumCapAlpha` (string) **(requerido)**: Minimum number of uppercase alphabetic character letters in password
- `minimumLowAlpha` (string) **(requerido)**: Minimum number of lowercase alphabetic character letters in password
- `minimumSpecial` (string) **(requerido)**: Minimum number of special characters included "~!@#$%^&*()-_=+[]{}|;:,.<>/?" in password
- `minimumLength` (string) **(requerido)**: Minimum length of password. Must be between 8 and 256, inclusive.
- `historyCount` (string) **(requerido)**: The number of former passwords in history, the new password can't be any one of them. Must be between 1 and 5, inclusive.
- `maxPasswordAge` (string) **(requerido)**: The password expired time, unit: day, that means user need to change password every "X" days. Must be between 90 and 1825, inclusive.
- `notAcceptableStrings` (string): The password can not be any one in this string list.

### Ejemplo de petición
```json
{
  "schemas": [
    "urn:cisco:codev:identity:idbroker:pwdpolicy:schemas:1.0"
  ],
  "minimumNumeric": "1",
  "minimumCapAlpha": "1",
  "minimumLowAlpha": "1",
  "minimumSpecial": "1",
  "minimumLength": "8",
  "historyCount": "3",
  "maxPasswordAge": "1825",
  "notAcceptableStrings": "password,passwd,pass,webex,cisco,xebew,ocsic"
}
```

## Respuestas
- **200**: OK
  - `minimumNumeric` (string): Minimum number of numeric characters in password.
  - `minimumCapAlpha` (string): Minimum number of uppercase alphabetic character letters in a password.
  - `minimumLowAlpha` (string): Minimum number of lowercase alphabetic character letters in a password.
  - `minimumSpecial` (string): Minimum number of special character included "~!@#$%^&*()-_=+[]{}|;:,.<>/?" in a password.
  - `minimumLength` (string): Minimum length of password. Must be between 8 and 256, inclusive.
  - `historyCount` (string): The number of former password in history, the new password can't be any one of them. Must be between 1 and 5, inclusive.
  - `maxPasswordAge` (string): The password expired time, unit: day, that means user need to change password every "X" days. Must be between 90 and 1825, inclusive.
  - `notAcceptableStrings` (string): The password can not be any one in this string list.
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
