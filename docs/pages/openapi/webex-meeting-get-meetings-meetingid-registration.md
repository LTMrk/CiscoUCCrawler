---
doc_id: webex-meeting-get-meetings-meetingid-registration
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /meetings/{meetingId}/registration
operation_id: getMeetingRegistration
tags: Meetings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.484357+00:00
---

# GET /meetings/{meetingId}/registration

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `getMeetingRegistration`

## Resumen
Get registration form for a meeting

## Descripción
Get a meeting's registration form to understand which fields are required.

## Parámetros
- `meetingId` [path] (string) (**requerido**): Unique identifier for the meeting. Only the ID of the meeting series is supported for meetingId. IDs of scheduled meetings, meeting instances, or scheduled personal room meetings are not supported. See the [Meetings Overview](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) for more information about meeting types.
- `current` [query] (boolean): Whether or not to retrieve only the current scheduled meeting of the meeting series, i.e. the meeting ready to join or start or the upcoming meeting of the meeting series. If it's `true`, return details for the current scheduled meeting of the series, i.e. the scheduled meeting ready to join or start or the upcoming scheduled meeting of the meeting series. If it's `false` or not specified, return details for the entire meeting series. This parameter only applies to meeting series. Por defecto: False.
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes. If set, the admin may specify the email of a user in a site they manage and the API will return details for a meeting that is hosted by that user.

