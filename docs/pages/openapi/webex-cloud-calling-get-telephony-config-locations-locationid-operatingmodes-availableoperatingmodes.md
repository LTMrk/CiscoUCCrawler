---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-operatingmodes-availableoperatingmodes
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/locations/{locationId}/operatingModes/availableOperatingModes
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.617558+00:00
---

# GET /telephony/config/locations/{locationId}/operatingModes/availableOperatingModes

**API:** Webex Cloud Calling
**Área:** Features: Operating Modes
**operationId:** `Retrieve the List of Available Operating Modes in a Location`

## Resumen
Retrieve the List of Available Operating Modes in a Location

## Descripción
Retrieve list of `Operating Modes` which are available to be assigned to a location level feature (`Auto Attendant`, `Call Queue`, or `Hunt Group`). Since each location and an org can have a max of 100 `Operating Modes` defined. The max number of `operating modes` that can be returned is 200.

`Operating modes` can be used to define call routing rules for different scenarios like business hours, after hours, holidays, etc. for the `Auto Attendant`, `Call Queue`, and `Hunt Group` features.

Retrieving this list requires a full, read-only, or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Retrieve `operating modes` list from this location.
- `orgId` [query] (string): Retrieve `operating modes` list from this organization.

## Respuestas
- **200**: OK
  - `operatingModes` (array): Array of `operating modes`.
    - `id` (string) **(requerido)**: A unique identifier for the `operating mode`.
    - `name` (string) **(requerido)**: Unique name for the `operating mode`.
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
