---
doc_id: webex-admin-get-workspacedurationmetrics
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /workspaceDurationMetrics
operation_id: Workspace Duration Metrics
tags: Workspace Metrics
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.594092+00:00
---

# GET /workspaceDurationMetrics

**API:** Webex Admin
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
- `workspaceId` [query] (string) (**requerido**): ID of the workspace to get metrics for.
- `aggregation` [query] (string): Unit of time over which to aggregate measurements. Valores: hourly, daily. Por defecto: hourly.
- `measurement` [query] (string): The measurement to return duration for. Valores: timeUsed, timeBooked. Por defecto: timeUsed.
- `from` [query] (string): Include data points after a specific date and time (ISO 8601 timestamp).
- `to` [query] (string): Include data points before a specific date and time (ISO 8601 timestamp).

## Ejemplo de invocación
```bash
curl -X GET '/workspaceDurationMetrics?workspaceId=<workspaceId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `workspaceId` (string) (**requerido**):
- `aggregation` (string):  Valores: hourly, daily.
- `measurement` (string):  Valores: timeUsed, timeBooked.
- `from` (string):
- `to` (string):
- `unit` (string): The time unit.
- `items` (array):
  - `start` (string): Timestamp indicating the start of the aggregation bucket (ISO 8601).
  - `end` (string): Timestamp indicating the end of the aggregation bucket (ISO 8601).
  - `duration` (number): The time duration (in a given state) in the bucket.

### Ejemplo — respuesta 200
```json
{
  "workspaceId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
  "aggregation": "hourly",
  "measurement": "timeBooked",
  "from": "2020-10-21T13:33:37.789Z",
  "to": "2020-10-31T16:00:00.532Z",
  "unit": "minutes",
  "items": [
    {
      "start": "2021-10-21T12:00:00Z",
      "end": "2021-10-21T13:00:00Z",
      "duration": 13
    }
  ]
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