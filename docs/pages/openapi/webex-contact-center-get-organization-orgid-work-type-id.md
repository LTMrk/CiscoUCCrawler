---
doc_id: webex-contact-center-get-organization-orgid-work-type-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/work-type/{id}
operation_id: getConfig
tags: Work Types
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.841773+00:00
---

# GET /organization/{orgid}/work-type/{id}

**API:** Webex Contact Center
**Área:** Work Types
**operationId:** `getConfig`

## Resumen
Get specific Work Type by ID

## Descripción
Retrieve an existing Work Type by ID in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) (**requerido**): ID of the work_type.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/work-type/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `organizationId` (string/uuid): ID of the contact center organization. It is required to define for the following operations - All bulk save operations Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): A name for the Work Type. Long. max: 80.
- `description` (string): A description for the Work type code created. Long. max: 255.
- `workTypeCode` (string) (**requerido**): Identifier for the Work Type being created. Can be 'WRAP_UP_CODE' or 'IDLE_CODE'.
- `active` (boolean) (**requerido**): Indicates whether the work type is active or not.
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
- `createdTime` (integer/int64) (solo lectura): Creation time(in epoch millis) of this resource.
- `lastUpdatedTime` (integer/int64) (solo lectura): Time(in epoch millis) when this resource was last updated.
- `organizationId` (string/uuid): ID of the contact center organization. It is required to define for the following operations - All bulk save operations Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): A name for the Work Type. Long. max: 80.
- `description` (string): A description for the Work type code created. Long. max: 255.
- `workTypeCode` (string) (**requerido**): Identifier for the Work Type being created. Can be 'WRAP_UP_CODE' or 'IDLE_CODE'.
- `active` (boolean) (**requerido**): Indicates whether the work type is active or not.
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
- `createdTime` (integer/int64) (solo lectura): Creation time(in epoch millis) of this resource.
- `lastUpdatedTime` (integer/int64) (solo lectura): Time(in epoch millis) when this resource was last updated.

## Respuestas de error
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs