---
doc_id: webex-cloud-calling-get-telephony-config-media-urls-s3path
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/media/urls/{s3Path}
operation_id: getMediaDownloadUrl
tags: Features: Announcement Repository
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.679438+00:00
---

# GET /telephony/config/media/urls/{s3Path}

**API:** Webex Cloud Calling
**Área:** Features: Announcement Repository
**operationId:** `getMediaDownloadUrl`

## Resumen
Get Media Download URL

## Descripción
Retrieve a pre-signed S3 download URL and KMS encryption key for a previously uploaded announcement media file identified by its S3 path.

To preview the announcement media file:

1. Download the KMS key - Use the Webex Node.js SDK and provide `kmsKeyUri` to download the key from KMS.

2. Download the encrypted media file - The encrypted media file content is stored in cloud and can be retrieved using `preSignedUrl`.

3. Decrypt the media content - Use the jose library to decrypt the content downloaded from `preSignedUrl` using the downloaded key.

This API is part of the Announcement Repository with Media URLs feature, which optimizes the media file upload process and adds the ability to preview existing announcement audio files by generating pre-signed S3 download URLs.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `s3Path` [path] (string) (**requerido**): The storage path of the announcement media file. Use the value after `/media/urls/` in the `fileUri` returned by the Get Announcement File URI or Get Location Announcement File URI API. For example, if `fileUri` is `cmf://customers/bf01164f-ed87-44d9-bc41-f63f26fb9663/media/urls/tmp/af01164f-ed87-44d9-bc41-f63f26fb8663`, then `s3Path` is `tmp/af01164f-ed87-44d9-bc41-f63f26fb8663`.
- `orgId` [query] (string): Retrieve the media download URL for this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/media/urls/<s3Path>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `preSignedUrl` (string) (**requerido**): A pre-signed S3 URL for downloading the announcement media file. The URL is time-limited and should be used promptly.
- `kmsKeyUri` (string) (**requerido**): The KMS key URI required to decrypt the media file downloaded from the pre-signed URL.

### Ejemplo — respuesta 200
```json
{
  "preSignedUrl": "https://s3.amazonaws.com/wxc-media/customers/bf01164f-ed87-44d9-bc41-f63f26fb9663/media/af01164f-ed87-44d9-bc41-f63f26fb8663?X-Amz-Signature=def456",
  "kmsKeyUri": "kms://kms-cisco.wbx2.com/keys/b56642f3-d597-420c-8a55-41aaa8c5b6e7"
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **410**: Gone: The requested media resource has expired and is no longer available.
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