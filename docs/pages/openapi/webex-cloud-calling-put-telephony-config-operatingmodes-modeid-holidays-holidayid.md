---
doc_id: webex-cloud-calling-put-telephony-config-operatingmodes-modeid-holidays-holidayid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/operatingModes/{modeId}/holidays/{holidayId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.617232+00:00
---

# PUT /telephony/config/operatingModes/{modeId}/holidays/{holidayId}

**API:** Webex Cloud Calling
**Área:** Features: Operating Modes
**operationId:** `Modify an Operating Mode Holiday`

## Resumen
Modify an Operating Mode Holiday

## Descripción
Modify the designated `Operating Mode Holiday's` configuration.

Modifying an `Operating Mode Holiday` requires a full, or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `modeId` [path] (string) **(requerido)**: Modify the holiday from this `operating mode` matching ID.
- `holidayId` [path] (string) **(requerido)**: Modify the `Holiday` with the matching ID.
- `orgId` [query] (string): Modify the `operating mode` from this organization.

## Cuerpo de la petición (application/json)
- `name` (string): Name of the holiday.
- `allDayEnabled` (boolean): Specifies if the `operating mode holiday` schedule event is enabled for the entire day. If `startTime`, and `endTime` are provided, this field is ignored.
- `startDate` (string): Start date of the `operating mode holiday`.
- `endDate` (string): End date of the `operating mode holiday`.
- `startTime` (string): Start time for the `operating mode holiday`. Mandatory if `allDayEnabled` is not set.
- `endTime` (string): End time for the `operating mode holiday`. Mandatory if `allDayEnabled` is not set.
- `recurrence` (object):
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
  "name": "Christmas",
  "allDayEnabled": true,
  "startDate": "2024-12-25",
  "endDate": "2024-12-26",
  "startTime": "09:00",
  "endTime": "17:00",
  "recurrence": {
    "recurYearlyByDay": {
      "day": "TUESDAY",
      "week": "FIRST",
      "month": "JANUARY"
    }
  }
}
```

## Respuestas
- **204**: No Content
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
