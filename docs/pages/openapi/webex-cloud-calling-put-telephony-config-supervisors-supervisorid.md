---
doc_id: webex-cloud-calling-put-telephony-config-supervisors-supervisorid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/supervisors/{supervisorId}
operation_id: updateCallQueueSupervisorAgents
tags: Features:  Call Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.267992+00:00
---

# PUT /telephony/config/supervisors/{supervisorId}

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `updateCallQueueSupervisorAgents`

## Resumen
Assign or Unassign Agents to Supervisor for Call Queue or Customer Assist

## Descripción
Assign or unassign agents to the supervisor for an organization.

Agents in a call queue can be associated with a supervisor who can silently monitor, coach, barge in or to take over calls that their assigned agents are currently handling.

This operation requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `supervisorId` [path] (string) (**requerido**): Identifier of the supervisor to be updated.
- `orgId` [query] (string): Assign or unassign agents to a supervisor in this organization.
- `hasCxEssentials` [query] (boolean): Must be set to `true` to modify a supervisor with Customer Assist license. This can otherwise be ommited or set to `false`.

## Cuerpo de la petición (application/json)
- `agents` (array) (**requerido**): People, workspaces and virtual lines that are eligible to receive calls. **WARNING**: The `id` returned is in UUID format, since we don't have agentType from OCI response. This will be converting to Hydra type in future release.
  - `id` (string) (**requerido**): ID of person, workspace or virtual line. **WARNING**: The `id` returned is always of type `PEOPLE` even if the agent is a workspace or virtual line. The `type` of the agent `id` will be corrected in a future release.
  - `action` (string) (**requerido**): * `ADD` - Assign an agent to a supervisor.  * `DELETE` - Remove an agent from a supervisor. Valores: ADD, DELETE.

### Ejemplo — petición
```json
{
  "agents": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85NTA4OTc4ZC05YmFkLTRmYWEtYTljNC0wOWQ4NWQ4ZmRjZTY",
      "action": "ADD"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iYzIyMTRlNi0zYzdlLTRkZDAtOTc3Yy0zNzRlOWE2ZDk4MWM",
      "action": "ADD"
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/supervisors/<supervisorId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"agents": []}'
```

## Respuestas correctas
**204**: No Content
**206**: Partial Content
- `supervisorAgentStatus` (array) (**requerido**): Array of supervisor agents status.
  - `id` (string) (**requerido**): ID of person, workspace or virtual line. **WARNING**: The `id` returned is in UUID format, since we don't have agentType from OCI response. This will be converting to Hydra type in future release.
  - `status` (string) (**requerido**): status of the agent.
  - `message` (string) (**requerido**): Detailed message for the status.

### Ejemplo — respuesta 206
```json
{
  "supervisorAgentStatus": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85NTA4OTc4ZC05YmFkLTRmYWEtYTljNC0wOWQ4NWQ4ZmRjZTY",
      "status": "DUPLICATE",
      "message": "[Error 6612] Agent 9508978d-9bad-4faa-a9c4-09d85d8fdce6 is already assigned to the supervisor."
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