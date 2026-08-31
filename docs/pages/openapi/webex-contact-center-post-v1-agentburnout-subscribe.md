---
doc_id: webex-contact-center-post-v1-agentburnout-subscribe
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/agentburnout/subscribe
operation_id: subscribe_agentburnout
tags: Agent Wellbeing
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.045031+00:00
---

# POST /v1/agentburnout/subscribe

**API:** Webex Contact Center
**Área:** Agent Wellbeing
**operationId:** `subscribe_agentburnout`

## Resumen
Subscribe for realtime burnout events

## Descripción
This endpoint provides real-time burnout events that are generated for agents belonging to the organization. It gives us a WebSocket URL to which we can connect to receive the real-time burnout events.

## Parámetros
- `X-ORGANIZATION-ID` [header] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Client-defined string naming the subscription. Long. max: 64.
- `description` (string): Client-defined string describing the subscription. Long. max: 1024.
- `eventTypes` (array) (**requerido**): Types of events to which the subscription will listen.
- `destinationUrl` (string/uri) (**requerido**): URL to which webhooks will be posted. Must be HTTPS on an IANA-listed top-level domain name (e.g. .com) with a path (at least /). No query parameters, userinfo, non-443 ports, or fragments allowed. We do not treat this field as sensitive data, so do not use secrets in this URL such as tokens or API keys.
- `secret` (string): Secret string used to sign payloads sent to the destination URL. Long. max: 256.
- `orgId` (string/uuid): Organization ID to be used for this operation. If unspecified, the Organization ID is inferred from the token. The token must have permission to interact with the organization.

## Ejemplo de invocación
```bash
curl -X POST '/v1/agentburnout/subscribe' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"destinationUrl": "<destinationUrl>", "eventTypes": [], "name": "<name>"}'
```

## Respuestas correctas
**200**: Successful operation
- `id` (string/uuid) (**requerido**): Subscription ID.
- `name` (string) (**requerido**): Client-defined string naming the subscription. Long. max: 64.
- `description` (string): Client-defined string describing the subscription. Long. max: 1024.
- `eventTypes` (array) (**requerido**): Types of events to which the subscription will listen.
- `destinationUrl` (string/uri) (**requerido**): URL to which webhooks will be posted. Must be HTTPS on an IANA-listed top-level domain name (e.g. .com) with a path (at least /). No query parameters, userinfo, non-443 ports, or fragments allowed. We do not treat this field as sensitive data, so do not use secrets in this URL such as tokens or API keys.
- `createdTime` (integer/int64) (**requerido**): Time when subscription was created (epoch milliseconds).
- `createdBy` (string/email) (**requerido**): Email address of the user who created the subscription.
- `status` (string) (**requerido**): Status of the subscription. Can be "active" or "inactive". The system may change the status to "inactive" in error scenarios. Valores: active, inactive.
- `lastUpdatedTime` (integer/int64) (**requerido**): Time when the subscription was last updated (epoch milliseconds).
- `lastUpdatedBy` (string/email) (**requerido**): Email address of the user who updated the subscription most recently.

## Respuestas de error
- **400**: Validation Error
- **401**: Unauthorized Operation
- **403**: Forbidden Operation
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited.
- **500**: An Unexpected Error Occurred

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs