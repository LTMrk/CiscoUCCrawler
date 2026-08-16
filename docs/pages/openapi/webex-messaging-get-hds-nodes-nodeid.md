---
doc_id: webex-messaging-get-hds-nodes-nodeid
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
method: GET
path: /hds/nodes/{nodeId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.511167+00:00
---

# GET /hds/nodes/{nodeId}

**API:** Webex Messaging
**Área:** Hybrid Data Security
**operationId:** `getHDSNodeDetails`

## Resumen
Get node details

## Descripción
Retrieve details for a specific Hybrid Data Security node, such as host name, release version, proxy details, deployment and build type, availability details, etc.
To obtain the Node ID needed for this API, use the [Get cluster details API](</docs/api/v1/hds/get-cluster-details>)

## Parámetros
- `nodeId` [path] (string) **(requerido)**: Unique ID of the Hybrid Data Security node

## Respuestas
- **200**: Ok
  - `context` (object): Metadata information about the cluster to which the node belongs.
    - `orgId` (string): Unique ID of the organization.
    - `clusterId` (string): Unique ID of the cluster.
    - `clusterName` (string): Name of the cluster.
  - `nodeId` (string): Unique ID of the connector/node.
  - `host` (string): Host Name or Host IP of the Hybrid Data Security node.
  - `availabilityDetails` (object): Availability and health details of the Hybrid Data Security node.
    - `nodeAvailability` (string): Current availability of the Hybrid Data Security node.
    - `hdsHealthStatus` (string): Health status of the Hybrid Data Security node.
    - `hdsUnhealthyReasons` (array): List of reasons for unhealthy status of the Hybrid Data Security node.
  - `releaseVersion` (string): The release version of the Hybrid Data Security node.
  - `proxyType` (string): Proxy type used by the Hybrid Data Security node.
  - `proxyStatus` (string): Current proxy status of the Hybrid Data Security node.
  - `maintenanceMode` (string): On indicates that the node is in maintenance mode, and Off indicates that the node is not in maintenance mode.
  - `ntpSync` (string): NTP sync status of the Hybrid Data Security node.
  - `ovaDeploymentType` (string): Deployment type of the Hybrid Data Security node.
  - `ovaBuildType` (string): Build type of the Hybrid Data Security node.
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
