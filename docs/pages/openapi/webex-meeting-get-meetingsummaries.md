---
doc_id: webex-meeting-get-meetingsummaries
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /meetingSummaries
operation_id: getSummaryByMeetingID
tags: Summaries
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.473448+00:00
---

# GET /meetingSummaries

**API:** Webex Meetings
**Área:** Summaries
**operationId:** `getSummaryByMeetingID`

## Resumen
Get Summary by Meeting ID

## Descripción
Get the summary of an ended [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) by the meeting ID.

Please note that only **meeting instances** in state `ended` are supported, and currently the meeting ID of a meeting series, a scheduled meeting, an in-progress meeting instance, or a scheduled personal room meeting is not supported for this API. This API can only fetch summaries that you have access to, and if a meeting summary is deleted, you won't be able to see it either. And, this is an API for normal user. If you are a compliance officer, please use the Get Summary For Compliance Officer API

## Parámetros
- `meetingId` [query] (string): Unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) to which the summary belongs. Please note that currently the meeting ID of a meeting series, a scheduled meeting, an in-progress meeting instance, or a scheduled personal room meeting is not supported for this API. If `meetingId` is not specified, the query will be rejected.

## Ejemplo de invocación
```bash
curl -X GET '/meetingSummaries' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): Meeting summary object.
  - `id` (string): A unique identifier for the summary.
  - `meetingId` (string): Unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) to which the summary belongs.
  - `status` (string): * `available` - Summary is available.  * `deleted` - Summary has been deleted.   Normal users can only see available summaries. Compliance officers can see both available and deleted summaries. Valores: available, deleted.
  - `notes` (object): Meeting summaries in HTML format
    - `content` (string) (**requerido**): Summary of the meeting in HTML format
  - `actionItems` (array): A list of action items
    - `content` (string) (**requerido**): Action item in plaintext

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "75ddf169-eef0-45b4-9faa-0112a16ec9d0",
      "meetingId": "0ed74a1c0551494fb7a04e2881bf50ae_I_166022169160077044",
      "status": "available",
      "notes": {
        "content": "<p>Summary of the meeting in HTML format</p>"
      },
      "actionItems": [
        {
          "content": "Action item No.1 in plaintext"
        },
        {
          "content": "Action item No.2 in plaintext"
        },
        {
          "content": "Action item No.3 in plaintext"
        }
      ]
    }
  ]
}
```

## Respuestas de error
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

## Contexto de la API
The Webex Meetings APIs enable developers to schedule, manage, and retrieve information about Webex meetings, webinars, and events. They provide endpoints for meeting creation, participant management, recordings, transcripts, in-meeting features such as chat and closed captions, and post-meeting analytics. Common use cases include integrating meeting scheduling into calendar apps, automating follow-ups with recordings and transcripts, embedding meeting controls in custom portals, and extracting insights for compliance or productivity analysis. The APIs support both real-time and asynchronous w...

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs