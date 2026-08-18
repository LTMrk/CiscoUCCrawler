---
doc_id: webex-meeting-get-meetingreports-usage
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /meetingReports/usage
operation_id: List Meeting Usage Reports
tags: Meetings Summary Report
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.475670+00:00
---

# GET /meetingReports/usage

**API:** Webex Meetings
**Área:** Meetings Summary Report
**operationId:** `List Meeting Usage Reports`

## Resumen
List Meeting Usage Reports

## Descripción
List meeting usage reports of all the users on the specified site by an admin. You can specify a date range and the maximum number of meeting usage reports to return.

The list returned is sorted in descending order by the date and time the meetings were started.

Long result sets are split into [pages](/docs/basics#pagination).

* `siteUrl` is required, and the meeting usage reports of the specified site are listed. All available Webex sites can be retrieved by the [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

#### Request Header

* `timezone`: [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default timezone is `UTC` if not defined.

## Parámetros
- `siteUrl` [query] (string) (**requerido**): URL of the Webex site which the API lists meeting usage reports from. All available Webex sites can be retrieved by the [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.
- `serviceType` [query] (string): Meeting usage report's service-type. If `serviceType` is specified, the API filters meeting usage reports by service-type. If `serviceType` is not specified, the API returns meeting usage reports by `MeetingCenter` by default. Valid values:  + `MeetingCenter`  + `EventCenter`  + `SupportCenter`  + `TrainingCenter`
- `from` [query] (string): Starting date and time for meeting usage reports to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `from` cannot be after `to`. The interval between `to` and `from` cannot exceed 30 days and `from` cannot be earlier than 90 days ago. Por defecto: If `to` is specified, the default value is 7 days before `to`; if `to` is not specified, the default value is 7 days before the current date and time..
- `to` [query] (string): Ending date and time for meeting usage reports to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `to` cannot be before `from`. The interval between `to` and `from` cannot exceed 30 days. Por defecto: If `from` is specified, the default value is 7 days after `from`; if `from` is not specified, the default value is the current date and time..
- `max` [query] (number): Maximum number of meetings to include in the meetings usage report in a single page. `max` must be greater than 0 and equal to or less than `1000`. Por defecto: 10.
- `timezone` [header] (string): e.g. Asia/Shanghai

## Ejemplo de invocación
```bash
curl -X GET '/meetingReports/usage?siteUrl=<siteUrl>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): An array of meeting usage report objects.
  - `meetingId` (string): Unique identifier for the meeting.
  - `meetingNumber` (string): Meeting number.
  - `meetingTitle` (string): Meeting title.
  - `start` (string): The date and time when the meeting was started. It's in the timezone specified in the request header or in the `UTC` timezone if timezone is not specified.
  - `end` (string): The date and time when the meeting was ended. It's in the timezone specified in the request header or in the `UTC` timezone if timezone is not specified.
  - `duration` (number): Duration of the meeting in minutes.
  - `scheduledType` (string): Scheduled type for the meeting.  * `meeting` - Regular meeting.  * `webinar` - Webinar meeting. Valores: meeting, webinar.
  - `hostDisplayName` (string): Display name for the meeting host.
  - `hostEmail` (string): Email address for the meeting host.
  - `totalPeopleMinutes` (number): Aggregated attendee minutes.
  - `totalCallInMinutes` (number): Aggregated attendee PSTN call-in minutes.
  - `totalCallOutDomestic` (number): Aggregated attendee domestic PSTN call-out minutes.
  - `totalCallInTollFreeMinutes` (number): Aggregated attendee toll-free PSTN call-in minutes.
  - `totalCallOutInternational` (number): Aggregated attendee international PSTN call-out minutes.
  - `totalVoipMinutes` (number): Aggregated attendee VoIP minutes.
  - `totalParticipants` (number): Total number of participants of the meeting.
  - `totalParticipantsVoip` (number): Total number of VoIP participants of the meeting.
  - `totalParticipantsCallIn` (number): Total number of PSTN call-in participants of the meeting.
  - `totalParticipantsCallOut` (number): Total number of PSTN call-out participants of the meeting.
  - `peakAttendee` (number): Peak number of attendees throughout the meeting.
  - `totalRegistered` (number): Total number of registrants of the meeting.
  - `totalInvitee` (number): Total number of invitees of the meeting.
  - `serviceType` (string): The service type for the meeting usage report.  * `MeetingCenter` - The service type for the usage report is meeting.  * `EventCenter` - The service type for the usage report is the event.  * `TrainingCenter` - The service type for the usage report is the training session.  * `SupportCenter` - The service type for the usage report is the support meeting. Valores: MeetingCenter, EventCenter, TrainingCenter, SupportCenter.
  - `trackingCodes` (array): Tracking codes of the meeting.
    - `name` (string): Name of the tracking code.
    - `value` (string): Value of the tracking code.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "meetingId": "089b137c3cf34b578896941e2d49dfe8_I_146987372776523573",
      "meetingNumber": "123456789",
      "meetingTitle": "John's Meeting",
      "start": "2023-01-18T10:26:30+08:00",
      "end": "2023-01-18T10:46:30+08:00",
      "duration": 20,
      "scheduledType": "meeting",
      "hostDisplayName": "John Andersen",
      "hostEmail": "john.andersen@example.com",
      "totalPeopleMinutes": 60,
      "totalCallInMinutes": 60,
      "totalCallOutDomestic": 60,
      "totalCallInTollFreeMinutes": 60,
      "totalCallOutInternational": 60,
      "totalVoipMinutes": 60,
      "totalParticipants": 30,
      "totalParticipantsVoip": 10,
      "totalParticipantsCallIn": 10,
      "totalParticipantsCallOut": 10,
      "peakAttendee": 30,
      "totalRegistered": 30,
      "totalInvitee": 30,
      "serviceType": "MeetingCenter",
      "trackingCodes": [
        {
          "name": "Department",
          "value": "Engineering"
        },
        {
          "name": "Division",
          "value": "Web"
        }
      ]
    }
  ]
}
```
- Cabecera `Link`: 

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