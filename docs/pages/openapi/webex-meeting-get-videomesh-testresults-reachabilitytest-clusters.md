---
doc_id: webex-meeting-get-videomesh-testresults-reachabilitytest-clusters
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /videoMesh/testResults/reachabilityTest/clusters
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.406088+00:00
---

# GET /videoMesh/testResults/reachabilityTest/clusters

**API:** Webex Meetings
**Área:** Video Mesh
**operationId:** `Get Reachability Test results for cluster V2`

## Resumen
Get Reachability Test results for cluster V2

## Descripción
Returns the test results of the Reachability tests for a single Video Mesh cluster.

<br/>

Changes in V2:

<br/>

1. On-demand test results can be obtained along with the periodic tests that are executed on Video Mesh nodes.

<br/>

2. You can now view the destination IP address of the destination cluster in the JSON response.

## Parámetros
- `clusterId` [query] (string) **(requerido)**: Unique ID of the Video Mesh cluster.
- `triggerType` [query] (string) **(requerido)**: Trigger type.
- `from` [query] (string) **(requerido)**: The start date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. The `from` parameter cannot have date and time values that exceed `to`.
- `to` [query] (string) **(requerido)**: The end date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.

## Respuestas
- **200**: OK
  - `orgId` (string): Unique ID of the organization.
  - `from` (string): Start date and time (inclusive) of the Reachability test results data.
  - `to` (string): End date and time (inclusive) of the Reachability test results data.
  - `items` (array): Reachability test results data.
    - `clusters` (array): List of Video Mesh clusters.
      - `clusterId` (string): Unique ID of the Video Mesh cluster.
      - `clusterName` (string): Name of the Video Mesh cluster.
      - `nodes` (array): The Video Mesh nodes in the cluster.
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
