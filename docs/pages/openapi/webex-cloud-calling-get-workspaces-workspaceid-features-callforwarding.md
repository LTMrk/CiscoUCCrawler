---
doc_id: webex-cloud-calling-get-workspaces-workspaceid-features-callforwarding
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /workspaces/{workspaceId}/features/callForwarding
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.664179+00:00
---

# GET /workspaces/{workspaceId}/features/callForwarding

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings (1/2)
**operationId:** `Retrieve Call Forwarding Settings for a Workspace`

## Resumen
Retrieve Call Forwarding Settings for a Workspace

## Descripción
Retrieve Call Forwarding Settings for a Workspace.

Three types of call forwarding are supported:

+ Always - forwards all incoming calls to the destination you choose.

+ When busy, forwards all incoming calls to the destination you chose while the phone is in use or the person is busy.

+ When no answer, forwarding only occurs when you are away or not answering your phone.

In addition, the Business Continuity feature will send calls to a destination of your choice if your phone is not connected to the network for any reason, such as a power outage, failed Internet connection, or wiring problem.

This API requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:workspaces_read` or a user auth token with `spark:workspaces_read` scope can be used to read workspace settings.

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Unique identifier for the workspace.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.

## Respuestas
- **200**: OK
  - `callForwarding` (object) **(requerido)**:
    - `always` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: "Always" call forwarding is enabled or disabled.
      - `destination` (string): Destination for "Always" call forwarding.
      - `ringReminderEnabled` (boolean) **(requerido)**: If `true`, a brief tone will be played on the person's phone when a call has been forwarded.
      - `destinationVoicemailEnabled` (boolean) **(requerido)**: Enabled or disabled state of sending incoming calls to voicemail when the destination is an internal phone number and that number has the voicemail service enabled.
    - `busy` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: "Busy" call forwarding is enabled or disabled.
      - `destination` (string): Destination for "Busy" call forwarding.
      - `destinationVoicemailEnabled` (boolean) **(requerido)**: Enabled or disabled state of sending incoming calls to voicemail when the destination is an internal phone number and that number has the voicemail service enabled.
    - `noAnswer` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: "No Answer" call forwarding is enabled or disabled.
      - `destination` (string): Destination for "No Answer" call forwarding.
      - `numberOfRings` (number) **(requerido)**: Number of rings before the call will be forwarded if unanswered.
      - `systemMaxNumberOfRings` (number) **(requerido)**: System-wide maximum number of rings allowed for `numberOfRings` setting.
      - `destinationVoicemailEnabled` (boolean) **(requerido)**: Enables and disables sending incoming to destination number's voicemail if the destination is an internal phone number and that number has the voicemail service enabled.
  - `businessContinuity` (object) **(requerido)**:
    - `enabled` (boolean) **(requerido)**: Business Continuity is enabled or disabled.
    - `destination` (string): Destination for Business Continuity.
    - `destinationVoicemailEnabled` (boolean) **(requerido)**: Enabled or disabled state of sending incoming calls to the destination number's voicemail if the destination is an internal phone number and that number has the voicemail service enabled.
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
