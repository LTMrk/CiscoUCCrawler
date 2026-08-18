---
doc_id: webex-meeting-get-meetingclosedcaptions-closedcaptionid-download
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /meetingClosedCaptions/{closedCaptionId}/download
operation_id: downloadTranscript
tags: Closed Captions
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.463863+00:00
---

# GET /meetingClosedCaptions/{closedCaptionId}/download

**API:** Webex Meetings
**Área:** Closed Captions
**operationId:** `downloadTranscript`

## Resumen
Download Meeting Closed Caption Snippets

## Descripción
Download meeting closed caption snippets from the meeting closed caption specified by `closedCaptionId` formatted either as a Video Text Track (.vtt) file or plain text (.txt) file.

#### Request Header

* `timezone`: *[Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) for time stamps in response body, defined in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default value is `UTC` if not specified.*

## Parámetros
- `closedCaptionId` [path] (string) (**requerido**): Unique identifier for the meeting closed caption.
- `format` [query] (string): Format for the downloaded meeting closed caption snippets. Valores: vtt, txt. Por defecto: vtt.
- `meetingId` [query] (string) (**requerido**): Unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) which the closed caption snippets belong to. This parameter only applies to meeting instances in the `ended` state. It does not apply to meeting series, scheduled meetings or scheduled [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings) meetings.
- `timezone` [header] (string): e.g. UTC

## Ejemplo de invocación
```bash
curl -X GET '/meetingClosedCaptions/<closedCaptionId>/download?meetingId=<meetingId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK

### Ejemplo — respuesta 200
```json
"WEBVTT\n\n1\n00:00:20.904 --> 00:00:24.564\nThis is an s sample closed caption snippet.\n\n2\n00:00:31.014 --> 00:00:33.744\nTesting out download closed captions.\n"
```

### Ejemplo — respuesta 200
```json
"WEBVTT\n\n1\n00:00:20.904 --> 00:00:24.564\nThis is an s sample closed caption snippet.\n\n2\n00:00:31.014 --> 00:00:33.744\nTesting out download closed captions.\n"
```

### Ejemplo — respuesta 200
```json
"WEBVTT\n\n1\n00:00:20.904 --> 00:00:24.564\nThis is an s sample closed caption snippet.\n\n2\n00:00:31.014 --> 00:00:33.744\nTesting out download closed captions.\n"
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