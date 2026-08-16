---
doc_id: webex-contact-center-post-organization-orgid-desktop-layout-bulk
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/desktop-layout/bulk
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.937700+00:00
---

# POST /organization/{orgid}/desktop-layout/bulk

**API:** Webex Contact Center
**Área:** Desktop Layout
**operationId:** `saveAllConfig_13`

## Resumen
Bulk save Desktop Layout(s)

## Descripción
Create, Update or delete Desktop Layout(s) in bulk in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `items` (array): List of items in the bulk request.
  - `itemIdentifier` (integer): Unique item identifier for a bulk operation.
  - `item` (object):
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
  - `requestAction` (string): Identifier for action type. Possible values are `SAVE` and `DELETE`.

## Respuestas
- **207**: Multi-Status
  - `items` (array):
    - `itemIdentifier` (integer): Unique item identifier for a bulk operation.
    - `status` (integer): Indicates the error status code.
    - `operationType` (string): The kind of operation desired of an entity. Valores: CREATE, UPDATE, DELETE, GET.
    - `href` (string): The resource URI of an entity.
    - `apiError` (object): Response body for an API error.
      - `trackingId` (string): An opaque identifier for mapping protocol failures to service internal codes.   When specified in a request, it can be used for co-relating events across services
      - `error` (object): Details of an error.
        - `key` (string): An application defined error code.
        - `message` (array): A message providing details about the error.
          - `description` (string): A human readable explanation for the occurrence of an error.
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **409**: Similar entity is already present
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
