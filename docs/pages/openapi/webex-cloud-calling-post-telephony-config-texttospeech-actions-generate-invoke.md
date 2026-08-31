---
doc_id: webex-cloud-calling-post-telephony-config-texttospeech-actions-generate-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/textToSpeech/actions/generate/invoke
operation_id: generateTextToSpeech
tags: Features: Announcement Repository
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.250374+00:00
---

# POST /telephony/config/textToSpeech/actions/generate/invoke

**API:** Webex Cloud Calling
**Área:** Features: Announcement Repository
**operationId:** `generateTextToSpeech`

## Resumen
Generate a Text-to-Speech Prompt

## Descripción
Generate a text-to-speech prompt from the provided text, voice, and language.

Text-to-speech (TTS) efficiently generates prompts, greetings, and announcements by converting written text into synthesized audio using the specified voice. The generated audio functions like a recorded WAV file, eliminating the need for manual recording.

This API requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Generate text-to-speech for this organization.

## Cuerpo de la petición (application/json)
- `voice` (string) (**requerido**): The voice ID used to generate the audio prompt. Use the List Text-to-Speech Voices API to retrieve available voices.
- `text` (string) (**requerido**): The text to convert to speech.
- `languageCode` (string) (**requerido**): The language code used to generate the audio prompt. Use the List Text-to-Speech Voices API to retrieve the language code supported by the selected voice.

### Ejemplo — petición
```json
{
  "voice": "ashley",
  "text": "Welcome to our service. Please hold while we connect you.",
  "languageCode": "en_us"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/textToSpeech/actions/generate/invoke' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"voice": "<voice>", "text": "<text>", "languageCode": "<languageCode>"}'
```

## Respuestas correctas
**202**: Accepted
- `id` (string) (**requerido**): Unique identifier of the text-to-speech generation request. Use this ID to track status using the Get Text-to-Speech Generation Status API.

### Ejemplo — respuesta 202
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1RFWFRfVE9fU1BFRUNILzMyMDE2NGY0LWU1YTMtNDFmZi1hMzI2LTY3YzA5OGU0MWQxZA"
}
```

## Respuestas de error
- **400**: Bad Request: The specified voice and language code do not match.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs