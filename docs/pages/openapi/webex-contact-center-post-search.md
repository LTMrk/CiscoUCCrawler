---
doc_id: webex-contact-center-post-search
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /search
operation_id: getSearchResults
tags: Search
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-20T13:57:48.728327+00:00
---

# POST /search

**API:** Webex Contact Center
**Área:** Search
**operationId:** `getSearchResults`

## Resumen
Search tasks

## Descripción
The /search API is a GraphQL endpoint that enables customers to fetch data from Webex Contact Center.

**Authentication & Authorization:**
- **Required Scopes:** `cjp:config` or `cjp:config_read`
- **Required Roles:** Administrator or Supervisor

Mandatory parameters are FROM and TO, which accept datetime in epoch format. The FROM parameter cannot be older than 36 months from the current time. The TO parameter, if given as a future time, will be set to the current time. Optional parameters such as filter and aggregation are accepted for each query.

Response Compression: For this API, response compression using gzip can be enabled by including the 'Accept-Encoding' header in the request with its value as 'gzip'. The response will be compressed only if its size exceeds 1 MB. If the header is not present in the request or if gzip is not listed as one of the encodings in the header's value (comma-separated encodings), then the API response will not be compressed, impacting latency as observed from clients.

## Parámetros
- `orgId` [query] (string): Organization ID to use for this operation. If unspecified, inferred from token. Token must have permission to interact with this organization.
- `TrackingId` [header] (string): Tracking ID to use for this operation, for traceability, debugging, and error reporting purposes.

## Cuerpo de la petición (application/json)
- `variables` (object): The variables definition are the part that looks like task(from: $startTime, to: $endTime) in the query.   It works just like the argument definitions for a function in a typed language. These variables are applicable only for persisted queries that has these variables. An example of persisted query with variables - {   task (from: $startTime, to: $endTime, filter: {     and : [       {channelType : {equals: telephony}}      ]   } , pagination: {cursor:"0"}) {       tasks {         id         channelType       }   } }
- `query` (string): A graphQL query specifying the task attributes needed in the response for the specified time window. from: Start time for the query (in epoch milliseconds) and it cannot be older than 36 months from the current time. to: End time for the query (in epoch milliseconds) and it cannot be greater than the current time. The duration between to and from must not be more than 365 days.

## Ejemplo de invocación
```bash
curl -X POST '/search' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK

### Ejemplo — respuesta 200
```json
{
  "data": {
    "task": {
      "tasks": [
        {
          "id": "fb53f6d1-5535-4ac8-b081-53834e17d6f5",
          "channelType": "telephony",
          "createdTime": 1629450000000,
          "endedTime": 1630380960406,
          "captureRequested": true,
          "isActive": false,
          "status": "ended",
          "queue": [
            {
              "id": "e434a654-df4c-42dc-908b-3d9d0206a616",
              "name": "cb_outdial_queue"
            }
          ],
          "owner": {
            "name": "callbackorg2user1 callbackorg2user1",
            "id": "74ab6507-a32a-479c-bda7-15ff0b6c6c3c"
          }
        }
      ]
    }
  }
}
```

## Respuestas de error
- **400**: Validation Error
- **401**: Unauthorized Operation
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **413**: Content Too Large
- **422**: Unprocessable Entity
- **500**: An Unexpected Error Occurred
- **503**: The service is currently unavailable to serve the requests

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs