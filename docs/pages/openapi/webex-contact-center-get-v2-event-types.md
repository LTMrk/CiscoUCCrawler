---
doc_id: webex-contact-center-get-v2-event-types
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /v2/event-types
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.961360+00:00
---

# GET /v2/event-types

**API:** Webex Contact Center
**Área:** Subscriptions
**operationId:** `getAllEventTypesWithResourceVersionMetadata`

## Resumen
List Event Types

## Descripción
Retrieve all available event types for an organization along with information about the currently supported resource versions. Requires `cjp:config_read` scope.

## Parámetros
- `orgId` [query] (string): Organization ID to be used for this operation. If unspecified, the Organization ID is inferred from the token. The token must have permissions to interact with the organization.
- `TrackingId` [header] (string): Tracking ID to use for this operation, for traceability, debugging, and error reporting purposes. If not provided, we will generate one for you.

## Respuestas
- **200**: OK
  - `data` (array) **(requerido)**:
    - `name` (string) **(requerido)**: The name of the event type. Consists of the resource and the action which occurred on it, separated by a colon. Use when registering a subscription.
    - `resource` (string) **(requerido)**: The resource to which the event type belongs.
    - `action` (string) **(requerido)**: The action being taken on the resource in the event.
  - `meta` (object) **(requerido)**:
    - `orgId` (string): Organization ID used for this operation.
    - `resourceVersionList` (array) **(requerido)**: List of all resources, and it's supported versions available to subscribe.
      - `resource` (string): Resource name.
      - `version` (string): Version of the resource.
- **400**: Validation Error
- **401**: Unauthorized Operation
- **403**: Forbidden Operation
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
