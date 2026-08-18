---
doc_id: webex-meeting-put-meetingparticipants-participantid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: PUT
path: /meetingParticipants/{participantId}
operation_id: Update a Participant
tags: Participants
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.466508+00:00
---

# PUT /meetingParticipants/{participantId}

**API:** Webex Meetings
**Área:** Participants
**operationId:** `Update a Participant`

## Resumen
Update a Participant

## Descripción
Mute, un-mute, expel, or admit a participant in a live meeting. The `participantId` is required to identify the meeting and the participant.

Notes:

* The owner of the OAuth token calling this API needs to be the meeting host or co-host.

* The `expel` attribute always takes precedence over `admit` and `muted`. The request can have all `expel`, `admit` and `muted` or any of them.

<div><Callout type="warning">There is an inconsistent behavior in Webex Meetings App when all active meeting participants join using Webex Meetings App and the host attempts to change meeting participant status using this API. Requests to mute, un-mute, admit, or expel a meeting participant return a successful response and update the state in the API, but the changes will not be applied to the Webex Meetings App participants. The inconsistent behavior in Webex Meetings App will be corrected in a future release.
**Workaround**: [Enable closed captions](https://help.webex.com/en-us/article/WBX47352/How-Do-I-Enable-Closed-Captions?) or enable the [Webex Assistant](https://help.webex.com/en-us/article/n91uf2x/Turn-on-or-turn-off-Webex-Assistant-during-a-meeting-or-webinar).</Callout></div>

## Parámetros
- `participantId` [path] (string) (**requerido**): The unique identifier for the meeting and the participant.

## Cuerpo de la petición (application/json)
- `muted` (boolean): If `true`, participant is muted.
- `admit` (boolean): If `true` the participant admit a participant in the lobby to the meeting. Has no effect if the participant is not in the lobby or when the value is set to `false`.
- `expel` (boolean): If `true` the participant is expelled from the meeting.

### Ejemplo — petición
```json
{
  "muted": false
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/meetingParticipants/<participantId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- `id` (string): The participant ID that identifies the meeting and the participant.
- `orgId` (string): The ID that identifies the organization.
- `host` (boolean): Whether or not the participant is the host of the meeting.
- `coHost` (boolean): Whether or not the participant has host privilege in the meeting.
- `spaceModerator` (boolean): Whether or not the participant is the team space moderator. This field returns only if the meeting is associated with a Webex space.
- `email` (string): The email address of the participant.
- `displayName` (string): The name of the participant.
- `invitee` (boolean): Whether or not the participant is invited to the meeting.
- `video` (string): The status of the participant's video.  * `on` - The video is turned on.  * `off` - The video is turned off. Valores: on, off.
- `muted` (boolean): Whether or not the participant's audio is muted.
- `state` (string): The status of the participant in the meeting.  * `lobby` - The participant is waiting in the meeting lobby.  * `joined` - The participant has joined the meeting. Valores: lobby, joined.
- `siteUrl` (string): The site URL.
- `meetingId` (string): A unique identifier for the meeting which the participant belongs to.
- `hostEmail` (string): The email address of the host.
- `devices` (array):
  - `correlationId` (string): An internal ID that is associated with each join.
  - `deviceType` (string): The type of device.
  - `audioType` (string): The audio type that the participant is using.  * `pstn` - `PSTN`  * `voip` - `VoIP`  * `inactive` - The participant is not connected to audio. Valores: pstn, voip, inactive.
  - `joinedTime` (string): The time the device joined the meeting. If the field is non-existent or shows `1970-01-01T00:00:00.000Z` the meeting may be still ongoing and the `joinedTime` will be filled in after the meeting ended. If you need real-time joined events, please refer to the webhooks guide.
  - `leftTime` (string): The time the device left the meeting, `leftTime` is the exact moment when a specific device left the meeting. If the field is non-existent or shows `1970-01-01T00:00:00.000Z` the meeting may be still ongoing and the `leftTime` will be filled in after the meeting ended. If you need real-time left events, please refer to the webhooks guide.

### Ejemplo — respuesta 200
```json
{
  "id": "560d7b784f5143e3be2fc3064a5c4999_3c2e2338-e950-43bf-b588-573773ee43d1",
  "orgId": "1eb65fdf-9643-417f-9974-ad72cae0e10f",
  "host": true,
  "coHost": false,
  "spaceModerator": false,
  "email": "joeDoe@cisco.com",
  "displayName": "Joe Doe",
  "invitee": false,
  "video": "on",
  "muted": false,
  "state": "lobby",
  "siteUrl": "example.webex.com",
  "meetingId": "3a688f62840346e8b87dde2b50703511_I_197977258267247872",
  "hostEmail": "janeDoe@cisco.com",
  "devices": [
    {
      "correlationId": "8ccced6c-b812-4dff-a5dd-4c5c28f8d47d",
      "deviceType": "mac",
      "audioType": "pstn",
      "joinedTime": "2019-04-23T17:31:00.000Z",
      "leftTime": "2019-04-23T17:32:00.000Z"
    }
  ]
}
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