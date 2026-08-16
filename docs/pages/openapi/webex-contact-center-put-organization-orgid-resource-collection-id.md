---
doc_id: webex-contact-center-put-organization-orgid-resource-collection-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PUT
path: /organization/{orgid}/resource-collection/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.947694+00:00
---

# PUT /organization/{orgid}/resource-collection/{id}

**API:** Webex Contact Center
**Área:** Resource Collection
**operationId:** `updateResourceCollection`

## Resumen
Update specific Resource Collection by ID

## Descripción
Update an existing resource collection by ID in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the Resource Collection.

## Cuerpo de la petición (application/json)
- `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) **(requerido)**: The name of the resource collection.
- `description` (string): An optional description of the resource collection.
- `resources` (array): The name of the resource and Type of resource list.
  - `name` (string) **(requerido)**: The name of the resource.multimedia-profile - Has access to multimedia profile[multimedia-profile] resource name.  queue - Has access to queue[queue] resource name.  override - Has access to override[override] resource name.  holiday-list - Has access to holiday list[holiday-list] resource name.  audio-prompt - Has access to audio prompt[audio-prompt] resource name.  flow - Has access to flow[flow] resource name.  skill-profile - Has access to skill profile[skill-profile] resource name.  team - Has access to team[team] resource name.  skill-definition - Has access to skill definition[skill-definition] resource name.  site - Has access to site[site] resource name.  outdial-ani - Has access to outdial ani[outdial-ani] resource name.  channel - Has access to channel[channel] resource name.  sub-flow - Has access to sub flow[sub-flow] resource name.  desktop-layout - Has access to desktop layout[desktop-layout] resource name.  working-hour - Has access to working hour[working-hour] resource name.  function - Has access to function[function] resource name.  desktop-profile - Has access to desktop profile[desktop-profile] resource name.  idle-wrapup-code - Has access to idle wrap-up code[idle-wrapup-code] resource name.  cad-variable - Has access to cad variable[cad-variable] resource name.  address-book - Has access to address book[address-book] resource name.
  - `accessLevel` (string) **(requerido)**: This can be used to allow users to access specific, none or all resources. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
  - `ids` (array): The id of the resource can be used to allow users to access specific, of resources.
- `resourceCount` (integer): The total count of resources in this collection
- `createdTime` (integer): This is the created time of the entity.
- `lastUpdatedTime` (integer): This is the updated time of the entity.

## Respuestas
- **200**: OK
  - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: The name of the resource collection.
  - `description` (string): An optional description of the resource collection.
  - `resources` (array): The name of the resource and Type of resource list.
    - `name` (string) **(requerido)**: The name of the resource.multimedia-profile - Has access to multimedia profile[multimedia-profile] resource name.  queue - Has access to queue[queue] resource name.  override - Has access to override[override] resource name.  holiday-list - Has access to holiday list[holiday-list] resource name.  audio-prompt - Has access to audio prompt[audio-prompt] resource name.  flow - Has access to flow[flow] resource name.  skill-profile - Has access to skill profile[skill-profile] resource name.  team - Has access to team[team] resource name.  skill-definition - Has access to skill definition[skill-definition] resource name.  site - Has access to site[site] resource name.  outdial-ani - Has access to outdial ani[outdial-ani] resource name.  channel - Has access to channel[channel] resource name.  sub-flow - Has access to sub flow[sub-flow] resource name.  desktop-layout - Has access to desktop layout[desktop-layout] resource name.  working-hour - Has access to working hour[working-hour] resource name.  function - Has access to function[function] resource name.  desktop-profile - Has access to desktop profile[desktop-profile] resource name.  idle-wrapup-code - Has access to idle wrap-up code[idle-wrapup-code] resource name.  cad-variable - Has access to cad variable[cad-variable] resource name.  address-book - Has access to address book[address-book] resource name.
    - `accessLevel` (string) **(requerido)**: This can be used to allow users to access specific, none or all resources. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
    - `ids` (array): The id of the resource can be used to allow users to access specific, of resources.
  - `resourceCount` (integer): The total count of resources in this collection
  - `createdTime` (integer): This is the created time of the entity.
  - `lastUpdatedTime` (integer): This is the updated time of the entity.
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **412**: Resource referred in other entity(s). Please get all the reference entities info by invoking Get incoming-references api.
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
