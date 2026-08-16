---
doc_id: webex-meeting-get-meetings-polls
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /meetings/polls
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.387315+00:00
---

# GET /meetings/polls

**API:** Webex Meetings
**Área:** Meeting Polls
**operationId:** `List Meeting Polls`

## Resumen
List Meeting Polls

## Descripción
Lists all the polls and the poll questions in a meeting when ready.

* Only [meeting instances](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) in state `ended` or `inProgress` are supported for `meetingId`.

* No pagination for this API because we don't expect a large number of questions for each meeting.

<div><Callout type="info">Polls are available within 15 minutes following the meeting.</Callout></div>

## Parámetros
- `meetingId` [query] (string) **(requerido)**: A unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) to which the polls belong.

## Respuestas
- **200**: OK
  - `items` (array):
    - `id` (string): A unique identifier for the poll.
    - `meetingId` (string): A unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) to which the poll belongs.
    - `startTime` (string): The date and time the poll started in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
    - `endTime` (string): The date and time the poll ended in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
    - `timerDuration` (number): The length of time in the alarm box, in seconds.
    - `displayName` (string): The name of the poll coordinator.
    - `email` (string): The email of the poll coordinator.
    - `personId` (string): The ID of the polling coordinator.
    - `questions` (array): Poll's questions.
      - `id` (string): A unique identifier for the question.
      - `order` (string): The order of the question.
      - `title` (string): The question.
      - `type` (string): The type of the question.  * `single` - A single-answer question.  * `multiple` - A multiple-answer question.  * `short` - A text answer. Valores: single, multiple, short.
      - `options` (array): Question's options.
        - `order` (string): The order of the option.
        - `value` (string): The value of the option.
        - `isCorrect` (boolean): Whether or not the option is correct.
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
