---
doc_id: webex-meeting-post-admin-meeting-config-trackingcodes
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: POST
path: /admin/meeting/config/trackingCodes
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.400093+00:00
---

# POST /admin/meeting/config/trackingCodes

**API:** Webex Meetings
**Área:** Tracking Codes
**operationId:** `Create a Tracking Code`

## Resumen
Create a Tracking Code

## Descripción
Create a new tracking code by an admin user.

* The `siteUrl` is required. The operation creates a tracking code for the specified site. All or a user's available Webex sites can be retrieved by the [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

* The `inputMode` of `hostProfileSelect` is only available for a host profile and sign-up pages and does not apply to the meeting scheduler page or the meeting start page. The value for `scheduleStartCodes` must be `null` or the value for all services must be `notUsed` when the `inputMode` is `hostProfileSelect`.

* The `hostProfileCode` of `required` is only allowed for a Site Admin managed site, and not for a Control Hub managed site.

* When the `hostProfileCode` is `adminSet`, only `adminSet`, `notUsed`, and `notApplicable` are available for the types of `scheduleStartCodes`. When the `hostProfileCode` is not `adminSet`, only `optional`, `required`, `notUsed`, and `notApplicable` are available for `scheduleStartCodes`.

* If the type of the `All` service has a value other than `notApplicable`, and another service, e.g. `EventCenter`, is missing from the `scheduleStartCodes`, then the type of this missing `EventCenter` service shares the same type as the `All` service. If the type of `All` service has a value other than `notApplicable`, and another service, e.g. `EventCenter`, has a type, then the type specified should be the same as the `All` service.

* If the `All` service is missing from the `scheduleStartCodes`, any of the other four services, e.g. `EventCenter`, have a default type of `notUsed` if it is also missing from the `scheduleStartCodes`.

* Admins can switch any Control Hub managed site from using classic tracking codes to mapped tracking codes in Control Hub, this is a one-time irreversible operation. Once the tracking codes are mapped to custom or user profile attributes, they cannot create tracking codes when the mapping process is in progress or the mapping process is completed.

## Cuerpo de la petición (application/json)
- `name` (string) **(requerido)**: Name for tracking code. The name cannot be empty and the maximum size is 120 characters.
- `siteUrl` (string) **(requerido)**: Site URL for the tracking code.
- `options` (array) **(requerido)**: Tracking code option list. The maximum size of `options` is 500.
  - `value` (string) **(requerido)**: The value of a tracking code option. `value` cannot be empty and the maximum size is 120 characters.
  - `defaultValue` (boolean) **(requerido)**: Whether or not the option is the default option of a tracking code.
- `inputMode` (string) **(requerido)**: Select an option for how users can provide a code value. Please note that if users set `inputMode` as `hostProfileSelect`, `scheduleStartCode` should be `null`, which means `hostProfileSelect` only applies to "Host Profile".  * `text` - Text input.  * `select` - Drop down list which requires `options`.  * `editableSelect` - Both text input and select from list.  * `hostProfileSelect` - An input method is only available for the host profile and sign-up pages. Valores: text, select, editableSelect, hostProfileSelect.
- `hostProfileCode` (string) **(requerido)**: Type for the host profile.  * `optional` - Available to be chosen but not compulsory.  * `required` - Officially compulsory.  * `adminSet` - The value is set by admin.  * `notUsed` - The value cannot be used. Valores: optional, required, adminSet, notUsed.
- `scheduleStartCodes` (array) **(requerido)**: Specify how tracking codes are used for each service on the meeting scheduler or meeting start pages. The maximum size of `scheduleStartCodes` is 5.
  - `service` (string) **(requerido)**: Service for schedule or sign up pages  * `All` - Tracking codes apply to all services.  * `MeetingCenter` - Users can set tracking codes when scheduling a meeting.  * `EventCenter` - Users can set tracking codes when scheduling an event.  * `TrainingCenter` - Users can set tracking codes when scheduling a training session.  * `SupportCenter` - Users can set tracking codes when scheduling a support meeting. Valores: All, MeetingCenter, EventCenter, TrainingCenter, SupportCenter.
  - `type` (string) **(requerido)**: Type for meeting scheduler or meeting start pages.  * `optional` - Available to be chosen but not compulsory.  * `required` - Officially compulsory.  * `adminSet` - The value is set by admin. This value only applies when `hostProfileCode` is `adminSet`.  * `notUsed` - The value cannot be used.  * `notApplicable` - This value only applies to the service of `All`. When the type of `All` for a tracking code is `notApplicable`, there are different types for different services. For example, `required` for `MeetingCenter`, `optional` for `EventCenter` and `notUsed` for others. Valores: optional, required, adminSet, notUsed, notApplicable.

