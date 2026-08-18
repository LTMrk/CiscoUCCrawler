---
doc_id: webex-meeting-post-videomesh-triggertest-nodes-nodeid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: POST
path: /videoMesh/triggerTest/nodes/{nodeId}
operation_id: Trigger on-demand test for node
tags: Video Mesh
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.505935+00:00
---

# POST /videoMesh/triggerTest/nodes/{nodeId}

**API:** Webex Meetings
**Área:** Video Mesh
**operationId:** `Trigger on-demand test for node`

## Resumen
Trigger on-demand test for node

## Descripción
Triggers an on-demand test for a node.

## Parámetros
- `nodeId` [path] (string) (**requerido**): Unique ID of the Video Mesh node.

## Cuerpo de la petición (application/json)
- `type` (string): Test type to trigger on node.  * `ReachabilityTest` - Used to test whether the media ports within the Video Mesh node are open, and whether the Video Mesh node is able to reach the cloud clusters pertaining to the media containers via those ports.  * `NetworkTest` - Used to test the network environment of the Video Mesh node by running various connectivity, bandwidth, and DNS resolution tests against Webex Cloud and ThirdParty Cloud (Docker) services.  * `MediaHealthMonitorTest` - Used to test the meetings and call health of Video Mesh nodes using signalling and cascading methods. Valores: ReachabilityTest, NetworkTest, MediaHealthMonitorTest.

### Ejemplo — petición
```json
{
  "type": "MediaHealthMonitorTest"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/videoMesh/triggerTest/nodes/<nodeId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- `orgId` (string): Unique ID of the organization.
- `commandId` (string): The unique ID of the test being executed.
- `clusterId` (string): Unique ID of the Video Mesh cluster.
- `nodes` (array):
  - `nodeId` (string): Unique ID of the Video Mesh node.
  - `status` (string): Status of the test triggered. Valores: Dispatched, Completed, Errored.

### Ejemplo — respuesta 200
```json
{
  "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8yYzNjOWY5NS03M2Q5LTQ0NjAtYTY2OC0wNDcxNjJmZjFiYWQ=",
  "commandId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DT01NQU5EX0lELzJjM2M5ZjllLTczZDktNDQ2MC1hNjY4LTA0NzE2MmZmMWJhYzo2NTJmNmMxMC01NjgxLTExZWQtOTkyZS1kNTY5YzlkMDlhNzU",
  "clusterId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzJjM2M5Zjk1LTczZDktNDQ2MC1hNjY4LTA0NzE2MmZmMWJhZDpmMWJmMGI1MC0yMDUyLTQ3ZmUtYjg3ZC01MTFjMmZlNzQ3MWk=",
  "nodes": [
    {
      "nodeId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DT05ORUNUT1IvMmMzYzlmOTUtNzNkOS00NDYwLWE2NjgtMDQ3MTYyZmYxYmFkOm1mX21nbXRAMTU2ZGY3ODljODU1NGQ1NWEyNzVkZjk5NzhmOTkwMmQ=",
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