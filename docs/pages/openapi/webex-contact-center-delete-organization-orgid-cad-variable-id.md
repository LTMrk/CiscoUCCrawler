---
doc_id: webex-contact-center-delete-organization-orgid-cad-variable-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: DELETE
path: /organization/{orgid}/cad-variable/{id}
operation_id: deleteConfig_20
tags: Global Variables
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-20T13:57:48.697464+00:00
---

# DELETE /organization/{orgid}/cad-variable/{id}

**API:** Webex Contact Center
**Área:** Global Variables
**operationId:** `deleteConfig_20`

## Resumen
Delete specific Global Variable by ID

## Descripción
Delete an existing Global Variable by ID in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) (**requerido**): ID of the Global Variable.

## Ejemplo de invocación
```bash
curl -X DELETE '/organization/<orgid>/cad-variable/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK

## Respuestas de error
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **412**: Resource referred in other entity(s). Please get all the reference entities info by invoking Get incoming-references api.
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs