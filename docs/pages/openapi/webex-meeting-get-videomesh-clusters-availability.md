---
doc_id: webex-meeting-get-videomesh-clusters-availability
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /videoMesh/clusters/availability
operation_id: List Clusters Availability
tags: Video Mesh
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.500235+00:00
---

# GET /videoMesh/clusters/availability

**API:** Webex Meetings
**Área:** Video Mesh
**operationId:** `List Clusters Availability`

## Resumen
List Clusters Availability

## Descripción
Returns the availability details for all Video Mesh clusters in an organization.

## Parámetros
- `from` [query] (string) (**requerido**): The starting date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `from` cannot be after `to`.
- `to` [query] (string) (**requerido**): The ending date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
- `orgId` [query] (string) (**requerido**): The unique ID for the organization.

## Ejemplo de invocación
```bash
curl -X GET '/videoMesh/clusters/availability?from=<from>&to=<to>&orgId=<orgId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array):
  - `orgId` (string): The unique ID for the organization.
  - `items` (array): Availability details of the Video Mesh cluster.
    - `clusterId` (string): ID of the Video Mesh cluster.
    - `clusterName` (string): Name of the Video Mesh cluster.
    - `availabilitySegments` (array):
      - (cualquiera de:)
        - `segmentStartTime` (string): Start date and time of the segment of availability data.
        - `segmentEndTime` (string): End date and time of the segment of availability data.
        - `availability` (string): Availability information of the Video Mesh cluster.
        - `noOfOnlineNodes` (number): Number of nodes that are online.
        - `noOfOfflineNodes` (number): Number of nodes that are offline.
        - `totalNodes` (number): Total number of nodes in the Video Mesh cluster.
        - `segmentStartTime` (string): Start date and time of the segment of availability data.
        - `segmentEndTime` (string): End date and time of the segment of availability data.
        - `availability` (string): Availability information of the Video Mesh cluster.
        - `noOfOnlineNodes` (number): Number of nodes that are online.
        - `noOfOfflineNodes` (number): Number of nodes that are offline.
        - `totalNodes` (number): Total number of nodes in the Video Mesh cluster.
  - `from` (string): Start date and time (inclusive) of the availability data.
  - `to` (string): End date and time (inclusive) of the availability data.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8zNmQ4OTRmNy0yYjU3LTQzYzEtYWNlZS1kNDdlNjc3NjE0MTQ=",
      "items": [
        {
          "clusterId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJjYWUwZTEwZjpiMzdmNTgzYy1kZGRjLTQyOGItODJlNS1jYmU2ODFkYjQ5NjI=",
          "clusterName": "San Jose",
          "availabilitySegments": [
            {
              "segmentStartTime": "2021-09-15T15:53:00Z",
              "segmentEndTime": "2021-09-15T16:53:00Z",
              "availability": "Available",
              "noOfOnlineNodes": 1,
              "noOfOfflineNodes": 1,
              "totalNodes": 2
            },
            {
              "segmentStartTime": "2021-09-15T16:53:00Z",
              "segmentEndTime": "2021-09-15T17:53:00Z",
              "availability": "Unavailable",
              "noOfOnlineNodes": 0,
              "noOfOfflineNodes": 2,
              "totalNodes": 2
            }
          ]
        }
      ],
      "from": "2021-09-15T15:53:00Z",
      "to": "2021-09-15T17:53:00Z"
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