---
doc_id: webex-meeting-post-videomesh-triggertest-nodes-nodeid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: POST
path: /videoMesh/triggerTest/nodes/{nodeId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.406707+00:00
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
- `nodeId` [path] (string) **(requerido)**: Unique ID of the Video Mesh node.

## Cuerpo de la petición (application/json)
- `type` (string): Test type to trigger on node.  * `ReachabilityTest` - Used to test whether the media ports within the Video Mesh node are open, and whether the Video Mesh node is able to reach the cloud clusters pertaining to the media containers via those ports.  * `NetworkTest` - Used to test the network environment of the Video Mesh node by running various connectivity, bandwidth, and DNS resolution tests against Webex Cloud and ThirdParty Cloud (Docker) services.  * `MediaHealthMonitorTest` - Used to test the meetings and call health of Video Mesh nodes using signalling and cascading methods. Valores: ReachabilityTest, NetworkTest, MediaHealthMonitorTest.

### Ejemplo de petición
```json
{
  "type": "MediaHealthMonitorTest"
}
```

## Respuestas
- **200**: OK
  - `orgId` (string): Unique ID of the organization.
  - `commandId` (string): The unique ID of the test being executed.
  - `clusterId` (string): Unique ID of the Video Mesh cluster.
  - `nodes` (array):
    - `nodeId` (string): Unique ID of the Video Mesh node.
    - `status` (string): Status of the test triggered. Valores: Dispatched, Completed, Errored.
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
