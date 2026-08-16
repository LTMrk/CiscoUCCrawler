---
doc_id: webex-meeting-get-meetingparticipants
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /meetingParticipants
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.386381+00:00
---

# GET /meetingParticipants

**API:** Webex Meetings
**Área:** Participants
**operationId:** `List Meeting Participants`

## Resumen
List Meeting Participants

## Descripción
List all participants in an in-progress meeting or an ended meeting. The `meetingId` parameter is required, which is the unique identifier for the meeting.

The authenticated user calling this API must either have an Administrator role with the `meeting:admin_participants_read` scope, or be the meeting host.

* If the `meetingId` value specified is for a meeting series, the operation returns participants' details for the last instance in the meeting series. If the `meetingStartTimeFrom` value and the `meetingStartTimeTo` value are specified, the operation returns participants' details for the last instance in the meeting series in the time range.

* If the `meetingId` value specified is for a scheduled meeting from a meeting series, the operation returns participants' details for that scheduled meeting. If the `meetingStartTimeFrom` value and the `meetingStartTimeTo` value are specified, the operation returns participants' details for the last instance in the scheduled meeting in the time range.

* If the `meetingId` value specified is for a meeting instance which is in progress or ended, the operation returns participants' details for that meeting instance.

* If the meeting is in progress, the operation returns all the real-time participants. If the meeting is ended, the operation returns all the participants that have joined the meeting.

* If the `breakoutSessionId` parameter is specified, the operation returns participants who joined the specified breakout session. It only applies to end meeting instances.

* The `breakoutSessionsAttended` attribute is only returned for a participant of an ended meeting instance if the participant joined breakout sessions in the meeitng.

* The `meetingStartTimeFrom` and `meetingStartTimeTo` only apply when `meetingId` is a series ID or an occurrence ID.

* If the webinar is in progress when the attendee has ever been unmuted to speak in the webinar, this attendee becomes a panelist. The operation returns include the people who have been designated as panelists when the webinar is created and have joined the webinar, and the attendees who have joined the webinar and are unmuted to speak in the webinar temporarily. If the webinar is ended, the operation returns all the participants, including all panelists and all attendees who are not panelists.

#### Request Header

* `timezone`: Time zone for time stamps in the response body, defined in conformance with the [IANA time zone database](https://www.iana.org/time-zones).

## Parámetros
- `max` [query] (number): Limit the maximum number of participants in the response, up to 100.
- `meetingId` [query] (string) **(requerido)**: The unique identifier for the meeting. Please note that currently meeting ID of a scheduled [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings) meeting is not supported for this API.
- `breakoutSessionId` [query] (string): The unique identifier for a breakout session which happened during an ended meeting instance. If the `breakoutSessionId` is specified, the operation returns participants who joined the breakout session. Only applies to ended meeting instances.
- `meetingStartTimeFrom` [query] (string): Meetings start from the specified date and time(exclusive) in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. If `meetingStartTimeFrom` is not specified, it equals `meetingStartTimeTo` minus 1 month; if `meetingStartTimeTo` is also not specified, the default value for `meetingStartTimeFrom` is 1 month before current date and time.
- `meetingStartTimeTo` [query] (string): Meetings start before the specified date and time(exclusive) in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. If `meetingStartTimeTo` is not specified, it equals the result of a comparison, `meetingStartTimeFrom` plus one month and the current time, and the result is the earlier of the two; if `meetingStartTimeFrom` is also not specified, the default value for `meetingStartTimeTo` is current date and time minus 1 month.
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes, the admin may specify the email of a user in a site they manage and the API will return meeting participants of the meetings that are hosted by that user.
- `joinTimeFrom` [query] (string): The time participants join a meeting starts from the specified date and time (inclusive) in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. If `joinTimeFrom` is not specified, it equals `joinTimeTo` minus 7 days.
- `joinTimeTo` [query] (string): The time participants join a meeting before the specified date and time (exclusive) in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. If `joinTimeTo` is not specified, it equals `joinTimeFrom` plus 7 days. The interval between `joinTimeFrom` and `joinTimeTo` must be within 90 days.
- `timezone` [header] (string): e.g. UTC

## Respuestas
- **200**: OK
  - `items` (array):
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
