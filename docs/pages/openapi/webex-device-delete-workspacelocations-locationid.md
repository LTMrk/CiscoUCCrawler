---
doc_id: webex-device-delete-workspacelocations-locationid
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
api_version: 1.0.0
method: DELETE
path: /workspaceLocations/{locationId}
operation_id: Delete a Workspace Location
tags: Workspace Locations
deprecated: true
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.210111+00:00
---

# DELETE /workspaceLocations/{locationId}

> **ENDPOINT DEPRECADO.** No usar en integraciones nuevas.

**API:** Webex Device
**Área:** Workspace Locations
**operationId:** `Delete a Workspace Location`

## Resumen
Delete a Workspace Location

## Descripción
<div><Callout type="warning">The Workspace Locations API is deprecated and will be decommissioned November 30, 2024. Please use the [/locations API](/docs/api/v1/locations) for future projects, and use `locationId` instead of `workspaceLocationId` when interacting with device or workspace APIs.</Callout></div>

Deletes a location, by ID. The workspaces associated to that location will no longer have a location, but a new location can be reassigned to them.
Requires an administrator auth token with the `spark-admin:workspace_locations_write` scope.

## Parámetros
- `locationId` [path] (string) (**requerido**): A unique identifier for the location.

## Ejemplo de invocación
```bash
curl -X DELETE '/workspaceLocations/<locationId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**204**: No Content

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
The Webex Device APIs provide endpoints for managing and monitoring Webex devices, including registration, configuration, status retrieval, workspace assignment, and firmware management. These APIs support automation of device onboarding, health monitoring, remote troubleshooting, and bulk configuration updates. Integration scenarios include custom device dashboards, proactive alerting, and seamless workspace management for meeting rooms and shared spaces. The APIs are essential for IT teams managing large fleets of Webex devices across distributed environments.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs