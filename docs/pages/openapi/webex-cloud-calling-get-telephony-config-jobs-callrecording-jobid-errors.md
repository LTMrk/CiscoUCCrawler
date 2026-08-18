---
doc_id: webex-cloud-calling-get-telephony-config-jobs-callrecording-jobid-errors
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/jobs/callRecording/{jobId}/errors
operation_id: getJobErrorsForACallRecordingJob
tags: Features: Call Recording
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.311875+00:00
---

# GET /telephony/config/jobs/callRecording/{jobId}/errors

**API:** Webex Cloud Calling
**Área:** Features: Call Recording
**operationId:** `getJobErrorsForACallRecordingJob`

## Resumen
Get Job Errors for a Call Recording Job

## Descripción
Get errors for a call recording job in an organization.

The Call Recording feature supports multiple third-party call recording providers, or vendors, to capture and manage call recordings. An organization is configured with an overall provider, but locations can be configured to use a different vendor than the overall organization default.

Requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `jobId` [path] (string) (**requerido**): Retrieve job errors for this job.
- `orgId` [query] (string): Retrieve job errors for a call recording job in this organization.
- `max` [query] (number): Limit the number of errors returned to this maximum count. The default is 50.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/jobs/callRecording/<jobId>/errors' \
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
      "itemNumber": 0,
      "item": "5d320be1-e28c-420a-8935-1a54c7826eb4",
      "error": {
        "key": "500",
        "message": [
          {
            "description": "POST failed: HTTP/1.1 404 Not Found",
            "code": "404",
            "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzlmZTFmZDllLTlkM2QtNDUxZi04MDEwLTMwY2U1ZjRlNTYyNQ"
          }
        ]
      },
      "trackingId": "ADMINBATCHCLIENT_2830be24-766e-4a2a-be36-d289eb890322_0_3"
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