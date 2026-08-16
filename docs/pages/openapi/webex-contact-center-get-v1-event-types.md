---
doc_id: webex-contact-center-get-v1-event-types
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /v1/event-types
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.960764+00:00
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

## Respuestas
- **200**: OK
  - `data` (array) **(requerido)**:
    - `name` (string) **(requerido)**: The name of the event type. Consists of the resource and the action which occurred on it, separated by a colon. Use when registering a subscription.
    - `resource` (string) **(requerido)**: The resource to which the event type belongs.
    - `action` (string) **(requerido)**: The action being taken on the resource in the event.
  - `meta` (object) **(requerido)**: Response metadata.
    - `orgId` (string): Organization ID to which resources belong.
- **400**: Validation Error
- **401**: Unauthorized Operation
- **403**: Forbidden Operation
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