## Ejemplo de invocación
```bash
curl -X GET '/meetings/<meetingId>/registration' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `autoAcceptRequest` (boolean): Whether or not meeting registration requests are accepted automatically.
- `requireFirstName` (boolean): Whether or not a registrant's first name is required for meeting registration. This option must always be `true`.
- `requireLastName` (boolean): Whether or not a registrant's last name is required for meeting registration. This option must always be `true`.
- `requireEmail` (boolean): Whether or not a registrant's email is required for meeting registration. This option must always be `true`.
- `requireJobTitle` (boolean): Whether or not a registrant's job title is shown or required for meeting registration.
- `requireCompanyName` (boolean): Whether or not a registrant's company name is shown or required for meeting registration.
- `requireAddress1` (boolean): Whether or not a registrant's first address field is shown or required for meeting registration.
- `requireAddress2` (boolean): Whether or not a registrant's second address field is shown or required for meeting registration.
- `requireCity` (boolean): Whether or not a registrant's city is shown or required for meeting registration.
- `requireState` (boolean): Whether or not a registrant's state is shown or required for meeting registration.
- `requireZipCode` (boolean): Whether or not a registrant's postal code is shown or required for meeting registration.
- `requireCountryRegion` (boolean): Whether or not a registrant's country or region is shown or required for meeting registration.
- `requireWorkPhone` (boolean): Whether or not a registrant's work phone number is shown or required for meeting registration.
- `requireFax` (boolean): Whether or not a registrant's fax number is shown or required for meeting registration.
- `customizedQuestions` (array): Customized questions for meeting registration.
  - `id` (number) (**requerido**): Unique identifier for the question.
  - `question` (string) (**requerido**): Title of the customized question.
  - `required` (boolean): Whether or not the customized question is required to be answered by participants.
  - `type` (string) (**requerido**): Type of the question being asked.  * `singleLineTextBox` - Single line text box.  * `multiLineTextBox` - Multiple line text box.  * `checkbox` - Check box which requires `options`.  * `dropdownList` - Drop down list box which requires `options`.  * `radioButtons` - Single radio button which requires `options`. Valores: singleLineTextBox, multiLineTextBox, checkbox, dropdownList, radioButtons.
  - `maxLength` (number): The maximum length of a string that can be entered by the user, ranging from `0` to `999`. Only required by `singleLineTextBox` and `multiLineTextBox`.
  - `options` (array): TThe content of `options`. Required if the question type is one of `checkbox`, `dropdownList`, or `radioButtons`.
    - `id` (number) (**requerido**): The unique id of options.
    - `value` (string) (**requerido**): The content of the option.
  - `rules` (array): The automatic approval rules for customized questions.
    - `condition` (string) (**requerido**): Judgment expression for approval rules.  * `contains` - The content of the answer contains the value.  * `notContains` - The content of the answer does not contain the value  * `beginsWith` - The content of the answer begins with the value.  * `endsWith` - The content of the answer ends with the value.  * `equals` - The content of the answer is the same as the value.  * `notEquals` - The content of the answer is not the same as the value. Valores: contains, notContains, beginsWith, endsWith, equals, notEquals.
    - `value` (string) (**requerido**): The keyword for the approval rule. If the rule matches the keyword, the corresponding action will be executed.
    - `result` (string) (**requerido**): The automatic approval result for the approval rule.  * `approve` - If the user's registration value meets the criteria, the registration form will be automatically approved.  * `reject` - If the user's registration value meets the criteria, the registration form will be automatically rejected. Valores: approve, reject.
    - `matchCase` (boolean): Whether to check the case of values.
    - `order` (number) (**requerido**): The priority number of the approval rule. Approval rules for standard questions and custom questions need to be ordered together.
- `rules` (array): The approval rules for standard questions.
  - `question` (string) (**requerido**): Name for standard question.  * `lastName` - If the value is `lastName`, this approval rule applies to the standard question of "Last Name".  * `email` - If the value is `email`, this approval rule applies to the standard question of "Email".  * `jobTitle` - If the value is `jobTitle`, this approval rule applies to the standard question of "Job Title".  * `companyName` - If the value is `companyName`, this approval rule applies to the standard question of "Company Name".  * `address1` - If the value is `address1`, this approval rule applies to the standard question of "Address 1".  * `address2` - If the value is `address2`, this approval rule applies to the standard question of "Address 2".  * `city` - If the value is `city`, this approval rule applies to the standard question of "City".  * `state` - If the value is `state`, this approval rule applies to the standard question of "State".  * `zipCode` - If the value is `zipCode`, this approval rule applies to the standard question of "Zip/Post Code".  * `countryRegion` - If the value is `countryRegion`, this approval rule applies to the standard question of "Country Region".  * `workPhone` - If the value is `workPhone`, this approval rule applies to the standard question of "Work Phone".  * `fax` - If the value is `fax`, this approval rule applies to the standard question of "Fax". Valores: lastName, email, jobTitle, companyName, address1, address2, city, state, zipCode, countryRegion, workPhone, fax.
  - `condition` (string) (**requerido**): Judgment expression for approval rules.  * `contains` - The content of the answer contains the value.  * `notContains` - The content of the answer does not contain the value  * `beginsWith` - The content of the answer begins with the value.  * `endsWith` - The content of the answer ends with the value.  * `equals` - The content of the answer is the same as the value.  * `notEquals` - The content of the answer is not the same as the value. Valores: contains, notContains, beginsWith, endsWith, equals, notEquals.
  - `value` (string) (**requerido**): The keyword for the approval rule. If the rule matches the keyword, the corresponding action will be executed.
  - `result` (string) (**requerido**): The automatic approval result for the approval rule.  * `approve` - If the user's registration value meets the criteria, the registration form will be automatically approved.  * `reject` - If the user's registration value meets the criteria, the registration form will be automatically rejected. Valores: approve, reject.
  - `matchCase` (boolean): Whether to check the case of values.
  - `order` (number) (**requerido**): The priority number of the approval rule. Approval rules for standard questions and custom questions need to be ordered together.

### Ejemplo — respuesta 200
```json
{
  "autoAcceptRequest": false,
  "requireFirstName": true,
  "requireLastName": true,
  "requireEmail": true,
  "requireJobTitle": false,
  "requireCompanyName": false,
  "requireAddress1": false,
  "requireAddress2": false,
  "requireCity": false,
  "requireState": false,
  "requireZipCode": false,
  "requireCountryRegion": false,
  "requireWorkPhone": false,
  "requireFax": false,
  "enabledRegistrationId": false,
  "customizedQuestions": [
    {
      "id": "330521",
      "question": "How are you",
      "required": true,
      "type": "singleLineTextBox",
      "options": [
        {
          "id": "1",
          "value": "green"
        }
      ],
      "rules": [
        {
          "condition": "contains",
          "value": "tom",
          "result": "approve",
          "matchCase": true,
          "order": 1
        }
      ]
    }
  ],
  "rules": [
    {
      "question": "state",
      "condition": "contains",
      "value": "tom",
      "result": "approve",
      "matchCase": true,
      "order": 1
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