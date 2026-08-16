---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-availablecallerids
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/availableCallerIds
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.561350+00:00
---

# GET /telephony/config/people/me/settings/availableCallerIds

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `getMyAvailableCallerIDList`

## Resumen
Get My Available Caller ID List

## Descripción
Get details of available caller IDs of the authenticated user.

Caller ID settings control how a person's information is displayed when making outgoing calls.
The available caller ID list shows the caller IDs that the user can choose from.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Respuestas
- **200**: OK
  - `availableCallerIds` (array) **(requerido)**: A List of available caller IDs.
    - `type` (string) **(requerido)**: * `DEFAULT_CLID` - Caller ID is the default configured caller ID.  * `ADDITIONAL_CLID` - Caller ID is an additional external caller ID phone number available for the user.  * `CALL_QUEUE` - Caller ID is associated with a call queue.  * `HUNT_GROUP` - Caller ID is associated with a hunt group. Valores: DEFAULT_CLID, ADDITIONAL_CLID, CALL_QUEUE, HUNT_GROUP.
    - `id` (string): Unique identifier of the available caller ID.
    - `name` (string) **(requerido)**: Name of the available caller ID.
    - `directNumber` (string): Direct number of the available caller ID.
    - `extension` (string): Extension of the available caller ID.
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
