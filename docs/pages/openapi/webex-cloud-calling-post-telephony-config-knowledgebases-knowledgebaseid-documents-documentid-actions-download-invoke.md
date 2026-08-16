---
doc_id: webex-cloud-calling-post-telephony-config-knowledgebases-knowledgebaseid-documents-documentid-actions-download-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/config/knowledgeBases/{knowledgeBaseId}/documents/{documentId}/actions/download/invoke
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.550295+00:00
---

# POST /telephony/config/knowledgeBases/{knowledgeBaseId}/documents/{documentId}/actions/download/invoke

**API:** Webex Cloud Calling
**Área:** AI Receptionist for Webex Calling, AI Receptionist
**operationId:** `downloadKnowledgeBaseDocument`

## Resumen
Download Knowledge Base Document

## Descripción
Download a document from a Knowledge Base.

Documents are files uploaded to a Knowledge Base that AI Receptionists use to answer caller queries. The response contains the file content with appropriate Content-Type and Content-Disposition headers.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

**WARNING:** This API is not callable using the developer portal web interface due to the lack of support for binary file downloads. This API can be utilized using other tools that support binary responses, such as Postman or curl.

## Parámetros
- `knowledgeBaseId` [path] (string) **(requerido)**: Unique identifier for the Knowledge Base.
- `documentId` [path] (string) **(requerido)**: Unique identifier for the document.
- `orgId` [query] (string): Optional target organization identifier. Defaults to token's organization if not provided.

## Respuestas
- **200**: OK - File content returned
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
