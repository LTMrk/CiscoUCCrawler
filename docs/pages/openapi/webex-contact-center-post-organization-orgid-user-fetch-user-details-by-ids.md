---
doc_id: webex-contact-center-post-organization-orgid-user-fetch-user-details-by-ids
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /organization/{orgid}/user/fetch-user-details-by-ids
operation_id: getUserdataByIdsUser
tags: Users
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.125179+00:00
---

# POST /organization/{orgid}/user/fetch-user-details-by-ids

**API:** Webex Contact Center
**Área:** Users
**operationId:** `getUserdataByIdsUser`

## Resumen
List Users with details

## Descripción
Retrieve an existing User's first name, last name and email by list of IDs in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 10.

## Cuerpo de la petición (application/json)
- `userIds` (array): List of valid user IDs. Provide this only when both `search` and `queueId` are not provided.
- `search` (string): Text used to search for users (e.g., by firstName, lastName or email of the user). If provided, `queueId` is **required**. Cannot be used in combination with `userIds`.
- `queueId` (string): Agent Based Queue ID to filter users . Required if `search` is provided. Cannot be used with `userIds`.

## Ejemplo de invocación
```bash
curl -X POST '/organization/<orgid>/user/fetch-user-details-by-ids' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- `meta` (object): Metadata of response with paging information. Includes orgId, page, pageSize, totalPages, totalRecords, and pagination links.
- `data` (array): List of Data.
  - `id` (string): Unique ID of the user
  - `firstName` (string): First name of the user
  - `lastName` (string): Last name of the user
  - `email` (string): Email address of the user

### Ejemplo — respuesta 200
```json
{
  "meta": {
    "orgid": "2f9eecc5-0472-4549-9a83-2afdae0d4ba1",
    "page": 1,
    "pageSize": 100,
    "totalPages": 3,
    "totalRecords": 300
  },
  "data": [
    {
      "id": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
      "firstName": "John",
      "lastName": "Doe",
      "email": "john.doe@company.com"
    }
  ]
}
```
- `meta` (object): Metadata of response with paging information. Includes orgId, page, pageSize, totalPages, totalRecords, and pagination links.
- `data` (array): List of Data.
  - `id` (string): Unique ID of the user
  - `firstName` (string): First name of the user
  - `lastName` (string): Last name of the user
  - `email` (string): Email address of the user

### Ejemplo — respuesta 200
```json
{
  "meta": {
    "orgid": "2f9eecc5-0472-4549-9a83-2afdae0d4ba1",
    "page": 1,
    "pageSize": 100,
    "totalPages": 3,
    "totalRecords": 300
  },
  "data": [
    {
      "id": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
      "firstName": "John",
      "lastName": "Doe",
      "email": "john.doe@company.com"
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