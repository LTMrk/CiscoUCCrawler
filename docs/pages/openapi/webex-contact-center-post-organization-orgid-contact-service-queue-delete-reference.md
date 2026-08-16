---
doc_id: webex-contact-center-post-organization-orgid-contact-service-queue-delete-reference
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/contact-service-queue/delete-reference
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.934587+00:00
---

# POST /organization/{orgid}/contact-service-queue/delete-reference

**API:** Webex Contact Center
**Área:** Contact Service Queue
**operationId:** `deleteReferencesContactServiceQueue`

## Resumen
Delete references from Contact Service Queues

## Descripción
Removes the references to the specified entities (such as teams, sites, or agents) from Contact Service Queues for a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**:

## Cuerpo de la petición (application/json)
- `references` (object): Map of entity type to entity identifier whose references must be removed from contact service queues. The key is the referenced entity type (e.g. `team`, `site`, `agent`, `skillProfile`) and the value is its UUID.

## Respuestas
- **200**: OK
  - `code` (integer):
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
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **409**: Similar entity is already present
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
