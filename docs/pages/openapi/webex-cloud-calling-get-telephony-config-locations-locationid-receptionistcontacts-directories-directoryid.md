---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-receptionistcontacts-directories-directoryid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/locations/{locationId}/receptionistContacts/directories/{directoryId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.624059+00:00
---

# GET /telephony/config/locations/{locationId}/receptionistContacts/directories/{directoryId}

**API:** Webex Cloud Calling
**Área:** Location Call Settings
**operationId:** `Get details for a Receptionist Contact Directory`

## Resumen
Get details for a Receptionist Contact Directory

## Descripción
Get details for a specific Receptionist Contact Directory from a location.

Receptionist Contact Directories are uniquely named per location and contain directories of Persons, Auto Attendants, Call Queues, Hunt Groups, Single Number Reaches, and Paging Groups.

This API is currently supported for Webex calling organizations with fewer than 2000 users or location-based calling features. For organizations with more than 2000 users or location features, the API will throw an error 25395.

Retrieving details requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Get a Receptionist Contact Directory from this location.
- `directoryId` [path] (string) **(requerido)**: Get details for the Receptionist Contact Directory with this identifier.
- `orgId` [query] (string): Get a Receptionist Contact Directory from this organization.
- `searchCriteriaModeOr` [query] (boolean): When `true`, results matching any one of the search criteria are included. The value can only be `true` or not included in the request. Specifying `searchCriteriaModeOr` without any search criteria, or setting it to `false` results in an `ErrorResponse`. If no search criteria is specified, all results are returned.
- `firstName` [query] (string): Search for directories that contain people with the indicated first name.
- `lastName` [query] (string): Search for directories that contain people with the indicated last name.
- `phoneNumber` [query] (string): Search for directories that contain people with the indicated phone number.
- `extension` [query] (string): Search for directories that contain people with the indicated extension.
- `personId` [query] (string): Search for directories that contain people with the indicated person ID.

## Respuestas
- **200**: OK
  - `contacts` (array) **(requerido)**: Array of Receptionist Contact Directories.
    - `personId` (string) **(requerido)**: ID of person.
    - `firstName` (string): First name of person.
    - `lastName` (string): Last name of person.
    - `department` (string) **(requerido)**: Department ID of person.
    - `phoneNumber` (string) **(requerido)**: Phone number of person.
    - `extension` (string) **(requerido)**: Extension of person.
    - `locationId` (string) **(requerido)**: Location ID of person.
    - `featureId` (string) **(requerido)**: Location feature ID of the contact. Supported location feature types are Auto Attendant, Call Queue, Hunt Group, Single Number Reach, and Paging Group.
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
