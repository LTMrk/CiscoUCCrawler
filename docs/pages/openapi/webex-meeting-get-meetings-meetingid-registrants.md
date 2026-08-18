---
doc_id: webex-meeting-get-meetings-meetingid-registrants
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /meetings/{meetingId}/registrants
operation_id: listMeetingRegistrants
tags: Meetings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.485549+00:00
---

# GET /meetings/{meetingId}/registrants

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `listMeetingRegistrants`

## Resumen
List Meeting Registrants

## Descripción
Meeting's host and cohost can retrieve the list of registrants for a meeting with a specified meeting Id.

## Parámetros
- `meetingId` [path] (string) (**requerido**): Unique identifier for the meeting. Only the ID of the meeting series is supported for meetingId. IDs of scheduled meetings, meeting instances, or scheduled personal room meetings are not supported. See the [Meetings Overview](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) for more information about meeting types.
- `max` [query] (number): Limit the maximum number of registrants in the response, up to 100. The default is 10.
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes. If set, the admin may specify the email of a user in a site they manage and the API will return details for a meeting that is hosted by that user.
- `current` [query] (boolean): Whether or not to retrieve only the current scheduled meeting of the meeting series, i.e. the meeting ready to join or start or the upcoming meeting of the meeting series. If it's `true`, return details for the current scheduled meeting of the series, i.e. the scheduled meeting ready to join or start or the upcoming scheduled meeting of the meeting series. If it's `false` or not specified, return details for the entire meeting series. This parameter only applies to meeting series. Por defecto: False.
- `email` [query] (string): Registrant's email to filter registrants.
- `registrationTimeFrom` [query] (string): The time registrants register a meeting starts from the specified date and time (inclusive) in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. If `registrationTimeFrom` is not specified, it equals `registrationTimeTo` minus 7 days.
- `registrationTimeTo` [query] (string): The time registrants register a meeting before the specified date and time (exclusive) in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. If `registrationTimeTo` is not specified, it equals `registrationTimeFrom` plus 7 days. The interval between `registrationTimeFrom` and `registrationTimeTo` must be within 90 days.

## Ejemplo de invocación
```bash
curl -X GET '/meetings/<meetingId>/registrants' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): Registrants array.
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
  - `sourceId` (string): Registrant's source id.The `sourceId` is from [Create Invitation Sources](/docs/api/v1/meetings/create-invitation-sources) API.
  - `registrationId` (string): Registrant's registration ID. Registrants have a special number to identify a registrations if it is webinar-enabled and enabled registration ID.

### Ejemplo — respuesta 200
```json
{
  "items": [
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
      ],
      "sourceId": "cisco",
      "registrationId": "566476"
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