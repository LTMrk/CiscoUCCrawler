---
doc_id: webex-cloud-calling-get-telephony-config-supervisors
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/supervisors
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.605957+00:00
---

# GET /telephony/config/supervisors

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `listCallQueueSupervisors`

## Resumen
Get List of Supervisors with Customer Assist

## Descripción
Get list of supervisors for an organization.

Agents in a call queue can be associated with a supervisor who can silently monitor, coach, barge in or to take over calls that their assigned agents are currently handling.

Requires a full, location, user or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): List the supervisors in this organization.
- `max` [query] (number): Limit the number of objects returned to this maximum count.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `name` [query] (string): Only return the supervisors that match the given name.
- `phoneNumber` [query] (string): Only return the supervisors that match the given phone number, extension, or ESN.
- `order` [query] (string): Sort results alphabetically by supervisor name, in ascending or descending order.
- `hasCxEssentials` [query] (boolean): Returns only the list of supervisors with Customer Assist license, when `true`. Otherwise returns the list of supervisors with Customer Experience Basic license.

## Respuestas
- **200**: OK
  - `supervisors` (array) **(requerido)**: Array of supervisors.
    - `id` (string) **(requerido)**: A unique identifier for the supervisor.
    - `firstName` (string): First name of the supervisor.
    - `lastName` (string): Last name of the supervisor.
    - `phoneNumber` (string): Primary phone number of the supervisor.
    - `extension` (string): Primary phone extension of the supervisor.
    - `routingPrefix` (string): Routing prefix of location.
    - `esn` (string): Routing prefix + extension of a person.
    - `agentCount` (integer) **(requerido)**: Number of agents managed by supervisor. A supervisor must manage at least one agent.
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
