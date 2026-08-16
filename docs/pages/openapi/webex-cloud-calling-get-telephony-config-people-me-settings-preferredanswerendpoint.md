---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-preferredanswerendpoint
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/preferredAnswerEndpoint
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.559831+00:00
---

# GET /telephony/config/people/me/settings/preferredAnswerEndpoint

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `getMyPreferredAnswerEndpoint`

## Resumen
Get Preferred Answer Endpoint

## Descripción
Retrieve the selected preferred answering endpoint for the user. If a preferred endpoint is not set for the person, API returns empty 

 A Webex Calling user may be associated with multiple endpoints such as Webex App (desktop or mobile), Cisco desk IP phone, Webex Calling-supported analog devices or third-party endpoints. Preferred answering endpoints allow users to specify which of these devices should be prioritized for answering calls, particularly when a person's extension (or a virtual line assigned to them) rings on multiple devices. This helps ensure that calls are answered on the most convenient or appropriate device for the person.

 This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Respuestas
- **200**: OK
  - `id` (string) **(requerido)**: Unique identifier for the endpoint.
  - `type` (string) **(requerido)**: * `DEVICE` - The endpoint is a device.  * `APPLICATION` - The endpoint is a application. Valores: DEVICE, APPLICATION.
  - `name` (string) **(requerido)**: The name field is either set to `Webex Desktop Application` or consists of the device model followed by the device tag in parentheses. For example, when the name is `Cisco 8865 (Phone in reception area)`, `Cisco 8865` is the device model and `Phone in reception area` is the device tag.
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

**Autenticación:** bearer-key

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
