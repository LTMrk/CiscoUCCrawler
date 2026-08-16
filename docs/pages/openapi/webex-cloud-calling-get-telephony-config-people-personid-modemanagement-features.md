---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-modemanagement-features
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/{personId}/modeManagement/features
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.648738+00:00
---

# GET /telephony/config/people/{personId}/modeManagement/features

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `getListOfFeaturesAssignedToAUserModeManagement`

## Resumen
Retrieve the List of Features Assigned to a User for Mode Management

## Descripción
Retrieve a list of feature identifiers that are already assigned to a user for `Mode Management`. Feature identifiers reference feature instances like `Auto Attendants`, `Call Queues`, and `Hunt Groups`.
A maximum of 50 features can be assigned to a user for `Mode Management`.

Features with mode-based call forwarding enabled can be assigned to a user for `Mode Management`.

Retrieving this list requires a full, read-only, or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `personId` [path] (string) **(requerido)**: A unique identifier for the user.
- `orgId` [query] (string): Retrieve features list from this organization.

## Respuestas
- **200**: OK
  - `features` (array) **(requerido)**: Array of assigned features.
    - `id` (string) **(requerido)**: A unique identifier for the feature.
    - `name` (string) **(requerido)**: Unique name for the feature.
    - `type` (string) **(requerido)**: * `AUTO_ATTENDANT` - Specifies the feature is an Auto Attendant.  * `CALL_QUEUE` - Specifies the feature is a Call Queue.  * `HUNT_GROUP` - Specifies the feature is a Hunt Group. Valores: AUTO_ATTENDANT, CALL_QUEUE, HUNT_GROUP.
    - `phoneNumber` (string): The primary phone number configured for the feature.
    - `extension` (string): The extension configured for the feature.
    - `modeBasedForwardingEnabled` (boolean) **(requerido)**: A flag to indicate whether mode-based call forwarding is enabled for the feature.
    - `forwardDestination` (string): The destination for call forwarding if mode-based call forwarding is enabled.
    - `currentOperatingModeName` (string): Name of the current operating mode.
    - `currentOperatingModeId` (string): Unique identifier for the current operating mode.
    - `exceptionType` (string) **(requerido)**: * `MANUAL_SWITCH_BACK` - The mode was switched to or extended by the user for manual switch back and runs as an exception until the user manually switches the feature back to normal operation or a different mode.  * `AUTOMATIC_SWITCH_BACK_EARLY_START` - The mode was switched to by the user before its start time and runs as an exception until its end time is reached, at which point it automatically switches the feature back to normal operation.  * `AUTOMATIC_SWITCH_BACK_EXTENSION` - The current mode was extended by the user before its end time and runs as an exception until the extension end time (mode's end time + extension of up to 12 hours) is reached, at which point it automatically switches the feature back to normal operation.  * `AUTOMATIC_SWITCH_BACK_STANDARD` - The mode will remain the current operating mode for the feature until its normal end time is reached. Valores: MANUAL_SWITCH_BACK, AUTOMATIC_SWITCH_BACK_EARLY_START, AUTOMATIC_SWITCH_BACK_EXTENSION, AUTOMATIC_SWITCH_BACK_STANDARD.
    - `location` (object):
      - `id` (string) **(requerido)**: Location identifier associated with the members.
      - `name` (string) **(requerido)**: Location name associated with the member.
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
