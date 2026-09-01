---
doc_id: webex-cloud-calling-delete-telephony-config-supervisors
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: DELETE
path: /telephony/config/supervisors
operation_id: deleteBulkCallQueueSupervisors
tags: Features:  Call Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.696292+00:00
---

# DELETE /telephony/config/supervisors

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `deleteBulkCallQueueSupervisors`

## Resumen
Delete Call Queue or Customer Assist Supervisors

## Descripción
Delete the Call Queue or Customer Assist supervisors for an organization. Once you remove the supervisor, assigned agents will lose their supervisor assignments.

Supervisors are users who manage agents and who perform functions including monitoring, coaching, and more.

Requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Delete supervisors in bulk for this organization.

## Cuerpo de la petición (application/json)
- `supervisorIds` (array) (**requerido**): Array of supervisors IDs to be deleted.
- `hasCxEssentials` (boolean): Delete the Customer Assist supervisors, when `true`. Otherwise delete the Call Queue supervisors. The default value is `false`.
- `deleteAll` (boolean): If present the `supervisorIds` array is ignored, and all supervisors in the context are deleted. **WARNING**: This will remove all supervisors from the organization.

### Ejemplo — petición
```json
{
  "supervisorIds": [
    "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80Y2I1M2ZmMy01NWViLTQ2MzYtYTE4ZC05NWVjZmFhM2E4NmY",
    "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8wNzY2ZDNjNC0xZTg1LTQ4YzgtYTFkZi1mMWUzYTAyMDg1MWE"
  ],
  "hasCxEssentials": true,
  "deleteAll": false
}
```

## Ejemplo de invocación
```bash
curl -X DELETE '/telephony/config/supervisors' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"supervisorIds": []}'
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