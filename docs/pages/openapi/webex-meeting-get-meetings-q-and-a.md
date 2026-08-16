---
doc_id: webex-meeting-get-meetings-q-and-a
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /meetings/q_and_a
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.389662+00:00
---

# GET /meetings/q_and_a

**API:** Webex Meetings
**Área:** Meeting Q and A
**operationId:** `List Meeting Q and A`

## Resumen
List Meeting Q and A

## Descripción
Lists questions and answers from a meeting, when ready.

Notes:

* Only [meeting instances](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) in state `ended` or `inProgress` are supported for `meetingId`.

* Long result sets will be split into [pages](/docs/basics#pagination).

* This API is paginated by the sum of answers in a meeting, These pagination links are returned in the response header.

## Parámetros
- `meetingId` [query] (string) **(requerido)**: A unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) which the Q&A belongs to.
- `max` [query] (number): Limits the maximum number of answers in the response, up to 100.

## Respuestas
- **200**: OK
  - `items` (array): An array of Q&A objects.
    - `id` (string): A unique identifier for the question.
    - `meetingId` (string): A unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) to which the Q&A belongs.
    - `totalAttendees` (number): The total number of attendees in the meeting.
    - `totalRespondents` (number): The total number of respondents in the meeting.
    - `displayName` (string): The name of the user who asked the question.
    - `email` (string): The email of the user who asked the question.
    - `question` (string): The question that was asked.
    - `answers` (object): Question's answers.
      - `links` (object): The pagination links of the question's answers.
        - `prev` (string): Link to the previous page of answers to this question.
        - `self` (string): Link to the current page of this answers to this question.
        - `next` (string): Link to the next page of answers to this question.
      - `items` (array): An array of answer objects for this question.
        - `displayName` (string): The name of the person who answered the question.
        - `email` (string): The email of the person who answered the question.
        - `personId` (string): The ID of the person who answered the question. Only present for authenticated users.
        - `answer` (array): The content of the answer.
        - `answered` (boolean): Whether or not the question was answered.
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed
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
