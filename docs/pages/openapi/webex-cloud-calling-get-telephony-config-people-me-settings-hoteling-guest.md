---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-hoteling-guest
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/hoteling/guest
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.576828+00:00
---

# GET /telephony/config/people/me/settings/hoteling/guest

**API:** Webex Cloud Calling
**Área:** Call Settings For Me Phase 5
**operationId:** `getHotelingGuestSettings`

## Resumen
Get Hoteling Guest Settings

## Descripción
Retrieve hoteling guest settings for a person. Hoteling allows a person to temporarily use a device as a guest, associating their extension and configuration with that device for a limited time. This API returns the current hoteling guest configuration including any active host association details.

Hoteling is a feature of Webex Calling that enables flexible workspace solutions by allowing users to log into shared devices.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Respuestas
- **200**: OK
  - `enabled` (boolean) **(requerido)**: Enable/Disable hoteling guest functionality for the person. When enabled, the person can associate themselves with a hoteling host device.
  - `associationLimitEnabled` (boolean): When enabled, the person's hoteling guest association will be automatically removed after the specified time period.
  - `associationLimitHours` (integer): Time limit in hours for the hoteling guest association (1-999). Applicable when associationLimitEnabled is true.
  - `hostAssociationLimitHours` (integer): Time limit in hours configured by the host for guest associations.
  - `hostEnforcedAssociationLimitEnabled` (boolean): Indicates whether the host has enforced an association time limit.
  - `hostFirstName` (string): First name of the hoteling host.
  - `hostLastName` (string): Last name of the hoteling host.
  - `hostId` (string): Unique identifier of the hoteling host person or workspace.
  - `hostPhoneNumber` (string): Phone number of the hoteling host.
  - `hostExtension` (string): Extension of the hoteling host.
  - `hostLocation` (object): Location information for the hoteling host.
    - `id` (string) **(requerido)**: Unique identifier of the hoteling host location.
    - `name` (string) **(requerido)**: Name of the hoteling host location.
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
