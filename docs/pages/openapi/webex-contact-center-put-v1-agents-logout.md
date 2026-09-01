---
doc_id: webex-contact-center-put-v1-agents-logout
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PUT
path: /v1/agents/logout
operation_id: logoutRoute
tags: Agents
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.705985+00:00
---

# PUT /v1/agents/logout

**API:** Webex Contact Center
**Área:** Agents
**operationId:** `logoutRoute`

## Resumen
Logout

## Descripción
Allows the user to logout from their Desktop. This API needs to be called once the WSS session has been successfully established. Requires 'cjp:user','id_full_admin','id_readonly_admin','atlas-portal.partner.salesadmin','cjp.admin','cjp.supervisor','atlas-portal.partner.provision_admin' scope for authorization. For a list of possible response messages, see the [Call Control API Guide](/docs/contact-control-apis).

## Cuerpo de la petición (application/json)
- `logoutReason` (string) (**requerido**): The reason for performing logout operation, maximum length 128 characters.
- `agentId` (string): Unique ID of the user who is being logged out, maximum length 36 characters.

## Ejemplo de invocación
```bash
curl -X PUT '/v1/agents/logout' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"logoutReason": "<logoutReason>"}'
```

## Respuestas correctas
**202**: The logout request was accepted for processing

## Respuestas de error
- **400**: Bad Request
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs