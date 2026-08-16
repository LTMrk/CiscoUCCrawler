---
doc_id: webex-contact-center-post-admin-v1-api-person-merge-identities-workspace-id-workspaceid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /admin/v1/api/person/merge-identities/workspace-id/{workspaceId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.970282+00:00
---

# POST /admin/v1/api/person/merge-identities/workspace-id/{workspaceId}

**API:** Webex Contact Center
**Área:** Journey - Customer Identification API
**operationId:** `mergeIdentities`

## Resumen
Creates or merges aliases to an Individual in JDS

## Descripción
This API enables you to consolidate multiple customer identifiers into a single, unified profile effortlessly. By integrating it with your Flow Designer, you can automatically retrieve and merge customer identifiers from various systems, such as your CRM or other third-party tools. This integration ensures all relevant data is consolidated into one profile, enhancing personalization and streamlining customer interactions. 

**Adding a New Alias** - To associate an additional alias (e.g., a new phone number) with an existing customer profile, simply update the API with the new identifier while leaving the existing identifiers intact. The system will automatically merge the new alias into the current profile, maintaining a comprehensive view of the customer.

**Removing an Alias** - If you need to delete an alias from a customer’s profile, set the override flag to true in your API request. Include only the identifiers you wish to retain in the payload. The system will remove any identifiers not included in the updated payload, keeping the profile streamlined and up-to-date.

Role and Scope: Requires id full admin OR any role with cjp:config_write scope.

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Workspace ID

## Cuerpo de la petición (application/json)
- `override` (boolean): Override flag which will override the existing person with the new data if set to true. Default is false.
- `firstName` (string): firstName
- `lastName` (string): lastName
- `phone` (array): Phone Number
- `email` (array): Email
- `temporaryId` (array): Temporary Id
- `customerId` (array): Customer Id
- `socialId` (array): Social Id

## Respuestas
- **200**: OK
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
- **400**: Bad Request
- **404**: Not found
- **500**: Internal error

**Autenticación:** bearerAuth

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
