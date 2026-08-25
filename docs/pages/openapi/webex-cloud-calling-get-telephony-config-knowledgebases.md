---
doc_id: webex-cloud-calling-get-telephony-config-knowledgebases
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/knowledgeBases
operation_id: listKnowledgeBases
tags: AI Receptionist for Webex Calling, AI Receptionist
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.328980+00:00
---

# GET /telephony/config/knowledgeBases

**API:** Webex Cloud Calling
**Área:** AI Receptionist for Webex Calling, AI Receptionist
**operationId:** `listKnowledgeBases`

## Resumen
List Knowledge Bases

## Descripción
Get list of Knowledge Bases for an organization.

Knowledge Bases are repositories of information that AI Receptionists use to answer caller queries. This API returns all knowledge bases available in the organization.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Optional target organization identifier. Defaults to token's organization if not provided.
- `max` [query] (integer): Maximum number of items returned in the response. Default: 100.
- `start` [query] (integer): Zero-based offset for pagination.
- `name` [query] (string): Search knowledge bases by name (contains match).

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/knowledgeBases' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `knowledgeBases` (array): List of Knowledge Bases.
  - `id` (string) (**requerido**): Unique identifier of the Knowledge Base.
  - `name` (string) (**requerido**): The display name assigned to the Knowledge Base. Used to identify the KB across the platform.
  - `description` (string): A human-readable description providing additional context about the purpose or contents of the Knowledge Base.
  - `documentsCount` (integer) (**requerido**): The total count of documents that have been uploaded or indexed into the Knowledge Base.
  - `filesCount` (integer) (**requerido**): The total count of files that have been uploaded to the Knowledge Base.
  - `filesSize` (integer/int64) (**requerido**): The cumulative size (in bytes) of all files stored in the Knowledge Base.
  - `createdAt` (string/date-time) (**requerido**): Timestamp indicating when the Knowledge Base was originally created, in ISO 8601 format.
  - `updatedAt` (string/date-time) (**requerido**): Timestamp indicating when the Knowledge Base was last modified, in ISO 8601 format.
  - `mappedBots` (array): List of AI Receptionists that are currently associated with this Knowledge Base.
    - `id` (string) (**requerido**): Unique identifier for the AI Receptionist.
    - `connectedAt` (string/date-time) (**requerido**): Timestamp indicating when the Knowledge Base was associated with the AI Receptionist, in ISO 8601 format.
    - `agentId` (string) (**requerido**): Unique identifier for the AI agent associated with this receptionist.
    - `name` (string) (**requerido**): Name of the AI Receptionist (Bot).

### Ejemplo — respuesta 200
```json
{
  "knowledgeBases": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0tOT1dMRURHRV9CQVNFLzY5YzNlY2NjZDc5MzYzZGM2ODliM2UyYw",
      "name": "Shree HealthCare Clinic KB",
      "description": "A centralized repository of medical and administrative information for Shree Health Care Clinic.",
      "documentsCount": 5,
      "filesCount": 3,
      "filesSize": 210,
      "createdAt": "2024-08-16T18:30:20.882Z",
      "updatedAt": "2024-08-16T18:30:20.882Z",
      "mappedBots": [
        {
          "id": "Y2lzY29zcGFyazovL3VzL0FJX1JFQ0VQVElPTklTVC8wNWViZTUzZS02YTg5LTRkMTktYmIzYi0xNmJhZDU4OWRhNmE",
          "connectedAt": "2024-08-16T18:30:20.882Z",
          "agentId": "Y2lzY29zcGFyazovL3VzL0FJX0FHRU5ULzY5YmFhZDIwOGUzOWUyMGE0ZTNkNjEwNA",
          "name": "AIR P Test"
        }
      ]
    }
  ]
}
```

## Respuestas de error
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

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs