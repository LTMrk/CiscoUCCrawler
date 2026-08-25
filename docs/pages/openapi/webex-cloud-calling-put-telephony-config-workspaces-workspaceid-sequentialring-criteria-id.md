---
doc_id: webex-cloud-calling-put-telephony-config-workspaces-workspaceid-sequentialring-criteria-id
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/workspaces/{workspaceId}/sequentialRing/criteria/{id}
operation_id: Modify Sequential Ring Criteria for a Workspace
tags: Workspace Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.599350+00:00
---

# PUT /telephony/config/workspaces/{workspaceId}/sequentialRing/criteria/{id}

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings (2/2)
**operationId:** `Modify Sequential Ring Criteria for a Workspace`

## Resumen
Modify Sequential Ring Criteria for a Workspace

## Descripción
Modify sequential ring criteria for a workspace.

The sequential ring feature enables you to create a list of up to five phone numbers. When the workspace receives incoming calls, these numbers will ring one after another.
The sequential ring criteria specify settings such as schedule and incoming numbers for which to sequentially ring or not.

This API requires a full, user or location administrator auth token with the `spark-admin:workspaces_write` to update workspace settings.

**NOTE**: This API is only available for professional licensed workspaces.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Unique identifier for the workspace.
- `id` [path] (string) (**requerido**): Unique identifier for the criteria.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.

## Cuerpo de la petición (application/json)
- `scheduleName` (string): Name of the location's schedule which determines when the sequential ring is in effect.
- `scheduleType` (string): This indicates the type of schedule.  * `holidays` - The Schedule is of type `holidays`.  * `businessHours` - The Schedule is of type `businessHours`. Valores: holidays, businessHours.
- `scheduleLevel` (string): This indicates the level of the schedule specified by `scheduleName`.  * `GROUP` - The Schedule specified is of `GROUP` level. Valores: GROUP.
- `callsFrom` (string): This indicates if criteria are applicable for calls from any phone number or selected phone numbers.  * `SELECT_PHONE_NUMBERS` - Sequential ring criteria only applies for selected incoming numbers.  * `ANY_PHONE_NUMBER` - Sequential ring criteria applies for any incoming number. Valores: SELECT_PHONE_NUMBERS, ANY_PHONE_NUMBER.
- `anonymousCallersEnabled` (boolean): When `true` incoming calls from private numbers are allowed. This is only applicable when `callsFrom` is set to `SELECT_PHONE_NUMBERS`.
- `unavailableCallersEnabled` (boolean): When `true` incoming calls from unavailable numbers are allowed. This is only applicable when `callsFrom` is set to `SELECT_PHONE_NUMBERS`.
- `phoneNumbers` (array): When callsFrom is set to `SELECT_PHONE_NUMBERS`, indicates a list of incoming phone numbers for which the criteria apply.
- `ringEnabled` (boolean): When set to `true` sequential ringing is enabled for calls that meet the current criteria. Criteria with `ringEnabled` set to `false` take priority.

### Ejemplo — petición
```json
{
  "scheduleName": "Business Vacation",
  "scheduleType": "holidays",
  "scheduleLevel": "GROUP",
  "callsFrom": "SELECT_PHONE_NUMBERS",
  "anonymousCallersEnabled": true,
  "unavailableCallersEnabled": false,
  "phoneNumbers": [
    "+442071838750",
    "+442071839751"
  ],
  "ringEnabled": true
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/workspaces/<workspaceId>/sequentialRing/criteria/<id>' \
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