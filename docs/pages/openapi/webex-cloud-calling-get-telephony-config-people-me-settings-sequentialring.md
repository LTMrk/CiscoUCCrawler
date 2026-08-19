---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-sequentialring
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/settings/sequentialRing
operation_id: getMySequentialRingSettings
tags: Call Settings For Me With UserHub Phase3
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.975700+00:00
---

# GET /telephony/config/people/me/settings/sequentialRing

**API:** Webex Cloud Calling
**Área:** Call Settings For Me With UserHub Phase3
**operationId:** `getMySequentialRingSettings`

## Resumen
Get Sequential Ring Settings for User

## Descripción
Get Sequential Ring Settings for the authenticated user.

Sequential Ring allows calls to ring additional phone numbers in sequence if the initial call is not answered. This can be configured to ring up to five phone numbers with customizable ring patterns.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/settings/sequentialRing' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Sequential Ring Settings retrieved for the authenticated user.
- `enabled` (boolean) (**requerido**): `true` if the sequential ring feature is enabled.
- `ringBaseLocationFirstEnabled` (boolean): When `true`, the user's own devices ring before sequential ring numbers.
- `baseLocationNumberOfRings` (integer): Number of rings for the user's own devices. Minimum: 2, Maximum: 20.
- `continueIfBaseLocationIsBusyEnabled` (boolean): When `true`, sequential ring continues even when the user is unavailable. It controls if we allow trying the sequential ring numbers when either a service for the user such as Do Not Disturb or Call Waiting sends the call to busy processing, or ringBaseLocationFirstEnabled is true but all the user's devices are unreachable.
- `callsToVoicemailEnabled` (boolean): When `true`, the caller is provided the option to press the # key to end the sequential ring service and send the call to no answer handling such as voicemail.
- `phoneNumbers` (array): List of phone numbers to ring sequentially.
  - `phoneNumber` (string): Phone number set as the sequential number.
  - `answerConfirmationRequiredEnabled` (boolean) (**requerido**): When set to `true` the called party is required to press 1 on the keypad to receive the call.
  - `numberOfRings` (number) (**requerido**): The number of rings to the specified phone number before the call advances to the subsequent number in the sequence or goes to voicemail.
- `criteria` (array): List of criteria specifying conditions when sequential ring is in effect.
  - `id` (string) (**requerido**): Unique identifier for criteria.
  - `scheduleName` (string) (**requerido**): Name of the schedule which determines when sequential ring is in effect.
  - `source` (string) (**requerido**): Type of the source.  * `ALL_NUMBERS` - sequential ring applies to calls from any phone number.  * `SPECIFIC_NUMBERS` - sequential ring applies to calls from specific phone numbers. Valores: ALL_NUMBERS, SPECIFIC_NUMBERS.
  - `ringEnabled` (boolean) (**requerido**): Determines whether sequential ring is applied for calls matching this criteria. If `true`, sequential ring is applied. If `false`, this criteria acts as a 'Don't Ring' rule. Criteria with ringEnabled set to false have precedence over criteria with ringEnabled set to true.

### Ejemplo — respuesta 200
```json
{
  "enabled": true,
  "ringBaseLocationFirstEnabled": false,
  "baseLocationNumberOfRings": 3,
  "continueIfBaseLocationIsBusyEnabled": true,
  "callsToVoicemailEnabled": false,
  "phoneNumbers": [
    {
      "phoneNumber": "+19075552859",
      "answerConfirmationRequiredEnabled": false,
      "numberOfRings": 3
    }
  ],
  "criteria": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0NSSVRFUklBL1oxNzU0MzgzODQzNTA5NzY",
      "scheduleName": "BusinessHours",
      "source": "ALL_NUMBERS",
      "ringEnabled": true
    }
  ]
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served.
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
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs