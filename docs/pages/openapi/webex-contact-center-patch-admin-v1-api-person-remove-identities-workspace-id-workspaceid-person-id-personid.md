---
doc_id: webex-contact-center-patch-admin-v1-api-person-remove-identities-workspace-id-workspaceid-person-id-personid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PATCH
path: /admin/v1/api/person/remove-identities/workspace-id/{workspaceId}/person-id/{personId}
operation_id: removeIdentitiesFromPerson
tags: Journey - Customer Identification API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.863207+00:00
---

# PATCH /admin/v1/api/person/remove-identities/workspace-id/{workspaceId}/person-id/{personId}

**API:** Webex Contact Center
**Área:** Journey - Customer Identification API
**operationId:** `removeIdentitiesFromPerson`
**Autenticación:** bearerAuth

## Resumen
Remove one/more Identities from a person

## Descripción
This Patch Api can be used to remove identities(email, phone, customerId) from a person.

Role and Scope: Requires id full admin or any role with cjp:config_write scope.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Workspace ID
- `personId` [path] (string) (**requerido**): Person ID

## Cuerpo de la petición (application/json-patch+json)
- (array de:)

### Ejemplo — petición
```json
[
  "ram@cisco.com",
  "1e4qre2g7"
]
```

## Ejemplo de invocación
```bash
curl -X PATCH '/admin/v1/api/person/remove-identities/workspace-id/<workspaceId>/person-id/<personId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: Ok
- `meta` (object): Meta information of the response
  - `organizationId` (string): Organization ID
- `data` (object): Person Response Model
  - `id` (string): Profile View Template Id
  - `firstName` (string): firstName
  - `lastName` (string): lastName
  - `phone` (array): Phone Number
  - `email` (array): Email
  - `temporaryId` (array): Temporary Id
  - `customerId` (array): Customer Id
  - `aliases` (array): Aliases

## Respuestas de error
- **400**: Bad Request
- **401**: UnAuthorized
- **404**: Resource not found
- **500**: Internal server error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs