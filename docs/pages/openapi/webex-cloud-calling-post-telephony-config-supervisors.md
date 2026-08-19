---
doc_id: webex-cloud-calling-post-telephony-config-supervisors
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/supervisors
operation_id: createCallQueueSupervisor
tags: Features:  Call Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.035245+00:00
---

# POST /telephony/config/supervisors

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `createCallQueueSupervisor`

## Resumen
Create a Supervisor for Call Queue or Customer Assist

## Descripción
Create a new supervisor. The supervisor must be created with at least one agent.

Agents in a call queue can be associated with a supervisor who can silently monitor, coach, barge in or to take over calls that their assigned agents are currently handling.

This operation requires a full or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): The organization ID where the supervisor needs to be created.
- `hasCxEssentials` [query] (boolean): Creates a Customer Assist queue supervisor, when `true`. Customer Assist queue supervisors must have a Customer Assist license.

## Cuerpo de la petición (application/json)
- `id` (string) (**requerido**): A unique identifier for the supervisor.
- `agents` (array) (**requerido**): People, workspaces and virtual lines that are eligible to receive calls.
  - `id` (string) (**requerido**): Identifier of the person, workspace or virtual line.

### Ejemplo — petición
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS83MTFlNWQ5NS0zODQyLTRmOGItOGZjNy00NGY5YjA0N2MyZTc",
  "agents": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BMQUNFLzE3NzczMWRiLWE1YzEtNGI2MC05ZTMwLTNhM2MxMGFiM2IxMQ"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfTElORS9hM2NjOTVhNC0zNzBjLTQyZmQtYWYzOS00MDE0MmE1YjMzMWU"
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/supervisors' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"id": "<id>", "agents": []}'
```

## Respuestas correctas
**201**: Created
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
      "status": "NOT_AVAILABLE",
      "message": "[Error 6612] Agent 9508978d-9bad-4faa-a9c4-09d85d8fdce6 is not available."
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