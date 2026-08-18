---
doc_id: webex-meeting-get-meetings
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /meetings
operation_id: listMeetings
tags: Meetings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.480139+00:00
---

# GET /meetings

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `listMeetings`

## Resumen
List Meetings

## Descripción
<div><Callout type="info">The previous `List Meetings of a Meeting Series` API is merged into the [List Meetings](/docs/api/v1/meetings/list-meetings) API.</Callout></div>

Retrieves details for meetings with a specified meeting number, web link, meeting type, etc. Please note that there are various products in the [Webex Suite](https://www.webex.com/collaboration-suite.html) such as `Meetings` and `Events`. Currently, only meetings of the `Meetings` product are supported by this API, meetings of others in the suite are not supported. Ad-hoc meetings created by [Create a Meeting](/docs/api/v1/meetings/create-a-meeting) with `adhoc` of `true` and a `roomId` will not be listed, but the ended and ongoing ad-hoc meeting instances will be listed.

Lists scheduled meeting and meeting instances of a meeting series identified by `meetingSeriesId`. Scheduled meetings of an ad-hoc meeting created by [Create a Meeting](/docs/api/v1/meetings/create-a-meeting) with `adhoc` of `true` and a `roomId` are not listed, but the ended and ongoing meeting instances of it are. Each _scheduled meeting_ or _meeting_ instance of a _meeting series_ has its own `start`, `end`, etc. Thus, for example, when a daily meeting has been scheduled from `2019-04-01` to `2019-04-10`, there are 10 scheduled meeting instances in this series, one instance for each day, and each one has its own attributes. When a scheduled meeting has been started and ended or is happening, there are even more ended or in-progress meeting instances.

Long result sets are split into [pages](/docs/basics#pagination).

* The default value of `meetingSeries` will be used if `meetingType` is not specified. When listing meetings with `meetingType=meetingSeries` implicitly or explicitly, the API returns all the recurring meeting series where the user is the meeting host or an invitee to the meeting. Please note that a meeting with no `recurrence` attribute is considered a meeting series with only one occurrence and it can also be listed with `meetingType=meetingSeries`. A recurring meeting series may have multiple occurrences which are scattered over weeks, months, or years. So, any meeting series that overlaps with the time range specified by `from` and `to` will be listed. For example, a monthly meeting series with `start=2024-01-01T10:00:00Z`, `end=2024-01-01T11:00:00Z` and `recurrence=FREQ=MONTHLY;INTERVAL=1;BYMONTHDAY=1;UNTIL=20250210T000000Z` can be listed with `meetingType=meetingSeries&from=2024-10-01&to=2024-11-01` even if the `start` and `end` are not in the specified time range.

* If `meetingType` is specified and equals `meeting`, it lists ongoing and ended instances of the meeting series. The default value of `from` and `to` is: `from` equals the current date and time minus 7 days, and `to` equals the current date and time.

* If `meetingSeriesId` is specified, `meetingNumber`, `webLink`, `roomId`, `current`, `integrationTag`, `scheduledType`, `siteUrl` will be ignored.

* If `meetingNumber` is specified, the operation returns an array of meeting objects specified by the `meetingNumber`. Each object in the array can be a scheduled meeting or a meeting series depending on whether the `current` parameter is `true` or `false`, and each object contains the simultaneous interpretation object. When `meetingNumber` is specified, parameters of `from`, `to`, `meetingType`, `state`, `isModified` and `siteUrl` will be ignored. Please note that `meetingNumber`, `webLink` and `roomId` are mutually exclusive and they cannot be specified simultaneously.

* If `webLink` is specified, the operation returns an array of meeting objects specified by the `webLink`. Each object in the array can be a scheduled meeting or a meeting series depending on whether the `current` parameter is `true` or `false`, and each object contains the simultaneous interpretation object. When `webLink` is specified, parameters of `from`, `to`, `meetingType`, `state`, `isModified` and `siteUrl` will be ignored. Please note that `meetingNumber`, `webLink` and `roomId` are mutually exclusive and they cannot be specified simultaneously.

* If `roomId` is specified, the operation returns an array of meeting objects of the Webex space specified by the `roomId`. When `roomId` is specified, parameters of `current`, `meetingType`, `state` and `isModified` will be ignored. The meeting objects are queried on the user's preferred site if no `siteUrl` is specified; otherwise, queried on the specified site. `meetingNumber`, `webLink` and `roomId` are mutually exclusive and they cannot be specified simultaneously.

* If `state` parameter is specified, the returned array only has items in the specified state. If `state` is not specified, return items of all states.

* If `meetingType` equals "meetingSeries", the `scheduledType` parameter can be "meeting", "webinar" or null. If `scheduledType` is specified, the returned array only has items of the specified scheduled type; otherwise, it has items of "meeting" and "webinar".

* If `meetingType` equals "scheduledMeeting", the `scheduledType` parameter can be "meeting", "webinar", "personalRoomMeeting" or null. If `scheduledType` is specified, the returned array only has items of the specified scheduled type; otherwise, it has items of all scheduled types.

* If `meetingType` equals "meeting", the `scheduledType` parameter can be "meeting", "webinar" or null. If `scheduledType` is specified, the returned array only has items of the specified scheduled type; otherwise, it has items of "meeting" and "webinar". Please note that ended or in-progress meeting instances of [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings) also fall into the category of "meeting" `scheduledType`.

* If `meetingType` equals "meeting", a maximum of 10000 meeting instances can be listed even if pagination is enabled.

* If `isModified` parameter is specified, the returned array only has items which have been modified to exceptional meetings. This parameter only applies to scheduled meeting.

* If any of the `hasChat`, `hasRecording`, `hasTranscription`, `hasSummary`, `hasClosedCaption`, `hasPolls `, `hasQA` and `hasSlido` parameters is specified, the `meetingType` must be "meeting" and `state` must be "ended". These parameters are null by default.

* The `current` parameter only applies to meeting series. If it's `false`, the `start` and `end` attributes of each returned meeting series object are for the first scheduled meeting of that series. If it's `true` or not specified, the `start` and `end` attributes are for the scheduled meeting which is ready to start or join or the upcoming scheduled meeting of that series.

* If `from` and `to` are specified, the operation returns an array of meeting objects in that specified time range.

* If the parameter `siteUrl` has a value, the operation lists meetings on the specified site; otherwise, lists meetings on the user's all sites. All available Webex sites of the user can be retrieved by `Get Site List` API.

* `trackingCodes` is not supported for ended meeting instances.

* A full admin or a content admin can list all the ended and ongoing meeting instances of the organization he manages with the `meeting:admin_schedule_read` scope and `meetingType=meeting` parameter.

* To learn more about which attributes are available for different meeting states, please refer to [Available Meeting Attributes for Different Meeting States](/docs/meetings#available-meeting-attributes-for-different-meeting-states).

#### Request Header

* `password`: Meeting password. Required when the meeting is protected by a password and the current user is not privileged to view it if they are not a host, cohost or invitee of the meeting.

* `timezone`: [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) for time stamps in response body, defined in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default value is `UTC` if not specified.

## Parámetros
- `meetingNumber` [query] (string): Meeting number for the meeting objects being requested. `meetingNumber`, `webLink` and `roomId` are mutually exclusive. If it's an exceptional meeting from a meeting series, the exceptional meeting instead of the primary meeting series is returned.
- `webLink` [query] (string): URL encoded link to information page for the meeting objects being requested. `meetingNumber`, `webLink` and `roomId` are mutually exclusive.
- `roomId` [query] (string): Associated Webex space ID for the meeting objects being requested. `meetingNumber`, `webLink` and `roomId` are mutually exclusive.
- `meetingSeriesId` [query] (string): Unique identifier for the meeting series. The meeting ID of a scheduled [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings) meeting is not supported. If `meetingSeriesId` is specified, it lists all occurrences and instances of the meeting series by default; with `meetingType` of `scheduledMeeting`, it lists occurrences; with `meetingType` of `meeting`, it lists ongoing and ended instances.
- `max` [query] (number): Limit the maximum number of meetings in the response, up to 100. This parameter is ignored if `meetingNumber`, `webLink` or `roomId` is specified. The default value is 10.
- `from` [query] (string): Start date and time (inclusive) for the range for which meetings are to be returned in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `from` cannot be after `to`. This parameter will be ignored if `meetingNumber`, `webLink` or `roomId` is specified.  When `meetingType` is `meetingSeries`(either explicitly set or by default), if `to` is specified, the default value for `from` is `to` minus 7 days. If `to` is also not specified, the default value for `from` is the current date and time. When `meetingType` is `scheduledMeeting`, `from` is the same as above. When `meetingType` is `meeting`, if `to` is specified, the default value for `from` is `to` minus 7 days. If `to` is also not specified, the default value for `from` is 7 days before the current date and time.
- `to` [query] (string): End date and time (exclusive) for the range for which meetings are to be returned in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `to` cannot be before `from`. This parameter will be ignored if `meetingNumber`, `webLink` or `roomId` is specified.  When `meetingType` is `meetingSeries`(either explicitly set or by default), if `from` is specified, the default value for `to` is `from` plus 7 days. If `from` is also not specified, the default value for `to` is 7 days after the current date and time. When `meetingType` is `scheduledMeeting`, `to` is the same as above. When `meetingType` is `meeting`, if `from` is specified, the default value for `to` is `from` plus 7 days. If `from` is also not specified, the default value for `to` is the current date and time.
- `meetingType` [query] (string): Meeting type for the meeting objects being requested. This parameter will be ignored if `meetingNumber`, `webLink` or `roomId` is specified. Valores: meetingSeries, scheduledMeeting, meeting. Por defecto: meetingSeries.
- `state` [query] (string): Meeting state for the meeting objects being requested. If not specified, return meetings of all states. This parameter will be ignored if `meetingNumber`, `webLink` or `roomId` is specified. Details of an `ended` meeting will only be available 15 minutes after the meeting has ended. `inProgress` meetings are not fully supported. The API will try to return details of an `inProgress` meeting 15 minutes after the meeting starts. However, it may take longer depending on the traffic. See the [Webex Meetings](/docs/meetings#meeting-states) guide for more information about the states of meetings. Valores: active, scheduled, ready, lobby, inProgress, ended, missed, expired.
- `scheduledType` [query] (string): Scheduled type for the meeting objects being requested. Valores: meeting, webinar, personalRoomMeeting.
- `isModified` [query] (boolean): Flag identifying whether a meeting has been modified. Only applies to scheduled meetings. If `true`, only return modified scheduled meetings; if `false`, only return unmodified scheduled meetings; if not specified, all scheduled meetings will be returned. Por defecto: False.
- `hasChat` [query] (boolean): Flag identifying whether a meeting has a chat log. Only applies to ended meeting instances. If `true`, only return meeting instances which have chats; if `false`, only return meeting instances which have no chats; if not specified, all meeting instances will be returned. Por defecto: False.
- `hasRecording` [query] (boolean): Flag identifying meetings which have been recorded. Only applies to ended meeting instances. If true, only return meeting instances which have been recorded; if false, only return meeting instances which have not been recorded; if not specified, all meeting instances will be returned. Por defecto: False.
- `hasTranscription` [query] (boolean): Flag identifying meetings with transcripts. Only applies to ended meeting instances. If `true`, only return meeting instances which have transcripts; if `false`, only return meeting instances which have no transcripts; if not specified, all meeting instances will be returned. Por defecto: False.
- `hasSummary` [query] (boolean): Flag identifying meetings with summaries. Only applies to ended meeting instances. If `true`, only return meeting instances which have summaries; if `false`, only return meeting instances which have no summaries; if not specified, all meeting instances will be returned. Por defecto: False.
- `hasClosedCaption` [query] (boolean): Flag identifying meetings with closed captions. Only applies to ended meeting instances. If `true`, only return meeting instances which have closed captions; if `false`, only return meeting instances which have no closed captions; if not specified, all meeting instances will be returned. Por defecto: False.
- `hasPolls` [query] (boolean): Flag identifying meetings with polls. Only applies to ended meeting instances. If `true`, only return meeting instances which have polls; if `false`, only return meeting instances which have no polls; if not specified, all meeting instances will be returned. Por defecto: False.
- `hasQA` [query] (boolean): Flag identifying meetings with Q&A. Only applies to ended meeting instances. If `true`, only return meeting instances which have Q&A; if `false`, only return meeting instances which have no Q&A; if not specified, all meeting instances will be returned. Por defecto: False.
- `hasSlido` [query] (boolean): Flag identifying meetings with Slido interactions. Only applies to ended meeting instances. If `true`, only return meeting instances which have Slido interactions like Q&A or polling; if `false`, only return meeting instances which have no Slido interactions; if not specified, all meeting instances will be returned. Por defecto: False.
- `current` [query] (boolean): Flag identifying to retrieve the current scheduled meeting of the meeting series or the entire meeting series. This parameter only applies to scenarios where the meeting is not an exceptional meeting from a meeting series. If it's `true`, return the scheduled meeting of the meeting series which is ready to join or start or the upcoming scheduled meeting of the meeting series; if it's `false`, return the entire meeting series. Por defecto: True.
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes. If set, the admin may specify the email of a user in a site they manage and the API returns meetings as if the user calling the API were the user of `hostEmail` themself, and the meetings returned by the API include the meetings where the user of `hostEmail` is the meeting host and those where they are an invitee.
- `siteUrl` [query] (string): URL of the Webex site which the API lists meetings from. If not specified, the API lists meetings from user's all sites. All available Webex sites of the user can be retrieved by `Get Site List` API.
- `integrationTag` [query] (string): External key created by an integration application. This parameter is used by the integration application to query meetings by a key in its own domain such as a Zendesk ticket ID, a Jira ID, a Salesforce Opportunity ID, etc. An integrationTag created by one client cannot be accessed or used as a filtering parameter by another client. For example, if a meeting has an `integrationTag` of "Sales" which is created by the client behind the developer portal, then this integrationTag can't be accessed on the meeting or its recordings by another client. Neither can it be used to filter meetings or recordings by a client other than the one that created the integrationTag of "Sales".
- `password` [header] (string): e.g. BgJep@4323
- `timezone` [header] (string): e.g. UTC

## Ejemplo de invocación
```bash
curl -X GET '/meetings' \
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
  - `agenda` (string): Meeting agenda. The agenda can be a maximum of 1300 characters long. This attribute can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
  - `password` (string) (**requerido**): Meeting password. Applies to meeting series, scheduled meetings, and in-progress meeting instances, but not to meeting instances which have ended. Can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
  - `phoneAndVideoSystemPassword` (string): 8-digit numeric password used to join a meeting from audio and video devices. This attribute applies to meeting series, scheduled meetings, and in-progress meeting instances, but not to meeting instances which have ended.
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
  - `hostKey` (string) (**requerido**): Key for joining the meeting as host.
  - `siteUrl` (string) (**requerido**): Site URL for the meeting.
  - `webLink` (string) (**requerido**): Link to a meeting information page where the meeting client is launched if the meeting is ready to start or join.
  - `sipAddress` (string): SIP address for callback from a video system.
  - `dialInIpAddress` (string): IP address for callback from a video system.
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
  - `panelistPassword` (string): Password for panelists of a webinar meeting. Must conform to the site's password complexity settings. Read [password management](https://help.webex.com/en-us/zrupm6/Manage-Security-Options-for-Your-Site-in-Webex-Site-Administration) for details. If not specified, a random password conforming to the site's password rules will be generated automatically.
  - `phoneAndVideoSystemPanelistPassword` (string): 8-digit numeric panelist password to join a webinar meeting from audio and video devices.
  - `enableAutomaticLock` (boolean): Whether or not to automatically lock the meeting after it starts.
  - `automaticLockMinutes` (number): The number of minutes after the meeting begins, for automatically locking it.
  - `allowFirstUserToBeCoHost` (boolean): Whether or not to allow the first attendee of the meeting with a host account on the target site to become a cohost. The target site is specified by the `siteUrl` parameter when creating the meeting. If not specified, it's a user's preferred site. The `allowFirstUserToBeCoHost` attribute can be modified for a meeting series or a scheduled meeting uisng the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
  - `allowAuthenticatedDevices` (boolean): Whether or not to allow authenticated video devices in the meeting's organization to start or join the meeting without a prompt. This attribute can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
  - `hasChat` (boolean): Whether or not this meeting instance has chat.
  - `hasRecording` (boolean): Whether or not this meeting instance has been recorded. `true` if the meeting instance has been recorded even if the recording has been deleted.
  - `hasTranscription` (boolean): Whether or not this meeting instance has a transcription.
  - `hasClosedCaption` (boolean): Whether or not this meeting instance has closed captions.
  - `hasPolls` (boolean): Whether or not this meeting instance has polls.
  - `hasQA` (boolean): Whether or not this meeting instance has Q&A.
  - `hasSlido` (boolean): Whether or not this meeting instance has Slido interactions. It's true if Slido is enabled in the meeting and there are interactions like Q&A or polling in Slido.
  - `hasRegistration` (boolean): Whether or not this meeting instance has a registration form. Only applies to ended meeting or webinar instances. Doesn't apply to meeting series, scheduled meetings, or in-progress meeting or webinar instances.
  - `hasRegistrants` (boolean): Whether or not someone has registered a this meeting instance via the registration form. Only applies to ended meeting or webinar instances. Doesn't apply to meeting series, scheduled meetings, or in-progress meeting or webinar instances.
  - `hasPostEventSurvey` (boolean): Whether this meeting instance has a survey and someone has responded to the survey. Only applies to ended webinar instances. Doesn't apply to meeting series, scheduled meetings, in-progress meeting or webinar instances, or ended meeting instances.
  - `telephony` (object) (**requerido**): Information for callbacks from a meeting to phone or for joining a teleconference using a phone.
    - `accessCode` (string) (**requerido**): Code for authenticating a user to join teleconference. Users join the teleconference using the call-in number or the global call-in number, followed by the value of the `accessCode`.
    - `callInNumbers` (array) (**requerido**): Array of call-in numbers for joining a teleconference from a phone.
      - `label` (string) (**requerido**): Label for the call-in number.
      - `callInNumber` (string) (**requerido**): Call-in number to join the teleconference from a phone.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "870f51ff287b41be84648412901e0402_20191101T120000Z",
      "meetingSeriesId": "870f51ff287b41be84648412901e0402",
      "meetingNumber": "123456789",
      "title": "Example Daily Meeting",
      "agenda": "Example Agenda",
      "password": "BgJep@43",
      "phoneAndVideoSystemPassword": "12345678",
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
      "hostKey": "123456",
      "siteUrl": "site4-example.webex.com",
      "webLink": "https://site4-example.webex.com/site4/j.php?MTID=md41817da6a55b0925530cb88b3577b1e",
      "sipAddress": "123456789@site4-example.webex.com",
      "dialInIpAddress": "192.168.100.100",
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
      "allowFir
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