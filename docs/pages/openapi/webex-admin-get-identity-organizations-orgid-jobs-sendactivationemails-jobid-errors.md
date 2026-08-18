---
doc_id: webex-admin-get-identity-organizations-orgid-jobs-sendactivationemails-jobid-errors
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /identity/organizations/{orgId}/jobs/sendActivationEmails/{jobId}/errors
operation_id: Get Bulk Activation Email Resend Job Errors
tags: Send Activation Email
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.589476+00:00
---

# GET /identity/organizations/{orgId}/jobs/sendActivationEmails/{jobId}/errors

**API:** Webex Admin
**Área:** Send Activation Email
**operationId:** `Get Bulk Activation Email Resend Job Errors`

## Resumen
Get Bulk Activation Email Resend Job Errors

## Descripción
Get errors of an activation email resend job by its job ID.

Requires a full or user administrator auth token with a scope of `spark-admin:people_write` or read-only administrator auth token with a scope of `spark-admin:people_read`.

## Parámetros
- `orgId` [path] (string) (**requerido**): Check job status for this organization.
- `jobId` [path] (string) (**requerido**): Retrieve job status for this `jobId`.
- `max` [query] (number): Limit the maximum number of errors in the response. Por defecto: 50.

## Ejemplo de invocación
```bash
curl -X GET '/identity/organizations/<orgId>/jobs/sendActivationEmails/<jobId>/errors' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array):
  - `itemNumber` (number): Index of error.
  - `trackingId` (string): Unique identifier to track the HTTP request.
  - `error` (object):
    - `key` (string): HTTP status code.
    - `message` (array): List of error messages.
      - `description` (string): Error message.
      - `code` (string): Internal error code.
      - `locationId` (string): Not used.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "itemNumber": 1,
      "error": {
        "key": "304",
        "message": [
          {
            "description": "Re-send invite for 875ae291-3430-4ccb-85de-3db73ccb31d8 by bfb4b090-fcea-488a-94f0-0ec1897e20da is suppressed as the user 875ae291-3430-4ccb-85de-3db73ccb31d8 has already received an invitation email in last 24 hours ; Error with user@example.com.",
            "code": "ATLAS-600199",
            "locationId": null
          }
        ]
      },
      "trackingId": "NA_e0047e0e-804b-4cbc-817a-80c99d5a87a2_1_2"
    }
  ]
}
```
- Cabecera `Link`: 

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