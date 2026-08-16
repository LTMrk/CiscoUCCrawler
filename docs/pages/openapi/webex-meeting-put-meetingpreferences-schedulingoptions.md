---
doc_id: webex-meeting-put-meetingpreferences-schedulingoptions
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: PUT
path: /meetingPreferences/schedulingOptions
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.388935+00:00
---

# PUT /meetingPreferences/schedulingOptions

**API:** Webex Meetings
**Área:** Preferences
**operationId:** `Update Scheduling Options`

## Resumen
Update Scheduling Options

## Descripción
Updates scheduling options for the authenticated user.

* If `delegateEmails` is null or not specified, the user's delegate emails are not changed. If `delegateEmails` is specified and not empty, the user's delegate emails are updated with the specified emails. If `delegateEmails` is specified as an empty array, the user's existing delegate emails are removed.

## Parámetros
- `userEmail` [query] (string): Email address for the user. This parameter is only used if the user or application calling the API has the [admin-level scopes](/docs/meetings#adminorganization-level-authentication-and-scopes). If set, the admin may specify the email of a user in a site they manage and the API will update scheduling options for that user.
- `siteUrl` [query] (string): URL of the Webex site to query. For individual use, if `siteUrl` is not specified, the query will use the default site of the user. For admin use, if `siteUrl` is not specified, the query will use the default site for the admin's authorization token used to make the call. In the case where the user belongs to a site different than the admin’s default site, the admin can set the site to query using the `siteUrl` parameter. All available Webex sites and default site of a user can be retrieved from [/meetingPreferences/sites](/docs/api/v1/meeting-preferences/get-site-list).

## Cuerpo de la petición (application/json)
- `enabledJoinBeforeHost` (boolean) **(requerido)**: Flag to enable/disable ***Join Before Host***. The period during which invitees can join before the start time is defined by `autoLockMinutes`. This attribute can be modified with the [Update Scheduling Options](/docs/api/v1/meeting-preferences/update-scheduling-options) API. ***Note***: This feature is only effective if the site supports the ***Join Before Host*** feature. This attribute can be modified with the [Update Scheduling Options](/docs/api/v1/meeting-preferences/update-scheduling-options) API.
- `joinBeforeHostMinutes` (number) **(requerido)**: Number of minutes before the start time that an invitee can join a meeting if `enabledJoinBeforeHost` is true. Valid options are 0, 5, 10 and 15. This attribute can be modified with the [Update Scheduling Options](/docs/api/v1/meeting-preferences/update-scheduling-options) API.
- `enabledAutoShareRecording` (boolean) **(requerido)**: Flag to enable/disable the automatic sharing of the meeting recording with invitees when it is available. This attribute can be modified with the [Update Scheduling Options](/docs/api/v1/meeting-preferences/update-scheduling-options) API.
- `enabledWebexAssistantByDefault` (boolean): Flag to automatically enable Webex Assistant whenever you start a meeting. This attribute can be modified with the [Update Scheduling Options](/docs/api/v1/meeting-preferences/update-scheduling-options) API.
- `delegateEmails` (array): You can allow other hosts to schedule meetings on your behalf by entering their email addresses here. This attribute can be modified with the [Update Scheduling Options](/docs/api/v1/meeting-preferences/update-scheduling-options), [Insert Delegate Emails](/docs/api/v1/meeting-preferences/insert-delegate-emails), and [Update Scheduling Options](/docs/api/v1/meeting-preferences/delete-delegate-emails) APIs.

### Ejemplo de petición
```json
{
  "enabledJoinBeforeHost": false,
  "joinBeforeHostMinutes": 0,
  "enabledAutoShareRecording": false,
  "enabledWebexAssistantByDefault": false,
  "delegateEmails": [
    "marcus.hoffmann@example.com, brenda.song@example.com"
  ]
}
```

## Respuestas
- **200**: OK
  - `enabledJoinBeforeHost` (boolean) **(requerido)**: Flag to enable/disable ***Join Before Host***. The period during which invitees can join before the start time is defined by `autoLockMinutes`. This attribute can be modified with the [Update Scheduling Options](/docs/api/v1/meeting-preferences/update-scheduling-options) API. ***Note***: This feature is only effective if the site supports the ***Join Before Host*** feature. This attribute can be modified with the [Update Scheduling Options](/docs/api/v1/meeting-preferences/update-scheduling-options) API.
  - `joinBeforeHostMinutes` (number) **(requerido)**: Number of minutes before the start time that an invitee can join a meeting if `enabledJoinBeforeHost` is true. Valid options are 0, 5, 10 and 15. This attribute can be modified with the [Update Scheduling Options](/docs/api/v1/meeting-preferences/update-scheduling-options) API.
  - `enabledAutoShareRecording` (boolean) **(requerido)**: Flag to enable/disable the automatic sharing of the meeting recording with invitees when it is available. This attribute can be modified with the [Update Scheduling Options](/docs/api/v1/meeting-preferences/update-scheduling-options) API.
  - `enabledWebexAssistantByDefault` (boolean): Flag to automatically enable Webex Assistant whenever you start a meeting. This attribute can be modified with the [Update Scheduling Options](/docs/api/v1/meeting-preferences/update-scheduling-options) API.
  - `delegateEmails` (array): You can allow other hosts to schedule meetings on your behalf by entering their email addresses here. This attribute can be modified with the [Update Scheduling Options](/docs/api/v1/meeting-preferences/update-scheduling-options), [Insert Delegate Emails](/docs/api/v1/meeting-preferences/insert-delegate-emails), and [Update Scheduling Options](/docs/api/v1/meeting-preferences/delete-delegate-emails) APIs.
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
