---
doc_id: webex-cloud-calling-get-telephony-config-jobs-locations-deletecallinglocation-jobid-errors
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/jobs/locations/deleteCallingLocation/{jobId}/errors
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.625000+00:00
---

# GET /telephony/config/jobs/locations/deleteCallingLocation/{jobId}/errors

**API:** Webex Cloud Calling
**Área:** Location Call Settings
**operationId:** `Retrieve Errors For Disable Calling Location Job`

## Resumen
Retrieve Errors for a Disable Calling Location Job

## Descripción
Retrieve detailed error information for a disable calling location job. This is particularly useful for jobs that have failed or encountered errors during processing.

Retrieving job errors requires a full administrator auth token with a scope of `spark-admin:telephony_config_read`.

Possible error codes include:
* `BATCH-1012002` - Unable to delete calling location from Broadworks.
* `BATCH-1012004` - Safe delete checks failed.
* `BATCH-1012005` - Failed to perform safe delete checks.
* `BATCH-1012006` - Trunks in use in the location. Count: {0}
* `BATCH-1012007` - Users associated with the location. Count: {0}
* `BATCH-1012008` - Workspaces associated with the location. Count: {0}
* `BATCH-1012009` - Virtual lines associated with the location. Count: {0}
* `BATCH-1012010` - Number order is pending.
* `BATCH-1012011` - Features associated with the location. This is a blocking error, use forceDelete to disable the calling location.
* `BATCH-1012012` - Not allowed to delete the last calling location. Calling requires at least one active location in the organization, This is a blocking error.
* `BATCH-1012013` - Local gateway's associated with the location. Count: {0}. This is a blocking error, use forceDelete to disable the calling location.
* `BATCH-1012014` - Location not found.

## Parámetros
- `jobId` [path] (string) **(requerido)**: Unique identifier for the job to get errors for.
- `orgId` [query] (string): Organization ID for disable calling location job.

## Respuestas
- **200**: OK
  - `items` (array): List of error items.
    - `itemNumber` (integer): Sequential number of the error item.
    - `item` (string): The item that caused the error.
    - `errorType` (object):
    - `error` (object): Error details.
      - `key` (string): Error key or status code.
      - `message` (array): Array of error message details.
        - `description` (string): Error description.
        - `code` (string): Error code for disable calling location operations.
        - `locationId` (string): Related location ID, can be null.
    - `trackingId` (string): Tracking ID for the error.
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited.
- **500**: Internal Server Error: Something went wrong on the server.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
