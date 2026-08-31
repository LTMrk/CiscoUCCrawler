---
doc_id: webex-contact-center-post-organization-orgid-resource-collection-update-resource
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /organization/{orgid}/resource-collection/update-resource
operation_id: updateResourceToResourceCollection
tags: Resource Collection
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.105465+00:00
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
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `resourceType` (string) (**requerido**): Resource type.
- `resourceId` (string) (**requerido**): Resource Id.
- `resourceCollections` (array): List of resource collections associated with the resource.
  - `id` (string) (**requerido**): ID of this contact center resource.

## Ejemplo de invocación
```bash
curl -X POST '/organization/<orgid>/resource-collection/update-resource' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"resourceId": "<resourceId>", "resourceType": "<resourceType>"}'
```

## Respuestas correctas
**201**: Created
- `response` (array): List of updated resources.
  - `id` (string) (**requerido**): ID of this contact center resource.
  - `resourceType` (string) (**requerido**): Name of the resource type.
  - `status` (integer/int32): The HTTP status code.
  - `apiError` (object): Response body for an API error.
    - `trackingId` (string): An opaque identifier for mapping protocol failures to service internal codes.   When specified in a request, it can be used for co-relating events across services
    - `error` (object): Details of an error.
      - `key` (string): An application defined error code.
      - `message` (array): A message providing details about the error.
        - `description` (string): A human readable explanation for the occurrence of an error.

### Ejemplo — respuesta 201
```json
{
  "response": [
    {
      "id": "80f49a6e-11d7-4651-b730-99ed2f726f61",
      "resourceType": "team",
      "status": 200
    },
    {
      "id": "90f49a6e-11d7-4651-b730-99ed2f726f62",
      "resourceType": "desktop-profile",
      "status": 400,
      "apiError": {
        "trackingId": "ccconfig_7113a3e7-bc11-43f2-9f2d-ded48e8685cd",
        "error": {
          "key": "400",
          "reason": "400 BAD_REQUEST \"Entity not found or more than one entity found on the unique fields\"",
          "message": [
            {
              "description": "400 BAD_REQUEST \"Entity not found or more than one entity found on the unique fields\""
            }
          ]
        }
      }
    }
  ]
}
```

## Respuestas de error
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "400",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "400",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **401**: Unauthorized Operation
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "401",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "401",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **403**: Operation is forbidden
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "403",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "403",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **409**: Similar entity is already present
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "409",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "409",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "429",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "429",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **500**: An Unexpected Error Occurred
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "500",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "500",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs