---
doc_id: webex-contact-center-post-organization-orgid-auxiliary-code-bulk
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /organization/{orgid}/auxiliary-code/bulk
operation_id: saveAllConfig_20
tags: Auxiliary Code
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.778102+00:00
---

# POST /organization/{orgid}/auxiliary-code/bulk

**API:** Webex Contact Center
**Área:** Auxiliary Code
**operationId:** `saveAllConfig_20`

## Resumen
Bulk save Auxiliary Code(s)

## Descripción
Create, Update or delete Auxiliary Code(s) in bulk in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `items` (array):
  - `itemIdentifier` (integer/int32): Unique item identifier for a bulk operation.
  - `item` (object):
    - `organizationId` (string/uuid): ID of the contact center organization. It is required to define for the following operations - All bulk save operations Long. max: 36.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `name` (string) (**requerido**): A name for the code. Long. max: 80.
    - `description` (string): A short description indicating the context of the code. Long. max: 255.
    - `defaultCode` (boolean) (**requerido**): Indicates whether this is the default code(true) or not(false).  If this is the first idle or wrap-up code for your organization,it must be the default. It can be made non-default later once more codes are created.
    - `active` (boolean) (**requerido**): Indicates whether the code is active(when true) or not active(when false).   It is required only during a create or an update operation.
    - `isSystemCode` (boolean): Indicates whether this is the system default code(true) or not(false).
    - `workTypeId` (string) (**requerido**): Indicates the work type id associated with this code.
    - `workTypeCode` (string) (**requerido**): Indicates the work type associated with this code. Valores: IDLE_CODE, WRAP_UP_CODE.
    - `burnoutInclusion` (string): Indicates the idle code Inclusion status for agent burnout calculation. Default value is 'INCLUDED' for idle codes and 'NOT_APPLICABLE' for wrap up codes. Valores: NOT_APPLICABLE, EXCLUDED, INCLUDED.
    - `systemDefault` (boolean): Indicates whether the created resource is system created or not
    - `createdTime` (integer/int64) (solo lectura): Creation time(in epoch millis) of this resource.
    - `lastUpdatedTime` (integer/int64) (solo lectura): Time(in epoch millis) when this resource was last updated.
  - `requestAction` (string): Identifier for action type. Possible values can be SAVE and DELETE.

## Ejemplo de invocación
```bash
curl -X POST '/organization/<orgid>/auxiliary-code/bulk' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**207**: Multi-Status
- `items` (array):
  - `itemIdentifier` (integer/int32): Unique item identifier for a bulk operation.
  - `status` (integer/int32): Indicates the error status code.
  - `operationType` (string): The kind of operation desired of an entity. Valores: CREATE, UPDATE, DELETE, GET.
  - `href` (string): The resource URI of an entity.
  - `apiError` (object): Response body for an API error.
    - `trackingId` (string): An opaque identifier for mapping protocol failures to service internal codes.   When specified in a request, it can be used for co-relating events across services
    - `error` (object): Details of an error.
      - `key` (string): An application defined error code.
      - `message` (array): A message providing details about the error.
        - `description` (string): A human readable explanation for the occurrence of an error.

## Respuestas de error
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **409**: Similar entity is already present
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs