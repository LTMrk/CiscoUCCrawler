---
doc_id: webex-meeting-patch-meetings-meetingid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: PATCH
path: /meetings/{meetingId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.394358+00:00
---

# PATCH /meetings/{meetingId}

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `patchMeeting`

## Resumen
Patch a Meeting

## Descripción
<div>
<Callout type="warning">If only guests are waiting in the lobby and the host or cohost has not started the meeting, the meeting state remains `inProgress` for 5 minutes after the last guest leaves. The meeting cannot be patched during this time. If the meeting is started by the host or cohost and then ended normally, it can be patched immediately after it ends.</Callout>
</div>

Updates details for a meeting with a specified meeting ID. This operation applies to meeting series and scheduled meetings. It doesn't apply to ended or in-progress meeting instances. Ad-hoc meetings created by [Create a Meeting](/docs/api/v1/meetings/create-a-meeting) with `adhoc` of `true` and a `roomId` cannot be updated.

* If the `meetingId` value specified is for a scheduled meeting, the operation updates that scheduled meeting without impact on other scheduled meeting of the parent meeting series.

* If the `meetingId` value specified is for a meeting series, the operation updates the entire meeting series. **Note**: If the value of `start`, `end`, or `recurrence` for the meeting series is changed, any exceptional scheduled meeting in this series is cancelled when the meeting series is updated.

* The `agenda`, `recurrence`, and `trackingCodes` attributes can be specified as `null` so that these attributes become null and hidden from the response after the patch. Note that it's the keyword `null` not the string "null".

* If the parameter `recurrence` has a value, a recurring meeting is created based on the rule defined by the value of `recurrence`. For a non-recurring meeting which has no `recurrence` value set, its `meetingType` is also `meetingSeries` which is a meeting series with only one occurrence in Webex meeting modeling. If you specify a `recurrence` like `FREQ=DAILY;INTERVAL=1` which never ends, the furthest date of the series is unlimited. You can also specify a `recurrence` with a very distant ending date in the future, e.g. `FREQ=DAILY;INTERVAL=1;UNTIL=21241001T000000Z`, but the actual furthest date accepted for the recurring meeting is five years from now. Specifically, if it has an ending date, there can be up to 5 occurrences for a yearly meeting, 60 occurrences for a monthly meeting, 261 occurrences for a weekly meeting, or 1826 occurrences for a daily meeting.

* You can't update a meeting that starts 10 years or more in the future.

* Updating a meeting in the API that was created via a calendar connector is not allowed. The meeting may be updated in Webex, but the calendar event may not be updated, resulting in duplicate entries. This action is therefore blocked. In case you must overwrite this behavior, please contact devsupport@webex.com.

## Parámetros
- `meetingId` [path] (string) **(requerido)**: Unique identifier for the meeting to be updated. This parameter applies to meeting series and scheduled meetings. It doesn't apply to ended or in-progress meeting instances. Please note that currently meeting ID of a scheduled [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings) meeting is not supported for this API.

## Cuerpo de la petición (application/json-patch+json)
- `title` (string): Meeting title. The title can be a maximum of 128 characters long.
- `agenda` (string): Meeting agenda. The agenda can be a maximum of 1300 characters long. It can be specified `null` so that it becomes null and hidden from the response after the patch.
- `password` (string): Meeting password. Must conform to the site's password complexity settings. Read [password management](https://help.webex.com/en-us/zrupm6/Manage-Security-Options-for-Your-Site-in-Webex-Site-Administration) for details.
- `start` (string): Date and time for the start of meeting in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `start` cannot be before current date and time or after `end`. Duration between `start` and `end` cannot be shorter than 10 minutes or longer than 23 hours 59 minutes. Refer to the [Webex Meetings](/docs/meetings#restrictions-on-updating-a-meeting) guide for more information about restrictions on updating date and time for a meeting. Please note that when a meeting is being updated, `start` of the meeting will be accurate to minutes, not seconds or milliseconds. Therefore, if `start` is within the same minute as the current time, `start` will be adjusted to the upcoming minute; otherwise, `start` will be adjusted with seconds and milliseconds stripped off. For instance, if the current time is `2022-03-01T10:32:16.657+08:00`, `start` of `2022-03-01T10:32:28.076+08:00` or `2022-03-01T10:32:41+08:00` will be adjusted to `2022-03-01T10:33:00+08:00`, and `start` of `2022-03-01T11:32:28.076+08:00` or `2022-03-01T11:32:41+08:00` will be adjusted to `2022-03-01T11:32:00+08:00`.
- `end` (string): Date and time for the end of meeting in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `end` cannot be before current date and time or before `start`. Duration between `start` and `end` cannot be shorter than 10 minutes or longer than 23 hours 59 minutes. Refer to the [Webex Meetings](/docs/meetings#restrictions-on-updating-a-meeting) guide for more information about restrictions on updating date and time for a meeting. Please note that when a meeting is being updated, `end` of the meeting will be accurate to minutes, not seconds or milliseconds. Therefore, `end` will be adjusted with seconds and milliseconds stripped off. For instance, `end` of `2022-03-01T11:52:28.076+08:00` or `2022-03-01T11:52:41+08:00` will be adjusted to `2022-03-01T11:52:00+08:00`.
- `timezone` (string): [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) in which the meeting was originally scheduled (conforming with the [IANA time zone database](https://www.iana.org/time-zones)).
- `recurrence` (string): Meeting series recurrence rule (conforming with [RFC 2445](https://www.ietf.org/rfc/rfc2445.txt)). Applies only to a recurring meeting series, not to a meeting series with only one scheduled meeting. Multiple days or dates for monthly or yearly `recurrence` rule are not supported, only the first day or date specified is taken. For example, "FREQ=MONTHLY;INTERVAL=1;COUNT=10;BYMONTHDAY=10,11,12" is not supported and it will be partially supported as "FREQ=MONTHLY;INTERVAL=1;COUNT=10;BYMONTHDAY=10". It can be specified `null` so that the meeting becomes non-recurring and the `recurrence` attribute becomes null and hidden from the response after the patch.
- `enabledAutoRecordMeeting` (boolean): Whether or not meeting is recorded automatically.
- `allowAnyUserToBeCoHost` (boolean): Whether or not to allow any attendee with a host account on the target site to become a cohost when joining the meeting. The target site is specified by `siteUrl` parameter when creating the meeting; if not specified, it's user's preferred site.
- `enabledJoinBeforeHost` (boolean): Whether or not to allow any attendee to join the meeting before the host joins the meeting.
- `enableConnectAudioBeforeHost` (boolean): Whether or not to allow any attendee to connect audio in the meeting before the host joins the meeting. This attribute is only applicable if the `enabledJoinBeforeHost` attribute is set to true.
- `joinBeforeHostMinutes` (number): Number of minutes an attendee can join the meeting before the meeting start time and the host joins. Only applicable if the `enabledJoinBeforeHost` attribute is set to true. Valid options for a meeting are `0`, `5`, `10`, and `15`, and valid options for a webinar are `0`, `15`, `30`, `45`, and `60`. The default is `0` if not specified.
- `excludePassword` (boolean): Whether or not to exclude the meeting password from the email invitation.
- `publicMeeting` (boolean): Whether or not to allow the meeting to be listed on the public calendar.
- `reminderTime` (number): The number of minutes before the meeting begins, that an email reminder is sent to the host.
- `unlockedMeetingJoinSecurity` (string): Specifies how the people who aren't on the invite can join the unlocked meeting.  * `allowJoin` - If the value of `unlockedMeetingJoinSecurity` attribute is `allowJoin`, people can join the unlocked meeting directly.  * `allowJoinWithLobby` - If the value of `unlockedMeetingJoinSecurity` attribute is `allowJoinWithLobby`, people will wait in the lobby until the host admits them.  * `blockFromJoin` - If the value of `unlockedMeetingJoinSecurity` attribute is `blockFromJoin`, people can't join the unlocked meeting. Valores: allowJoin, allowJoinWithLobby, blockFromJoin.
- `sessionTypeId` (number): Unique identifier for a meeting session type for the user. This attribute is required while scheduling webinar meeting. All available meeting session types enabled for the user can be retrieved by [List Meeting Session Types](/docs/api/v1/meetings/list-meeting-session-types) API.
- `enabledWebcastView` (boolean): Whether or not webcast view is enabled.
- `panelistPassword` (string): Password for panelists of a webinar meeting. Must conform to the site's password complexity settings. Read [password management](https://help.webex.com/en-us/zrupm6/Manage-Security-Options-for-Your-Site-in-Webex-Site-Administration) for details. If not specified, a random password conforming to the site's password rules will be generated automatically.
- `enableAutomaticLock` (boolean): Whether or not to automatically lock the meeting after it starts.
- `automaticLockMinutes` (number): The number of minutes after the meeting begins, for automatically locking it.
- `allowFirstUserToBeCoHost` (boolean): Whether or not to allow the first attendee of the meeting with a host account on the target site to become a cohost. The target site is specified by `siteUrl` parameter when creating the meeting; if not specified, it's user's preferred site.
- `allowAuthenticatedDevices` (boolean): Whether or not to allow authenticated video devices in the meeting's organization to start or join the meeting without a prompt.
- `sendEmail` (boolean): Whether or not to send emails to host and invitees. It is an optional field and default value is true.
- `hostEmail` (string): Email address for the meeting host. This attribute should only be set if the user or application calling the API has the admin-level scopes. When used, the admin may specify the email of a user in a site they manage to be the meeting host. The field is not editable and is only used to patch a meeting on behalf of the real meeting host. Please use the [Reassign Meetings to a New Host](/docs/api/v1/meetings/reassign-meetings-to-a-new-host) API if you need to update the meeting host.
- `meetingOptions` (object): Meeting Options.
  - `enabledChat` (boolean): Whether or not to allow any attendee to chat in the meeting. Also depends on the session type.
  - `enabledVideo` (boolean): Whether or not to allow any attendee to have video in the meeting. Also depends on the session type.
  - `enabledPolling` (boolean): Whether or not to allow any attendee to poll in the meeting. Can only be set `true` for a webinar. The value of this attribute depends on the session type for a meeting. Please contact your site admin if this attribute is not available. Not supported if the site has been migrated to the Webex Suite meeting platform.
  - `enabledNote` (boolean): Whether or not to allow any attendee to take notes in the meeting. The value of this attribute also depends on the session type. Not supported if the site has been migrated to the Webex Suite meeting platform.
  - `noteType` (string): Whether note taking is enabled. If the value of `enabledNote` is false, users cannot set this attribute and get the default value `allowAll`. Not supported if the site has been migrated to the Webex Suite meeting platform.  * `allowAll` - If the value of `noteType` attribute is `allowAll`, all participants can take notes.  * `allowOne` - If the value of `noteType` attribute is `allowOne`, only a single note taker is allowed. Valores: allowAll, allowOne.
  - `enabledFileTransfer` (boolean): Whether or not to allow any attendee to transfer files in the meeting. The value of this attribute also depends on the session type.
  - `enabledUCFRichMedia` (boolean): Whether or not to allow any attendee to share [Universal Communications Format](https://www.cisco.com/c/en/us/td/docs/collaboration/training_center/wbs30/WebEx_BK_TE1FB6C1_00_training-center-frequently-asked-questions/WebEx_BK_TE1FB6C1_00_training-center-frequently-asked-questions_chapter_0110.pdf) media files in the meeting. The value of this attribute also depends on the sessionType. Not supported if the site has been migrated to the Webex Suite meeting platform.
- `attendeePrivileges` (object): Attendee Privileges. This attribute is not supported for a webinar.
  - `enabledShareContent` (boolean): Whether or not to allow any attendee to share content in the meeting.
  - `enabledSaveDocument` (boolean): Whether or not to allow any attendee to save shared documents, slides, or whiteboards when they are shared as files in the content viewer instead of in a window or application.
  - `enabledPrintDocument` (boolean): Whether or not to allow any attendee to print shared documents, slides, or whiteboards when they are shared as files in the content viewer instead of in a window or application.
  - `enabledAnnotate` (boolean): Whether or not to allow any attendee to annotate shared documents, slides, or whiteboards when they are shared as files in the content viewer instead of in a window or application.
  - `enabledViewParticipantList` (boolean): Whether or not to allow any attendee to view participants.
  - `enabledViewThumbnails` (boolean): Whether or not to allow any attendee to see a small preview image of any page of shared documents or slides when they are shared as files in the content viewer instead of in a window or application.
  - `enabledRemoteControl` (boolean): Whether or not to allow any attendee to control applications, web browsers, or desktops remotely.
  - `enabledViewAnyDocument` (boolean): Whether or not to allow any attendee to view any shared documents or slides when they are shared as files in the content viewer instead of in a window or application.
  - `enabledViewAnyPage` (boolean): Whether or not to allow any attendee to scroll through any page of shared documents or slides when they are shared as files in the content viewer instead of in a window or application.
  - `enabledContactOperatorPrivately` (boolean): Whether or not to allow any attendee to contact the operator privately.
  - `enabledChatHost` (boolean): Whether or not to allow any attendee to chat with the host in private.
  - `enabledChatPresenter` (boolean): Whether or not to allow any attendee to chat with the presenter in private.
  - `enabledChatOtherParticipants` (boolean): Whether or not to allow any attendee to chat with other participants in private.
- `integrationTags` (array): External keys created by an integration application in its own domain, for example Zendesk ticket IDs, Jira IDs, Salesforce Opportunity IDs, etc. The integration application queries meetings by a key in its own domain. The maximum size of `integrationTags` is 3 and each item of `integrationTags` can be a maximum of 64 characters long. Please note that an empty or null `integrationTags` will delete all existing integration tags for the meeting implicitly. Developer can update integration tags for a `meetingSeries` but he cannot update it for a `scheduledMeeting` or a `meeting` instance.
- `enabledBreakoutSessions` (boolean): Whether or not breakout sessions are enabled. If the value of `enabledBreakoutSessions` is false, users can not set breakout sessions. If the value of `enabledBreakoutSessions` is true, users can update breakout sessions using the [Update Breakout Sessions](/docs/api/v1/meetings/{meetingId}/breakoutSessions) API. Updating breakout sessions are not supported by this API.
- `trackingCodes` (array): Tracking codes information. All available tracking codes and their options for the specified site can be retrieved by [List Meeting Tracking Codes](/docs/api/v1/meetings/list-meeting-tracking-codes) API. If an optional tracking code is missing from the `trackingCodes` array and there's a default option for this tracking code, the default option is assigned automatically. If the `inputMode` of a tracking code is `select`, its value must be one of the site-level options or the user-level value. Tracking code is not supported for a personal room meeting or an ad-hoc space meeting. It can be specified `null` so that it becomes null and hidden from the response after the patch.
  - `name` (string) **(requerido)**: Name of the tracking code. The name cannot be empty and the maximum size is 120 characters.
  - `value` (string) **(requerido)**: Value for the tracking code. `value` cannot be empty and the maximum size is 120 characters.
- `enabledAudioWatermark` (boolean): Whether or not the audio watermark is enabled. If it's `true`, `scheduledType` equals or defaults to `meeting`, and `audioConnectionOptions.audioConnectionType` equals `VoIP`, the audio for this meeting will have a watermark. In this case, a unique identifier is embedded into the audio that plays out of each Webex app and device. An administrator can use this watermark when analyzing an unauthorized recording to identify which Webex app or device was the source of the recording.
- `enabledVisualWatermark` (boolean): Whether or not the visual watermark is enabled. If it's `true`, the video for this meeting will have a watermark. In this case, Webex superimposes a watermark image pattern on top of the meeting video and shared content to deter participants from leaking meeting information. Each participant viewing the meeting sees a watermark image pattern with their email address. If the participant is not signed in, the watermark image pattern includes their display name and email address.
- `visualWatermarkOpacity` (number): Opacity level for the visual watermark. The value must be between 5 and 80, inclusive. A smaller value means less distraction for meeting participants, while a larger value shows a clearer watermark. It's supported when `enabledVisualWatermark` is `true`.
- `audioConnectionOptions` (object): Audio connection options.
  - `audioConnectionType` (string): Choose how meeting attendees join the audio portion of the meeting.  * `webexAudio` - Provide a hybrid audio option, allowing attendees to join using their computer audio or a phone.  * `VoIP` - Only restricts attendees to join the audio portion of the meeting using their computer instead of a telephone option.  * `other` - Other teleconference services.  * `none` - The way of attendees join the audio portion of the meeting is the default value. Valores: webexAudio, VoIP, other, none.
  - `enabledTollFreeCallIn` (boolean): Whether or not to show toll-free call-in numbers.
  - `enabledGlobalCallIn` (boolean): Whether or not to show global call-in numbers to attendees.
  - `enabledAudienceCallBack` (boolean): Whether or not to allow attendees to receive a call-back and call-in is available. Can only be set `true` for a webinar.
  - `entryAndExitTone` (string): Select the sound you want users who have a phone audio connection to hear when someone enters or exits the meeting.  * `beep` - All call-in users joining the meeting will hear the beep.  * `announceName` - All call-in users joining the meeting will hear their names.  * `noTone` - Turn off beeps and name announcements. Valores: beep, announceName, noTone.
  - `allowHostToUnmuteParticipants` (boolean): Whether or not to allow the host to unmute participants.
  - `allowAttendeeToUnmuteSelf` (boolean): Whether or not to allow attendees to unmute themselves.
  - `muteAttendeeUponEntry` (boolean): Whether or not to auto-mute attendees when attendees enter meetings.
- `requireAttendeeLogin` (boolean): Require attendees to sign in before joining the webinar. This option works when the value of `scheduledType` attribute is `webinar`. Please note that `requireAttendeeLogin` cannot be set if someone has already registered for the webinar.
- `restrictToInvitees` (boolean): Restrict webinar to invited attendees only. This option works when the registration option is disabled and the value of `scheduledType` attribute is `webinar`. Please note that `restrictToInvitees` cannot be set to `true` if `requireAttendeeLogin` is `false`.
- `enabledLiveStream` (boolean): Whether or not live streaming is enabled.
- `liveStream` (object):
  - `destination` (string) **(requerido)**: A descriptive text to describe the destination of the live streaming.
  - `rtmpUrl` (string) **(requerido)**: Live streaming RTMP URL.
  - `streamUrl` (string) **(requerido)**: The URL to view the live streaming, i.e. the playback URL.
  - `layoutWithoutSharedContent` (string): Live streaming layout when there's no shared content.  * `grid` - The video layout that allows you to see multiple participants in a meeting in grids.  * `stack` - The video layout that displays the active speaker on the stage and up to six participants in thumbnails across the top.  * `focus` - The video layout that only displays the active speaker. Valores: grid, stack, focus.
  - `layoutWithSharedContent` (string): Live streaming layout when there's shared content.  * `stack` - The video layout that displays the shared content on the stage and up to six participants in thumbnails across the top.  * `focusedContentWithActiveSpeaker` - The layout that displays the shared content in the main part of the screen and a large thumbnail of the active speaker in the upper right corner.  * `focusedContent` - The layout that only displays the shared content in the main part of the screen and does not display the participants. Valores: stack, focusedContentWithActiveSpeaker, focusedContent.
  - `allowChangeLayoutInMeeting` (boolean): Whether or not to allow change the live streaming layout in the meeitng.
  - `followStageLayoutWhenSynced` (boolean): Whether or not to follow the stage layout when it's being synchronized.
  - `resolution` (string): Resolution of the live streaming.

### Ejemplo de petición
```json
{
  "title": "Example Daily Meeting Modified",
  "agenda": "Example Agenda Modified",
  "password": "P@ssword789",
  "timezone": "Asia/Shanghai",
  "start": "2020-01-27T20:30:00+08:00",
  "end": "2020-01-27T21:30:00+08:00",
  "enabledAutoRecordMeeting": true,
  "allowAnyUserToBeCoHost": true,
  "enabledJoinBeforeHost": true,
  "enableConnectAudioBeforeHost": true,
  "joinBeforeHostMinutes": 15,
  "excludePassword": false,
  "publicMeeting": false,
  "reminderTime": 30,
  "unlockedMeetingJoinSecurity": "allowJoin",
  "enableAutomaticLock": false,
  "automaticLockMinutes": 0,
  "allowFirstUserToBeCoHost": false,
  "allowAuthenticatedDevices": true,
  "sendEmail": true,
  "hostEmail": "john.andersen@example.com",
  "meetingOptions": {
    "enabledChat": true,
    "enabledVideo": true,
    "enabledPolling": false,
    "enabledNote": true,
    "noteType": "allowAll",
    "enabledFileTransfer": false,
    "enabledUCFRichMedia": false
  },
  "attendeePrivileges": {
    "enabledShareContent": true,
    "enabledSaveDocument": false,
    "enabledPrintDocument": false,
    "enabledAnnotate": false,
    "enabledViewParticipantList": true,
    "enabledViewThumbnails": false,
    "enabledRemoteControl": true,
    "enabledViewAnyDocument": false,
    "enabledViewAnyPage": false,
    "enabledContactOperatorPrivately": false,
    "enabledChatHost": true,
    "enabledChatPresenter": true,
    "enabledChatOtherParticipants": true
  },
  "integrationTags": [
    "dbaeceebea5c4a63ac9d5ef1edfe36b9",
    "85e1d6319aa94c0583a6891280e3437d",
    "27226d1311b947f3a68d6bdf8e4e19a1"
  ],
  "enabledBreakoutSessions": true,
  "trackingCodes": [
    {
      "name": "Department",
      "value": "Sales"
    },
    {
      "name": "Division",
      "value": "Part-time"
    }
  ],
  "enabledAudioWatermark": true,
  "enabledVisualWatermark": true,
  "visualWatermarkOpacity": 40,
  "audioConnectionOptions": {
    "audioConnectionType": "VoIP",
    "enabledTollFreeCallIn": false,
    "enabledGlobalCallIn": false,
    "enabledAudienceCallBack": true,
    "entryAndExitTone": "beep",
    "allowHostToUnmuteParticipants": true,
    "allowAttendeeToUnmuteSelf": false,
    "muteAttendeeUponEntry": true
  },
  "enabledLiveStream": true,
  "liveStream": {
    "destination": "Youtube",
    "rtmpUrl": "rtmps://example.com:1935/MediaLive/WebexStreaming",
    "streamUrl": "https://example.com/Webex-Streaming/index_a.m3u8",
    "layoutWithoutSharedContent": "grid",
    "layoutWithSharedContent": "stack",
    "allowChangeLayoutInMeeting": false,
    "followStageLayoutWhenSynced": true,
    "resolution": "1920x1080"
  }
}
```

## Respuestas
- **200**: OK
  - `id` (string) **(requerido)**: Unique identifier for meeting. For a meeting series, the `id` is used to identify the entire series. For scheduled meetings from a series, the `id` is used to identify that scheduled meeting. For a meeting instance that is in progress or has concluded, the `id` is used to identify that instance.
  - `meetingSeriesId` (string) **(requerido)**: Unique identifier for meeting series. It only apples to scheduled meeting and meeting instance. If it's a scheduled meeting from a series or a meeting instance that is happening or has happened, the `meetingSeriesId` is the `id` of the primary series.
  - `scheduledMeetingId` (string): Unique identifier for scheduled meeting which current meeting is associated with. It only apples to meeting instance which is happening or has happened. It's the `id` of the scheduled meeting this instance is associated with.
  - `meetingNumber` (string): Meeting number. Applies to meeting series, scheduled meeting, and meeting instances, but not to meeting instances which have ended.
  - `title` (string) **(requerido)**: Meeting title. Can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
  - `agenda` (string): Meeting agenda. The agenda can be a maximum of 1300 characters long. This attribute can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
  - `password` (string) **(requerido)**: Meeting password. Applies to meeting series, scheduled meetings, and in-progress meeting instances, but not to meeting instances which have ended. Can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
  - `phoneAndVideoSystemPassword` (string): 8-digit numeric password used to join a meeting from audio and video devices. This attribute applies to meeting series, scheduled meetings, and in-progress meeting instances, but not to meeting instances which have ended.
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
  - `hostKey` (string) **(requerido)**: Key for joining the meeting as host.
  - `siteUrl` (string) **(requerido)**: Site URL for the meeting.
  - `webLink` (string) **(requerido)**: Link to a meeting information page where the meeting client is launched if the meeting is ready to start or join.
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
