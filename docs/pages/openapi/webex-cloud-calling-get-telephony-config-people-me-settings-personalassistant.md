---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-personalassistant
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/settings/personalAssistant
operation_id: getPersonalAssistantSettings
tags: Call Settings For Me Phase 5
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.953568+00:00
---

# GET /telephony/config/people/me/settings/personalAssistant

**API:** Webex Cloud Calling
**Área:** Call Settings For Me Phase 5
**operationId:** `getPersonalAssistantSettings`

## Resumen
Get Personal Assistant Settings

## Descripción
Retrieve personal assistant settings for a person. The personal assistant feature allows users to configure an automated attendant that can handle incoming calls when they are unavailable, including presence-based routing and call transfer options.

Personal Assistant is a feature of Webex Calling that helps manage incoming calls based on the user's availability status.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/settings/personalAssistant' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `enabled` (boolean) (**requerido**): Enable/Disable the personal assistant feature.
- `presence` (string): Presence status that triggers the personal assistant. Valores: BUSINESS_TRIP, GONE_FOR_THE_DAY, LUNCH, MEETING, OUT_OF_OFFICE, TEMPORARILY_OUT, TRAINING, UNAVAILABLE, VACATION.
- `untilDateTime` (string/date-time): Date and time until which the personal assistant is active (ISO 8601 format).
- `transferEnabled` (boolean): Enable/Disable call transfer when personal assistant is active.
- `transferNumber` (string): Phone number to transfer calls to when transfer is enabled.
- `alerting` (string): Alerting behavior for incoming calls when personal assistant is active. Possible values: ALERT_ME_FIRST - Ring the user's phone first before the personal assistant takes over. PLAY_RING_REMINDER - Play a ring reminder to the user. NONE - No alerting. Valores: ALERT_ME_FIRST, PLAY_RING_REMINDER, NONE.
- `alertMeFirstNumberOfRings` (integer): Number of rings before transferring the call when alerting is set to ALERT_ME_FIRST.

### Ejemplo — respuesta 200
```json
{
  "enabled": true,
  "presence": "OUT_OF_OFFICE",
  "untilDateTime": "2026-03-28T14:30:00Z",
  "transferEnabled": true,
  "transferNumber": "+14126525012",
  "alerting": "ALERT_ME_FIRST",
  "alertMeFirstNumberOfRings": 3
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