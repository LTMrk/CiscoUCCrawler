---
doc_id: webex-device-get-locations
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
api_version: 1.0.0
method: GET
path: /locations
operation_id: listLocations
tags: Locations
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.207682+00:00
---

# GET /locations

**API:** Webex Device
**Área:** Locations
**operationId:** `listLocations`

## Resumen
List Locations

## Descripción
List locations for an organization.

* Use query parameters to filter the result set by location name, ID, or organization.

* Long result sets will be split into [pages](/docs/basics#pagination).

* Searching and viewing locations in your organization requires an administrator or location administrator auth token with any of the following scopes: `spark-admin:locations_read`, `spark-admin:people_read` or `spark-admin:device_read`.

## Parámetros
- `name` [query] (string): List locations whose name contains this string (case-insensitive).
- `id` [query] (string): List locations by ID.
- `orgId` [query] (string): List locations in this organization. Only admin users of another organization (such as partners) may use this parameter.
- `max` [query] (number): Limit the maximum number of location in the response. Por defecto: 500.

## Ejemplo de invocación
```bash
curl -X GET '/locations' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array):
  - `id` (string): Unique identifier for the location.
  - `locationId` (string): The ID to use for this location in the [/locations API](/docs/api/v1/locations)
  - `displayName` (string): A friendly name for the location.
  - `address` (string) (**requerido**): The location address.
  - `countryCode` (string) (**requerido**): The location country code (ISO 3166-1).
  - `cityName` (string): The location city name.
  - `latitude` (number) (**requerido**): The location latitude.
  - `longitude` (number) (**requerido**): The location longitude.
  - `notes` (string): Notes associated with the location.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2M5N2VlMDQ5LTM1OWItNGM3OC04NDU0LTA1OGMyZWRlMjU2Mw",
      "name": "Denver",
      "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9hNDVkNmNkYS1hZTVhLTQwYzMtYTdhZC01NjUwZmRkZGQ1M2M",
      "address": {
        "address1": "123 Some St.",
        "address2": "Suite 456",
        "city": "Supercity",
        "state": "Goodstate",
        "postalCode": "12345",
        "country": "US"
      },
      "timeZone": "America/Chicago",
      "preferredLanguage": "en_us",
      "latitude": "12.935784",
      "longitude": "77.697332",
      "notes": "Suite 456 Denver location"
    }
  ]
}
```
- Cabecera `Link`: 

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