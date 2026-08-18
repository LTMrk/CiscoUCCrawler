---
doc_id: webex-admin-post-partner-tags-organizations-orgid-assigntags
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: POST
path: /partner/tags/organizations/{orgId}/assignTags
operation_id: Create or Replace existing customer tags with the provided ones
tags: Partner Tags
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.590496+00:00
---

# POST /partner/tags/organizations/{orgId}/assignTags

**API:** Webex Admin
**Área:** Partner Tags
**operationId:** `Create or Replace existing customer tags with the provided ones`

## Resumen
Create or Replace existing customer tags with the provided ones

## Descripción
Assign or replace tag(s) which for a customer organization. If the tag doesn't already exist, a new one is created and assigned to the customer automatically.
This API can be used by partner full admins and partner admins. 
Each tag has a character limit of 25. Currently, there is a limit of 5 tags per organization when creating tags. To remove all the tags, pass an empty array.
Specify the customer organization ID in the `orgId` parameter in the URI.

## Parámetros
- `orgId` [path] (string) (**requerido**): The unique identifier for the customer organization.

## Cuerpo de la petición (application/json)
- `tags` (array): An array of tags.
  - `name` (string) (**requerido**): Name of the tag.
  - `description` (string): Description of the tag

## Ejemplo de invocación
```bash
curl -X POST '/partner/tags/organizations/<orgId>/assignTags' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- (array de:)
  - `name` (string) (**requerido**): Name of the tag.
  - `description` (string): Description of the tag

### Ejemplo — respuesta 200
```json
[
  {
    "name": "Tag name",
    "description": "Tag description"
  }
]
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