---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-schedules-scheduletype-scheduleid-events-actions-validate-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/locations/{locationId}/schedules/{scheduleType}/{scheduleId}/events/actions/validate/invoke
operation_id: validateLocationScheduleEventName
tags: Location Call Settings:  Schedules
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:50.746968+00:00
---

# POST /telephony/config/locations/{locationId}/schedules/{scheduleType}/{scheduleId}/events/actions/validate/invoke

**API:** Webex Cloud Calling
**Área:** Location Call Settings:  Schedules
**operationId:** `validateLocationScheduleEventName`

## Resumen
Validate a Location Schedule Event Name

## Descripción
Checks whether an event name is available in the specified location schedule without creating or changing an event.

A time schedule establishes a set of times during the day or holidays in the year in which a feature, for example auto attendants, can perform a specific action.

Validating a location schedule event name requires full, read-only, user or location administrator access, or delegated organization schedule access, with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location containing the schedule to check.
- `scheduleType` [path] (string) (**requerido**): Type of schedule to check. Valores: businessHours, holidays.
- `scheduleId` [path] (string) (**requerido**): Identifier of the schedule to check.
- `orgId` [query] (string): Target organization for the schedule check.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Event name to check. It must contain at least one non-whitespace character. Long. max: 40.

### Ejemplo — petición
```json
{
  "name": "Holiday Event"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations/<locationId>/schedules/<scheduleType>/<scheduleId>/events/actions/validate/invoke' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>"}'
```

## Respuestas correctas
**204**: The event name is available for the specified location schedule.

## Respuestas de error
- **400**: Bad Request: The schedule type is invalid, or the request is missing a non-blank event name.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but access is not allowed.
- **404**: Not Found: The location or schedule does not exist.
- **409**: Conflict: An event with the requested name already exists in the schedule.
- **415**: Unsupported Media Type: The request was made without a supported media type.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time.
- **500**: Internal Server Error: Something went wrong on the server.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs