---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-priorityalert
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/settings/priorityAlert
operation_id: getMyPriorityAlertSettings
tags: Call Settings For Me With UserHub Phase2
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.157317+00:00
---

# GET /telephony/config/people/me/settings/priorityAlert

**API:** Webex Cloud Calling
**Área:** Call Settings For Me With UserHub Phase2
**operationId:** `getMyPriorityAlertSettings`

## Resumen
Get Priority Alert Settings

## Descripción
Get Priority Alert Settings for the authenticated user.

Priority alert allows you to set up a unique ringtone based on predefined criteria. This is helpful, when the user wants to be quickly notified that a specific phone number is calling.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/settings/priorityAlert' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Priority Alert Settings retrieved successfully for the authenticated user.
- `enabled` (boolean) (**requerido**): `true` if the Priority Alert feature is enabled.
- `criteria` (array): A list of criteria specifying conditions when priority alert is in effect.
  - `id` (string) (**requerido**): Unique identifier for criteria.
  - `scheduleName` (string): Name of the location's schedule which determines when the priority alert is in effect.
  - `source` (string) (**requerido**): If criteria are applicable for calls from any phone number or specific phone number.  * `ALL_NUMBERS` - Indicates that priority alert criteria apply for all incoming numbers.  * `SPECIFIC_NUMBERS` - Indicates priority alert criteria only apply to specific incoming numbers. Valores: ALL_NUMBERS, SPECIFIC_NUMBERS.
  - `notificationEnabled` (boolean) (**requerido**): When set to `true` notification is enabled for calls that meet the current criteria. Criteria with `notificationEnabled` set to `false` take priority.

### Ejemplo — respuesta 200
```json
{
  "enabled": false,
  "criteria": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0NSSVRFUklBL1oxNzU0MzgzODQzNTA5NzY",
      "scheduleName": "CustomHoliday(Group)",
      "source": "ALL_NUMBERS",
      "notificationEnabled": false
    }
  ]
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served.
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