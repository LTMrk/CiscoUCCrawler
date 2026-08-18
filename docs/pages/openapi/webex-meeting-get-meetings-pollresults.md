---
doc_id: webex-meeting-get-meetings-pollresults
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /meetings/pollResults
operation_id: Get Meeting PollResults
tags: Meeting Polls
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.468176+00:00
---

# GET /meetings/pollResults

**API:** Webex Meetings
**Área:** Meeting Polls
**operationId:** `Get Meeting PollResults`

## Resumen
Get Meeting PollResults

## Descripción
List the meeting polls, the poll's questions, and answers from the meeting when ready.

* Only [meeting instances](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) in state `ended` or `inProgress` are supported for `meetingId`.

* Long result sets will be split into [pages](/docs/basics#pagination).

* This API is paginated by the sum of respondents from all questions in a meeting, these pagination links are returned in the response header.

<div><Callout type="info">Polls results are available within 15 minutes following the meeting.</Callout></div>

## Parámetros
- `meetingId` [query] (string) (**requerido**): A unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) to which the polls belong.
- `max` [query] (number): Limit the maximum number of respondents in a meeting in the response, up to 100. Por defecto: 10.

## Ejemplo de invocación
```bash
curl -X GET '/meetings/pollResults?meetingId=<meetingId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array):
  - `id` (string): A unique identifier for the poll.
  - `meetingId` (string): A unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) to which the poll belongs.
  - `totalAttendees` (number): The total number of attendees in the meeting.
  - `totalRespondents` (number): The total number of respondents in the poll.
  - `startTime` (string): The date and time the poll started in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
  - `endTime` (string): The date and time the poll ended in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
  - `timerDuration` (number): The duration of the poll, in seconds.
  - `displayName` (string): The name of the poll coordinator.
  - `email` (string): The email of the poll coordinator.
  - `personId` (string): The ID of the the poll coordinator.
  - `questions` (array): An array of questions in this poll.
    - `id` (string): A unique identifier of the question.
    - `order` (string): The order of the question in the poll.
    - `title` (string): The question.
    - `type` (string): The type of the question.  * `single` - A single-answer question.  * `multiple` - A multiple-answer question.  * `short` - A text answer. Valores: single, multiple, short.
    - `answerSummary` (array): Summary of all answers.
      - `order` (string): The order of the answer in the question.
      - `value` (string): The content of the answer.
      - `totalRespondents` (number): The total number of people who selected this answer.
      - `isCorrect` (boolean): Whether the answer is correct.
    - `respondents` (object):
      - `links` (object):
        - `prev` (string): Link to the previous question's respondents.
        - `self` (string): Link to the current question's respondents.
        - `next` (string): Link to the next page question's respondents.
      - `items` (array): An array of answers.
        - `displayName` (string): The name of the person who answers the question.
        - `email` (string): The email of the person who answers the question.
        - `answers` (array): An array of answers. Single answer or text questions contain only a single answer.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "1aea8390-e375-4547-b7ff-58ecd9e0b03d",
      "meetingId": "a2f95f5073e347489f7611492dbd6ad5_I_199075330905867928",
      "totalAttendees": 10,
      "totalRespondents": 10,
      "startTime": "2021-07-06T09:25:34Z",
      "endTime": "2021-07-06T09:28:34Z",
      "timerDuration": 300,
      "displayName": "John Andersen",
      "email": "john.andersen@example.com",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xYTY5MmE2Mi00MTNmLTRjYWEtYjdkOS0wYzg0ZDZmMDdlNzY",
      "questions": [
        {
          "id": "6f31147e-dd69-4ea9-8b75-2c5834b72ba2",
          "order": "1",
          "title": "What colors do you like?",
          "type": "single",
          "answerSummary": [
            {
              "order": "1",
              "value": "China",
              "totalRespondents": 10,
              "isCorrect": true
            }
          ],
          "respondents": {
            "links": {
              "prev": "https://webexapis.com/v1/meetings/polls/1d4959fe-682e-4107-a346-0e1feac7b899_M_7b789da198e531ce0c4d84243abd9fee_I_231245894851233679/questions/6f31147e-dd69-4ea9-8b75-2c5834b72ba2/respondents?meetingId=7b789da198e531ce0c4d84243abd9fee_I_231245894851233679&offset=0&max=5",
              "self": "https://webexapis.com/v1/meetings/polls/1d4959fe-682e-4107-a346-0e1feac7b899_M_7b789da198e531ce0c4d84243abd9fee_I_231245894851233679/questions/6f31147e-dd69-4ea9-8b75-2c5834b72ba2/respondents?meetingId=7b789da198e531ce0c4d84243abd9fee_I_231245
  ... (truncado)
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