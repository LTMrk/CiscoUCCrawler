---
doc_id: webex-contact-center-post-search
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /search
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.960138+00:00
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

## Respuestas
- **200**: OK
- **400**: Validation Error
- **401**: Unauthorized Operation
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **413**: Content Too Large
- **422**: Unprocessable Entity
- **500**: An Unexpected Error Occurred
- **503**: The service is currently unavailable to serve the requests

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
