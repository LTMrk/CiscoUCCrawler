---
doc_id: webex-meeting-get-meetings-templates-templateid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /meetings/templates/{templateId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.395437+00:00
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
- `templateId` [path] (string) **(requerido)**: Unique identifier for the meeting template being requested.
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes. If set, the admin may specify the email of a user in a site they manage and the API will return the meeting template that is available for that user.
- `timezone` [header] (string): e.g. UTC

## Respuestas
- **200**: OK
  - `id` (string) **(requerido)**: Unique identifier for meeting template.
  - `name` (string) **(requerido)**: Meeting template name.
  - `locale` (string) **(requerido)**: Meeting template locale.
  - `siteUrl` (string) **(requerido)**: Site URL for the meeting template.
  - `templateType` (string) **(requerido)**: Meeting template type.  * `meeting` - Webex meeting.  * `webinar` - Webex webinar. Valores: meeting, webinar.
  - `isDefault` (boolean) **(requerido)**: Whether or not the meeting template is a default template.
  - `isStandard` (boolean) **(requerido)**: Whether or not the meeting template is a standard template.
  - `meeting` (object) **(requerido)**:
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
