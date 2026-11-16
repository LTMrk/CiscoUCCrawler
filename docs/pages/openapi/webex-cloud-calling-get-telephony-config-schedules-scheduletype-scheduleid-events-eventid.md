---
doc_id: webex-cloud-calling-get-telephony-config-schedules-scheduletype-scheduleid-events-eventid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/schedules/{scheduleType}/{scheduleId}/events/{eventId}
operation_id: getOrganizationScheduleEvent
tags: Org-Wide Schedules
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:50.759160+00:00
---

# GET /telephony/config/schedules/{scheduleType}/{scheduleId}/events/{eventId}

**API:** Webex Cloud Calling
**Área:** Org-Wide Schedules
**operationId:** `getOrganizationScheduleEvent`

## Resumen
Get an Organization Schedule Event

## Descripción
Returns an event from an organization-level schedule.

A time schedule establishes a set of times during the day or holidays in the year in which a Webex Calling feature, such as an auto attendant, can perform a specific action.

Viewing an organization schedule event requires full, read-only, user, or location administrator access, or delegated organization schedule access, with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Organization from which to retrieve, update, or delete the schedule event.
- `scheduleType` [path] (string) (**requerido**): Type of schedule. * `businessHours` - Business or working hours schedule type. * `holidays` - Holiday schedule type. Valores: businessHours, holidays.
- `scheduleId` [path] (string) (**requerido**): Retrieve or modify an event in the schedule with this identifier.
- `eventId` [path] (string) (**requerido**): Identifier of the event to retrieve, modify, or delete.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/schedules/<scheduleType>/<scheduleId>/events/<eventId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Schedule event retrieved successfully.
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
        - `sunday` (boolean) (**requerido**): Whether the event recurs on Sunday.
        - `monday` (boolean) (**requerido**): Whether the event recurs on Monday.
        - `tuesday` (boolean) (**requerido**): Whether the event recurs on Tuesday.
        - `wednesday` (boolean) (**requerido**): Whether the event recurs on Wednesday.
        - `thursday` (boolean) (**requerido**): Whether the event recurs on Thursday.
        - `friday` (boolean) (**requerido**): Whether the event recurs on Friday.
        - `saturday` (boolean) (**requerido**): Whether the event recurs on Saturday.
    - `recurYearlyByDate` (object): Yearly recurrence by date, when present.
      - (todos de:)
        - `dayOfMonth` (integer) (**requerido**): Day of the month on which the event recurs.
        - `month` (string) (**requerido**): Month in which the event recurs. * `JANUARY` - January. * `FEBRUARY` - February. * `MARCH` - March. * `APRIL` - April. * `MAY` - May. * `JUNE` - June. * `JULY` - July. * `AUGUST` - August. * `SEPTEMBER` - September. * `OCTOBER` - October. * `NOVEMBER` - November. * `DECEMBER` - December. Valores: JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER.
    - `recurYearlyByDay` (object): Yearly recurrence by weekday, when present.
      - (todos de:)
        - `day` (string) (**requerido**): Day of the week for the recurrence. * `SUNDAY` - Sunday. * `MONDAY` - Monday. * `TUESDAY` - Tuesday. * `WEDNESDAY` - Wednesday. * `THURSDAY` - Thursday. * `FRIDAY` - Friday. * `SATURDAY` - Saturday. Valores: SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY.
        - `week` (string) (**requerido**): Week of the month for the recurrence. * `FIRST` - First week. * `SECOND` - Second week. * `THIRD` - Third week. * `FOURTH` - Fourth week. * `LAST` - Last week. Valores: FIRST, SECOND, THIRD, FOURTH, LAST.
        - `month` (string) (**requerido**): Month in which the event recurs. * `JANUARY` - January. * `FEBRUARY` - February. * `MARCH` - March. * `APRIL` - April. * `MAY` - May. * `JUNE` - June. * `JULY` - July. * `AUGUST` - August. * `SEPTEMBER` - September. * `OCTOBER` - October. * `NOVEMBER` - November. * `DECEMBER` - December. Valores: JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1NDSEVEVUxFX0VWRU5UL1NHOXNhV1JoZVhNPQ",
  "name": "Holidays",
  "startDate": "2026-01-01",
  "endDate": "2026-01-01",
  "startTime": "09:00",
  "endTime": "17:00",
  "allDayEnabled": false,
  "recurrence": {
    "recurForEver": true,
    "recurWeekly": {
      "sunday": false,
      "monday": true,
      "tuesday": false,
      "wednesday": false,
      "thursday": false,
      "friday": false,
      "saturday": false
    }
  }
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The schedule or schedule event does not exist.
- **405**: Method Not Allowed: The feature is not supported for this customer.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time.
- **500**: Internal Server Error: Something went wrong on the server.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs