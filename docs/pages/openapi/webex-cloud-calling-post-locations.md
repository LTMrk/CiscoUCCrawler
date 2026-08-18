---
doc_id: webex-cloud-calling-post-locations
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /locations
operation_id: createLocation
tags: Locations
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.348084+00:00
---

# POST /locations

**API:** Webex Cloud Calling
**Área:** Locations
**operationId:** `createLocation`

## Resumen
Create a Location

## Descripción
Create a new Location for a given organization. Only an admin in the organization can create a new Location.

* Creating a location in your organization requires a full administrator auth token with a scope of `spark-admin:locations_write`.

* Partners may specify `orgId` query parameter to create location in managed organization.

* The following body parameters are required to create a new location: 
    * `name`
    * `timeZone`
    * `preferredLanguage`
    * `address`
    * `announcementLanguage`.

* `latitude`, `longitude` and `notes` are optional parameters to create a new location.

* **Important:** While the `name` field supports up to 256 characters, locations that will be enabled for Webex Calling must have names with a maximum of 80 characters. If you plan to enable calling for this location, ensure the name does not exceed 80 characters to maintain compatibility with Control Hub and calling features.

## Parámetros
- `orgId` [query] (string): Create a location common attribute for this organization.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): The name of the location. Supports up to 256 characters, but locations enabled for Webex Calling are limited to 80 characters maximum.
- `timeZone` (string) (**requerido**): Time zone associated with this location, refer to this link (https://developer.webex.com/docs/api/guides/webex-for-broadworks-developers-guide#webex-meetings-site-timezone) for format.
- `preferredLanguage` (string) (**requerido**): Default email language.
- `announcementLanguage` (string) (**requerido**): Location's phone announcement language.
- `address` (object) (**requerido**): The address of the location.
  - `address1` (string) (**requerido**): Address 1
  - `address2` (string): Address 2
  - `city` (string) (**requerido**): City
  - `state` (string) (**requerido**): State code
  - `postalCode` (string) (**requerido**): Postal Code
  - `country` (string) (**requerido**): ISO-3166 2-Letter Country Code.
- `latitude` (string): Latitude
- `longitude` (string): Longitude
- `notes` (string): Notes

### Ejemplo — petición
```json
{
  "name": "Denver",
  "timeZone": "America/Chicago",
  "announcementLanguage": "fr_fr",
  "preferredLanguage": "en_us",
  "address": {
    "address1": "123 Some St.",
    "address2": "Suite 456",
    "city": "Supercity",
    "state": "Goodstate",
    "postalCode": "12345",
    "country": "US"
  },
  "latitude": "12.935784",
  "longitude": "77.697332",
  "notes": "123 Some St. Denver location"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/locations' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "timeZone": "<timeZone>", "preferredLanguage": "<preferredLanguage>", "announcementLanguage": "<announcementLanguage>", "address": {}}'
```

## Respuestas correctas
**201**: Created
- `id` (string) (**requerido**): ID of the newly created location.

### Ejemplo — respuesta 201
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzljYTNhZmQ3LTE5MjYtNGQ0ZS05ZDA3LTk5ZDJjMGU4OGFhMA"
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