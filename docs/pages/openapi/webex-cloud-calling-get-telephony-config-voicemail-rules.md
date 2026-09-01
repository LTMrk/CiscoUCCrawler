---
doc_id: webex-cloud-calling-get-telephony-config-voicemail-rules
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/voicemail/rules
operation_id: Get Voicemail Rules
tags: Calling Service Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.606188+00:00
---

# GET /telephony/config/voicemail/rules

**API:** Webex Cloud Calling
**Área:** Calling Service Settings
**operationId:** `Get Voicemail Rules`

## Resumen
Get Voicemail Rules

## Descripción
Retrieve the organization's voicemail rules.

Organizational voicemail rules specify the default passcode requirements. They are provided for informational purposes only and cannot be modified.

Retrieving the organization's voicemail rules requires a full, user or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Retrieve voicemail rules for this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/voicemail/rules' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `defaultVoicemailPinRules` (object): Default voicemail passcode requirements.
  - `blockRepeatedPatternsEnabled` (boolean): If enabled, the passcode cannot contain repeated patterns. For example, 121212 and 123123.
  - `blockRepeatedDigits` (object): Settings to prevent single digits from being repeated in the passcode. For example, with a maximum value of 3, 111222 is allowed but 112222 is not allowed since it contains a repeated digit sequence longer than 3.
    - `enabled` (boolean): If enabled, checks for sequence of the same digit being repeated.
    - `max` (number): Maximum number of repeated digit sequence allowed. The minimum value is 1. The maximum value is 6.
  - `blockContiguousSequences` (object): Settings for not allowing numerical sequence in passcode (for example, 012345 or 987654).
    - `enabled` (boolean): If enabled, passcode should not contain a numerical sequence.
    - `numberOfAscendingDigits` (number): Specifies the maximum length of an ascending numerical sequence allowed. The minimum value is 2. The maximum value is 5. Example: If this value is set to 3, then 123856 is allowed, but 123485 is not allowed (since the ascending sequence 1234 exceeds 3 digits).
    - `numberOfDescendingDigits` (number): Specifies the maximum length of a descending numerical sequence allowed. The minimum value is 2. The maximum value is 5. Example: If this value is set to 3, then 321856 is allowed, but 432185 is not allowed (since the descending sequence 4321 exceeds 3 digits).
  - `length` (object): Length of the passcode.
    - `min` (number): The minimum value is 2. The maximum value is 15.
    - `max` (number): The minimum value is 3. The maximum value is 30.
  - `defaultVoicemailPinEnabled` (boolean): If enabled, the default voicemail passcode can be set.
- `expirePasscode` (object): Settings for passcode expiry.
  - `enabled` (boolean): If enabled, passcode expires after the number of days specified.
  - `numberOfDays` (number): Number of days for password expiry. The minimum value is 15. The maximum value is 180.
- `changePasscode` (object): Settings for passcode changes.
  - `enabled` (boolean): If enabled, set minimum number of days between passcode changes.
  - `numberOfDays` (number): Number of days between passcode changes. The minimum value is 1. The maximum value is 7.
- `blockPreviousPasscodes` (object): Settings for previous passcode usage.
  - `enabled` (boolean): If enabled, set how many of the previous passcodes are not allowed to be re-used.
  - `numberOfPasscodes` (number): Number of previous passcodes. The minimum value is 1. The maximum value is 10.

### Ejemplo — respuesta 200
```json
{
  "defaultVoicemailPinRules": {
    "blockRepeatedPatternsEnabled": true,
    "blockRepeatedDigits": {
      "enabled": true,
      "max": 3
    },
    "blockContiguousSequences": {
      "enabled": true,
      "numberOfAscendingDigits": 3,
      "numberOfDescendingDigits": 3
    },
    "length": {
      "min": 6,
      "max": 30
    },
    "defaultVoicemailPinEnabled": true
  },
  "expirePasscode": {
    "enabled": true,
    "numberOfDays": 100
  },
  "changePasscode": {
    "enabled": true,
    "numberOfDays": 1
  },
  "blockPreviousPasscodes": {
    "enabled": false,
    "numberOfPasscodes": 10
  }
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
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs