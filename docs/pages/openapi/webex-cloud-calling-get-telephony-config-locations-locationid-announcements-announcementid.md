---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-announcements-announcementid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/locations/{locationId}/announcements/{announcementId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.595862+00:00
---

# GET /telephony/config/locations/{locationId}/announcements/{announcementId}

**API:** Webex Cloud Calling
**Área:** Features: Announcement Repository
**operationId:** `Fetch details of a binary announcement greeting at location level`

## Resumen
Fetch details of a binary announcement greeting at location level

## Descripción
Fetch details of a binary announcement greeting by its ID at a location level.

An admin can upload a file at a location level. This file will be uploaded to the announcement repository.

This API requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Unique identifier of a location where an announcement is being created.
- `announcementId` [path] (string) **(requerido)**: Unique identifier of an announcement.
- `orgId` [query] (string): Fetch an announcement for location in this organization.

## Respuestas
- **200**: OK
  - `id` (string) **(requerido)**: Unique identifier of the announcement.
  - `name` (string) **(requerido)**: Name of the announcement.
  - `fileName` (string): File name of the uploaded binary announcement greeting.
  - `fileSize` (string) **(requerido)**: Size of the file in kilobytes.
  - `mediaFileType` (string) **(requerido)**: Media file type of the announcement file.
  - `lastUpdated` (string) **(requerido)**: Last updated timestamp (in UTC format) of the announcement.
  - `featureReferenceCount` (number) **(requerido)**: Reference count of the call features this announcement is assigned to.
  - `featureReferences` (array): Call features referenced by this announcement.
    - `id` (string) **(requerido)**: Unique identifier of the call feature referenced. The call Feature can be Auto Attendant, Call Queue or Music On hold.
    - `name` (string) **(requerido)**: Name of the call feature referenced.
    - `type` (string) **(requerido)**: Resource Type of the call feature.
    - `locationId` (string) **(requerido)**: Unique identifier of the location.
    - `locationName` (string) **(requerido)**: Location name of the announcement file.
  - `isTextToSpeech` (boolean): Indicates whether the announcement is text-to-speech.
  - `voice` (string): Voice used for text-to-speech announcement.
  - `language` (string): Language code for the text-to-speech announcement.
  - `text` (string): Text content for text-to-speech announcement.
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
