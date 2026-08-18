---
doc_id: webex-meeting-delete-meetings-meetingid-interpreters-interpreterid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: DELETE
path: /meetings/{meetingId}/interpreters/{interpreterId}
operation_id: deleteInterpreterById
tags: Meetings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.488639+00:00
---

# DELETE /meetings/{meetingId}/interpreters/{interpreterId}

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `deleteInterpreterById`

## Resumen
Delete a Meeting Interpreter

## Descripción
Removes a meeting interpreter identified by `meetingId` and `interpreterId` in the URI. The deleted meeting interpreter cannot be recovered.

## Parámetros
- `meetingId` [path] (string) (**requerido**): Unique identifier for the meeting whose interpreters were belong to.
- `interpreterId` [path] (string) (**requerido**): Unique identifier for the interpreter to be removed.
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin on-behalf-of scopes. If set, the admin may specify the email of a user in a site they manage and the API will delete an interpreter of the meeting that is hosted by that user.
- `sendEmail` [query] (boolean): If `true`, send email to the interpreter. Por defecto: True.

## Ejemplo de invocación
```bash
curl -X DELETE '/meetings/<meetingId>/interpreters/<interpreterId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**204**: No Content

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found
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