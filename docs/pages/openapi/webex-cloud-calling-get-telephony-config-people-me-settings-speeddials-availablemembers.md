---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-speeddials-availablemembers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/speedDials/availableMembers
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.577358+00:00
---

# GET /telephony/config/people/me/settings/speedDials/availableMembers

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `getSpeedDialAvailableMembers`

## Resumen
Get Speed Dial Available Members

## Descripción
Get the available members which can be configured as Speed Dials for the authenticated user.

Speed Dials allow Webex Calling users to quickly dial frequently contacted people, places, or virtual lines by assigning them to dedicated keys on their desk phones or soft clients.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Parámetros
- `max` [query] (integer): Limit the number of objects returned to this maximum count.
- `start` [query] (integer): Start at the zero-based offset in the list of matching objects.
- `locationId` [query] (string): Return the members list available in this location.
- `name` [query] (array): Search (Contains) based on first name and last name.
- `phoneNumber` [query] (array): Search (Contains) based on number and extension.
- `order` [query] (string): Sort by first name (`firstName`) or last name (`lastName`). Sort directions asc or desc.  * `asc` - Sort in ascending order.  * `desc` - Sort in descending order.

## Respuestas
- **200**: OK
  - `members` (array) **(requerido)**: List of available members which can be configured as Speed Dials.
    - `id` (string) **(requerido)**: The identifier of the person, place or virtual line. See type for the resource type.
    - `lastName` (string): The last name of the person or virtual line.
    - `firstName` (string): The first name of the person or virtual line.
    - `displayName` (string): The display name of the person, place or virtual line.
    - `phoneNumber` (string) **(requerido)**: The phone number of the person, place or virtual line.
    - `extension` (string): The extension number for the person, place or virtual line.
    - `type` (string) **(requerido)**: Indicates whether the type is `PEOPLE`, `VIRTUAL_LINE` or `PLACE`.  * `PEOPLE` - The member is a person.  * `VIRTUAL_LINE` - The member is a virtual line.  * `PLACE` - The member is a workspace. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
    - `locationId` (string): The ID for the location.
    - `locationName` (string): The location name where the member is.
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
