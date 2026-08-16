---
doc_id: webex-cloud-calling-post-people-personid-features-voicemail-actions-uploadnoanswergreeting-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /people/{personId}/features/voicemail/actions/uploadNoAnswerGreeting/invoke
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.642732+00:00
---

# POST /people/{personId}/features/voicemail/actions/uploadNoAnswerGreeting/invoke

**API:** Webex Cloud Calling
**Área:** User Call Settings (1/2)
**operationId:** `Configure No Answer Voicemail Greeting for a Person`

## Resumen
Configure No Answer Voicemail Greeting for a Person

## Descripción
Configure a person's No Answer Voicemail Greeting by uploading a Waveform Audio File Format, `.wav`, encoded audio file.

Your request will need to be a `multipart/form-data` request rather than JSON, using the `audio/wav` Content-Type.

This API requires a full or user administrator or location administrator auth token with the `spark-admin:people_write` scope or a user auth token with `spark:people_write` scope can be used by a person to update their settings.

## Parámetros
- `personId` [path] (string) **(requerido)**: Unique identifier for the person.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Respuestas
- **201**: Created
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
