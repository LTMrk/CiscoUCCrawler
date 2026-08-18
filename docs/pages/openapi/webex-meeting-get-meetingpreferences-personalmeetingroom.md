---
doc_id: webex-meeting-get-meetingpreferences-personalmeetingroom
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /meetingPreferences/personalMeetingRoom
operation_id: Get Personal Meeting Room Options
tags: Preferences
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.468954+00:00
---

# GET /meetingPreferences/personalMeetingRoom

**API:** Webex Meetings
**Área:** Preferences
**operationId:** `Get Personal Meeting Room Options`

## Resumen
Get Personal Meeting Room Options

## Descripción
Retrieves the Personal Meeting Room options for the authenticated user.

## Parámetros
- `userEmail` [query] (string): Email address for the user. This parameter is only used if the user or application calling the API has the [admin-level scopes](/docs/meetings#adminorganization-level-authentication-and-scopes). If set, the admin may specify the email of a user in a site they manage and the API will return details of the Personal Meeting Room options for that user.
- `siteUrl` [query] (string): URL of the Webex site to query. For individual use, if `siteUrl` is not specified, the query will use the default site of the user. For admin use, if `siteUrl` is not specified, the query will use the default site for the admin's authorization token used to make the call. In the case where the user belongs to a site different than the admin’s default site, the admin can set the site to query using the `siteUrl` parameter. All available Webex sites and default site of a user can be retrieved from [/meetingPreferences/sites](/docs/api/v1/meeting-preferences/get-site-list).

## Ejemplo de invocación
```bash
curl -X GET '/meetingPreferences/personalMeetingRoom' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `topic` (string) (**requerido**): Personal Meeting Room topic. The length of `topic` is between 1 and 128. This attribute can be modified with the [Update Personal Meeting Room Options](/docs/api/v1/meeting-preferences/update-personal-meeting-room-options) API.
- `hostPin` (string) (**requerido**): PIN for joining the room as host. The host PIN must be digits of a predefined length, e.g. 4 digits. It cannot contain sequential digits, such as 1234 or 4321, or repeated digits of the predefined length, such as 1111. The predefined length for host PIN can be viewed in user's `My Personal Room` page and it can only be changed by site administrator. This attribute can be modified with the [Update Personal Meeting Room Options](/docs/api/v1/meeting-preferences/update-personal-meeting-room-options) API.
- `personalMeetingRoomLink` (string) (**requerido**): Personal Meeting Room link. It cannot be empty. ***Note***: This is a read-only attribute.
- `enabledAutoLock` (boolean) (**requerido**): Option to automatically lock the Personal Room a number of minutes after a meeting starts. When a room is locked, invitees cannot enter until the owner admits them. The period after which the meeting is locked is defined by `autoLockMinutes`. This attribute can be modified with the [Update Personal Meeting Room Options](/docs/api/v1/meeting-preferences/update-personal-meeting-room-options) API.
- `autoLockMinutes` (number): Number of minutes after which the Personal Room is locked if `enabledAutoLock` is enabled. Valid options are 0, 5, 10, 15 and 20. This attribute can be modified with the [Update Personal Meeting Room Options](/docs/api/v1/meeting-preferences/update-personal-meeting-room-options) API.
- `enabledNotifyHost` (boolean) (**requerido**): Flag to enable notifying the owner of a Personal Room when someone enters the Personal Room lobby while the owner is not in the room. This attribute can be modified with the [Update Personal Meeting Room Options](/docs/api/v1/meeting-preferences/update-personal-meeting-room-options) API.
- `supportCoHost` (boolean) (**requerido**): Flag allowing other invitees to host a meeting in the Personal Room without the owner. This attribute can be modified with the [Update Personal Meeting Room Options](/docs/api/v1/meeting-preferences/update-personal-meeting-room-options) API.
- `supportAnyoneAsCoHost` (boolean): Whether or not to allow any attendee with a host account on the target site to become a cohost when joining the Personal Room. The target site is user's preferred site. This attribute can be modified with the [Update Personal Meeting Room Options](/docs/api/v1/meeting-preferences/update-personal-meeting-room-options) API.
- `allowFirstUserToBeCoHost` (boolean): Whether or not to allow the first attendee with a host account on the target site to become a cohost when joining the Personal Room. The target site is user's preferred site. This attribute can be modified with the [Update Personal Meeting Room Options](/docs/api/v1/meeting-preferences/update-personal-meeting-room-options) API.
- `allowAuthenticatedDevices` (boolean): Whether or not to allow authenticated video devices in the user's organization to start or join the meeting without a prompt. This attribute can be modified with the [Update Personal Meeting Room Options](/docs/api/v1/meeting-preferences/update-personal-meeting-room-options) API.
- `coHosts` (array): Array defining cohosts for the room if both `supportAnyoneAsCoHost` and `allowFirstUserToBeCoHost` are `false`. This attribute can be modified with the [Update Personal Meeting Room Options](/docs/api/v1/meeting-preferences/update-personal-meeting-room-options) API.
  - `email` (string) (**requerido**): Email address for cohost. This attribute can be modified with the [Update Personal Meeting Room Options](/docs/api/v1/meeting-preferences/update-personal-meeting-room-options) API.
  - `displayName` (string) (**requerido**): Display name for cohost. This attribute can be modified with the [Update Personal Meeting Room Options](/docs/api/v1/meeting-preferences/update-personal-meeting-room-options) API.
- `sipAddress` (string) (**requerido**): SIP address for callback from a video system.
- `dialInIpAddress` (string) (**requerido**): IP address for callback from a video system.
- `telephony` (object) (**requerido**): Information for callbacks from meeting to phone or for joining a teleconference using a phone.
  - `accessCode` (string) (**requerido**): Code for authenticating a user to join teleconference. Users join the teleconference using the call-in number or the global call-in number, followed by the value of the `accessCode`.
  - `callInNumbers` (array) (**requerido**): Array of call-in numbers for joining teleconference from a phone.
    - `label` (string) (**requerido**): Label for call-in number.
    - `callInNumber` (string) (**requerido**): Call-in number to join teleconference from a phone.
    - `tollType` (string) (**requerido**): Type of toll for the call-in number. Valores: toll, tollFree.
  - `links` (object): [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS) information of global call-in numbers for joining teleconference from a phone.
    - `rel` (string) (**requerido**): Link relation describing how the target resource is related to the current context (conforming with [RFC5998](https://tools.ietf.org/html/rfc5988)).
    - `href` (string) (**requerido**): Target resource URI (conforming with [RFC5998](https://tools.ietf.org/html/rfc5988)).
    - `method` (string) (**requerido**): Target resource method (conforming with [RFC5998](https://tools.ietf.org/html/rfc5988)).

### Ejemplo — respuesta 200
```json
{
  "topic": "John's PMR",
  "hostPin": "4325",
  "enabledAutoLock": false,
  "autoLockMinutes": 10,
  "enabledNotifyHost": true,
  "supportCoHost": true,
  "supportAnyoneAsCoHost": false,
  "allowFirstUserToBeCoHost": false,
  "allowAuthenticatedDevices": false,
  "coHosts": [
    {
      "email": "john.andersen@example.com",
      "displayName": "John Andersen"
    }
  ],
  "personalMeetingRoomLink": "https://site4-example.webex.com/meet/john",
  "sipAddress": "john.andersen@example.com",
  "dialInIpAddress": "192.168.100.100",
  "telephony": {
    "accessCode": "1234567890",
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
        "href": "/v1/meetings/0fc6ec1109e0d9b6c94e1f6caccda976/globalCallinNumbers",
        "method": "GET"
      }
    ]
  }
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden
  Ejemplo:
```json
{
  "message": "Not permitted to view or change other user's preferences",
  "errors": [
    {
      "description": "Not permitted to view or change other user's preferences"
    }
  ],
  "trackingId": "C385085C959545C8813E51803297E132_1562293603899"
}
```
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