---
doc_id: webex-messaging-get-hds-nodes-nodeid-resourceusage
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
method: GET
path: /hds/nodes/{nodeId}/resourceUsage
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.511777+00:00
---

# GET /hds/nodes/{nodeId}/resourceUsage

**API:** Webex Messaging
**Área:** Hybrid Data Security
**operationId:** `getHDSNodeResourceUsage`

## Resumen
Get resource usage for an Hybrid Data Security node

## Descripción
Retrieve CPU, memory, and disk resource usage details for a specific Hybrid Data Security node over the requested time range.
To obtain the Node ID needed for this API, use the [List nodes for an Hybrid Data Security cluster API](</docs/api/v1/hds/list-hds-cluster-nodes>)

## Parámetros
- `nodeId` [path] (string) **(requerido)**: Unique ID of the Hybrid Data Security node.
- `from` [query] (string) **(requerido)**: The start date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
- `to` [query] (string) **(requerido)**: The end date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.

## Respuestas
- **200**: OK
  - `context` (object): Metadata information about the node for which resource usage is being retrieved.
    - `orgId` (string): Unique ID of the organization.
    - `clusterId` (string): Unique ID of the cluster.
    - `clusterName` (string): Name of the cluster.
    - `nodeId` (string): Unique ID of the node.
    - `host` (string): Host name or IP address of the Hybrid Data Security node.
  - `resourceUsage` (array): List of resource usage segments over the requested time range.
    - `startTime` (string): Start time of the resource usage segment.
    - `endTime` (string): End time of the resource usage segment.
    - `cpuUsage` (object): CPU usage details for the segment.
      - `peakCpuUsagePercent` (number): Peak CPU usage percentage in the segment.
      - `averageCpuUsagePercent` (number): Average CPU usage percentage in the segment.
    - `memoryUsage` (object): Memory usage details for the segment.
      - `totalMemoryUsageInMB` (number): Total memory available on the node in MB.
      - `peakMemoryUsageInMB` (number): Peak memory usage in MB in the segment.
      - `peakMemoryUsagePercent` (number): Peak memory usage percentage in the segment.
      - `averageMemoryUsageInMB` (number): Average memory usage in MB in the segment.
      - `averageMemoryUsagePercent` (number): Average memory usage percentage in the segment.
    - `diskUsage` (object): Disk usage details for the segment.
      - `totalDiskSpaceUsageInMB` (number): Total disk space available on the node in MB.
      - `peakDiskSpaceUsageInMB` (number): Peak disk space usage in MB in the segment.
      - `peakDiskUsagePercent` (number): Peak disk usage percentage in the segment.
      - `averageDiskUsage` (number): Average disk usage in MB in the segment.
      - `averageDiskUsagePercent` (number): Average disk usage percentage in the segment.
  - `timeRange` (object): The time range for the resource usage data.
    - `from` (string): Start time of the requested data range.
    - `to` (string): End time of the requested data range.
- **400**: Bad Request: The request was invalid or could not be processed. An accompanying error message will provide more details.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request was understood, but it has been refused or access is not allowed.
- **404**: Not Found: The requested URI is invalid, or the resource requested (such as a user) does not exist. This response is also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP method that is not supported.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **410**: Gone: The requested resource is no longer available.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type, or with a media type that is not supported.
- **423**: Locked: The requested resource is temporarily unavailable. A Retry-After header may be present to indicate how many seconds you should wait before attempting the request again.
- **428**: Precondition Required: The file(s) cannot be scanned for malware and must be force downloaded.
- **429**: Too Many Requests: Too many requests have been sent in a given period of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, please contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond in time. If your query uses the max parameter, please try reducing its value.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
