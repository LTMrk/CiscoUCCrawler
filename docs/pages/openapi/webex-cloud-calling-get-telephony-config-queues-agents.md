---
doc_id: webex-cloud-calling-get-telephony-config-queues-agents
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/queues/agents
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.606879+00:00
---

# GET /telephony/config/queues/agents

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `listCallQueueAgents`

## Resumen
Read the List of Call Queue Agents with Customer Assist

## Descripción
List all Call Queues Agents for the organization.

Agents can be users, workplace or virtual lines assigned to a call queue. Calls from the call queue are routed to agents based on configuration. 
An agent can be assigned to one or more call queues and can be managed by supervisors.

Retrieving this list requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

**Note**: The decoded value of the agent's `id`, and the `type` returned in the response, are always returned as `PEOPLE`, even when the agent is a workspace or virtual line. This will be addressed in a future release.

## Parámetros
- `orgId` [query] (string): List call queues agents in this organization.
- `locationId` [query] (string): Return only the call queue agents in this location.
- `queueId` [query] (string): Only return call queue agents with the matching queue ID.
- `max` [query] (number): Limit the number of objects returned to this maximum count.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `name` [query] (string): Returns only the list of call queue agents that match the given name.
- `phoneNumber` [query] (string): Returns only the list of call queue agents that match the given phone number or extension.
- `joinEnabled` [query] (boolean): Returns only the list of call queue agents that match the given `joinEnabled` value.
- `hasCxEssentials` [query] (boolean): Returns only the list of call queues with Customer Assist license when `true`, otherwise returns the list of Customer Experience Basic call queues.
- `order` [query] (string): Sort results alphabetically by call queue agent's name, in ascending or descending order.

## Respuestas
- **200**: OK
  - `agents` (array) **(requerido)**: Array of call queue agents.
    - `id` (string) **(requerido)**: Unique call queue agent identifier.
    - `firstName` (string): First name for the call queue agent.
    - `lastName` (string): Last name for the call queue agent.
    - `phoneNumber` (string): Primary phone number of the call queue agent.
    - `extension` (string): Primary phone extension of the call queue agent.
    - `routingPrefix` (string): Routing prefix of the call queue agent.
    - `esn` (string): Routing prefix + extension of a agent.
    - `queueCount` (number) **(requerido)**: Denotes the queue count for call queue agent.
    - `locationCount` (number) **(requerido)**: Denotes the location count for call queue agent.
    - `joinCount` (number) **(requerido)**: Denotes the join count for call queue agent.
    - `unjoinCount` (number) **(requerido)**: Denotes the unjoin count for call queue agent.
    - `location` (object) **(requerido)**: The location information.
      - `name` (string) **(requerido)**: The location name where the call queue agent resides.
      - `id` (string) **(requerido)**: ID of location for call queue agent.
    - `type` (string) **(requerido)**: The type of the call queue agent.
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
