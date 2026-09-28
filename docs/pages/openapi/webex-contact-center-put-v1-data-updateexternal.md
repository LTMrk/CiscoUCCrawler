---
doc_id: webex-contact-center-put-v1-data-updateexternal
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PUT
path: /v1/data/updateExternal
operation_id: updateTaskGlobalVariables
tags: External Data Updates
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-27T10:51:19.963875+00:00
---

# PUT /v1/data/updateExternal

**API:** Webex Contact Center
**Área:** External Data Updates
**operationId:** `updateTaskGlobalVariables`
**Autenticación:** bearer-key

## Resumen
Update Task Global Variables

## Descripción
Updates numeric global variable values associated with a completed Webex Contact Center task. The request must identify the organization and task along with its start and end timestamps. The task should have ended within two days prior to the time of making the request.

## Parámetros
- `X-ORGANIZATION-ID` [header] (string/uuid): Organization identifier used for partner or delegated access.
- `TrackingId` [header] (string): Optional identifier used for request traceability, debugging, and error reporting.

## Cuerpo de la petición (application/json)
- `orgId` (string/uuid) (**requerido**): Organization identifier. It must correspond to the organization associated with the bearer token or the `X-ORGANIZATION-ID` header. Long. max: 36.
- `updateType` (string) (**requerido**): Specifies the update type. This value must be `contact` for the global variables update. Valores: contact.
- `data` (array) (**requerido**): Array containing the task data to update. Each request may contain only one task.
  - `id` (string/uuid) (**requerido**): Unique identifier of the task to update (`taskId`). Long. max: 36.
  - `startTimestamp` (string/date-time) (**requerido**): Task start timestamp in UTC using `yyyy-MM-dd'T'HH:mm:ss.SSS'Z'` format.
  - `endTimestamp` (string/date-time) (**requerido**): Task end timestamp in UTC using `yyyy-MM-dd'T'HH:mm:ss.SSS'Z'` format. The task must have ended within the preceding two days.
  - `globalVariables` (array) (**requerido**): Global variables to be updated. This array must contain a maximum of 30 entries.
    - `name` (string) (**requerido**): Name of the global variable.
    - `value` (number) (**requerido**): Numeric value of the global variable. Integer, long, and double values are supported.

### Ejemplo — petición
```json
{
  "orgId": "3dae8fdd-06e2-411a-9035-51f3719f5b65",
  "updateType": "contact",
  "data": [
    {
      "id": "315fbb91-2288-427c-9588-ec764cd46ea4",
      "startTimestamp": "2026-09-22T10:00:00.000Z",
      "endTimestamp": "2026-09-22T10:30:00.000Z",
      "globalVariables": [
        {
          "name": "UpSell",
          "value": 12
        },
        {
          "name": "CustomerHappiness",
          "value": 7.5
        }
      ]
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/v1/data/updateExternal' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"orgId": "<orgId>", "updateType": "<updateType>", "data": []}'
```

## Respuestas correctas
**202**: Accepted. The request passed configuration-level validation and was accepted for processing. Additional interaction-level validation may occur after acceptance.
- (todos de:)
  - `trackingId` (string) (**requerido**): Identifier used to trace the request within the application logs.
  - `response` (object) (**requerido**): Details confirming that the request was accepted.

### Ejemplo — respuesta 202
```json
{
  "trackingId": "c1a4fcef-aee2-4dea-8977-29f594760552",
  "response": {
    "key": "202",
    "message": [
      {
        "description": "Request has been accepted."
      }
    ]
  }
}
```

## Respuestas de error
- **400**: Bad Request. The request is missing required data or contains invalid organization, task, timestamp, update type, or global-variable information.
  Ejemplo:
```json
{
  "trackingId": "c1a4fcef-aee2-4dea-8977-29f594760552",
  "error": {
    "key": "400",
    "message": [
      {
        "description": "The request contains an invalid updateType."
      }
    ]
  }
}
```
- **401**: Unauthorized. Authentication credentials are missing or invalid.
  Ejemplo:
```json
{
  "trackingId": "c1a4fcef-aee2-4dea-8977-29f594760552",
  "error": {
    "key": "401",
    "message": [
      {
        "description": "Authentication credentials are missing or invalid."
      }
    ]
  }
}
```
- **403**: Forbidden. The caller does not have the required scopes or roles.
  Ejemplo:
```json
{
  "trackingId": "c1a4fcef-aee2-4dea-8977-29f594760552",
  "error": {
    "key": "403",
    "message": [
      {
        "description": "The caller does not have the required permissions."
      }
    ]
  }
}
```
- **423**: Locked. The API is disabled by a feature flag or service kill switch.
  Ejemplo:
```json
{
  "trackingId": "c1a4fcef-aee2-4dea-8977-29f594760552",
  "error": {
    "key": "423",
    "message": [
      {
        "description": "The API is currently locked."
      }
    ]
  }
}
```
- **429**: Too Many Requests. The organization has exceeded the rate limit of five requests per second.
  Ejemplo:
```json
{
  "trackingId": "c1a4fcef-aee2-4dea-8977-29f594760552",
  "error": {
    "key": "429",
    "message": [
      {
        "description": "The rate limit was exceeded."
      }
    ]
  }
}
```
- **500**: Internal Server Error.
  Ejemplo:
```json
{
  "trackingId": "c1a4fcef-aee2-4dea-8977-29f594760552",
  "error": {
    "key": "500",
    "message": [
      {
        "description": "The service was unable to process the request."
      }
    ]
  }
}
```

**Documentación adicional:** https://developer.webex.com/webex-contact-center/docs/api/

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs