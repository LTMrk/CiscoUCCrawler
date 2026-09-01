---
doc_id: webex-contact-center-post-organization-orgid-cad-variable-purge-inactive-entities
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /organization/{orgid}/cad-variable/purge-inactive-entities
operation_id: purgeInactiveConfig_9
tags: Global Variables
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.670834+00:00
---

# POST /organization/{orgid}/cad-variable/purge-inactive-entities

**API:** Webex Contact Center
**Área:** Global Variables
**operationId:** `purgeInactiveConfig_9`

## Resumen
Purge inactive Global Variable(s)

## Descripción
Purge inactive Global Variable(s) older than the configured interval for a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `nextStartId` [query] (string): This is the entity ID from which items for the next purge batch with be selected. Por defecto: .

## Ejemplo de invocación
```bash
curl -X POST '/organization/<orgid>/cad-variable/purge-inactive-entities' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `code` (integer/int32):
- `details` (object):
- `links` (array):
  - `href` (string):
  - `hreflang` (string):
  - `title` (string):
  - `type` (string):
  - `deprecation` (string):
  - `profile` (string):
  - `name` (string):
  - `templated` (boolean):

## Respuestas de error
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **409**: Similar entity is already present
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs