---
doc_id: webex-contact-center-post-v1-callbacks-organization-orgid-scheduled-callback
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/callbacks/organization/{orgId}/scheduled-callback
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.963024+00:00
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
- `orgId` [path] (string) **(requerido)**: The organization ID for which the callback is being scheduled. This should be a valid UUID.

## Cuerpo de la petición (application/json)
- `customerName` (string) **(requerido)**: Name of the Customer for which callback has to be scheduled. Max customer name length should be 250 character
- `callbackNumber` (string) **(requerido)**: Customer's phone number for the callback. Allows an optional country code followed by digits (0-9) and the special characters: space, hyphen -, parentheses ( and ), and period ., ensuring the total length is between 7 and 15 characters.
- `timezone` (string) **(requerido)**: Valid IANA timezone name
- `scheduleDate` (string) **(requerido)**: Scheduled date in ISO-8601 (YYYY-MM-DD) format. This must be a valid date in local time zone and within 31 days from current date
- `startTime` (string) **(requerido)**: Scheduled start time in ISO-8601 (HH:mm:ss) format. Start time must be at least 30 minutes in the future from current time.
- `endTime` (string) **(requerido)**: Scheduled end time in ISO-8601 (HH:mm:ss) format. End time must be at least 30 minutes after the startTime and must not exceed 8 hours after startTime.
- `queueId` (string) **(requerido)**: Unique identifier for the queue to which the callback is associated.
- `callbackReason` (string): Reason for the callback request. This is optional and can be used to provide additional context.
- `sourceInteraction` (string): Source interaction ID for the callback. This is optional and can be used to link the callback to a specific interaction. This should be a valid UUID.
- `assigneeAgent` (string): The unique identifier of the specific agent (CI userId), who should be assigned to handle the callback. This field is optional and is primarily used for personal callbacks.

## Respuestas
- **201**: Callback successfully scheduled.
- **400**: Bad Request
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **429**: Too Many Requests
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
