---
doc_id: webex-cloud-calling-post-telephony-config-schedules-scheduletype-scheduleid-events-actions-validate-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/schedules/{scheduleType}/{scheduleId}/events/actions/validate/invoke
operation_id: validateOrganizationScheduleEventName
tags: Org-Wide Schedules
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T14:22:47.329191+00:00
---

# POST /telephony/config/schedules/{scheduleType}/{scheduleId}/events/actions/validate/invoke

**API:** Webex Cloud Calling
**Área:** Org-Wide Schedules
**operationId:** `validateOrganizationScheduleEventName`

## Resumen
Validate an Organization Schedule Event Name

## Descripción
Checks whether an event name is available in the specified organization schedule without creating or changing an event.

A time schedule establishes a set of times during the day or holidays in the year in which a Webex Calling feature, such as an auto attendant, can perform a specific action.

Validating an organization schedule event name requires full, read-only, or user administrator access, or delegated organization schedule access, with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `scheduleType` [path] (string) (**requerido**): Type of schedule: `businessHours` or `holidays`.
- `scheduleId` [path] (string) (**requerido**): Unique identifier of the organization schedule to check.
- `orgId` [query] (string): Unique identifier of the Organization

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Event name to check. It must contain 1 to 40 characters. Long. max: 40.

### Ejemplo — petición
```json
{
  "name": "Holiday Event"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/schedules/<scheduleType>/<scheduleId>/events/actions/validate/invoke' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>"}'
```

## Respuestas correctas
**204**: The event name is available for the specified organization schedule.

## Respuestas de error
- **400**: Bad Request: The schedule type or schedule ID is invalid, or the request is missing a valid event name of 1 to 40 characters.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but access is not allowed.
- **404**: Not Found: The URI requested is invalid or the organization does not exist.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: An event with the requested name already exists in the schedule.
- **415**: Unsupported Media Type: The request was made without a supported media type.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time.
- **500**: Internal Server Error: Something went wrong on the server.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs