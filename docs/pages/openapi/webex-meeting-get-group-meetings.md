---
doc_id: webex-meeting-get-group-meetings
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /group/meetings
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.392310+00:00
---

# GET /group/meetings

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `listGroupMeetings`

## Resumen
List Group Meetings

## Descripción
List group meetings with a specified meeting number or web link by a service app which has group meeting access. You can specify the `personId` parameter or `hostEmail` header of whom the meetings will be retrieved. Please note that there are various products in the [Webex Suite](https://www.webex.com/collaboration-suite.html) such as `Meetings` and `Events`. Currently, only meetings of the `Meetings` product are supported by this API, meetings of others in the suite are not supported. Ad-hoc meetings created by [Create a Meeting](/docs/api/v1/meetings/create-a-meeting) with `adhoc` of `true` and a `roomId` will not be listed.

* One of the `personId` parameter and `hostEmail` header must be specified so that only meetings hosted by the person of `personId` or `hostEmail` will be listed.

* `meetingNumber` and `webLink` are mutually exclusive and they cannot be specified simultaneously, but one of them must be specified. The operation returns an array of meeting objects specified by the `meetingNumber` or `webLink`.

* Each object in the array can be a scheduled meeting or a meeting series depending on whether the `current` parameter is `true` or `false`. If it's `false`, the `start` and `end` attributes are for the first scheduled meeting of that series. If it's `true` or not specified, the `start` and `end` attributes are for the scheduled meeting which is ready to start or join or the upcoming scheduled meeting of that series.

* To learn more about which attributes are available for different meeting states, please refer to [Available Meeting Attributes for Different Meeting States](/docs/meetings#available-meeting-attributes-for-different-meeting-states).

#### Request Header

* `timezone`: [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) for time stamps in response body, defined in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default value is `UTC` if not specified.

* `hostEmail`: Email of the user whose meetings will be retrieved. The `hostEmail` parameter is optional, but one of the `personId` parameter and `hostEmail` header must be specified.

## Parámetros
- `personId` [query] (string): Person ID of the user whose meetings will be retrieved. The person ID can be retrieved from the [People APIs](/docs/api/v1/people), e.g. [Lit People](/docs/api/v1/people/list-people). Note that a person ID retrieved from the People APIs is a Base64-encoded string, e.g. `Y2lzY29zcGFyazovL3VzL1BFT1BMRS9kNDdiMmU3ZC01ZTBmLTRmNjktYWVmNC1lNGZmOTBhZWE3Yzk`. The person ID in the raw UUID format which is the last part of the Base64-decoded string, e.g. `d47b2e7d-5e0f-4f69-aef4-e4ff90aea7c9`, is also supported. The `personId` parameter is optional, but one of the `personId` parameter and `hostEmail` header must be specified.
- `meetingNumber` [query] (string): Meeting number for the meeting objects being requested. `meetingNumber` and `webLink` are mutually exclusive. If it's an exceptional meeting from a meeting series, the exceptional meeting instead of the primary meeting series is returned.
- `webLink` [query] (string): URL encoded link to information page for the meeting objects being requested. `meetingNumber` and `webLink` are mutually exclusive.
- `current` [query] (boolean): Flag identifying to retrieve the current scheduled meeting of the meeting series or the entire meeting series. This parameter only applies to scenarios where the meeting is not an exceptional meeting from a meeting series. If it's `true`, return the scheduled meeting of the meeting series which is ready to join or start or the upcoming scheduled meeting of the meeting series; if it's `false`, return the entire meeting series. The default value is `true`.
- `timezone` [header] (string): [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) for time stamps in response body, defined in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default value is `UTC` if not specified.
- `hostEmail` [header] (string): Email of the user whose meetings will be retrieved. The `hostEmail` parameter is optional, but one of the `personId` parameter and `hostEmail` header must be specified.

## Respuestas
- **200**: OK
  - `items` (array): Meetings array.
    - `id` (string) **(requerido)**: Unique identifier for meeting. For a meeting series, the `id` is used to identify the entire series. For scheduled meetings from a series, the `id` is used to identify that scheduled meeting. For a meeting instance that is in progress or has concluded, the `id` is used to identify that instance.
    - `meetingSeriesId` (string) **(requerido)**: Unique identifier for meeting series. It only apples to scheduled meeting and meeting instance. If it's a scheduled meeting from a series or a meeting instance that is happening or has happened, the `meetingSeriesId` is the `id` of the primary series.
    - `scheduledMeetingId` (string): Unique identifier for scheduled meeting which current meeting is associated with. It only apples to meeting instance which is happening or has happened. It's the `id` of the scheduled meeting this instance is associated with.
    - `meetingNumber` (string): Meeting number. Applies to meeting series, scheduled meeting, and meeting instances, but not to meeting instances which have ended.
    - `title` (string) **(requerido)**: Meeting title. Can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
    - `meetingType` (string) **(requerido)**: Meeting type.  * `meetingSeries` - Primary instance of a scheduled series of meetings which consists of one or more scheduled meetings based on a `recurrence` rule. When a non-recurring meeting is scheduled with no `recurrence`, its `meetingType` is also `meetingSeries` which is a meeting series with only one occurrence in Webex meeting modeling.  * `scheduledMeeting` - Instance from a primary meeting series.  * `meeting` - Meeting instance that is in progress or has completed. Valores: meetingSeries, scheduledMeeting, meeting.
    - `state` (string) **(requerido)**: Meeting state.  * `active` - Only applies to a meeting series. Indicates that one or more future scheduled meetings exist for this meeting series.  * `scheduled` - Only applies to scheduled meeting. Indicates that the meeting is scheduled in the future.  * `ready` - Only applies to scheduled meeting. Indicates that this scheduled meeting is ready to start or join immediately.  * `lobby` - Only applies to meeting instances. Indicates that a locked meeting has been joined by participants, but no hosts have joined.  * `inProgress` - Applies to meeting series and meeting instance. For meeting series, indicates that an instance of this series is in progress; for a meeting instances, indicates that the meeting has been joined and unlocked.  * `ended` - Applies to scheduled meetings and meeting instances. For scheduled meetings, indicates that the meeting was started and is now over. For meeting instances, indicates that the meeting instance has concluded.  * `missed` - This state only applies to scheduled meetings. Indicates that the meeting was scheduled in the past but never happened.  * `expired` - This state only applies to a meeting series. Indicates that all scheduled meetings of this series have passed. Valores: active, scheduled, ready, lobby, inProgress, ended, missed, expired.
    - `hostDidJoin` (boolean): Only applies to meeting series in the `inProgress` state, scheduled meetings in the `ready` state, and meeting instances in the `inProgress` state, whether or not the meeting host joined the meeting. If true, the meeting host has joined the meeitng even if they dropped off; otherwise, the meeting host hasn't ever join the meeting. Indicates that someone is waiting in the lobby and the host hasn't joined the meeting if `attendeeDidJoin` is true and `hostDidJoin` is false.
    - `attendeeDidJoin` (boolean): Only applies to meeting series in the `inProgress` state, scheduled meetings in the `ready` state, and meeting instances in the `inProgress` state. Whether or not anyone has joined the meeting. If true, the meeting host or any attendee has joined the meeting; otherwise, no one has joined the meeting. Indicates that someone is waiting in the lobby and the host hasn't joined the meeting if `attendeeDidJoin` is true and `hostDidJoin` is false.
    - `isModified` (boolean): This state only applies to scheduled meeting. Flag identifying whether or not the scheduled meeting has been modified.
    - `timezone` (string) **(requerido)**: [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) of `start` and `end`, conforming with the [IANA time zone database](https://www.iana.org/time-zones).
    - `start` (string) **(requerido)**: Start time for meeting in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. If the meetingType of a meeting is `meetingSeries`, `start` is the scheduled start time of the first occurrence of this series. If the meeting is a meeting series and the `current` filter is true, `start` is the date and time the upcoming or ongoing meeting of the series starts. If the meetingType of a meeting is `scheduledMeeting`, `start` is the scheduled start time of this occurrence. If the meetingType of a meeting is `meeting`, `start` is the actual start time of the meeting instance. Can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
    - `end` (string) **(requerido)**: End time for a meeting in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. If the meetingType of a meeting is `meetingSeries`, `end` is the scheduled end time of the first occurrence of this series. If the meeting is a meeting series and the current filter is true, `end` is the date and time the upcoming or ongoing meeting of the series ends. If the meetingType of a meeting is `scheduledMeeting`, `end` is the scheduled end time of this occurrence. If the meetingType of a meeting is `meeting`, `end` is the actual end time of the meeting instance. If a meeting instance is in progress, `end` is not available. Can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
    - `recurrence` (string): Meeting series recurrence rule (conforming with [RFC 2445](https://www.ietf.org/rfc/rfc2445.txt)). Applies only to a recurring meeting series, not to a meeting series with only one scheduled meeting. Can be modified for a meeting series using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API. Multiple days or dates for monthly or yearly `recurrence` rule are not supported, only the first day or date specified is taken. For example, "FREQ=MONTHLY;INTERVAL=1;COUNT=10;BYMONTHDAY=10,11,12" is not supported and it will be partially supported as "FREQ=MONTHLY;INTERVAL=1;COUNT=10;BYMONTHDAY=10".
    - `hostUserId` (string) **(requerido)**: Unique identifier for the meeting host.
    - `hostDisplayName` (string) **(requerido)**: Display name for the meeting host.
    - `hostEmail` (string) **(requerido)**: Email address for the meeting host.
    - `siteUrl` (string) **(requerido)**: Site URL for the meeting.
    - `roomId` (string): Room ID of the associated Webex space. Only applies to ad-hoc meetings and space meetings.
    - `enabledAutoRecordMeeting` (boolean): Whether or not meeting is recorded automatically. Can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
    - `allowAnyUserToBeCoHost` (boolean): Whether or not to allow any attendee with a host account on the target site to become a cohost when joining the meeting. The target site is specified by a `siteUrl` parameter when creating the meeting. If not specified, it's a user's preferred site. The `allowAnyUserToBeCoHost` attribute can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
    - `enabledJoinBeforeHost` (boolean): Whether or not to allow any attendee to join the meeting before the host joins the meeting. The `enabledJoinBeforeHost` attribute can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
    - `enableConnectAudioBeforeHost` (boolean): Whether or not to allow any attendee to connect to audio before the host joins the meeting. Only applicable if the `enabledJoinBeforeHost` attribute is set to `true`. The `enableConnectAudioBeforeHost` attribute can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
    - `joinBeforeHostMinutes` (number): Number of minutes an attendee can join the meeting before the meeting start time and the host joins. Only applicable if the `enabledJoinBeforeHost` attribute is set to true. The `joinBeforeHostMinutes` attribute can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API. Valid options for a meeting are `0`, `5`, `10`, and `15`, and valid options for a webinar are `0`, `15`, `30`, `45`, and `60`. The default is `0` if not specified.
    - `excludePassword` (boolean): Whether or not to exclude the meeting password from the email invitation.
    - `publicMeeting` (boolean): Whether or not to allow the meeting to be listed on the public calendar.
    - `reminderTime` (number): The number of minutes before the meeting begins, that an email reminder is sent to the host.
    - `unlockedMeetingJoinSecurity` (string): Specifies how the people who aren't on the invite can join the unlocked meeting.  * `allowJoin` - If the value of `unlockedMeetingJoinSecurity` attribute is `allowJoin`, people can join the unlocked meeting directly.  * `allowJoinWithLobby` - If the value of `unlockedMeetingJoinSecurity` attribute is `allowJoinWithLobby`, people will wait in the lobby until the host admits them.  * `blockFromJoin` - If the value of `unlockedMeetingJoinSecurity` attribute is `blockFromJoin`, people can't join the unlocked meeting. Valores: allowJoin, allowJoinWithLobby, blockFromJoin.
    - `sessionTypeId` (number): Unique identifier for a meeting session type for the user. This attribute is required when scheduling a webinar meeting. All available meeting session types enabled for the user can be retrieved using the [List Meeting Session Types](/docs/api/v1/meetings/list-meeting-session-types) API.
    - `scheduledType` (string): Specifies whether the meeting is a regular meeting, a webinar, or a meeting scheduled in the user's [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings).  * `meeting` - If the value of `scheduledType` attribute is `meeting`, it is a regular meeting.  * `webinar` - If the value of `scheduledType` attribute is `webinar`, it is a webinar meeting.  * `personalRoomMeeting` - If the value of `scheduledType` attribute is `personalRoomMeeting`, it is a meeting scheduled in the user's [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings). Valores: meeting, webinar, personalRoomMeeting.
    - `enabledWebcastView` (boolean): Whether or not webcast view is enabled.
    - `enableAutomaticLock` (boolean): Whether or not to automatically lock the meeting after it starts.
    - `automaticLockMinutes` (number): The number of minutes after the meeting begins, for automatically locking it.
    - `allowFirstUserToBeCoHost` (boolean): Whether or not to allow the first attendee of the meeting with a host account on the target site to become a cohost. The target site is specified by the `siteUrl` parameter when creating the meeting. If not specified, it's a user's preferred site. The `allowFirstUserToBeCoHost` attribute can be modified for a meeting series or a scheduled meeting uisng the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
    - `allowAuthenticatedDevices` (boolean): Whether or not to allow authenticated video devices in the meeting's organization to start or join the meeting without a prompt. This attribute can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
    - `hasChat` (boolean): Whether or not this meeting instance has chat.
    - `hasRecording` (boolean): Whether or not this meeting instance has been recorded. `true` if the meeting instance has been recorded even if the recording has been deleted.
    - `hasTranscription` (boolean): Whether or not this meeting instance has a transcription.
    - `hasSummary` (boolean): Whether or not this meeting instance has a summary.
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
