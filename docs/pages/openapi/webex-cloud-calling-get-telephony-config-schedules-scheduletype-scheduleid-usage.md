---
doc_id: webex-cloud-calling-get-telephony-config-schedules-scheduletype-scheduleid-usage
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/schedules/{scheduleType}/{scheduleId}/usage
operation_id: listOrganizationScheduleUsage
tags: Org-Wide Schedules
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:50.758671+00:00
---

# GET /telephony/config/schedules/{scheduleType}/{scheduleId}/usage

**API:** Webex Cloud Calling
**Área:** Org-Wide Schedules
**operationId:** `listOrganizationScheduleUsage`

## Resumen
List People and Features Using a Schedule

## Descripción
Lists people and calling feature instances that use the specified organization schedule. Results can be filtered by location and are returned with pagination.

A time schedule establishes a set of times during the day or holidays in the year in which a Webex Calling feature, such as an auto attendant, can perform a specific action.

Viewing schedule usage requires full, read-only, or user administrator access, location administrator access, delegated organization schedule access with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Unique identifier of the Organization
- `scheduleType` [path] (string) (**requerido**): Schedule type to retrieve usage for. Valores: businessHours, holidays.
- `scheduleId` [path] (string) (**requerido**): Unique identifier of the schedule whose usage is returned.
- `locationId` [query] (string): Limits usage results to the specified location.
- `max` [query] (integer): Maximum number of usage records to return. Defaults to 2000 and cannot exceed 2000. Por defecto: 2000.
- `start` [query] (integer): Zero-based offset of the first usage record to return. Defaults to 0. The sum of `start` and `max` must not exceed 2000; because `max` defaults to 2000, reduce `max` when `start` is greater than 0. Por defecto: 0.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/schedules/<scheduleType>/<scheduleId>/usage' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Schedule usage retrieved successfully.
- `usedBy` (array) (**requerido**): People and calling feature instances that use the organization schedule.
  - `type` (string) (**requerido**): Resource type of the person, workspace, or calling feature that uses the schedule. * `PEOPLE` - A person uses the schedule. * `PLACE` - A workspace uses the schedule. * `AUTO_ATTENDANT` - An auto attendant uses the schedule. * `CALL_QUEUE` - A call queue uses the schedule. * `HUNT_GROUP` - A hunt group uses the schedule. Valores: PEOPLE, PLACE, AUTO_ATTENDANT, CALL_QUEUE, HUNT_GROUP.
  - `id` (string) (**requerido**): Unique identifier for the person, workspace, or calling feature indicated by `type`.
  - `name` (string) (**requerido**): Name of the person or calling feature that uses the schedule.
  - `locationName` (string) (**requerido**): Name of the associated location, when available.
  - `locationId` (string) (**requerido**): Unique identifier of the associated location, when available.

### Ejemplo — respuesta 200
```json
{
  "usedBy": [
    {
      "type": "PEOPLE",
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS83MGU3MjYzMC1mZjlmLTExZWItODU5YS0xZjhiYjRjNzc1MWQ",
      "name": "Alice",
      "locationName": "San Jose",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzEyMzQ1"
    }
  ]
}
```
- Cabecera `Link`: Link to the next page of schedule usage when another page is available.

## Respuestas de error
- **400**: Bad Request: The schedule type, location ID, or pagination parameters are invalid.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The schedule or organization does not exist.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **415**: Unsupported Media Type: The request was made without a supported media type.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time.
- **500**: Internal Server Error: Something went wrong on the server.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs