---
doc_id: webex-cloud-calling-put-people-personid-features-callerid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /people/{personId}/features/callerId
operation_id: Configure Caller ID Settings for a Person
tags: User Call Settings (1/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.362304+00:00
---

# PUT /people/{personId}/features/callerId

**API:** Webex Cloud Calling
**Área:** User Call Settings (1/2)
**operationId:** `Configure Caller ID Settings for a Person`

## Resumen
Configure Caller ID Settings for a Person

## Descripción
Configure a person's Caller ID settings.

Caller ID settings control how a person's information is displayed when making outgoing calls.

This API requires a full or user administrator or location administrator auth token with the `spark-admin:people_write` scope.

## Parámetros
- `personId` [path] (string) (**requerido**): Unique identifier for the person.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Cuerpo de la petición (application/json)
- `selected` (string) (**requerido**): Specifies which source will be used for the outgoing Caller ID phone number. The allowed values for the current virtual line can be retrieved from the [Read Caller ID Settings for a Virtual Line](/calling/docs/api/v1/virtual-line-call-settings/read-caller-id-settings-for-a-virtual-line) `types` field.  * `DIRECT_LINE` - Outgoing caller ID will show the caller's direct line number.  * `LOCATION_NUMBER` - Outgoing caller ID will show the main number for the location.  * `CUSTOM` - Outgoing caller ID will show the value from the customNumber field. Valores: DIRECT_LINE, LOCATION_NUMBER, CUSTOM.
- `customNumber` (string): Custom number which will be shown if CUSTOM is selected. This value must be a number from the virtual line's location or from another location with the same country, PSTN provider, and zone (only applicable for India locations) as the virtual line's location.
- `firstName` (string): Virtual line's Caller ID first name. The characters `%`,  `+`, ``, `"` and Unicode characters are not allowed. This field has been deprecated. Please use `directLineCallerIdName` and `dialByFirstName` instead.
- `lastName` (string): Virtual line's Caller ID last name. The characters `%`,  `+`, ``, `"` and Unicode characters are not allowed. This field has been deprecated. Please use `directLineCallerIdName` and `dialByLastName` instead.
- `blockInForwardCallsEnabled` (boolean): Block this virtual line's identity when receiving a call.
- `externalCallerIdNamePolicy` (string): Designates which type of External Caller ID Name policy is used. Default is DIRECT_LINE.  * `DIRECT_LINE` - Outgoing caller ID will show the caller's direct line name.  * `LOCATION` - Outgoing caller ID will show the external caller ID name for the location.  * `OTHER` - Outgoing caller ID will show the value from the `customExternalCallerIdName` field. Valores: DIRECT_LINE, LOCATION, OTHER.
- `customExternalCallerIdName` (string): Custom external caller ID name which will be shown if external caller ID name policy is `OTHER`.
- `additionalExternalCallerIdDirectLineEnabled` (boolean): Set the virtual line's direct line number as additional external caller ID.
- `additionalExternalCallerIdLocationNumberEnabled` (boolean): Set the Location main number as additional external caller ID for the virtual line.
- `additionalExternalCallerIdCustomNumber` (string): To set a custom number as additional external caller ID for the virtual line. This value must be a number from the virtual line's location or from another location with the same country, PSTN provider, and zone (only applicable for India locations) as the virtual line's location.
- `directLineCallerIdName` (object): Settings for the direct line caller ID name to be shown for this virtual line.
  - `selection` (string): * `DISPLAY_NAME` - When this option is selected, `displayName` is to be shown for this virtual line.  * `FIRSTNAME_LASTNAME` - When this option is selected, `firstName` and `lastName` are to be shown for this virtual line.  * `LASTNAME_FIRSTNAME` - When this option is selected, `lastName` and `firstName` are to be shown for this virtual line.  * `CUSTOM_NAME` - When this option is selected, `customName` is to be shown for this virtual line. Valores: CUSTOM_NAME, FIRSTNAME_LASTNAME, LASTNAME_FIRSTNAME, DISPLAY_NAME.
  - `customName` (string): Sets or clears the custom direct line caller ID name.  To clear the `customName`, the attribute must be set to null or empty string. Required if `selection` is set to `CUSTOM_NAME`.
- `dialByFirstName` (string): Sets or clears the first name to be used for dial-by-name functions. To clear the `dialByFirstName`, the attribute must be set to null or empty string. Characters of `%`,  `+`, `\`, `"` and Unicode characters are not allowed.
- `dialByLastName` (string): Sets or clears the last name to be used for dial-by-name functions. To clear the `dialByLastName`, the attribute must be set to null or empty string. Characters of `%`,  `+`, `\`, `"` and Unicode characters are not allowed.

### Ejemplo — petición
```json
{
  "selected": "LOCATION_NUMBER",
  "directNumber": "3182202028",
  "extensionNumber": "4000",
  "locationNumber": "+13182202021",
  "firstName": "Lya",
  "lastName": "Charrel",
  "blockInForwardCallsEnabled": false,
  "externalCallerIdNamePolicy": "OTHER",
  "customExternalCallerIdName": "Lya Custom",
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

## Ejemplo de invocación
```bash
curl -X PUT '/people/<personId>/features/callerId' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"selected": "<selected>"}'
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