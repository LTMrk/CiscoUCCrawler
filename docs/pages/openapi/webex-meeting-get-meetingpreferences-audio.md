---
doc_id: webex-meeting-get-meetingpreferences-audio
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /meetingPreferences/audio
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.388260+00:00
---

# GET /meetingPreferences/audio

**API:** Webex Meetings
**Área:** Preferences
**operationId:** `Get Audio Options`

## Resumen
Get Audio Options

## Descripción
Retrieves audio options for the authenticated user.

## Parámetros
- `userEmail` [query] (string): Email address for the user. This parameter is only used if the user or application calling the API has the [admin-level scopes](/docs/meetings#adminorganization-level-authentication-and-scopes). If set, the admin may specify the email of a user in a site they manage and the API will return details of the audio options for that user.
- `siteUrl` [query] (string): URL of the Webex site to query. For individual use, if `siteUrl` is not specified, the query will use the default site of the user. For admin use, if `siteUrl` is not specified, the query will use the default site for the admin's authorization token used to make the call. In the case where the user belongs to a site different than the admin’s default site, the admin can set the site to query using the `siteUrl` parameter. All available Webex sites and default site of a user can be retrieved from [/meetingPreferences/sites](/docs/api/v1/meeting-preferences/get-site-list).

## Respuestas
- **200**: OK
  - `defaultAudioType` (string) **(requerido)**: Default audio type. This attribute can be modified with the with the [Update Audio Options](/docs/api/v1/meeting-preferences/update-audio-options) API.  * `webexAudio` - Webex audio. This supports telephony and VoIP.  * `voipOnly` - Support only VoIP.  * `otherTeleconferenceService` - Other teleconference service. Details are defined in the `otherTeleconferenceDescription` parameter.  * `none` - No audio. Valores: webexAudio, voipOnly, otherTeleconferenceService, none.
  - `otherTeleconferenceDescription` (string) **(requerido)**: Phone number and other information for the teleconference provider to be used, along with instructions for invitees. This attribute can be modified with the with the [Update Audio Options](/docs/api/v1/meeting-preferences/update-audio-options) API.
  - `enabledGlobalCallIn` (boolean) **(requerido)**: Flag to enable/disable global call ins. ***Note***: If the site does not support global call-ins, you cannot set this option. This attribute can be modified with the with the [Update Audio Options](/docs/api/v1/meeting-preferences/update-audio-options) API.
  - `enabledTollFree` (boolean) **(requerido)**: Flag to enable/disable call-ins from toll-free numbers.  ***Note***: If the site does not support calls from toll-free numbers, you cannot set this option. This attribute can be modified with the with the [Update Audio Options](/docs/api/v1/meeting-preferences/update-audio-options) API.
  - `enabledAutoConnection` (boolean) **(requerido)**: Flag to enable/disable automatically connecting to audio using a computer. The meeting host can enable/disable this option. When this option is set to `true`, the user is automatically connected to audio via a computer when they start or join a Webex Meetings meeting on a desktop. This attribute can be modified with the with the [Update Audio Options](/docs/api/v1/meeting-preferences/update-audio-options) API.
  - `audioPin` (string): PIN to provide a secondary level of authentication for calls where the host is using the phone and may need to invite additional invitees. It must be exactly 4 digits. It cannot contain sequential digits, such as 1234 or 4321, or repeat a digit 4 times, such as 1111. This attribute can be modified with the with the [Update Audio Options](/docs/api/v1/meeting-preferences/update-audio-options) API.
  - `officeNumber` (object) **(requerido)**: Office phone number. We recommend that phone numbers be specified to facilitate connecting via audio. This attribute can be modified with the with the [Update Audio Options](/docs/api/v1/meeting-preferences/update-audio-options) API.
    - `countryCode` (string) **(requerido)**: Country code for the phone number. This attribute can be modified with the with the [Update Audio Options](/docs/api/v1/meeting-preferences/update-audio-options) API.
    - `number` (string) **(requerido)**: Phone number. It cannot be longer than 30 characters. This attribute can be modified with the with the [Update Audio Options](/docs/api/v1/meeting-preferences/update-audio-options) API.
    - `enabledCallInAuthentication` (boolean) **(requerido)**: Flag identifying the phone number as the one that will be used to dial into a teleconference. This attribute can be modified with the with the [Update Audio Options](/docs/api/v1/meeting-preferences/update-audio-options) API.
    - `enabledCallMe` (boolean) **(requerido)**: Flag to enable/disable Call Me number display on the meeting client. This attribute can be modified with the with the [Update Audio Options](/docs/api/v1/meeting-preferences/update-audio-options) API. ***Note***: This feature is only effective if the site supports the ***Call Me*** feature.
  - `mobileNumber` (object) **(requerido)**: Mobile phone number. We recommend that phone numbers be specified to facilitate connecting via audio. This attribute can be modified with the with the [Update Audio Options](/docs/api/v1/meeting-preferences/update-audio-options) API.
    - `countryCode` (string) **(requerido)**: Country code for the phone number. This attribute can be modified with the with the [Update Audio Options](/docs/api/v1/meeting-preferences/update-audio-options) API.
    - `number` (string) **(requerido)**: Phone number. It cannot be longer than 30 characters. This attribute can be modified with the with the [Update Audio Options](/docs/api/v1/meeting-preferences/update-audio-options) API.
    - `enabledCallInAuthentication` (boolean) **(requerido)**: Flag identifying the phone number as the one that will be used to dial into a teleconference. This attribute can be modified with the with the [Update Audio Options](/docs/api/v1/meeting-preferences/update-audio-options) API.
    - `enabledCallMe` (boolean) **(requerido)**: Flag to enable/disable Call Me number display on the meeting client. This attribute can be modified with the with the [Update Audio Options](/docs/api/v1/meeting-preferences/update-audio-options) API. ***Note***: This feature is only effective if the site supports the ***Call Me*** feature.
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden
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
