---
doc_id: webex-cloud-calling-get-telephony-config-people-me-voicemail-rules
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/voicemail/rules
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.576629+00:00
---

# GET /telephony/config/people/me/voicemail/rules

**API:** Webex Cloud Calling
**Área:** Call Settings For Me Phase 5
**operationId:** `getUserVoicemailRules`

## Resumen
Get Person's Voicemail Rules

## Descripción
Get person's voicemail passcode rules. Voicemail rules specify the default passcode requirements. They are provided for informational purposes only and cannot be modified.

The voicemail feature allows users to manage their voicemail settings as part of Webex Calling. Voicemail rules help ensure secure access to voice messages by defining passcode complexity requirements.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Respuestas
- **200**: OK
  - `blockRepeatedPatternsEnabled` (boolean) **(requerido)**: If enabled, the passcode cannot contain repeated patterns. For example, 121212 and 123123.
  - `blockUserNumberEnabled` (boolean) **(requerido)**: If enabled, the passcode must not match the user's own phone number.
  - `blockReversedUserNumberEnabled` (boolean) **(requerido)**: If enabled, the passcode must not match the user's phone number in reverse.
  - `blockPreviousPasscodes` (object) **(requerido)**: Settings for previous passcode usage.
    - `enabled` (boolean) **(requerido)**: If enabled, set how many of the previous passcodes are not allowed to be re-used.
    - `numberOfPasscodes` (integer) **(requerido)**: Number of previous passcodes. The minimum value is 1. The maximum value is 10.
  - `blockReversedOldPasscodeEnabled` (boolean) **(requerido)**: If enabled, the passcode must not match the user's old passcodes in reverse.
  - `blockRepeatedDigits` (object) **(requerido)**: Settings to prevent single digits from being repeated in the passcode. For example, with a maximum value of 3, 111222 is allowed but 112222 is not allowed since it contains a repeated digit sequence longer than 3.
    - `enabled` (boolean) **(requerido)**: If enabled, checks for sequence of the same digit being repeated.
    - `max` (integer) **(requerido)**: Maximum number of repeated digit sequence allowed. The minimum value is 1. The maximum value is 6.
  - `blockContiguousSequences` (object) **(requerido)**: Settings for not allowing numerical sequence in passcode (for example, 012345 or 987654).
    - `enabled` (boolean) **(requerido)**: If enabled, passcode should not contain a numerical sequence.
    - `numberOfAscendingDigits` (integer) **(requerido)**: Specifies the maximum length of an ascending numerical sequence allowed. The minimum value is 2. The maximum value is 5. Example: If this value is set to 3, then 123856 is allowed, but 123485 is not allowed (since the ascending sequence 1234 exceeds 3 digits).
    - `numberOfDescendingDigits` (integer) **(requerido)**: Specifies the maximum length of a descending numerical sequence allowed. The minimum value is 2. The maximum value is 5. Example: If this value is set to 3, then 321856 is allowed, but 432185 is not allowed (since the descending sequence 4321 exceeds 3 digits).
  - `length` (object) **(requerido)**: Length of the passcode.
    - `min` (integer) **(requerido)**: The minimum value is 2. The maximum value is 15.
    - `max` (integer) **(requerido)**: The minimum value is 3. The maximum value is 30.
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
