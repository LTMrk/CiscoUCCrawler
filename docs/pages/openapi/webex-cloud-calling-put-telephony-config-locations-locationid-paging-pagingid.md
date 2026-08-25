---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-paging-pagingid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/paging/{pagingId}
operation_id: Update a Paging Group
tags: Features:  Paging Group
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.500618+00:00
---

# PUT /telephony/config/locations/{locationId}/paging/{pagingId}

**API:** Webex Cloud Calling
**Área:** Features:  Paging Group
**operationId:** `Update a Paging Group`

## Resumen
Update a Paging Group

## Descripción
Update the designated Paging Group.

Group Paging allows a person to place a one-way call or group page to up to 75 people, workspaces and virtual lines by
dialing a number or extension assigned to a specific paging group. The Group Paging service makes a simultaneous call to all the assigned targets.

Updating a paging group requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Update settings for a paging group in this location.
- `pagingId` [path] (string) (**requerido**): Update settings for the paging group with this identifier.
- `orgId` [query] (string): Update paging group settings from this organization.

## Cuerpo de la petición (application/json)
- `enabled` (boolean): Whether or not the paging group is enabled.
- `name` (string): Unique name for the paging group. Minimum length is 1. Maximum length is 30.
- `phoneNumber` (string): Paging group phone number. Minimum length is 1. Maximum length is 23.  Either `phoneNumber` or `extension` is mandatory.
- `extension` (string): Paging group extension. Minimum length is 2. Maximum length is 10.  Either `phoneNumber` or `extension` is mandatory.
- `languageCode` (string): Language code.
- `firstName` (string): First name to be shown when calls are forwarded out of this paging group. Defaults to ".". This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `lastName` (string): Last name to be shown when calls are forwarded out of this paging group. Defaults to the phone number if set, otherwise defaults to call group name. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `originatorCallerIdEnabled` (boolean): Determines what is shown on target users caller ID when a group page is performed. If true shows page originator ID.
- `originators` (array): An array of people and/or workspaces, who may originate pages to this paging group.
- `targets` (array): People, including workspaces, that are added to paging group as paging call targets.
- `directLineCallerIdName` (object): Settings for the direct line caller ID name to be shown for this workspace.
  - `selection` (string): * `DISPLAY_NAME` - When this option is selected, `displayName` is to be shown for this workspace.  * `CUSTOM_NAME` - When this option is selected, `customName` is to be shown for this workspace. Valores: CUSTOM_NAME, DISPLAY_NAME.
  - `customName` (string): Sets or clears the custom direct line caller ID name.  To clear the `customName`, the attribute must be set to null or empty string. Required if `selection` is set to `CUSTOM_NAME`.
- `dialByName` (string): Sets or clears the name to be used for dial by name functions. To clear the `dialByName`, the attribute must be set to null or empty string. Characters of `%`,  `+`, `\`, `"` and Unicode characters are not allowed.

### Ejemplo — petición
```json
{
  "name": "PagingGroup-1",
  "phoneNumber": "+15558675309",
  "extension": "7781",
  "languageCode": "en_us",
  "firstName": "John",
  "lastName": "Doe",
  "originatorCallerIdEnabled": false,
  "originators": [
    "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80YTc2ZmVmNC1mZjlmLTExZWItYWYwZC00M2YwZjY1NTdjYWI",
    "Y2lzY29zcGFyazovL3VzL1BMQUNFLzU1YjUyZThhLWZmOWYtMTFlYi05ZjRhLTAzZDY1NzdhYzg1Yg",
    "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfTElORS83MGY2MzYzMC1mZjlmLTExZWItODU5YS0xZjhiYjRjNzc3OGg="
  ],
  "targets": [
    "Y2lzY29zcGFyazovL3VzL1BMQUNFLzg0YjQ1OTIyLWZmOWYtMTFlYi1hNGI4LTMzNjI3YmVkNjdiNQ",
    "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfTElORS83MGY2MzYzMC1mZjlmLTExZWItODU5YS0xZjhiYjRjNzc3OGg="
  ],
  "directLineCallerIdName": {
    "selection": "CUSTOM_NAME",
    "customName": "Hakim Smith"
  },
  "dialByName": "Hakim Smith"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>/paging/<pagingId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
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

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs