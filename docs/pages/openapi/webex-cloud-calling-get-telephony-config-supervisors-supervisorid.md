---
doc_id: webex-cloud-calling-get-telephony-config-supervisors-supervisorid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/supervisors/{supervisorId}
operation_id: getCallQueueSupervisor
tags: Features:  Call Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.478112+00:00
---

# GET /telephony/config/supervisors/{supervisorId}

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `getCallQueueSupervisor`

## Resumen
Get Supervisor Details for Call Queue or Customer Assist

## Descripción
Get details of a specific supervisor, which includes the agents associated agents with the supervisor, in an organization.

Agents in a call queue can be associated with a supervisor who can silently monitor, coach, barge in or to take over calls that their assigned agents are currently handling.

This operation requires a full, user or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `supervisorId` [path] (string) (**requerido**): List the agents assigned to this supervisor.
- `orgId` [query] (string): List the agents assigned to a supervisor in this organization.
- `max` [query] (number): Limit the number of objects returned to this maximum count.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `name` [query] (string): Only return the agents that match the given name.
- `phoneNumber` [query] (string): Only return agents that match the given phone number, extension, or ESN.
- `order` [query] (string): Sort results alphabetically by supervisor name, in ascending or descending order.
- `hasCxEssentials` [query] (boolean): Must be set to `true`, to view the details of a supervisor with Customer Assist license. This can otherwise be ommited or set to `false`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/supervisors/<supervisorId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string): unique identifier of the supervisor
- `agents` (array) (**requerido**): Array of agents assigned to a specific supervisor.
  - `id` (string) (**requerido**): ID of person, workspace or virtual line.
  - `lastName` (string): Last name of the agent.
  - `firstName` (string): First name of the agent.
  - `extension` (string): Primary phone extension of the agent.
  - `esn` (string): Routing prefix + extension of a agent.
  - `phoneNumber` (string): Primary phone number of the agent.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85M2JlNTgxNi01YTIyLTQ5MzgtOWNmMy0wODIwODhiNDkxOGU",
  "agents": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8wNzViMGE4Mi1jNzM5LTRlMDktYWQ5NC0zNTc2YTBlMjYwZDA",
      "lastName": ".",
      "firstName": "Barn61",
      "extension": "1060",
      "esn": "1060"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85NTA4OTc4ZC05YmFkLTRmYWEtYTljNC0wOWQ4NWQ4ZmRjZTY",
      "lastName": "user",
      "firstName": "test",
      "extension": "892827",
      "esn": "892827"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iZjE5YWQzMC00NzAyLTQ3NWMtOTg0Ni1lM2M0M2Y1NGFlYzk",
      "lastName": ".",
      "firstName": "Test9",
      "routingPrefix": "34543",
      "phoneNumber": "+19729989982"
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