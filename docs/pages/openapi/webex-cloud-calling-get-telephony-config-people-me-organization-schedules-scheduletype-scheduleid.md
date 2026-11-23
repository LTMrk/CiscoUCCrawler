---
doc_id: webex-cloud-calling-get-telephony-config-people-me-organization-schedules-scheduletype-scheduleid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/organization/schedules/{scheduleType}/{scheduleId}
operation_id: getOrganizationScheduleForMe
tags: Call Settings For Me With UserHub Phase2
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-23T14:21:15.722203+00:00
---

# GET /telephony/config/people/me/organization/schedules/{scheduleType}/{scheduleId}

**API:** Webex Cloud Calling
**Área:** Call Settings For Me With UserHub Phase2
**operationId:** `getOrganizationScheduleForMe`

## Resumen
Get an Organization Schedule for the User

## Descripción
Retrieves an organization schedule and its events for the authenticated user.

Schedules are used to define specific time periods which can be applied to various Call Settings, such as Sequential Ring, or Priority Alert. These call settings perform the defined actions based on the time frame in the schedule, making it more convenient for users to manage their calls.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Parámetros
- `scheduleType` [path] (string) (**requerido**): Schedule category to retrieve. Valores: holidays, businessHours.
- `scheduleId` [path] (string) (**requerido**): Hydra-encoded identifier of the organization schedule.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/organization/schedules/<scheduleType>/<scheduleId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Organization schedule details are retrieved.
- `id` (string) (**requerido**): Unique identifier for the schedule.
- `type` (string) (**requerido**): Schedule type.  * `businessHours` - A schedule for business or working hours.  * `holidays` - A schedule for holidays. Valores: businessHours, holidays.
- `name` (string) (**requerido**): Name of the schedule.
- `level` (string) (**requerido**): Schedule level.  * `ORGANIZATION` - The schedule applies across the organization.  * `LOCATION` - The schedule applies to a location. Valores: ORGANIZATION, LOCATION.
- `locationName` (string): Name of the associated location. Present only for location-level schedules; omitted for organization-level schedules.
- `locationId` (string): Unique identifier of the associated location. Present only for location-level schedules; omitted for organization-level schedules.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1VTRVJfU0NIRURVTEUvVTJOb1pXUjFiR1V4",
  "type": "businessHours",
  "name": "Organization hours",
  "events": []
}
```

## Respuestas de error
- **400**: The request contains an invalid schedule type or identifier, or the schedule does not exist.
- **401**: Authentication credentials are missing or invalid.
- **403**: The authenticated user is not authorized to retrieve the schedule.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs