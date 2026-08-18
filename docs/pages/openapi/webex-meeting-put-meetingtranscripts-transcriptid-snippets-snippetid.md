---
doc_id: webex-meeting-put-meetingtranscripts-transcriptid-snippets-snippetid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: PUT
path: /meetingTranscripts/{transcriptId}/snippets/{snippetId}
operation_id: Update a Transcript Snippet
tags: Transcripts
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.475127+00:00
---

# PUT /meetingTranscripts/{transcriptId}/snippets/{snippetId}

**API:** Webex Meetings
**Área:** Transcripts
**operationId:** `Update a Transcript Snippet`

## Resumen
Update a Transcript Snippet

## Descripción
Updates details for a transcript snippet specified by `snippetId` from the meeting transcript specified by `transcriptId`.

## Parámetros
- `transcriptId` [path] (string) (**requerido**): Unique identifier for the meeting transcript to which the snippet to be updated belongs.
- `snippetId` [path] (string) (**requerido**): Unique identifier for the snippet being updated.

## Cuerpo de la petición (application/json)
- `reason` (string): Reason for snippet update; only required for Compliance Officers.
- `text` (string) (**requerido**): Text for the snippet.

### Ejemplo — petición
```json
{
  "reason": "audit",
  "text": "Hello everybody!"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/meetingTranscripts/<transcriptId>/snippets/<snippetId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"text": "<text>"}'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): A unique identifier for the snippet.
- `text` (string) (**requerido**): Text for the snippet.
- `personName` (string) (**requerido**): Name of the person generating the speech for the snippet.
- `personEmail` (string) (**requerido**): Email address of the person generating the speech for the snippet.
- `offsetMillisecond` (number) (**requerido**): Offset from the beginning of the parent transcript in milliseconds indicating the start time of the snippet.
- `durationMillisecond` (number) (**requerido**): Duration of the snippet in milliseconds.

### Ejemplo — respuesta 200
```json
{
  "id": "195d64646ad14be2924ea50f541fd91d_00001",
  "text": "Hello everybody!",
  "personName": "John Andersen",
  "personEmail": "john.andersen@example.com",
  "offsetMillisecond": 1000,
  "durationMillisecond": 1500
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