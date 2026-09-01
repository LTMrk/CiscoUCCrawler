---
doc_id: webex-contact-center-get-organization-orgid-desktop-layout-id-incoming-references
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/desktop-layout/{id}/incoming-references
operation_id: getIncomingReferences_12
tags: Desktop Layout
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.659606+00:00
---

# GET /organization/{orgid}/desktop-layout/{id}/incoming-references

**API:** Webex Contact Center
**Área:** Desktop Layout
**operationId:** `getIncomingReferences_12`

## Resumen
List references for a specific Desktop Layout

## Descripción
Retrieve a list of all entities that have reference to an existing Desktop Layout by ID in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) (**requerido**): ID of this contact center resource.
- `type` [query] (string): Entity type of the other entity that has a reference to this specific entity.
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 100.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/desktop-layout/<id>/incoming-references' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `description` (string): Description about reference info.
- `meta` (object): Metadata of response for references with paging information
  - `orgid` (string/uuid): Org ID Long. max: 36.
  - `page` (integer/int32): Current page number
  - `pageSize` (integer/int32): Page size for current data set
  - `totalPages` (integer/int32): Number of pages
  - `totalRecords` (integer/int32): Total number of items
  - `links` (object): Map of pagination links with self, next, prev, last and first
  - `referencedEntities` (array): List of referenced entities
  - `currentEntity` (string): Name of current entity
- `data` (array):
  - `id` (string): id
  - `name` (string): name
  - `additionalAttributes` (object): A map containing additional attributes of entity where both the key and value are Strings.
  - `createdDate` (string):
  - `lastModifiedDate` (string):
  - `version` (integer/int32):

## Respuestas de error
- **401**: Unauthorized Operation
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "401",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "401",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **403**: Operation is forbidden
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "403",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "403",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **404**: Resource not found or URI is invalid
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "404",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "404",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "429",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "429",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **500**: An Unexpected Error Occurred
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "500",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "500",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs