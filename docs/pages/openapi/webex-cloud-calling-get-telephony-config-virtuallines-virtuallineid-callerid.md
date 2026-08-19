---
doc_id: webex-cloud-calling-get-telephony-config-virtuallines-virtuallineid-callerid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/virtualLines/{virtualLineId}/callerId
operation_id: Read Caller ID Settings for a Virtual Line
tags: Virtual Line Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.175524+00:00
---

# GET /telephony/config/virtualLines/{virtualLineId}/callerId

**API:** Webex Cloud Calling
**Área:** Virtual Line Call Settings
**operationId:** `Read Caller ID Settings for a Virtual Line`

## Resumen
Read Caller ID Settings for a Virtual Line

## Descripción
Retrieve a virtual line's Caller ID settings.

Caller ID settings control how a virtual line's information is displayed when making outgoing calls.

Retrieving the caller ID settings for a virtual line requires a full, user, read-only administrator, or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `virtualLineId` [path] (string) (**requerido**): Retrieve settings for a virtual line with the matching ID.
- `orgId` [query] (string): ID of the organization in which the virtual line resides. Only admin users of another organization (such as partners) may use this parameter, as the default is the same organization as the token used to access the API.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/virtualLines/<virtualLineId>/callerId' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `types` (array) (**requerido**): Allowed types for the `selected` field. This field is read-only and cannot be modified.
- `selected` (string) (**requerido**): Which type of outgoing Caller ID will be used. This setting is for the number portion.  * `DIRECT_LINE` - Outgoing caller ID will show the caller's direct line number.  * `LOCATION_NUMBER` - Outgoing caller ID will show the main number for the location.  * `CUSTOM` - Outgoing caller ID will show the value from the customNumber field. Valores: DIRECT_LINE, LOCATION_NUMBER, CUSTOM.
- `directNumber` (string): Direct number which will be shown if `DIRECT_LINE` is selected.
- `extensionNumber` (string): Extension number of the virtual line.
- `locationNumber` (string): Location number which will be shown if `LOCATION_NUMBER` is selected.
- `tollFreeLocationNumber` (boolean) (**requerido**): Flag to indicate if the location number is toll-free number.
- `customNumber` (string): Custom number which will be shown if CUSTOM is selected. This value must be a number from the virtual line's location or from another location with the same country, PSTN provider, and zone (only applicable for India locations) as the virtual line's location.
- `firstName` (string): The virtual line's Caller ID first name. The characters `%`,  `+`, ``, `"` and Unicode characters are not allowed. This field has been deprecated. Please use `directLineCallerIdName` and `dialByFirstName` instead.
- `lastName` (string): The virtual line's Caller ID last name. The characters `%`,  `+`, ``, `"` and Unicode characters are not allowed. This field has been deprecated. Please use `directLineCallerIdName` and `dialByLastName` instead.
- `blockInForwardCallsEnabled` (boolean) (**requerido**): Block this virtual line's identity when receiving a call.
- `externalCallerIdNamePolicy` (string): Designates which type of External Caller ID Name policy is used. Default is `DIRECT_LINE`.  * `DIRECT_LINE` - Outgoing caller ID will show the caller's direct line name.  * `LOCATION` - Outgoing caller ID will show the external caller ID name for the location.  * `OTHER` - Outgoing caller ID will show the value from the `customExternalCallerIdName` field. Valores: DIRECT_LINE, LOCATION, OTHER.
- `customExternalCallerIdName` (string): Custom external caller ID name which will be shown if external caller ID name policy is `OTHER`.
- `locationExternalCallerIdName` (string) (**requerido**): Location's external caller ID name which will be shown if external caller ID name policy is `LOCATION`.
- `additionalExternalCallerIdDirectLineEnabled` (boolean): Flag to indicate the virtual line's direct line number is available as an additional external caller ID for the virtual line.
- `additionalExternalCallerIdLocationNumberEnabled` (boolean): Flag to indicate the location main number is available as an additional external caller ID for the virtual line.
- `additionalExternalCallerIdCustomNumber` (string): The custom number available as an additional external caller ID for the virtual line. This value must be a number from the virtual line's location or from another location with the same country, PSTN provider, and zone (only applicable for India locations) as the virtual line's location.
- `directLineCallerIdName` (object): Settings for the direct line caller ID name to be shown for this workspace.
  - `selection` (string): * `DISPLAY_NAME` - When this option is selected, `displayName` is to be shown for this workspace.  * `CUSTOM_NAME` - When this option is selected, `customName` is to be shown for this workspace. Valores: CUSTOM_NAME, DISPLAY_NAME.
  - `customName` (string): The custom direct line caller ID name. Required if `selection` is set to `CUSTOM_NAME`.
- `dialByFirstName` (string): The first name to be used for dial-by-name functions.
- `dialByLastName` (string): The last name to be used for dial-by-name functions.

### Ejemplo — respuesta 200
```json
{
  "types": [
    "DIRECT_LINE",
    "LOCATION_NUMBER",
    "CUSTOM"
  ],
  "selected": "DIRECT_LINE",
  "directNumber": "3182202028",
  "extensionNumber": "4000",
  "locationNumber": "+13182202021",
  "tollFreeLocationNumber": false,
  "firstName": "Lya",
  "lastName": "Charrel",
  "blockInForwardCallsEnabled": false,
  "externalCallerIdNamePolicy": "OTHER",
  "customExternalCallerIdName": "Lya Custom",
  "locationExternalCallerIdName": "Location caller id",
  "additionalExternalCallerIdDirectLineEnabled": false,
  "additionalExternalCallerIdLocationNumberEnabled": false,
  "additionalExternalCallerIdCustomNumber": "2025552000",
  "directLineCallerIdName": {
    "selection": "CUSTOM_NAME",
    "customName": "Lya Charrel"
  },
  "dialByFirstName": "Lya",
  "dialByLastName": "Charrel"
}
```

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