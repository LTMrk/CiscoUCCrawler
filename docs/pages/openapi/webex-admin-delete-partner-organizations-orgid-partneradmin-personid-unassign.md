---
doc_id: webex-admin-delete-partner-organizations-orgid-partneradmin-personid-unassign
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: DELETE
path: /partner/organizations/{orgId}/partnerAdmin/{personId}/unassign
operation_id: Unassign partner admin from a customer
tags: Partner Administrators
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.570718+00:00
---

# DELETE /partner/organizations/{orgId}/partnerAdmin/{personId}/unassign

**API:** Webex Admin
**Área:** Partner Administrators
**operationId:** `Unassign partner admin from a customer`

## Resumen
Unassign partner admin from a customer

## Descripción
Unassign a specific partner admin from a customer organization. Unassigning a customer organization from a partner admin does not remove the role from the user. If a partner admin is also managing the customer organization through a Customer Group, they will continue to have access.
This API can be used by Partner Full Admin.

Specify the `orgId` and the `personId` in the path param.

## Parámetros
- `orgId` [path] (string) (**requerido**): The ID of the customer organization.
- `personId` [path] (string) (**requerido**): User ID of the partner admin in the partners org.

## Ejemplo de invocación
```bash
curl -X DELETE '/partner/organizations/<orgId>/partnerAdmin/<personId>/unassign' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK

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