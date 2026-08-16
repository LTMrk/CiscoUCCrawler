---
doc_id: webex-meeting-post-group-meetings-controls
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: POST
path: /group/meetings/controls
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.392882+00:00
---

# POST /group/meetings/controls

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `updateGroupMeetingControl`

## Resumen
Update Group Meeting Control Status

## Descripción
Update meeting recording control status by a service app which has group meeting access. The service app can use this API to start, stop, pause, or resume meeting recording by providing an `action` value. The `personId` parameter or `hostEmail` header of the person to whom the meeting belongs must be specified. The service app which invokes the API manages one or more groups, and it also manages one or more sites. The user specified by `hostEmail` or `personId` must be in a group that is managed by the service app. The meeting specified by `meetingId` must be on a site that is managed by the service app. Please note that once the meeting recording has been controlled by a person in the meeting, the recording control of this meeting can no longer be controlled by the service app via the API.

## Parámetros
- `personId` [query] (string): Person ID of the user whose meeting control will be updated. The person ID can be retrieved from the [People APIs](/docs/api/v1/people), e.g. [Lit People](/docs/api/v1/people/list-people). Note that a person ID retrieved from the People APIs is a Base64-encoded string, e.g. `Y2lzY29zcGFyazovL3VzL1BFT1BMRS9kNDdiMmU3ZC01ZTBmLTRmNjktYWVmNC1lNGZmOTBhZWE3Yzk`. The person ID in the raw UUID format which is the last part of the Base64-decoded string, e.g. `d47b2e7d-5e0f-4f69-aef4-e4ff90aea7c9`, is also supported. The `personId` parameter is optional, but one of the `personId` parameter and `hostEmail` header must be specified.
- `hostEmail` [header] (string): Email of the user whose meeting control will be updated. The `hostEmail` parameter is optional, but one of the `personId` parameter and `hostEmail` header must be specified.

## Cuerpo de la petición (application/json)
- `meetingId` (string) **(requerido)**: Unique identifier for the meeting.
- `action` (string) **(requerido)**: Action to apply to the meeting recording. Valores: startRecording, stopRecording, pauseRecording, resumeRecording.

### Ejemplo de petición
```json
{
  "meetingId": "560d7b784f5143e3be2fc3064a5c4999",
  "action": "startRecording"
}
```

## Respuestas
- **202**: Accepted: The update request has been accepted for processing.
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
