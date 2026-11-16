---
doc_id: webex-cloud-calling-get-telephony-config-schedules-scheduletype-scheduleid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/schedules/{scheduleType}/{scheduleId}
operation_id: getOrganizationSchedule
tags: Org-Wide Schedules
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T14:22:47.328759+00:00
---

# GET /telephony/config/schedules/{scheduleType}/{scheduleId}

**API:** Webex Cloud Calling
**Área:** Org-Wide Schedules
**operationId:** `getOrganizationSchedule`

## Resumen
Get an Organization Schedule

## Descripción
Returns an organization-level schedule and its event details.

A time schedule establishes a set of times during the day or holidays in the year in which a Webex Calling feature, such as an auto attendant, can perform a specific action.

Viewing an organization schedule requires full, read-only, or user administrator access, location administrator access, delegated organization schedule access with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Unique identifier of the Organization
- `scheduleType` [path] (string) (**requerido**): Type of the organization schedule Valores: businessHours, holidays.
- `scheduleId` [path] (string) (**requerido**): Unique identifier of the organization schedule.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/schedules/<scheduleType>/<scheduleId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Organization schedule retrieved successfully.
- `id` (string) (**requerido**): Unique identifier of the schedule.
- `type` (string) (**requerido**): Schedule type. * `businessHours` - Business or working hours schedule type. * `holidays` - Holiday schedule type. Valores: businessHours, holidays.
- `level` (string) (**requerido**): Scope of the schedule. * `ORGANIZATION` - The schedule applies across the organization. Valores: ORGANIZATION.
- `name` (string) (**requerido**): Name of the schedule.
- `events` (array) (**requerido**): Events configured for the schedule. Returns an empty array when no events are present.
  - `id` (string) (**requerido**): Unique identifier of the schedule event.
  - `name` (string) (**requerido**): Name of the schedule event.
  - `startDate` (string) (**requerido**): Start date of the event, formatted as `yyyy-MM-dd` when non-empty.
  - `endDate` (string) (**requerido**): End date of the event, formatted as `yyyy-MM-dd` when non-empty.
  - `startTime` (string): Start time of the event in hour and minute form. Omitted for all-day events.
  - `endTime` (string): End time of the event in hour and minute form. Omitted for all-day events.
  - `allDayEnabled` (boolean) (**requerido**): Whether the event spans the full day.
  - `recurrence` (object): Recurrence configuration for the event, when present.
    - (todos de:)
      - `recurForEver` (boolean): Whether the recurrence continues indefinitely.
      - `recurEndDate` (string): End date of the recurrence, formatted as `yyyy-MM-dd` when non-empty.
      - `recurWeekly` (object): Weekly recurrence settings, when present.
        - (todos de:)
      - `recurYearlyByDate` (object): Yearly recurrence by date, when present.
        - (todos de:)
      - `recurYearlyByDay` (object): Yearly recurrence by weekday, when present.
        - (todos de:)

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1NDSEVEVUxFL1FuVnphVzVsYzNNZ1NHOTFjbk09",
  "type": "businessHours",
  "level": "ORGANIZATION",
  "name": "Business Hours",
  "events": []
}
```

## Respuestas de error
- **400**: Bad Request: The schedule type, identifier, or request fields are invalid.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The schedule or organization does not exist.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **415**: Unsupported Media Type: The request was made without a supported media type.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time.
- **500**: Internal Server Error: Something went wrong on the server.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs