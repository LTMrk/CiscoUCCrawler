---
doc_id: webex-meeting-put-meetings-meetingid-simultaneousinterpretation
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: PUT
path: /meetings/{meetingId}/simultaneousInterpretation
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.397896+00:00
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
- `meetingId` [path] (string) **(requerido)**: Unique identifier for the meeting. Does not support meeting IDs for a scheduled [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings) meeting.

## Cuerpo de la petición (application/json)
- `enabled` (boolean) **(requerido)**: Whether or not simultaneous interpretation is enabled.
- `interpreters` (array): Interpreters for meeting.
  - `languageCode1` (string) **(requerido)**: Forms a set of simultaneous interpretation channels together with `languageCode2`. Standard language format from [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) code. Read [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for details.
  - `languageCode2` (string) **(requerido)**: Forms a set of simultaneous interpretation channels together with `languageCode1`. Standard language format from [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) code. Read [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for details.
  - `email` (string): Email address of meeting interpreter.
  - `displayName` (string): Display name of meeting interpreter.

### Ejemplo de petición
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

## Respuestas
- **200**: OK
  - `enabled` (boolean) **(requerido)**: Whether or not simultaneous interpretation is enabled.
  - `interpreters` (array): Interpreters for meeting.
    - `id` (string) **(requerido)**: Unique identifier for meeting interpreter.
    - `languageCode1` (string) **(requerido)**: Forms a set of simultaneous interpretation channels together with `languageCode2`. Standard language format from [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) code. Read [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for details.
    - `languageCode2` (string) **(requerido)**: Forms a set of simultaneous interpretation channels together with `languageCode1`. Standard language format from [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) code. Read [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for details.
    - `email` (string): Email address of meeting interpreter.
    - `displayName` (string): Display name of meeting interpreter.
- **400**: Bad Request
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
