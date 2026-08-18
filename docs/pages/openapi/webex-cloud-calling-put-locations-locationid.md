---
doc_id: webex-cloud-calling-put-locations-locationid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /locations/{locationId}
operation_id: updateLocation
tags: Locations
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.348488+00:00
---

# PUT /locations/{locationId}

**API:** Webex Cloud Calling
**Área:** Locations
**operationId:** `updateLocation`

## Resumen
Update a Location

## Descripción
Update details for a location, by ID.

* Updating a location in your organization requires a full administrator or location administrator auth token with a scope of `spark-admin:locations_write`.

* Specify the location ID in the `locationId` parameter in the URI.

* Partners may specify `orgId` query parameter to update location in managed organization.

* **Important:** While the `name` field supports up to 256 characters, locations that are enabled for Webex Calling must have names with a maximum of 80 characters. If the location is enabled for calling, ensure the name does not exceed 80 characters to maintain compatibility with Control Hub and calling features.

## Parámetros
- `locationId` [path] (string) (**requerido**): Update location common attributes for this location.
- `orgId` [query] (string): Update location common attributes for this organization.

## Cuerpo de la petición (application/json)
- `name` (string): The name of the location. Supports up to 256 characters, but locations enabled for Webex Calling are limited to 80 characters maximum.
- `timeZone` (string): Time zone associated with this location, refer to this link (https://developer.webex.com/docs/api/guides/webex-for-broadworks-developers-guide#webex-meetings-site-timezone) for format.
- `preferredLanguage` (string): Default email language.
- `address` (object): The address of the location. Once PSTN connectivity is set up for a location, please go to the [Update the Emergency Address of a Location](/docs/api/v1/pstn/update-the-emergency-address-of-a-location) API to update the location address.
  - `address1` (string): Address 1
  - `address2` (string): Address 2
  - `city` (string): City
  - `state` (string): State code
  - `postalCode` (string): Postal Code
  - `country` (string): ISO-3166 2-Letter Country Code.

### Ejemplo — petición
```json
{
  "name": "Denver",
  "address": {
    "address1": "123 Some St.",
    "address2": "Suite 456",
    "city": "Supercity",
    "state": "Goodstate",
    "postalCode": "12345",
    "country": "US"
  },
  "timeZone": "America/Chicago",
  "preferredLanguage": "en_us"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/locations/<locationId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
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
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs