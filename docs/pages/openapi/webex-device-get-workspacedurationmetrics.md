---
doc_id: webex-device-get-workspacedurationmetrics
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
method: GET
path: /workspaceDurationMetrics
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.136980+00:00
---

# GET /workspaceDurationMetrics

**API:** Webex Device
**Área:** Workspace Metrics
**operationId:** `Workspace Duration Metrics`

## Resumen
Workspace Duration Metrics

## Descripción
Get metrics for how much time a workspace has been in the state given by the `measurement` parameter.

For example, if the measurement is  `timeBooked` then the duration for which the workspace has been booked is returned. The `workspaceId` parameter indicates which workspace to fetch metrics for. If no `measurement` is given, the default value is `timeUsed`.

* When executing a query, the result bucket start times will default to the start of an hour or a day, depending on
the aggregation interval. However, the buckets will not contain data from outside the requested time range. For example, when
passing `from=2020-10-21T10:34:56.000Z` and `aggregation=hourly`, the first output bucket would start at `2020-10-21T10:00:00.000Z`,
but the bucket would only aggregate data timestamped after `10:34:56`.

* For aggregation mode `hourly`, the maximum time span is 48 hours. For aggregation mode `daily`, the maximum
time span is 30 days.

## Parámetros
- `workspaceId` [query] (string) **(requerido)**: ID of the workspace to get metrics for.
- `aggregation` [query] (string): Unit of time over which to aggregate measurements.
- `measurement` [query] (string): The measurement to return duration for.
- `from` [query] (string): Include data points after a specific date and time (ISO 8601 timestamp).
- `to` [query] (string): Include data points before a specific date and time (ISO 8601 timestamp).

## Respuestas
- **200**: OK
  - `workspaceId` (string) **(requerido)**:
  - `aggregation` (string):  Valores: hourly, daily.
  - `measurement` (string):  Valores: timeUsed, timeBooked.
  - `from` (string):
  - `to` (string):
  - `unit` (string): The time unit.
  - `items` (array):
    - `start` (string): Timestamp indicating the start of the aggregation bucket (ISO 8601).
    - `end` (string): Timestamp indicating the end of the aggregation bucket (ISO 8601).
    - `duration` (number): The time duration (in a given state) in the bucket.
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **410**: Gone: The requested resource is no longer available.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **423**: Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **428**: Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
