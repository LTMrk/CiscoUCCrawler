---
doc_id: webex-cloud-calling-post-telephony-pstn-locations-locationid-emergencyaddress-lookup
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/pstn/locations/{locationId}/emergencyAddress/lookup
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.634954+00:00
---

# POST /telephony/pstn/locations/{locationId}/emergencyAddress/lookup

**API:** Webex Cloud Calling
**Área:** PSTN
**operationId:** `emergencyAddressLookup`

## Resumen
Emergency Address Lookup to Verify if Address is Valid

## Descripción
Returns a suggested address. If the input address is valid and unchanged, no errors are returned. If the input address requires corrections, the response includes a suggested address along with error details.

Emergency address settings allow the admin to configure or update the physical address associated with a phone number or a location.

Emergency address lookup to verify if address is valid requires a full administrator auth token with scope of `spark-admin:telephony_pstn_read`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Emergency address lookup for this location.
- `orgId` [query] (string): Emergency address lookup for this organization.

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
- **200**: OK
  - `addresses` (array): List of suggested addresses based on the input address. If the input address is valid and unchanged, no errors are returned. If the input address requires corrections, the response includes a suggested address along with error details.
    - `address1` (string): Primary street information for the emergency address.
    - `address2` (string): Apartment number or any other secondary information for the emergency address.
    - `city` (string): City for the emergency address.
    - `state` (string): State or Province or Region for the emergency address.
    - `postalCode` (string): Postal code for the emergency address.
    - `country` (string): Country for the emergency address.
    - `meta` (object): Additional metadata for the emergency address.
    - `errors` (array): List of errors encountered during address validation. Returned only when the input address was corrected and a suggested address was provided. Each error describes a specific issue with the original input.
      - `code` (string): Error code.
      - `title` (string): Error title.
      - `detail` (string): Detailed error message.
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
