---
doc_id: webex-contact-center-put-v2-agents-logout
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PUT
path: /v2/agents/logout
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.962227+00:00
---

# PUT /v2/agents/logout

**API:** Webex Contact Center
**Área:** Agents
**operationId:** `LogoutRoute`

## Resumen
Logout

## Descripción
Allows the user to logout from their Desktop. This API needs to be called once the WSS session has been successfully established. Requires 'cjp:user','id_full_admin','id_readonly_admin','atlas-portal.partner.salesadmin','cjp.admin','cjp.supervisor','atlas-portal.partner.provision_admin' scope for authorization. For a list of possible response messages, see the [Call Control API Guide](/documentation/guides/contact-control-apis).

## Parámetros
- `Authorization` [header] (string) **(requerido)**: The bearer token would be sent to validate the active users.

## Cuerpo de la petición (application/json)
- `logoutReason` (string) **(requerido)**: The reason for performing logout operation, maximum length 128 characters.
- `agentId` (string): Unique ID of the user who is being logged out, maximum length 36 characters.

## Respuestas
- **202**: The logout request was accepted for processing
- **400**: Bad Request
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
