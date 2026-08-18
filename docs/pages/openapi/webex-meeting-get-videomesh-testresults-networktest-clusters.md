---
doc_id: webex-meeting-get-videomesh-testresults-networktest-clusters
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /videoMesh/testResults/networkTest/clusters
operation_id: Get Network Test results for cluster
tags: Video Mesh
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.507397+00:00
---

# GET /videoMesh/testResults/networkTest/clusters

**API:** Webex Meetings
**Área:** Video Mesh
**operationId:** `Get Network Test results for cluster`

## Resumen
Get Network Test results for cluster

## Descripción
Returns the test results of the Network tests triggered for a single Video Mesh cluster. The tests listed below are run as a part of the Network Test execution on the node.

<b>Bandwidth Test</b> - Tests the bandwidth parameters of the Video Mesh node's network. The test is run between the Video Mesh node and cloud services.<br/>
<b>DNS Resolution Test</b> - Tests the resolution of IP addresses related to cloud services, against the DNS servers configured on the Video Mesh node's network.<br/>
<b>HTTPS Connectivity Test</b> - Tests whether the Video Mesh node is able to connect to cloud services via HTTPS protocol.<br/>
<b>Websocket Connectivity Test</b> - Tests whether the Video Mesh node is able to connect to Webex cloud services via Websocket.<br/>

## Parámetros
- `clusterId` [query] (string) (**requerido**): Unique ID of the Video Mesh cluster.
- `triggerType` [query] (string) (**requerido**): Trigger type. Valores: OnDemand, Periodic, All.
- `from` [query] (string) (**requerido**): The start date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. The `from` parameter cannot have date and time values that exceed `to`.
- `to` [query] (string) (**requerido**): The end date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.

## Ejemplo de invocación
```bash
curl -X GET '/videoMesh/testResults/networkTest/clusters?clusterId=<clusterId>&triggerType=<triggerType>&from=<from>&to=<to>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `orgId` (string): Unique ID of the organization.
- `from` (string): Start date and time (inclusive) of the Network Test data.
- `to` (string): End date and time (inclusive) of the Network Test data.
- `items` (array): Network test results.
  - `clusters` (array): List of Video Mesh clusters.
    - `clusterId` (string): Unique ID of the Video Mesh cluster.
    - `clusterName` (string): Name of the Video Mesh cluster.
    - `nodes` (array):
      - `nodeId` (string): Unique ID of the Video Mesh node.
      - `hostNameOrIP` (string): Host name or IP Address of the Video Mesh node.
      - `testResults` (array):
        - `timestamp` (string): The timestamp of the test run.
        - `triggerType` (string): The type of the test being executed. Can be either `OnDemand` or `Periodic`.
        - `id` (string): Unique ID of the test.
        - `result` (array):

### Ejemplo — respuesta 200
```json
{
  "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8yYzNjOWY5NS03M2Q5LTQ0NjAtYTY2OC0wNDcxNjJmZjFiYWQ=",
  "from": "2023-01-15T15:53:00Z",
  "to": "2023-01-20T15:53:00Z",
  "items": [
    {
      "clusters": [
        {
          "clusterId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzJjM2M5Zjk1LTczZDktNDQ2MC1hNjY4LTA0NzE2MmZmMWJhZDpmMWJmMGI1MC0yMDUyLTQ3ZmUtYjg3ZC01MTFjMmZlNzQ3MWk=",
          "clusterName": "shangai",
          "nodes": [
            {
              "nodeId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DT05ORUNUT1IvMmMzYzlmOTUtNzNkOS00NDYwLWE2NjgtMDQ3MTYyZmYxYmFkOm1mX21nbXRAMTU2ZGY3ODljODU1NGQ1NWEyNzVkZjk5NzhmOTkwMmQ=",
              "hostNameOrIP": "def.company.com",
              "testResults": [
                {
                  "timestamp": "2022-03-15T15:53:00Z",
                  "triggerType": "OnDemand",
                  "id": "Y2lzY29zcGFyazovL3VzL0NPTU1BTkRJRC8xZWI2NWZkZi05NjQzLTQxN2YtOTk3NC1hZDcyY2FlMGUxMGY6YWRlODhhNjAtMzk5Mi0xMWVkLTlhYmQtYzUyMjRiZjNjMzQ4",
                  "result": [
                    {
                      "type": "DNSResolutionTest",
                      "results": [
                        {
                          "serviceType": "WebexCloud",
                          "testResult": "Failed",
                          "failureDetails": {
                            "possibleFailureReason": [
                              "DNS Resolution issue detected in the Video Mesh Node [Error Code: 1302]."
                            ],
  
  ... (truncado)
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