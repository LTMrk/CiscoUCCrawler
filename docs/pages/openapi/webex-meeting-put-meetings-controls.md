---
doc_id: webex-meeting-put-meetings-controls
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: PUT
path: /meetings/controls
operation_id: updateMeetingControl
tags: Meetings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.483721+00:00
---

# PUT /meetings/controls

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `updateMeetingControl`

## Resumen
Update Meeting Control Status

## Descripción
To start, pause, resume, or stop a meeting recording; To lock or unlock an on-going meeting.

## Parámetros
- `meetingId` [query] (string) (**requerido**): Unique identifier for the meeting. Does not support meeting IDs for a scheduled [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings) meeting.

## Cuerpo de la petición (application/json)
- `recordingStarted` (boolean): The value can be true or false. true means to start the recording, false to end the recording.
- `recordingPaused` (boolean): The value can be true or false, will be ignored if 'recordingStarted' sets to false, and true to resume the recording only if the recording is paused vise versa.
- `locked` (boolean): The value is true or false.

### Ejemplo — petición
```json
{
  "recordingStarted": true,
  "recordingPaused": true,
  "locked": true
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/meetings/controls?meetingId=<meetingId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- `locked` (boolean): Whether the meeting is locked or not.
- `recordingStarted` (boolean): The value can be true or false, it indicates the meeting recording started or not.
- `recordingPaused` (boolean): The value can be true or false, it indicates the meeting recording paused or not.

### Ejemplo — respuesta 200
```json
{
  "locked": false,
  "recordingStarted": true,
  "recordingPaused": true
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