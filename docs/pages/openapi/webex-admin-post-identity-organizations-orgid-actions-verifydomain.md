---
doc_id: webex-admin-post-identity-organizations-orgid-actions-verifydomain
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: POST
path: /identity/organizations/{orgId}/actions/verifyDomain
operation_id: Verify Domain
tags: API - Domain Management
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.561598+00:00
---

# POST /identity/organizations/{orgId}/actions/verifyDomain

**API:** Webex Admin
**Área:** API - Domain Management
**operationId:** `Verify Domain`

## Resumen
Verify Domain

## Descripción
This endpoint helps verify a given domain within the specified organization. This API verifies domain ownership by looking up and validating the 'TXT' record for the domain.
Once verified, domain enforcement will be applied to the organization. Any users in the organization whose email domain doesn't match one of the verified domains will be marked as transient.

If you want to verify and claim the domain, just set the 'claimDomain' parameter to true. By default, it's set to false, which will only verify the domain.

**Possible Errors:**

- 400: The request was a Bad Request. The domain can't be verified. This error happens if the user didn't request a token before trying to verify the domain.

- 409: The request resulted in a resource conflict. This error occurs if the domain has already been claimed by another organization.

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
- `domain` (string) (**requerido**): The domain name to be verified.
- `claimDomain` (boolean): A boolean to specify whether the domain needs to be claimed. The default value is false. If false, the domain will be verified but not claimed.
- `reserveDomain` (boolean): For FedRAMP only: If true, add the domain to the FedRAMP reserved domain list. The default value is false.

### Ejemplo — petición
```json
{
  "domain": "cisco.com",
  "claimDomain": false,
  "reserveDomain": false
}
```

## Ejemplo de invocación
```bash
curl -X POST '/identity/organizations/<orgId>/actions/verifyDomain' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"domain": "<domain>"}'
```

## Respuestas correctas
**200**: OK
- `verifiedDomains` (array) (**requerido**): A list of verified domains for a given organization.
- `claimedDomains` (array) (**requerido**): A list of claimed domains for a given organization.
- `url` (string) (**requerido**): Use this URL for verifying domain ownership and managing the domain lifecycle within the organization.

### Ejemplo — respuesta 200
```json
{
  "verifiedDomains": [
    "cisco.com",
    "webex.com"
  ],
  "claimedDomains": [
    "cisco.com",
    "webex.com"
  ],
  "url": "https://identity.webex.com/organization/bf732c85-68ca-4867-94e4-937286ad2fd4/v1/actions/DomainVerification/Verify/invoke"
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