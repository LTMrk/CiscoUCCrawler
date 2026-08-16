---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-callrecording-vendor
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/locations/{locationId}/callRecording/vendor
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.609931+00:00
---

# PUT /telephony/config/locations/{locationId}/callRecording/vendor

**API:** Webex Cloud Calling
**Área:** Features: Call Recording
**operationId:** `setCallRecordingVendorForALocation`

## Resumen
Set Call Recording Vendor for a Location

## Descripción
Assign a call recording vendor to a location of an organization. Response will be `204` if the changes can be applied immediatley otherwise `200` with a job ID is returned.

The Call Recording feature supports multiple third-party call recording providers, or vendors, to capture and manage call recordings. An organization is configured with an overall provider, but locations can be configured to use a different vendor than the overall organization default.

Requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Update the call recording vendor for this location
- `orgId` [query] (string): Update the call recording vendor for this organization.

## Cuerpo de la petición (application/json)
- `id` (string): Unique identifier of the call recording vendor.
- `orgDefaultEnabled` (boolean): Vendor is enabled by default.
- `failureBehavior` (object): Type of failure behavior.
- `orgFailureBehaviorEnabled` (boolean): Failure behavior is enabled.

### Ejemplo de petición
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1JFQ09SRElOR19WRU5ET1IvMGE0MjY3NTQtYTQ3MC00YzJkLThiYTAtZmJjNjc3M2E4YTdj",
  "orgDefaultEnabled": false,
  "failureBehavior": "PROCEED_CALL_WITH_ANNOUNCEMENT",
  "orgFailureBehaviorEnabled": true
}
```

## Respuestas
- **200**: OK
  - `jobId` (string) **(requerido)**: Unique job ID of the call recording job.
- **204**: No Content
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
