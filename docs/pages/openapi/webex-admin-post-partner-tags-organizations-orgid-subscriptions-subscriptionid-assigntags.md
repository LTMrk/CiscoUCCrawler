---
doc_id: webex-admin-post-partner-tags-organizations-orgid-subscriptions-subscriptionid-assigntags
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: POST
path: /partner/tags/organizations/{orgId}/subscriptions/{subscriptionId}/assignTags
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.163927+00:00
---

# POST /partner/tags/organizations/{orgId}/subscriptions/{subscriptionId}/assignTags

**API:** Webex Admin
**Área:** Partner Tags
**operationId:** `Create or Replace existing subscription tags with the provided ones`

## Resumen
Create or Replace existing subscription tags with the provided ones

## Descripción
Assign or replace tags specific to each subscription for an organization. Each organization may have one or more subscriptions.
This API can be used by partner full admins and partner admins. 
Currently there is a limit of 5 tags per subscription when creating tags. To remove all the tags, pass an empty array.
Specify the customer organization ID in the `orgId` parameter in the URI and subscription ID in `subscriptionId` parameter

## Parámetros
- `orgId` [path] (string) **(requerido)**: The unique identifier for the customer organization.
- `subscriptionId` [path] (string) **(requerido)**: The unique identifier for the subscription.

## Cuerpo de la petición (application/json)
- `tags` (array): An array of tags.
  - `name` (string) **(requerido)**: Name of the tag.
  - `description` (string): Description of the tag

## Respuestas
- **200**: OK
  - (array de:)
    - `name` (string) **(requerido)**: Name of the tag.
    - `description` (string): Description of the tag
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
