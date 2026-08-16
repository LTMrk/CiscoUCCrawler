---
doc_id: webex-cloud-calling-get-telephony-config-countries-countrycode
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/countries/{countryCode}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.653815+00:00
---

# GET /telephony/config/countries/{countryCode}

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `getCountryConfiguration`

## Resumen
Get Country Calling Configuration

## Descripción
Retrieve country-specific configuration details including state requirements, zip code requirements, available states, and supported time zones.

This information helps administrators configure user settings with valid timezone and location data for a specific country.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `countryCode` [path] (string) **(requerido)**: The ISO country code to retrieve configuration for.
- `orgId` [query] (string): Organization ID. If not specified, uses the organization from the OAuth token.

## Respuestas
- **200**: OK
  - `stateRequired` (boolean) **(requerido)**: Indicates whether state is required for this country.
  - `zipCodeRequired` (boolean) **(requerido)**: Indicates whether zip code is required for this country.
  - `states` (array) **(requerido)**: List of states available for this country. Returns all items in a single response.
    - `code` (string) **(requerido)**: Two-letter state or province abbreviation (e.g., CA for California).
    - `name` (string) **(requerido)**: Full name of the state or province.
  - `timeZones` (array) **(requerido)**: List of time zones supported for this country. Returns all items in a single response.
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
