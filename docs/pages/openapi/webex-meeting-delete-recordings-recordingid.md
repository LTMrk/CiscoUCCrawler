---
doc_id: webex-meeting-delete-recordings-recordingid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: DELETE
path: /recordings/{recordingId}
operation_id: deleteRecordingByRecordId
tags: Recordings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.497754+00:00
---

# DELETE /recordings/{recordingId}

**API:** Webex Meetings
**Área:** Recordings
**operationId:** `deleteRecordingByRecordId`

## Resumen
Delete a Recording

## Descripción
Removes a recording with a specified recording ID. The deleted recording cannot be recovered. If a Compliance Officer deletes another user's recording, the recording will be inaccessible to regular users (host, attendees and shared), but will be still available to the Compliance Officer.

Only recordings of meetings hosted by the authenticated user can be deleted.

The `temporaryDirectDownloadLinks` of a recording which are retrieved by the [Get Recording Details](/docs/api/v1/recordings/get-recording-details) API are still available to Compliance Officers even if the recording has been deleted.

## Parámetros
- `recordingId` [path] (string) (**requerido**): A unique identifier for the recording.
- `hostEmail` [query] (string): Email address for the meeting host. Only used if the user or application calling the API has the required [admin-level meeting scopes](/docs/meetings#adminorganization-level-authentication-and-scopes). If set, the admin may specify the email of a user in a site they manage and the API will delete a recording of that user.

## Cuerpo de la petición (application/json)
- `reason` (string): Reason for deleting a recording. Only required when a Compliance Officer is operating on another user's recording.
- `comment` (string): Compliance Officer's explanation for deleting a recording. The comment can be a maximum of 255 characters long.

### Ejemplo — petición
```json
{
  "reason": "audit",
  "comment": "Compliance Officer's optional explanation for deleting a recording"
}
```

## Ejemplo de invocación
```bash
curl -X DELETE '/recordings/<recordingId>' \
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