---
doc_id: webex-contact-center-put-organization-orgid-auxiliary-code-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PUT
path: /organization/{orgid}/auxiliary-code/{id}
operation_id: updateConfig_24
tags: Auxiliary Code
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.779119+00:00
---

# PUT /organization/{orgid}/auxiliary-code/{id}

**API:** Webex Contact Center
**Área:** Auxiliary Code
**operationId:** `updateConfig_24`

## Resumen
Update specific Auxiliary Code by ID

## Descripción
Update an existing Auxiliary Code by ID in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) (**requerido**): Resource ID of the Auxiliary Code.

## Cuerpo de la petición (application/json)
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

## Ejemplo de invocación
```bash
curl -X PUT '/organization/<orgid>/auxiliary-code/<id>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"active": true, "defaultCode": true, "name": "<name>", "workTypeCode": "<workTypeCode>", "workTypeId": "<workTypeId>"}'
```

## Respuestas correctas
**200**: OK
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

## Respuestas de error
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **412**: Resource referred in other entity(s). Please get all the reference entities info by invoking Get incoming-references api.
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs