---
doc_id: webex-contact-center-get-organization-orgid-desktop-layout-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/desktop-layout/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.937914+00:00
---

# GET /organization/{orgid}/desktop-layout/{id}

**API:** Webex Contact Center
**Área:** Desktop Layout
**operationId:** `getConfig_14`

## Resumen
Get specific Desktop Layout by ID

## Descripción
Retrieve an existing Desktop Layout by ID in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the Desktop Layout.

## Respuestas
- **200**: OK
  - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: A name for the Desktop Layout.
  - `description` (string): A short description indicating the context of the Desktop Layout.
  - `editedBy` (string) **(requerido)**: Indicates who modified the Desktop Layout.
  - `jsonFileName` (string) **(requerido)**: Enter the name of the file.
  - `jsonFileContent` (string) **(requerido)**: Enter the Desktop Layout json.
  - `global` (boolean) **(requerido)**: Indicates if the Desktop Layout is a global layout or a custom layout.
  - `status` (boolean) **(requerido)**: Indicates if the Desktop Layout is in active state or inactive.
  - `defaultJsonModified` (boolean) **(requerido)**: Indicates if the default Desktop Layout is modified.
  - `validated` (boolean) **(requerido)**: Indicates if the Desktop Layout is validated.
  - `validatedTime` (integer): Validated time(in epoch milliseconds) of this resource.
  - `defaultJsonModifiedTime` (integer): Default Json Modified time(in epoch milliseconds) of this resource.
  - `modifiedTime` (integer): Modified time(in epoch milliseconds) of this resource.
  - `teamIds` (array): Specify the teams id to assign to this Desktop Layout.
  - `systemDefault` (boolean): Indicates whether the created resource is system created or not
  - `createdTime` (integer): This is the created time of the entity.
  - `lastUpdatedTime` (integer): This is the updated time of the entity.
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
