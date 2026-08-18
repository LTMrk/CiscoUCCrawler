---
doc_id: webex-meeting-post-meetings-meetingid-interpreters
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: POST
path: /meetings/{meetingId}/interpreters
operation_id: createInterpreter
tags: Meetings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.487875+00:00
---

# POST /meetings/{meetingId}/interpreters

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `createInterpreter`

## Resumen
Create a Meeting Interpreter

## Descripción
Assign an interpreter to a bi-directional simultaneous interpretation language channel for a meeting.

## Parámetros
- `meetingId` [path] (string) (**requerido**): Unique identifier for the meeting to which the interpreter is to be assigned.

## Cuerpo de la petición (application/json)
- `languageCode1` (string) (**requerido**): The pair of `languageCode1` and `languageCode2` form a bi-directional simultaneous interpretation language channel. The language codes conform with [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
- `languageCode2` (string) (**requerido**): The pair of `languageCode1` and `languageCode2` form a bi-directional simultaneous interpretation language channel. The language codes conform with [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
- `email` (string): Email address of meeting interpreter. If not specified, an empty interpreter will be created for this bi-directional language channel, and a specific email can be assigned to this empty interpreter by `Update a Meeting Interpreter` API later. Please note that multiple interpreters with different emails can be assigned to the same bi-directional language channel, but the same email cannot be assigned to more than one interpreter.
- `displayName` (string): Display name of meeting interpreter. If the interpreter is already an invitee of the meeting and it has a different display name, that invitee's display name will be overwritten by this attribute.
- `hostEmail` (string): Email address for the meeting host. This attribute should only be set if the user or application calling the API has the admin on-behalf-of scopes. When used, the admin may specify the email of a user in a site they manage to be the meeting host.
- `sendEmail` (boolean): If `true`, send email to the interpreter.

### Ejemplo — petición
```json
{
  "languageCode1": "en",
  "languageCode2": "de",
  "email": "marcus.hoffmann@example.com",
  "displayName": "Hoffmann"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/meetings/<meetingId>/interpreters' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"languageCode1": "<languageCode1>", "languageCode2": "<languageCode2>"}'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Unique identifier for meeting interpreter.
- `languageCode1` (string) (**requerido**): The pair of `languageCode1` and `languageCode2` form a bi-directional simultaneous interpretation language channel. The language codes conform with [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
- `languageCode2` (string) (**requerido**): The pair of `languageCode1` and `languageCode2` form a bi-directional simultaneous interpretation language channel. The language codes conform with [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
- `email` (string): Email address of meeting interpreter.
- `displayName` (string): Display name of meeting interpreter.

### Ejemplo — respuesta 200
```json
{
  "id": "OGQ0OGRiM2U3ZTAxNDZiMGFjYzJjMzYxNDNmNGZhN2RfZTA5MTJiZDBjNWVlNDA4YjgxMTZlMjU4Zjg2NWIzZmM",
  "languageCode1": "en",
  "languageCode2": "de",
  "email": "marcus.hoffmann@example.com",
  "displayName": "Hoffmann"
}
```

## Respuestas de error
- **400**: Bad Request
  Ejemplo:
```json
{
  "message": "'marcus.hoffmann@example.com' is found in more than one interpreter.",
  "trackingId": "8E12317727354470B5258F5B28D93FB9_1562296858685"
}
```
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