---
doc_id: webex-meeting-post-meetings
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: POST
path: /meetings
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.393419+00:00
---

# POST /meetings

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `createMeeting`

## Resumen
Create a Meeting

## Descripción
Creates a new meeting. Regular users can schedule up to 100 meetings in 24 hours and admin users up to 3000 overall or 800 for a single user. Please note that the failed requests are also counted toward the limits.

* The `spark:all` scope is required when `roomId` is specified.

* If the parameter `adhoc` is `true` and `roomId` is specified, an ad-hoc meeting is created for the target room. An ad-hoc meeting is a non-recurring instant meeting for the target room which is supposed to be started immediately after being created for a quick collaboration. There's only one ad-hoc meeting for a room at the same time. So, if there's already an ongoing ad-hoc meeting for the room, the API returns this ongoing meeting instead of creating a new one. If it's a [direct](/docs/api/v1/rooms/get-room-details) room, both members of the room can create an ad-hoc meeting for the room. If it's a [group](/docs/api/v1/rooms/get-room-details) room, only room members that are in the same [organization](/docs/api/v1/organizations/get-organization-details) as the room can create an ad-hoc meeting for the room. Please note that an ad-hoc meeting is for the purpose of an instant collaboration with people in a room, user should not persist the `id` and `meetingNumber` of the ad-hoc meeting when it's been created since this meeting may become an inactive ad-hoc meeting for the room if it's not been started after being created for a while or it has been started and ended. Each time a user needs an ad-hoc meeting for a room, they should create one instead of reusing the previous persisted one. Moreover, for the same reason, no email will be sent when an ad-hoc meeting is created. Ad-hoc meetings cannot be updated by [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) or deleted by [Delete a Meeting](/docs/api/v1/meetings/delete-a-meeting). Ad-hoc meetings cannot be listed by [List Meetings](/docs/api/v1/meetings/list-meetings) and the scheduled meetings of an ad-hoc meeting cannot be listed by [List Meetings of a Meeting Series](/docs/api/v1/meetings/list-meetings-of-a-meeting-series), but the ended and ongoing instances of ad-hoc meetings can be listed by [List Meetings](/docs/api/v1/meetings/list-meetings) and [List Meetings of a Meeting Series](/docs/api/v1/meetings/list-meetings-of-a-meeting-series).

* If the parameter `adhoc` is `true`, `roomId` is required and the others are optional or ignored.

* The default value of `title` for an ad-hoc meeting is the user's name if not specified. The following parameters for an ad-hoc meeting have default values and the user's input values will be ignored: `scheduledType` is always `meeting`; `start` and `end` are 5 minutes after the current time and 20 minutes after the current time respectively; `timezone` is `UTC`; `allowAnyUserToBeCoHost`, `allowAuthenticatedDevices`, `enabledJoinBeforeHost`, `enableConnectAudioBeforeHost` are always `true`; `allowFirstUserToBeCoHost`, `enableAutomaticLock`, `publicMeeting`, `sendEmail` are always `false`; `invitees` is the room members except "me"; `joinBeforeHostMinutes` is 5; `automaticLockMinutes` is null; `unlockedMeetingJoinSecurity` is `allowJoinWithLobby`. An ad-hoc meeting can be started immediately even if the `start` is 5 minutes after the current time.

* The following parameters are not supported and will be ignored for an ad-hoc meeting: `templateId`, `recurrence`, `excludePassword`, `reminderTime`, `registration`, `integrationTags`, `enabledWebcastView`, and `panelistPassword`.

* If the value of the parameter `recurrence` is null, a non-recurring meeting is created.

* If the parameter `recurrence` has a value, a recurring meeting is created based on the rule defined by the value of `recurrence`. For a non-recurring meeting which has no `recurrence` value set, its `meetingType` is also `meetingSeries` which is a meeting series with only one occurrence in Webex meeting modeling. If you specify a `recurrence` like `FREQ=DAILY;INTERVAL=1` which never ends, the furthest date of the series is unlimited. You can also specify a `recurrence` with a very distant ending date in the future, e.g. `FREQ=DAILY;INTERVAL=1;UNTIL=21241001T000000Z`, but the actual furthest date accepted for the recurring meeting is five years from now. Specifically, if it has an ending date, there can be up to 5 occurrences for a yearly meeting, 60 occurrences for a monthly meeting, 261 occurrences for a weekly meeting, or 1826 occurrences for a daily meeting.

* If the parameter `templateId` has a value, the meeting is created based on the meeting template specified by `templateId`. The list of meeting templates that is available for the authenticated user can be retrieved from [List Meeting Templates](/docs/api/v1/meetings/list-meeting-templates).

* If the parameter `siteUrl` has a value, the meeting is created on the specified site. Otherwise, the meeting is created on the user's preferred site. All available Webex sites and preferred site of the user can be retrieved by `Get Site List` API.

* If the parameter `scheduledType` equals "personalRoomMeeting", the meeting is created in the user's [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings).

* If the parameter `roomId` has a value, the meeting is created for the Webex space specified by `roomId`. If `roomId` is specified but the user calling the API is not a member of the Webex space specified by `roomId`, the API will fail even if the user has the admin-level scopes or he is calling the API on behalf of another user which is specified by `hostEmail` and is a member of the Webex space.

