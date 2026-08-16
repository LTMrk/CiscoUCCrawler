---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-selectiveforward
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/selectiveForward
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.572511+00:00
---

# GET /telephony/config/people/me/settings/selectiveForward

**API:** Webex Cloud Calling
**Área:** Call Settings For Me With UserHub Phase2
**operationId:** `getMySelectiveForwardSettings`

## Resumen
Get Selective Call Forward Settings for User

## Descripción
Get Selective Call Forward Settings for the authenticated user.

Selective Call Forward allows you to create customized rules to forward specific calls for users based on the phone number,identity and the time or day of the call.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Respuestas
- **200**: Selective Call Forwarding Settings retrieved for the authenticated user.
  - `enabled` (boolean) **(requerido)**: `true` if the Selective Forward feature is enabled.
  - `defaultPhoneNumberToForward` (string): The phone number to which calls are forwarded by default when the criteria conditions are met.
  - `ringReminderEnabled` (boolean): If `true`, a brief tone will be played on the person's phone when a call has been forwarded.
  - `destinationVoicemailEnabled` (boolean): Indicates whether calls that meet the criteria are forwarded to the destination phone number's voicemail.
  - `criteria` (array): A list of criteria specifying conditions when selective accept is in effect.
    - `id` (string) **(requerido)**: Unique identifier for criteria.
    - `scheduleName` (string) **(requerido)**: Name of the location's schedule which determines when the sequential ring is in effect.
    - `source` (string) **(requerido)**: * `ALL_NUMBERS` - Criteria applies to all incoming numbers.  * `SPECIFIC_NUMBERS` - Criteria applies only for specific incoming numbers.  * `ANY_INTERNAL` - Criteria applies to all internal incoming numbers.  * `ANY_EXTERNAL` - Criteria applies to all external incoming numbers. Valores: ALL_NUMBERS, SPECIFIC_NUMBERS, ANY_INTERNAL, ANY_EXTERNAL.
    - `ringEnabled` (boolean) **(requerido)**: When set to `true` sequential ringing is enabled for calls that meet the current criteria. Criteria with `ringEnabled` set to `false` take priority.
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
