---
doc_id: webex-cloud-calling-put-telephony-config-workspaces-workspaceid-priorityalert-criteria-id
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/workspaces/{workspaceId}/priorityAlert/criteria/{id}
operation_id: Modify Priority Alert Criteria for a Workspace
tags: Workspace Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.391013+00:00
---

# PUT /telephony/config/workspaces/{workspaceId}/priorityAlert/criteria/{id}

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings (2/2)
**operationId:** `Modify Priority Alert Criteria for a Workspace`

## Resumen
Modify Priority Alert Criteria for a Workspace

## Descripción
Modify Priority Alert Criteria Settings for a Workspace.

The priority alert feature enables administrators to configure priority alert settings for a professional workspace.
Priority Alert Criteria (Schedules) can also be set up to alert these phones during certain times of the day or days of the week.

This API requires a full, user, or location administrator auth token with the `spark-admin:workspaces_write` scope or a user auth token with a scope of `spark:workspaces_write` to update workspace settings.

**NOTE**: This API is only available for professional licensed workspaces.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Unique identifier for the workspace.
- `id` [path] (string) (**requerido**): Unique identifier for the criteria.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.

## Cuerpo de la petición (application/json)
- `scheduleName` (string): Name of the location's schedule which determines when the priority alert is in effect.
- `scheduleType` (string): * `businessHours` - The Schedule type that specifies the business or working hours during the day.  * `holidays` - The Schedule type that specifies the day when your organization is not open. Valores: businessHours, holidays.
- `scheduleLevel` (string): * `GROUP` - Indicates the schedule level that specifies that criteria is of Group level. Valores: GROUP.
- `callsFrom` (string): * `ANY_PHONE_NUMBER` - The Schedule applies to any phone number.  * `SELECT_PHONE_NUMBERS` - Indicates the schedule applies to select phone number defined in the `phoneNumbers` property. Valores: ANY_PHONE_NUMBER, SELECT_PHONE_NUMBERS.
- `anonymousCallersEnabled` (boolean): When `true`, enables calls from anonymous callers.
- `unavailableCallersEnabled` (boolean): When `true`, enables calls even if callers are unavailable.
- `phoneNumbers` (array): the list of phone numbers that will checked against incoming calls for a match.
- `notificationEnabled` (boolean): When set to `true` priority alerting criteria is enabled for calls that meet the current criteria. Criteria with `notificationEnabled` set to `false` take priority.

### Ejemplo — petición
```json
{
  "scheduleName": "Business Vacation YearEnd",
  "scheduleType": "Holidays",
  "scheduleLevel": "GROUP",
  "callsFrom": "SELECT_PHONE_NUMBERS",
  "anonymousCallersEnabled": true,
  "unavailableCallersEnabled": true,
  "phoneNumbers": [
    "+19064441748",
    "+19186663950"
  ],
  "notificationEnabled": false
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/workspaces/<workspaceId>/priorityAlert/criteria/<id>' \
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