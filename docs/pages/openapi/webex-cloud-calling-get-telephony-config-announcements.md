---
doc_id: webex-cloud-calling-get-telephony-config-announcements
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/announcements
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.594709+00:00
---

# GET /telephony/config/announcements

**API:** Webex Cloud Calling
**Área:** Features: Announcement Repository
**operationId:** `Fetch list of announcement greetings on location and organization level`

## Resumen
Fetch list of announcement greetings on location and organization level

## Descripción
Fetch a list of binary announcement greetings at an organization as well as location level.

An admin can upload a file at an organization level. This file will be uploaded to the announcement repository.

This API requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Get announcements in this organization.
- `locationId` [query] (string): Return the list of enterprise or Location announcement files. Without this parameter, the Enterprise level announcements are returned.
- `max` [query] (number): Limit the number of objects returned to this maximum count.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `order` [query] (string): Sort the list according to fileName or fileSize. The default sort will be in Ascending order.
- `fileName` [query] (string): Return the list of announcements with the given fileName.
- `fileType` [query] (string): Return the list of announcement files for this fileType.
- `mediaFileType` [query] (string): Return the list of announcement files for this mediaFileType.
- `name` [query] (string): Return the list of announcement files for this announcement label.

## Respuestas
- **200**: OK
  - `announcements` (array) **(requerido)**: Array of announcements.
    - `id` (string) **(requerido)**: Unique identifier of the announcement.
    - `name` (string) **(requerido)**: Name of the announcement.
    - `fileName` (string): File name of the uploaded binary announcement greeting.
    - `fileSize` (string) **(requerido)**: Size of the file in kilobytes.
    - `mediaFileType` (string) **(requerido)**: Media file type of the announcement file.
    - `lastUpdated` (string) **(requerido)**: LastUpdated timestamp (in UTC format) of the announcement.
    - `level` (string) **(requerido)**: The level at which this announcement exists. Valores: LOCATION, ORGANIZATION.
    - `location` (object):
      - `id` (string): The ID of the location.
      - `name` (string): The name of the location.
    - `isTextToSpeech` (boolean): Indicates whether the announcement is text-to-speech.
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
