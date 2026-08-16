---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-speeddials
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/speedDials
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.577131+00:00
---

# GET /telephony/config/people/me/settings/speedDials

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `getSpeedDials`

## Resumen
Get Speed Dials

## Descripción
Get the Speed Dials settings for the authenticated user. This API returns all configured speed dials (no pagination).

Speed Dials allow Webex Calling users to quickly dial frequently contacted people, places, or virtual lines by assigning them to dedicated keys on their desk phones or soft clients.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Respuestas
- **200**: OK
  - `speedDials` (array) **(requerido)**: List of speed dial entries configured for the person.
    - `id` (string): The identifier of the person, place or virtual line. See type for the resource type (PEOPLE, PLACE, or VIRTUAL_LINE). Only present for org speed dials.
    - `lastName` (string): The last name of the person or virtual line.
    - `firstName` (string): The first name of the person or virtual line.
    - `displayName` (string): The display name of the person, place or virtual line.
    - `type` (string): Indicates whether the type is `PEOPLE`, `PLACE` or `VIRTUAL_LINE`. Only present for org speed dials.  * `PEOPLE` - The speed dial is a person.  * `PLACE` - The speed dial is a workspace.  * `VIRTUAL_LINE` - The speed dial is a virtual line. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
    - `phoneNumber` (string) **(requerido)**: The phone number of the person, place or virtual line.
    - `extension` (string): The extension number for the person, place or virtual line.
    - `routingPrefix` (string): Routing prefix of location.
    - `locationName` (string): The location name where the speed dial is. Only present for org speed dials.
    - `locationId` (string): The ID for the location. Only present for org speed dials.
    - `lineKeyLabel` (string): This is a custom label configured for the speed dial on the device.
  - `availableEntriesCount` (integer) **(requerido)**: This is the number of additional entries that can be stored (more than the number of entries listed).
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
