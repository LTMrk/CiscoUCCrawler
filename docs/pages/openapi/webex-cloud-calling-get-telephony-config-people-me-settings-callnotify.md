---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-callnotify
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/settings/callNotify
operation_id: getMyCallNotifySettings
tags: Call Settings For Me With UserHub Phase2
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.970966+00:00
---

# GET /telephony/config/people/me/settings/callNotify

**API:** Webex Cloud Calling
**Área:** Call Settings For Me With UserHub Phase2
**operationId:** `getMyCallNotifySettings`

## Resumen
Get Call Notify Settings for User

## Descripción
Get Call Notify Settings for the authenticated user.

Call Notify allows you to set up a unique ringtone based on predefined criteria. This is helpful, when the user wants to be quickly notified that a specific phone number is calling.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/settings/callNotify' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Call Notify Settings retrieved for the authenticated user.
- `enabled` (boolean): Indicates whether the call notify feature is enabled for the user.
- `emailAddress` (string): Email Address to which call notifications to be received.
- `criteria` (array): List of Call Notify Criteria configured by the user.
  - `id` (string): Unique identifier for the call notify criteria.
  - `scheduleName` (string): Name of the schedule associated with the criteria.
  - `source` (string): Type of the source.  * `ALL_NUMBERS` - User wants to be notified for calls from Any Phone Number.  * `SPECIFIC_NUMBERS` - User wants to be notified for calls from Select Phone Numbers. Valores: ALL_NUMBERS, SPECIFIC_NUMBERS.
  - `notificationEnabled` (boolean): Determines whether call notify is applied for calls matching this criteria. If `true`, call notification is applied. If `false`, this criteria acts as a 'Don't Notify Me' rule, preventing call notification. Criteria with `notificationEnabled` set to `false` (Don't Notify Me) take precedence over criteria with `notificationEnabled` set to `true` (Notify Me).

### Ejemplo — respuesta 200
```json
{
  "emailAddress": "callnotify@example.com",
  "enabled": true,
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