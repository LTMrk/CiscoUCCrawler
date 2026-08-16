---
doc_id: webex-meeting-post-meetings-reassignhost
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: POST
path: /meetings/reassignHost
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.399647+00:00
---

# POST /meetings/reassignHost

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `reassignHost`

## Resumen
Reassign Meetings to a New Host

## Descripción
Reassigns a list of meetings to a new host by an admin user.

All the meetings of `meetingIds` should belong to the same site, which is the `siteUrl` in the request header, if specified, or the admin user's preferred site, if not specified. All available Webex sites and the preferred sites of a user can be retrieved by [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

If the user of `hostEmail` is not qualified to be a host of the target site, the API returns an error with the HTTP status code `403`. If all the meetings referenced by `meetingIds` have been reassigned the new host successfully, the API returns an empty response with the HTTP status code `204`. Otherwise, if all the meetings of `meetingIds` fail or some of them fail, the API returns a "Multi-Status" response with status code of `207`, and individual errors for each meeting in the response body.

If a meeting already has several ended meeting instances before it's assigned to a new host, the existing ended instances are accessible to the original host and not accessible to the new host, but the new meeting instances which happen after the reassignment are only accessible to the new host.

After the reassignment, the original host will receive an email of meeting cancellation. However, the meeting in the original host's calendar will not necessarily be removed because user's calendar, e.g. Outlook calendar, is not managed by the meeting system directly.

**Note**: Only IDs of meeting series are supported for the `meetingIds`. IDs of scheduled meetings, meeting instances, or scheduled personal room meetings are not supported. To learn more about different types of meetings, please refer to [Meeting Series, Scheduled Meetings, and Meeting Instances](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances).

There are several limitations when reassigning meetings:

* Users cannot assign an in-progress meeting.

* Users cannot assign a meeting to a user who is not a Webex user, or an attendee who does not have host privilege.

* Users cannot assign a meeting with calling/callback to a host user who does not have calling/callback privileges

* Users cannot assign a meeting with session type A to a host user who does not have session type A privileges.

* Users cannot assign an MC or Webinar to a new host who does not have an MC license or a Webinar license.

* Users cannot assign a TC/EC1.0/SC meeting, or a meeting that is created by on-behalf to a new host.

* Users can reassign hosts for meetings from third-party integrations, such as Outlook or Google. Note that this is not recommended because it may result in inconsistent data between both parties.

#### Request Header

* `siteUrl`: Optional request header parameter. All the meetings of `meetingIds` should belong to the site referenced by siteUrl if specified. Otherwise, the meetings should belong to the admin user's preferred sites. All available Webex sites and the preferred sites of a user can be retrieved by [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

## Parámetros
- `siteUrl` [header] (string): e.g. example.webex.com

## Cuerpo de la petición (application/json)
- `hostEmail` (string) **(requerido)**: Email address of the new meeting host.
- `meetingIds` (array) **(requerido)**: List of meeting series IDs to be reassigned the new host. The size is between 1 and 100. All the meetings of `meetingIds` should belong to the same site, which is the `siteUrl` in the request header, if specified, or the admin user's preferred site, if not specified. All available Webex sites and the preferred sites of a user can be retrieved by [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

### Ejemplo de petición
```json
{
  "hostEmail": "john.andersen@example.com",
  "meetingIds": [
    "870f51ff287b41be84648412901e0402",
    "1d824a4a205042eba9574e00b711b226",
    "41be84640b711b8414a4a205042ebba9"
  ]
}
```

## Respuestas
- **204**: No Content
- **207**: Multi-Status
  - `items` (array): Array of meeting reassignment results.
    - `meetingId` (string) **(requerido)**: Unique identifier for the meeting to be reassigned host.
    - `httpStatus` (string) **(requerido)**: HTTP status code for the meeting reassignment result.
    - `message` (string): General message for the host reassignment of `meetingId` if it fails.
    - `errors` (array): Detailed descriptions for the host reassignment of `meetingId` if it fails.
      - `description` (string) **(requerido)**: Detailed description for the host reassignment of `meetingId` if it fails.
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
