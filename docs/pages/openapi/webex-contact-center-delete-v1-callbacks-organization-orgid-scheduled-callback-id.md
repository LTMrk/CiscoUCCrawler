---
doc_id: webex-contact-center-delete-v1-callbacks-organization-orgid-scheduled-callback-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: DELETE
path: /v1/callbacks/organization/{orgId}/scheduled-callback/{id}
operation_id: DeleteScheduledCallbackById
tags: Callbacks
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.708375+00:00
---

# DELETE /v1/callbacks/organization/{orgId}/scheduled-callback/{id}

**API:** Webex Contact Center
**Área:** Callbacks
**operationId:** `DeleteScheduledCallbackById`

## Resumen
Delete scheduled callback by Id

## Descripción
Delete an existing scheduled callback by Id, those whose scheduled trigger time has already passed cannot be deleted. Requires 'cjp:user' scope for authorization.

## Parámetros
- `orgId` [path] (string) (**requerido**): The organization ID for which the callback is being scheduled. This should be a valid UUID.
- `id` [path] (string/UUID) (**requerido**): The id with which the Scheduled Callback has been created.

## Ejemplo de invocación
```bash
curl -X DELETE '/v1/callbacks/organization/<orgId>/scheduled-callback/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**204**: The request was successfully deleted.

## Respuestas de error
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **404**: Not Found
- **429**: Too Many Requests
- **500**: Internal Server Error
- **503**: Service Unavailable

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs