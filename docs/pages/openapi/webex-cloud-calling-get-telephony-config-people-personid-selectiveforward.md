---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-selectiveforward
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/{personId}/selectiveForward
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.650344+00:00
---

# GET /telephony/config/people/{personId}/selectiveForward

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `getUserSelectiveCallForwarding`

## Resumen
Get the User’s Selective Call Forwarding

## Descripción
Retrieve selective call forwarding criteria for a user.

With the Selective Call Forwarding feature, you can create different rules to forward specific calls based on the phone number, who's calling, and/or the time and day of the call.

Requires a full, user, read-only, or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `personId` [path] (string) **(requerido)**: A unique identifier for the person.
- `orgId` [query] (string): Organization in which the user resides.

## Respuestas
- **200**: OK
  - `enabled` (boolean) **(requerido)**: `true` if the Selective Forward feature is enabled.
  - `defaultPhoneNumberToForward` (string) **(requerido)**: Enter the phone number to forward calls to during this schedule.
  - `ringReminderEnabled` (boolean) **(requerido)**: When `true`, enables a ring reminder for such calls.
  - `destinationVoicemailEnabled` (boolean) **(requerido)**: Enables forwarding for all calls to voicemail. This option is only available for internal phone numbers or extensions.
  - `criteria` (array) **(requerido)**: A list of criteria specifying conditions when selective forward feature is in effect.
    - `id` (string) **(requerido)**: Unique identifier for criteria.
    - `scheduleName` (string) **(requerido)**: Name of the location's schedule which determines when the sequential ring is in effect.
    - `source` (string) **(requerido)**: * `ALL_NUMBERS` - Criteria applies to all incoming numbers.  * `SPECIFIC_NUMBERS` - Criteria applies only for specific incoming numbers.  * `ANY_INTERNAL` - Criteria applies to all internal incoming numbers.  * `ANY_EXTERNAL` - Criteria applies to all external incoming numbers. Valores: ALL_NUMBERS, SPECIFIC_NUMBERS, ANY_INTERNAL, ANY_EXTERNAL.
    - `ringEnabled` (boolean) **(requerido)**: When set to `true` sequential ringing is enabled for calls that meet the current criteria. Criteria with `ringEnabled` set to `false` take priority.
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
