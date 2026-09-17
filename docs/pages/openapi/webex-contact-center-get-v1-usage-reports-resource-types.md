---
doc_id: webex-contact-center-get-v1-usage-reports-resource-types
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /v1/usage-reports/resource-types
operation_id: listResourceTypes
tags: Usage Reports
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-17T19:59:29.926199+00:00
---

# GET /v1/usage-reports/resource-types

**API:** Webex Contact Center
**Área:** Usage Reports
**operationId:** `listResourceTypes`

## Resumen
Get available resource types

## Descripción
Returns the list of available resource types that can be used for report generation, along with available data dates.

## Ejemplo de invocación
```bash
curl -X GET '/v1/usage-reports/resource-types' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- (array de:)
  - `resourceType` (string): Technical identifier for the resource type.
  - `displayName` (string): Human-readable name of the resource type.
  - `description` (string): Description of the data contained in this resource type.
  - `dataStartDate` (string): Earliest date for which data is available.
  - `dataEndDate` (string): Latest date for which data is available.

### Ejemplo — respuesta 200
```json
[
  {
    "resourceType": "ContactSessionRecord",
    "displayName": "Contact Session Record",
    "description": "Detailed records of all contact sessions including call details, queue times, and outcomes.",
    "dataStartDate": "2023-01-01",
    "dataEndDate": "2025-01-31"
  }
]
```

## Respuestas de error
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **500**: Internal Server Error: Something went wrong on the server
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs