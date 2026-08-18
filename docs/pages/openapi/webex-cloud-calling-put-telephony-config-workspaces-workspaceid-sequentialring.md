---
doc_id: webex-cloud-calling-put-telephony-config-workspaces-workspaceid-sequentialring
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/workspaces/{workspaceId}/sequentialRing
operation_id: Modify Sequential Ring Settings for a Workspace
tags: Workspace Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.413770+00:00
---

# PUT /telephony/config/workspaces/{workspaceId}/sequentialRing

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings (2/2)
**operationId:** `Modify Sequential Ring Settings for a Workspace`

## Resumen
Modify Sequential Ring Settings for a Workspace

## Descripción
Modify sequential ring settings for a workspace.

The sequential ring feature enables you to create a list of up to five phone numbers. When the workspace receives incoming calls, these numbers will ring one after another.

This API requires a full, user or location administrator auth token with the `spark-admin:workspaces_write` to update workspace settings.

**NOTE**: This API is only available for professional licensed workspaces.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Unique identifier for the workspace.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.

## Cuerpo de la petición (application/json)
- `enabled` (boolean): When set to `true` sequential ring is enabled.
- `ringBaseLocationFirstEnabled` (boolean): When set to `true`, the webex calling primary line will ring first.
- `baseLocationNumberOfRings` (number): The number of times the primary line will ring. `baseLocationNumberOfRings` must be between 2 and 20, inclusive.
- `continueIfBaseLocationIsBusyEnabled` (boolean): When set to `true` and the primary line is busy, the system redirects calls to the numbers configured for sequential ringing.
- `callsToVoicemailEnabled` (boolean): When set to `true` calls are directed to voicemail.
- `phoneNumbers` (array): A list of up to five phone numbers to which calls will be directed.
  - `phoneNumber` (string): Phone number set as the sequential number.
  - `answerConfirmationRequiredEnabled` (boolean): When set to `true` the called party is required to press 1 on the keypad to receive the call.
  - `numberOfRings` (number): The number of rings to the specified phone number before the call advances to the subsequent number in the sequence or goes to voicemail. `numberOfRings` must be between 2 and 20, inclusive.

### Ejemplo — petición
```json
{
  "enabled": true,
  "ringBaseLocationFirstEnabled": true,
  "baseLocationNumberOfRings": "2",
  "continueIfBaseLocationIsBusyEnabled": true,
  "callsToVoicemailEnabled": true,
  "phoneNumbers": [
    {
      "phoneNumber": "+442071838750",
      "answerConfirmationRequiredEnabled": true,
      "numberOfRings": 3
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/workspaces/<workspaceId>/sequentialRing' \
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