---
doc_id: webex-cloud-calling-post-convergedrecordings-reassign
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /convergedRecordings/reassign
operation_id: reassign_recordings
tags: Converged Recordings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.179972+00:00
---

# POST /convergedRecordings/reassign

**API:** Webex Cloud Calling
**Área:** Converged Recordings
**operationId:** `reassign_recordings`

## Resumen
Reassign Recordings

## Descripción
Reassigns recordings to a new user. As an administrator, you can reassign a list of recordings or all recordings of a particular user to a new user.
The recordings can belong to an org user, a virtual line, or a workspace, but the destination user should only be a valid org user.

* For a org user either `ownerEmail` or `recordingIds` or both must be provided.

* For a virtual line or a workspace, `ownerID` or `recordingIds` or both must be provided.

* If `recordingIds` and `ownerID` is empty but `ownerEmail` is provided, all recordings owned by the `ownerEmail` are reassigned to `reassignOwnerEmail`.

* If `recordingIds` is provided and `ownerEmail` or `ownerID` is also provided, only the recordings specified by `recordingIds` that are owned by `ownerEmail` or `ownerID` are reassigned to `reassignOwnerEmail`.

* If `ownerEmail` and `ownerID` is empty but `recordingIds` is provided, the recordings specified by `recordingIds` are reassigned to `reassignOwnerEmail` regardless of the current owner.

* If both `ownerId` and `ownerEmail` are passed along with `recordingIds`, only the recordings specified by `recordingIds` that are owned by `ownerEmail` are reassigned to `reassignOwnerEmail`.

* If `recordingIds` is empty but both `ownerId` and `ownerEmail` is provided, all recordings owned by the `ownerEmail` are reassigned to `reassignOwnerEmail`.

The `spark-admin:recordings_write` scope is required to reassign recordings.

## Cuerpo de la petición (application/json)
- `ownerEmail` (string): Recording owner email.
- `ownerID` (string): Recording owner ID. Can be a user, a virtual line, or a workspace.
- `recordingIds` (array): List of recording identifiers to be reassigned.
- `reassignOwnerEmail` (string) (**requerido**): New owner of the recordings.

### Ejemplo — petición
```json
{
  "ownerEmail": "john.andersen@example.com",
  "recordingIds": [
    "4f914b1dfe3c4d11a61730f18c0f5387",
    "4f914b1dfe3c4d11a61730f18c0f5388"
  ],
  "reassignOwnerEmail": "brenda.song@example.com"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/convergedRecordings/reassign' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"reassignOwnerEmail": "<reassignOwnerEmail>"}'
```

## Respuestas correctas
**204**: No Content

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