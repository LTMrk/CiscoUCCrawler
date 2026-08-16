---
doc_id: webex-contact-center-patch-organization-orgid-user-bulk-update-dynamic-skill-skillid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PATCH
path: /organization/{orgid}/user/bulk/update-dynamic-skill/{skillId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.954202+00:00
---

# PATCH /organization/{orgid}/user/bulk/update-dynamic-skill/{skillId}

**API:** Webex Contact Center
**Área:** Users
**operationId:** `patchDynamicSkillsUser`

## Resumen
Bulk partial update Users with dynamic skills

## Descripción
Assign or unassign a dynamic skill to/from multiple users in bulk for a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `skillId` [path] (string) **(requerido)**: Dynamic skill ID used for bulk update

## Cuerpo de la petición (application/json)
- `items` (array): List of items in the bulk request.
  - `itemIdentifier` (integer): Unique item identifier for a bulk operation.
  - `item` (object): Data transfer object for updating dynamic skills assigned to a user
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `userId` (string): The unique identifier of the user whose dynamic skills are being updated
    - `enumSkillValues` (array): Set of enumerated skill values for enum-type dynamic skills
    - `textValue` (string): Text value for text-type dynamic skills (maximum 100 characters)
    - `booleanValue` (boolean): Boolean value for boolean-type dynamic skills
    - `proficiencyValue` (integer): Proficiency value for proficiency-type dynamic skills (range: 0-10)
    - `skillId` (string): The unique identifier of the dynamic skill being updated
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
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
