---
doc_id: webex-cloud-calling-get-workspaces-workspaceid-features-callerid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /workspaces/{workspaceId}/features/callerId
operation_id: Read Caller ID Settings for a Workspace
tags: Workspace Call Settings (1/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.587152+00:00
---

# GET /workspaces/{workspaceId}/features/callerId

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings (1/2)
**operationId:** `Read Caller ID Settings for a Workspace`

## Resumen
Read Caller ID Settings for a Workspace

## Descripción
Retrieve a workspace's Caller ID settings.

Caller ID settings control how a workspace's information is displayed when making outgoing calls.

This API requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:workspaces_read` or a user auth token with `spark:workspaces_read` scope can be used to read workspace settings.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Unique identifier for the workspace.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.

## Ejemplo de invocación
```bash
curl -X GET '/workspaces/<workspaceId>/features/callerId' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `types` (array) (**requerido**): Allowed types for the `selected` field. This field is read-only and cannot be modified.
- `selected` (string) (**requerido**): Which type of outgoing Caller ID will be used. This setting is for the number portion.  * `DIRECT_LINE` - Outgoing caller ID shows the caller's direct line number.  * `LOCATION_NUMBER` - Outgoing caller ID shows the main number for the location.  * `CUSTOM` - Outgoing caller ID shows the value from the customNumber field. Valores: DIRECT_LINE, LOCATION_NUMBER, CUSTOM.
- `directNumber` (string) (**requerido**): Direct number which is shown if `DIRECT_LINE` is selected.
- `locationNumber` (string) (**requerido**): Location number which is shown if `LOCATION_NUMBER` is selected
- `tollFreeLocationNumber` (boolean) (**requerido**): Flag to indicate if the location number is toll-free number.
- `customNumber` (string): Custom number which is shown if CUSTOM is selected. This value must be a number from the workspace's location or from another location with the same country, PSTN provider, and zone (only applicable for India locations) as the workspace's location.
- `displayName` (string): Workspace's caller ID display name. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `displayDetail` (string): Workspace's caller ID display details. Default is `.`. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `blockInForwardCallsEnabled` (boolean) (**requerido**): Block this workspace's identity when receiving a call.
- `externalCallerIdNamePolicy` (string) (**requerido**): Designates which type of External Caller ID Name policy is used. Default is `DIRECT_LINE`.  * `DIRECT_LINE` - Outgoing caller ID shows the caller's direct line name.  * `LOCATION` - Outgoing caller ID shows the external caller ID name for the location.  * `OTHER` - Outgoing caller ID shows the value from the `customExternalCallerIdName` field. Valores: DIRECT_LINE, LOCATION, OTHER.
- `customExternalCallerIdName` (string): Custom external caller ID name which is shown if external caller ID name policy is `OTHER`.
- `locationExternalCallerIdName` (string) (**requerido**): Location's external caller ID name which is shown if external caller ID name policy is `LOCATION`.
- `directLineCallerIdName` (object): Settings for the direct line caller ID name to be shown for this workspace.
  - `selection` (string): * `DISPLAY_NAME` - When this option is selected, `displayName` is to be shown for this workspace.  * `CUSTOM_NAME` - When this option is selected, `customName` is to be shown for this workspace. Valores: CUSTOM_NAME, DISPLAY_NAME.
  - `customName` (string): The custom direct line caller ID name. Required if `selection` is set to `CUSTOM_NAME`.
- `dialByName` (string): The name to be used for dial by name functions.

### Ejemplo — respuesta 200
```json
{
  "types": [
    "DIRECT_LINE",
    "LOCATION_NUMBER",
    "CUSTOM"
  ],
  "selected": "DIRECT_LINE",
  "directNumber": "+12815550003",
  "locationNumber": "+12815550002",
  "tollFreeLocationNumber": false,
  "customNumber": "+12815550003",
  "displayName": "Clockmaker's shop 7.1",
  "displayDetail": ".",
  "blockInForwardCallsEnabled": false,
  "externalCallerIdNamePolicy": "DIRECT_LINE",
  "customExternalCallerIdName": "Custom external caller name",
  "locationExternalCallerIdName": "Anna",
  "directLineCallerIdName": {
    "selection": "CUSTOM_NAME",
    "customName": "Hakim Smith"
  },
  "dialByName": "Hakim Smith"
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