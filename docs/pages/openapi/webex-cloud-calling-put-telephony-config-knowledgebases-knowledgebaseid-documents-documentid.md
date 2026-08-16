---
doc_id: webex-cloud-calling-put-telephony-config-knowledgebases-knowledgebaseid-documents-documentid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/knowledgeBases/{knowledgeBaseId}/documents/{documentId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.550118+00:00
---

# PUT /telephony/config/knowledgeBases/{knowledgeBaseId}/documents/{documentId}

**API:** Webex Cloud Calling
**Área:** AI Receptionist for Webex Calling, AI Receptionist
**operationId:** `updateKnowledgeBaseDocument`

## Resumen
Modify Knowledge Base Document

## Descripción
Modify a document in a Knowledge Base.

Documents are content entries in a Knowledge Base that AI Receptionists use to answer caller queries. This API allows updating the name and content of an existing document.

This API requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `knowledgeBaseId` [path] (string) **(requerido)**: Unique identifier for the Knowledge Base.
- `documentId` [path] (string) **(requerido)**: Unique identifier for the document.
- `orgId` [query] (string): Optional target organization identifier. Defaults to token's organization if not provided.

## Cuerpo de la petición (application/json)
- `name` (string): The display name assigned to the Knowledge Base document. Used to identify the document across the platform.
- `content` (string): The content of the document.

### Ejemplo de petición
```json
{
  "name": "Updated FAQ Document",
  "content": "This is the updated content for the FAQ document."
}
```

## Respuestas
- **204**: No Content
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
