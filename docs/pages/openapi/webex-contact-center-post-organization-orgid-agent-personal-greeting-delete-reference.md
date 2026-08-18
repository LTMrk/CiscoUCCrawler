---
doc_id: webex-contact-center-post-organization-orgid-agent-personal-greeting-delete-reference
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /organization/{orgid}/agent-personal-greeting/delete-reference
operation_id: deleteReferencesAgentPersonalGreeting
tags: Agent Personal Greeting Files
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.772370+00:00
---

# POST /organization/{orgid}/agent-personal-greeting/delete-reference

**API:** Webex Contact Center
**Área:** Agent Personal Greeting Files
**operationId:** `deleteReferencesAgentPersonalGreeting`

## Resumen
Delete references of an agent from greeting files

## Descripción
Removes all references of the specified agent (ciUserId) from greeting files in the given organization. Typically invoked when an agent is deleted or unassigned. in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**):

## Cuerpo de la petición (application/json)
- `references` (object): Map of entity type to entity identifier whose references must be removed from contact service queues. The key is the referenced entity type (e.g. `team`, `site`, `agent`, `skillProfile`) and the value is its UUID.

### Ejemplo — petición
```json
{
  "references": {
    "team": "76cf35bc-12df-49ef-88e1-c86226d8a645",
    "skillProfile": "af9eecc5-0472-4549-9a83-2afdae0d4ba0"
  }
}
```

## Ejemplo de invocación
```bash
curl -X POST '/organization/<orgid>/agent-personal-greeting/delete-reference' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
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
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "400",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "400",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **401**: Unauthorized Operation
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "401",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "401",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **403**: Operation is forbidden
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "403",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "403",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **409**: Similar entity is already present
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "409",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "409",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "429",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "429",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **500**: An Unexpected Error Occurred
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "500",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "500",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs