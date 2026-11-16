---
doc_id: webex-cloud-calling-delete-telephony-config-schedules-scheduletype-scheduleid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: DELETE
path: /telephony/config/schedules/{scheduleType}/{scheduleId}
operation_id: deleteOrganizationSchedule
tags: Org-Wide Schedules
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:50.758321+00:00
---

# DELETE /telephony/config/schedules/{scheduleType}/{scheduleId}

**API:** Webex Cloud Calling
**Área:** Org-Wide Schedules
**operationId:** `deleteOrganizationSchedule`

## Resumen
Delete an Organization Schedule

## Descripción
Deletes an organization-level schedule. A successful deletion returns no response body.

A time schedule establishes a set of times during the day or holidays in the year in which a Webex Calling feature, such as an auto attendant, can perform a specific action.

Managing an organization schedule requires full administrator access or delegated organization schedule access with `spark-admin:telephony_config_write` scope.

## Parámetros
- `orgId` [query] (string): Unique identifier of the Organization
- `scheduleType` [path] (string) (**requerido**): Type of the organization schedule Valores: businessHours, holidays.
- `scheduleId` [path] (string) (**requerido**): Unique identifier of the organization schedule.

## Ejemplo de invocación
```bash
curl -X DELETE '/telephony/config/schedules/<scheduleType>/<scheduleId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**204**: Organization schedule deleted successfully.

## Respuestas de error
- **400**: Bad Request: The schedule type, identifier are invalid.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The schedule or organization does not exist.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: The schedule cannot be deleted because it is being used by a service.
- **415**: Unsupported Media Type: The request was made without a supported media type.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time.
- **500**: Internal Server Error: Something went wrong on the server.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs