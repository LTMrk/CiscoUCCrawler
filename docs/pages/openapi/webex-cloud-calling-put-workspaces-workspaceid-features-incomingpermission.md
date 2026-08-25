---
doc_id: webex-cloud-calling-put-workspaces-workspaceid-features-incomingpermission
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /workspaces/{workspaceId}/features/incomingPermission
operation_id: Modify Incoming Permission Settings for a Workspace
tags: Workspace Call Settings (1/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.589208+00:00
---

# PUT /workspaces/{workspaceId}/features/incomingPermission

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings (1/2)
**operationId:** `Modify Incoming Permission Settings for a Workspace`

## Resumen
Modify Incoming Permission Settings for a Workspace

## Descripción
Modify Incoming Permission settings for a Workspace.

Incoming permission settings allow modifying permissions for a workspace that can be different from the organization's default to manage different call types.

This API requires a full or user administrator or location administrator auth token with the `spark-admin:workspaces_write` scope or a user auth token with `spark:workspaces_write` scope can be used to update workspace settings.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Unique identifier for the workspace.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.

## Cuerpo de la petición (application/json)
- `useCustomEnabled` (boolean): Incoming Permission state. If disabled, the default settings are used.
- `externalTransfer` (string): Call transfer setting.  * `ALLOW_ALL_EXTERNAL` - All external calls are allowed.  * `ALLOW_ONLY_TRANSFERRED_EXTERNAL` - Only externally transferred external calls are allowed.  * `BLOCK_ALL_EXTERNAL` - All external calls are blocked. Valores: ALLOW_ALL_EXTERNAL, ALLOW_ONLY_TRANSFERRED_EXTERNAL, BLOCK_ALL_EXTERNAL.
- `internalCallsEnabled` (boolean): Flag to indicate if the workspace can receive internal calls.
- `collectCallsEnabled` (boolean): Flag to indicate if the workspace can receive collect calls.

### Ejemplo — petición
```json
{
  "useCustomEnabled": true,
  "externalTransfer": "BLOCK_ALL_EXTERNAL",
  "internalCallsEnabled": false,
  "collectCallsEnabled": false
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/workspaces/<workspaceId>/features/incomingPermission' \
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