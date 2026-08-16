---
doc_id: webex-messaging-get-hds-testresults-nodes-nodeid-networktest
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
method: GET
path: /hds/testResults/nodes/{nodeId}/networkTest
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.511638+00:00
---

# GET /hds/testResults/nodes/{nodeId}/networkTest

**API:** Webex Messaging
**Área:** Hybrid Data Security
**operationId:** `getNetworkTestResultsForHDSNode`

## Resumen
Get test results for Hybrid Data Security node

## Descripción
Get the latest results of the network tests triggered for a single Hybrid Data Security node. The test results are generated as part of the Network Test execution on the node. The network tests include the Bandwidth Test, DNS Resolution Test, and HTTPS Connectivity Test.
 The results from the latest test run are provided, covering up to the past 90 days if available.
To obtain the Node ID needed for this API, use the [Get cluster details API](</docs/api/v1/hds/get-cluster-details>)

## Parámetros
- `nodeId` [path] (string) **(requerido)**: Unique ID of the Hybrid Data Security node.
- `triggerType` [query] (string): Trigger type.

## Respuestas
- **200**: OK
  - `context` (object): Metadata information about the node for which network test results are being retrieved.
    - `orgId` (string): Unique ID of the organization.
    - `clusterId` (string): Unique ID of the cluster.
    - `clusterName` (string): Name of the cluster.
    - `nodeId` (string): Unique ID of the node.
    - `hostName` (string): Hostname of the Hybrid Data Security node.
    - `hostIP` (string): IP address of the Hybrid Data Security node.
  - `testResults` (array): List of network test results.
    - `timestamp` (string): Timestamp when the test was triggered.
    - `triggerType` (string): Type of trigger for the test.
    - `result` (array): List of results per test type.
      - `type` (string): Type of network test.
      - `results` (array): List of service type test results.
        - `serviceType` (string): Type of service.
        - `services` (array): List of individual service test results.
          - `serviceName` (string): Name of the service.
          - `testResult` (string): Result of the test for the service.
          - `failureDetails` (object): Failure details for a failed network test, present only when testResult is Failed.
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
