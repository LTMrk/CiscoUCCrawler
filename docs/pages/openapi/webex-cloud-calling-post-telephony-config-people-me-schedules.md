---
doc_id: webex-cloud-calling-post-telephony-config-people-me-schedules
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/people/me/schedules
operation_id: createMySchedule
tags: Call Settings For Me With UserHub Phase2
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.589792+00:00
---

# POST /telephony/config/people/me/schedules

**API:** Webex Cloud Calling
**Área:** Call Settings For Me With UserHub Phase2
**operationId:** `createMySchedule`

## Resumen
Add a User level Schedule for Call Settings

## Descripción
Create a new Schedule for the authenticated user.

Schedules are used to define specific time periods which can be applied to various Call Settings, such as Sequential Ring, or Priority Alert. These call settings perform the defined actions based on the time frame in the schedule, making it more convenient for users to manage their calls.

This API requires a user auth token with a scope of `spark:telephony_config_write`.

## Cuerpo de la petición (application/json)
- `type` (string) (**requerido**): Type of the schedule.  * `businessHours` - Business hours schedule type.  * `holidays` - Holidays schedule type. Valores: businessHours, holidays.
- `name` (string) (**requerido**): Unique name for the schedule.
- `events` (array): List of schedule events.
  - `name` (string) (**requerido**): Name for the event.
  - `startDate` (string) (**requerido**): Start date of event.
  - `endDate` (string) (**requerido**): End date of event.
  - `startTime` (string): Start time of event. Mandatory if the event is not all day.
  - `endTime` (string): End time of event. Mandatory if the event is not all day.
  - `allDayEnabled` (boolean): An indication of whether given event is an all-day event or not. Mandatory if the `startTime` and `endTime` are not defined.
  - `recurrence` (object):
    - `recurForEver` (boolean): Flag to indicate if event will recur forever.
    - `recurEndDate` (string): End date of recurrence.
    - `recurWeekly` (object):
      - `sunday` (boolean) (**requerido**): Frequency of occurrence in weeks and select the day - Sunday.
      - `monday` (boolean): Frequency of occurrence in weeks and select the day - Monday.
      - `tuesday` (boolean): Frequency of occurrence in weeks and select the day - Tuesday.
      - `wednesday` (boolean): Frequency of occurrence in weeks and select the day - Wednesday.
      - `thursday` (boolean): Frequency of occurrence in weeks and select the day - Thursday.
      - `friday` (boolean): Frequency of occurrence in weeks and select the day - Friday.
      - `saturday` (boolean): Frequency of occurrence in weeks and select the day - Saturday.
    - `recurYearlyByDate` (object):
      - `dayOfMonth` (number) (**requerido**): Schedule the event on a specific day of the month.
      - `month` (string) (**requerido**): Schedule the event on a specific month of the year. Valores: JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER.
    - `recurYearlyByDay` (object):
      - `day` (string) (**requerido**): Schedule the event on a specific day. Valores: SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY.
      - `week` (string) (**requerido**): Schedule the event on a specific week. Valores: FIRST, SECOND, THIRD, FOURTH, LAST.
      - `month` (string) (**requerido**): Schedule the event on a specific month. Valores: JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER.

### Ejemplo — petición
```json
{
  "name": "Holiday V2",
  "type": "businessHours",
  "events": [
    {
      "name": "Day_Shift",
      "startDate": "2020-03-18",
      "endDate": "2020-03-18",
      "startTime": "08:00",
      "endTime": "17:00",
      "allDayEnabled": false,
      "recurrence": {
        "recurForEver": true,
        "recurEndDate": "2020-03-18",
        "recurEndOccurrence": 1,
        "recurDaily": {
          "recurInterval": 1
        },
        "recurWeekly": {
          "recurInterval": 1,
          "sunday": false,
          "monday": false,
          "tuesday": false,
          "wednesday": true,
          "thursday": false,
          "friday": false,
          "saturday": false
        }
      }
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/people/me/schedules' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"type": "<type>", "name": "<name>"}'
```

## Respuestas correctas
**200**: Schedule created successfully. Returns the Schedule ID.
- `id` (string): The unique identifier for the criteria.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1VTRVJfU0NIRURVTEUvU0c5c2FXUmhlU0JXTWc"
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs