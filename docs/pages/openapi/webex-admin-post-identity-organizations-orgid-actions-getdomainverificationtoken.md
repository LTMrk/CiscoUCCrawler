---
doc_id: webex-admin-post-identity-organizations-orgid-actions-getdomainverificationtoken
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: POST
path: /identity/organizations/{orgId}/actions/getDomainVerificationToken
operation_id: Get Domain Verification Token
tags: API - Domain Management
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.561338+00:00
---

# POST /identity/organizations/{orgId}/actions/getDomainVerificationToken

**API:** Webex Admin
**Área:** API - Domain Management
**operationId:** `Get Domain Verification Token`

## Resumen
Get Domain Verification Token

## Descripción
This endpoint helps generate a token for a given domain within the specified organization. The user needs to add this token as a 'TXT' record to the DNS server.

**Possible Error:**

- 409: The request encountered a resource conflict. This error occurs if the domain is either claimed by another organization or by the same organization.

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
- `domain` (string) (**requerido**): A valid domain name.

### Ejemplo — petición
```json
{
  "domain": "cisco.com"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/identity/organizations/<orgId>/actions/getDomainVerificationToken' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"domain": "<domain>"}'
```

## Respuestas correctas
**200**: OK
- `domain` (string) (**requerido**): The domain name for which the token is generated.
- `token` (string) (**requerido**): A token needs to be added as a TXT record in your domain's DNS settings. You should add the following string: 'cisco-ci-domain-verification=<token>' as a TXT record in your DNS settings.
- `verificationMethod` (string) (**requerido**): Domain verification method: Currently, we only support the DNS_TXT method for domain verification.
- `url` (string) (**requerido**): Use this URL for retrieving an authentication token needed to interact with the Domain Verification API.

### Ejemplo — respuesta 200
```json
{
  "domain": "cisco.com",
  "token": "f5014515-6559-4a30-9d68-0deb028f27b7",
  "verificationMethod": "DNS_TXT",
  "url": "https://identity.webex.com/organization/bf732c85-68ca-4867-94e4-937286ad2fd4/v1/actions/DomainVerification/GetToken/invoke"
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