---
doc_id: webex-cloud-calling-post-telephony-config-schedules-scheduletype-scheduleid-events
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/schedules/{scheduleType}/{scheduleId}/events
operation_id: createOrganizationScheduleEvent
tags: Org-Wide Schedules
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T14:22:47.329605+00:00
---

# POST /telephony/config/schedules/{scheduleType}/{scheduleId}/events

**API:** Webex Cloud Calling
**Área:** Org-Wide Schedules
**operationId:** `createOrganizationScheduleEvent`

## Resumen
Create an Event in an Organization Schedule

## Descripción
Creates an event in an organization-level schedule and returns its identifier.

A time schedule establishes a set of times during the day or holidays in the year in which a Webex Calling feature, such as an auto attendant, can perform a specific action.

Creating an organization schedule event requires full administrator access or delegated organization schedule access with `spark-admin:telephony_config_write` scope.

## Parámetros
- `orgId` [query] (string): Organization to which the schedule belongs.
- `scheduleType` [path] (string) (**requerido**): Type of schedule. * `businessHours` - Business or working hours schedule type. * `holidays` - Holiday schedule type. Valores: businessHours, holidays.
- `scheduleId` [path] (string) (**requerido**): Identifier of the organization schedule receiving the event.

## Cuerpo de la petición (application/json)
- (uno de:)
  - `allDayEnabled` (object):  Valores: False.
  - `allDayEnabled` (object) (**requerido**):  Valores: True.

### Ejemplo — petición
```json
{
  "name": "Holidays",
  "startDate": "2026-01-01",
  "endDate": "2026-01-01",
  "allDayEnabled": true
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/schedules/<scheduleType>/<scheduleId>/events' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "startDate": "<startDate>", "endDate": "<endDate>"}'
```

## Respuestas correctas
**201**: Schedule event created successfully.
- `id` (string) (**requerido**): Unique identifier of the created schedule event.

### Ejemplo — respuesta 201
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1NDSEVEVUxFX0VWRU5UL1NHOXNhV1JoZVhNPQ"
}
```

## Respuestas de error
- **400**: Bad Request: Required event fields are missing or an event, schedule type, date, time, or recurrence value is invalid.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but access is not allowed.
- **404**: Not Found: The schedule does not exist.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: An event with the same name already exists.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time.
- **500**: Internal Server Error: Something went wrong on the server.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs