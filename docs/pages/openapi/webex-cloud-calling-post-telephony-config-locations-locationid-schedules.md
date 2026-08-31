---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-schedules
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/locations/{locationId}/schedules
operation_id: Create a Schedule
tags: Location Call Settings:  Schedules
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.305475+00:00
---

# POST /telephony/config/locations/{locationId}/schedules

**API:** Webex Cloud Calling
**Área:** Location Call Settings:  Schedules
**operationId:** `Create a Schedule`

## Resumen
Create a Schedule

## Descripción
Create new Schedule for the given location.

A time schedule establishes a set of times during the day or holidays in the year in which a feature, for example auto attendants, can perform a specific action.

Creating a schedule requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Create the schedule for this location.
- `orgId` [query] (string): Create the schedule for this organization.

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
  "name": "AUTOATTENDANT-BUSINESS-HOURS",
  "type": "businessHours",
  "events": [
    {
      "name": "Monday 1",
      "startDate": "2021-11-03",
      "endDate": "2021-11-03",
      "startTime": "09:00",
      "endTime": "11:00",
      "allDayEnabled": false,
      "recurrence": {
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
    },
    {
      "name": "Monday 2",
      "startDate": "2021-11-03",
      "endDate": "2021-11-03",
      "startTime": "12:00",
      "endTime": "17:00",
      "allDayEnabled": false,
      "recurrence": {
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
    },
    {
      "name": "Tuesday 1",
      "startDate": "2021-11-03",
      "endDate": "2021-11-03",
      "startTime": "09:00",
      "endTime": "11:00",
      "allDayEnabled": false,
      "recurrence": {
        "recurWeekly": {
          "sunday": false,
          "monday": false,
          "tuesday": true,
          "wednesday": false,
          "thursday": false,
          "friday": false,
          "saturday": false
        }
      }
    },
    {
      "name": "Tuesday 2",
      "startDate": "2021-11-03",
      "
  ... (truncado)
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations/<locationId>/schedules' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"type": "<type>", "name": "<name>"}'
```

## Respuestas correctas
**201**: Created
- `id` (string) (**requerido**): ID of the newly created schedule.

### Ejemplo — respuesta 201
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1NDSEVEVUxFL1FWVlVUMEZVVkVWT1JFRk9WQzFDVlZOSlRrVlRVeTFJVDFWU1V3"
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