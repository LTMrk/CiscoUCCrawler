---
doc_id: webex-cloud-calling-put-telephony-config-people-personid-features-hotdesking-members
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/people/{personId}/features/hotDesking/members
operation_id: updateHotDeskingMembers
tags: Features: Hot Desking Members, User Call Settings (3/3)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.388541+00:00
---

# PUT /telephony/config/people/{personId}/features/hotDesking/members

**API:** Webex Cloud Calling
**Área:** Features: Hot Desking Members, User Call Settings (3/3)
**operationId:** `updateHotDeskingMembers`

## Resumen
Update Hot Desking Members

## Descripción
Modify the primary and shared-line members assigned to a person's hot desking guest profile.

The request replaces the hot desking profile member list with the members supplied in the request body.

This API requires a full, user, device, or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `personId` [path] (string) (**requerido**): Unique identifier for the person.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization, such as partners, may use this parameter. If not specified, the organization from the OAuth token is used.

## Cuerpo de la petición (application/json)
- `members` (array) (**requerido**): Members to assign to the person's hot desking guest profile.
  - `id` (string) (**requerido**): Unique identifier for the member.
  - `port` (integer) (**requerido**): Port to assign to the member.
  - `primaryOwner` (boolean) (**requerido**): Indicates whether this member is the hot desking guest profile owner.
  - `lineType` (string) (**requerido**): Line type for the hot desking guest profile member.  * `HOTDESKING_GUEST` - Primary hot desking guest profile line.  * `SHARED_CALL_APPEARANCE` - Shared line assigned to the hot desking guest profile.  * `PRIMARY` - Primary line.  * `MOBILITY` - Mobility line. Valores: HOTDESKING_GUEST, SHARED_CALL_APPEARANCE, PRIMARY, MOBILITY.
  - `lineWeight` (integer) (**requerido**): Number of lines to configure for the member on the hot desking guest profile endpoint.
  - `t38FaxCompressionEnabled` (boolean): T.38 fax compression setting for the member line.
  - `hotlineEnabled` (boolean): Whether this line automatically calls a predefined number when taken off-hook.
  - `hotlineDestination` (string): Preconfigured number for the hotline. Required when `hotlineEnabled` is `true`.
  - `allowCallDeclineEnabled` (boolean): When enabled, a call decline request is extended to all endpoints on the line. When disabled, the call is declined only at the current endpoint.
  - `memberType` (string): Type of member in the update request. Include this field when the member ID needs an explicit resource type for decoding.  * `USER` - The member is a person.  * `PLACE` - The member is a workspace.  * `VIRTUAL_PROFILE` - The member is a virtual line. Valores: USER, PLACE, VIRTUAL_PROFILE.

### Ejemplo — petición
```json
{
  "members": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8wZTQ5NjAzNC1lNTQ1LTRmMmEtODI4ZC03MjhjYjJlNjNlMWQ",
      "port": 1,
      "primaryOwner": true,
      "lineType": "HOTDESKING_GUEST",
      "lineWeight": 1,
      "hotlineEnabled": false,
      "allowCallDeclineEnabled": true,
      "memberType": "USER"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfTElORS83MGY2MzYzMC1mZjlmLTExZWItODU5YS0xZjhiYjRjNzc3OGg",
      "port": 2,
      "primaryOwner": false,
      "lineType": "SHARED_CALL_APPEARANCE",
      "lineWeight": 1,
      "hotlineEnabled": false,
      "allowCallDeclineEnabled": true,
      "memberType": "VIRTUAL_PROFILE"
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/people/<personId>/features/hotDesking/members' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"members": []}'
```

## Respuestas correctas
**204**: No Content

## Respuestas de error
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

**Documentación adicional:** https://developer.webex.com/docs/api/v1/webex-calling

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs