---
doc_id: webex-contact-center-post-admin-v1-api-person-merge-workspace-id-workspaceid-primary-person-id-primarypersonid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /admin/v1/api/person/merge/workspace-id/{workspaceId}/primary-person-id/{primaryPersonId}
operation_id: mergeAliases
tags: Journey - Customer Identification API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.863768+00:00
---

# POST /admin/v1/api/person/merge/workspace-id/{workspaceId}/primary-person-id/{primaryPersonId}

**API:** Webex Contact Center
**Área:** Journey - Customer Identification API
**operationId:** `mergeAliases`
**Autenticación:** bearerAuth

## Resumen
Merges Identities to a Primary Identity

## Descripción
Merges one/more Identities to a **Primary** Individual in JDS. 

Role and Scope: Requires id full admin role with cjp:config_write scope.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Workspace ID
- `primaryPersonId` [path] (string) (**requerido**): Primary Person ID

## Cuerpo de la petición (application/json)
- `personIdsToMerge` (array) (**requerido**): List of Person Ids to merge

## Ejemplo de invocación
```bash
curl -X POST '/admin/v1/api/person/merge/workspace-id/<workspaceId>/primary-person-id/<primaryPersonId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"personIdsToMerge": []}'
```

## Respuestas correctas
**202**: Accepted
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
- **404**: Not found
- **500**: Internal error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs