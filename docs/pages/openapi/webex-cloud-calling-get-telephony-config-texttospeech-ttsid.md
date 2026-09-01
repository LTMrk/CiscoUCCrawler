---
doc_id: webex-cloud-calling-get-telephony-config-texttospeech-ttsid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/textToSpeech/{ttsId}
operation_id: getTextToSpeechGenerationStatus
tags: Features: Announcement Repository
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.680092+00:00
---

# GET /telephony/config/textToSpeech/{ttsId}

**API:** Webex Cloud Calling
**Área:** Features: Announcement Repository
**operationId:** `getTextToSpeechGenerationStatus`

## Resumen
Get Text-to-Speech Generation Status

## Descripción
Get the status of a text-to-speech generation request by its ID. If the status is SUCCESS, the response includes `promptUrl`, `kmsKeyUri`, and `fileUri` to preview or use the audio prompt.

To preview the audio prompt:

1. Download the KMS key - use the Webex Node.js SDK and provide `kmsKeyUri` to download the key from KMS.

2. Download the encrypted audio - The encrypted audio file content is stored in cloud and can be retrieved using `promptURL`.

3. Decrypt the audio content - Use the jose library to decrypt the content downloaded from `promptUrl` using the downloaded key.

Text-to-speech (TTS) efficiently generates prompts, greetings, and announcements by converting written text into synthesized audio using the specified voice. The generated audio functions like a recorded WAV file, eliminating the need for manual recording.

This API requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `ttsId` [path] (string) (**requerido**): Unique identifier of the text-to-speech generation request.
- `orgId` [query] (string): Get text-to-speech status for this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/textToSpeech/<ttsId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Unique identifier of the text-to-speech generation request.
- `voice` (string) (**requerido**): The voice ID used to generate the audio prompt.
- `text` (string) (**requerido**): The input text used to generate the audio prompt.
- `languageCode` (string) (**requerido**): The language code used to generate the audio prompt.
- `status` (string) (**requerido**): The status of the text-to-speech generation request. Valores: IN_PROGRESS, SUCCESS, FAILURE.
- `promptUrl` (string): A URL to download the encrypted audio prompt. Only available when status is `SUCCESS`.
- `kmsKeyUri` (string): The KMS key URI required to decrypt the prompt downloaded from `promptUrl`. Only available when status is `SUCCESS`.
- `fileUri` (string): A file URI you can use when configuring an announcement. Only available when status is `SUCCESS`.
- `errorMessage` (string): A detailed message describing why generation failed. Only present when status is `FAILURE`.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1RFWFRfVE9fU1BFRUNILzMyMDE2NGY0LWU1YTMtNDFmZi1hMzI2LTY3YzA5OGU0MWQxZA",
  "voice": "ashley",
  "text": "Welcome to our service. Please hold while we connect you.",
  "languageCode": "en_us",
  "status": "SUCCESS",
  "promptUrl": "https://wxc-int-media-file.ciscospark.com/b535b87e-0994-4387-ace1-56facfba9b75/tmp/af01164f-ed87-44d9-bc41-f63f26fb8663",
  "kmsKeyUri": "kms://kms-cisco.wbx2.com/keys/b56642f3-d597-420c-8a55-41aaa8c5b6e7",
  "fileUri": "cmf://customers/bf01164f-ed87-44d9-bc41-f63f26fb9663/media/tmp/af01164f-ed87-44d9-bc41-f63f26fb8663"
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **410**: Gone: The requested resource is no longer available.
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