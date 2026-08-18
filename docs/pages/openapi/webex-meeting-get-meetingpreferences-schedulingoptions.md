---
doc_id: webex-meeting-get-meetingpreferences-schedulingoptions
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /meetingPreferences/schedulingOptions
operation_id: Get Scheduling Options
tags: Preferences
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.470331+00:00
---

# GET /meetingPreferences/schedulingOptions

**API:** Webex Meetings
**Área:** Preferences
**operationId:** `Get Scheduling Options`

## Resumen
Get Scheduling Options

## Descripción
Retrieves scheduling options for the authenticated user.

## Parámetros
- `userEmail` [query] (string): Email address for the user. This parameter is only used if the user or application calling the API has the [admin-level scopes](/docs/meetings#adminorganization-level-authentication-and-scopes). If set, the admin may specify the email of a user in a site they manage and the API will return details of the scheduling options for that user.
- `siteUrl` [query] (string): URL of the Webex site to query. For individual use, if `siteUrl` is not specified, the query will use the default site of the user. For admin use, if `siteUrl` is not specified, the query will use the default site for the admin's authorization token used to make the call. In the case where the user belongs to a site different than the admin’s default site, the admin can set the site to query using the `siteUrl` parameter. All available Webex sites and default site of a user can be retrieved from [/meetingPreferences/sites](/docs/api/v1/meeting-preferences/get-site-list).

## Ejemplo de invocación
```bash
curl -X GET '/meetingPreferences/schedulingOptions' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `enabledJoinBeforeHost` (boolean) (**requerido**): Flag to enable/disable ***Join Before Host***. The period during which invitees can join before the start time is defined by `autoLockMinutes`. This attribute can be modified with the [Update Scheduling Options](/docs/api/v1/meeting-preferences/update-scheduling-options) API. ***Note***: This feature is only effective if the site supports the ***Join Before Host*** feature. This attribute can be modified with the [Update Scheduling Options](/docs/api/v1/meeting-preferences/update-scheduling-options) API.
- `joinBeforeHostMinutes` (number) (**requerido**): Number of minutes before the start time that an invitee can join a meeting if `enabledJoinBeforeHost` is true. Valid options are 0, 5, 10 and 15. This attribute can be modified with the [Update Scheduling Options](/docs/api/v1/meeting-preferences/update-scheduling-options) API.
- `enabledAutoShareRecording` (boolean) (**requerido**): Flag to enable/disable the automatic sharing of the meeting recording with invitees when it is available. This attribute can be modified with the [Update Scheduling Options](/docs/api/v1/meeting-preferences/update-scheduling-options) API.
- `enabledWebexAssistantByDefault` (boolean): Flag to automatically enable Webex Assistant whenever you start a meeting. This attribute can be modified with the [Update Scheduling Options](/docs/api/v1/meeting-preferences/update-scheduling-options) API.
- `delegateEmails` (array): You can allow other hosts to schedule meetings on your behalf by entering their email addresses here. This attribute can be modified with the [Update Scheduling Options](/docs/api/v1/meeting-preferences/update-scheduling-options), [Insert Delegate Emails](/docs/api/v1/meeting-preferences/insert-delegate-emails), and [Update Scheduling Options](/docs/api/v1/meeting-preferences/delete-delegate-emails) APIs.

### Ejemplo — respuesta 200
```json
{
  "enabledJoinBeforeHost": false,
  "joinBeforeHostMinutes": 10,
  "enabledAutoShareRecording": false,
  "enabledWebexAssistantByDefault": false,
  "delegateEmails": [
    "marcus.hoffmann@example.com",
    "brenda.song@example.com"
  ]
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden
  Ejemplo:
```json
{
  "message": "The server understood the request, but refused to fulfill it because the access token is missing required scopes or the user is missing required roles or licenses.",
  "errors": [
    {
      "description": "Not permitted to view or change other user's preferences."
    }
  ],
  "trackingId": "4A78EB66D02E4C78B9955AA504ECFC3D_1572666592909"
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