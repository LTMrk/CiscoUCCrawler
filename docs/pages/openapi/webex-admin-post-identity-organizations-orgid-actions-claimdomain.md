---
doc_id: webex-admin-post-identity-organizations-orgid-actions-claimdomain
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: POST
path: /identity/organizations/{orgId}/actions/claimDomain
operation_id: Claim Domain
tags: API - Domain Management
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.561792+00:00
---

# POST /identity/organizations/{orgId}/actions/claimDomain

**API:** Webex Admin
**Área:** API - Domain Management
**operationId:** `Claim Domain`

## Resumen
Claim Domain

## Descripción
This endpoint helps claim the given domain within the specified organization. The domain needs to be verified before it can be claimed.

**Note**
<callout type="warning">

There's an organization-level boolean flag called 'enforceVerifiedDomains'. If this flag is set to false, we won't put any user in the organization into a transient state when verifying or claiming a domain.
Customers can still create users within the organization who don't use the verified domains as their email. However, if the flag is set to true, all users in the organization must use one of the verified domains as their email.
This flag defines whether the organization enforces user email verification within the organization. If set to true, all users inside the organization must use one of the verified domains.
This flag is effective only after the admin has verified at least one email domain.
</callout>

**Possible Error:**

- 400: The request was a Bad Request. This error occurs if the domain is not verified.

**Authorization:**

An 'OAuth' token issued by the 'Identity Broker' is required to access this endpoint. The token must include one of the following scopes:

- `Identity:Organization`

- `identity:organizations_rw`

**Administrator Roles:**

The following administrators can use this API:

- `id_full_admin`

## Parámetros
- `orgId` [path] (string) (**requerido**): The Webex Identity-assigned organization identifier for a user's organization.

## Cuerpo de la petición (application/json)
- `data` (array): A List of valid domain name that is already verified by the organization.
  - `domain` (string) (**requerido**): A valid domain name that is already verified by the organization.
- `forceDomainClaim` (boolean): Indicate if the domain should be claimed when there are users outside the organization using the same domain. The default is true.
- `claimDomainOnly` (boolean): Indicate to just claim the domain only without searching/marking external users as transient. The default is false.

### Ejemplo — petición
```json
{
  "data": [
    {
      "domain": "cisco.com"
    }
  ],
  "forceDomainClaim": true,
  "claimDomainOnly": false
}
```

## Ejemplo de invocación
```bash
curl -X POST '/identity/organizations/<orgId>/actions/claimDomain' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- `data` (array):
  - `domain` (string) (**requerido**): A list of verified domains for a given organizations.
  - `url` (string) (**requerido**): Use this location URL for the domain resource. The resource component of the URL will be the base64 encoded domain name.

### Ejemplo — respuesta 200
```json
{
  "data": [
    {
      "domain": "cisco.com",
      "url": "https://identity.webex.com/organizations/bf732c85-68ca-4867-94e4-937286ad2fd4/v1/domains/ZXhhbXBsZTMuY29t"
    }
  ]
}
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