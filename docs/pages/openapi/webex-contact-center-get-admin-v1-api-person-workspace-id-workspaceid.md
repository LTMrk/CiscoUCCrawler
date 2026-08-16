---
doc_id: webex-contact-center-get-admin-v1-api-person-workspace-id-workspaceid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /admin/v1/api/person/workspace-id/{workspaceId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.969942+00:00
---

# GET /admin/v1/api/person/workspace-id/{workspaceId}

**API:** Webex Contact Center
**Área:** Journey - Customer Identification API
**operationId:** `getPersonDetails`

## Resumen
Get all or a specific Person Details

## Descripción
Get Person Details in JDS. If personId is provided by query parameter, this returns the Person whose personId matches the parameter.
If not, this will return ALL the Persons within the organization and workspace. 

Role and Scope: Requires id full admin role with cjp:config_write or cjp:config_read scope. Or it requires any role with cjp:user, cjp:config_write  or cjp:config_read scope.

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Workspace ID
- `personId` [query] (string): Person ID
- `filter` [query] (string): Optional filter which can be applied to the elements to be fetched.   This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see [this reference](https://developer.here.com/documentation/data-client-library/dev_guide/client/rsql.html). For a list of supported operators, see this [syntax guide](https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference).
- `sortBy` [query] (string): Sort By Field
- `sort` [query] (string): Sort direction
- `page` [query] (integer): Index of the page of results to be fetched.  Results are returned in blocks of pageSize elements. This parameter specifies which page number to retrieve. The page numbering starts with 0.
- `pageSize` [query] (integer): Number of items to be displayed on a page

## Respuestas
- **200**: Success
  - `meta` (object): Meta information of the response
    - `organizationId` (string): Organization ID
  - `data` (array): Data part of the response
    - `id` (string): Profile View Template Id
    - `firstName` (string): firstName
    - `lastName` (string): lastName
    - `phone` (array): Phone Number
    - `email` (array): Email
    - `temporaryId` (array): Temporary Id
    - `customerId` (array): Customer Id
    - `aliases` (array): Aliases
- **404**: Not found
- **500**: Internal error

**Autenticación:** bearerAuth

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
