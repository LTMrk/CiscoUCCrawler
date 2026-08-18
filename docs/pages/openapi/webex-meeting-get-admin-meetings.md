---
doc_id: webex-meeting-get-admin-meetings
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /admin/meetings
operation_id: adminListMeetings
tags: Meetings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.476847+00:00
---

# GET /admin/meetings

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `adminListMeetings`

## Resumen
List Meetings By an Admin

## Descripción
Retrieves details for meetings by an admin with a specified meeting number or web link. Please note that there are various products in the [Webex Suite](https://www.webex.com/collaboration-suite.html) such as `Meetings` and `Events`. Currently, only meetings of the `Meetings` product are supported by this API, meetings of others in the suite are not supported. Ad-hoc meetings created by [Create a Meeting](/docs/api/v1/meetings/create-a-meeting) with `adhoc` of `true` and a `roomId` will not be listed, but the ended and ongoing ad-hoc meeting instances will be listed. The following sensitive attributes are hidden from the response: `agenda`, `hostKey`, `password`, `phoneAndVideoSystemPassword`, `panelistPassword`, `phoneAndVideoSystemPanelistPassword`, `webLink`, `sipAddress`, `dialInIpAddress`, `registration` and `telephony.accessCode`.

* If `meetingNumber` is specified, the operation returns an array of meeting objects specified by the `meetingNumber`. Each object in the array can be a scheduled meeting or a meeting series depending on whether the `current` parameter is `true` or `false`, and each object contains the simultaneous interpretation object. Please note that `meetingNumber` and `webLink` are mutually exclusive and they cannot be specified simultaneously.

* If `webLink` is specified, the operation returns an array of meeting objects specified by the `webLink`. Each object in the array can be a scheduled meeting or a meeting series depending on whether the `current` parameter is `true` or `false`, and each object contains the simultaneous interpretation object. Please note that `meetingNumber` and `webLink` are mutually exclusive and they cannot be specified simultaneously.

* The `current` parameter only applies to meeting series. If it's `false`, the `start` and `end` attributes of each returned meeting series object are for the first scheduled meeting of that series. If it's `true` or not specified, the `start` and `end` attributes are for the scheduled meeting which is ready to start or join or the upcoming scheduled meeting of that series.

* To learn more about which attributes are available for different meeting states, please refer to [Available Meeting Attributes for Different Meeting States](/docs/meetings#available-meeting-attributes-for-different-meeting-states).

#### Request Header

* `timezone`: [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) for time stamps in response body, defined in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default value is `UTC` if not specified.

## Parámetros
- `meetingNumber` [query] (string): Meeting number for the meeting objects being requested. `meetingNumber` and `webLink` are mutually exclusive. If it's an exceptional meeting from a meeting series, the exceptional meeting instead of the primary meeting series is returned.
- `webLink` [query] (string): URL encoded link to information page for the meeting objects being requested. `meetingNumber` and `webLink` are mutually exclusive.
- `current` [query] (boolean): Flag identifying to retrieve the current scheduled meeting of the meeting series or the entire meeting series. This parameter only applies to scenarios where `meetingNumber` is specified and the meeting is not an exceptional meeting from a meeting series. If it's `true`, return the scheduled meeting of the meeting series which is ready to join or start or the upcoming scheduled meeting of the meeting series; if it's `false`, return the entire meeting series. The default value is `true`. Por defecto: True.
- `timezone` [header] (string): e.g. UTC

## Ejemplo de invocación
```bash
curl -X GET '/admin/meetings' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): Meetings array.
  - `id` (string) (**requerido**): Unique identifier for meeting. For a meeting series, the `id` is used to identify the entire series. For scheduled meetings from a series, the `id` is used to identify that scheduled meeting. For a meeting instance that is in progress or has concluded, the `id` is used to identify that instance.
  - `meetingSeriesId` (string) (**requerido**): Unique identifier for meeting series. It only apples to scheduled meeting and meeting instance. If it's a scheduled meeting from a series or a meeting instance that is happening or has happened, the `meetingSeriesId` is the `id` of the primary series.
  - `scheduledMeetingId` (string): Unique identifier for scheduled meeting which current meeting is associated with. It only apples to meeting instance which is happening or has happened. It's the `id` of the scheduled meeting this instance is associated with.
  - `meetingNumber` (string): Meeting number. Applies to meeting series, scheduled meeting, and meeting instances, but not to meeting instances which have ended.
  - `title` (string) (**requerido**): Meeting title. Can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
  - `meetingType` (string) (**requerido**): Meeting type.  * `meetingSeries` - Primary instance of a scheduled series of meetings which consists of one or more scheduled meetings based on a `recurrence` rule. When a non-recurring meeting is scheduled with no `recurrence`, its `meetingType` is also `meetingSeries` which is a meeting series with only one occurrence in Webex meeting modeling.  * `scheduledMeeting` - Instance from a primary meeting series.  * `meeting` - Meeting instance that is in progress or has completed. Valores: meetingSeries, scheduledMeeting, meeting.
  - `state` (string) (**requerido**): Meeting state.  * `active` - Only applies to a meeting series. Indicates that one or more future scheduled meetings exist for this meeting series.  * `scheduled` - Only applies to scheduled meeting. Indicates that the meeting is scheduled in the future.  * `ready` - Only applies to scheduled meeting. Indicates that this scheduled meeting is ready to start or join immediately.  * `lobby` - Only applies to meeting instances. Indicates that a locked meeting has been joined by participants, but no hosts have joined.  * `inProgress` - Applies to meeting series and meeting instance. For meeting series, indicates that an instance of this series is in progress; for a meeting instances, indicates that the meeting has been joined and unlocked.  * `ended` - Applies to scheduled meetings and meeting instances. For scheduled meetings, indicates that the meeting was started and is now over. For meeting instances, indicates that the meeting instance has concluded.  * `missed` - This state only applies to scheduled meetings. Indicates that the meeting was scheduled in the past but never happened.  * `expired` - This state only applies to a meeting series. Indicates that all scheduled meetings of this series have passed. Valores: active, scheduled, ready, lobby, inProgress, ended, missed, expired.
  - `hostDidJoin` (boolean): Only applies to meeting series in the `inProgress` state, scheduled meetings in the `ready` state, and meeting instances in the `inProgress` state, whether or not the meeting host joined the meeting. If true, the meeting host has joined the meeitng even if they dropped off; otherwise, the meeting host hasn't ever join the meeting. Indicates that someone is waiting in the lobby and the host hasn't joined the meeting if `attendeeDidJoin` is true and `hostDidJoin` is false.
  - `attendeeDidJoin` (boolean): Only applies to meeting series in the `inProgress` state, scheduled meetings in the `ready` state, and meeting instances in the `inProgress` state. Whether or not anyone has joined the meeting. If true, the meeting host or any attendee has joined the meeting; otherwise, no one has joined the meeting. Indicates that someone is waiting in the lobby and the host hasn't joined the meeting if `attendeeDidJoin` is true and `hostDidJoin` is false.
  - `isModified` (boolean): This state only applies to scheduled meeting. Flag identifying whether or not the scheduled meeting has been modified.
  - `timezone` (string) (**requerido**): [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) of `start` and `end`, conforming with the [IANA time zone database](https://www.iana.org/time-zones).
  - `start` (string) (**requerido**): Start time for meeting in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. If the meetingType of a meeting is `meetingSeries`, `start` is the scheduled start time of the first occurrence of this series. If the meeting is a meeting series and the `current` filter is true, `start` is the date and time the upcoming or ongoing meeting of the series starts. If the meetingType of a meeting is `scheduledMeeting`, `start` is the scheduled start time of this occurrence. If the meetingType of a meeting is `meeting`, `start` is the actual start time of the meeting instance. Can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
  - `end` (string) (**requerido**): End time for a meeting in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. If the meetingType of a meeting is `meetingSeries`, `end` is the scheduled end time of the first occurrence of this series. If the meeting is a meeting series and the current filter is true, `end` is the date and time the upcoming or ongoing meeting of the series ends. If the meetingType of a meeting is `scheduledMeeting`, `end` is the scheduled end time of this occurrence. If the meetingType of a meeting is `meeting`, `end` is the actual end time of the meeting instance. If a meeting instance is in progress, `end` is not available. Can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
  - `recurrence` (string): Meeting series recurrence rule (conforming with [RFC 2445](https://www.ietf.org/rfc/rfc2445.txt)). Applies only to a recurring meeting series, not to a meeting series with only one scheduled meeting. Can be modified for a meeting series using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API. Multiple days or dates for monthly or yearly `recurrence` rule are not supported, only the first day or date specified is taken. For example, "FREQ=MONTHLY;INTERVAL=1;COUNT=10;BYMONTHDAY=10,11,12" is not supported and it will be partially supported as "FREQ=MONTHLY;INTERVAL=1;COUNT=10;BYMONTHDAY=10".
  - `hostUserId` (string) (**requerido**): Unique identifier for the meeting host.
  - `hostDisplayName` (string) (**requerido**): Display name for the meeting host.
  - `hostEmail` (string) (**requerido**): Email address for the meeting host.
  - `siteUrl` (string) (**requerido**): Site URL for the meeting.
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
  - `hasClosedCaption` (boolean): Whether or not this meeting instance has closed captions.
  - `hasPolls` (boolean): Whether or not this meeting instance has polls.
  - `hasQA` (boolean): Whether or not this meeting instance has Q&A.
  - `hasRegistration` (boolean): Whether or not this meeting instance has a registration form. Only applies to ended meeting or webinar instances. Doesn't apply to meeting series, scheduled meetings, or in-progress meeting or webinar instances.
  - `hasRegistrants` (boolean): Whether or not someone has registered a this meeting instance via the registration form. Only applies to ended meeting or webinar instances. Doesn't apply to meeting series, scheduled meetings, or in-progress meeting or webinar instances.
  - `hasPostEventSurvey` (boolean): Whether this meeting instance has a survey and someone has responded to the survey. Only applies to ended webinar instances. Doesn't apply to meeting series, scheduled meetings, in-progress meeting or webinar instances, or ended meeting instances.
  - `telephony` (object) (**requerido**): Information for callbacks from a meeting to phone or for joining a teleconference using a phone.
    - `callInNumbers` (array) (**requerido**): Array of call-in numbers for joining a teleconference from a phone.
      - `label` (string) (**requerido**): Label for the call-in number.
      - `callInNumber` (string) (**requerido**): Call-in number to join the teleconference from a phone.
      - `tollType` (string) (**requerido**): Type of toll for the call-in number. Valores: toll, tollFree.
    - `links` (array): [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS) information of global call-in numbers for joining a teleconference from a phone.
      - `rel` (string) (**requerido**): Link relation describing how the target resource is related to the current context (conforming with [RFC5998](https://tools.ietf.org/html/rfc5988)).
      - `href` (string) (**requerido**): Target resource URI (conforming with [RFC5998](https://tools.ietf.org/html/rfc5988)).
      - `method` (string) (**requerido**): Target resource method (conforming with [RFC5998](https://tools.ietf.org/html/rfc5988)).
  - `meetingOptions` (object): Meeting Options.
    - `enabledChat` (boolean): Whether or not to allow any attendee to chat in the meeting. Also depends on the session type.
    - `enabledVideo` (boolean): Whether or not to allow any attendee to have video in the meeting. Also depends on the session type.
    - `enabledPolling` (boolean): Whether or not to allow any attendee to poll in the meeting. Can only be set `true` for a webinar. The value of this attribute depends on the session type for a meeting. Please contact your site admin if this attribute is not available. Not supported if the site has been migrated to the Webex Suite meeting platform.
    - `enabledNote` (boolean): Whether or not to allow any attendee to take notes in the meeting. The value of this attribute also depends on the session type. Not supported if the site has been migrated to the Webex Suite meeting platform.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "870f51ff287b41be84648412901e0402_20191101T120000Z",
      "meetingSeriesId": "870f51ff287b41be84648412901e0402",
      "meetingNumber": "123456789",
      "title": "Example Daily Meeting",
      "meetingType": "scheduledMeeting",
      "state": "ready",
      "hostDidJoin": true,
      "attendeeDidJoin": true,
      "isModified": false,
      "timezone": "UTC",
      "start": "2019-11-01T12:00:00Z",
      "end": "2019-11-01T13:00:00Z",
      "hostUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jN2ZkNzNmMi05ZjFlLTQ3ZjctYWEwNS05ZWI5OGJiNjljYzY",
      "hostDisplayName": "John Andersen",
      "hostEmail": "john.andersen@example.com",
      "siteUrl": "site4-example.webex.com",
      "enabledAutoRecordMeeting": false,
      "allowAnyUserToBeCoHost": false,
      "enabledJoinBeforeHost": false,
      "enableConnectAudioBeforeHost": false,
      "joinBeforeHostMinutes": 0,
      "excludePassword": false,
      "publicMeeting": false,
      "reminderTime": 10,
      "unlockedMeetingJoinSecurity": "allowJoin",
      "sessionTypeId": 3,
      "enableAutomaticLock": false,
      "automaticLockMinutes": 0,
      "allowFirstUserToBeCoHost": false,
      "allowAuthenticatedDevices": false,
      "telephony": {
        "callInNumbers": [
          {
            "label": "US Toll",
            "callInNumber": "123456789",
            "tollType": "toll"
          }
        ],
        "links": [
          {
            "rel": "globalCallinNumbers",
            "hre
  ... (truncado)
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