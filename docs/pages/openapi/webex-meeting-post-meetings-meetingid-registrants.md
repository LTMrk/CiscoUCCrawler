---
doc_id: webex-meeting-post-meetings-meetingid-registrants
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: POST
path: /meetings/{meetingId}/registrants
operation_id: createRegistrant
tags: Meetings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.485298+00:00
---

# POST /meetings/{meetingId}/registrants

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `createRegistrant`

## Resumen
Register a Meeting Registrant

## Descripción
Register a new registrant for a meeting. When a meeting or webinar is created, this API can only be used if Registration is checked on the page or the registration attribute is specified through the [Create a Meeting](/docs/api/v1/meetings/create-a-meeting) API.

## Parámetros
- `meetingId` [path] (string) (**requerido**): Unique identifier for the meeting. Only the ID of the meeting series is supported for meetingId. IDs of scheduled meetings, meeting instances, or scheduled personal room meetings are not supported. See the [Meetings Overview](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) for more information about meeting types.
- `current` [query] (boolean): Whether or not to retrieve only the current scheduled meeting of the meeting series, i.e. the meeting ready to join or start or the upcoming meeting of the meeting series. If it's `true`, return details for the current scheduled meeting of the series, i.e. the scheduled meeting ready to join or start or the upcoming scheduled meeting of the meeting series. If it's `false` or not specified, return details for the entire meeting series. This parameter only applies to meeting series. Por defecto: False.
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes. If set, the admin may specify the email of a user in a site they manage and the API will return details for a meeting that is hosted by that user.

## Cuerpo de la petición (application/json)
- `firstName` (string) (**requerido**): The registrant's first name.
- `lastName` (string) (**requerido**): The registrant's last name. (Required)
- `email` (string) (**requerido**): The registrant's email.
- `sendEmail` (boolean): If `true` send email to the registrant. Default: `true`.
- `jobTitle` (string): The registrant's job title. Registration options define whether or not this is required.
- `companyName` (string): The registrant's company. Registration options define whether or not this is required.
- `address1` (string): The registrant's first address line. Registration options define whether or not this is required.
- `address2` (string): The registrant's second address line. Registration options define whether or not this is required.
- `city` (string): The registrant's city name. Registration options define whether or not this is required.
- `state` (string): The registrant's state. Registration options define whether or not this is required.
- `zipCode` (number): The registrant's postal code. Registration options define whether or not this is required.
- `countryRegion` (string): The America is not a country or a specific region. Registration options define whether or not this is required.
- `workPhone` (string): The registrant's work phone number. Registration options define whether or not this is required.
- `fax` (string): The registrant's FAX number. Registration options define whether or not this is required.
- `customizedQuestions` (array): The registrant's answers for customized questions. Registration options define whether or not this is required.
  - `questionId` (number) (**requerido**): Unique identifier for the customized questions retrieved from the registration form.
  - `answers` (array) (**requerido**): The answers for customized questions. If the question type is checkbox, more than one answer can be set.
    - `optionId` (number): Unique identifier for the option.
    - `answer` (string) (**requerido**): The content of the answer or the option for this question.

### Ejemplo — petición
```json
{
  "firstName": "Bob",
  "lastName": "Lee",
  "email": "bob@example.com",
  "sendEmail": true,
  "jobTitle": "manager",
  "companyName": "Cisco Systems, Inc.",
  "address1": "address1 string",
  "address2": "address2 string",
  "city": "New York",
  "state": "New York",
  "zipCode": 123456,
  "countryRegion": "United States",
  "workPhone": "+1 123456",
  "fax": "123456",
  "customizedQuestions": [
    {
      "questionId": 330087,
      "answers": [
        {
          "optionId": 1,
          "answer": "green"
        }
      ]
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X POST '/meetings/<meetingId>/registrants' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"firstName": "<firstName>", "lastName": "<lastName>", "email": "<email>"}'
```

## Respuestas correctas
**200**: OK
- `id` (string): New registrant's ID.
- `status` (string): New registrant's status.  * `approved` - Registrant has been approved.  * `pending` - Registrant is in a pending list waiting for host or cohost approval.  * `rejected` - Registrant has been rejected by the host or cohost. Valores: approved, pending, rejected.
- `firstName` (string): Registrant's first name.
- `lastName` (string): Registrant's last name.
- `email` (string): Registrant's email.
- `jobTitle` (string): Registrant's job title.
- `companyName` (string): Registrant's company.
- `address1` (string): Registrant's first address line.
- `address2` (string): Registrant's second address line.
- `city` (string): Registrant's city name.
- `state` (string): Registrant's state.
- `zipCode` (number): Registrant's postal code.
- `countryRegion` (string): Registrant's country or region.
- `workPhone` (string): Registrant's work phone number.
- `fax` (string): Registrant's FAX number.
- `registrationTime` (string): Registrant's registration time.
- `customizedQuestions` (array): Registrant's answers for customized questions, Registration options define whether or not this is required.
  - `questionId` (number) (**requerido**): Unique identifier for the customized questions retrieved from the registration form.
  - `answers` (array) (**requerido**): The answers for customized questions. If the question type is checkbox, more than one answer can be set.
    - `optionId` (number): Unique identifier for the option.
    - `answer` (string) (**requerido**): The content of the answer or the option for this question.

### Ejemplo — respuesta 200
```json
{
  "id": "fbd83190-97b2-4bb0-b56b-8fde463d137b",
  "status": "pending",
  "firstName": "bob",
  "lastName": "Lee",
  "email": "bob@example.com",
  "jobTitle": "manager",
  "companyName": "cisco",
  "address1": "address1 string",
  "address2": "address2 string",
  "city": "New York",
  "state": "New York",
  "zipCode": 123456,
  "countryRegion": "United States",
  "workPhone": "+1 123456",
  "fax": "123456",
  "registrationTime": "2021-09-07T09:29:13+08:00",
  "registrationId": "566476",
  "customizedQuestions": [
    {
      "questionId": 330087,
      "answers": [
        {
          "optionId": 1,
          "answer": "green"
        }
      ]
    }
  ]
}
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