---
doc_id: webex-meeting-get-videomesh-eventthresholds
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /videoMesh/eventThresholds
operation_id: List Event Threshold Configuration
tags: Video Mesh
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.508544+00:00
---

# GET /videoMesh/eventThresholds

**API:** Webex Meetings
**Área:** Video Mesh
**operationId:** `List Event Threshold Configuration`

## Resumen
List Event Threshold Configuration

## Descripción
Returns the event threshold configurations for `orgId` or `clusterId`, with optional filters `eventName` and `eventScope`.

## Parámetros
- `eventName` [query] (string): Event name to fetch threshold details. Valores: clusterCallsRedirected, orgCallsOverflowed.
- `clusterId` [query] (string): Unique ID of the Video Mesh Cluster.
- `orgId` [query] (string): Unique ID of the Organization.
- `eventScope` [query] (string): Scope name to filter events. Valores: CLUSTER, ORG.

## Ejemplo de invocación
```bash
curl -X GET '/videoMesh/eventThresholds' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `orgId` (string): Unique ID of the organization.
- `eventThresholds` (array):
  - (cualquiera de:)
    - `eventName` (string): Name of the event.
    - `eventThresholdId` (string): Unique ID of the event threshold configuration.
    - `eventScope` (string): The `eventScope` is scope of event.
    - `entityId` (string): The `entityId` is the unique ID of the Organization or the unique ID of the Video Mesh Cluster.
    - `thresholdConfig` (object):
      - `minThreshold` (number): Threshold value (in percentage) to trigger an event.
      - `defaultMinThreshold` (number): Deafault Threshold value (in percentage) to trigger an event.
    - `eventName` (string): Name of the event.
    - `eventThresholdId` (string): Unique ID of the event threshold configuration.
    - `eventScope` (string): The `eventScope` is scope of event.
    - `entityId` (string): The `entityId` is the unique ID of the Organization or the unique ID of the Video Mesh Cluster.
    - `thresholdConfig` (object):
      - `minThreshold` (number): Threshold value (in percentage) to trigger an event.
      - `defaultMinThreshold` (number): Deafault Threshold value (in percentage) to trigger an event.

### Ejemplo — respuesta 200
```json
{
  "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8yYzNjOWY5NS03M2Q5LTQ0NjAtYTY2OC0wNDcxNjJmZjFiYWQ",
  "eventThresholds": [
    {
      "eventName": "clusterCallsRedirected",
      "eventThresholdId": "Y2lzY29zcGFyazovL3VzL0VWRU5ULzQyN2U5ZTk2LTczYTctNDYwYS04MGZhLTcyNWU4MWE2MDg3Zjo2YzJhZGRmMS0wYjAzLTRiZWEtYjIxYy0xYzFjYzdiY2UwOWQ",
      "eventScope": "CLUSTER",
      "entityId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzRiNTk5NzkwLWVlMzctMTFlZC1hMDViLTAyNDJhYzEyMDAwMzo2NjMxOTMyNC1lZTM3LTExZWQtYTA1Yi0wMjQyYWMxMjAwMDM",
      "thresholdConfig": {
        "minThreshold": 10,
        "defaultMinThreshold": 10
      }
    },
    {
      "eventName": "orgCallsOverflowed",
      "eventThresholdId": "Y2lzY29zcGFyazovL3VzL0VWRU5ULzQyN2U5ZTk2LTczYTctNDYwYS04MGZhLTcyNWU4MWE2MDg3ZjowM2ZkYjkzZC1jNTllLTQzMjQtODIwNS1lNDIyYzA3NGQ5Mzg",
      "eventScope": "ORG",
      "entityId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8yYzNjOWY5NS03M2Q5LTQ0NjAtYTY2OC0wNDcxNjJmZjFiYWQ",
      "thresholdConfig": {
        "minThreshold": 10,
        "defaultMinThreshold": 10
      }
    }
  ]
}
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