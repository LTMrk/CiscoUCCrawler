---
doc_id: webex-cloud-calling-put-workspaces-workspaceid-features-outgoingpermission
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /workspaces/{workspaceId}/features/outgoingPermission
operation_id: Modify Outgoing Permission Settings for a Workspace
tags: Workspace Call Settings (1/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.374380+00:00
---

# PUT /workspaces/{workspaceId}/features/outgoingPermission

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings (1/2)
**operationId:** `Modify Outgoing Permission Settings for a Workspace`

## Resumen
Modify Outgoing Permission Settings for a Workspace

## Descripción
Modify Outgoing Permission settings for a Place.

Turn on outgoing call settings for this workspace to override the calling settings from the location that are used by default.

This API requires a full or user administrator or location administrator auth token with the `spark-admin:workspaces_write` scope or a user auth token with `spark:workspaces_write` scope can be used to update workspace settings.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Unique identifier for the workspace.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.

## Cuerpo de la petición (application/json)
- `useCustomEnabled` (boolean): When `true`, indicates that this workspace uses the shared control that applies to all outgoing call settings categories when placing outbound calls.
- `useCustomPermissions` (boolean): When `true`, indicates that this workspace uses the specified outgoing calling permissions when placing outbound calls.
- `callingPermissions` (array): Workspace's list of outgoing permissions.
  - `callType` (string): Types for outgoing calls.  * `INTERNAL_CALL` - Internal call type.  * `TOLL_FREE` - Toll Free call type.  * `INTERNATIONAL` - International call type.  * `OPERATOR_ASSISTED` - Operator Assisted call type.  * `CHARGEABLE_DIRECTORY_ASSISTED` - Chargeable Directory assisted call type.  * `SPECIAL_SERVICES_I` - Special Services I call type.  * `SPECIAL_SERVICES_II` - Special Services II call type.  * `PREMIUM_SERVICES_I` - Premium Services I call type.  * `PREMIUM_SERVICES_II` - Premium Services II call type.  * `NATIONAL` - National call type. Valores: INTERNAL_CALL, TOLL_FREE, INTERNATIONAL, OPERATOR_ASSISTED, CHARGEABLE_DIRECTORY_ASSISTED, SPECIAL_SERVICES_I, SPECIAL_SERVICES_II, PREMIUM_SERVICES_I, PREMIUM_SERVICES_II, NATIONAL.
  - `action` (string): Permission for call types.  * `ALLOW` - The call type is allowed.  * `BLOCK` - The call type is blocked.  * `AUTH_CODE` - Access Code action for the specified call type.  * `TRANSFER_NUMBER_1` - Transfer to Auto Transfer Number 1. The answering person can then approve the call and send it through or reject the call.  * `TRANSFER_NUMBER_2` - Transfer to Auto Transfer Number 2. The answering person can then approve the call and send it through or reject the call.  * `TRANSFER_NUMBER_3` - Transfer to Auto Transfer Number 3. The answering person can then approve the call and send it through or reject the call. Valores: ALLOW, BLOCK, AUTH_CODE, TRANSFER_NUMBER_1, TRANSFER_NUMBER_2, TRANSFER_NUMBER_3.
  - `transferEnabled` (boolean): If `true`, allows transfer and forwarding for the call type.

### Ejemplo — petición
```json
{
  "useCustomEnabled": true,
  "useCustomPermissions": true,
  "callingPermissions": [
    {
      "callType": "INTERNAL_CALL",
      "action": "ALLOW",
      "transferEnabled": true
    },
    {
      "callType": "TOLL_FREE",
      "action": "ALLOW",
      "transferEnabled": true
    },
    {
      "callType": "INTERNATIONAL",
      "action": "BLOCK",
      "transferEnabled": false
    },
    {
      "callType": "OPERATOR_ASSISTED",
      "action": "ALLOW",
      "transferEnabled": true
    },
    {
      "callType": "CHARGEABLE_DIRECTORY_ASSISTED",
      "action": "BLOCK",
      "transferEnabled": true
    },
    {
      "callType": "SPECIAL_SERVICES_I",
      "action": "ALLOW",
      "transferEnabled": true
    },
    {
      "callType": "SPECIAL_SERVICES_II",
      "action": "ALLOW",
      "transferEnabled": true
    },
    {
      "callType": "PREMIUM_SERVICES_I",
      "action": "BLOCK",
      "transferEnabled": false
    },
    {
      "callType": "PREMIUM_SERVICES_II",
      "action": "BLOCK",
      "transferEnabled": false
    },
    {
      "callType": "NATIONAL",
      "action": "ALLOW",
      "transferEnabled": true
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/workspaces/<workspaceId>/features/outgoingPermission' \
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