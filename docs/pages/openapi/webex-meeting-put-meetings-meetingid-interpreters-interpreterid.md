---
doc_id: webex-meeting-put-meetings-meetingid-interpreters-interpreterid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: PUT
path: /meetings/{meetingId}/interpreters/{interpreterId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.398339+00:00
---

# PUT /meetings/{meetingId}/interpreters/{interpreterId}

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `updateInterpreterById`

## Resumen
Update a Meeting Interpreter

## Descripción
Updates details for a meeting interpreter identified by `meetingId` and `interpreterId` in the URI.

## Parámetros
- `meetingId` [path] (string) **(requerido)**: Unique identifier for the meeting whose interpreters were belong to.
- `interpreterId` [path] (string) **(requerido)**: Unique identifier for the interpreter whose details are being requested.

## Cuerpo de la petición (application/json)
- `languageCode1` (string) **(requerido)**: The pair of `languageCode1` and `languageCode2` form a bi-directional simultaneous interpretation language channel. The language codes conform with [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
- `languageCode2` (string) **(requerido)**: The pair of `languageCode1` and `languageCode2` form a bi-directional simultaneous interpretation language channel. The language codes conform with [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
- `email` (string): Email address of meeting interpreter. If not specified, it'll be an empty interpreter for the bi-directional language channel. Please note that multiple interpreters with different emails can be assigned to the same bi-directional language channel, but the same email cannot be assigned to more than one interpreter.
- `displayName` (string): Display name of meeting interpreter. If the interpreter is already an invitee of the meeting and it has a different display name, that invitee's display name will be overwritten by this attribute.
- `hostEmail` (string): Email address for the meeting host. This attribute should only be set if the user or application calling the API has the admin on-behalf-of scopes. When used, the admin may specify the email of a user in a site they manage to be the meeting host.
- `sendEmail` (boolean): If `true`, send email to the interpreter.

### Ejemplo de petición
```json
{
  "languageCode1": "en",
  "languageCode2": "de",
  "email": "marcus.tuchel@example.com",
  "displayName": "Tuchel"
}
```

## Respuestas
- **200**: OK
  - `id` (string) **(requerido)**: Unique identifier for meeting interpreter.
  - `languageCode1` (string) **(requerido)**: The pair of `languageCode1` and `languageCode2` form a bi-directional simultaneous interpretation language channel. The language codes conform with [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
  - `languageCode2` (string) **(requerido)**: The pair of `languageCode1` and `languageCode2` form a bi-directional simultaneous interpretation language channel. The language codes conform with [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
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
