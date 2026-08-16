---
doc_id: webex-cloud-calling-get-telephony-config-cxessentials-wrapup-reasons
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/cxEssentials/wrapup/reasons
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.611461+00:00
---

# GET /telephony/config/cxEssentials/wrapup/reasons

**API:** Webex Cloud Calling
**Área:** Features: Customer Assist
**operationId:** `List Wrap Up Reasons`

## Resumen
List Wrap Up Reasons

## Descripción
Return the list of wrap-up reasons configured for a customer.

Agents handling calls use wrap-up reasons to categorize the outcome after a call ends. The control hub admin can configure these reasons for customers and assign them to queues. Upon call completion, agents select a wrap-up reason from the queue's assigned list. Each wrap-up reason includes a name and description, and can be set as the default for a queue. Admins can also configure a timer, which dictates the time agents have to select a reason post-call, with a default of 60 seconds. This timer can be disabled if necessary.

Retrieving the list of wrap-up reasons requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Respuestas
- **200**: OK
  - `wrapupReasons` (array) **(requerido)**: List of wrap-up reasons.
    - `id` (string) **(requerido)**: Unique wrap-up identifier.
    - `name` (string) **(requerido)**: Name of the wrap-up reason.
    - `description` (string): Description of the wrap-up reason.
    - `numberOfQueuesAssigned` (number) **(requerido)**: Number of queues assigned to the wrap-up reason.
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
