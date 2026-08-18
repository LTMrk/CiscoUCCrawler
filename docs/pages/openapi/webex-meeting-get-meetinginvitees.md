---
doc_id: webex-meeting-get-meetinginvitees
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /meetingInvitees
operation_id: List Meeting Invitees
tags: Invitees
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.464057+00:00
---

# GET /meetingInvitees

**API:** Webex Meetings
**Área:** Invitees
**operationId:** `List Meeting Invitees`

## Resumen
List Meeting Invitees

## Descripción
Lists meeting invitees for a meeting with a specified `meetingId`. You can set a maximum number of invitees to return.

This operation can be used for meeting series, scheduled meetings, and ended or ongoing meeting instance objects. If the specified `meetingId` is for a meeting series, the invitees for the series will be listed; if the `meetingId` is for a scheduled meeting, the invitees for the particular scheduled meeting will be listed; if the `meetingId` is for an ended or ongoing meeting instance, the invitees for the particular meeting instance will be listed. See the [Webex Meetings](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) guide for more information about the types of meetings.

The list returned is sorted in ascending order by email address.

Long result sets are split into [pages](/docs/basics#pagination).

## Parámetros
- `meetingId` [query] (string) (**requerido**): Unique identifier for the meeting for which invitees are being requested. The meeting can be a meeting series, a scheduled meeting, or a meeting instance which has ended or is ongoing. The meeting ID of a scheduled [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings) meeting is not supported for this API.
- `max` [query] (number): Limit the maximum number of meeting invitees in the response, up to 100. Por defecto: 10.
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin on-behalf-of scopes. If set, the admin may specify the email of a user in a site they manage and the API will return meeting invitees that are hosted by that user.
- `panelist` [query] (string): Filter invitees or attendees for webinars only. If `true`, returns invitees. If `false`, returns attendees. If `null`, returns both invitees and attendees.

## Ejemplo de invocación
```bash
curl -X GET '/meetingInvitees?meetingId=<meetingId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): Array of meeting invitees.
  - `id` (string) (**requerido**): Unique identifier for meeting invitee.
  - `email` (string) (**requerido**): Email address for meeting invitee. This attribute can be modified by `Update a Meeting Invitee` API.
  - `displayName` (string) (**requerido**): Display name for meeting invitee. This attribute can be modified by `Update a Meeting Invitee` API.
  - `coHost` (boolean): Whether or not invitee is a designated alternate host for the meeting. See [Add Alternate Hosts for Cisco Webex Meetings](https://help.webex.com/b5z6he/) for more details.
  - `meetingId` (string) (**requerido**): Unique identifier for the meeting for which invitees are being requested. The meeting can be a meeting series, a scheduled meeting, or a meeting instance which has ended or is ongoing.
  - `panelist` (boolean): If `true`, the invitee is a designated panelist for the event meeting.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "870f51ff287b41be84648412901e0402_2628957",
      "email": "john.andersen@example.com",
      "displayName": "John Andersen",
      "coHost": false,
      "panelist": false,
      "meetingId": "870f51ff287b41be84648412901e0402"
    },
    {
      "id": "870f51ff287b41be84648412901e0402_2628962",
      "email": "brenda.song@example.com",
      "displayName": "Brenda Song",
      "coHost": false,
      "panelist": false,
      "meetingId": "870f51ff287b41be84648412901e0402"
    }
  ]
}
```
- Cabecera `Link`: 

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