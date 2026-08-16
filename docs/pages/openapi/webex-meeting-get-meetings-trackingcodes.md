---
doc_id: webex-meeting-get-meetings-trackingcodes
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /meetings/trackingCodes
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.399501+00:00
---

# GET /meetings/trackingCodes

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `getMeetingHostTrackingCodes`

## Resumen
List Meeting Tracking Codes

## Descripción
Lists tracking codes on a site by a meeting host. The result indicates which tracking codes and what options can be used to create or update a meeting on the specified site.

* The `options` here differ from those in the [site-level tracking codes](/docs/api/v1/tracking-codes/get-a-tracking-code) and the [user-level tracking codes](/docs/api/v1/tracking-codes/get-user-tracking-codes). It is the result of a selective combination of the two.

* For a tracking code, if there is no user-level tracking code, the API returns the site-level options, and the `defaultValue` of the site-level default option is `true`. If there is a user-level tracking code, it is merged into the `options`. Meanwhile, the `defaultValue` of this user-level option is `true` and the site-level default option becomes non default.

* If `siteUrl` is specified, tracking codes of the specified site will be listed; otherwise, tracking codes of the user's preferred site will be listed. All available Webex sites and the preferred sites of a user can be retrieved by [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

## Parámetros
- `siteUrl` [query] (string): URL of the Webex site which the API retrieves the tracking code from. If not specified, the API retrieves the tracking code from the user's preferred site. All available Webex sites and preferred sites of a user can be retrieved by [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.
- `service` [query] (string) **(requerido)**: Service for schedule or sign-up pages.
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if a user or application calling the API has the admin-level scopes. The admin may specify the email of a user on a site they manage and the API will return meeting participants of the meetings that are hosted by that user.

## Respuestas
- **200**: OK
  - `items` (array): Tracking code array.
    - `id` (string) **(requerido)**: Unique identifier for the tracking code.
    - `name` (string) **(requerido)**: Name for the tracking code.
    - `siteUrl` (string) **(requerido)**: Site URL for the tracking code.
    - `options` (array) **(requerido)**: Tracking code option list. The options here differ from those in the [site-level tracking codes](/docs/api/v1/tracking-codes/get-a-tracking-code) and the [user-level tracking codes](/docs/api/v1/tracking-codes/get-user-tracking-codes). It is the result of a selective combination of the two. If there's user-level value for a tracking code, the user-level value becomes the default option for the tracking code, and the site-level default value becomes non-default.
      - `value` (string) **(requerido)**: The value of a tracking code option. `value` cannot be empty and the maximum size is 120 characters.
      - `defaultValue` (boolean) **(requerido)**: Whether or not the option is the default option of a tracking code.
    - `inputMode` (string) **(requerido)**: The input mode in which the tracking code value can be assigned.  * `text` - Text input.  * `select` - Drop down list which requires `options`.  * `editableSelect` - Both text input and select from list.  * `hostProfileSelect` - An input method which is only available for the host profile and sign-up pages. Valores: text, select, editableSelect, hostProfileSelect.
    - `service` (string) **(requerido)**: Service for schedule or sign up pages  * `All` - Tracking codes apply to all services.  * `MeetingCenter` - Users can set tracking codes when scheduling a meeting.  * `EventCenter` - Users can set tracking codes when scheduling an event.  * `TrainingCenter` - Users can set tracking codes when scheduling a training session.  * `SupportCenter` - Users can set tracking codes when scheduling a support meeting. Valores: All, MeetingCenter, EventCenter, TrainingCenter, SupportCenter.
    - `type` (string) **(requerido)**: Type for meeting scheduler or meeting start pages.  * `optional` - Available to be chosen but not compulsory.  * `required` - Officially compulsory.  * `adminSet` - The value is set by admin.  * `notUsed` - The value cannot be used.  * `notApplicable` - This value only applies to the service of `All`. When the type of `All` for a tracking code is `notApplicable`, there are different types for different services. For example, `required` for `MeetingCenter`, `optional` for `EventCenter` and `notUsed` for others. Valores: optional, required, adminSet, notUsed, notApplicable.
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found
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
