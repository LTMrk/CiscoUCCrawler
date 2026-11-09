---
doc_id: webex-meeting-post-meetingparticipants-admit
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: POST
path: /meetingParticipants/admit
operation_id: Admit Participants
tags: Participants
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-09T12:44:29.442275+00:00
---

# POST /meetingParticipants/admit

**API:** Webex Meetings
**Área:** Participants
**operationId:** `Admit Participants`

## Resumen
Admit Participants

## Descripción
To admit participants into a live meeting or its breakout sessions in bulk. If `breakoutSessionId` is null for all the requested participants, they are admitted into the main session of the meeting. If `breakoutSessionId` is not null for all the requested participants, they are admitted into the breakout sessions specified by each `breakoutSessionId`. It's not allowed that some requested participants have `breakoutSessionId` and the others haven't.

This API limits the maximum size of `items` in the request body to 100.

Each `participantId` of `items` in the request body should have the same prefix of `meetingId`.

## Cuerpo de la petición (application/json)
- `items` (array):
  - `participantId` (string): The ID that identifies the meeting participant.
  - `breakoutSessionId` (string): The breakout session ID that identifies which breakout session to admit the participant into. Admit into the main session if the value is empty.

### Ejemplo — petición
```json
{
  "items": [
    {
      "participantId": "560d7b784f5143e3be2fc3064a5c4999_I_204252993233618782_23e16d67-17f3-3ef1-b830-f33d17c0232e",
      "breakoutSessionId": "23e16d67-17f3-3ef1-b830-f33d17c0232e"
    },
    {
      "participantId": "560d7b784f5143e3be2fc3064a5c4999_I_204252993233618782_23e16d67-17f3-3ef1-b830-f33d17c0233d",
      "breakoutSessionId": "046afcde-d6c0-44da-aa79-96cb88762151"
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X POST '/meetingParticipants/admit' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**204**: No Content

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