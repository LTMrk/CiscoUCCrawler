---
doc_id: webex-contact-center-get-v1-event-types
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /v1/event-types
operation_id: getAllEventTypes
tags: Subscriptions
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.845760+00:00
---

# GET /v1/event-types

**API:** Webex Contact Center
**Área:** Subscriptions
**operationId:** `getAllEventTypes`

## Resumen
List Event Types

## Descripción
Retrieve all available event types for an organization. Requires `cjp:config_read` scope.

## Parámetros
- `orgId` [query] (string): Organization ID to be used for this operation. If unspecified, the Organization ID is inferred from the token. The token must have permissions to interact with the organization.
- `TrackingId` [header] (string): Tracking ID to use for this operation, for traceability, debugging, and error reporting purposes. If not provided, we will generate one for you.

## Ejemplo de invocación
```bash
curl -X GET '/v1/event-types' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `data` (array) (**requerido**):
  - `name` (string) (**requerido**): The name of the event type. Consists of the resource and the action which occurred on it, separated by a colon. Use when registering a subscription. Long. max: 64.
  - `resource` (string) (**requerido**): The resource to which the event type belongs. Long. max: 64.
  - `action` (string) (**requerido**): The action being taken on the resource in the event. Long. max: 64.
- `meta` (object) (**requerido**): Response metadata.
  - `orgId` (string): Organization ID to which resources belong.

## Respuestas de error
- **400**: Validation Error
- **401**: Unauthorized Operation
- **403**: Forbidden Operation
- **500**: An Unexpected Error Occurred

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs