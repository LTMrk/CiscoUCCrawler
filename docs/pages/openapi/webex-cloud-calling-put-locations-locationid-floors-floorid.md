---
doc_id: webex-cloud-calling-put-locations-locationid-floors-floorid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /locations/{locationId}/floors/{floorId}
operation_id: updateLocationFloor
tags: Locations
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.311744+00:00
---

# PUT /locations/{locationId}/floors/{floorId}

**API:** Webex Cloud Calling
**Área:** Locations
**operationId:** `updateLocationFloor`

## Resumen
Update a Location Floor

## Descripción
Updates details for a floor, by ID. Specify the floor ID in the `floorId` parameter in the URI. Include all details for the floor returned by a previous call to [Get Location Floor Details](/docs/api/v1/locations/get-location-floor-details). Omitting the optional `displayName` field will result in that field no longer being defined for the floor.
Requires an administrator auth token with the `spark-admin:locations_write` scope.

## Parámetros
- `locationId` [path] (string) (**requerido**): A unique identifier for the location.
- `floorId` [path] (string) (**requerido**): A unique identifier for the floor.

## Cuerpo de la petición (application/json)
- `floorNumber` (number) (**requerido**): The floor number.
- `displayName` (string): The floor display name.

### Ejemplo — petición
```json
{
  "floorNumber": 1,
  "displayName": "My custom name"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/locations/<locationId>/floors/<floorId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"floorNumber": 0}'
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
  "id": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMl9hL1dPUktTUEFDRV9MT0NBVElPTl9GTE9PUi83NDhkZDNmMS1iYmE5LTQxMDItODk5NC00M2IyOTM2MzNlNj",
  "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2E4NjczZDIwLWM0M2EtNDQ5Ni1iYWIxLTNiMjhhZGJjMjViYQ",
  "floorNumber": 1,
  "displayName": "My custom name"
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
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs