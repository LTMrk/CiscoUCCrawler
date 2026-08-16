---
doc_id: webex-cloud-calling-get-telephony-config-queues
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/queues
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.601918+00:00
---

# GET /telephony/config/queues

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `listCallQueues`

## Resumen
Read the List of Call Queues with Customer Assist

## Descripción
List all Call Queues for the organization.

Call queues temporarily hold calls in the cloud, when all agents
assigned to receive calls from the queue are unavailable. Queued calls are routed to 
an available agent, when not on an active call. Each call queue is assigned a lead number, which is a telephone
number that external callers can dial to reach the users assigned to the call queue.
Call queues are also assigned an internal extension, which can be dialed
internally to reach the users assigned to the call queue.

Retrieving this list requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Returns the list of call queues in this organization.
- `locationId` [query] (string): Returns the list of call queues in this location.
- `max` [query] (number): Limit the number of objects returned to this maximum count.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `name` [query] (string): Returns only the call queues matching the given name.
- `phoneNumber` [query] (string): Returns only the call queues matching the given primary phone number or extension.
- `departmentId` [query] (string): Returns only call queues matching the given department ID.
- `departmentName` [query] (string): Returns only call queues matching the given department name.
- `hasCxEssentials` [query] (boolean): Returns only the list of call queues with Customer Assist license when `true`, otherwise returns the list of Customer Experience Basic call queues.
- `digitalInboxEnabled` [query] (boolean): Returns only the list of call queues with digital inbox enabled when `true`, or disabled when `false`. This query parameter is only valid when `hasCxEssentials` is `true`.

## Respuestas
- **200**: OK
  - `queues` (array) **(requerido)**: Array of call queues.
    - `id` (string) **(requerido)**: A unique identifier for the call queue.
    - `name` (string) **(requerido)**: Unique name for the call queue.
    - `hasCxEssentials` (boolean) **(requerido)**: Denotes if the call queue has Customer Assist license.
    - `locationName` (string) **(requerido)**: Name of location for call queue.
    - `locationId` (string) **(requerido)**: ID of location for call queue.
    - `phoneNumber` (string): Primary phone number of the call queue.
    - `extension` (string): Primary phone extension of the call queue.
    - `enabled` (boolean) **(requerido)**: Whether or not the call queue is enabled.
    - `department` (object): The department information.
      - `id` (string): Unique identifier of the department.
      - `name` (string): Name of the department.
    - `digitalInboxEnabled` (boolean): Digital Inbox enabled for Queue. This field is applicable for queue which has `hasCxEssentials=true`.
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
