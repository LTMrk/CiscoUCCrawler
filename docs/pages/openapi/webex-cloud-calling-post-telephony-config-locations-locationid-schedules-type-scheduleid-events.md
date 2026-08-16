---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-schedules-type-scheduleid-events
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/config/locations/{locationId}/schedules/{type}/{scheduleId}/events
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.628824+00:00
---

# POST /telephony/config/locations/{locationId}/schedules/{type}/{scheduleId}/events

**API:** Webex Cloud Calling
**Área:** Location Call Settings:  Schedules
**operationId:** `Create a Schedule Event`

## Resumen
Create a Schedule Event

## Descripción
Create new Event for the given location Schedule.

A time schedule establishes a set of times during the day or holidays in the year in which a feature, for example auto attendants, can perform a specific action.

Creating a schedule event requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Create the schedule for this location.
- `type` [path] (string) **(requerido)**: Type of schedule.
- `scheduleId` [path] (string) **(requerido)**: Create event for a given schedule ID.
- `orgId` [query] (string): Create the schedule for this organization.

## Cuerpo de la petición (application/json)
- `name` (string) **(requerido)**: Name for the event.
- `startDate` (string) **(requerido)**: Start Date of Event.
- `endDate` (string) **(requerido)**: End Date of Event.
- `startTime` (string): Start time of event. Mandatory if the event is not all day.
- `endTime` (string): End time of event. Mandatory if the event is not all day.
- `allDayEnabled` (boolean): An indication of whether given event is an all-day event or not. Mandatory if the `startTime` and `endTime` are not defined.
- `recurrence` (object):
  - `recurForEver` (boolean): Flag to indicate if event will recur forever.
  - `recurEndDate` (string): End date of recurrence.
  - `recurWeekly` (object):
    - `sunday` (boolean) **(requerido)**: Frequency of occurrence in weeks and select the day - Sunday.
    - `monday` (boolean): Frequency of occurrence in weeks and select the day - Monday.
    - `tuesday` (boolean): Frequency of occurrence in weeks and select the day - Tuesday.
    - `wednesday` (boolean): Frequency of occurrence in weeks and select the day - Wednesday.
    - `thursday` (boolean): Frequency of occurrence in weeks and select the day - Thursday.
    - `friday` (boolean): Frequency of occurrence in weeks and select the day - Friday.
    - `saturday` (boolean): Frequency of occurrence in weeks and select the day - Saturday.
  - `recurYearlyByDate` (object):
    - `dayOfMonth` (number) **(requerido)**: Schedule the event on a specific day of the month.
    - `month` (string) **(requerido)**: Schedule the event on a specific month of the year. Valores: JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER.
  - `recurYearlyByDay` (object):
    - `day` (string) **(requerido)**: Schedule the event on a specific day. Valores: SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY.
    - `week` (string) **(requerido)**: Schedule the event on a specific week. Valores: FIRST, SECOND, THIRD, FOURTH, LAST.
    - `month` (string) **(requerido)**: Schedule the event on a specific month. Valores: JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER.

### Ejemplo de petición
```json
{
  "name": "New Year's Day",
  "startDate": "2022-01-01",
  "endDate": "2022-01-01",
  "allDayEnabled": true,
  "recurrence": {
    "recurYearlyByDate": {
      "dayOfMonth": 1,
      "month": "JANUARY"
    }
  }
}
```

## Respuestas
- **201**: Created
  - `id` (string) **(requerido)**: ID of the newly created schedule event.
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
