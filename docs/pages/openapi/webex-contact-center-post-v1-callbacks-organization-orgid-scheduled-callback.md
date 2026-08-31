---
doc_id: webex-contact-center-post-v1-callbacks-organization-orgid-scheduled-callback
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/callbacks/organization/{orgId}/scheduled-callback
operation_id: ScheduleCallback
tags: Callbacks
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.749372+00:00
---

# POST /v1/callbacks/organization/{orgId}/scheduled-callback

**API:** Webex Contact Center
**Área:** Callbacks
**operationId:** `ScheduleCallback`

## Resumen
Schedule a Callback

## Descripción
Creates a new callback request for a customer. Authorization requires the cjp:user scope. The callback default endpoint (EP) and default ANI must be configured as mandatory settings to successfully make API calls.

## Parámetros
- `orgId` [path] (string) (**requerido**): The organization ID for which the callback is being scheduled. This should be a valid UUID.

## Cuerpo de la petición (application/json)
- `customerName` (string) (**requerido**): Name of the Customer for which callback has to be scheduled. Max customer name length should be 250 character
- `callbackNumber` (string) (**requerido**): Customer's phone number for the callback. Allows an optional country code followed by digits (0-9) and the special characters: space, hyphen -, parentheses ( and ), and period ., ensuring the total length is between 7 and 15 characters.
- `timezone` (string) (**requerido**): Valid IANA timezone name
- `scheduleDate` (string/date) (**requerido**): Scheduled date in ISO-8601 (YYYY-MM-DD) format. This must be a valid date in local time zone and within 31 days from current date
- `startTime` (string/time) (**requerido**): Scheduled start time in ISO-8601 (HH:mm:ss) format. Start time must be at least 30 minutes in the future from current time.
- `endTime` (string/time) (**requerido**): Scheduled end time in ISO-8601 (HH:mm:ss) format. End time must be at least 30 minutes after the startTime and must not exceed 8 hours after startTime.
- `queueId` (string) (**requerido**): Unique identifier for the queue to which the callback is associated.
- `callbackReason` (string): Reason for the callback request. This is optional and can be used to provide additional context.
- `sourceInteraction` (string/uuid): Source interaction ID for the callback. This is optional and can be used to link the callback to a specific interaction. This should be a valid UUID.
- `assigneeAgent` (string/uuid): The unique identifier of the specific agent (CI userId), who should be assigned to handle the callback. This field is optional and is primarily used for personal callbacks.

## Ejemplo de invocación
```bash
curl -X POST '/v1/callbacks/organization/<orgId>/scheduled-callback' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"customerName": "<customerName>", "callbackNumber": "<callbackNumber>", "timezone": "<timezone>", "scheduleDate": "<scheduleDate>", "startTime": "<startTime>", "endTime": "<endTime>"}'
```

## Respuestas correctas
**201**: Callback successfully scheduled.

## Respuestas de error
- **400**: Bad Request
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **429**: Too Many Requests
- **500**: Internal Server Error
- **503**: Service Unavailable

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs