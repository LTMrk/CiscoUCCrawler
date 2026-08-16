---
doc_id: webex-cloud-calling-get-people-personid-features-privacy
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /people/{personId}/features/privacy
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.640339+00:00
---

# GET /people/{personId}/features/privacy

**API:** Webex Cloud Calling
**Área:** User Call Settings (1/2)
**operationId:** `Get Privacy Settings for a Person`

## Resumen
Get a person's Privacy Settings

## Descripción
Get a person's privacy settings for the specified person ID.

The privacy feature enables the person's line to be monitored by others and determine if they can be reached by Auto Attendant services.

This API requires a full, user, or read-only administrator or location administrator auth token with a scope of spark-admin:people_read.

## Parámetros
- `personId` [path] (string) **(requerido)**: Unique identifier for the person.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Respuestas
- **200**: OK
  - `aaExtensionDialingEnabled` (boolean): When `true` auto attendant extension dialing is enabled.
  - `aaNamingDialingEnabled` (boolean): When `true` auto attendant dialing by first or last name is enabled.
  - `enablePhoneStatusDirectoryPrivacy` (boolean): When `true` phone status directory privacy is enabled.
  - `enablePhoneStatusPickupBargeInPrivacy` (boolean): When `true` privacy is enforced for call pickup and barge-in. Only members specified by `monitoringAgents` can pickup or barge-in on the call.
  - `monitoringAgents` (array): List of people that are being monitored.
    - `id` (string): Unique identifier of the person.
    - `lastName` (string): Last name of the person.
    - `firstName` (string): First name of the person.
    - `displayName` (string): Display name of the person.
    - `type` (string): * `PEOPLE` - Person or list of people.  * `PLACE` - Workspace that is not assigned to a specific person such as for a shared device in a common area.  * `VIRTUAL_LINE` - Virtual line or list of virtual lines. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
    - `email` (string): Email address of the person.
    - `numbers` (array): List of phone numbers of the person.
      - `external` (string): External phone number of the person.
      - `extension` (string): Extension number of the person.
      - `routingPrefix` (string): Routing prefix of location.
      - `esn` (string): Routing prefix + extension of a person or workspace.
      - `primary` (boolean): If `true`, specifies whether the phone number is primary number.
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
