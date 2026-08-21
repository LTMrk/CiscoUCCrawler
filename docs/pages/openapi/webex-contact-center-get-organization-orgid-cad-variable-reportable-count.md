---
doc_id: webex-contact-center-get-organization-orgid-cad-variable-reportable-count
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/cad-variable/reportable-count
operation_id: getReportableCountConfig
tags: Global Variables
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.756394+00:00
---

# GET /organization/{orgid}/cad-variable/reportable-count

**API:** Webex Contact Center
**Área:** Global Variables
**operationId:** `getReportableCountConfig`

## Resumen
Get reportable count for Global Variable(s)

## Descripción
Get count for all the reportable Global Variable(s) in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/cad-variable/reportable-count' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK

## Respuestas de error
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs