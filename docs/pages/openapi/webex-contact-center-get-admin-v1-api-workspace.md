---
doc_id: webex-contact-center-get-admin-v1-api-workspace
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /admin/v1/api/workspace
operation_id: getAllWorkspaces
tags: Journey - Workspace management API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.771875+00:00
---

# GET /admin/v1/api/workspace

**API:** Webex Contact Center
**Área:** Journey - Workspace management API
**operationId:** `getAllWorkspaces`
**Autenticación:** bearerAuth

## Resumen
Get All Workspaces

## Descripción
Get All Workspaces. Use the cjp scope if you have a contact center license; otherwise, use the cjds scope. It requires the appropriate cjds:admin_org_read or cjds:admin_org_write scopes or cjp:config_read or cjp:config_write scopes

## Parámetros
- `filter` [query] (string): Optional filter which can be applied to the elements to be fetched.   This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see [this reference](https://developer.here.com/documentation/data-client-library/dev_guide/client/rsql.html). For a list of supported operators, see this [syntax guide](https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference).
- `sortBy` [query] (string): Sort By Field
- `sort` [query] (string): Sort direction
- `page` [query] (integer): Index of the page of results to be fetched.  Results are returned in blocks of pageSize elements. This parameter specifies which page number to retrieve.The page numbering starts with 0.
- `pageSize` [query] (integer): Number of items to be displayed on a page.

## Ejemplo de invocación
```bash
curl -X GET '/admin/v1/api/workspace' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Ok
- `meta` (object): Meta information of the response
  - `organizationId` (string): Organization ID
- `data` (array): Data part of the response
  - `id` (string): Workspace ID
  - `name` (string): Workspace Name
  - `description` (string): Workspace Description
  - `wxccSubscriptionIds` (array): List of Wxcc Subscription Ids

## Respuestas de error
- **404**: Resource not found
- **409**: Resource already exists
- **429**: Too many requests
- **500**: Internal server error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs