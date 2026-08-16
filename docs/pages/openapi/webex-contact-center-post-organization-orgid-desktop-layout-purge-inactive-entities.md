---
doc_id: webex-contact-center-post-organization-orgid-desktop-layout-purge-inactive-entities
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/desktop-layout/purge-inactive-entities
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.937813+00:00
---

# POST /organization/{orgid}/desktop-layout/purge-inactive-entities

**API:** Webex Contact Center
**Área:** Desktop Layout
**operationId:** `purgeInactiveConfig_6`

## Resumen
Purge inactive Desktop Layout(s)

## Descripción
Purge inactive Desktop Layout(s) older than the configured interval for a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `nextStartId` [query] (string): This is the entity ID from which items for the next purge batch with be selected.

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
