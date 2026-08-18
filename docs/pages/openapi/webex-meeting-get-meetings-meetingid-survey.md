---
doc_id: webex-meeting-get-meetings-meetingid-survey
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /meetings/{meetingId}/survey
operation_id: getSurveyByMeetingId
tags: Meetings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.489510+00:00
---

# GET /meetings/{meetingId}/survey

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `getSurveyByMeetingId`

## Resumen
Get a Meeting Survey

## Descripción
Retrieves details for a meeting survey identified by `meetingId`.

#### Request Header

* `hostEmail`: Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin on-behalf-of scopes. If set, the admin may specify the email of a user in a site they manage and the API will return survey details of that user.

## Parámetros
- `meetingId` [path] (string) (**requerido**): Unique identifier for the meeting. Please note that only the meeting ID of a scheduled webinar is supported for this API.
- `hostEmail` [header] (string): e.g. john.andersen@example.com

## Ejemplo de invocación
```bash
curl -X GET '/meetings/<meetingId>/survey' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Unique identifier for the survey.
- `surveyName` (string) (**requerido**): Name for the survey.
- `meetingId` (string) (**requerido**): Unique identifier for the meeting.
- `description` (string): Description for the survey.
- `allowAnonymousSubmit` (boolean): Whether the survey allows attendees to submit anonymously.
- `questions` (array) (**requerido**): Questions for the survey.
  - `id` (number) (**requerido**): Unique identifier for the question.
  - `question` (string) (**requerido**): Details for the question.
  - `type` (string) (**requerido**): Type for the question.  * `text` - Text input.  * `rating` - Rating.  * `checkbox` - Check box which requires `options`.  * `singleDropdown` - Drop down list box which requires `options`.  * `singleRadio` - Single radio button which requires `options`. Valores: text, rating, checkbox, singleDropdown, singleRadio.
  - `fromScore` (number): The lowest score of the rating question. This attribute will be ingnored, if the value of `type` attribute is not `rating`.
  - `fromLabel` (string): The lowest score label of the rating question. This attribute will be ingnored, if the value of `type` attribute is not `rating`.
  - `toScore` (number): The highest score of the rating question. This attribute will be ingnored, if the value of `type` attribute is not `rating`.
  - `toLabel` (string): The highest score label of the rating question. This attribute will be ingnored, if the value of `type` attribute is not `rating`.
  - `options` (array): Options for the question. This attribute will be ingnored, if the value of `type` attribute is `text` or `rating`.
    - `id` (number) (**requerido**): Unique identifier for the question option.
    - `value` (string) (**requerido**): Value for the question option.

### Ejemplo — respuesta 200
```json
{
  "id": "f2d58ef6cc5848c9a0fb41e3b7aa0ed3",
  "surveyName": "Webinar User Experience Survey",
  "meetingId": "fe32230212b7421286a1f300572a6517",
  "description": "A survey about user experience with webinars",
  "allowAnonymousSubmit": false,
  "questions": [
    {
      "id": 3388057,
      "question": "First text question",
      "required": true,
      "type": "text"
    },
    {
      "id": 3388062,
      "question": "Second text question",
      "required": true,
      "type": "text"
    },
    {
      "id": 3388067,
      "question": "like rating",
      "required": true,
      "type": "rating",
      "fromScore": 1,
      "fromLabel": "Not Likely",
      "toScore": 5,
      "toLabel": "Very Likely"
    },
    {
      "id": 3388072,
      "question": "check box question",
      "required": false,
      "type": "checkbox",
      "options": [
        {
          "id": 1,
          "value": "Answer 1"
        },
        {
          "id": 2,
          "value": "Answer 2"
        },
        {
          "id": 3,
          "value": "Answer 3"
        },
        {
          "id": 4,
          "value": "Answer 4"
        }
      ]
    },
    {
      "id": 3388077,
      "question": "dropdown list question",
      "required": false,
      "type": "singleDropdown",
      "options": [
        {
          "id": 1,
          "value": "Answer 1"
        },
        {
          "id": 2,
          "value": "Answer 2"
        },
        {
          "id": 3,
          "value": "Answer 3"
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