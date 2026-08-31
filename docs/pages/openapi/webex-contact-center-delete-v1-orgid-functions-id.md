---
doc_id: webex-contact-center-delete-v1-orgid-functions-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: DELETE
path: /v1/{orgId}/functions/{id}
operation_id: delete
tags: Functions
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.760944+00:00
---

# DELETE /v1/{orgId}/functions/{id}

**API:** Webex Contact Center
**Área:** Functions
**operationId:** `delete`

## Resumen
Delete a Custom Function

## Descripción
Delete a custom function by ID. Use `isForceDeletion=true` to delete even when the function is referenced by one or more flows.

Scope: `cjp:config_write`

## Parámetros
- `orgId` [path] (string) (**requerido**): Organization ID.
- `id` [path] (string) (**requerido**): Custom function ID.
- `isForceDeletion` [query] (boolean): If `true`, deletes the function regardless of its usage in flows. Por defecto: False.

## Ejemplo de invocación
```bash
curl -X DELETE '/v1/<orgId>/functions/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**204**: Custom function deleted successfully.

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