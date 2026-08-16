---
doc_id: webex-cloud-calling-get-telephony-config-jobs-devices-dynamicdevicesettings-jobid-errors
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/jobs/devices/dynamicDeviceSettings/{jobId}/errors
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.589742+00:00
---

# GET /telephony/config/jobs/devices/dynamicDeviceSettings/{jobId}/errors

**API:** Webex Cloud Calling
**Área:** Device Call Settings With Device Dynamic Settings
**operationId:** `listDynamicDeviceSettingsJobErrors`

## Resumen
List Device Dynamic Settings Job Errors

## Descripción
List Update device dynamic settings job errors.

Lists all error details of the job with `jobId` of `jobType` `dynamicdevicesettings`.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `jobId` [path] (string) **(requerido)**: Retrieve job details for this `jobId`.
- `orgId` [query] (string): Retrieve the status of job for this organization.
- `start` [query] (number): Specifies the offset from the first result that you want to fetch. Default is 0.
- `max` [query] (number): Specifies the maximum number of records that you want to fetch. Default is 2000

## Respuestas
- **200**: OK
  - `items` (array):
    - `item` (string): Phone number
    - `itemNumber` (number): Index of error number.
    - `trackingId` (string): Unique identifier to track the HTTP requests.
    - `error` (object):
      - `key` (string): HTTP error code.
      - `message` (array): Message string with further error information.
        - `description` (string): Error message.
        - `code` (string): Internal error code.
        - `locationId` (string): Error messages describing the location ID in which the error occurs. For a move operation, this is the target location ID.
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
