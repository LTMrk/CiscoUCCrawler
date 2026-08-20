---
doc_id: webex-contact-center-delete-admin-v1-api-wxcc-subscription-workspace-id-workspaceid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: DELETE
path: /admin/v1/api/wxcc-subscription/workspace-id/{workspaceId}
operation_id: deleteWXCCSubscription
tags: Journey - Subscription API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-20T13:57:48.746848+00:00
---

# DELETE /admin/v1/api/wxcc-subscription/workspace-id/{workspaceId}

**API:** Webex Contact Center
**Área:** Journey - Subscription API
**operationId:** `deleteWXCCSubscription`
**Autenticación:** bearerAuth

## Resumen
Delete WXCC Subscription

## Descripción
Delete WXCC Subscription in JDS. Use the cjp scope if you have a contact center license; otherwise, use the cjds scope. It requires the appropriate cjds:admin_org_write or cjp:config_write scopes

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Workspace ID

## Ejemplo de invocación
```bash
curl -X DELETE '/admin/v1/api/wxcc-subscription/workspace-id/<workspaceId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: No Content

## Respuestas de error
- **404**: Resource not found
- **409**: Resource already exists
- **429**: Too many requests
- **500**: Internal server error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs