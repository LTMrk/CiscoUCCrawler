---
doc_id: webex-meeting-get-admin-meeting-config-commonsettings
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /admin/meeting/config/commonSettings
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.404222+00:00
---

# GET /admin/meeting/config/commonSettings

**API:** Webex Meetings
**Área:** Site
**operationId:** `getMeetingCommonSettingsConfiguration`

## Resumen
Get Meeting Common Settings Configuration

## Descripción
Site administrators can use this API to get a list of functions, options, and privileges that are configured for their Webex service sites.

* If `siteUrl` is specified, common settings of the meeting's configuration of the specified site will be queried; otherwise, the API will query from the site administrator's preferred site. All available Webex sites and preferred site of the user can be retrieved by [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

## Parámetros
- `siteUrl` [query] (string): URL of the Webex site which the API queries common settings of the meeting's configuration from. If not specified, the API will query from the site administrator's preferred site. All available Webex sites and the preferred site of the user can be retrieved by the [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

## Respuestas
- **200**: OK
  - `siteOptions` (object): Site Options on Webex Administration.
    - `allowCustomPersonalRoomURL` (boolean): Allow hosts to change their Personal Room URLs.
  - `telephonyConfig` (object): Telephony Configuration on WebEx Super Admin (These options are read-only, unable to update by Update Common Settings API).
    - `allowCallIn` (boolean): Whether call-in teleconferencing for sessions was enabled.
    - `allowCallBack` (boolean): Whether call-back teleconferencing for sessions was enabled.
    - `allowOtherTeleconf` (boolean): Whether other teleconferencing for sessions was enabled.
    - `allowTollFreeCallin` (boolean): Whether toll-free call-in teleconferencing was enabled.
    - `allowInternationalCallin` (boolean): Whether international call-in teleconferencing was enabled.
    - `allowInternationalCallback` (boolean): Whether international call-back teleconferencing was enabled.
    - `VoIP` (boolean): Whether Voice Over IP functionality using the attendee computer's speakers and microphones was enabled.
  - `defaultSchedulerOptions` (object): Default Scheduler Options on Webex Administration (These options are applied to the site as defaults, but individual users can change them).
    - `entryAndExitTone` (string) **(requerido)**: Determines if a sound is made when someone enters or exits.  * `NoTone` - No tone.  * `Beep` - Beep.  * `AnnounceName` - Announce name. Valores: NoTone, Beep, AnnounceName.
    - `joinTeleconfNotPress1` (boolean): Specifies whether or not joining teleconference without pressing 1 is checked by default.
    - `telephonySupport` (string) **(requerido)**: Specifies the type of teleconference support for meetings.  * `None` - None.  * `WebexTeleconferencing` - Webex teleconferencing.  * `Other` - Other Teleconferencing. Valores: None, WebexTeleconferencing, Other.
    - `tollFree` (boolean): Specifies whether toll-free call-in is available.
    - `VoIP` (boolean): Denotes if VoIP protocols are being used.
  - `scheduleMeetingOptions` (object): Schedule Meeting Options on Webex Administration.
    - `emailReminders` (boolean): Determines if email reminders are to be sent out.
  - `securityOptions` (object): Security Options on Webex Administration.
    - `joinBeforeHost` (boolean): Allow attendees or panelists to join before the host.
    - `audioBeforeHost` (boolean): Allows attendees or panelists to join the teleconference before the host.
    - `firstAttendeeAsPresenter` (boolean): Allows first attendee or panelist as the presenter.
    - `unlistAllMeetings` (boolean): Specifies that all meetings must be unlisted.
    - `requireLoginBeforeAccess` (boolean): Determines if a user must login before getting site access.
    - `allowMobileScreenCapture` (boolean): Allow screen capture (Android devices only).
    - `requireStrongPassword` (boolean): Determines if strict passwords are required for meetings.
    - `passwordCriteria` (object): Criteria of a strong password.
      - `mixedCase` (boolean): Determines if a password requires mixed case.
      - `minLength` (number): Sets the minimum password length.
      - `minNumeric` (number): Sets the minimum number of numeric characters in the password.
      - `minAlpha` (number): Sets the minimum number of alphabetical characters in the password.
      - `minSpecial` (number): Sets the minimum number of special characters in the password.
      - `disallowDynamicWebText` (boolean): Do not allow dynamic web page text for meeting passwords (like site name, host's name, username, meeting topic).
      - `disallowList` (boolean): Specifies if passwords from the `disallowValues` list are to be allowed.
      - `disallowValues` (array): Sets password values that are not allowed.
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
