---
doc_id: webex-contact-center-post-orgid-project-projectid-flows-flowid-lock
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /{orgId}/project/{projectId}/flows/{flowId}:lock
operation_id: lockFlowUsingPOST
tags: Flows
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.713301+00:00
---

# POST /{orgId}/project/{projectId}/flows/{flowId}:lock

**API:** Webex Contact Center
**Área:** Flows
**operationId:** `lockFlowUsingPOST`

## Resumen
Lock a Flow or Subflow

## Descripción
Lock a flow to prevent concurrent edits by other users. Locks expire after 15 minutes of inactivity.

Scope: `cjp:config_write`. Roles: [`Organizational Full Admin`, `Contact Center Service Admin`]

## Parámetros
- `flowId` [path] (string) (**requerido**): Flow ID.
- `orgId` [path] (string) (**requerido**): Organization ID.
- `projectId` [path] (string) (**requerido**): Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.
- `flowType` [query] (string): Either of 'FLOW' or 'SUBFLOW'. Por defecto: FLOW.

## Ejemplo de invocación
```bash
curl -X POST '/<orgId>/project/<projectId>/flows/<flowId>:lock' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Lock confirmation with expiry information.

### Ejemplo — respuesta 200
```json
"OK"
```

## Respuestas de error
- **401**: Unauthorized.
- **403**: Forbidden.
- **404**: Not Found.
- **409**: Conflict — the flow is already locked by another user.
- **429**: Too Many Requests.

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs