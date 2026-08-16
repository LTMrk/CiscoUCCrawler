---
doc_id: webex-cloud-calling-get-telephony-config-virtualextensionranges
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/virtualExtensionRanges
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.620267+00:00
---

# GET /telephony/config/virtualExtensionRanges

**API:** Webex Cloud Calling
**Área:** Features: Virtual Extensions
**operationId:** `Get a list of a Virtual Extension Range`

## Resumen
Get a list of a Virtual Extension Range

## Descripción
Retrieves the list of Virtual Extension Ranges.

Virtual extension ranges integrate remote workers on a separate telephony system into Webex Calling and enable extension dialing. Using these ranges, you can define patterns that can be used to route calls at a location level or an organization level. You are allowed to define virtual extensions ranges in addition to individual virtual extensions.
This works in both Standard and Enhanced modes

Retrieving a virtual extension range requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Unique identifier for the organization.
- `max` [query] (number): Maximum number of results to return.
- `start` [query] (number): The starting index of the results to return.
- `order` [query] (string): Sort the list of virtual extension ranges by name or prefix, either ASC or DSC. Default sort order is ASC.
- `name` [query] (string): Filter the list of virtual extension ranges by name.
- `prefix` [query] (string): Filter the list of virtual extension ranges by prefix.
- `locationId` [query] (string): Filter the list of virtual extension ranges by location ID. Only one of the `locationId` and `OrgLevelOnly` query parameters is allowed at the same time.
- `orgLevelOnly` [query] (boolean): Filter the list of virtual extension ranges by organization level. If `orgLevelOnly` is true, return only the organization level virtual extension ranges.

## Respuestas
- **200**: OK
  - `virtualExtensionRanges` (array): Array of virtual extension ranges.
    - `id` (string) **(requerido)**: ID of the virtual extension range.
    - `name` (string) **(requerido)**: Name of the virtual extension range. This is a unique name for the virtual extension range.
    - `prefix` (string) **(requerido)**: Prefix used for a virtual extension range. Prefix works in Standard and Enhanced modes. In Standard mode, it must be E.164 and it must be unique. In Enhanced mode, it can be E.164 or non-E.164.
    - `level` (string) **(requerido)**: Level of the virtual extension range. It can be either `ORGANIZATION` or `LOCATION`.  * `ORGANIZATION` - Organization level.  * `LOCATION` - Location level. Valores: ORGANIZATION, LOCATION.
    - `locationId` (string): ID of the location to which the virtual extension range is assigned. This is set only for virtual extension ranges at the location level.
    - `locationName` (string): Name of the location to which the virtual extension range is assigned. This is set only for virtual extension ranges at the location level
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
