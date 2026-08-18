---
doc_id: webex-messaging-get-hds-clusters-clusterid-nodes
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
api_version: 1.0.0
method: GET
path: /hds/clusters/{clusterId}/nodes
operation_id: listHDSClusterNodes
tags: Hybrid Data Security
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.804863+00:00
---

# GET /hds/clusters/{clusterId}/nodes

**API:** Webex Messaging
**Área:** Hybrid Data Security
**operationId:** `listHDSClusterNodes`

## Resumen
List nodes for an Hybrid Data Security cluster

## Descripción
Retrieve a list of all nodes for a specific Hybrid Data Security cluster, including availability, proxy details, deployment type, and release version.
To obtain the Cluster ID needed for this API, use the [List clusters for an Hybrid Data Security organization API](</docs/api/v1/hds/list-hds-organization-clusters>)

## Parámetros
- `clusterId` [path] (string) (**requerido**): Unique ID of the Hybrid Data Security cluster.

## Ejemplo de invocación
```bash
curl -X GET '/hds/clusters/<clusterId>/nodes' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `nodes` (array): List of nodes in the cluster.
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

### Ejemplo — respuesta 200
```json
{
  "nodes": [
    {
      "context": {
        "orgId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJVGNG",
        "clusterId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJjYWUwZTEwZjpiMzdmNTgzYy1kZGRjLTQyOGItODJlNS1jYmU2ODFkYjQ5NjI",
        "clusterName": "San Jose"
      },
      "nodeId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzM2ZDg5NGY3LTJiNTctNDNjMS1hY2VlLWQ0N2U2Nzc2MTQxNDo0NjdiNGIxZC1jZWI2LTQwN2EtYWZmOC1mMjIxZmFiNzhjNzI",
      "host": "xyz.abc.com",
      "availabilityDetails": {
        "nodeAvailability": "Online",
        "hdsHealthStatus": "Healthy / Unhealthy",
        "hdsUnhealthyReasons": [
          "kms unhealthy",
          "avalon unhealthy"
        ]
      },
      "releaseVersion": "2025.07.16.7042",
      "proxyType": "Explicit",
      "proxyStatus": "Enabled",
      "maintenanceMode": "On",
      "ntpSync": "active",
      "ovaDeploymentType": "Large",
      "ovaBuildType": "Dev"
    },
    {
      "context": {
        "orgId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJVGNG",
        "clusterId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJjYWUwZTEwZjpiMzdmNTgzYy1kZGRjLTQyOGItODJlNS1jYmU2ODFkYjQ5NjI",
        "clusterName": "Bangalore"
      },
      "nodeId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzM2ZDg5NGY3LTJiNTctNDNjMS1hY2VlLWQ0N2U2Nzc2MTQxNDo0NjdiNGIxZC1jZWI2LTQwN2EtYWZmOC1mMjIxZmFiNzhjNzI",
   
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