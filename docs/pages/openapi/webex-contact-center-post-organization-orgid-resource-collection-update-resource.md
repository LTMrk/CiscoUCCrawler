---
doc_id: webex-contact-center-post-organization-orgid-resource-collection-update-resource
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/resource-collection/update-resource
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.947449+00:00
---

# POST /organization/{orgid}/resource-collection/update-resource

**API:** Webex Contact Center
**Área:** Resource Collection
**operationId:** `updateResourceToResourceCollection`

## Resumen
Update resource with default resource collection

## Descripción
Update resource with default resource collection. Ensure resource should not associated to any resource collection and resource should not be updated and not older than 15 min. Only single Resource Collection is allowed to update.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `resourceType` (string) **(requerido)**: Resource type.
- `resourceId` (string) **(requerido)**: Resource Id.
- `resourceCollections` (array): List of resource collections associated with the resource.
  - `id` (string) **(requerido)**: ID of this contact center resource.

## Respuestas
- **201**: Created
  - `response` (array): List of updated resources.
    - `id` (string) **(requerido)**: ID of this contact center resource.
    - `resourceType` (string) **(requerido)**: Name of the resource type.
    - `status` (integer): The HTTP status code.
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
