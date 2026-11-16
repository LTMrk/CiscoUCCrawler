---
doc_id: webex-cloud-calling-post-telephony-config-schedules
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/schedules
operation_id: createOrganizationSchedule
tags: Org-Wide Schedules
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:50.758022+00:00
---

# POST /telephony/config/schedules

**API:** Webex Cloud Calling
**Área:** Org-Wide Schedules
**operationId:** `createOrganizationSchedule`

## Resumen
Create an Organization-Level Schedule

## Descripción
Creates an organization-level schedule without events and returns its identifier.

A time schedule establishes a set of times during the day or holidays in the year in which a Webex Calling feature, such as an auto attendant, can perform a specific action.

Creating an organization schedule requires full administrator access or delegated organization schedule access with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Unique identifier of the Organization

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Name for the organization schedule. It must contain 1 to 40 characters and must not contain slashes. Long. max: 40.
- `type` (string) (**requerido**): Schedule type.  * `businessHours` - A schedule for business or working hours.  * `holidays` - A schedule for holidays. Valores: businessHours, holidays.

### Ejemplo — petición
```json
{
  "name": "orgSchedule1",
  "type": "holidays"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/schedules' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "type": "<type>"}'
```

## Respuestas correctas
**201**: Organization schedule created successfully.
- `id` (string) (**requerido**): Unique identifier of the newly created schedule.

### Ejemplo — respuesta 201
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1NDSEVEVUxFL2IzSm5VMk5vWldSMWJHVXg"
}
```

## Respuestas de error
- **400**: Bad Request: Required fields, schedule type, or schedule name validation failed.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The organization does not exist.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **415**: Unsupported Media Type: The request was made without a supported media type.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time.
- **500**: Internal Server Error: Something went wrong on the server.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs