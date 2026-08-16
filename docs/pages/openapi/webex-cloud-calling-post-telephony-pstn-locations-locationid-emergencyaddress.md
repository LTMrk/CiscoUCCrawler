---
doc_id: webex-cloud-calling-post-telephony-pstn-locations-locationid-emergencyaddress
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/pstn/locations/{locationId}/emergencyAddress
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.635070+00:00
---

# POST /telephony/pstn/locations/{locationId}/emergencyAddress

**API:** Webex Cloud Calling
**Área:** PSTN
**operationId:** `addEmergencyAddressToLocation`

## Resumen
Add an Emergency Address to a Location

## Descripción
Adds a new emergency address to the specified location. On success, returns the unique identifier of the newly created emergency address.

Emergency address settings allow the admin to configure or update the physical address associated with a phone number or a location.

Adding emergency address to a location requires a full administrator auth token with scope of `spark-admin:telephony_pstn_write`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Location to which the emergency address will be added.
- `orgId` [query] (string): Adding emergency address for a location in this organization.

## Cuerpo de la petición (application/json)
- `address1` (string): Primary street information for the emergency address.
- `address2` (string): Apartment number or any other secondary information for the emergency address.
- `city` (string): City for the emergency address.
- `state` (string): State or Province or Region for the emergency address.
- `postalCode` (string): Postal code for the emergency address.
- `country` (string): Country for the emergency address.

### Ejemplo de petición
```json
{
  "address1": "3487 Chase Ave",
  "address2": "Apt 112",
  "city": "Miami Beach",
  "state": "FL",
  "postalCode": "33140",
  "country": "US"
}
```

## Respuestas
- **201**: Created
  - `id` (string) **(requerido)**: Unique identifier for the emergency address.
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
