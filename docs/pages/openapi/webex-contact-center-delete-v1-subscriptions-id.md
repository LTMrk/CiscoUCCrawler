---
doc_id: webex-contact-center-delete-v1-subscriptions-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: DELETE
path: /v1/subscriptions/{id}
operation_id: deleteSubscriptionById
tags: Subscriptions
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.845383+00:00
---

# DELETE /v1/subscriptions/{id}

**API:** Webex Contact Center
**Área:** Subscriptions
**operationId:** `deleteSubscriptionById`

## Resumen
Delete Subscription

## Descripción
Deletes a subscription for a given subscription ID. Requires `cjp:config_write` scope.

## Parámetros
- `id` [path] (string/uuid) (**requerido**):
- `orgId` [query] (string): Organization ID to be used for this operation. If unspecified, the Organization ID is inferred from the token. The token must have permissions to interact with the organization.
- `TrackingId` [header] (string): Tracking ID to use for this operation, for traceability, debugging, and error reporting purposes. If not provided, we will generate one for you.

## Ejemplo de invocación
```bash
curl -X DELETE '/v1/subscriptions/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**204**: No Content

## Respuestas de error
- **400**: Validation Error
- **401**: Unauthorized Operation
- **403**: Forbidden Operation
- **500**: An Unexpected Error Occurred

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs