---
doc_id: webex-admin-get-v1-analytics-roomdevicemetrics-dailytotals
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /v1/analytics/roomDeviceMetrics/dailyTotals
operation_id: Historical Data related to Room Devices
tags: Historical Analytics APIs
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.565507+00:00
---

# GET /v1/analytics/roomDeviceMetrics/dailyTotals

**API:** Webex Admin
**Área:** Historical Analytics APIs
**operationId:** `Historical Data related to Room Devices`

## Resumen
Historical Data related to Room Devices

## Descripción
Returns daily aggregates of various metrics related to Room Devices.

<div><Callout type="error">The base URL for these APIs is **analytics.webexapis.com**, which does not work with the **Try It** feature. </Callout></div>

## Parámetros
- `from` [query] (string): Starting UTC Date from which historical data should be returned. Por defecto: Data related to the date specified in 'to' if 'from' is not provided. If neither 'from' nor 'to' are provided then yesterday's data is returned..
- `to` [query] (string): Ending UTC Date for which data should be returned. Por defecto: Data from the date mentioned in 'from' parameter up to yesterday if 'to' parameter is not provided. Yesterday's data is returned if neither 'from' nor 'to' are provided. Yesterday is the latest day the data series will contain..

## Ejemplo de invocación
```bash
curl -X GET '/v1/analytics/roomDeviceMetrics/dailyTotals' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `startDate` (string): Data is returned starting from this UTC date.
- `endDate` (string): Data is returned up to this UTC date.
- `metrics` (object):
  - `dates` (string): An Array containing the UTC dates for which the data is returned
  - `totalActiveDevices` (string): An array containing the aggregated values for each day for which the data is returned.
  - `totalAssistantCommands` (string):
  - `totalUsageHours` (string):
  - `incallUsageDuration` (string):
  - `signageUsageDuration` (string):
  - `usbpassthroughUsageDuration` (string):
  - `whiteboardingUsageDuration` (string):
  - `video` (string):
  - `sharing` (object):
    - `localsharingcableUsageDuration` (string):
    - `localsharingwirelessUsageDuration` (string):
  - `recording` (string):
  - `audio` (string):

### Ejemplo — respuesta 200
```json
{
  "startDate": "2020-08-01",
  "endDate": "2020-08-03",
  "metrics": {
    "dates": "['2020-08-01','2020-08-02']",
    "totalActiveDevices": "[200,300]",
    "totalAssistantCommands": "[2,3]",
    "totalUsageHours": "[100,100]",
    "incallUsageDuration": "[50,50]",
    "signageUsageDuration": "[1,1]",
    "usbpassthroughUsageDuration": "[1,2]",
    "whiteboardingUsageDuration": "[3,4]",
    "video": "",
    "sharing": {
      "localsharingcableUsageDuration": "[1,1]",
      "localsharingwirelessUsageDuration": "[2,2]"
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