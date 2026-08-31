---
doc_id: webex-cloud-calling-get-telephony-config-workspaces-workspaceid-simultaneousring
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/workspaces/{workspaceId}/simultaneousRing
operation_id: Retrieve Simultaneous Ring Settings for a Workspace
tags: Workspace Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.385849+00:00
---

# GET /telephony/config/workspaces/{workspaceId}/simultaneousRing

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings (2/2)
**operationId:** `Retrieve Simultaneous Ring Settings for a Workspace`

## Resumen
Retrieve Simultaneous Ring Settings for a Workspace

## Descripción
Retrieve Simultaneous Ring Settings for a Workspace.

The Simultaneous Ring feature allows you to configure your office phone and other phones of your choice to ring simultaneously.
Schedules can also be set up to ring these phones during certain times of the day or days of the week.

This API requires a full, read-only or location administrator auth token with a scope of `spark-admin:workspaces_read` or a user auth token with a scope of `spark:workspaces_read` to read workspace settings.

**NOTE**: This API is only available for professional licensed workspaces.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Unique identifier for the workspace.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/workspaces/<workspaceId>/simultaneousRing' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `enabled` (boolean) (**requerido**): Simultaneous Ring is enabled or not.
- `doNotRingIfOnCallEnabled` (boolean) (**requerido**): When set to `true`, the configured phone numbers won't ring when on a call.
- `phoneNumbers` (array): Enter up to 10 phone numbers to ring simultaneously when a workspace phone receives an incoming call.
  - `phoneNumber` (string) (**requerido**): Phone number set as the sequential number.
  - `answerConfirmationRequiredEnabled` (boolean) (**requerido**): When set to `true` the called party is required to press 1 on the keypad to receive the call.
- `criteria` (array): A list of criteria specifying conditions when simultaneous ring is in effect.
  - `id` (string) (**requerido**): Unique identifier for criteria.
  - `scheduleName` (string): Name of the location's schedule which determines when the simultaneous ring is in effect.
  - `source` (string) (**requerido**): * `ALL_NUMBERS` - Criteria applies to all incoming numbers.  * `SPECIFIC_NUMBERS` - Criteria applies only for specific incoming numbers. Valores: ALL_NUMBERS, SPECIFIC_NUMBERS.
  - `ringEnabled` (boolean) (**requerido**): When set to `true` simultaneous ringing is enabled for calls that meet the current criteria. Criteria with `ringEnabled` set to `false` take priority.
- `criteriasEnabled` (boolean) (**requerido**): When `true`, enables the selected schedule for simultaneous ring.

### Ejemplo — respuesta 200
```json
{
  "enabled": true,
  "doNotRingIfOnCallEnabled": true,
  "phoneNumbers": [
    {
      "phoneNumber": "+19075552859",
      "answerConfirmationRequiredEnabled": true
    },
    {
      "phoneNumber": "+19186663950",
      "answerConfirmationRequiredEnabled": false
    }
  ],
  "criteria": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0NSSVRFUklBLzg2NTAxZDFlLTg1MWMtNDgwYi1hZmE2LTA5MTU4NzQ3NzdmZQ",
      "scheduleName": "Business Vacation",
      "source": "ALL_NUMBERS",
      "ringEnabled": true
    }
  ],
  "criteriasEnabled": true
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