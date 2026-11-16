---
doc_id: webex-cloud-calling-get-telephony-config-workspaces-workspaceid-emergencycallbacknumber
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/workspaces/{workspaceId}/emergencyCallbackNumber
operation_id: getAWorkspaceEmergencyCallbackNumber
tags: Emergency Services Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T14:22:47.289465+00:00
---

# GET /telephony/config/workspaces/{workspaceId}/emergencyCallbackNumber

**API:** Webex Cloud Calling
**Área:** Emergency Services Settings
**operationId:** `getAWorkspaceEmergencyCallbackNumber`

## Resumen
Get a Workspace Emergency Callback Number

## Descripción
Retrieve the emergency callback number setting associated with a specific workspace.

Emergency Callback Configurations can be enabled at the organization level, Users without individual telephone numbers, such as extension-only users, must be set up with accurate Emergency Callback Numbers (ECBN) and Emergency Service Addresses to enable them to make emergency calls. These users can either utilize the default ECBN for their location or be assigned another specific telephone number from that location for emergency purposes.

To retrieve an emergency callback number, it requires a full, location, user, or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Retrieve Emergency Callback Number attributes for this workspace.
- `orgId` [query] (string): Retrieve Emergency Callback Number attributes for this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/workspaces/<workspaceId>/emergencyCallbackNumber' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `selected` (object): Selected number type to configure emergency call back.
- `directLineInfo` (object): Data relevant to the ECBN for this user/location/virtual line/hunt group.
  - `phoneNumber` (string): The callback phone number that is associated with the direct line.
  - `firstName` (string): The first name of the user.
  - `lastName` (string): The last name of the user.
  - `effectiveLevel` (object): The source from which the emergency calling line ID (CLID) is selected for an actual emergency call, applying fallback rules as necessary.
  - `effectiveValue` (string): The field contains the valid ECBN number at the location level, or the user's main number if valid, defaulting to the location's main number if both are unavailable.
  - `quality` (object): Used to represent whether a number is a recommended ECBN.
- `locationECBNInfo` (object): Data relevant to the user/place/virtual line/hunt group selected for ECBN for this location.
  - `phoneNumber` (string): The callback phone number that is associated with the location's ECBN configuration.
  - `lastName` (string): The last name of the user or location member.
  - `effectiveLevel` (object): The source from which the emergency calling line ID (CLID) is selected for an actual emergency call, applying fallback rules as necessary.
  - `effectiveValue` (string): The field contains the valid ECBN number at the location level, or the user's main number if valid, defaulting to the location's main number if both are unavailable.
  - `quality` (object): Used to represent whether a number is a recommended ECBN.
  - `firstName` (string): The first name of the user, location member, or group name.
- `locationMemberInfo` (object): Data relevant to the user/place/virtual line/hunt group selected for ECBN.
  - `phoneNumber` (string): The callback phone number that is associated with member configured for the location ECBN.
  - `firstName` (string): The first name of the user.
  - `lastName` (string): The last name of the user or location member.
  - `memberId` (string): Member ID of user/place/virtual line/hunt group within the location.
  - `effectiveLevel` (object): The source from which the emergency calling line ID (CLID) is selected for an actual emergency call, applying fallback rules as necessary.
  - `effectiveValue` (string): The field contains the valid ECBN number at the location level, or the user's main number if valid, defaulting to the location's main number if both are unavailable.
  - `quality` (object): Used to represent whether a number is a recommended ECBN.
  - `memberType` (object): Type of the member.
- `defaultInfo` (object): Gives Emergency Callback Number effective value when none of the above is assigned or some other value is set behind the scene.
  - `effectiveValue` (string): The field contains the ECBN number.
  - `quality` (object): Used to represent whether a number is a recommended ECBN.
- `elinEnabled` (boolean): Indicates whether this workspace is allowed to use an Emergency Location Identification Number (ELIN) for emergency calls made from one of its devices.

### Ejemplo — respuesta 200
```json
{
  "selected": "DIRECT_LINE",
  "directLineInfo": {
    "phoneNumber": "+18164196065",
    "firstName": "backUpworkspace",
    "lastName": ".",
    "effectiveLevel": "DIRECT_LINE",
    "effectiveValue": "+18164196065",
    "quality": "RECOMMENDED"
  },
  "locationECBNInfo": {
    "phoneNumber": "+18164196065",
    "lastName": ".",
    "effectiveLevel": "DIRECT_LINE",
    "effectiveValue": "+18164196065",
    "quality": "RECOMMENDED",
    "firstName": "backUpworkspace"
  },
  "locationMemberInfo": {
    "phoneNumber": "+18164196065",
    "firstName": "backUpworkspace",
    "lastName": ".",
    "memberId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMV9pbnQxMy9QTEFDRS8wY2VlYjFmYy04ZmEyLTQ5OGEtYWM3Ni02N2MyZGQ3MGQ2ZGY=",
    "effectiveLevel": "LOCATION_MEMBER_NUMBER",
    "effectiveValue": "+18164196065",
    "quality": "RECOMMENDED",
    "memberType": "PLACE"
  },
  "elinEnabled": true
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