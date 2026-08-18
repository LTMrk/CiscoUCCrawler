---
doc_id: webex-admin-get-workspacelocations-locationid-floors-floorid
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /workspaceLocations/{locationId}/floors/{floorId}
operation_id: Get a Workspace Location Floor Details
tags: Workspace Locations
deprecated: true
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.593330+00:00
---

# GET /workspaceLocations/{locationId}/floors/{floorId}

> **ENDPOINT DEPRECADO.** No usar en integraciones nuevas.

**API:** Webex Admin
**Área:** Workspace Locations
**operationId:** `Get a Workspace Location Floor Details`

## Resumen
Get a Workspace Location Floor Details

## Descripción
<div><Callout type="warning">The Workspace Locations API is deprecated and will be decommissioned November 30, 2024. Please use the [/locations API](/docs/api/v1/locations) for future projects, and use `locationId` instead of `workspaceLocationId` when interacting with device or workspace APIs.</Callout></div>

Shows details for a floor, by ID. Specify the floor ID in the `floorId` parameter in the URI.
Requires an administrator auth token with the `spark-admin:workspace_locations_read` scope.

## Parámetros
- `locationId` [path] (string) (**requerido**): A unique identifier for the location.
- `floorId` [path] (string) (**requerido**): A unique identifier for the floor.

## Ejemplo de invocación
```bash
curl -X GET '/workspaceLocations/<locationId>/floors/<floorId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string): Unique identifier for the floor.
- `locationId` (string): Unique identifier for the location.
- `floorNumber` (number) (**requerido**): The floor number.
- `displayName` (string): The floor display name.

### Ejemplo — respuesta 200
```json
{
  "id": "xxx==",
  "locationId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMV9pbnQxMy9XT1JLU1BBQ0VfTE9DQVRJT04vM2E2ZmYzNzMtNjhhNy00NGU0LTkxZDYtYTI3NDYwZTBhYzVjIzUxOWY2N2E1LTlkOTktNGM2My04YTA5LWI5MTcxY2M2NmJkMQ==",
  "floorNumber": -1,
  "displayName": "The basement"
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