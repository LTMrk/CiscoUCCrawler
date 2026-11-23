---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-schedules-scheduletype-scheduleid-actions-promote-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/locations/{locationId}/schedules/{scheduleType}/{scheduleId}/actions/promote/invoke
operation_id: promoteLocationScheduleToOrganizationScope
tags: Location Call Settings:  Schedules
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-23T14:21:15.942126+00:00
---

# POST /telephony/config/locations/{locationId}/schedules/{scheduleType}/{scheduleId}/actions/promote/invoke

**API:** Webex Cloud Calling
**Área:** Location Call Settings:  Schedules
**operationId:** `promoteLocationScheduleToOrganizationScope`

## Resumen
Promote a Location Schedule to Organization Scope

## Descripción
Promotes a location schedule to organization scope.

A time schedule establishes a set of times during the day or holidays in the year in which a feature, for example auto attendants, can perform a specific action.

Promoting a location schedule requires full administrator access or delegated organization schedule access with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location containing the schedule to promote.
- `scheduleType` [path] (string) (**requerido**): Type of the schedule to promote. Valores: businessHours, holidays.
- `scheduleId` [path] (string) (**requerido**): Identifier of the location schedule to promote.
- `orgId` [query] (string): Identifier of the organization to which the schedule belongs.

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations/<locationId>/schedules/<scheduleType>/<scheduleId>/actions/promote/invoke' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**204**: Location schedule promoted to organization scope.

## Respuestas de error
- **400**: Bad Request: The schedule type or an id value is invalid.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but access is not allowed.
- **404**: Not Found: The specified location schedule does not exist.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: A schedule with the same name already exists at organization scope.
- **500**: Internal Server Error: Something went wrong on the server.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs