---
doc_id: webex-cloud-calling-get-workspaces-workspaceid-features-intercept
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /workspaces/{workspaceId}/features/intercept
operation_id: Read Call Intercept Settings for a Workspace
tags: Workspace Call Settings (1/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.193465+00:00
---

# GET /workspaces/{workspaceId}/features/intercept

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings (1/2)
**operationId:** `Read Call Intercept Settings for a Workspace`

## Resumen
Read Call Intercept Settings for a Workspace

## Descripción
Retrieves Workspace's Call Intercept Settings

The intercept feature gracefully takes a workspace's phone out of service, while providing callers with informative announcements and alternative routing options. Depending on the service configuration, none, some, or all incoming calls to the specified workspace are intercepted. Also depending on the service configuration, outgoing calls are intercepted or rerouted to another location.

This API requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:workspaces_read` or a user auth token with `spark:workspaces_read` scope can be used to read workspace settings.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Unique identifier for the workspace.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.

## Ejemplo de invocación
```bash
curl -X GET '/workspaces/<workspaceId>/features/intercept' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `enabled` (boolean) (**requerido**): `true` if call intercept is enabled.
- `incoming` (object) (**requerido**):
  - `type` (string) (**requerido**): Incoming calls are intercepted.  * `INTERCEPT_ALL` - All incoming calls are intercepted.  * `ALLOW_ALL` - Incoming calls are not intercepted. Valores: INTERCEPT_ALL, ALLOW_ALL.
  - `voicemailEnabled` (boolean) (**requerido**): Enabled or disabled state of sending incoming calls to voicemail when the destination is an internal phone number and that number has the voicemail service enabled.
  - `announcements` (object) (**requerido**):
    - `greeting` (string) (**requerido**): System default message places when incoming calls are intercepted.  * `CUSTOM` - A custom greeting is played when incoming calls are intercepted.  * `DEFAULT` - A System default greeting is played when incoming calls are intercepted. Valores: CUSTOM, DEFAULT.
    - `filename` (string): Filename of the custom greeting; this is an empty string if no custom greeting has been uploaded.
    - `newNumber` (object) (**requerido**):
      - `enabled` (boolean) (**requerido**): If `true`, the caller hears this new number when the call is intercepted.
      - `destination` (string): New number the caller hears announced.
    - `zeroTransfer` (object) (**requerido**):
      - `enabled` (boolean) (**requerido**): If `true`, the caller hears this new number when the call is intercepted.
      - `destination` (string): New number the caller hears announced.
- `outgoing` (object) (**requerido**):
  - `type` (string) (**requerido**): All outgoing calls are intercepted.  * `INTERCEPT_ALL` - Outgoing calls are intercepted.  * `ALLOW_LOCAL_ONLY` - Only non-local calls are intercepted. Valores: INTERCEPT_ALL, ALLOW_LOCAL_ONLY.
  - `transferEnabled` (boolean) (**requerido**): If `true`, allows transfer and forwarding for the call type.
  - `destination` (string): Number to which the outbound call be transferred.

### Ejemplo — respuesta 200
```json
{
  "enabled": true,
  "incoming": {
    "type": "INTERCEPT_ALL",
    "voicemailEnabled": true,
    "announcements": {
      "greeting": "DEFAULT",
      "newNumber": {
        "enabled": true,
        "destination": "+12145551003"
      },
      "zeroTransfer": {
        "enabled": true,
        "destination": "+12145551003"
      }
    }
  },
  "outgoing": {
    "type": "INTERCEPT_ALL",
    "transferEnabled": true,
    "destination": "+12145551003"
  }
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