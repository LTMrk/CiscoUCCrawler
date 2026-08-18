---
doc_id: webex-meeting-get-admin-meeting-config-trackingcodes-trackingcodeid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /admin/meeting/config/trackingCodes/{trackingCodeId}
operation_id: Get a Tracking Code
tags: Tracking Codes
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.492083+00:00
---

# GET /admin/meeting/config/trackingCodes/{trackingCodeId}

**API:** Webex Meetings
**Área:** Tracking Codes
**operationId:** `Get a Tracking Code`

## Resumen
Get a Tracking Code

## Descripción
Retrieves details for a tracking code by an admin user.

* If `siteUrl` is specified, the tracking code is retrieved from the specified site; otherwise, the tracking code is retrieved from the user's preferred site. All available Webex sites and the preferred sites of a user can be retrieved by the [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

* Admins can switch any Control Hub managed site from using classic tracking codes to mapped tracking codes in Control Hub, this is a one-time irreversible operation. Once the tracking codes are mapped to custom or user profile attributes, the response returns details for a mapped tracking code.

## Parámetros
- `trackingCodeId` [path] (string) (**requerido**): Unique identifier for the tracking code whose details are being requested.
- `siteUrl` [query] (string): URL of the Webex site which the API retrieves the tracking code from. If not specified, the API retrieves the tracking code from the user's preferred site. All available Webex sites and the preferred sites of a user can be retrieved by the [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

## Ejemplo de invocación
```bash
curl -X GET '/admin/meeting/config/trackingCodes/<trackingCodeId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Unique identifier for tracking code.
- `name` (string) (**requerido**): Name for tracking code.
- `siteUrl` (string) (**requerido**): Site URL for the tracking code.
- `options` (array) (**requerido**): Tracking code option list.
  - `value` (string) (**requerido**): The value of a tracking code option. `value` cannot be empty and the maximum size is 120 characters.
  - `defaultValue` (boolean) (**requerido**): Whether or not the option is the default option of a tracking code.
- `inputMode` (string) (**requerido**): An option for how an admin user can provide a code value.  * `text` - Text input.  * `select` - Drop down list which requires `options`.  * `editableSelect` - Both text input and select from list.  * `hostProfileSelect` - An input method is only available for the host profile and sign-up pages. Valores: text, select, editableSelect, hostProfileSelect.
- `hostProfileCode` (string) (**requerido**): Type for the host profile.  * `optional` - Available to be chosen but not compulsory.  * `required` - Officially compulsory.  * `adminSet` - The value is set by admin.  * `notUsed` - The value cannot be used. Valores: optional, required, adminSet, notUsed.
- `scheduleStartCodes` (array) (**requerido**): Specify how tracking codes are used for each service on the meeting scheduler or meeting start pages.
  - `service` (string) (**requerido**): Service for schedule or sign up pages  * `All` - Tracking codes apply to all services.  * `MeetingCenter` - Users can set tracking codes when scheduling a meeting.  * `EventCenter` - Users can set tracking codes when scheduling an event.  * `TrainingCenter` - Users can set tracking codes when scheduling a training session.  * `SupportCenter` - Users can set tracking codes when scheduling a support meeting. Valores: All, MeetingCenter, EventCenter, TrainingCenter, SupportCenter.
  - `type` (string) (**requerido**): Type for meeting scheduler or meeting start pages.  * `optional` - Available to be chosen but not compulsory.  * `required` - Officially compulsory.  * `adminSet` - The value is set by admin. This value only applies when `hostProfileCode` is `adminSet`.  * `notUsed` - The value cannot be used.  * `notApplicable` - This value only applies to the service of `All`. When the type of `All` for a tracking code is `notApplicable`, there are different types for different services. For example, `required` for `MeetingCenter`, `optional` for `EventCenter` and `notUsed` for others. Valores: optional, required, adminSet, notUsed, notApplicable.

### Ejemplo — respuesta 200
```json
{
  "id": "1",
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

## Respuestas de error
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

## Contexto de la API
The Webex Meetings APIs enable developers to schedule, manage, and retrieve information about Webex meetings, webinars, and events. They provide endpoints for meeting creation, participant management, recordings, transcripts, in-meeting features such as chat and closed captions, and post-meeting analytics. Common use cases include integrating meeting scheduling into calendar apps, automating follow-ups with recordings and transcripts, embedding meeting controls in custom portals, and extracting insights for compliance or productivity analysis. The APIs support both real-time and asynchronous w...

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs