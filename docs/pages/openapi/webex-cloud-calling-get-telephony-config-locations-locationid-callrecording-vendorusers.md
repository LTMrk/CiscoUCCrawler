---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-callrecording-vendorusers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/callRecording/vendorUsers
operation_id: getCallRecordingVendorUsersForALocation
tags: Features: Call Recording
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.485047+00:00
---

# GET /telephony/config/locations/{locationId}/callRecording/vendorUsers

**API:** Webex Cloud Calling
**Área:** Features: Call Recording
**operationId:** `getCallRecordingVendorUsersForALocation`

## Resumen
Get Call Recording Vendor Users for a Location

## Descripción
Retrieve call recording vendor users of a location. This API is used to get the list of users assigned to the call recording vendor of the location.

The Call Recording feature supports multiple third-party call recording providers, or vendors, to capture and manage call recordings. An organization is configured with an overall provider, but locations can be configured to use a different vendor than the overall organization default.

Requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieve vendor users for this location.
- `orgId` [query] (string): Retrieve vendor users for this organization.
- `max` [query] (number): Limit the number of vendor users returned to this maximum count. The default is 2000.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects. The default is 0.
- `standardUserOnly` [query] (boolean): If true, results only include Webex Calling standard users.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/callRecording/vendorUsers' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `vendorId` (string) (**requerido**): Call recording vendor ID.
- `members` (array) (**requerido**): Contains member details
  - `id` (string) (**requerido**): Unique identifier of the member.
  - `lastName` (string): Last name of the member.
  - `firstName` (string): First name of the member.
  - `type` (object) (**requerido**): Type of the member.
  - `licenseType` (object) (**requerido**): License type of the member.

### Ejemplo — respuesta 200
```json
{
  "vendorId": "Y2lzY29zcGFyazovL3VzL1JFQ09SRElOR19WRU5ET1IvMGE0MjY3NTQtYTQ3MC00YzJkLThiYTAtZmJjNjc3M2E4YTdj",
  "members": [
    {
      "id": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1BMQUNFL2U2OTczZDgyLWM1NTUtNDMwOC05NGU3LWI3ZWU2MjczY2YyMg",
      "lastName": "Last",
      "firstName": "HQ-Shared-Device",
      "type": "PLACE",
      "licenseType": "WORKSPACE"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xYzQ1Y2U0OC1hZWFmLTRmOGUtYmVlOS0zMjg5NDI2ZmYxZTY",
      "lastName": "Miller",
      "firstName": "Gary",
      "type": "PEOPLE",
      "licenseType": "PROFESSIONAL_USER"
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