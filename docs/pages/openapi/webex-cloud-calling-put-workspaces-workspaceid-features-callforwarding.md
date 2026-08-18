---
doc_id: webex-cloud-calling-put-workspaces-workspaceid-features-callforwarding
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /workspaces/{workspaceId}/features/callForwarding
operation_id: Modify Call Forwarding Settings for a Workspace
tags: Workspace Call Settings (1/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.402043+00:00
---

# PUT /workspaces/{workspaceId}/features/callForwarding

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings (1/2)
**operationId:** `Modify Call Forwarding Settings for a Workspace`

## Resumen
Modify Call Forwarding Settings for a Workspace

## Descripción
Modify call forwarding settings for a Workspace.

Three types of call forwarding are supported:

+ Always - forwards all incoming calls to the destination you choose.

+ When busy, forwards all incoming calls to the destination you chose while the phone is in use or the person is busy.

+ When no answer, forwarding only occurs when you are away or not answering your phone.

In addition, the Business Continuity feature will send calls to a destination of your choice if your phone is not connected to the network for any reason, such as a power outage, failed Internet connection, or wiring problem.

This API requires a full or user administrator or location administrator auth token with the `spark-admin:workspaces_write` scope or a user auth token with `spark:workspaces_write` scope can be used to update workspace settings.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Unique identifier for the workspace.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.

## Cuerpo de la petición (application/json)
- `callForwarding` (object) (**requerido**):
  - `always` (object) (**requerido**):
    - `enabled` (boolean) (**requerido**): "Always" call forwarding is enabled or disabled.
    - `destination` (string): Destination for "Always" call forwarding.
    - `ringReminderEnabled` (boolean) (**requerido**): If `true`, a brief tone will be played on the person's phone when a call has been forwarded.
    - `destinationVoicemailEnabled` (boolean) (**requerido**): Enabled or disabled state of sending incoming calls to voicemail when the destination is an internal phone number and that number has the voicemail service enabled.
  - `busy` (object):
    - `enabled` (boolean) (**requerido**): "Busy" call forwarding is enabled or disabled.
    - `destination` (string): Destination for "Busy" call forwarding.
    - `destinationVoicemailEnabled` (boolean) (**requerido**): Enabled or disabled state of sending incoming calls to voicemail when the destination is an internal phone number and that number has the voicemail service enabled.
  - `noAnswer` (object):
    - `enabled` (boolean): "No Answer" call forwarding is enabled or disabled.
    - `destination` (string): Destination for "No Answer" call forwarding. If enabled true, destination is required.
    - `numberOfRings` (number): Number of rings before the call will be forwarded if unanswered. `numberOfRings` must be between 2 and 20, inclusive.
    - `systemMaxNumberOfRings` (number): Max number of rings before the call will be forwarded if unanswered.
    - `destinationVoicemailEnabled` (boolean): Enables and disables sending incoming to destination number's voicemail if the destination is an internal phone number and that number has the voicemail service enabled.
- `businessContinuity` (object) (**requerido**):
  - `enabled` (boolean) (**requerido**): Business Continuity is enabled or disabled.
  - `destination` (string): Destination for Business Continuity.
  - `destinationVoicemailEnabled` (boolean) (**requerido**): Enabled or disabled state of sending incoming calls to the destination number's voicemail if the destination is an internal phone number and that number has the voicemail service enabled.

### Ejemplo — petición
```json
{
  "callForwarding": {
    "always": {
      "enabled": false,
      "destination": "",
      "ringReminderEnabled": false,
      "destinationVoicemailEnabled": false
    },
    "busy": {
      "enabled": true,
      "destination": "+17084004987",
      "destinationVoicemailEnabled": true
    },
    "noAnswer": {
      "enabled": true,
      "destination": "+12815550001",
      "numberOfRings": 2,
      "destinationVoicemailEnabled": false
    }
  },
  "businessContinuity": {
    "enabled": false,
    "destination": "",
    "destinationVoicemailEnabled": false
  }
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/workspaces/<workspaceId>/features/callForwarding' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"callForwarding": {}, "businessContinuity": {}}'
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