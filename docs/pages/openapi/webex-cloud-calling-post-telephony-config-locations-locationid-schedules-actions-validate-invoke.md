---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-schedules-actions-validate-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/locations/{locationId}/schedules/actions/validate/invoke
operation_id: validateLocationScheduleName
tags: Location Call Settings:  Schedules
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-23T14:21:15.942531+00:00
---

# POST /telephony/config/locations/{locationId}/schedules/actions/validate/invoke

**API:** Webex Cloud Calling
**Área:** Location Call Settings:  Schedules
**operationId:** `validateLocationScheduleName`

## Resumen
Validate a Location Schedule Name

## Descripción
Checks whether a schedule name is available for the given type for the specified location without saving a schedule.

A time schedule establishes a set of times during the day or holidays in the year in which a feature, for example auto attendants, can perform a specific action.

Validating a location schedule name requires full, read-only, user or location administrator access, or delegated organization schedule access, with a scope of `spark-admin:telephony_config_read`. Full administrators can also use a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location containing the schedule to check.
- `orgId` [query] (string): Organization to which the location belongs.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Nonblank name to check for the schedule. Name must not contain slashes. Long. max: 40.
- `type` (string) (**requerido**): Type of schedule to validate. * `businessHours` - A schedule for business or working hours. * `holidays` - A schedule for holidays. Valores: businessHours, holidays.

### Ejemplo — petición
```json
{
  "name": "Holiday Schedule",
  "type": "holidays"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations/<locationId>/schedules/actions/validate/invoke' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "type": "<type>"}'
```

## Respuestas correctas
**204**: The schedule name and type are valid, and the name is available.

## Respuestas de error
- **400**: Bad Request: The request is missing a nonblank schedule name or contains an invalid schedule type.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the location does not exist.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: A schedule with the proposed name and type already exists.
- **415**: Unsupported Media Type: The request was made without a supported media type.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time.
- **500**: Internal Server Error: Something went wrong on the server.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs