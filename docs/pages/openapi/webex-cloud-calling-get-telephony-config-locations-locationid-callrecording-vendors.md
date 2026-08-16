---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-callrecording-vendors
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/locations/{locationId}/callRecording/vendors
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.610044+00:00
---

# GET /telephony/config/locations/{locationId}/callRecording/vendors

**API:** Webex Cloud Calling
**Área:** Features: Call Recording
**operationId:** `getLocationCallRecordingVendors`

## Resumen
Get Location Call Recording Vendors

## Descripción
Retrieve details of the call recording vendor that the location is assigned and also a list of vendors.

The Call Recording feature supports multiple third-party call recording providers, or vendors, to capture and manage call recordings. An organization is configured with an overall provider, but locations can be configured to use a different vendor than the overall organization default.

Requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Retrieve vendor details for this location.
- `orgId` [query] (string): Retrieve vendor details for this organization.

## Respuestas
- **200**: OK
  - `orgDefaultEnabled` (boolean) **(requerido)**: Default call recording is enabled.
  - `orgDefaultVendorId` (string) **(requerido)**: Unique identifier of a vendor.
  - `orgDefaultVendorName` (string) **(requerido)**: Name of the call recording vendor.
  - `defaultVendorId` (string) **(requerido)**: Unique identifier of a vendor.
  - `defaultVendorName` (string) **(requerido)**: Name of the call recording vendor.
  - `vendors` (array) **(requerido)**: List of available vendors and their details.
    - `id` (string) **(requerido)**: Unique identifier of a vendor.
    - `name` (string) **(requerido)**: Name of a call recording vendor.
    - `description` (string) **(requerido)**: Describing some vendor info.
    - `migrateUserCreationEnabled` (boolean) **(requerido)**: Users can be migrated.
    - `loginUrl` (string) **(requerido)**: Login URL of the vendor.
    - `termsOfServiceUrl` (string) **(requerido)**: URL to vendor's terms of service.
  - `orgStorageRegionEnabled` (boolean): Region-based storage is enabled.
  - `orgStorageRegion` (string): Org level two character Region code.
  - `storageRegion` (string): Location level character Region code.
  - `orgFailureBehaviorEnabled` (boolean): Failure behavior is enabled.
  - `orgFailureBehavior` (object): Type of org-level failure behavior.
  - `failureBehavior` (object) **(requerido)**: Type of location level failure behavior.
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
