---
doc_id: webex-meeting-get-videomesh-testresults-reachabilitytest-nodes
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /videoMesh/testResults/reachabilityTest/nodes
operation_id: Get Reachability Test results for node V2
tags: Video Mesh
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.504947+00:00
---

# GET /videoMesh/testResults/reachabilityTest/nodes

**API:** Webex Meetings
**Área:** Video Mesh
**operationId:** `Get Reachability Test results for node V2`

## Resumen
Get Reachability Test results for node V2

## Descripción
Returns the test results of the Reachability tests for a single Video Mesh node.

<br/>

Changes in V2:

<br/>

1. On-demand test results can be obtained along with the periodic tests that are executed on Video Mesh nodes.

<br/>

2. You can now view the destination IP address of the destination cluster in the JSON response.

## Parámetros
- `nodeId` [query] (string) (**requerido**): Unique ID of the Video Mesh node.
- `triggerType` [query] (string) (**requerido**): Trigger type. Valores: OnDemand, Periodic, All.
- `from` [query] (string) (**requerido**): The start date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. The `from` parameter cannot have date and time values that exceed `to`.
- `to` [query] (string) (**requerido**): The end date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.

## Ejemplo de invocación
```bash
curl -X GET '/videoMesh/testResults/reachabilityTest/nodes?nodeId=<nodeId>&triggerType=<triggerType>&from=<from>&to=<to>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `orgId` (string): Unique ID of the organization.
- `from` (string): Start date and time (inclusive) of the Reachability test results data.
- `to` (string): End date and time (inclusive) of the Reachability test results data.
- `items` (array): Reachability test results data.
  - `clusters` (array): List of Video Mesh clusters.
    - `clusterId` (string): Unique ID of the Video Mesh cluster.
    - `clusterName` (string): Name of the Video Mesh cluster.
    - `nodes` (array): The Video Mesh nodes in the cluster.
      - `nodeId` (string): Unique ID of the Video Mesh node.
      - `hostNameOrIP` (string): Host name or the IP of the Video Mesh node.
      - `testResults` (array): Reachability test results for a single Video Mesh node.
        - `destinationCluster` (string): Cloud Webex cluster against which Reachability test is being executed.
        - `stunResults` (array): STUN test results for a Video Mesh cluster.

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
          "clusterId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzJjM2M5Zjk1LTczZDktNDQ2MC1hNjY4LTA0NzE2MmZmMWJhZDpmMWJmMGI1MC0yMDUyLTQ3ZmUtYjg3ZC01MTFjMmZlNzQ3MWI=",
          "clusterName": "banglore",
          "nodes": [
            {
              "nodeId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DT05ORUNUT1IvMmMzYzlmOTUtNzNkOS00NDYwLWE2NjgtMDQ3MTYyZmYxYmFkOm1mX21nbXRAMTU2ZGY3ODljODU1NGQ1NWEyNzVkZjk5NzhmOTkwMmQ=",
              "hostNameOrIP": "xyz.company.com",
              "testResults": [
                {
                  "destinationCluster": "Amsterdam Cluster",
                  "stunResults": [
                    {
                      "timestamp": "2022-03-15T15:53:00Z",
                      "triggerType": "OnDemand",
                      "id": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DT01NQU5EX0lELzJjM2M5ZjllLTczZDktNDQ2MC1hNjY4LTA0NzE2MmZmMWJhYzo2NTJmNmMxMC01NjgxLTExZWQtOTkyZS1kNTY5YzlkMDlhNzU",
                      "udp": [
                        {
                          "ipAddress": "1.1.1.1",
                          "port": 51004,
                          "reachable": false
                        },
                        {
                          "ipAddress": "1.1.1.1",
                          "port": 5004,
                          "rea
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