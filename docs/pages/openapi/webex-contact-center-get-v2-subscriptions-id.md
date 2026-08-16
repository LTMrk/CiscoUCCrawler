---
doc_id: webex-contact-center-get-v2-subscriptions-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /v2/subscriptions/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.961072+00:00
---

# GET /v2/subscriptions/{id}

**API:** Webex Contact Center
**Área:** Subscriptions
**operationId:** `getSubscriptionByIdV2`

## Resumen
Get Subscription

## Descripción
Retrieve a subscription for a given subscription ID. Requires `cjp:config_read` scope.

## Parámetros
- `id` [path] (string) **(requerido)**:
- `orgId` [query] (string): Organization ID to be used for this operation. If unspecified, the Organization ID is inferred from the token. The token must have permissions to interact with the organization.
- `TrackingId` [header] (string): Tracking ID to use for this operation, for traceability, debugging, and error reporting purposes. If not provided, we will generate one for you.

## Respuestas
- **200**: OK
  - `meta` (object): Response metadata.
    - `orgId` (string): Organization ID to which resources belong.
  - `data` (object):
    - `id` (string) **(requerido)**: Subscription ID.
    - `name` (string) **(requerido)**: Client-defined string naming the subscription.
    - `description` (string): Client-defined string describing the subscription.
    - `eventTypes` (array) **(requerido)**: Types of events to which the subscription will listen.
    - `destinationUrl` (string) **(requerido)**: URL to which webhooks will be posted. Must be HTTPS on an IANA-listed top-level domain name (e.g. .com) with a path (at least /). No query parameters, userinfo, non-443 ports, or fragments allowed. We do not treat this field as sensitive data, so do not use secrets in this URL such as tokens or API keys.
    - `createdTime` (integer) **(requerido)**: Time when subscription was created (epoch milliseconds).
    - `createdBy` (string) **(requerido)**: Email address of the user who created the subscription.
    - `status` (string) **(requerido)**: Status of the subscription. Can be "active" or "inactive". The system may change the status to "inactive" in error scenarios. Valores: active, inactive.
    - `lastUpdatedTime` (integer) **(requerido)**: Time when the subscription was last updated (epoch milliseconds).
    - `lastUpdatedBy` (string) **(requerido)**: Email address of the user who updated the subscription most recently.
    - `resourceVersion` (string) **(requerido)**: Version of the resource.
- **400**: Validation Error
- **401**: Unauthorized Operation
- **403**: Forbidden Operation
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
