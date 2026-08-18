---
doc_id: webex-meeting-get-meetingclosedcaptions-closedcaptionid-snippets
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /meetingClosedCaptions/{closedCaptionId}/snippets
operation_id: getMeetingClosedCaptionsSnippets
tags: Closed Captions
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.463669+00:00
---

# GET /meetingClosedCaptions/{closedCaptionId}/snippets

**API:** Webex Meetings
**Área:** Closed Captions
**operationId:** `getMeetingClosedCaptionsSnippets`

## Resumen
List Meeting Closed Caption Snippets

## Descripción
Lists snippets of a meeting closed caption specified by `closedCaptionId`.

## Parámetros
- `closedCaptionId` [path] (string) (**requerido**): Unique identifier for the meeting closed caption which the snippets belong to.
- `meetingId` [query] (string) (**requerido**): Unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) which the closed caption snippets belong to. This parameter only applies to ended meeting instances. It does not apply to meeting series, scheduled meetings or scheduled [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings) meetings.

## Ejemplo de invocación
```bash
curl -X GET '/meetingClosedCaptions/<closedCaptionId>/snippets?meetingId=<meetingId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): Closed caption snippet array
  - `id` (string) (**requerido**): A unique identifier for the snippet.
  - `text` (string) (**requerido**): Text for the snippet.
  - `personName` (string) (**requerido**): Name of the person generating the speech for the snippet.
  - `personEmail` (string) (**requerido**): Email address of the person generating the speech for the snippet.
  - `offsetMillisecond` (number) (**requerido**): Offset from the beginning of the parent transcript in milliseconds indicating the start time of the snippet.
  - `durationMillisecond` (number) (**requerido**): Duration of the snippet in milliseconds.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "195d64646ad14be2924ea50f541fd91d_00001",
      "meetingId": "0ed74a1c0551494fb7a04e2881bf50ae_I_166022169160077044",
      "text": "Hello everyone",
      "personName": "John Andersen",
      "personEmail": "john.andersen@example.com",
      "peopleId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
      "start": "2019-11-01T12:30:05Z",
      "offsetMillisecond": "0",
      "durationMillisecond": "200",
      "language": "en"
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