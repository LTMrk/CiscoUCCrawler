---
doc_id: webex-admin-patch-identity-organizations-orgid
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: PATCH
path: /identity/organizations/{orgId}
operation_id: Update an organization
tags: Identity Organization
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.562522+00:00
---

# PATCH /identity/organizations/{orgId}

**API:** Webex Admin
**Área:** Identity Organization
**operationId:** `Update an organization`

## Resumen
Update an organization

## Descripción
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

1. Input JSON must contain schema: "urn:cisco:codev:identity:organization:core:1.0".

## Parámetros
- `orgId` [path] (string) (**requerido**): Webex Identity assigned organization identifier.

## Cuerpo de la petición (application/json)
- `schemas` (array) (**requerido**): Input JSON schemas.
- `displayName` (string) (**requerido**): New full name of the organization.
- `preferredLanguage` (string): It is the default preferredLanguage for user creation in this org. It is set in ISO639 format.

### Ejemplo — petición
```json
{
  "schemas": [
    "urn:cisco:codev:identity:organization:core:1.0"
  ],
  "displayName": "Acme_New, Inc.",
  "preferredLanguage": "en_US"
}
```

## Ejemplo de invocación
```bash
curl -X PATCH '/identity/organizations/<orgId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"schemas": [], "displayName": "<displayName>"}'
```

## Respuestas correctas
**200**: OK
- `schemas` (array) (**requerido**): Output JSON schemas.
- `id` (string) (**requerido**): Webex Identity assigned organization identifier.
- `displayName` (string) (**requerido**): Full name of the organization.
- `preferredLanguage` (string): It is the default preferredLanguage for user creation in this org. It is set in ISO639 format.
- `meta` (object):
  - `created` (string) (**requerido**): The date and time the organization was created.
  - `lastModified` (string) (**requerido**): The last modification time of the organization.
  - `version` (string) (**requerido**): The version information of the organization.

### Ejemplo — respuesta 200
```json
{
  "schemas": [
    "urn:cisco:codev:identity:organization:core:1.0"
  ],
  "id": "82adacf4-453f-4e2b-a406-2939fddcaad2",
  "displayName": "Acme_New, Inc.",
  "preferredLanguage": "en_US",
  "meta": {
    "created": "2021-05-13T15:51:09.736Z",
    "lastModified": "2024-05-20T12:25:16.739Z",
    "version": "W/\"67863100894\""
  }
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