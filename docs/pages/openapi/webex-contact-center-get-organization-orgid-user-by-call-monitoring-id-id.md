---
doc_id: webex-contact-center-get-organization-orgid-user-by-call-monitoring-id-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/user/by-call-monitoring-id/{id}
operation_id: getUsersByCallMonitoringIdUser
tags: Users
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.730370+00:00
---

# GET /organization/{orgid}/user/by-call-monitoring-id/{id}

**API:** Webex Contact Center
**Área:** Users
**operationId:** `getUsersByCallMonitoringIdUser`

## Resumen
List users by call monitoring id

## Descripción
Fetch paginated users associated to the selected call monitoring team filters while enforcing team ACL.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) (**requerido**): Resource ID of the call monitoring.
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 100.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/user/by-call-monitoring-id/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `meta` (object): Meta Data Paged User schema.
  - `orgid` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `page` (integer/int32): Current page number.
  - `pageSize` (integer/int32): Page size for current data set.
  - `totalPages` (integer/int32): Number of pages.
  - `totalRecords` (integer/int64): Total number of items.
  - `links` (object):
    - `self` (string) (**requerido**): Link to the current page.
    - `first` (string): Link to the first page.
    - `last` (string): Link to the last page.
    - `next` (string): Link to the next page.
    - `prev` (string): Link to the previous page.
  - `actualBurnoutInclusionCount` (integer/int64): Indicates the actual count of Agents selected for Agent burnout detection, including restricted agents that are not visible to requesting user.
  - `actualAutoCSATCount` (integer/int64): Indicates the actual count of Agents selected for Auto CSAT scores, including restricted agents that are not visible to requesting user.
  - `actualSummariesCount` (integer/int64): Indicates the actual count of Agents selected for Generated Summaries, including restricted agents that are not visible to requesting user.
- `data` (array):
  - `id` (string): Unique ID of the user
  - `firstName` (string): First name of the user
  - `lastName` (string): Last name of the user
  - `email` (string): Email address of the user
- `meta` (object): Meta Data Paged User schema.
  - `orgid` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `page` (integer/int32): Current page number.
  - `pageSize` (integer/int32): Page size for current data set.
  - `totalPages` (integer/int32): Number of pages.
  - `totalRecords` (integer/int64): Total number of items.
  - `links` (object):
    - `self` (string) (**requerido**): Link to the current page.
    - `first` (string): Link to the first page.
    - `last` (string): Link to the last page.
    - `next` (string): Link to the next page.
    - `prev` (string): Link to the previous page.
  - `actualBurnoutInclusionCount` (integer/int64): Indicates the actual count of Agents selected for Agent burnout detection, including restricted agents that are not visible to requesting user.
  - `actualAutoCSATCount` (integer/int64): Indicates the actual count of Agents selected for Auto CSAT scores, including restricted agents that are not visible to requesting user.
  - `actualSummariesCount` (integer/int64): Indicates the actual count of Agents selected for Generated Summaries, including restricted agents that are not visible to requesting user.
- `data` (array):
  - `id` (string): Unique ID of the user
  - `firstName` (string): First name of the user
  - `lastName` (string): Last name of the user
  - `email` (string): Email address of the user

## Respuestas de error
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
- **404**: Resource not found or URI is invalid
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "404",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "404",
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