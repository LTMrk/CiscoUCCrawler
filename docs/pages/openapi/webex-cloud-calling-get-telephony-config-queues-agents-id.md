---
doc_id: webex-cloud-calling-get-telephony-config-queues-agents-id
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/queues/agents/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.606995+00:00
---

# GET /telephony/config/queues/agents/{id}

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `getCallQueueAgent`

## Resumen
Get Details for a Call Queue Agent with Customer Assist

## Descripción
Retrieve details of a particular Call queue agent based on the agent ID.

Agents can be users, workplace or virtual lines assigned to a call queue. Calls from the call queue are routed to agents based on configuration. 
An agent can be assigned to one or more call queues and can be managed by supervisors.

Retrieving a call queue agent's details require a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

**Note**: The agent's `type` returned in the response and in the decoded value of the agent's `id`, is always of type `PEOPLE`, even if the agent is a workspace or virtual line. This` will be corrected in a future release.

## Parámetros
- `id` [path] (string) **(requerido)**: Retrieve call queue agents with this identifier.
- `orgId` [query] (string): Retrieve call queue agents from this organization.
- `hasCxEssentials` [query] (boolean): Must be set to `true` to view the details of an agent with Customer Assist license. This can otherwise be ommited or set to `false`.
- `max` [query] (number) **(requerido)**: Limit the number of objects returned to this maximum count.
- `start` [query] (number) **(requerido)**: Start at the zero-based offset in the list of matching objects.

## Respuestas
- **200**: OK
  - `agent` (object) **(requerido)**:
    - `id` (string) **(requerido)**: A unique identifier for the call queue agent.
    - `firstName` (string): First name for the call queue agent.
    - `lastName` (string): last name for the call queue agent.
    - `phoneNumber` (string): Primary phone number of the call queue agent.
    - `extension` (string): Primary phone extension of the call queue agent.
    - `esn` (string): Routing prefix + extension of a agent.
    - `location` (object) **(requerido)**: The location information.
      - `name` (string) **(requerido)**: The location name where the call queue agent resides.
      - `id` (string) **(requerido)**: ID of location for call queue agent.
    - `type` (string) **(requerido)**: The type of the call queue agent.
  - `queues` (array) **(requerido)**:
    - `id` (string) **(requerido)**: Unique identifier of the call queue.
    - `name` (string) **(requerido)**: Unique name for the call queue.
    - `phoneNumber` (string): Primary phone number of the call queue.
    - `routingPrefix` (string) **(requerido)**: The routing prefix for the call queue.
    - `locationId` (string) **(requerido)**: The location identifier of the call queue.
    - `locationName` (string) **(requerido)**: The location name where the call queue resides.
    - `joinEnabled` (boolean) **(requerido)**: Whether or not the call queue is enabled.
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
