---
doc_id: webex-meeting-get-meetings-polls-pollid-questions-questionid-respondents
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /meetings/polls/{pollId}/questions/{questionId}/respondents
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.387623+00:00
---

# GET /meetings/polls/{pollId}/questions/{questionId}/respondents

**API:** Webex Meetings
**Área:** Meeting Polls
**operationId:** `List Respondents of a Question`

## Resumen
List Respondents of a Question

## Descripción
Lists the respondents to a specific questions in a poll.

* Only [meeting instances](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) in state `ended` or `inProgress` are supported for `meetingId`.

* Long result sets are split into [pages](/docs/basics#pagination).

<div><Callout type="info">The list of poll respondents are available within 15 minutes following the meeting.</Callout></div>

## Parámetros
- `pollId` [path] (string) **(requerido)**: A unique identifier for the poll to which the respondents belong.
- `questionId` [path] (string) **(requerido)**: A unique identifier for the question to which the respondents belong.
- `meetingId` [query] (string) **(requerido)**: A unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) to which the respondents belong.
- `max` [query] (number): Limit the maximum number of respondents in a specified question in the response, up to 100.

## Respuestas
- **200**: OK
  - `items` (array):
    - `displayName` (string): The name of the person who answers the question.
    - `email` (string): The email of the person who answers the question.
    - `answers` (array): An array of answers. Single answer or text questions contain only a single answer.
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
