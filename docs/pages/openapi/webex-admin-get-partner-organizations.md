---
doc_id: webex-admin-get-partner-organizations
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /partner/organizations
operation_id: Get all customers managed by a partner admin
tags: Partner Administrators
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.570304+00:00
---

# GET /partner/organizations

**API:** Webex Admin
**Área:** Partner Administrators
**operationId:** `Get all customers managed by a partner admin`

## Resumen
Get all customers managed by a partner admin

## Descripción
Get all customer organizations managed by given partner admin, in the `managedBy` request parameter. The `managedBy` user typically has the role of a Partner Admin. In case where a Partner Full Admin or Partner Read-Only admin is selected an error like "The user already has access to all customers managed by their partner organization." is shown as a Partner Admin (Full and Read-Only) is able to manage all customers by default. This does not include customers managed through Customer Groups.

This API can be invoked by Partner Full Admin and Partner Readonly Admin.
Specify the `personId` in the `managedBy` parameter in the URI.

## Parámetros
- `managedBy` [query] (string) (**requerido**): List customer orgs associated with this person ID.

## Ejemplo de invocación
```bash
curl -X GET '/partner/organizations?managedBy=<managedBy>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): An array of managed orgs objects.
  - `orgId` (string): The org ID of the managed org.
  - `role` (string): role ID of the user to this org.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "orgId": "Y2LZY29ZCGFYAZOVL3VZL1BFT1BMRS9MNWIZNJE4NY1JOGRKLTQ3MJCTOGIYZI1MOWM0NDDMMJKWNDY",
      "role": "YXRSYXMTCG9YDGFSLNBHCNRUZXIUC2FSZXNMDWXSYWRTAW4="
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