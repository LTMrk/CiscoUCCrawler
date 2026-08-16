---
doc_id: webex-cloud-calling-get-people-personid-features-callingbehavior
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /people/{personId}/features/callingBehavior
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.638386+00:00
---

# GET /people/{personId}/features/callingBehavior

**API:** Webex Cloud Calling
**Área:** User Call Settings (1/2)
**operationId:** `Read Calling Behavior for a Person`

## Resumen
Read Person's Calling Behavior

## Descripción
Retrieves the calling behavior and UC Manager Profile settings for the person which includes overall calling behavior and calling UC Manager Profile ID.

Webex Calling Behavior controls which Webex telephony application and which UC Manager Profile is to be used for a person.

An organization has an organization-wide default Calling Behavior that may be overridden for individual persons.

UC Manager Profiles are applicable if your organization uses Jabber in Team Messaging mode or Calling in Webex (Unified CM).

The UC Manager Profile also has an organization-wide default and may be overridden for individual persons.

This API requires a full, user, or read-only administrator auth token with a scope of `spark-admin:people_read`.

## Parámetros
- `personId` [path] (string) **(requerido)**: Unique identifier for the person.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Respuestas
- **200**: OK
  - `behaviorType` (string): The current Calling Behavior setting for the person. If `null`, the effective Calling Behavior will be the Organization's current default.  * `NATIVE_WEBEX_TEAMS_CALLING` - Calling in Webex or Hybrid Calling.  * `CALL_WITH_APP_REGISTERED_FOR_CISCOTEL` - Cisco Jabber app  * `CALL_WITH_APP_REGISTERED_FOR_TEL` - Third-Party app  * `CALL_WITH_APP_REGISTERED_FOR_WEBEXCALLTEL` - Webex Calling app  * `NATIVE_SIP_CALL_TO_UCM` - Calling in Webex (Unified CM) Valores: NATIVE_WEBEX_TEAMS_CALLING, CALL_WITH_APP_REGISTERED_FOR_CISCOTEL, CALL_WITH_APP_REGISTERED_FOR_TEL, CALL_WITH_APP_REGISTERED_FOR_WEBEXCALLTEL, NATIVE_SIP_CALL_TO_UCM.
  - `effectiveBehaviorType` (string) **(requerido)**: The effective Calling Behavior setting for the person, will be the organization's default Calling Behavior if the user's `behaviorType` is set to `null`.  * `NATIVE_WEBEX_TEAMS_CALLING` - Calling in Webex or Hybrid Calling.  * `CALL_WITH_APP_REGISTERED_FOR_CISCOTEL` - Cisco Jabber app  * `CALL_WITH_APP_REGISTERED_FOR_TEL` - Third-Party app  * `CALL_WITH_APP_REGISTERED_FOR_WEBEXCALLTEL` - Webex Calling app  * `NATIVE_SIP_CALL_TO_UCM` - Calling in Webex (Unified CM) Valores: NATIVE_WEBEX_TEAMS_CALLING, CALL_WITH_APP_REGISTERED_FOR_CISCOTEL, CALL_WITH_APP_REGISTERED_FOR_TEL, CALL_WITH_APP_REGISTERED_FOR_WEBEXCALLTEL, NATIVE_SIP_CALL_TO_UCM.
  - `profileId` (string): The UC Manager Profile ID.
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
