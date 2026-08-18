---
doc_id: webex-meeting-get-meetings-meetingid-surveyresults
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /meetings/{meetingId}/surveyResults
operation_id: listSurveyResultsByMeetingId
tags: Meetings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.489808+00:00
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
- `meetingId` [path] (string) (**requerido**): Unique identifier for the meeting. Please note that only the meeting ID of a scheduled webinar is supported for this API.
- `meetingStartTimeFrom` [query] (string): Start date and time (inclusive) in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format for the meeting objects being requested. `meetingStartTimeFrom` cannot be after `meetingStartTimeTo`. This parameter will be ignored if `meetingId` is the unique identifier for the specific meeting instance. When `meetingId` is not the unique identifier for the specific meeting instance, the `meetingStartTimeFrom`, if not specified, equals `meetingStartTimeTo` minus `1` month; if `meetingStartTimeTo` is also not specified, the default value for `meetingStartTimeFrom` is `1` month before the current date and time.
- `meetingStartTimeTo` [query] (string): End date and time (exclusive) in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format for the meeting objects being requested. `meetingStartTimeTo` cannot be prior to `meetingStartTimeFrom`. This parameter will be ignored if `meetingId` is the unique identifier for the specific meeting instance. When `meetingId` is not the unique identifier for the specific meeting instance, if `meetingStartTimeFrom` is also not specified, the default value for `meetingStartTimeTo` is the current date and time;For example,if `meetingStartTimeFrom` is a month ago, the default value for `meetingStartTimeTo` is `1` month after `meetingStartTimeFrom`.Otherwise it is the current date and time.
- `max` [query] (number): Limit the maximum number of meetings in the response, up to 100. The default is 10.
- `timezone` [header] (string): e.g. UTC
- `hostEmail` [header] (string): e.g. john.andersen@example.com

## Ejemplo de invocación
```bash
curl -X GET '/meetings/<meetingId>/surveyResults' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): SurveyResult array
  - `id` (string) (**requerido**): Unique identifier for the survey result.
  - `surveyName` (string) (**requerido**): Name for the survey.
  - `meetingId` (string) (**requerido**): Unique identifier for the meeting.
  - `email` (string) (**requerido**): Email address of the user who submits the survey.
  - `displayName` (string) (**requerido**): Name of the user who submits the survey.
  - `createTime` (string) (**requerido**): The time when the user submits the survey.
  - `questions` (array) (**requerido**): User's answers for the questions
    - `id` (number) (**requerido**): Unique identifier for the question.
    - `question` (string) (**requerido**): Details for the question.
    - `type` (string) (**requerido**): Type for the question.  * `text` - Text input.  * `rating` - Rating.  * `checkbox` - Check box which requires `options`.  * `singleDropdown` - Drop down list box which requires `options`.  * `singleRadio` - Single radio button which requires `options`. Valores: text, rating, checkbox, singleDropdown, singleRadio.
    - `answers` (array): The user's answers for the question.
      - `optionId` (number) (**requerido**): Unique identifier for the question option. This attribute will be ingnored, if the value of `type` attribute is `text` or `rating`.
      - `answer` (string) (**requerido**): The user's answers for the question.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "01c98ac1-e741-4bc1-b92b-6eb42f66caea",
      "surveyName": "Webinar User Experience Survey",
      "meetingId": "870f51ff287b41be84648412901e0402",
      "email": "kingu1@example.com",
      "displayName": "kingu1",
      "createTime": "2022-07-06T14:13:06Z",
      "questions": [
        {
          "id": 3388057,
          "question": "First text question",
          "type": "text",
          "answers": [
            {
              "optionId": 1,
              "answer": "yes"
            }
          ]
        },
        {
          "id": 3388062,
          "question": "Second text question",
          "type": "text",
          "answers": [
            {
              "optionId": 1,
              "answer": "no"
            }
          ]
        },
        {
          "id": 3388067,
          "question": "like rating",
          "type": "rating",
          "answers": [
            {
              "optionId": 1,
              "answer": "4"
            }
          ]
        },
        {
          "id": 3388072,
          "question": "check box question",
          "type": "checkbox",
          "answers": [
            {
              "optionId": 2,
              "answer": "Answer 2"
            },
            {
              "optionId": 3,
              "answer": "Answer 3"
            },
            {
              "optionId": 4,
              "answer": "Answer 4"
            }
          ]
        },
        {
          "id": 3388077,
        
  ... (truncado)
```

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