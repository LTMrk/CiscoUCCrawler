---
doc_id: webex-cloud-calling-get-telephony-config-texttospeech-usage
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/textToSpeech/usage
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.596375+00:00
---

# GET /telephony/config/textToSpeech/usage

**API:** Webex Cloud Calling
**Área:** Features: Announcement Repository
**operationId:** `getTextToSpeechUsage`

## Resumen
Get Text-to-Speech Usage

## Descripción
Retrieve text-to-speech usage information, including the number of API calls made, the maximum allowed within the time window, and the timestamp indicating when the usage will reset.

Text-to-speech (TTS) efficiently generates prompts, greetings, and announcements by converting written text into synthesized audio using the specified voice. The generated audio functions like a recorded WAV file, eliminating the need for manual recording.

This API requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Get text-to-speech usage for this organization.

## Respuestas
- **200**: OK
  - `noOfApiCalls` (integer) **(requerido)**: The number of text-to-speech API calls made in the current time window.
  - `maxAllowedApiCalls` (integer) **(requerido)**: The maximum number of text-to-speech API calls allowed in the current time window.
  - `usageResetTimestamp` (string): The timestamp when the usage counter will reset. It will be returned when reaching the maximum allowed API calls in the time window.
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