* If the parameter `enabledAudioWatermark` is `true`, `scheduledType` equals or defaults to `meeting`, and `audioConnectionOptions.audioConnectionType` equals `VoIP`, the audio for this meeting will have a watermark. In this case, a unique identifier is embedded into the audio that plays out of each Webex app and device. An administrator can use this watermark when analyzing an unauthorized recording to identify which Webex app or device was the source of the recording.

* If the parameter `enabledVisualWatermark` is `true`, the video for this meeting will have a watermark. In this case, Webex superimposes a watermark image pattern on top of the meeting video and shared content to deter participants from leaking meeting information. Each participant viewing the meeting sees a watermark image pattern with their email address. If the participant is not signed in, the watermark image pattern includes their display name and email address.

* The default value of `visualWatermarkOpacity` is 10 if not specified. The value must be between 5 and 80, inclusive. A smaller value means less distraction for meeting participants, while a larger value shows a clearer watermark. It's supported when `enabledVisualWatermark` is `true`.

* When `enabledLiveStream` is `true`, `liveStream` must be specified. With these setting, the RTMP streaming specified by `liveStream.rtmpUrl` can be started and viewed during the meeting without any ad-hoc settings.

* The `registration` can be specified when creating a meeting, but it can't be updated by [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) or [Patch a Meeting](/docs/api/v1/meetings/patch-a-meeting). Create a registration form for a meeting that doesn't have one or update the registration form for a meeting that already has one by using [Update Meeting Registration Form](/docs/api/v1/meetings/update-meeting-registration-form). Delete the registration form for a meeting by using [Delete Meeting Registration Form](/docs/api/v1/meetings/delete-meeting-registration-form).

* You can't create a meeting that starts 10 years or more in the future.

* If all meeting invitees of a meeting should not receive emails, the host can create a meeting with invitees, and the parameter `sendEmail` is set to `false`. If only some meeting invitees should not receive emails and others can, the host should not invite these invitees along with creating a meeting request. Instead, the host should add the invitees by [Create a Meeting Invitee](/docs/api/v1/meeting-invitees/create-a-meeting-invitee) or [Create Meeting Invitees](/docs/api/v1/meeting-invitees/create-meeting-invitees) with the parameter `sendEmail` is set to `false` after the meeting has been created.

