---
doc_id: webex-contact-center-post-v1-orgid-functions-id-unlock
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/{orgId}/functions/{id}:unlock
operation_id: unlockFnById
tags: Functions
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.761390+00:00
---

# POST /v1/{orgId}/functions/{id}:unlock

**API:** Webex Contact Center
**Área:** Functions
**operationId:** `unlockFnById`

## Resumen
Unlock a Custom Function

## Descripción
Release the edit lock on a custom function so that other users can edit it.

Scope: `cjp:config_write`

## Parámetros
- `orgId` [path] (string) (**requerido**): Organization ID.
- `id` [path] (string) (**requerido**): Custom function ID.

## Ejemplo de invocación
```bash
curl -X POST '/v1/<orgId>/functions/<id>:unlock' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Custom function unlocked successfully.

### Ejemplo — respuesta 200
```json
"OK"
```

## Respuestas de error
- **400**: Bad Request.
  Ejemplo:
```json
{
  "code": "InvalidRequest",
  "message": "The campaign ID is missing"
}
```
- **401**: Unauthorized.
- **404**: No function found for the supplied ID.
- **500**: Internal Server Error.
  Ejemplo:
```json
{
  "code": "InvalidRequest",
  "message": "The campaign ID is missing"
}
```

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs