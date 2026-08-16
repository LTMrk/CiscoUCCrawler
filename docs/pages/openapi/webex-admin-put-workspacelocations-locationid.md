---
doc_id: webex-admin-put-workspacelocations-locationid
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: PUT
path: /workspaceLocations/{locationId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.164650+00:00
---

# PUT /workspaceLocations/{locationId}

**API:** Webex Admin
**Área:** Workspace Locations
**operationId:** `Update a Workspace Location`

## Resumen
Update a Workspace Location

## Descripción
<div><Callout type="warning">The Workspace Locations API is deprecated and will be decommissioned November 30, 2024. Please use the [/locations API](/docs/api/v1/locations) for future projects, and use `locationId` instead of `workspaceLocationId` when interacting with device or workspace APIs.</Callout></div>

Updates details for a location, by ID. Specify the location ID in the `locationId` parameter in the URI. The request should include all details for the location returned in a previous call to [Get Workspace Location Details](/docs/api/v1/workspace-locations/get-a-workspace-location-details). Omitting the optional `cityName` or `notes` fields will result in those fields no longer being defined for the location.
Requires an administrator auth token with the `spark-admin:workspace_locations_write` scope.

## Parámetros
- `locationId` [path] (string) **(requerido)**: A unique identifier for the location.

## Cuerpo de la petición (application/json)
- `id` (string): Unique identifier for the location.
- `displayName` (string) **(requerido)**: A friendly name for the location.
- `address` (string) **(requerido)**: The location address.
- `countryCode` (string) **(requerido)**: The location country code (ISO 3166-1).
- `cityName` (string): The location city name.
- `latitude` (number) **(requerido)**: The location latitude.
- `longitude` (number) **(requerido)**: The location longitude.
- `notes` (string): Notes associated with the location.

### Ejemplo de petición
```json
{
  "id": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMV9pbnQxMy9XT1JLU1BBQ0VfTE9DQVRJT04vM2E2ZmYzNzMtNjhhNy00NGU0LTkxZDYtYTI3NDYwZTBhYzVjIzUxOWY2N2E1LTlkOTktNGM2My04YTA5LWI5MTcxY2M2NmJkMQ==",
  "displayName": "Cisco Barcelona",
  "address": "Carrer de Pere IV, Barcelona, Spain",
  "countryCode": "ES",
  "cityName": "Barcelona",
  "latitude": 41.406615,
  "longitude": 2.200717,
  "notes": "A note about the location"
}
```

## Respuestas
- **200**: OK
  - `id` (string): Unique identifier for the location.
  - `locationId` (string): The ID to use for this location in the [/locations API](/docs/api/v1/locations)
  - `displayName` (string): A friendly name for the location.
  - `address` (string) **(requerido)**: The location address.
  - `countryCode` (string) **(requerido)**: The location country code (ISO 3166-1).
  - `cityName` (string): The location city name.
  - `latitude` (number) **(requerido)**: The location latitude.
  - `longitude` (number) **(requerido)**: The location longitude.
  - `notes` (string): Notes associated with the location.
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
