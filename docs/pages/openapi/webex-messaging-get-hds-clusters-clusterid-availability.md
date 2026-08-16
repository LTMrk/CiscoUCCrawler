---
doc_id: webex-messaging-get-hds-clusters-clusterid-availability
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
method: GET
path: /hds/clusters/{clusterId}/availability
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.511886+00:00
---

# GET /hds/clusters/{clusterId}/availability

**API:** Webex Messaging
**Área:** Hybrid Data Security
**operationId:** `getHDSClusterAvailabilityDetails`

## Resumen
Get availability details for Hybrid Data Security cluster

## Descripción
Get the availability details for an Hybrid Data Security cluster, where each segment specifies the start and end times, as well as the number of online, offline, and total nodes within that segment.
To obtain the Cluster ID needed for this API, use the [Get organization details API](</docs/api/v1/hds/get-organization-details>)

## Parámetros
- `clusterId` [path] (string) **(requerido)**: Unique ID of the Hybrid Data Security cluster.
- `from` [query] (string) **(requerido)**: The start date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. The 'from' value cannot be later than the 'to' value, and it cannot be more than 1 day older than the current date and time.
- `to` [query] (string) **(requerido)**: The end date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.

## Respuestas
- **200**: OK
  - `context` (object): Metadata information about the cluster for which availability details are being retrieved.
    - `orgId` (string): Unique ID of the organization.
    - `clusterId` (string): Unique ID of the cluster.
    - `clusterName` (string): Name of the cluster.
  - `availabilitySegments` (array): List of availability segments for the cluster.
    - `segmentStartTime` (string): Start time of the availability segment.
    - `segmentEndTime` (string): End time of the availability segment.
    - `noOfOnlineNodes` (integer): Number of online nodes in the cluster in the segment.
    - `noOfOfflineNodes` (integer): Number of offline nodes in the cluster in the segment.
    - `totalNodes` (integer): Total number of nodes in the cluster in the segment.
  - `timeRange` (object): The time range for the availability data.
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
