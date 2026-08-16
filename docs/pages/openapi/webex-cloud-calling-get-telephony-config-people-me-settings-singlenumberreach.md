---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-singlenumberreach
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/singleNumberReach
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.563319+00:00
---

# GET /telephony/config/people/me/settings/singleNumberReach

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `getMySingleNumberReachSettings`

## Resumen
Get User's Single Number Reach Settings

## Descripción
Retrieves all single number reach settings configured for the authenticated user.

The "Single Number Reach" feature in Webex allows users to access their business phone capabilities from any device, making it easy to make and receive calls as if at their office. This is especially useful for remote or mobile workers needing flexibility.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Respuestas
- **200**: OK
  - `enabled` (boolean) **(requerido)**: A flag to enable or disable single Number Reach.
  - `alertAllNumbersForClickToDialCallsEnabled` (boolean): Flag to enable alerting single number reach numbers for click to dial calls.
  - `numbers` (array) **(requerido)**: Array of single number reach number entries.
    - `id` (string) **(requerido)**: ID of Single number reach. Note that this ID contains base64 encoded phoneNumber data and can change if the phone number is modified.
    - `phoneNumber` (string) **(requerido)**: The phone number that will ring when a call is received. The number should be in E.164 format.
    - `enabled` (boolean) **(requerido)**: A flag to enable or disable this single Number Reach phone number.
    - `name` (string) **(requerido)**: Name of the single number reach phone number entry.
    - `doNotForwardCallsEnabled` (boolean) **(requerido)**: If enabled, the call forwarding settings of provided phone Number will not be applied.
    - `answerConfirmationEnabled` (boolean) **(requerido)**: If enabled, the call recipient will be prompted to press a key before being connected.
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
