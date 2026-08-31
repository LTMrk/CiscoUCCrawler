---
doc_id: webex-cloud-calling-post-telephony-config-locations
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/locations
operation_id: Enable a Location for Webex Calling
tags: Location Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.293196+00:00
---

# POST /telephony/config/locations

**API:** Webex Cloud Calling
**Área:** Location Call Settings
**operationId:** `Enable a Location for Webex Calling`

## Resumen
Enable a Location for Webex Calling

## Descripción
Enable a location by adding it to Webex Calling. This add Webex Calling support to a
location created created using the POST /v1/locations API.

Locations are used to support calling features which can be defined at the location level.

This API requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Cuerpo de la petición (application/json)
- `id` (string) (**requerido**): A unique identifier for the location.
- `name` (string) (**requerido**): The name of the location.
- `timeZone` (string) (**requerido**): Time zone associated with this location. Refer to this link (https://developer.webex.com/docs/api/guides/webex-for-broadworks-developers-guide#webex-meetings-site-timezone) for the format.
- `preferredLanguage` (string) (**requerido**): Default email language.
- `announcementLanguage` (string) (**requerido**): Location's phone announcement language.
- `address` (object) (**requerido**): The address of the location.
  - `address1` (string) (**requerido**): Address 1 of the location.
  - `address2` (string): Address 2 of the location.
  - `city` (string) (**requerido**): City of the location.
  - `state` (string) (**requerido**): State code of the location.
  - `postalCode` (string) (**requerido**): Postal code of the location.
  - `country` (string) (**requerido**): ISO-3166 2-Letter country code of the location.

### Ejemplo — petición
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzhmZjMwMjg5LWVhMzMtNDc1Ny1iMTBmLWQ2MWIyNzFhMDVlZg",
  "name": "Denver",
  "timeZone": "America/Chicago",
  "announcementLanguage": "fr_fr",
  "preferredLanguage": "en_us",
  "address": {
    "address1": "771 Alder Drive",
    "address2": "Cisco Site 5",
    "city": "Milpitas",
    "state": "CA",
    "postalCode": "95035",
    "country": "US"
  }
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"id": "<id>", "name": "<name>", "timeZone": "<timeZone>", "preferredLanguage": "<preferredLanguage>", "announcementLanguage": "<announcementLanguage>", "address": {}}'
```

## Respuestas correctas
**201**: Created
- `id` (string) (**requerido**): A unique identifier for the location.

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