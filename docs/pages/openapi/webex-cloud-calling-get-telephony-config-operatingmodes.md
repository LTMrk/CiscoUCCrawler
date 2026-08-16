---
doc_id: webex-cloud-calling-get-telephony-config-operatingmodes
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/operatingModes
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.616254+00:00
---

# GET /telephony/config/operatingModes

**API:** Webex Cloud Calling
**Área:** Features: Operating Modes
**operationId:** `Read the List of Operating Modes`

## Resumen
Read the List of Operating Modes

## Descripción
Retrieve `Operating Modes` list defined at location, or organization level. Use query parameters to filter the result set by location or level. The list returned is sorted in ascending order by operating mode name. Long result sets are split into [pages](/docs/basics#pagination).

`Operating modes` help manage calls more efficiently by routing them based on predefined settings.

Retrieving this list requires a full, read-only, or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `name` [query] (string): List `operating modes` whose name contains this string.
- `limitToLocationId` [query] (string) **(requerido)**: Location query parameter to filter the `operating modes` from that location only.
- `limitToOrgLevelEnabled` [query] (boolean): If true, only return `operating modes` defined at the organization level.
- `max` [query] (number): Maximum number of `operating modes` to return in a single page. `max` must be equal to, or greater than `1`, and equal to or less than `100`.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `order` [query] (string): Sort the list of `operating modes` based on `name`, either asc, or desc.
- `orgId` [query] (string): Retrieve `operating modes` list from this organization.

## Respuestas
- **200**: OK
  - `operatingModes` (array) **(requerido)**: Array of `operating modes`.
    - `id` (string) **(requerido)**: A unique identifier for the `operating mode`.
    - `name` (string) **(requerido)**: Unique name for the `operating mode`.
    - `type` (string) **(requerido)**: * `SAME_HOURS_DAILY` - Specifies the `operating mode` is active during the same hours daily (i.e., same schedule for Monday to Friday, and Saturday to Sunday).  * `DIFFERENT_HOURS_DAILY` - Specifies the `operating mode` is active during different hours for different days of the week.  * `HOLIDAY` - Specifies the `operating mode` is active during holidays with their own days, and recurrence.  * `NONE` - Specifies the `operating mode` doesn't have any schedules defined. Valores: SAME_HOURS_DAILY, DIFFERENT_HOURS_DAILY, HOLIDAY, NONE.
    - `level` (string) **(requerido)**: * `ORGANIZATION` - Specifies this `operating mode` is configured across the organization.  * `LOCATION` - Specifies this `operating mode` is configured across a location. Valores: ORGANIZATION, LOCATION.
    - `location` (object):
      - `id` (string): The ID of the location.
      - `name` (string): The name of the location.
    - `callForwarding` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: Call forwarding is enabled, or disabled. `False` if the flag is not set.
      - `destination` (string) **(requerido)**: The destination for forwarding.
      - `destinationVoicemailEnabled` (boolean) **(requerido)**: The destination voicemail enabled. `False` if the flag is not set.
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
