---
doc_id: webex-cloud-calling-put-workspaces-workspaceid-features-monitoring
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /workspaces/{workspaceId}/features/monitoring
operation_id: modifyMonitoringSettingsWorkspace
tags: Workspace Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.403339+00:00
---

# PUT /workspaces/{workspaceId}/features/monitoring

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings
**operationId:** `modifyMonitoringSettingsWorkspace`

## Resumen
Modify Monitoring Settings for a Workspace

## Descripción
Modifies the monitoring settings of the workspace.
Monitors the line status of specified people, places, virtual lines or call park extension. The line status indicates if a person, place or virtual line is on a call and if a call has been parked on that extension. Maximum 50 monitored elements.

This API requires a full or user administrator or location administrator auth token with the `spark-admin:workspaces_write` scope or a user auth token with `spark:workspaces_write` scope can be used to update workspace settings.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Unique identifier for the workspace.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.

## Cuerpo de la petición (application/json)
- `enableCallParkNotification` (boolean): Call park notification is enabled or disabled.
- `monitoredElements` (array): Array of monitored elements. Maximum 50 elements.
  - `id` (string): The identifier of the monitored element.
  - `type` (string): The type of the monitored element.  * `MEMBER` - Monitored element is a person, place, or virtual line.  * `CALL_PARK_EXTENSION` - Monitored element is a call park extension.  * `SPEED_DIAL` - Monitored element is a speed dial. Valores: MEMBER, CALL_PARK_EXTENSION, SPEED_DIAL.
  - `lineKeyLabel` (string): Customizable line key label for speed dial.
  - `phoneNumber` (string): Phone number for the speed dial.

### Ejemplo — petición
```json
{
  "enableCallParkNotification": true,
  "monitoredElements": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xYjhkYjA4YS0wY2JlLTRlZDctOThmMy05ZThlZjBhOGI2N2E",
      "type": "MEMBER"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUEFSS19FWFRFTlNJT04vZmJjNzlkNzAtMjM5Zi00YjIyLWE2YTAtZjAwNWFmOGNlMjA0",
      "type": "CALL_PARK_EXTENSION"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUEFSS19FWFRFTlNJT04vZmJjNzlkNzAtMjM5Zi00YjIyLWE2YTAtZjAwNWFmOGNlMjA0",
      "type": "SPEED_DIAL"
    },
    {
      "lineKeyLabel": "Sr Manager",
      "phoneNumber": "+19075552859"
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/workspaces/<workspaceId>/features/monitoring' \
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