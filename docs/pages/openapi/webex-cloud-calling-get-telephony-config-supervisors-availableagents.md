---
doc_id: webex-cloud-calling-get-telephony-config-supervisors-availableagents
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/supervisors/availableAgents
operation_id: listAvailableCallQueueAgents
tags: Features:  Call Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.305036+00:00
---

# GET /telephony/config/supervisors/availableAgents

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `listAvailableCallQueueAgents`

## Resumen
List Available Agents for Call Queue or Customer Assist

## Descripción
Get list of available agents for an organization.

Agents in a call queue can be associated with a supervisor who can silently monitor, coach, barge in or to take over calls that their assigned agents are currently handling.

This operation requires a full, user or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): List of available agents in a supervisor's list for this organization.
- `max` [query] (number): Limit the number of objects returned to this maximum count.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `name` [query] (string): Returns only the agents that match the given name.
- `phoneNumber` [query] (string): Returns only the agents that match the phone number, extension, or ESN.
- `order` [query] (string): Sort results alphabetically by supervisor name, in ascending or descending order.
- `hasCxEssentials` [query] (boolean): Returns only the list of available agents with Customer Assist license, when `true`. When ommited or set to `false`, will return the list of available agents with Customer Experience Basic license.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/supervisors/availableAgents' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `agents` (array) (**requerido**): Array of agents assigned to a specific supervisor.
  - `id` (string) (**requerido**): A unique identifier for the agent.
  - `firstName` (string): First name of the agent.
  - `lastName` (string): Last name of the agent.
  - `displayName` (string): (string, optional) - Display name of the agent.
  - `phoneNumber` (string): Primary phone number of the agent.
  - `extension` (string): Primary phone extension of the agent.
  - `routingPrefix` (string): Routing prefix of location.
  - `esn` (string): Routing prefix + extension of a person.
  - `type` (string) (**requerido**): * `PEOPLE` - The associated member is a person.  * `PLACE` - The associated member is a workspace.  * `VIRTUAL_LINE` - The associated member is a virtual line. Valores: PEOPLE, PLACE, VIRTUAL_LINE.

### Ejemplo — respuesta 200
```json
{
  "agents": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jZGUzZWU0YS02ZDI5LTQ3OGItOGU5MC00MmE3YWFlNWIzNTE",
      "lastName": "CP-WS",
      "firstName": "CP-WS-1",
      "displayName": "CP-WS-1 .",
      "extension": "1248",
      "esn": "1248",
      "type": "PLACE"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hZWRlNmE0OS00NmNkLTQ4NWQtODQyZC1kY2ZmNTg4ZmQyMTU",
      "lastName": "CP-WS",
      "firstName": "CP-WS-6",
      "displayName": "CP-WS-6 .",
      "extension": "7539",
      "esn": "7539",
      "routingPrefix": "34543",
      "phoneNumber": "+19729989982",
      "type": "PEOPLE"
    }
  ]
}
```

## Respuestas de error
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

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs