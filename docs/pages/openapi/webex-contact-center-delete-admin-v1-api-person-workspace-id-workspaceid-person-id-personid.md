---
doc_id: webex-contact-center-delete-admin-v1-api-person-workspace-id-workspaceid-person-id-personid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: DELETE
path: /admin/v1/api/person/workspace-id/{workspaceId}/person-id/{personId}
operation_id: deletePersonbyId
tags: Journey - Customer Identification API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.766332+00:00
---

# DELETE /admin/v1/api/person/workspace-id/{workspaceId}/person-id/{personId}

**API:** Webex Contact Center
**Área:** Journey - Customer Identification API
**operationId:** `deletePersonbyId`
**Autenticación:** bearerAuth

## Resumen
Delete specific Person by id

## Descripción
Delete Person Details searched by Person id in JDS. 

Role and Scope: Requires id full admin or any role with cjp:config_write scope

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Workspace ID
- `personId` [path] (string) (**requerido**): Person ID

## Ejemplo de invocación
```bash
curl -X DELETE '/admin/v1/api/person/workspace-id/<workspaceId>/person-id/<personId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Success
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
- **404**: Not found
- **500**: Internal error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs