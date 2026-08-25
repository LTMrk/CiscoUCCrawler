---
doc_id: webex-cloud-calling-get-telephony-config-people-me-schedules
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/schedules
operation_id: getMySchedules
tags: Call Settings For Me With UserHub Phase2
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.368784+00:00
---

# GET /telephony/config/people/me/schedules

**API:** Webex Cloud Calling
**Área:** Call Settings For Me With UserHub Phase2
**operationId:** `getMySchedules`

## Resumen
Get User (and Location) Schedules

## Descripción
Get Schedules for Call Settings for the authenticated user.

Schedules are used to define specific time periods which can be applied to various Call Settings, such as Sequential Ring, or Priority Alert. These call settings perform the defined actions based on the time frame in the schedule, making it more convenient for users to manage their calls.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/schedules' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Schedules retrieved successfully for the authenticated user.
- `schedules` (array): List of schedules
  - `id` (string) (**requerido**): Unique identifier for the schedule.
  - `name` (string) (**requerido**): Name of the schedule.
  - `type` (string) (**requerido**): * `businessHours` - The schedule is for business hours.  * `holidays` - The schedule is for holidays. Valores: businessHours, holidays.
  - `level` (string) (**requerido**): * `PEOPLE` - The schedule is at the user level.  * `LOCATION` - The schedule is at the location level. Valores: PEOPLE, LOCATION.

### Ejemplo — respuesta 200
```json
{
  "schedules": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1VTRVJfU0NIRURVTEUvVTJOb1pXUjFiR1V4",
      "name": "Schedule1",
      "type": "businessHours",
      "level": "PEOPLE"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1VTRVJfU0NIRURVTEUvVkdWaGJTQkliMnhwWkdGNQ",
      "name": "Team Holiday",
      "type": "holidays",
      "level": "LOCATION"
    }
  ]
}
```

## Respuestas de error
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

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs