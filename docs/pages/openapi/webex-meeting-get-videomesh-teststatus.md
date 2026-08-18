---
doc_id: webex-meeting-get-videomesh-teststatus
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /videoMesh/testStatus
operation_id: Get Triggered test status
tags: Video Mesh
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.506146+00:00
---

# GET /videoMesh/testStatus

**API:** Webex Meetings
**Área:** Video Mesh
**operationId:** `Get Triggered test status`

## Resumen
Get Triggered test status

## Descripción
Returns the status of the test triggered using the Trigger on-demand test API.

## Parámetros
- `commandId` [query] (string) (**requerido**): The unique command ID generated from Trigger on-demand test API.

## Ejemplo de invocación
```bash
curl -X GET '/videoMesh/testStatus?commandId=<commandId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `orgId` (string): Unique ID of the organization.
- `commandId` (string): The unique ID of the test being executed.
- `clusterId` (string): Unique ID of the Video Mesh cluster.
- `nodes` (array):
  - (cualquiera de:)
    - `nodeId` (string): Unique ID of the Video Mesh node.
    - `status` (string): Status of the test triggered. Valores: Dispatched, Completed, Errored.
    - `nodeId` (string): Unique ID of the Video Mesh node.
    - `status` (string): Status of the test triggered. Valores: Dispatched, Completed, Errored.

### Ejemplo — respuesta 200
```json
{
  "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8yYzNjOWY5NS03M2Q5LTQ0NjAtYTY2OC0wNDcxNjJmZjFiYWQ=",
  "commandId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DT01NQU5EX0lELzJjM2M5ZjllLTczZDktNDQ2MC1hNjY4LTA0NzE2MmZmMWJhYzo2NTJmNmMxMC01NjgxLTExZWQtOTkyZS1kNTY5YzlkMDlhNzU",
  "clusterId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzJjM2M5Zjk1LTczZDktNDQ2MC1hNjY4LTA0NzE2MmZmMWJhZDpmMWJmMGI1MC0yMDUyLTQ3ZmUtYjg3ZC01MTFjMmZlNzQ3MWI=",
  "nodes": [
    {
      "nodeId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DT05ORUNUT1IvMmMzYzlmOTUtNzNkOS00NDYwLWE2NjgtMDQ3MTYyZmYxYmFkOm1mX21nbXRAMTU2ZGY3ODljODU1NGQ1NWEyNzVkZjk5NzhmOTkwMmQ=",
      "status": "Dispatched"
    },
    {
      "nodeId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DT05ORUNUT1IvMmMzYzlmOWUtNzNkOS00NDYwLWE2NjgtMDQ3MTYyZmYxYmFjOm1mX21nbXRAMTU2ZGY3ODljODU1NGQ1NWEyNzVkZTk5NzhmOTkwMmU=",
      "status": "Dispatched"
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
The Webex Meetings APIs enable developers to schedule, manage, and retrieve information about Webex meetings, webinars, and events. They provide endpoints for meeting creation, participant management, recordings, transcripts, in-meeting features such as chat and closed captions, and post-meeting analytics. Common use cases include integrating meeting scheduling into calendar apps, automating follow-ups with recordings and transcripts, embedding meeting controls in custom portals, and extracting insights for compliance or productivity analysis. The APIs support both real-time and asynchronous w...

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs