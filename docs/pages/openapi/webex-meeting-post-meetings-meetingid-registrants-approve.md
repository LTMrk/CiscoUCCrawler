---
doc_id: webex-meeting-post-meetings-meetingid-registrants-approve
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: POST
path: /meetings/{meetingId}/registrants/approve
operation_id: batchApproveMeetingRegistrants
tags: Meetings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.486722+00:00
---

# POST /meetings/{meetingId}/registrants/approve

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `batchApproveMeetingRegistrants`

## Resumen
Batch Approve Meeting Registrants

## Descripción
Batch approve a set of registrants for a meeting by the meeting host or cohost.

## Parámetros
- `meetingId` [path] (string) (**requerido**): Unique identifier for the meeting. Only the ID of the meeting series is supported for meetingId. IDs of scheduled meetings, meeting instances, or scheduled personal room meetings are not supported. See the [Meetings Overview](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) for more information about meeting types.
- `current` [query] (boolean): Whether or not to retrieve only the current scheduled meeting of the meeting series, i.e. the meeting ready to join or start or the upcoming meeting of the meeting series. If it's `true`, return details for the current scheduled meeting of the series, i.e. the scheduled meeting ready to join or start or the upcoming scheduled meeting of the meeting series. If it's `false` or not specified, return details for the entire meeting series. This parameter only applies to meeting series.     + Default: `false`
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes. If set, the admin may specify the email of a user in a site they manage and the API will return details for a meeting that is hosted by that user.

## Cuerpo de la petición (application/json)
- `sendEmail` (boolean): If `true` send email to registrants. Default: `true`.
- `registrants` (array): Registrants array.
  - `id` (string) (**requerido**): Registrant ID.

### Ejemplo — petición
```json
{
  "sendEmail": true,
  "registrants": [
    {
      "id": "6e341788-3bad-4bf0-8037-93709fe8b427"
    },
    {
      "id": "8919b6bf-01f6-4693-9c0b-cc75e956ba06"
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X POST '/meetings/<meetingId>/registrants/approve' \
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