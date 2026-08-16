---
doc_id: webex-contact-center-post-v1-realtime-subscribe
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/realtime/subscribe
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.960046+00:00
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
- `isKeepAliveEnabled` (boolean): This represents that a json message {\"keepalive\":\"true\"} is expected over the websocket connection from Client. This should be sent periodically (usually 4s). If there are no keep-alive messages from the client for a period of 15 seconds, the server will drop the websocket.
- `clientType` (string): ClientType is used to identify a web application differently from other web applications. It is used to group connections together for a specific user coming from that specific web application.
- `allowMultiLogin` (boolean): This cannot be used without providing \"clientType\". When set to true, it informs the server to allow multiple logins for this user coming from the same clientType. Upto 10 multiple logins will be allowed.
- `force` (boolean): When true, will drop a random connection and then subscribes if connections for a user exceed maximum limit. When allowMultiLogin is false and a multi-login is attempted, if set to true will drop all connections for that user of that clientType & then subscribes.

## Respuestas
- **200**: OK
  - `webSocketUrl` (string) **(requerido)**: Url used by the client to setup websocket.
  - `subscriptionId` (object) **(requerido)**: Id used by client to subscribe to interested events.
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
