---
doc_id: webex-cloud-calling-put-telephony-config-schedules-scheduletype-scheduleid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/schedules/{scheduleType}/{scheduleId}
operation_id: updateOrganizationSchedule
tags: Org-Wide Schedules
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T14:22:47.328915+00:00
---

# PUT /telephony/config/schedules/{scheduleType}/{scheduleId}

**API:** Webex Cloud Calling
**Área:** Org-Wide Schedules
**operationId:** `updateOrganizationSchedule`

## Resumen
Update an Organization Schedule

## Descripción
Renames an organization-level schedule and returns its updated identifier.

A time schedule establishes a set of times during the day or holidays in the year in which a Webex Calling feature, such as an auto attendant, can perform a specific action.

Managing an organization schedule requires full administrator access or delegated organization schedule access with `spark-admin:telephony_config_write` scope.

## Parámetros
- `orgId` [query] (string): Unique identifier of the Organization
- `scheduleType` [path] (string) (**requerido**): Type of the organization schedule Valores: businessHours, holidays.
- `scheduleId` [path] (string) (**requerido**): Unique identifier of the organization schedule.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): New name for the schedule. It must contain 1 to 40 characters and must not contain slashes. Long. max: 40.

### Ejemplo — petición
```json
{
  "name": "Business Hours"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/schedules/<scheduleType>/<scheduleId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>"}'
```

## Respuestas correctas
**200**: Organization schedule renamed successfully.
- `id` (string) (**requerido**): Unique identifier of the renamed schedule.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1NDSEVEVUxFL1FuVnphVzVsYzNNZ1NHOTFjbk09"
}
```

## Respuestas de error
- **400**: Bad Request: The schedule type, identifier, or request fields are invalid.
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