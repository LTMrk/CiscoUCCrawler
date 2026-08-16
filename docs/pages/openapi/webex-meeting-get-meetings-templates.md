---
doc_id: webex-meeting-get-meetings-templates
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /meetings/templates
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.395208+00:00
---

# GET /meetings/templates

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `listTemplates`

## Resumen
List Meeting Templates

## Descripción
Retrieves the list of meeting templates that is available for the authenticated user.

There are separate lists of meeting templates for different `templateType`, `locale` and `siteUrl`.

* If `templateType` is specified, the operation returns an array of meeting template objects specified by the `templateType`; otherwise, returns an array of meeting template objects of all template types.

* If `locale` is specified, the operation returns an array of meeting template objects specified by the `locale`; otherwise, returns an array of meeting template objects of the default `en_US` locale. Refer to [Meeting Template Locales](/docs/meetings#meeting-template-locales) for all the locales supported by Webex.

* If the parameter `siteUrl` has a value, the operation lists meeting templates on the specified site; otherwise, lists meeting templates on the user's preferred site. All available Webex sites and preferred site of the user can be retrieved by `Get Site List` API.

## Parámetros
- `templateType` [query] (string): Meeting template type for the meeting template objects being requested. If not specified, return meeting templates of all types.
- `locale` [query] (string): Locale for the meeting template objects being requested. If not specified, return meeting templates of the default `en_US` locale. Refer to [Meeting Template Locales](/docs/meetings#meeting-template-locales) for all the locales supported by Webex.
- `isDefault` [query] (boolean): The value is `true` or `false`. If it's `true`, return the default meeting templates; if it's `false`, return the non-default meeting templates. If it's not specified, return both default and non-default meeting templates.
- `isStandard` [query] (boolean): The value is `true` or `false`. If it's `true`, return the standard meeting templates; if it's `false`, return the non-standard meeting templates. If it's not specified, return both standard and non-standard meeting templates.
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes. If set, the admin may specify the email of a user in a site they manage and the API will return meeting templates that are available for that user.
- `siteUrl` [query] (string): URL of the Webex site which the API lists meeting templates from. If not specified, the API lists meeting templates from user's preferred site. All available Webex sites and preferred site of the user can be retrieved by `Get Site List` API.

## Respuestas
- **200**: OK
  - `items` (array): Meeting templates array.
    - `id` (string) **(requerido)**: Unique identifier for meeting template.
    - `name` (string) **(requerido)**: Meeting template name.
    - `locale` (string) **(requerido)**: Meeting template locale.
    - `siteUrl` (string) **(requerido)**: Site URL for the meeting template.
    - `templateType` (string) **(requerido)**: Meeting template type.  * `meeting` - Webex meeting.  * `webinar` - Webex webinar. Valores: meeting, webinar.
    - `isDefault` (boolean) **(requerido)**: Whether or not the meeting template is a default template.
    - `isStandard` (boolean) **(requerido)**: Whether or not the meeting template is a standard template.
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
