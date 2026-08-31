---
doc_id: webex-cloud-calling-delete-convergedrecordings-recordingid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: DELETE
path: /convergedRecordings/{recordingId}
operation_id: delete_a_recording
tags: Converged Recordings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.179427+00:00
---

# DELETE /convergedRecordings/{recordingId}

**API:** Webex Cloud Calling
**Área:** Converged Recordings
**operationId:** `delete_a_recording`

## Resumen
Delete a Recording

## Descripción
Removes a recording with a specified recording ID. The deleted recording cannot be recovered.

If a Compliance Officer deletes another user's recording, the recording will be inaccessible to regular users (host, attendees and shared), and to the Compliance officer as well. This action purges the recordings from Webex.

Delete a Recording requires the `spark-compliance:recordings_write` scope.

## Parámetros
- `recordingId` [path] (string) (**requerido**): A unique identifier for the recording.

## Cuerpo de la petición (application/json)
- `reason` (string): Reason for deleting a recording. Only required when a Compliance Officer is operating on another user's recording.
- `comment` (string): Compliance Officer's explanation for deleting a recording. The comment can be a maximum of 255 characters long.

### Ejemplo — petición
```json
{
  "reason": "audit",
  "comment": "Compliance Officer's optional explanation for deleting a recording"
}
```

## Ejemplo de invocación
```bash
curl -X DELETE '/convergedRecordings/<recordingId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
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