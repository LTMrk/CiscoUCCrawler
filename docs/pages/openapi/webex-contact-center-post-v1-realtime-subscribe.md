---
doc_id: webex-contact-center-post-v1-realtime-subscribe
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/realtime/subscribe
operation_id: subscribeRealtimeRoute
tags: Realtime
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-20T13:57:48.728129+00:00
---

# POST /v1/realtime/subscribe

**API:** Webex Contact Center
**Área:** Realtime
**operationId:** `subscribeRealtimeRoute`

## Resumen
Subscribe Realtime Notification

## Descripción
Access this endpoint when the user has to register for a WebSocket Session to receive realtime events. Requires 'cjp:user' scope or roles 'id_full_admin', 'id_readonly_admin', 'atlas-portal.partner.salesadmin', 'atlas-portal.partner.helpdesk', 'cjp.supervisor', 'cjp.admin', 'atlas-portal.partner.provision_admin' for authorization

## Cuerpo de la petición (application/json)
- `isKeepAliveEnabled` (boolean): This represents that a json message {\"keepalive\":\"true\"} is expected over the websocket connection from Client. This should be sent periodically (usually 4s). If there are no keep-alive messages from the client for a period of 15 seconds, the server will drop the websocket. Por defecto: True.
- `clientType` (string): ClientType is used to identify a web application differently from other web applications. It is used to group connections together for a specific user coming from that specific web application. Por defecto: DefaultClient. Long. max: 64.
- `allowMultiLogin` (boolean): This cannot be used without providing \"clientType\". When set to true, it informs the server to allow multiple logins for this user coming from the same clientType. Upto 10 multiple logins will be allowed. Por defecto: False. Long. max: 64.
- `force` (boolean): When true, will drop a random connection and then subscribes if connections for a user exceed maximum limit. When allowMultiLogin is false and a multi-login is attempted, if set to true will drop all connections for that user of that clientType & then subscribes. Por defecto: False. Long. max: 64.

## Ejemplo de invocación
```bash
curl -X POST '/v1/realtime/subscribe' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- `webSocketUrl` (string) (**requerido**): Url used by the client to setup websocket.
- `subscriptionId` (object/uuid) (**requerido**): Id used by client to subscribe to interested events.

## Respuestas de error
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs