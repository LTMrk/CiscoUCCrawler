---
doc_id: webex-admin-post-identity-organizations-orgid-actions-unclaimdomain
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: POST
path: /identity/organizations/{orgId}/actions/unclaimDomain
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.148585+00:00
---

# POST /identity/organizations/{orgId}/actions/unclaimDomain

**API:** Webex Admin
**Área:** API - Domain Management
**operationId:** `Unclaim Domain`

## Resumen
Unclaim Domain

## Descripción
This API is used to unclaim a domain for the organization. The domain will remain verified, and domain enforcement will still apply to the given organization.

**Possible Error:**

- 400: The request was a Bad Request. The domain cannot be unclaimed. This error occurs if the requested parameter is invalid.

**Authorization:**

An 'OAuth' token issued by the 'Identity Broker' is required to access this endpoint. The token must include one of the following scopes:

- `Identity:Organization`

- `identity:organizations_rw`

**Administrator Roles:**

The following administrators can use this API:

- `id_full_admin`

## Parámetros
- `orgId` [path] (string) **(requerido)**: The Webex Identity-assigned organization identifier for a user's organization.

## Cuerpo de la petición (application/json)
- `domain` (string) **(requerido)**: A claimed domain.

### Ejemplo de petición
```json
{
  "domain": "test.dc-01.com"
}
```

## Respuestas
- **204**: No Content
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
