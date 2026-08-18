---
doc_id: webex-meeting-put-meetinginvitees-meetinginviteeid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: PUT
path: /meetingInvitees/{meetingInviteeId}
operation_id: Update a Meeting Invitee
tags: Invitees
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.465038+00:00
---

# PUT /meetingInvitees/{meetingInviteeId}

**API:** Webex Meetings
**Área:** Invitees
**operationId:** `Update a Meeting Invitee`

## Resumen
Update a Meeting Invitee

## Descripción
Update details for a meeting invitee identified by a `meetingInviteeId` in the URI.

## Parámetros
- `meetingInviteeId` [path] (string) (**requerido**): Unique identifier for the invitee to be updated. This parameter only applies to an invitee to a meeting series or a scheduled meeting. It doesn't apply to an invitee to an ended or ongoing meeting instance.

## Cuerpo de la petición (application/json)
- `email` (string) (**requerido**): Email address for meeting invitee.
- `displayName` (string): Display name for meeting invitee. The maximum length of `displayName` is 128 characters. In the Webex app, if the email has been associated with an existing Webex account, the display name associated with the Webex account will be used; otherwise, the `email` will be used as `displayName`. In a Webex site, if `displayName` is specified, it will show `displayName`. If `displayName` is not specified, and the `email` has been associated with an existing Webex account, the display name associated with the Webex account will be used; otherwise, the `email` will be used as `displayName`.  If the invitee has an existing Webex account, the `displayName` shown in the meeting will be the `displayName` associated with the Webex account; otherwise, `displayName` shown in the meeting will be the `displayName` which is specified by the invitee who does not have a Webex account.
- `coHost` (boolean): Whether or not the invitee is a designated alternate host for the meeting. See [Add Alternate Hosts for Cisco Webex Meetings](https://help.webex.com/b5z6he/) for more details.
- `hostEmail` (string): Email address for the meeting host. This attribute should only be set if the user or application calling the API has the admin on-behalf-of scopes. When used, the admin may specify the email of a user in a site they manage to be the meeting host.
- `sendEmail` (boolean): If `true`, send an email to the invitee.
- `panelist` (boolean): If `true`, the invitee is a designated panelist for the event meeting.

### Ejemplo — petición
```json
{
  "email": "john.andersen@example.com",
  "displayName": "John Andersen",
  "coHost": false,
  "hostEmail": "brenda.song@example.com",
  "panelist": false,
  "sendEmail": true
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/meetingInvitees/<meetingInviteeId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"email": "<email>"}'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Unique identifier for meeting invitee.
- `email` (string) (**requerido**): Email address for meeting invitee. This attribute can be modified by `Update a Meeting Invitee` API.
- `displayName` (string) (**requerido**): Display name for meeting invitee. This attribute can be modified by `Update a Meeting Invitee` API.
- `coHost` (boolean): Whether or not invitee is a designated alternate host for the meeting. See [Add Alternate Hosts for Cisco Webex Meetings](https://help.webex.com/b5z6he/) for more details.
- `meetingId` (string) (**requerido**): Unique identifier for the meeting for which invitees are being requested. The meeting can be a meeting series, a scheduled meeting, or a meeting instance which has ended or is ongoing.
- `panelist` (boolean): If `true`, the invitee is a designated panelist for the event meeting.

### Ejemplo — respuesta 200
```json
{
  "id": "870f51ff287b41be84648412901e0402_2628962",
  "email": "john.andersen@example.com",
  "displayName": "John Andersen",
  "coHost": false,
  "panelist": false,
  "meetingId": "870f51ff287b41be84648412901e0402"
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict
  Ejemplo:
```json
{
  "message": "User is already a meeting invitee.",
  "errors": [
    {
      "description": "User is already a meeting invitee."
    }
  ],
  "trackingId": "8E12317727354470B5258F5B28D93FB9_1562296858685"
}
```
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