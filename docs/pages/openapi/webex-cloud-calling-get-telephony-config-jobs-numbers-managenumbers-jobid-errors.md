---
doc_id: webex-cloud-calling-get-telephony-config-jobs-numbers-managenumbers-jobid-errors
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/jobs/numbers/manageNumbers/{jobId}/errors
operation_id: List Manage Numbers Job errors
tags: Numbers
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.314567+00:00
---

# GET /telephony/config/jobs/numbers/manageNumbers/{jobId}/errors

**API:** Webex Cloud Calling
**Área:** Numbers
**operationId:** `List Manage Numbers Job errors`

## Resumen
List Manage Numbers Job Errors

## Descripción
Lists all error details of Manage Numbers job. This will not list any errors if `exitCode` is `COMPLETED`. If the status is `COMPLETED_WITH_ERRORS` then this lists the cause of failures.

List of possible Errors:

+ BATCH-1017021 - Failed to move because it is an inactive number.

+ BATCH-1017022 - Failed to move because the source location and target location have different CCP providers.

+ BATCH-1017023 - Failed because it is not an unassigned number.

+ BATCH-1017024 - Failed because it is a main number.

+ BATCH-1017027 - Manage Numbers Move Operation is not supported.

+ BATCH-1017031 - Hydra request is supported only for single number move job.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `jobId` [path] (string) (**requerido**): Retrieve the error details for this `jobId`.
- `orgId` [query] (string): Retrieve list of jobs for this organization.
- `start` [query] (integer): Specifies the error offset from the first result that you want to fetch.
- `max` [query] (integer): Specifies the maximum number of records that you want to fetch. Por defecto: 2000.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/jobs/numbers/manageNumbers/<jobId>/errors' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
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

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "itemNumber": 1,
      "item": "+12025558374",
      "error": {
        "key": "400",
        "message": [
          {
            "description": "Failed because it is not an unassigned number.",
            "code": "BATCH-1017023",
            "locationid": "5223bbed-42c9-454d-a1f3-7fad5cc7e6e3"
          }
        ]
      },
      "trackingId": "ROUTER_6332cccb-e492-01bb-0165-48a3dc0a0165_0"
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
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs