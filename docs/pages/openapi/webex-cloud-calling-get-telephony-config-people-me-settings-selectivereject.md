---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-selectivereject
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/selectiveReject
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.572779+00:00
---

# GET /telephony/config/people/me/settings/selectiveReject

**API:** Webex Cloud Calling
**Área:** Call Settings For Me With UserHub Phase3
**operationId:** `getMySelectiveRejectSettings`

## Resumen
Get Selective Call Reject Settings for User

## Descripción
Get Selective Call Reject Settings for the authenticated user.

Selective Call Reject allows you to create customized rules to reject specific calls for users based on the phone number,identity and the time or day of the call.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Respuestas
- **200**: Selective Call Reject Settings retrieved for the authenticated user.
  - `enabled` (boolean) **(requerido)**: `true` if the selective reject feature is enabled.
  - `criteria` (array): A list of criteria specifying conditions when selective reject is in effect.
    - `id` (string) **(requerido)**: Unique identifier for criteria.
    - `scheduleName` (string) **(requerido)**: Name of the schedule associated with the criteria.
    - `source` (string) **(requerido)**: Type of the source.  * `ALL_NUMBERS` - Select to reject calls from Any Phone Number.  * `SPECIFIC_NUMBERS` - Select to reject calls from Select Phone Numbers.  * `FORWARDED` - Select to reject calls that have been forwarded. Valores: ALL_NUMBERS, SPECIFIC_NUMBERS, FORWARDED.
    - `rejectEnabled` (boolean) **(requerido)**: Determines whether selective call reject is applied for calls matching this criteria. If `true`, selective call reject is applied. If `false`, this criteria acts as a 'Don't Reject' rule, preventing call rejections. Criteria with rejectEnabled set to false have precedence over criteria with rejectEnabled set to true.
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