### Ejemplo de petición
```json
{
  "name": "Department",
  "siteUrl": "example.webex.com",
  "inputMode": "select",
  "options": [
    {
      "value": "Engineering",
      "defaultValue": false
    },
    {
      "value": "Design",
      "defaultValue": true
    },
    {
      "value": "Sales",
      "defaultValue": false
    }
  ],
  "hostProfileCode": "optional",
  "scheduleStartCodes": [
    {
      "service": "All",
      "type": "notApplicable"
    },
    {
      "service": "MeetingCenter",
      "type": "required"
    },
    {
      "service": "EventCenter",
      "type": "optional"
    },
    {
      "service": "TrainingCenter",
      "type": "notUsed"
    },
    {
      "service": "SupportCenter",
      "type": "notUsed"
    }
  ]
}
```

## Respuestas
- **200**: OK
  - `id` (string) **(requerido)**: Unique identifier for tracking code.
  - `name` (string) **(requerido)**: Name for tracking code.
  - `siteUrl` (string) **(requerido)**: Site URL for the tracking code.
  - `options` (array) **(requerido)**: Tracking code option list.
    - `value` (string) **(requerido)**: The value of a tracking code option. `value` cannot be empty and the maximum size is 120 characters.
    - `defaultValue` (boolean) **(requerido)**: Whether or not the option is the default option of a tracking code.
  - `inputMode` (string) **(requerido)**: An option for how an admin user can provide a code value.  * `text` - Text input.  * `select` - Drop down list which requires `options`.  * `editableSelect` - Both text input and select from list.  * `hostProfileSelect` - An input method is only available for the host profile and sign-up pages. Valores: text, select, editableSelect, hostProfileSelect.
  - `hostProfileCode` (string) **(requerido)**: Type for the host profile.  * `optional` - Available to be chosen but not compulsory.  * `required` - Officially compulsory.  * `adminSet` - The value is set by admin.  * `notUsed` - The value cannot be used. Valores: optional, required, adminSet, notUsed.
  - `scheduleStartCodes` (array) **(requerido)**: Specify how tracking codes are used for each service on the meeting scheduler or meeting start pages.
    - `service` (string) **(requerido)**: Service for schedule or sign up pages  * `All` - Tracking codes apply to all services.  * `MeetingCenter` - Users can set tracking codes when scheduling a meeting.  * `EventCenter` - Users can set tracking codes when scheduling an event.  * `TrainingCenter` - Users can set tracking codes when scheduling a training session.  * `SupportCenter` - Users can set tracking codes when scheduling a support meeting. Valores: All, MeetingCenter, EventCenter, TrainingCenter, SupportCenter.
    - `type` (string) **(requerido)**: Type for meeting scheduler or meeting start pages.  * `optional` - Available to be chosen but not compulsory.  * `required` - Officially compulsory.  * `adminSet` - The value is set by admin. This value only applies when `hostProfileCode` is `adminSet`.  * `notUsed` - The value cannot be used.  * `notApplicable` - This value only applies to the service of `All`. When the type of `All` for a tracking code is `notApplicable`, there are different types for different services. For example, `required` for `MeetingCenter`, `optional` for `EventCenter` and `notUsed` for others. Valores: optional, required, adminSet, notUsed, notApplicable.
- **400**: Bad Request
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
