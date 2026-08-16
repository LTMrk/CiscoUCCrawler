---
doc_id: webex-cloud-calling-get-telephony-config-texttospeech-voices
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/textToSpeech/voices
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.596586+00:00
---

# GET /telephony/config/textToSpeech/voices

**API:** Webex Cloud Calling
**Área:** Features: Announcement Repository
**operationId:** `listTextToSpeechVoices`

## Resumen
List Text-to-Speech Voices

## Descripción
Fetch a list of available text-to-speech voices. Use the returned voice ID and language code in the generation request.

Text-to-speech (TTS) efficiently generates prompts, greetings, and announcements by converting written text into synthesized audio using the specified voice. The generated audio functions like a recorded WAV file, eliminating the need for manual recording.

This API requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `languageCode` [query] (string): Language code used to filter the available text-to-speech voices. Use the Read the List of Announcement Languages API to retrieve supported language codes. If not specified, the default language code is `en_us`.
- `orgId` [query] (string): List text-to-speech voices supported for this organization.

## Respuestas
- **200**: OK
  - `voices` (array) **(requerido)**: Array of available text-to-speech voices.
    - `id` (string) **(requerido)**: The voice ID used to generate the audio prompt.
    - `label` (string) **(requerido)**: The voice label, including the voice name and gender.
    - `languageCode` (string) **(requerido)**: The language code supported by the voice.
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
