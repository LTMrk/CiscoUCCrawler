---
doc_id: webex-messaging-get-hds-testresults-nodes-nodeid-networktest
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
api_version: 1.0.0
method: GET
path: /hds/testResults/nodes/{nodeId}/networkTest
operation_id: getNetworkTestResultsForHDSNode
tags: Hybrid Data Security
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.806062+00:00
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
- `nodeId` [path] (string) (**requerido**): Unique ID of the Hybrid Data Security node.
- `triggerType` [query] (string): Trigger type. Valores: OnDemand, Periodic, All.

## Ejemplo de invocación
```bash
curl -X GET '/hds/testResults/nodes/<nodeId>/networkTest' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `context` (object): Metadata information about the node for which network test results are being retrieved.
  - `orgId` (string): Unique ID of the organization.
  - `clusterId` (string): Unique ID of the cluster.
  - `clusterName` (string): Name of the cluster.
  - `nodeId` (string): Unique ID of the node.
  - `hostName` (string): Hostname of the Hybrid Data Security node.
  - `hostIP` (string): IP address of the Hybrid Data Security node.
- `testResults` (array): List of network test results.
  - `timestamp` (string/date-time): Timestamp when the test was triggered.
  - `triggerType` (string): Type of trigger for the test.
  - `result` (array): List of results per test type.
    - `type` (string): Type of network test.
    - `results` (array): List of service type test results.
      - `serviceType` (string): Type of service.
      - `services` (array): List of individual service test results.
        - `serviceName` (string): Name of the service.
        - `testResult` (string): Result of the test for the service.
        - `failureDetails` (object): Failure details for a failed network test, present only when testResult is Failed.

### Ejemplo — respuesta 200
```json
{
  "context": {
    "orgId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJVGNG",
    "clusterId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzJjM2M5Zjk1LTczZDktNDQ2MC1hNjY4LTA0NzE2MmZmMWJhZDpmMWJmMGI1MC0yMDUyLTQ3ZmUtYjg3ZC01MTFjMmZlNzQ3MWI=",
    "clusterName": "hds_bangalore",
    "nodeId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DT05ORUNUT1IvMmMzYzlmOTUtNzNkOS00NDYwLWE2NjgtMDQ3MTYyZmYxYmFkOjE1NmRmNzg5Yzg1NTRkNTVhMjc1ZGY5OTc4Zjk5MDJk",
    "hostName": "abc.xyz.com",
    "hostIP": "10.196.5.82"
  },
  "testResults": [
    {
      "timestamp": "2025-06-15T35:53:00Z",
      "triggerType": "OnDemand",
      "result": [
        {
          "type": "DNSResolutionTest",
          "results": [
            {
              "serviceType": "WebexCloud",
              "services": [
                {
                  "serviceName": "idBroker",
                  "testResult": "Failed",
                  "failureDetails": {
                    "possibleFailureReason": [
                      "DNS Resolution issue detected in the Hybrid Data Security Node [Error Code: 1302]."
                    ],
                    "possibleRemediation": [
                      "Please ensure that the configured DNS Servers are correct and healthy, and verify the network settings are adhering to the Hybrid Data Security Deployment Guide."
                    ]
                  }
                },
                {
                  "serviceName": "identity",
                 
  ... (truncado)
```

## Respuestas de error
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

## Contexto de la API
The Webex Messaging APIs offer robust programmatic access to messaging features within Webex, including sending and receiving messages, managing spaces, memberships, attachments, and moderating content. These APIs enable integration with bots, workflow automation, notification systems, and custom messaging solutions to enhance team collaboration and productivity. Use cases include building chatbots, integrating with ticketing or alerting platforms, automating onboarding flows, and creating custom collaboration experiences tailored to business needs.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs