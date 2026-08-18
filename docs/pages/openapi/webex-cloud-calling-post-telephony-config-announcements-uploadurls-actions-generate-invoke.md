---
doc_id: webex-cloud-calling-post-telephony-config-announcements-uploadurls-actions-generate-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/announcements/uploadUrls/actions/generate/invoke
operation_id: generateUploadUrl
tags: Features: Announcement Repository
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.284978+00:00
---

# POST /telephony/config/announcements/uploadUrls/actions/generate/invoke

**API:** Webex Cloud Calling
**Área:** Features: Announcement Repository
**operationId:** `generateUploadUrl`

## Resumen
Generate Upload URL

## Descripción
Generate a pre-signed S3 upload URL, KMS encryption key for uploading an announcement media file. And file URI to create announcement using the media file.

To encrypt and upload the announcement media file:

1. Download the KMS key - Use the Webex Node.js SDK and provide `kmsKeyUri` to download the key from KMS.

2. Encrypt media file - Use the jose library to encrypt the raw media file with the downloaded key.

3. Upload the encrypted media file - Send a `PUT` request with encrypted media file to the `preSignedUrl`. The request must include following headers:

- `x-amz-meta-contenttype`: The media MIME type, for example: `audio/wav`

- `x-amz-meta-kmskeyuri`: The returned `kmsKeyUri`, for example: `kms://kms-cisco.wbx2.com/keys/b56642f3-d597-420c-8a55-41aaa8c5b6e7`

- `x-amz-tagging`: `tmp=true`

This API is part of the Announcement Repository with Media URLs feature, which optimizes the media file upload process by enabling direct S3 uploads and adds the ability to preview existing announcement audio files.

This API requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Generate the upload URL for this organization.

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/announcements/uploadUrls/actions/generate/invoke' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `preSignedUrl` (string) (**requerido**): A pre-signed S3 URL for uploading the announcement media file. The URL is time-limited and should be used promptly.
- `kmsKeyUri` (string) (**requerido**): The KMS key URI used to encrypt the media file before uploading to the pre-signed URL.
- `fileUri` (string) (**requerido**): A file URI that identifies the uploaded media. Use this URI when configuring announcements.

### Ejemplo — respuesta 200
```json
{
  "preSignedUrl": "https://s3.amazonaws.com/wxc-media/uploads/af01164f-ed87-44d9-bc41-f63f26fb8663?X-Amz-Signature=abc123",
  "kmsKeyUri": "kms://kms-cisco.wbx2.com/keys/b56642f3-d597-420c-8a55-41aaa8c5b6e7",
  "fileUri": "cmf://customers/bf01164f-ed87-44d9-bc41-f63f26fb9663/media/af01164f-ed87-44d9-bc41-f63f26fb8663"
}
```

## Respuestas de error
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

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs