---
doc_id: webex-cloud-calling-get-telephony-config-schedules
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/schedules
operation_id: listOrganizationSchedules
tags: Org-Wide Schedules
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:50.757833+00:00
---

# GET /telephony/config/schedules

**API:** Webex Cloud Calling
**Área:** Org-Wide Schedules
**operationId:** `listOrganizationSchedules`

## Resumen
List Organization and Location Schedules

## Descripción
Lists organization-level and Location-level schedules. Results can be filtered by name, type, level, and location, and pagination.

A time schedule establishes a set of times during the day or holidays in the year in which a Webex Calling feature, such as an auto attendant, can perform a specific action.

Viewing schedules requires full, read-only, or user administrator access, location administrator access, or delegated organization schedule access with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Unique identifier of the Organization
- `max` [query] (integer): Maximum number of schedules to return. Defaults to 2000 and cannot exceed 2000. Por defecto: 2000.
- `start` [query] (integer): Zero-based offset of the first schedule to return. Defaults to 0. Por defecto: 0.
- `name` [query] (string): Filters schedules by a partial, case-insensitive name match. The value cannot be blank.
- `type` [query] (string): Filters results by schedule type. Valores: businessHours, holidays.
- `level` [query] (string): Filters results by schedule level. Valores: LOCATION, ORGANIZATION.
- `locationId` [query] (string): Limits results to schedules associated with this location.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/schedules' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Schedules retrieved successfully.
- `schedules` (array) (**requerido**): Schedules matching the supplied filters.
  - `id` (string) (**requerido**): Unique identifier for the schedule.
  - `type` (string) (**requerido**): Schedule type.  * `businessHours` - A schedule for business or working hours.  * `holidays` - A schedule for holidays. Valores: businessHours, holidays.
  - `name` (string) (**requerido**): Name of the schedule.
  - `level` (string) (**requerido**): Schedule level.  * `ORGANIZATION` - The schedule applies across the organization.  * `LOCATION` - The schedule applies to a location. Valores: ORGANIZATION, LOCATION.
  - `locationName` (string): Name of the associated location. Present only for location-level schedules; omitted for organization-level schedules.
  - `locationId` (string): Unique identifier of the associated location. Present only for location-level schedules; omitted for organization-level schedules.

### Ejemplo — respuesta 200
```json
{
  "schedules": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1NDSEVEVUxFL1FuVnphVzVsYzNNZ1NHOTFjbk09",
      "type": "businessHours",
      "name": "Business Hours",
      "level": "LOCATION",
      "locationName": "San Jose",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzEyMzQ1"
    }
  ]
}
```
- Cabecera `Link`: Link to the next page of schedules when another page is available.

## Respuestas de error
- **400**: Bad Request: A filter or pagination value is invalid.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the organization does not exist.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **415**: Unsupported Media Type: The request was made without a supported media type.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time.
- **500**: Internal Server Error: Something went wrong on the server.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs