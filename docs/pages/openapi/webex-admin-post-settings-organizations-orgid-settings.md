---
doc_id: webex-admin-post-settings-organizations-orgid-settings
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: POST
path: /settings/organizations/{orgId}/settings
operation_id: Create or Update an Organization Setting
tags: Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.590112+00:00
---

# POST /settings/organizations/{orgId}/settings

**API:** Webex Admin
**Área:** Settings
**operationId:** `Create or Update an Organization Setting`

## Resumen
Create or Update an Organization Setting

## Descripción
This endpoint creates or updates the specified setting for the given organization; however, the 'name' of the setting cannot be modified. It is accessible with the scope 'identity:organizations_rw'.

## Parámetros
- `orgId` [path] (string) (**requerido**): The Webex organization id in Control Hub UUID or API orgId format.

## Cuerpo de la petición (application/json)
- `key` (string): Key of the setting.
- `value` (boolean): Value of the setting.

### Ejemplo — petición
```json
{
  "key": "allow-admin-invite-emails",
  "value": false
}
```

## Ejemplo de invocación
```bash
curl -X POST '/settings/organizations/<orgId>/settings' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- `key` (string): Key of the setting.
- `value` (boolean): Value of the setting.
- `name` (string): Name of the setting.

### Ejemplo — respuesta 200
```json
{
  "key": "allow-admin-invite-emails",
  "value": false,
  "name": "Automatic Activation Emails"
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