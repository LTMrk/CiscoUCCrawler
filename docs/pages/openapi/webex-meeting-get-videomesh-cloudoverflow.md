---
doc_id: webex-meeting-get-videomesh-cloudoverflow
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /videoMesh/cloudOverflow
operation_id: List Overflow to Cloud details
tags: Video Mesh
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.502446+00:00
---

# GET /videoMesh/cloudOverflow

**API:** Webex Meetings
**Área:** Video Mesh
**operationId:** `List Overflow to Cloud details`

## Resumen
List Overflow to Cloud details

## Descripción
Returns details of overflows to the cloud in an organization.

## Parámetros
- `from` [query] (string) (**requerido**): The starting date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `from` cannot be after `to`.
- `to` [query] (string) (**requerido**): The ending date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
- `orgId` [query] (string) (**requerido**): The unique Video Mesh organization ID.

## Ejemplo de invocación
```bash
curl -X GET '/videoMesh/cloudOverflow?from=<from>&to=<to>&orgId=<orgId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array):
  - `orgId` (string): The unique ID for the organization.
  - `from` (string): Start date and time (inclusive) for the Overflow to Cloud data.
  - `to` (string): End date and time (inclusive) for the Overflow to Cloud data.
  - `aggregationInterval` (string): The aggregation period of the trend data.
  - `items` (array): Overflow data for the organization.
    - (cualquiera de:)
      - `timestamp` (string): Timestamp.
      - `overflowDetails` (array): Overflow Details.
        - (cualquiera de:)
      - `timestamp` (string): Timestamp.
      - `overflowDetails` (array): Overflow Details.
        - `overflowReason` (string): The reason for this overflow.
        - `overflowCount` (number): Number of overflows.
        - `possibleRemediation` (string): Any possible remediations for this overflow.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8zNmQ4OTRmNy0yYjU3LTQzYzEtYWNlZS1kNDdlNjc3NjE0MTQ",
      "from": "2022-03-23T10:22:03Z",
      "to": "2022-03-24T04:22:03Z",
      "aggregationInterval": "10m",
      "items": [
        {
          "timestamp": "2022-03-23T10:30:00Z",
          "overflowDetails": [
            {
              "overflowReason": "Capacity exceeded",
              "overflowCount": 25,
              "possibleRemediation": "Video Mesh exceeded its capacity. If this happens frequently, consider adding more nodes to your clusters."
            },
            {
              "overflowReason": "Connectivity issues",
              "overflowCount": 1,
              "possibleRemediation": "Connectivity Issues between Video Mesh Node and Cloud. Check your network configuration."
            }
          ]
        },
        {
          "timestamp": "2022-03-23T10:40:00Z",
          "overflowDetails": [
            {
              "overflowReason": "Capacity exceeded",
              "overflowCount": 38,
              "possibleRemediation": "Video Mesh exceeded its capacity. If this happens frequently, consider adding more nodes to your clusters."
            }
          ]
        }
      ]
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