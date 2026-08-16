---
doc_id: webex-meeting-get-meetingparticipants-participantid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /meetingParticipants/{participantId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.386709+00:00
---

# GET /meetingParticipants/{participantId}

**API:** Webex Meetings
**Área:** Participants
**operationId:** `Get Meeting Participant Details`

## Resumen
Get Meeting Participant Details

## Descripción
Get a meeting participant details of a live or post meeting. The `participantId` is required to identify the meeting and the participant.

The authenticated user calling this API must either have an Administrator role with the `meeting:admin_participants_read` scope, or be the meeting host.

## Parámetros
- `participantId` [path] (string) **(requerido)**: The unique identifier for the meeting and the participant.
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes, the admin may specify the email of a user in a site they manage and the API will return meeting participants of the meetings that are hosted by that user.

## Respuestas
- **200**: OK
  - `id` (string): The ID that identifies the meeting and the participant.
  - `orgId` (string): The ID that identifies the organization. It only applies to participants of ongoing meetings.
  - `host` (boolean): Whether or not the participant is the host of the meeting.
  - `coHost` (boolean): Whether or not the participant has host privilege in the meeting.
  - `spaceModerator` (boolean): Whether or not the participant is the team space moderator. This field returns only if the meeting is associated with a Webex space.
  - `email` (string): The email address of the participant.
  - `displayName` (string): The name of the participant.
  - `invitee` (boolean): Whether or not the participant is invited to the meeting.
  - `muted` (boolean): Whether or not the participant's audio is muted.
  - `meetingStartTime` (string): The time the meeting started.
  - `video` (string): The status of the participant's video.  * `on` - The video is turned on.  * `off` - The video is turned off. Valores: on, off.
  - `state` (string): The status of the participant in the meeting. The value of `state` is `breakoutSession` which is only returned when the meeting is in progress and the breakout session is enabled.  * `lobby` - The participant is waiting in the meeting lobby.  * `end` - The participant has left the meeting.  * `joined` - The participant has joined the meeting and is in the main session.  * `breakoutSession` - The participant has joined a breakout session. Valores: lobby, end, joined, breakoutSession.
  - `breakoutSessionId` (string): The ID of the breakout session including the participant.
  - `joinedTime` (string): The time the participant joined the meeting. If the field is non-existent or shows `1970-01-01T00:00:00.000Z` the meeting may be still ongoing and the `joinedTime` will be filled in after the meeting ended. If you need real-time join events, please refer to the webhooks guide.
  - `leftTime` (string): The time the participant left the meeting. If the field is non-existent or shows `1970-01-01T00:00:00.000Z` the meeting may be still ongoing and the `leftTime` will be filled in after the meeting ended. If you need real-time left events, please refer to the webhooks guide.
  - `siteUrl` (string): The site URL.
  - `meetingId` (string): A unique identifier for the meeting which the participant belongs to.
  - `hostEmail` (string): The email address of the host.
  - `devices` (array):
    - `correlationId` (string): An internal ID that is associated with each join.
    - `deviceType` (string): The type of the device.
    - `audioType` (string): The audio type that the participant is using.  * `pstn` - `PSTN`  * `voip` - `VoIP`  * `inactive` - The participant is not connected to audio. Valores: pstn, voip, inactive.
    - `joinedTime` (string): The time the device joined the meeting. If the field is non-existent or shows `1970-01-    01T00:00:00.000Z` the meeting may be still ongoing and the `joinedTime` will be filled in after the meeting ended. If you need real-time joined     events, please refer to the webhooks guide.
    - `leftTime` (string): The time the device left the meeting, `leftTime` is the exact moment when a specific devi    ce left the meeting. If the field is non-existent or shows `1970-01-01T00:00:00.000Z` the meeting may be still ongoing and the `leftTime` will     be filled in after the meeting ended. If you need real-time left events, please refer to the webhooks guide.
    - `durationSecond` (number): The duration in seconds the device stayed in the meeting.
    - `callType` (string): The PSTN call type in which the device joined the meeting.  * `callIn` - Connect audio by dialing a toll or toll-free phone number provided by the meeting.  * `callBack` - Connect audio by dialing out a phone number from the meeting. Valores: callIn, callBack.
    - `phoneNumber` (string): The PSTN phone number from which the device joined the meeting. Only [compliance officer](/docs/compliance#compliance) can retrieve the `phoneNumber`. The meeting host and admin users cannot retrieve it. NOTE: The `phoneNumber` will be returned after the meeting ends; it is not returned while the meeting is in progress.
  - `breakoutSessionsAttended` (array): The breakout sessions attended by the participant. Only applies to ended meeting instances.
    - `id` (string): Unique identifier for the breakout session the participant attended.
    - `name` (string): Name of the breakout session the participant attended.
    - `joinedTime` (string): The time the participant joined the breakout session.
    - `leftTime` (string): The time the participant left the breakout session.
  - `sourceId` (string): The source ID of the participant. The `sourceId` is from the [Create Invitation Sources](/docs/api/v1/meetings/create-invitation-sources) API.
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
