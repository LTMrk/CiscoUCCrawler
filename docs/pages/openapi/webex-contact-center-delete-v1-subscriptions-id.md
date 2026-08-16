---
doc_id: webex-contact-center-delete-v1-subscriptions-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: DELETE
path: /v1/subscriptions/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.960540+00:00
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
- `id` [path] (string) **(requerido)**:
- `orgId` [query] (string): Organization ID to be used for this operation. If unspecified, the Organization ID is inferred from the token. The token must have permissions to interact with the organization.
- `TrackingId` [header] (string): Tracking ID to use for this operation, for traceability, debugging, and error reporting purposes. If not provided, we will generate one for you.

## Respuestas
- **204**: No Content
- **400**: Validation Error
- **401**: Unauthorized Operation
- **403**: Forbidden Operation
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
