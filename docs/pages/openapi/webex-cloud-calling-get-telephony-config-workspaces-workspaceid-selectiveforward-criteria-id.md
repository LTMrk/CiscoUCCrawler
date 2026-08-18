---
doc_id: webex-cloud-calling-get-telephony-config-workspaces-workspaceid-selectiveforward-criteria-id
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/workspaces/{workspaceId}/selectiveForward/criteria/{id}
operation_id: Retrieve Selective Forward Criteria for a Workspace
tags: Workspace Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.418765+00:00
---

# GET /telephony/config/workspaces/{workspaceId}/selectiveForward/criteria/{id}

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings (2/2)
**operationId:** `Retrieve Selective Forward Criteria for a Workspace`

## Resumen
Retrieve Selective Forward Criteria for a Workspace

## Descripción
Retrieve Selective Forward Criteria Settings for a Workspace.

With the Selective Forward feature, you can forward calls at specific times from specific callers. This setting takes precedence over call forwarding.
Schedules can also be set up for this feature during certain times of the day or days of the week.

This API requires a full, read-only or location administrator auth token with a scope of `spark-admin:workspaces_read` or a user auth token with a scope of `spark:workspaces_read` to read workspace settings.

**NOTE**: This API is only available for professional licensed workspaces.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Unique identifier for the workspace.
- `id` [path] (string) (**requerido**): Unique identifier for the criteria.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/workspaces/<workspaceId>/selectiveForward/criteria/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Unique identifier for criteria.
- `forwardToPhoneNumber` (string): Phone number to forward calls to during this schedule.
- `sendToVoicemailEnabled` (boolean): Enables forwarding for all calls to voicemail. This option is only available for internal phone numbers or extensions.
- `scheduleName` (string): Name of the location's schedule which determines when the selective forward is in effect.
- `scheduleType` (string): * `businessHours` - The Schedule type that specifies the business or working hours during the day.  * `holidays` - The Schedule type that specifies the day when your organization is not open. Valores: businessHours, holidays.
- `scheduleLevel` (string): * `GROUP` - Indicates the schedule level that specifies that criteria is of Group level. Valores: GROUP.
- `callsFrom` (string) (**requerido**): * `ANY_PHONE_NUMBER` - The schedule applies to any phone number.  * `SELECT_PHONE_NUMBERS` - The schedule applies to select phone number defined in the `phoneNumbers` property.  * `ANY_INTERNAL` - The schedule applies to any internal phone number.  * `ANY_EXTERNAL` - The schedule applies to any external phone number. Valores: ANY_PHONE_NUMBER, SELECT_PHONE_NUMBERS, ANY_INTERNAL, ANY_EXTERNAL.
- `anonymousCallersEnabled` (boolean): When `true`, enables selective forward to calls from anonymous callers.
- `unavailableCallersEnabled` (boolean): When `true`, enables selective forward to calls if the callers are unavailable.
- `numbers` (array): List of phone numbers checked against incoming calls for a match.
- `forwardEnabled` (boolean): Indicates whether the calls, that fit within these parameters, will be forwarded (if forwardEnabled = `true`) or not (if forwardEnabled = `false`).

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0NSSVRFUklBLzg2NTAxZDFlLTg1MWMtNDgwYi1hZmE2LTA5MTU4NzQ3NzdmZQ",
  "forwardToPhoneNumber": "+1934898988",
  "sendToVoicemailEnabled": true,
  "scheduleName": "Business Vacation",
  "scheduleType": "holidays",
  "scheduleLevel": "GROUP",
  "callsFrom": "ANY_PHONE_NUMBER",
  "anonymousCallersEnabled": true,
  "unavailableCallersEnabled": true,
  "numbers": [
    "+19075552859",
    "+19186663950"
  ],
  "forwardEnabled": true
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