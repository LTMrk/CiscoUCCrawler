---
doc_id: webex-cloud-calling-post-telephony-config-operatingmodes-modeid-holidays
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/operatingModes/{modeId}/holidays
operation_id: Create an Operating Mode Holiday
tags: Features: Operating Modes
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.498829+00:00
---

# POST /telephony/config/operatingModes/{modeId}/holidays

**API:** Webex Cloud Calling
**Área:** Features: Operating Modes
**operationId:** `Create an Operating Mode Holiday`

## Resumen
Create an Operating Mode Holiday

## Descripción
Create a holiday schedule event for the designated `Operating Mode`.

Holidays define a recurring schedule for the `Operating Modes`. An `Operating Mode` can have a max of 150 holidays.

Creating an `Operating Mode Holiday` requires a full, or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `modeId` [path] (string) (**requerido**): Create the holiday for this `operating mode`.
- `orgId` [query] (string): Create the `operating mode holiday` for this organization.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Name of the holiday.
- `allDayEnabled` (boolean) (**requerido**): Specifies if the `operating mode holiday` schedule event is enabled for the entire day. `False` if the flag is not set.
- `startDate` (string) (**requerido**): Start date of the `operating mode holiday`.
- `endDate` (string) (**requerido**): End date of the `operating mode holiday`.
- `startTime` (string): Start time for the `operating mode holiday`. Mandatory if `allDayEnabled` is false.
- `endTime` (string): End time for the `operating mode holiday`. Mandatory if `allDayEnabled` is false.
- `recurrence` (object):
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

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/operatingModes/<modeId>/holidays' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "allDayEnabled": true, "startDate": "<startDate>", "endDate": "<endDate>"}'
```

## Respuestas correctas
**201**: Created
- `id` (string) (**requerido**): ID of the newly created holiday.

### Ejemplo — respuesta 201
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1NDSEVEVUxFX0VWRU5UL2E4Mjg5NzIyLTFiODAtNDFiNy05Njc4LTBlNzdhZThjMTIwOQ"
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