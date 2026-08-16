---
doc_id: webex-cloud-calling-get-telephony-config-locations
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/locations
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.621060+00:00
---

# GET /telephony/config/locations

**API:** Webex Cloud Calling
**Área:** Location Call Settings
**operationId:** `List Locations Webex Calling Details`

## Resumen
List Locations Webex Calling Details

## Descripción
Lists Webex Calling locations for an organization with Webex Calling details.

Searching and viewing locations with Webex Calling details in your
organization require an administrator auth token with the
`spark-admin:telephony_config_read` scope.

## Parámetros
- `orgId` [query] (string): List locations for this organization.
- `max` [query] (number): Limit the maximum number of locations in the response.
- `start` [query] (number): Specify the offset from the first result that you want to fetch.
- `name` [query] (string): List locations whose name contains this string.
- `order` [query] (string): Sort the list of locations based on `name`, either asc or desc.

## Respuestas
- **200**: OK
  - `locations` (array) **(requerido)**: Array of locations.
    - `id` (string) **(requerido)**: A unique identifier for the location.
    - `name` (string) **(requerido)**: The name of the location.
    - `outsideDialDigit` (string): Must dial to reach an outside line, default is None.
    - `enforceOutsideDialDigit` (boolean): True when enforcing outside dial digit at location level to make PSTN calls.
    - `routingPrefix` (string): Must dial a prefix when calling between locations having the same extension within the same location.
    - `callingLineId` (object) **(requerido)**: Location calling line information.
      - `name` (string): Group calling line ID name. By default the Org name.
      - `phoneNumber` (string) **(requerido)**: Directory Number / Main number in E.164 Format.
    - `e911SetupRequired` (boolean) **(requerido)**: True if E911 setup is required.
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
