---
doc_id: webex-admin-get-workspacemetrics
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /workspaceMetrics
operation_id: Workspace Metrics
tags: Workspace Metrics
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.593885+00:00
---

# GET /workspaceMetrics

**API:** Webex Admin
**Área:** Workspace Metrics
**operationId:** `Workspace Metrics`

## Resumen
Workspace Metrics

## Descripción
Get metric data for the specified workspace and metric name, optionally aggregated over a specified time period.

* The `workspaceId` and `metricName` parameters indicate which workspace to fetch metrics for and what kind of metrics to get.

* When executing an aggregated query, the result bucket start times will be truncated to the start of an hour or a day, depending on
the aggregation interval. However, the buckets will not contain data from outside the requested time range. For example, when
passing `from=2020-10-21T10:34:56.000Z` and `aggregation=hourly`, the first output bucket would start at `2020-10-21T10:00:00.000Z`,
but the bucket would only aggregate data timestamped after `10:34:56`.

* For aggregation modes `none` and `hourly`, the maximum time span is 48 hours. For aggregation mode `daily`, the maximum
time span is 30 days.

* If the aggregation mode query parameter is set to `none`, the returned data in the response will be an array of items with the `deviceId`, `timestamp` and the raw `value`.

* If the aggregation mode is `hourly` or `daily`, the returned data in the response will be an array of items with the `start` and `end` of the aggregation time bucket, and the `mean`, `max` and `min` values of the requested value. Note that zeroes and negative values are ignored. For example, this means that the `peopleCount` mean value should be interpreted as the average number of people in the room _when it is in use_.

## Parámetros
- `workspaceId` [query] (string) (**requerido**): ID of the workspace to get metrics for.
- `metricName` [query] (string) (**requerido**): The type of data to extract. Valores: soundLevel, ambientNoise, temperature, humidity, tvoc, peopleCount.
- `aggregation` [query] (string): Time unit over which to aggregate measurements. Valores: none, hourly, daily. Por defecto: hourly.
- `from` [query] (string): List only data points after a specific date and time (ISO 8601 timestamp)
- `to` [query] (string): List data points before a specific date and time (ISO 8601 timestamp)
- `unit` [query] (string): Output data unit (only a valid parameter if `metricName` is `temperature`). Valores: celsius, fahrenheit. Por defecto: Celsius if the metricName parameter is set to "temperature". No default value is provided for other metric names..
- `sortBy` [query] (string): Sort results. Valores: newestFirst, oldestFirst. Por defecto: newestFirst.

## Ejemplo de invocación
```bash
curl -X GET '/workspaceMetrics?workspaceId=<workspaceId>&metricName=<metricName>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `workspaceId` (string) (**requerido**):
- `metricName` (string) (**requerido**):  Valores: soundLevel, ambientNoise, temperature, humidity, tvoc, peopleCount.
- `aggregation` (string):  Valores: none, hourly, daily.
- `from` (string):
- `to` (string):
- `unit` (string): Output data unit (only present if `metricName` is `temperature`). Valores: celsius, fahrenheit.
- `sortBy` (string):  Valores: newestFirst, oldestFirst.
- `items` (array): The structure of the elements will depend on whether or not aggregated data was requested

### Ejemplo — respuesta 200
```json
{
  "workspaceId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
  "metricName": "temperature",
  "aggregation": "hourly",
  "from": "2020-10-21T13:33:37.789Z",
  "to": "2020-10-31T16:00:00.532Z",
  "unit": "celsius",
  "sortBy": "newestFirst",
  "items": []
}
```

## Respuestas de error
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

## Contexto de la API
The Webex Admin APIs provide comprehensive programmatic access to administrative functions for managing Webex organizations, users, licenses, and settings. These APIs enable automation of user provisioning, license assignment, compliance management, and audit event retrieval. Administrators can integrate with enterprise identity systems, enforce security policies, monitor usage, and streamline onboarding/offboarding processes. The APIs support granular control over organizational resources, making them ideal for large-scale deployments and custom admin tooling.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs