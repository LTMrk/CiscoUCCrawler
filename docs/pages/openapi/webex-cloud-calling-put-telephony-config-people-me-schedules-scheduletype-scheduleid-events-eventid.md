---
doc_id: webex-cloud-calling-put-telephony-config-people-me-schedules-scheduletype-scheduleid-events-eventid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/people/me/schedules/{scheduleType}/{scheduleId}/events/{eventId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.570270+00:00
---

# PUT /telephony/config/people/me/schedules/{scheduleType}/{scheduleId}/events/{eventId}

**API:** Webex Cloud Calling
**Área:** Call Settings For Me With UserHub Phase2
**operationId:** `updateMyScheduleEvent`

## Resumen
Modify User Schedule Event

## Descripción
Modify a Schedule event details for Call Settings of the authenticated user.

Schedules are used to define specific time periods which can be applied to various Call Settings, such as Sequential Ring, or Priority Alert. These call settings perform the defined actions based on the time frame in the schedule, making it more convenient for users to manage their calls.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Parámetros
- `scheduleType` [path] (string) **(requerido)**: Type of the schedule.  * `businessHours` - Business hours schedule type.  * `holidays` - Holidays schedule type.
- `scheduleId` [path] (string) **(requerido)**: Update an event for the specified schedule ID.
- `eventId` [path] (string) **(requerido)**: Update the event with the matching ID.

## Cuerpo de la petición (application/json)
- `name` (string) **(requerido)**: Name for the event.
- `newName` (string): New Name for the event.
- `startDate` (string) **(requerido)**: Start Date of Event.
- `endDate` (string) **(requerido)**: End Date of Event.
- `startTime` (string): Start time of event.
- `endTime` (string): End time of event.
- `allDayEnabled` (boolean) **(requerido)**: An indication of whether given event is an all-day event or not.
- `recurrence` (object): Recurrence definition for a user's schedule event.
  - `recurForEver` (boolean): Flag to indicate if event will recur forever.
  - `recurEndDate` (string): End date of recurrence.
  - `recurEndOccurrence` (integer): Number of occurrences after which the event will stop recurring.
  - `recurDaily` (object): Specifies the number of days between the start of each recurrence and is not allowed with `recurWeekly`.
    - `recurInterval` (number) **(requerido)**: Recurring interval in days. The number of days after the start when an event will repeat.  Repetitions cannot overlap.
  - `recurWeekly` (object):
    - `sunday` (boolean) **(requerido)**: Frequency of occurrence in weeks and select the day - Sunday.
    - `monday` (boolean): Frequency of occurrence in weeks and select the day - Monday.
    - `tuesday` (boolean): Frequency of occurrence in weeks and select the day - Tuesday.
    - `wednesday` (boolean): Frequency of occurrence in weeks and select the day - Wednesday.
    - `thursday` (boolean): Frequency of occurrence in weeks and select the day - Thursday.
    - `friday` (boolean): Frequency of occurrence in weeks and select the day - Friday.
    - `saturday` (boolean): Frequency of occurrence in weeks and select the day - Saturday.

### Ejemplo de petición
```json
{
  "name": "Schedule1",
  "startDate": "2023-02-06",
  "endDate": "2023-02-06",
  "allDayEnabled": true,
  "startTime": "09:00",
  "endTime": "18:00",
  "recurrence": {
    "recurForEver": false,
    "recurEndDate": "2023-02-06",
    "recurEndOccurrence": 1,
    "recurDaily": {
      "recurInterval": 1
    },
    "recurWeekly": {
      "sunday": false,
      "monday": false,
      "tuesday": false,
      "wednesday": false,
      "thursday": false,
      "friday": true,
      "saturday": false
    }
  }
}
```

## Respuestas
- **204**: Schedule Event Configurations updated successfully for the authenticated user.
- **400**: Bad Request: The request was invalid or cannot be otherwise served.
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
