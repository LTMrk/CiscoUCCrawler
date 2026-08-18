---
doc_id: webex-admin-get-v1-analytics-messagingmetrics-dailytotals
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /v1/analytics/messagingMetrics/dailyTotals
operation_id: Historical Data related to Messaging
tags: Historical Analytics APIs
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.565332+00:00
---

# GET /v1/analytics/messagingMetrics/dailyTotals

**API:** Webex Admin
**Área:** Historical Analytics APIs
**operationId:** `Historical Data related to Messaging`

## Resumen
Historical Data related to Messaging

## Descripción
Returns daily aggregates of various metrics related to Webex messaging.

<div><Callout type="error">The base URL for these APIs is **analytics.webexapis.com**, which does not work with the **Try It** feature. </Callout></div>

## Parámetros
- `from` [query] (string): UTC date starting from which the data needs to be returned. Por defecto: Data related to the date mentioned in 'to' parameter if 'from' parameter is not provided. If neither 'from' nor 'to' are provided then yesterday's data is returned..
- `to` [query] (string): UTC date up to which the data needs to be returned Por defecto: Data from the date mentioned in 'from' parameter up to yesterday if 'to' parameter is not provided. If neither 'from' nor 'to' are provided then yesterday's data is returned. Yesterday's data would be the latest data returned..

## Ejemplo de invocación
```bash
curl -X GET '/v1/analytics/messagingMetrics/dailyTotals' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `startDate` (string): UTC start date of the data set.
- `endDate` (string): UTC end date of the data set.
- `metrics` (object):
  - `dates` (string): An Array containing the UTC dates for which the data is returned.
  - `dailyActiveUsers` (string): An array containing the aggregated values for each day for which the data is returned.
  - `totalMessagesSent` (string):
  - `deskTopMessagesSent` (string):
  - `mobileMessagesSent` (string):
  - `totalActiveSpaces` (string):
  - `groupActiveSpaces` (string):
  - `one2oneActiveSpaces` (string):
  - `video` (string):
  - `sharing` (object):
    - `totalFilesShared` (string):
    - `fileShareSize` (string):
  - `recording` (string):
  - `audio` (string):

### Ejemplo — respuesta 200
```json
{
  "startDate": "2020-08-01",
  "endDate": "2020-08-03",
  "metrics": {
    "dates": "['2020-08-01','2020-08-02']",
    "dailyActiveUsers": "[200, 300]",
    "totalMessagesSent": "[2000, 3000]",
    "deskTopMessagesSent": "[289, 456]",
    "mobileMessagesSent": "[122, 233]",
    "totalActiveSpaces": "[2,3]",
    "groupActiveSpaces": "[3,4]",
    "one2oneActiveSpaces": "[5,6]",
    "video": "",
    "sharing": {
      "totalFilesShared": "[1,2]",
      "fileShareSize": "`[6,7]` ## Bytes"
    },
    "recording": "",
    "audio": ""
  }
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