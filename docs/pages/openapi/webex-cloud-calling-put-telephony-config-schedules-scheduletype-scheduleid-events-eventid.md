---
doc_id: webex-cloud-calling-put-telephony-config-schedules-scheduletype-scheduleid-events-eventid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/schedules/{scheduleType}/{scheduleId}/events/{eventId}
operation_id: patchOrganizationScheduleEvent
tags: Org-Wide Schedules
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T14:22:47.329504+00:00
---

# PUT /telephony/config/schedules/{scheduleType}/{scheduleId}/events/{eventId}

**API:** Webex Cloud Calling
**Área:** Org-Wide Schedules
**operationId:** `patchOrganizationScheduleEvent`

## Resumen
Update an Organization Schedule Event

## Descripción
Updates an event in an organization-level schedule and returns its identifier. Omitted fields are left unchanged.

A time schedule establishes a set of times during the day or holidays in the year in which a Webex Calling feature, such as an auto attendant, can perform a specific action.

Managing an organization schedule event requires full administrator access, or delegated organization schedule access with `spark-admin:telephony_config_write` scope.

## Parámetros
- `orgId` [query] (string): Organization from which to retrieve, update, or delete the schedule event.
- `scheduleType` [path] (string) (**requerido**): Type of schedule. * `businessHours` - Business or working hours schedule type. * `holidays` - Holiday schedule type. Valores: businessHours, holidays.
- `scheduleId` [path] (string) (**requerido**): The schedule to which the event belongs.
- `eventId` [path] (string) (**requerido**): The unique identifier of the event to modify

## Cuerpo de la petición (application/json)
- (cualquiera de:)
  - `allDayEnabled` (object):  Valores: True.

### Ejemplo — petición
```json
{
  "name": "Holiday event",
  "startDate": "2026-01-01",
  "endDate": "2026-01-01",
  "allDayEnabled": true,
  "recurrence": {
    "recurForEver": false,
    "recurEndDate": "2026-12-31",
    "recurWeekly": {
      "monday": true
    }
  }
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/schedules/<scheduleType>/<scheduleId>/events/<eventId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: Schedule event updated successfully.
- `id` (string) (**requerido**): Unique identifier of the updated schedule event.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1NDSEVEVUxFX0VWRU5UL1NHOXNhV1JoZVNCbGRtVnVkQT09"
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The schedule or schedule event does not exist.
- **405**: Method Not Allowed: The feature is not supported for this customer.
- **409**: Conflict: The event name already exists.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time.
- **500**: Internal Server Error: Something went wrong on the server.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs