---
doc_id: webex-meeting-get-meetingreports-attendees
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /meetingReports/attendees
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.391636+00:00
---

# GET /meetingReports/attendees

**API:** Webex Meetings
**Área:** Meetings Summary Report
**operationId:** `List Meeting Attendee Reports`

## Resumen
List Meeting Attendee Reports

## Descripción
Lists of meeting attendee reports by a date range, the maximum number of meeting attendee reports, a meeting ID, a meeting number or a meeting title.

If the requesting user is an admin, the API returns meeting attendee reports of the meetings hosted by all the users on the specified site filtered by meeting ID, meeting number or meeting title.

If it's a normal meeting host, the API returns meeting attendee reports of the meetings hosted by the user himself on the specified site filtered by meeting ID, meeting number or meeting title.

The list returned is grouped by meeting instances. Both the groups and items of each group are sorted in descending order of `joinedTime`. For example, if `meetingId` is specified and it's a meeting series ID, the returned list is grouped by meeting instances of that series. The groups are sorted in descending order of `joinedTime`, and within each group the items are also sorted in descending order of `joinedTime`. Please refer to [Meetings Overview](/docs/meetings) for details of meeting series, scheduled meeting and meeting instance.

Long result sets are split into [pages](/docs/basics#pagination).

* `siteUrl` is required, and the meeting attendee reports of the specified site are listed. All available Webex sites can be retrieved by the [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

* `meetingId`, `meetingNumber` and `meetingTitle` are optional parameters to query the meeting attendee reports, but at least one of them should be specified. If more than one parameter in the sequence of `meetingId`, `meetingNumber`, and `meetingTitle` are specified, the first one in the sequence is used. Currently, only ended meeting instance IDs and meeting series IDs are supported for `meetingId`. IDs of scheduled meetings or personal room meetings are not supported.

#### Request Header

* `timezone`: [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default timezone is `UTC` if not defined.

## Parámetros
- `siteUrl` [query] (string) **(requerido)**: URL of the Webex site which the API lists meeting attendee reports from. All available Webex sites can be retrieved by the [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.
- `from` [query] (string): Starting date and time for the meeting attendee reports to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `from` cannot be after `to`. The interval between `to` and `from` cannot exceed 30 days and `from` cannot be earlier than 90 days ago.
- `to` [query] (string): Ending date and time for the meeting attendee reports to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `to` cannot be before `from`. The interval between `to` and `from` cannot exceed 30 days.
- `max` [query] (number): Maximum number of meeting attendees to include in the meeting attendee report in a single page. `max` must be greater than 0 and equal to or less than `1000`.
- `meetingId` [query] (string): Meeting ID for the meeting attendee reports to return. If specified, return meeting attendee reports of the specified meeting; otherwise, return meeting attendee reports of all meetings. Currently, only ended meeting instance IDs are supported. IDs of meeting series, scheduled meetings or personal room meetings are not supported.
- `meetingNumber` [query] (string): Meeting number for the meeting attendee reports to return. If specified, return meeting attendee reports of the specified meeting; otherwise, return meeting attendee reports of all meetings.
- `meetingTitle` [query] (string): Meeting title for the meeting attendee reports to return. If specified, return meeting attendee reports of the specified meeting; otherwise, return meeting attendee reports of all meetings.
- `timezone` [header] (string): e.g. Asia/Shanghai

## Respuestas
- **200**: OK
  - `items` (array): An array of meeting attendee report objects.
    - `meetingId` (string): Unique identifier for the meeting.
    - `meetingNumber` (number): Meeting number.
    - `meetingTitle` (string): Meeting title.
    - `displayName` (string): Attendee's display name.
    - `email` (string): Attendee's email.
    - `joinedTime` (string): The date and time when the attendee joined the meeting. It's in the timezone specified in the request header or in the `UTC` timezone if timezone is not specified.
    - `leftTime` (string): The date and time when the attendee left the meeting. It's in the timezone specified in the request header or in the `UTC` timezone if timezone is not specified.
    - `duration` (number): Duration of the attendee in the meeting in minutes.
    - `participantType` (string): The attendee's role in the meeting.  * `host` - Meeting host.  * `attendee` - Meeting attendee. Valores: host, attendee.
    - `ipAddress` (string): IP address of the attendee when he attended the meeting.
    - `clientAgent` (string): Information of the attendee's operating system and application when he attended the meeting.
    - `company` (string): Attendee's company.
    - `phoneNumber` (string): Attendee's phone number.
    - `address1` (string): Attendee's address, part one.
    - `address2` (string): Attendee's address, part two.
    - `city` (string): Attendee's city.
    - `state` (string): Attendee's state.
    - `country` (string): Attendee's country.
    - `zipCode` (string): Attendee's zip code.
    - `registered` (boolean): Whether or not the attendee has registered the meeting.
    - `invited` (boolean): Whether or not the attendee has been invited to the meeting.
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
