---
doc_id: webex-cloud-calling-get-telephony-config-knowledgebases-knowledgebaseid-documents-documentid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/knowledgeBases/{knowledgeBaseId}/documents/{documentId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.550016+00:00
---

# GET /telephony/config/knowledgeBases/{knowledgeBaseId}/documents/{documentId}

**API:** Webex Cloud Calling
**Área:** AI Receptionist for Webex Calling, AI Receptionist
**operationId:** `getKnowledgeBaseDocument`

## Resumen
Get Knowledge Base Document Details

## Descripción
Get details of a specific document in a Knowledge Base.

Documents are content entries in a Knowledge Base that AI Receptionists use to answer caller queries. This API returns document metadata including name, content, status, and timestamps.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `knowledgeBaseId` [path] (string) **(requerido)**: Unique identifier for the Knowledge Base.
- `documentId` [path] (string) **(requerido)**: Unique identifier for the document.
- `orgId` [query] (string): Optional target organization identifier. Defaults to token's organization if not provided.

## Respuestas
- **200**: OK
  - `id` (string) **(requerido)**: Unique identifier for the document.
  - `knowledgeBaseId` (string) **(requerido)**: Unique identifier for the Knowledge Base this document belongs to.
  - `name` (string) **(requerido)**: Name of the document.
  - `content` (string) **(requerido)**: Content of the document.
  - `description` (string): Description of the document.
  - `fileName` (string): Original file name if the document was uploaded as a file.
  - `fileSize` (integer) **(requerido)**: Size of the document in bytes.
  - `knowledgeType` (string) **(requerido)**: Type of knowledge content. - `article` - Text-based content created directly via API. - `file` - Content uploaded as a document file. Valores: article, file.
  - `status` (string) **(requerido)**: Processing status of the document. - `pending` - Document is waiting to be processed. - `processing` - Document is currently being indexed. - `success` - Document has been successfully indexed and is available for queries. - `failed` - Document processing failed. Valores: pending, processing, success, failed.
  - `createdAt` (string) **(requerido)**: Timestamp indicating when the document was created, in ISO 8601 format.
  - `updatedAt` (string) **(requerido)**: Timestamp indicating when the document was last modified, in ISO 8601 format.
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
