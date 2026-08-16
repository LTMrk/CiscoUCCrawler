---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-cxessentials-agents-availableagents
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/locations/{locationId}/cxEssentials/agents/availableAgents
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.612722+00:00
---

# GET /telephony/config/locations/{locationId}/cxEssentials/agents/availableAgents

**API:** Webex Cloud Calling
**Área:** Features: Customer Assist
**operationId:** `List Available Agents`

## Resumen
List Available Agents

## Descripción
Return a list of available agents with Customer Assist license in a location.

Retrieving the list of available agents requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Retrieve the list of avaiilable agents in this location.
- `orgId` [query] (string): The organization ID of the customer or partner's organization.
- `hasCxEssentials` [query] (boolean): Returns only the list of available agents with Customer Assist license when `true`, otherwise returns the list of available agents with Customer Experience Basic license.

## Respuestas
- **200**: OK
  - `agents` (array) **(requerido)**: List of available agents in the given location.
    - `id` (string) **(requerido)**: Unique agent identifier.
    - `lastName` (string): Last name of the agent assigned to the particular location.
    - `firstName` (string): First name of the agent assigned to the particular location.
    - `displayName` (string): Display name of the agent.
    - `type` (string) **(requerido)**: * `PEOPLE` - The associated member is a person.  * `PLACE` - The associated member is a workspace.  * `VIRTUAL_LINE` - The associated member is a virtual line. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
    - `email` (string): Email of the agent.
    - `hasCxEssentials` (boolean): Denotes whether the agent has Customer Assist license.
    - `phoneNumbers` (object): Phone number and extension of the agent.
      - `external` (string): External phoneNumber of the agent.
      - `extension` (string): Extension of the agent.
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
