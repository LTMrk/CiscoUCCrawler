---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-voiceportal-passcoderules
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/voicePortal/passcodeRules
operation_id: Get VoicePortal Passcode Rule
tags: Location Call Settings:  Voicemail
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.126598+00:00
---

# GET /telephony/config/locations/{locationId}/voicePortal/passcodeRules

**API:** Webex Cloud Calling
**Área:** Location Call Settings:  Voicemail
**operationId:** `Get VoicePortal Passcode Rule`

## Resumen
Get VoicePortal Passcode Rule

## Descripción
Retrieve the voice portal passcode rule for a location.

Voice portals provide an interactive voice response (IVR) system so administrators can manage auto attendant anouncements

Retrieving the voice portal passcode rule requires a full read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieve voice portal passcode rules for this location.
- `orgId` [query] (string): Retrieve voice portal passcode rules for this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/voicePortal/passcodeRules' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `expirePasscode` (object): Settings for passcode expiry.
  - `enabled` (boolean): If enabled, passcode expires after the number of days specified.
  - `numberOfDays` (number): Number of days for passcode expiry. The minimum value is 15. The maximum value is 100.
- `failedAttempts` (object): Number of failed attempts allowed.
  - `enabled` (boolean): If enabled, allows specified number of attempts before locking voice portal access.
  - `attempts` (number): Number of failed attempts allowed.
- `blockPreviousPasscodes` (object): Settings for previous passcode usage.
  - `enabled` (boolean): If enabled, the specified number of passcode changes must occur before a passcode can be re-used.
  - `numberOfPasscodes` (number): Number of previous passcodes not allowed to be re-used. The minimum value is 1. The maximum value is 10.
- `blockRepeatedDigits` (object): Settings to prevent single digits from being repeated in the passcode. For example, with a maximum value of 3, 111222 is allowed but 112222 is not allowed since it contains a repeated digit sequence longer than 3.
  - `enabled` (boolean): If enabled, checks for sequence of the same digit being repeated.
  - `max` (number): Maximum number of repeated digit sequence allowed. The minimum value is 1. The maximum value is 6.
- `blockContiguousSequences` (object): Settings for not allowing numerical sequence in passcode (for example, 012345 or 987654).
  - `enabled` (boolean): If enabled, do not allow the specified number of ascending or descending digits in a row.
  - `numberOfAscendingDigits` (number): Specifies the maximum length of an ascending numerical sequence allowed. The minimum value is 2. The maximum value is 5. Example: If this value is set to 3, then 123856 is allowed, but 123485 is not allowed (since the ascending sequence 1234 exceeds 3 digits).
  - `numberOfDescendingDigits` (number): Specifies the maximum length of a descending numerical sequence allowed. The minimum value is 2. The maximum value is 5. Example: If this value is set to 3, then 321856 is allowed, but 432185 is not allowed (since the descending sequence 4321 exceeds 3 digits).
- `length` (object): Allowed length of the passcode.
  - `min` (number): The minimum value is 2. The maximum value is 15.
  - `max` (number): The minimum value is 3. The maximum value is 30.
- `blockRepeatedPatternsEnabled` (boolean): If enabled, the passcode cannot contain repeated patterns. For example, 121212 and 123123.
- `blockUserNumberEnabled` (boolean): If enabled, the passcode do not allow user phone number or extension.
- `blockReversedUserNumberEnabled` (boolean): If enabled, the passcode do not allow revered phone number or extension.
- `blockReversedOldPasscodeEnabled` (boolean): If enabled, the passcode do not allow setting reversed old passcode.

### Ejemplo — respuesta 200
```json
{
  "expirePasscode": {
    "enabled": true,
    "numberOfDays": 180
  },
  "failedAttempts": {
    "enabled": true,
    "attempts": 3
  },
  "blockPreviousPasscodes": {
    "enabled": true,
    "numberOfPasscodes": 10
  },
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
    "min": 3,
    "max": 3
  },
  "blockRepeatedPatternsEnabled": true,
  "blockUserNumberEnabled": true,
  "blockReversedUserNumberEnabled": true,
  "blockReversedOldPasscodeEnabled": true
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