## Cuerpo de la petición (application/json)
- `adhoc` (boolean): Whether or not to create an ad-hoc meeting for the room specified by `roomId`. When `true`, `roomId` is required.
- `roomId` (string): Unique identifier for the Webex space which the meeting is to be associated with. It can be retrieved by [List Rooms](/docs/api/v1/rooms/list-rooms). `roomId` is required when `adhoc` is `true`. When `roomId` is specified, the parameter `hostEmail` will be ignored.
- `templateId` (string): Unique identifier for meeting template. Please note that `start` and `end` are optional when `templateId` is specified. The list of meeting templates that is available for the authenticated user can be retrieved from [List Meeting Templates](/docs/api/v1/meetings/list-meeting-templates). This parameter is ignored for an ad-hoc meeting.
- `title` (string) **(requerido)**: Meeting title. The title can be a maximum of 128 characters long. The default value for an ad-hoc meeting is the user's name if not specified.
- `agenda` (string): Meeting agenda. The agenda can be a maximum of 1300 characters long.
- `password` (string): Meeting password. Must conform to the site's password complexity settings. Read [password management](https://help.webex.com/en-us/zrupm6/Manage-Security-Options-for-Your-Site-in-Webex-Site-Administration) for details. If not specified, a random password conforming to the site's password rules will be generated automatically.
- `start` (string) **(requerido)**: Date and time for the start of meeting in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `start` cannot be before current date and time or after `end`. Duration between `start` and `end` cannot be shorter than 10 minutes or longer than 23 hours 59 minutes. Please note that when a meeting is being scheduled, `start` of the meeting will be accurate to minutes, not seconds or milliseconds. Therefore, if `start` is within the same minute as the current time, `start` will be adjusted to the upcoming minute; otherwise, `start` will be adjusted with seconds and milliseconds stripped off. For instance, if the current time is `2022-03-01T10:32:16.657+08:00`, `start` of `2022-03-01T10:32:28.076+08:00` or `2022-03-01T10:32:41+08:00` will be adjusted to `2022-03-01T10:33:00+08:00`, and `start` of `2022-03-01T11:32:28.076+08:00` or `2022-03-01T11:32:41+08:00` will be adjusted to `2022-03-01T11:32:00+08:00`. The default value for an ad-hoc meeting is 5 minutes after the current time and the user's input value will be ignored. An ad-hoc meeting can be started immediately even if the `start` is 5 minutes after the current time.
- `end` (string) **(requerido)**: Date and time for the end of meeting in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `end` cannot be before current date and time or before `start`. Duration between `start` and `end` cannot be shorter than 10 minutes or longer than 23 hours 59 minutes. Please note that when a meeting is being scheduled, `end` of the meeting will be accurate to minutes, not seconds or milliseconds. Therefore, `end` will be adjusted with seconds and milliseconds stripped off. For instance, `end` of `2022-03-01T11:52:28.076+08:00` or `2022-03-01T11:52:41+08:00` will be adjusted to `2022-03-01T11:52:00+08:00`. The default value for an ad-hoc meeting is 20 minutes after the current time and the user's input value will be ignored.
- `timezone` (string): [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) in which the meeting was originally scheduled (conforming with the [IANA time zone database](https://www.iana.org/time-zones)). The default value for an ad-hoc meeting is `UTC` and the user's input value will be ignored.
- `recurrence` (string): Meeting series recurrence rule (conforming with [RFC 2445](https://www.ietf.org/rfc/rfc2445.txt)), applying only to meeting series. It doesn't apply to a scheduled meeting or an ended or ongoing meeting instance. This parameter is ignored for an ad-hoc meeting. Multiple days or dates for monthly or yearly `recurrence` rule are not supported, only the first day or date specified is taken. For example, "FREQ=MONTHLY;INTERVAL=1;COUNT=10;BYMONTHDAY=10,11,12" is not supported and it will be partially supported as "FREQ=MONTHLY;INTERVAL=1;COUNT=10;BYMONTHDAY=10".
- `enabledAutoRecordMeeting` (boolean): Whether or not meeting is recorded automatically.
- `allowAnyUserToBeCoHost` (boolean): Whether or not to allow any attendee with a host account on the target site to become a cohost when joining the meeting. The target site is specified by `siteUrl` parameter when creating the meeting; if not specified, it's the user's preferred site. The default value for an ad-hoc meeting is `true` and the user's input value will be ignored.
- `enabledJoinBeforeHost` (boolean): Whether or not to allow any attendee to join the meeting before the host joins the meeting. The default value for an ad-hoc meeting is `true` and the user's input value will be ignored.
- `enableConnectAudioBeforeHost` (boolean): Whether or not to allow any attendee to connect audio in the meeting before the host joins the meeting. This attribute is only applicable if the `enabledJoinBeforeHost` attribute is set to true. The default value for an ad-hoc meeting is `true` and the user's input value will be ignored.
- `joinBeforeHostMinutes` (number): Number of minutes an attendee can join the meeting before the meeting start time and the host joins. This attribute is only applicable if the `enabledJoinBeforeHost` attribute is set to true. Valid options for a meeting are `0`, `5`, `10`, and `15`, and valid options for a webinar are `0`, `15`, `30`, `45`, and `60`. The default value for an ad-hoc meeting is 0 and the user's input value will be ignored.
- `excludePassword` (boolean): Whether or not to exclude the meeting password from the email invitation. This parameter is ignored for an ad-hoc meeting.
- `publicMeeting` (boolean): Whether or not to allow the meeting to be listed on the public calendar. The default value for an ad-hoc meeting is `false` and the user's input value will be ignored.
- `reminderTime` (number): The number of minutes before the meeting begins, that an email reminder is sent to the host. This parameter is ignored for an ad-hoc meeting.
- `unlockedMeetingJoinSecurity` (string): Specifies how the people who aren't on the invite can join the unlocked meeting. The default value for an ad-hoc meeting is `allowJoinWithLobby` and the user's input value will be ignored.  * `allowJoin` - If the value of `unlockedMeetingJoinSecurity` attribute is `allowJoin`, people can join the unlocked meeting directly.  * `allowJoinWithLobby` - If the value of `unlockedMeetingJoinSecurity` attribute is `allowJoinWithLobby`, people will wait in the lobby until the host admits them.  * `blockFromJoin` - If the value of `unlockedMeetingJoinSecurity` attribute is `blockFromJoin`, people can't join the unlocked meeting. Valores: allowJoin, allowJoinWithLobby, blockFromJoin.
- `sessionTypeId` (number): Unique identifier for a meeting session type for the user. This attribute is required when scheduling a webinar meeting. All available meeting session types enabled for the user can be retrieved using the [List Meeting Session Types](/docs/api/v1/meetings/list-meeting-session-types) API.
- `scheduledType` (string): When set as an attribute in a POST request body, specifies whether it's a regular meeting, a webinar, or a meeting scheduled in the user's [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings). If not specified, it's a regular meeting by default. The default value for an ad-hoc meeting is `meeting` and the user's input value will be ignored.  * `meeting` - Set the value of `scheduledType` attribute to `meeting` for creating a regular meeting.  * `webinar` - Set the value of `scheduledType` attribute to `webinar` for creating a webinar meeting.  * `personalRoomMeeting` - Set the value of `scheduledType` attribute to `personalRoomMeeting` for creating a meeting in the user's [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings). Please note that `templateId`, `roomId`, `integrationTags`, `enabledWebcastView`, `enabledAutoRecordMeeting` and `registration` are not supported when creating a personal room meeting. Valores: meeting, webinar, personalRoomMeeting.
- `enabledWebcastView` (boolean): Whether or not webcast view is enabled. This parameter is ignored for an ad-hoc meeting.
- `panelistPassword` (string): Password for panelists of a webinar meeting. Must conform to the site's password complexity settings. Read [password management](https://help.webex.com/en-us/zrupm6/Manage-Security-Options-for-Your-Site-in-Webex-Site-Administration) for details. If not specified, a random password conforming to the site's password rules will be generated automatically. This parameter is ignored for an ad-hoc meeting.
- `enableAutomaticLock` (boolean): Whether or not to automatically lock the meeting after it starts. The default value for an ad-hoc meeting is `false` and the user's input value will be ignored.
- `automaticLockMinutes` (number): The number of minutes after the meeting begins, for automatically locking it. The default value for an ad-hoc meeting is null and the user's input value will be ignored.
- `allowFirstUserToBeCoHost` (boolean): Whether or not to allow the first attendee of the meeting with a host account on the target site to become a cohost. The target site is specified by `siteUrl` parameter when creating the meeting; if not specified, it's user's preferred site. The default value for an ad-hoc meeting is `false` and the user's input value will be ignored.
- `allowAuthenticatedDevices` (boolean): Whether or not to allow authenticated video devices in the meeting's organization to start or join the meeting without a prompt. The default value for an ad-hoc meeting is `true` and the user's input value will be ignored.
- `invitees` (array): Invitees for meeting. The maximum size of invitees is 1000. If `roomId` is specified and `invitees` is missing, all the members in the space are invited implicitly. If both `roomId` and `invitees` are specified, only those in the `invitees` list are invited. `coHost` for each invitee is `true` by default if `roomId` is specified when creating a meeting, and anyone in the invitee list that is not qualified to be a cohost will be invited as a non-cohost invitee. The user's input value will be ignored for an ad-hoc meeting and the the members of the room specified by `roomId` except "me" will be used by default.
  - `email` (string) **(requerido)**: Email address of meeting invitee.
  - `displayName` (string): Display name of meeting invitee. The maximum length of `displayName` is 128 characters. If not specified but the email has been registered, user's registered name for the email will be taken as `displayName`. If not specified and the email hasn't been registered, the email will be taken as `displayName`.
  - `coHost` (boolean): Whether or not invitee is allowed to be a cohost for the meeting. `coHost` for each invitee is `true` by default if `roomId` is specified when creating a meeting, and anyone in the invitee list that is not qualified to be a cohost will be invited as a non-cohost invitee.
  - `panelist` (boolean): Whether or not an invitee is allowed to be a panelist. Only applies to webinars.
- `sendEmail` (boolean): Whether or not to send emails to host and invitees. It is an optional field and default value is true. The default value for an ad-hoc meeting is `false` and the user's input value will be ignored.
- `hostEmail` (string): Email address for the meeting host. This attribute should only be set if the user or application calling the API has the admin-level scopes. When used, the admin may specify the email of a user in a site they manage to be the meeting host.
- `siteUrl` (string): URL of the Webex site which the meeting is created on. If not specified, the meeting is created on user's preferred site. All available Webex sites and preferred site of the user can be retrieved by `Get Site List` API.
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
  - `enabledSaveDocument` (boolean): Whether or not to allow any attendee to save shared documents, slides, or whiteboards when they are shared as files in the content viewer instead of in a window or application. This option is no longer supported for meetings on a site which has been migrated to the Webex Suite Meeting Platform (WSMP).
  - `enabledPrintDocument` (boolean): Whether or not to allow any attendee to print shared documents, slides, or whiteboards when they are shared as files in the content viewer instead of in a window or application. This option is no longer supported for meetings on a site which has been migrated to the Webex Suite Meeting Platform (WSMP).
  - `enabledAnnotate` (boolean): Whether or not to allow any attendee to annotate shared documents, slides, or whiteboards when they are shared as files in the content viewer instead of in a window or application. This option is no longer supported for meetings on a site which has been migrated to the Webex Suite Meeting Platform (WSMP).
  - `enabledViewParticipantList` (boolean): Whether or not to allow any attendee to view participants.
  - `enabledViewThumbnails` (boolean): Whether or not to allow any attendee to see a small preview image of any page of shared documents or slides when they are shared as files in the content viewer instead of in a window or application. This option is no longer supported for meetings on a site which has been migrated to the Webex Suite Meeting Platform (WSMP).
  - `enabledRemoteControl` (boolean): Whether or not to allow any attendee to control applications, web browsers, or desktops remotely. This option is no longer supported for meetings on a site which has been migrated to the Webex Suite Meeting Platform (WSMP).
  - `enabledViewAnyDocument` (boolean): Whether or not to allow any attendee to view any shared documents or slides when they are shared as files in the content viewer instead of in a window or application. This option is no longer supported for meetings on a site which has been migrated to the Webex Suite Meeting Platform (WSMP).
  - `enabledViewAnyPage` (boolean): Whether or not to allow any attendee to scroll through any page of shared documents or slides when they are shared as files in the content viewer instead of in a window or application. This option is no longer supported for meetings on a site which has been migrated to the Webex Suite Meeting Platform (WSMP).
  - `enabledContactOperatorPrivately` (boolean): Whether or not to allow any attendee to contact the operator privately. This option is no longer supported for meetings on a site which has been migrated to the Webex Suite Meeting Platform (WSMP).
  - `enabledChatHost` (boolean): Whether or not to allow any attendee to chat with the host in private. This option is no longer supported for meetings on a site which has been migrated to the Webex Suite Meeting Platform (WSMP).
  - `enabledChatPresenter` (boolean): Whether or not to allow any attendee to chat with the presenter in private. This option is no longer supported for meetings on a site which has been migrated to the Webex Suite Meeting Platform (WSMP).
  - `enabledChatOtherParticipants` (boolean): Whether or not to allow any attendee to chat with other participants in private. This option is no longer supported for meetings on a site which has been migrated to the Webex Suite Meeting Platform (WSMP).
- `registration` (object): Meeting registration. When this option is enabled, meeting invitees must register personal information in order to join the meeting. Meeting invitees will receive an email with a registration link for the registration. When the registration form has been submitted and approved, an email with a real meeting link will be received. By clicking that link the meeting invitee can join the meeting. Please note that meeting registration does not apply to a meeting when it's a recurring meeting with a `recurrence` field or no `password` or when the feature toggle `DecoupleJBHWithRegistration` is disabled the `Join Before Host` option is enabled for the meeting, See [Register for a Meeting in Cisco Webex Meetings](https://help.webex.com/en-us/nmgmeff/Register-for-a-Meeting-in-Cisco-Webex-Meetings) for details.
  - `autoAcceptRequest` (boolean): Whether or not meeting registration request is accepted automatically.
  - `requireFirstName` (boolean): Whether or not a registrant's first name is required for meeting registration. This option must always be `true`.
  - `requireLastName` (boolean): Whether or not a registrant's last name is required for meeting registration. This option must always be `true`.
  - `requireEmail` (boolean): Whether or not a registrant's email is required for meeting registration. This option must always be `true`.
  - `requireJobTitle` (boolean): Whether or not a registrant's job title is shown or required for meeting registration.
  - `requireCompanyName` (boolean): Whether or not a registrant's company name is shown or required for meeting registration.
  - `requireAddress1` (boolean): Whether or not a registrant's first address field is shown or required for meeting registration.
  - `requireAddress2` (boolean): Whether or not a registrant's second address field is shown or required for meeting registration.
  - `requireCity` (boolean): Whether or not a registrant's city is shown or required for meeting registration.
  - `requireState` (boolean): Whether or not a registrant's state is shown or required for meeting registration.
  - `requireZipCode` (boolean): Whether or not a registrant's postal code is shown or required for meeting registration.
  - `requireCountryRegion` (boolean): Whether or not a registrant's country or region is shown or required for meeting registration.
  - `requireWorkPhone` (boolean): Whether or not a registrant's work phone number is shown or required for meeting registration.
  - `requireFax` (boolean): Whether or not a registrant's fax number is shown or required for meeting registration.
  - `maxRegisterNum` (number): Maximum number of meeting registrations. This only applies to meetings. The maximum number of participants for meetings and webinars, with the limit based on the user capacity and controlled by a toggle at the site level. The default maximum number of participants for webinars is 10000, but the actual maximum number of participants is limited by the user capacity.
  - `customizedQuestions` (array): Customized questions for meeting registration.
    - `question` (string) **(requerido)**: Title of the customized question.
    - `required` (boolean): Whether or not the customized question is required to be answered by participants.
    - `type` (string) **(requerido)**: Type of the question being asked.  * `singleLineTextBox` - Single line text box.  * `multiLineTextBox` - Multiple line text box.  * `checkbox` - Check box which requires `options`.  * `dropdownList` - Drop down list box which requires `options`.  * `radioButtons` - Single radio button which requires `options`. Valores: singleLineTextBox, multiLineTextBox, checkbox, dropdownList, radioButtons.
    - `maxLength` (number): The maximum length of a string that can be entered by the user, ranging from `0` to `999`. Only required by `singleLineTextBox` and `multiLineTextBox`.
    - `options` (array): The content of `options`. Required if the question type is one of `checkbox`, `dropdownList`, or `radioButtons`.
      - `value` (string) **(requerido)**: The content of the option.
    - `rules` (array): The automatic approval rules for customized questions.
      - `condition` (string) **(requerido)**: Judgment expression for approval rules.  * `contains` - The content of the answer contains the value.  * `notContains` - The content of the answer does not contain the value  * `beginsWith` - The content of the answer begins with the value.  * `endsWith` - The content of the answer ends with the value.  * `equals` - The content of the answer is the same as the value.  * `notEquals` - The content of the answer is not the same as the value. Valores: contains, notContains, beginsWith, endsWith, equals, notEquals.
      - `value` (string) **(requerido)**: The keyword for the approval rule. If the rule matches the keyword, the corresponding action will be executed.
      - `result` (string) **(requerido)**: The automatic approval result for the approval rule.  * `approve` - If the user's registration value meets the criteria, the registration form will be automatically approved.  * `reject` - If the user's registration value meets the criteria, the registration form will be automatically rejected. Valores: approve, reject.
      - `matchCase` (boolean): Whether to check the case of values.
  - `rules` (array): The approval rules for standard questions.
    - `question` (string) **(requerido)**: Name for standard question.  * `lastName` - If the value is `lastName`, this approval rule applies to the standard question of "Last Name".  * `email` - If the value is `email`, this approval rule applies to the standard question of "Email".  * `jobTitle` - If the value is `jobTitle`, this approval rule applies to the standard question of "Job Title".  * `companyName` - If the value is `companyName`, this approval rule applies to the standard question of "Company Name".  * `address1` - If the value is `address1`, this approval rule applies to the standard question of "Address 1".  * `address2` - If the value is `address2`, this approval rule applies to the standard question of "Address 2".  * `city` - If the value is `city`, this approval rule applies to the standard question of "City".  * `state` - If the value is `state`, this approval rule applies to the standard question of "State".  * `zipCode` - If the value is `zipCode`, this approval rule applies to the standard question of "Zip/Post Code".  * `countryRegion` - If the value is `countryRegion`, this approval rule applies to the standard question of "Country Region".  * `workPhone` - If the value is `workPhone`, this approval rule applies to the standard question of "Work Phone".  * `fax` - If the value is `fax`, this approval rule applies to the standard question of "Fax". Valores: lastName, email, jobTitle, companyName, address1, address2, city, state, zipCode, countryRegion, workPhone, fax.
    - `condition` (string) **(requerido)**: Judgment expression for approval rules.  * `contains` - The content of the answer contains the value.  * `notContains` - The content of the answer does not contain the value  * `beginsWith` - The content of the answer begins with the value.  * `endsWith` - The content of the answer ends with the value.  * `equals` - The content of the answer is the same as the value.  * `notEquals` - The content of the answer is not the same as the value. Valores: contains, notContains, beginsWith, endsWith, equals, notEquals.
    - `value` (string) **(requerido)**: The keyword for the approval rule. If the rule matches the keyword, the corresponding action will be executed.
    - `result` (string) **(requerido)**: The automatic approval result for the approval rule.  * `approve` - If the user's registration value meets the criteria, the registration form will be automatically approved.  * `reject` - If the user's registration value meets the criteria, the registration form will be automatically rejected. Valores: approve, reject.
    - `matchCase` (boolean): Whether to check the case of values.
    - `order` (number) **(requerido)**: The priority number of the approval rule. Approval rules for standard questions and custom questions need to be ordered together.
- `integrationTags` (array): External keys created by an integration application in its own domain, for example Zendesk ticket IDs, Jira IDs, Salesforce Opportunity IDs, etc. The integration application queries meetings by a key in its own domain. The maximum size of `integrationTags` is 3 and each item of `integrationTags` can be a maximum of 64 characters long. This parameter is ignored for an ad-hoc meeting.
- `simultaneousInterpretation` (object): Simultaneous interpretation information for a meeting.
  - `enabled` (boolean) **(requerido)**: Whether or not simultaneous interpretation is enabled.
  - `interpreters` (array): Interpreters for meeting.
    - `languageCode1` (string) **(requerido)**: Forms a set of simultaneous interpretation channels together with `languageCode2`. Standard language format from [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) code. Read [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for details.
    - `languageCode2` (string) **(requerido)**: Forms a set of simultaneous interpretation channels together with `languageCode1`. Standard language format from [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) code. Read [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for details.
    - `email` (string): Email address of meeting interpreter.
    - `displayName` (string): Display name of meeting interpreter.
- `enabledBreakoutSessions` (boolean): Whether or not breakout sessions are enabled.
- `breakoutSessions` (array): Breakout sessions are smaller groups that are split off from the main meeting or webinar. They allow a subset of participants to collaborate and share ideas over audio and video. Use breakout sessions for workshops, classrooms, or for when you need a moment to talk privately with a few participants outside of the main session. Please note that maximum number of breakout sessions in a meeting or webinar is 100. In webinars, if hosts preassign attendees to breakout sessions, the role of `attendee` will be changed to `panelist`. Breakout session is not supported for a meeting with simultaneous interpretation.
  - `name` (string) **(requerido)**: Name for breakout session.
  - `invitees` (array): Invitees for breakout session. Please note that one invitee cannot be assigned to more than one breakout session.
- `trackingCodes` (array): Tracking codes information. All available tracking codes and their options for the specified site can be retrieved by [List Meeting Tracking Codes](/docs/api/v1/meetings/list-meeting-tracking-codes) API. If an optional tracking code is missing from the `trackingCodes` array and there's a default option for this tracking code, the default option is assigned automatically. If the `inputMode` of a tracking code is `select`, its value must be one of the site-level options or the user-level value. Tracking code is not supported for a personal room meeting or an ad-hoc space meeting.
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
- `enabledLiveStream` (boolean): Whether or not live streaming is enabled. If it's enabled, the `liveStream` must be specified. The RTMP streaming specified by `liveStream.rtmpUrl` can be started and viewed during the meeting without any ad-hoc settings.
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
  "title": "Example Daily Meeting",
  "agenda": "Example Agenda",
  "password": "BgJep@43",
  "start": "2019-11-01 20:00:00",
  "end": "2019-11-01 21:00:00",
  "timezone": "Asia/Shanghai",
  "recurrence": "FREQ=DAILY;INTERVAL=1;COUNT=10",
  "enabledAutoRecordMeeting": false,
  "allowAnyUserToBeCoHost": false,
  "enabledJoinBeforeHost": false,
  "enableConnectAudioBeforeHost": false,
  "joinBeforeHostMinutes": 0,
  "excludePassword": false,
  "publicMeeting": false,
  "reminderTime": 10,
  "unlockedMeetingJoinSecurity": "allowJoin",
  "enableAutomaticLock": false,
  "automaticLockMinutes": 0,
  "allowFirstUserToBeCoHost": false,
  "allowAuthenticatedDevices": false,
  "invitees": [
    {
      "email": "john.andersen@example.com",
      "displayName": "John Andersen",
      "coHost": false,
      "panelist": false
    },
    {
      "email": "brenda.song@example.com",
      "displayName": "Brenda Song",
      "coHost": false,
      "panelist": false
    }
  ],
  "sendEmail": true,
  "hostEmail": "john.andersen@example.com",
  "siteUrl": "site4-example.webex.com",
  "registration": {
    "requireFirstName": true,
    "requireLastName": true,
    "requireEmail": true,
    "requireCompanyName": true,
    "requireCountryRegion": false,
    "requireWorkPhone": true,
    "enabledRegistrationId": false,
    "customizedQuestions": [
      {
        "question": "What color do you like?",
        "required": true,
        "type": "checkbox",
        "options": [
          {
            "value": "green"
          },
          {
            "value": "black"
          },
          {
            "value": "yellow"
          },
          {
            "value": "red"
          }
        ],
        "rules": [
          {
            "condition": "notEquals",
            "value": "red",
            "result": "reject",
            "matchCase": true
          }
        ]
      },
      {
        "question": "Project Team",
        "type": "singleLineTextBox",
        "maxLength": 120
      },
      {
        "question": "How are you",
        "type": "multiLineTextBox"
      },
      {
        "question": "Dropdownlist Q",
        "type": "dropdownList",
        "options": [
          {
            "value": "A1"
          },
          {
            "value": "A2"
          }
        ]
      },
      {
        "question": "weather",
        "required": false,
        "type": "radioButtons",
        "maxLength": 120,
        "options": [
          {
            "value": "sunny"
          },
          {
            "value": "rain"
          }
        ]
      }
    ],
    "rules": [
      {
        "question": "lastName",
        "condition": "endsWith",
        "value": "tom",
        "result": "reject",
        "matchCase": false,
        "order": 1
      }
    ]
  },
  "integrationTags": [
    "dbaeceebea5c4a63ac9d5ef1edfe36b9",
    "85e1d6319aa94c0583a6891280e3437d",
    "27226d1311b947f3a68d6bdf8e4e19a1"
  ],
  "simultaneousInterpretation": {
    "enabled": true,
    "interpreters": [
      {
        "languageCode1": "en",
        "languageCode2": "de",
        "email": "marcus.hoffmann@example.com",
        "displayName": "Hoffmann"
      },
      {
        "languageCode1": "en",
        "languageCode2": "fr",
        "email": "antoine.martin@example.com",
        "displayName": "Martin"
      }
    ]
  },
  "enabledBreakoutSessions": true,
  "breakoutSessions": [
    {
      "name": "Breakout Session 1",
      "invitees": [
        "rachel.green@example.com",
        "monica.geller@example.com"
      ]
    },
    {
      "name": "Breakout Session N",
      "invitees": [
        "ross.geller@example.com",
        "chandler.bing@example.com"
      ]
    }
  ],
  "trackingCodes": [
    {
      "name": "Department",
      "value": "Engineering"
    },
    {
      "name": "Division",
      "value": "Full-time"
    }
  ],
  "enabledAudioWatermark": true,
  "enabledVisualWatermark": true,
  "visualWatermarkOpacity": 10,
  "scheduledType": "meeting",
  "audioConnectionOptions": {
    "audioConnectionType": "VoIP"
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
  - `meetingNumber` (string): Meeting number. Applies to meeting series, scheduled meeting, and meeting instances, but not to meeting instances which have ended.
  - `title` (string) **(requerido)**: Meeting title. Can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
  - `agenda` (string): Meeting agenda. The agenda can be a maximum of 1300 characters long. This attribute can be modified for a meeting series or a scheduled meeting using the  [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
  - `password` (string) **(requerido)**: Meeting password. Applies to meeting series, scheduled meetings, and in-progress meeting instances, but not to meeting instances which have ended. Can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
  - `phoneAndVideoSystemPassword` (string): 8-digit numeric password used to join a meeting from audio and video devices. This attribute applies to meeting series, scheduled meetings, and in-progress meeting instances, but not to meeting instances which have ended.
  - `meetingType` (string) **(requerido)**: Meeting type.  * `meetingSeries` - Primary instance of a scheduled series of meetings which consists of one or more scheduled meetings based on a `recurrence` rule. When a non-recurring meeting is scheduled with no `recurrence`, its `meetingType` is also `meetingSeries` which is a meeting series with only one occurrence in Webex meeting modeling.  * `scheduledMeeting` - Instance from a primary meeting series.  * `meeting` - Meeting instance that is in progress or has completed. Valores: meetingSeries, scheduledMeeting, meeting.
  - `state` (string) **(requerido)**: Meeting state.  * `active` - Only applies to a meeting series. Indicates that one or more future scheduled meetings exist for this meeting series.  * `scheduled` - Only applies to scheduled meeting. Indicates that the meeting is scheduled in the future.  * `ready` - Only applies to scheduled meeting. Indicates that this scheduled meeting is ready to start or join immediately.  * `lobby` - Only applies to meeting instances. Indicates that a locked meeting has been joined by participants, but no hosts have joined.  * `inProgress` - Applies to meeting series and meeting instances. For a meeting series, indicates that an instance of this series is happening now. For a meeting instance, indicates that the meeting has been joined and unlocked.  * `ended` - Applies to scheduled meetings and meeting instances. For scheduled meetings, indicates that the meeting was started and is now over. For meeting instances, indicates that the meeting instance has concluded.  * `missed` - This state only applies to scheduled meetings. Indicates that the meeting was scheduled in the past but never happened.  * `expired` - This state only applies to a meeting series. Indicates that all scheduled meetings of this series have passed. Valores: active, scheduled, ready, lobby, inProgress, ended, missed, expired.
  - `hostDidJoin` (boolean): Only applies to meeting series in the `inProgress` state, scheduled meetings in the `ready` state, and meeting instances in the `inProgress` state, whether or not the meeting host joined the meeting. If true, the meeting host has joined the meeitng even if they dropped off; otherwise, the meeting host hasn't ever join the meeting. Indicates that someone is waiting in the lobby and the host hasn't joined the meeting if `attendeeDidJoin` is true and `hostDidJoin` is false.
  - `attendeeDidJoin` (boolean): Only applies to meeting series in the `inProgress` state, scheduled meetings in the `ready` state, and meeting instances in the `inProgress` state. Whether or not anyone has joined the meeting. If true, the meeting host or any attendee has joined the meeting; otherwise, no one has joined the meeting. Indicates that someone is waiting in the lobby and the host hasn't joined the meeting if `attendeeDidJoin` is true and `hostDidJoin` is false.
  - `timezone` (string) **(requerido)**: [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) of `start` and `end`, conforming with the [IANA time zone database](https://www.iana.org/time-zones).
  - `start` (string) **(requerido)**: Start time for meeting in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. If the meeting is a meeting series, `start` is the date and time the first meeting of the series starts. If the meeting is a meeting series and the `current` filter is true, `start` is the date and time the upcoming or ongoing meeting of the series starts. If the meeting is a scheduled meeting from a meeting series, `start` is the date and time when that scheduled meeting starts. If the meeting is a meeting instance that has happened or is happening, `start` is the date and time that the instance actually starts. Can be modified for a meeting series or a scheduled meeting using the  [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
  - `end` (string) **(requerido)**: End time for a meeting in ISO 8601 compliant format. If the meeting is a meeting series, `end` is the date and time the first meeting of the series ends. If the meeting is a meeting series and the current filter is true, `end` is the date and time the upcoming or ongoing meeting of the series ends. If the meeting is a scheduled meeting from a meeting series, `end` is the date and time when that scheduled meeting ends. If the meeting is a meeting instance that has happened, `end` is the date and time that instance actually ends. If a meeting instance is in progress, `end` is not available. Can be modified for a meeting series or a scheduled meeting using the  [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
  - `recurrence` (string): Meeting series recurrence rule (conforming with [RFC 2445](https://www.ietf.org/rfc/rfc2445.txt)). Applies only to a recurring meeting series, not to a meeting series with only one scheduled meeting. Can be modified for a meeting series using the  [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API. Multiple days or dates for monthly or yearly `recurrence` rule are not supported, only the first day or date specified is taken. For example, "FREQ=MONTHLY;INTERVAL=1;COUNT=10;BYMONTHDAY=10,11,12" is not supported and it will be partially supported as "FREQ=MONTHLY;INTERVAL=1;COUNT=10;BYMONTHDAY=10". For a non-recurring meeting which has no `recurrence`, its `meetingType` is also `meetingSeries` which is a meeting series with only one occurrence in Webex meeting modeling.
  - `hostUserId` (string) **(requerido)**: Unique identifier for the meeting host.
  - `hostDisplayName` (string) **(requerido)**: Display name for the meeting host.
  - `hostEmail` (string) **(requerido)**: Email address for the meeting host.
  - `hostKey` (string) **(requerido)**: Key for joining the meeting as host.
  - `siteUrl` (string) **(requerido)**: Site URL for the meeting.
  - `webLink` (string) **(requerido)**: Link to a meeting information page where the meeting client is launched if the meeting is ready to start or join.
  - `registerLink` (string): Link to register a meeting which has enabled registration.
  - `sipAddress` (string): SIP address for callback from a video system.
  - `dialInIpAddress` (string): IP address for callback from a video system.
  - `roomId` (string): Room ID of the associated Webex space. Only applies to ad-hoc meetings and space meetings.
  - `enabledAutoRecordMeeting` (boolean): Whether or not meeting is recorded automatically. Can be modified for a meeting series or a scheduled meeting using the  [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
  - `allowAnyUserToBeCoHost` (boolean): Whether or not to allow any attendee with a host account on the target site to become a cohost when joining the meeting. The target site is specified by a `siteUrl` parameter when creating the meeting. If not specified, it's a user's preferred site. The `allowAnyUserToBeCoHost` attribute can be modified for a meeting series or a scheduled meeting using the [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
  - `enabledJoinBeforeHost` (boolean): Whether or not to allow any attendee to join the meeting before the host joins the meeting. The `enabledJoinBeforeHost` attribute can be modified for a meeting series or a scheduled meeting using the  [Update a Meeting](/docs/api/v1/meetings/update-a-meeting) API.
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
