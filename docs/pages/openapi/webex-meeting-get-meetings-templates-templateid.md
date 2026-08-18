---
doc_id: webex-meeting-get-meetings-templates-templateid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /meetings/templates/{templateId}
operation_id: getTemplateById
tags: Meetings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.483331+00:00
---

# GET /meetings/templates/{templateId}

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `getTemplateById`

## Resumen
Get a Meeting Template

## Descripción
Retrieves details for a meeting template with a specified meeting template ID.

#### Request Header

* `timezone`: [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) for time stamps in response body, defined in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default value is `UTC` if not specified.

## Parámetros
- `templateId` [path] (string) (**requerido**): Unique identifier for the meeting template being requested.
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes. If set, the admin may specify the email of a user in a site they manage and the API will return the meeting template that is available for that user.
- `timezone` [header] (string): e.g. UTC

## Ejemplo de invocación
```bash
curl -X GET '/meetings/templates/<templateId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Unique identifier for meeting template.
- `name` (string) (**requerido**): Meeting template name.
- `locale` (string) (**requerido**): Meeting template locale.
- `siteUrl` (string) (**requerido**): Site URL for the meeting template.
- `templateType` (string) (**requerido**): Meeting template type.  * `meeting` - Webex meeting.  * `webinar` - Webex webinar. Valores: meeting, webinar.
- `isDefault` (boolean) (**requerido**): Whether or not the meeting template is a default template.
- `isStandard` (boolean) (**requerido**): Whether or not the meeting template is a standard template.
- `meeting` (object) (**requerido**):
  - `adhoc` (boolean): Whether or not to create an ad-hoc meeting for the room specified by `roomId`. When `true`, `roomId` is required.
  - `roomId` (string): Unique identifier for the Webex space which the meeting is to be associated with. It can be retrieved by [List Rooms](/docs/api/v1/rooms/list-rooms). `roomId` is required when `adhoc` is `true`. When `roomId` is specified, the parameter `hostEmail` will be ignored.
  - `templateId` (string): Unique identifier for meeting template. Please note that `start` and `end` are optional when `templateId` is specified. The list of meeting templates that is available for the authenticated user can be retrieved from [List Meeting Templates](/docs/api/v1/meetings/list-meeting-templates). This parameter is ignored for an ad-hoc meeting.
  - `title` (string) (**requerido**): Meeting title. The title can be a maximum of 128 characters long. The default value for an ad-hoc meeting is the user's name if not specified.
  - `agenda` (string): Meeting agenda. The agenda can be a maximum of 1300 characters long.
  - `password` (string): Meeting password. Must conform to the site's password complexity settings. Read [password management](https://help.webex.com/en-us/zrupm6/Manage-Security-Options-for-Your-Site-in-Webex-Site-Administration) for details. If not specified, a random password conforming to the site's password rules will be generated automatically.
  - `start` (string) (**requerido**): Date and time for the start of meeting in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `start` cannot be before current date and time or after `end`. Duration between `start` and `end` cannot be shorter than 10 minutes or longer than 23 hours 59 minutes. Please note that when a meeting is being scheduled, `start` of the meeting will be accurate to minutes, not seconds or milliseconds. Therefore, if `start` is within the same minute as the current time, `start` will be adjusted to the upcoming minute; otherwise, `start` will be adjusted with seconds and milliseconds stripped off. For instance, if the current time is `2022-03-01T10:32:16.657+08:00`, `start` of `2022-03-01T10:32:28.076+08:00` or `2022-03-01T10:32:41+08:00` will be adjusted to `2022-03-01T10:33:00+08:00`, and `start` of `2022-03-01T11:32:28.076+08:00` or `2022-03-01T11:32:41+08:00` will be adjusted to `2022-03-01T11:32:00+08:00`. The default value for an ad-hoc meeting is 5 minutes after the current time and the user's input value will be ignored. An ad-hoc meeting can be started immediately even if the `start` is 5 minutes after the current time.
  - `end` (string) (**requerido**): Date and time for the end of meeting in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `end` cannot be before current date and time or before `start`. Duration between `start` and `end` cannot be shorter than 10 minutes or longer than 23 hours 59 minutes. Please note that when a meeting is being scheduled, `end` of the meeting will be accurate to minutes, not seconds or milliseconds. Therefore, `end` will be adjusted with seconds and milliseconds stripped off. For instance, `end` of `2022-03-01T11:52:28.076+08:00` or `2022-03-01T11:52:41+08:00` will be adjusted to `2022-03-01T11:52:00+08:00`. The default value for an ad-hoc meeting is 20 minutes after the current time and the user's input value will be ignored.
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
    - `email` (string) (**requerido**): Email address of meeting invitee.
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

### Ejemplo — respuesta 200
```json
{
  "id": "N2Q3ZWE1ZjQyYjkyMWVhY2UwNTM4NmNhMjRhZDczMGU6VS0yMDA5NzItTUMtZW5fVVM",
  "name": "Meeting template 1",
  "locale": "en_US",
  "siteUrl": "site4-example.webex.com",
  "templateType": "meeting",
  "isDefault": false,
  "isStandard": false,
  "meeting": {
    "title": "My meeting template 1",
    "agenda": "My meeting template 1 agenda",
    "password": "gugUTMY4?25",
    "start": "2021-11-09T03:19:00Z",
    "end": "2021-11-09T03:39:00Z",
    "timezone": "UTC",
    "enabledJoinBeforeHost": false,
    "joinBeforeHostMinutes": 0,
    "enableConnectAudioBeforeHost": false,
    "hostEmail": "john.andersen@example.com",
    "sendEmail": true,
    "invitees": [
      {
        "email": "brenda.song@example.com",
        "displayName": "Brenda Song",
        "coHost": false,
        "panelist": false
      },
      {
        "email": "catherine.sinu@example.com",
        "displayName": "Catherine Sinu",
        "coHost": false,
        "panelist": false
      }
    ],
    "enabledAutoRecordMeeting": false,
    "allowAnyUserToBeCoHost": false,
    "allowFirstUserToBeCoHost": false,
    "allowAuthenticatedDevices": false,
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
      "enabledPrin
  ... (truncado)
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