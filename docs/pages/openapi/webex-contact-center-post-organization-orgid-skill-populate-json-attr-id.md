---
doc_id: webex-contact-center-post-organization-orgid-skill-populate-json-attr-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/skill/populate-json-attr/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.949485+00:00
---

# POST /organization/{orgid}/skill/populate-json-attr/{id}

**API:** Webex Contact Center
**Área:** Skill
**operationId:** `populateJsonAttributesByOrgIdAndSkillId`

## Resumen
Populate json-attributes field for a given skill-id of an organization

## Parámetros
- `orgid` [path] (string) **(requerido)**:
- `id` [path] (string) **(requerido)**:

## Respuestas
- **200**: OK
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **409**: Similar entity is already present
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
