---
doc_id: webex-cloud-calling-put-people-personid-features-schedules-scheduletype-scheduleid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /people/{personId}/features/schedules/{scheduleType}/{scheduleId}
operation_id: Update a Schedule
tags: User Call Settings (1/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.330114+00:00
---

# PUT /people/{personId}/features/schedules/{scheduleType}/{scheduleId}

**API:** Webex Cloud Calling
**Área:** User Call Settings (1/2)
**operationId:** `Update a Schedule`

## Resumen
Update a Schedule

## Descripción
Modify a schedule by its schedule ID.

Schedules are used to support calling features and can be defined at the location or person level. `businessHours` schedules allow you to apply specific call settings at different times of the day or week by defining one or more events. `holidays` schedules define exceptions to normal business hours by defining one or more events.

This API requires a full or user administrator auth token with the `spark-admin:people_write` scope.

## Parámetros
- `personId` [path] (string) (**requerido**): Unique identifier for the person.
- `scheduleType` [path] (string) (**requerido**): Type of schedule, either `businessHours` or `holidays`.
- `scheduleId` [path] (string) (**requerido**): Unique identifier for the schedule.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Cuerpo de la petición (application/json)
- `newName` (string) (**requerido**): New name for the schedule.
- `name` (string) (**requerido**): Name for the schedule.
- `type` (string) (**requerido**): * `businessHours` - The schedule type that specifies the business or working hours during the day.  * `holidays` - The schedule type that specifies the day when your organization is not open. Valores: businessHours, holidays.
- `events` (array): List of events.
  - `name` (string) (**requerido**): Name for the event.
  - `startDate` (string) (**requerido**): Start date of the event, or first occurrence if repeating, in the format of `YYYY-MM-DD`.  This field is required if the `allDayEnabled` field is present.
  - `endDate` (string) (**requerido**): End date of the event, or first occurrence if repeating, in the format of `YYYY-MM-DD`.  This field is required if the `allDayEnabled` field is present.
  - `startTime` (string) (**requerido**): Start time of the event in the format of `HH:MM` (24 hours format).  This field is required if the `allDayEnabled` field is false or omitted.
  - `endTime` (string) (**requerido**): End time of the event in the format of `HH:MM` (24 hours format).  This field is required if the `allDayEnabled` field is false or omitted.
  - `allDayEnabled` (boolean): True if it is all-day event.
  - `recurrence` (object): Recurrence scheme for an event.
    - `recurForEver` (boolean): True if the event repeats forever. Requires either `recurDaily` or `recurWeekly` to be specified.
    - `recurEndDate` (string): End date for the recurring event in the format of `YYYY-MM-DD`. Requires either `recurDaily` or `recurWeekly` to be specified.
    - `recurEndOccurrence` (number): End recurrence after the event has repeated the specified number of times. Requires either `recurDaily` or `recurWeekly` to be specified.
    - `recurDaily` (object): Specifies the number of days between the start of each recurrence. Not allowed with `recurWeekly`.
      - `recurInterval` (number) (**requerido**): Recurring interval in days. The number of days after the start when an event will repeat.  Repetitions cannot overlap.
    - `recurWeekly` (object): Specifies the event recur weekly on the designated days of the week. Not allowed with `recurDaily`.
      - `recurInterval` (number) (**requerido**): Specifies the number of weeks between the start of each recurrence.
      - `sunday` (boolean): The Event occurs weekly on Sunday.
      - `monday` (boolean): The Event occurs weekly on Monday.
      - `tuesday` (boolean): The Event occurs weekly on Tuesday.
      - `wednesday` (boolean): The Event occurs weekly on Wednesday.
      - `thursday` (boolean): The Event occurs weekly on Thursday.
      - `friday` (boolean): The Event occurs weekly on Friday.
      - `saturday` (boolean): The Event occurs weekly on Saturday.

## Ejemplo de invocación
```bash
curl -X PUT '/people/<personId>/features/schedules/<scheduleType>/<scheduleId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"newName": "<newName>", "name": "<name>", "type": "<type>"}'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Identifier for a schedule.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1VTRVJfU0NIRURVTEUvVW1samFHRnlaSE52Ymw5UFptWnBZMlZmU0c5MWNuTT0"
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