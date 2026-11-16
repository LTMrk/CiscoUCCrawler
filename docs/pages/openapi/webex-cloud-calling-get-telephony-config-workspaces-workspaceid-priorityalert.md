---
doc_id: webex-cloud-calling-get-telephony-config-workspaces-workspaceid-priorityalert
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/workspaces/{workspaceId}/priorityAlert
operation_id: retrievePriorityAlertSettingsForAWorkspace
tags: Workspace Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:50.867882+00:00
---

# GET /telephony/config/workspaces/{workspaceId}/priorityAlert

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings (2/2)
**operationId:** `retrievePriorityAlertSettingsForAWorkspace`

## Resumen
Retrieve Priority Alert Settings for a Workspace

## Descripción
Retrieve Priority Alert Settings for a Workspace.

The priority alert feature enables administrators to configure priority alert settings for a professional workspace.

This API requires a full, user, or location administrator auth token with a scope of `spark-admin:workspaces_read` or a user auth token with a scope of `spark:workspaces_read` to read workspace settings.

**NOTE**: This API is only available for professional licensed workspaces.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Unique identifier for the workspace.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/workspaces/<workspaceId>/priorityAlert' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Priority Alert Settings retrieved successfully for the workspace.
- `enabled` (boolean) (**requerido**): `true` if the Priority Alert feature is enabled.
- `criteria` (array) (**requerido**): A list of criteria specifying conditions when priority alert is in effect.
  - `id` (string) (**requerido**): Unique identifier for criteria.
  - `scheduleName` (string) (**requerido**): Name of the schedule which determines when the priority alert is in effect.
  - `source` (string) (**requerido**): If criteria are applicable for calls from any phone number or specific phone number. `ALL_NUMBERS` is equivalent to `ANY_PHONE_NUMBER` and `SPECIFIC_NUMBERS` is equivalent to `SELECT_PHONE_NUMBERS` in the criteria detail APIs.  * `ALL_NUMBERS` - Indicates that priority alert criteria apply for all incoming external numbers.  * `SPECIFIC_NUMBERS` - Indicates priority alert criteria only apply to specific incoming numbers.  * `ANY_INTERNAL` - Indicates that priority alert criteria apply for any internal call. Valores: ALL_NUMBERS, SPECIFIC_NUMBERS, ANY_INTERNAL.
  - `notificationEnabled` (boolean) (**requerido**): Determines whether priority alerting is applied for calls matching this criteria. If `true`, priority alerting is applied. If `false`, this criteria acts as a 'Don't Alert' rule, preventing priority alerting. Criteria with `notificationEnabled` set to `false` (Don't Alert) take precedence over criteria with `notificationEnabled` set to `true` (Alert).
  - `ringPattern` (string): Distinctive ringtone pattern for incoming calls matching this criteria.  * `NORMAL` - Standard ring pattern.  * `LONG_LONG` - Two long rings.  * `SHORT_LONG_SHORT` - Short ring, long ring, short ring pattern.  * `SHORT_SHORT_LONG` - Two short rings followed by one long ring. Valores: NORMAL, LONG_LONG, SHORT_LONG_SHORT, SHORT_SHORT_LONG.

### Ejemplo — respuesta 200
```json
{
  "enabled": true,
  "criteria": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0NSSVRFUklBLzg2NTAxZDFlLTg1MWMtNDgwYi1hZmE2LTA5MTU4NzQ3NzdmZQ",
      "scheduleName": "Business Vacation",
      "source": "ALL_NUMBERS",
      "notificationEnabled": true,
      "ringPattern": "LONG_LONG"
    }
  ]
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