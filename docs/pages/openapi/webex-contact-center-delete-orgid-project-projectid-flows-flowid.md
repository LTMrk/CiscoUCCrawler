---
doc_id: webex-contact-center-delete-orgid-project-projectid-flows-flowid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: DELETE
path: /{orgId}/project/{projectId}/flows/{flowId}
operation_id: deleteFlowUsingDELETE
tags: Flows
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.805147+00:00
---

# DELETE /{orgId}/project/{projectId}/flows/{flowId}

**API:** Webex Contact Center
**Área:** Flows
**operationId:** `deleteFlowUsingDELETE`

## Resumen
Delete a Flow or Subflow

## Descripción
Permanently deletes a flow or subflow. Flows deleted via this API are removed permanently and cannot be recovered.

Scope: `cjp:config_write`. Roles: [`Organizational Full Admin`, `Contact Center Service Admin`]

## Parámetros
- `orgId` [path] (string) (**requerido**): Organization ID.
- `projectId` [path] (string) (**requerido**): Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.
- `flowId` [path] (string) (**requerido**): ID of the flow/subflow to delete.
- `force` [query] (string): If 'yes', the flow is deleted even if it is still referenced by other entities. Defaults to 'no'. Por defecto: no.
- `skipRsEPCheck` [query] (boolean): If true, skips the check for routing strategy and entry point associations before deleting the flow. Por defecto: True.
- `flowType` [query] (string): Either of 'FLOW' or 'SUBFLOW'. Por defecto: FLOW.

## Ejemplo de invocación
```bash
curl -X DELETE '/<orgId>/project/<projectId>/flows/<flowId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK

### Ejemplo — respuesta 200
```json
"OK"
```

## Respuestas de error
- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **500**: Internal Server Error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs