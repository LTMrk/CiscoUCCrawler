---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-features-personalassistant
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/{personId}/features/personalAssistant
operation_id: getPersonalAssistant
tags: User Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.556446+00:00
---

# GET /telephony/config/people/{personId}/features/personalAssistant

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `getPersonalAssistant`

## Resumen
Get Personal Assistant

## Descripción
Retrieve Personal Assistant details for a specific user.

Personal Assistant is used to manage a user's incoming calls when they are away.

Retrieving Personal Assistant details requires a full, user, or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `personId` [path] (string) (**requerido**): Unique identifier for the person.
- `orgId` [query] (string): Get Personal Assistant details for the organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/<personId>/features/personalAssistant' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `enabled` (boolean) (**requerido**): Toggles feature.
- `presence` (string) (**requerido**): Person's availability.  * `NONE` - User is available.  * `BUSINESS_TRIP` - User is gone for a business trip.  * `GONE_FOR_THE_DAY` - User is gone for the day.  * `LUNCH` - User is gone for lunch.  * `MEETING` - User is gone for a meeting.  * `OUT_OF_OFFICE` - User is out of office.  * `TEMPORARILY_OUT` - User is temporarily out.  * `TRAINING` - User is gone for training.  * `UNAVAILABLE` - User is unavailable.  * `VACATION` - User is gone for vacation. Valores: NONE, BUSINESS_TRIP, GONE_FOR_THE_DAY, LUNCH, MEETING, OUT_OF_OFFICE, TEMPORARILY_OUT, TRAINING, UNAVAILABLE, VACATION.
- `untilDateTime` (string): The date until which personal assistant is active.
- `transferEnabled` (boolean) (**requerido**): If `true`, allows transfer and forwarding for the call type.
- `transferNumber` (string): Number to transfer to.
- `alerting` (string) (**requerido**): Alert type.  * `ALERT_ME_FIRST` - Ring the recipient first.  * `PLAY_RING_REMINDER` - Reminder ring the recipient.  * `NONE` - No alert. Valores: ALERT_ME_FIRST, PLAY_RING_REMINDER, NONE.
- `alertMeFirstNumberOfRings` (number) (**requerido**): Number of rings for alert type: `ALERT_ME_FIRST`; available range is 2-20

### Ejemplo — respuesta 200
```json
{
  "enabled": true,
  "presence": "BUSINESS_TRIP",
  "untilDateTime": "2022-08-24T06:18:31.092Z",
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