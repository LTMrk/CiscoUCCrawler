---
doc_id: webex-cloud-calling-delete-telephony-config-people-me-schedules-scheduletype-scheduleid-events-eventid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: DELETE
path: /telephony/config/people/me/schedules/{scheduleType}/{scheduleId}/events/{eventId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.570362+00:00
---

# DELETE /telephony/config/people/me/schedules/{scheduleType}/{scheduleId}/events/{eventId}

**API:** Webex Cloud Calling
**Área:** Call Settings For Me With UserHub Phase2
**operationId:** `deleteMyUserScheduleEvent`

## Resumen
Delete User a Schedule Event

## Descripción
Delete a specific schedule event for the authenticated user.

Schedules are used to define specific time periods which can be applied to various Call Settings, such as Sequential Ring, or Priority Alert. These call settings perform the defined actions based on the time frame in the schedule, making it more convenient for users to manage their calls.

This API requires a user auth token with a scope of `spark:telephony_config_write`.

## Parámetros
- `scheduleType` [path] (string) **(requerido)**: Type of the schedule.  * `businessHours` - Business hours schedule type.  * `holidays` - Holidays schedule type.
- `scheduleId` [path] (string) **(requerido)**: Delete an event for the specified schedule ID.
- `eventId` [path] (string) **(requerido)**: Delete the event with the matching ID.

## Respuestas
- **204**: Schedule Event deleted successfully. No content is returned.
- **400**: Bad Request: The request was invalid or cannot be otherwise served.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
