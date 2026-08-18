---
doc_id: webex-meeting-put-meetings-meetingid-simultaneousinterpretation
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: PUT
path: /meetings/{meetingId}/simultaneousInterpretation
operation_id: updateMeetingSimultaneousInterpretation
tags: Meetings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.487646+00:00
---

# PUT /meetings/{meetingId}/simultaneousInterpretation

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `updateMeetingSimultaneousInterpretation`

## Resumen
Update Meeting Simultaneous interpretation

## Descripción
Updates simultaneous interpretation options of a meeting with a specified meeting ID. This operation applies to meeting series and scheduled meetings. It doesn't apply to ended or in-progress meeting instances.

## Parámetros
- `meetingId` [path] (string) (**requerido**): Unique identifier for the meeting. Does not support meeting IDs for a scheduled [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings) meeting.

## Cuerpo de la petición (application/json)
- `enabled` (boolean) (**requerido**): Whether or not simultaneous interpretation is enabled.
- `interpreters` (array): Interpreters for meeting.
  - `languageCode1` (string) (**requerido**): Forms a set of simultaneous interpretation channels together with `languageCode2`. Standard language format from [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) code. Read [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for details.
  - `languageCode2` (string) (**requerido**): Forms a set of simultaneous interpretation channels together with `languageCode1`. Standard language format from [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) code. Read [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for details.
  - `email` (string): Email address of meeting interpreter.
  - `displayName` (string): Display name of meeting interpreter.

### Ejemplo — petición
```json
{
  "enabled": true,
  "interpreters": [
    {
      "languageCode1": "en",
      "languageCode2": "de",
      "email": "marcus.hoffmann@example.com",
      "displayName": "Hoffmann"
    }
  ],
  "hostEmail": "john.andersen@example.com"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/meetings/<meetingId>/simultaneousInterpretation' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"enabled": true}'
```

## Respuestas correctas
**200**: OK
- `enabled` (boolean) (**requerido**): Whether or not simultaneous interpretation is enabled.
- `interpreters` (array): Interpreters for meeting.
  - `id` (string) (**requerido**): Unique identifier for meeting interpreter.
  - `languageCode1` (string) (**requerido**): Forms a set of simultaneous interpretation channels together with `languageCode2`. Standard language format from [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) code. Read [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for details.
  - `languageCode2` (string) (**requerido**): Forms a set of simultaneous interpretation channels together with `languageCode1`. Standard language format from [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) code. Read [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for details.
  - `email` (string): Email address of meeting interpreter.
  - `displayName` (string): Display name of meeting interpreter.

### Ejemplo — respuesta 200
```json
{
  "enabled": true,
  "interpreters": [
    {
      "id": "OGQ0OGRiM2U3ZTAxNDZiMGFjYzJjMzYxNDNmNGZhN2RfZTA5MTJiZDBjNWVlNDA4YjgxMTZlMjU4Zjg2NWIzZmM",
      "languageCode1": "en",
      "languageCode2": "de",
      "email": "marcus.hoffmann@example.com",
      "displayName": "Hoffmann"
    }
  ]
}
```

## Respuestas de error
- **400**: Bad Request
  Ejemplo:
```json
{
  "message": "The request could not be understood by the server due to malformed syntax. See 'errors' for more details.",
  "errors": [
    {
      "description": "'interpreters' should be empty when simultaneous interpretation is disabled."
    }
  ],
  "trackingId": "19085D1FCFEE445DA358375500D25E44_1598154356721"
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