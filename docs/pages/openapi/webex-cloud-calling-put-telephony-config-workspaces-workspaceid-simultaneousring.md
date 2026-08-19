---
doc_id: webex-cloud-calling-put-telephony-config-workspaces-workspaceid-simultaneousring
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/workspaces/{workspaceId}/simultaneousRing
operation_id: Modify Simultaneous Ring Settings for a Workspace
tags: Workspace Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.202189+00:00
---

# PUT /telephony/config/workspaces/{workspaceId}/simultaneousRing

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings (2/2)
**operationId:** `Modify Simultaneous Ring Settings for a Workspace`

## Resumen
Modify Simultaneous Ring Settings for a Workspace

## Descripción
Modify Simultaneous Ring Settings for a Workspace.

The Simultaneous Ring feature allows you to configure the workspace phones of your choice to ring simultaneously.
Schedules can also be set up to ring these phones during certain times of the day or days of the week.

This API requires a full, user or location administrator auth token with the `spark-admin:workspaces_write` scope or a user auth token with a scope of `spark:workspaces_write` to update workspace settings.

**NOTE**: This API is only available for professional licensed workspaces.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Unique identifier for the workspace.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.

## Cuerpo de la petición (application/json)
- `enabled` (boolean): Simultaneous Ring is enabled or not.
- `doNotRingIfOnCallEnabled` (boolean): When set to `true`, the configured phone numbers won't ring when on a call.
- `phoneNumbers` (array): Enter up to 10 phone numbers to ring simultaneously when a workspace phone receives an incoming call.
  - `phoneNumber` (string) (**requerido**): Phone number set as the sequential number.
  - `answerConfirmationRequiredEnabled` (boolean) (**requerido**): When set to `true` the called party is required to press 1 on the keypad to receive the call.
- `criteriasEnabled` (boolean) (**requerido**): When `true`, enables the selected schedule for simultaneous ring.

### Ejemplo — petición
```json
{
  "enabled": false,
  "doNotRingIfOnCallEnabled": false,
  "phoneNumbers": [
    {
      "phoneNumber": "+19075552859",
      "answerConfirmationRequiredEnabled": false
    }
  ],
  "criteriasEnabled": false
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/workspaces/<workspaceId>/simultaneousRing' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"criteriasEnabled": true}'
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