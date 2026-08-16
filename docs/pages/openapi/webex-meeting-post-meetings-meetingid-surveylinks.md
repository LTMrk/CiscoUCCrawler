---
doc_id: webex-meeting-post-meetings-meetingid-surveylinks
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: POST
path: /meetings/{meetingId}/surveyLinks
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.399155+00:00
---

# POST /meetings/{meetingId}/surveyLinks

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `generateSurveyLink`

## Resumen
Get Meeting Survey Links

## Descripción
Get survey links of a meeting for different users.

#### Request Header

* `timezone`: Time zone for the `meetingStartTimeFrom` and `meetingStartTimeTo` parameters and defined in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default value is `UTC` if not specified.

## Parámetros
- `meetingId` [path] (string) **(requerido)**: Unique identifier for the meeting. Only applies to webinars. Meetings and personal room meetings are not supported.
- `timezone` [header] (string): e.g. UTC

## Cuerpo de la petición (application/json)
- `hostEmail` (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin on-behalf-of scopes. An admin can specify the email of the meeting host who is in a site he manages and the API returns post survey links on behalf of the meeting host.
- `meetingStartTimeFrom` (string): Start date and time (inclusive) in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format for the meeting objects being requested and conforms with the `timezone` in the request header if specified. `meetingStartTimeFrom` cannot be after `meetingStartTimeTo`. Only applies when `meetingId` is not an instance ID. The API generates survey links for the last instance of `meetingId` in the time range specified by `meetingStartTimeFrom` and `meetingStartTimeTo`. If not specified, `meetingStartTimeFrom` equals `meetingStartTimeTo` minus `1` month; if `meetingStartTimeTo` is also not specified, the default value for `meetingStartTimeFrom` is `1` month before the current date and time.
- `meetingStartTimeTo` (string): End date and time (exclusive) in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format for the meeting objects being requested and conforms with the `timezone` in the request header if specified. `meetingStartTimeTo` cannot be prior to `meetingStartTimeFrom`. Only applies when `meetingId` is not an instance ID. The API generates survey links for the last instance of `meetingId` in the time range specified by `meetingStartTimeFrom` and `meetingStartTimeTo`. If not specified, `meetingStartTimeTo` equals `meetingStartTimeFrom` plus `1` month; if `meetingStartTimeFrom` is also not specified, the default value for `meetingStartTimeTo` is the current date and time.
- `emails` (array): Participants' email list. The maximum size of `emails` is 100.

### Ejemplo de petición
```json
{
  "hostEmail": "john.andersen@example.com",
  "meetingStartTimeFrom": "2019-03-18T09:30:00Z",
  "meetingStartTimeTo": "2019-03-25T09:30:00Z",
  "emails": [
    "kingu1@example.com",
    "kingu2@example.com",
    "kingu3@example.com"
  ]
}
```

## Respuestas
- **200**: OK
  - `items` (array): Survey link array
    - `email` (string): Participant email.
    - `surveyLink` (string): Meeting survey Link for the participant.
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
