---
doc_id: webex-meeting-get-meetings-meetingid-surveyresults
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /meetings/{meetingId}/surveyResults
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.399032+00:00
---

# GET /meetings/{meetingId}/surveyResults

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `listSurveyResultsByMeetingId`

## Resumen
List Meeting Survey Results

## Descripción
Retrieves results for a meeting survey identified by `meetingId`.

#### Request Header

* `timezone`: Time zone for time stamps in response body, defined in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default value is `UTC` if not specified.

* `hostEmail`: Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin on-behalf-of scopes. If set, the admin may specify the email of a user in a site they manage and the API will return the survey results of that user.

## Parámetros
- `meetingId` [path] (string) **(requerido)**: Unique identifier for the meeting. Please note that only the meeting ID of a scheduled webinar is supported for this API.
- `meetingStartTimeFrom` [query] (string): Start date and time (inclusive) in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format for the meeting objects being requested. `meetingStartTimeFrom` cannot be after `meetingStartTimeTo`. This parameter will be ignored if `meetingId` is the unique identifier for the specific meeting instance. When `meetingId` is not the unique identifier for the specific meeting instance, the `meetingStartTimeFrom`, if not specified, equals `meetingStartTimeTo` minus `1` month; if `meetingStartTimeTo` is also not specified, the default value for `meetingStartTimeFrom` is `1` month before the current date and time.
- `meetingStartTimeTo` [query] (string): End date and time (exclusive) in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format for the meeting objects being requested. `meetingStartTimeTo` cannot be prior to `meetingStartTimeFrom`. This parameter will be ignored if `meetingId` is the unique identifier for the specific meeting instance. When `meetingId` is not the unique identifier for the specific meeting instance, if `meetingStartTimeFrom` is also not specified, the default value for `meetingStartTimeTo` is the current date and time;For example,if `meetingStartTimeFrom` is a month ago, the default value for `meetingStartTimeTo` is `1` month after `meetingStartTimeFrom`.Otherwise it is the current date and time.
- `max` [query] (number): Limit the maximum number of meetings in the response, up to 100. The default is 10.
- `timezone` [header] (string): e.g. UTC
- `hostEmail` [header] (string): e.g. john.andersen@example.com

## Respuestas
- **200**: OK
  - `items` (array): SurveyResult array
    - `id` (string) **(requerido)**: Unique identifier for the survey result.
    - `surveyName` (string) **(requerido)**: Name for the survey.
    - `meetingId` (string) **(requerido)**: Unique identifier for the meeting.
    - `email` (string) **(requerido)**: Email address of the user who submits the survey.
    - `displayName` (string) **(requerido)**: Name of the user who submits the survey.
    - `createTime` (string) **(requerido)**: The time when the user submits the survey.
    - `questions` (array) **(requerido)**: User's answers for the questions
      - `id` (number) **(requerido)**: Unique identifier for the question.
      - `question` (string) **(requerido)**: Details for the question.
      - `type` (string) **(requerido)**: Type for the question.  * `text` - Text input.  * `rating` - Rating.  * `checkbox` - Check box which requires `options`.  * `singleDropdown` - Drop down list box which requires `options`.  * `singleRadio` - Single radio button which requires `options`. Valores: text, rating, checkbox, singleDropdown, singleRadio.
      - `answers` (array): The user's answers for the question.
        - `optionId` (number) **(requerido)**: Unique identifier for the question option. This attribute will be ingnored, if the value of `type` attribute is `text` or `rating`.
        - `answer` (string) **(requerido)**: The user's answers for the question.
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
