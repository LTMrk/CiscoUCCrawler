---
doc_id: webex-cloud-calling-get-telephony-config-virtuallines-virtuallineid-emergencycallbacknumber
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/virtualLines/{virtualLineId}/emergencyCallbackNumber
operation_id: getVirtualLineEmergencyCallbackSettings
tags: Emergency Services Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.012946+00:00
---

# GET /telephony/config/virtualLines/{virtualLineId}/emergencyCallbackNumber

**API:** Webex Cloud Calling
**Área:** Emergency Services Settings
**operationId:** `getVirtualLineEmergencyCallbackSettings`

## Resumen
Get the Virtual Line's Emergency Callback Settings

## Descripción
Retrieve the emergency callback number settings for a specific virtual line.

A virtual line is a capability in Webex Calling that allows administrators to configure multiple lines for Webex Calling users.

Retrieving these settings requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `virtualLineId` [path] (string) (**requerido**): The unique identifier for the virtual line.
- `orgId` [query] (string): List virtual lines for this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/virtualLines/<virtualLineId>/emergencyCallbackNumber' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `selected` (string) (**requerido**): * `DIRECT_LINE` - Returned calls from the Public Safety Answering Point go directly to the member. The Emergency Service Address configured by the PSTN to the member's phone is specific to the member’s location.  * `LOCATION_ECBN` - Each location can have an ECBN configured that is different from the location’s main number. Location Default ECBN is typically configured for users without dedicated telephone numbers or with only an extension.  * `LOCATION_MEMBER_NUMBER` - Configure one user with another user’s telephone number as an ECBN. This option is used in place of a location’s main number when the location has multiple floors or buildings. This allows the ECBN assigned to have a more accurate Emergency Service Address associated with it.  * `NONE` - When no other option is selected. Valores: DIRECT_LINE, LOCATION_ECBN, LOCATION_MEMBER_NUMBER, NONE.
- `directLineInfo` (object): Data relevant to the ECBN for this user/location/virtual line/hunt group.
  - `phoneNumber` (string): The callback phone number that is associated with the direct line.
  - `firstName` (string): The first name of the user.
  - `lastName` (string): The last name of the user.
  - `effectiveLevel` (string) (**requerido**): * `DIRECT_LINE` - Returned calls from the Public Safety Answering Point go directly to the member. The Emergency Service Address configured by the PSTN to the member's phone is specific to the member’s location.  * `LOCATION_ECBN` - Each location can have an ECBN configured that is different from the location’s main number. Location Default ECBN is typically configured for users without dedicated telephone numbers or with only an extension.  * `LOCATION_NUMBER` - A location’s main number that is suitable for when the location has a single building with a single floor.  * `NONE` - There is no effective level type selected. Valores: DIRECT_LINE, LOCATION_ECBN, LOCATION_NUMBER, NONE.
  - `effectiveValue` (string): The field contains the valid ECBN number at the location level, or the user's main number if valid, defaulting to the location's main number if both are unavailable.
  - `quality` (string) (**requerido**): * `RECOMMENDED` - An activated number, associated with a User or Workspace.  * `NOT_RECOMMENDED` - An activated number, associated with anything else, like Auto Attendant or Hunt Group.  * `INVALID` - An inactive or non-existent number. Valores: RECOMMENDED, NOT_RECOMMENDED, INVALID.
- `locationECBNInfo` (object): Data relevant to the user/place/virtual line/hunt group selected for ECBN for this location.
  - `phoneNumber` (string): The callback phone number that is associated with the location's ECBN configuration.
  - `firstName` (string): The first name for the location. This field is populated with the group name when the `effectiveLevel` is `LOCATION_ECBN` or `LOCATION_NUMBER`.
  - `lastName` (string): The location member's last name when the `effectiveLevel` is `LOCATION_ECBN`, the location is using a location member number, and the selected member is a user. This field will not be present when the `effectiveLevel` is `LOCATION_ECBN`, the location is using the location member number, and the selected member is a place.
  - `effectiveLevel` (string) (**requerido**): * `DIRECT_LINE` - Returned calls from the Public Safety Answering Point go directly to the member. The Emergency Service Address configured by the PSTN to the member's phone is specific to the member’s location.  * `LOCATION_ECBN` - Each location can have an ECBN configured that is different from the location’s main number. Location Default ECBN is typically configured for users without dedicated telephone numbers or with only an extension.  * `LOCATION_NUMBER` - A location’s main number that is suitable for when the location has a single building with a single floor.  * `NONE` - There is no effective level type selected. Valores: DIRECT_LINE, LOCATION_ECBN, LOCATION_NUMBER, NONE.
  - `effectiveValue` (string): Contains the location-level emergency callback number if valid. If not, contains the user's main number if valid.
  - `quality` (string) (**requerido**): * `RECOMMENDED` - An activated number, associated with a User or Workspace.  * `NOT_RECOMMENDED` - An activated number, associated with anything else, like Auto Attendant or Hunt Group.  * `INVALID` - An inactive or non-existent number. Valores: RECOMMENDED, NOT_RECOMMENDED, INVALID.
- `locationMemberInfo` (object):
  - `phoneNumber` (string): A unique identifier for the location member's PSTN phone number.
  - `firstName` (string): The first name of the location member.
  - `lastName` (string): The last name of the location member. This field will not be present when `effectiveLevel` is `DIRECT_LINE` or `LOCATION_MEMBER_NUMBER`, and the selected member is a place.
  - `memberId` (string): Member ID of user/place/virtual line/hunt group within the location.
  - `effectiveLevel` (string) (**requerido**): * `DIRECT_LINE` - Returned calls from the Public Safety Answering Point go directly to the member. The Emergency Service Address configured by the PSTN to the member's phone is specific to the member’s location.  * `LOCATION_ECBN` - Each location can have an ECBN configured that is different from the location’s main number. Location Default ECBN is typically configured for users without dedicated telephone numbers or with only an extension.  * `LOCATION_NUMBER` - A location’s main number that is suitable for when the location has a single building with a single floor.  * `LOCATION_MEMBER_NUMBER` - Configure one user with another user’s telephone number as an ECBN. This option is used in place of a location’s main number when the location has multiple floors or buildings. This allows the ECBN assigned to have a more accurate Emergency Service Address associated with it.  * `NONE` - When no other option is selected. Valores: DIRECT_LINE, LOCATION_ECBN, LOCATION_NUMBER, LOCATION_MEMBER_NUMBER, NONE.
  - `effectiveValue` (string): Contains the location-level emergency callback number if valid. If not, contains the user's main number if valid.
  - `quality` (string) (**requerido**): * `RECOMMENDED` - An activated number, associated with a User or Workspace.  * `NOT_RECOMMENDED` - An activated number, associated with anything else, like Auto Attendant or Hunt Group.  * `INVALID` - An inactive or non-existent number. Valores: RECOMMENDED, NOT_RECOMMENDED, INVALID.
  - `memberType` (string): * `PEOPLE` - Indicates the associated member is a person.  * `PLACE` - Indicates the associated member is a workspace. Valores: PEOPLE, PLACE.
- `defaultInfo` (object): Contains the Emergency Callback Number effective value when none of the above parameters are assigned or some other value is set.
  - `effectiveValue` (string): The field contains ECBN number.
  - `quality` (string) (**requerido**): * `RECOMMENDED` - An activated number, associated with a User or Workspace.  * `NOT_RECOMMENDED` - An activated number, associated with anything else, like Auto Attendant or Hunt Group.  * `INVALID` - An inactive or non-existent number. Valores: RECOMMENDED, NOT_RECOMMENDED, INVALID.

### Ejemplo — respuesta 200
```json
{
  "selected": "DIRECT_LINE",
  "directLineInfo": {
    "phoneNumber": "9726856700",
    "firstName": "John",
    "lastName": "Smith",
    "effectiveLevel": "DIRECT_LINE",
    "effectiveValue": "9726856770",
    "quality": "RECOMMENDED"
  },
  "locationECBNInfo": {
    "phoneNumber": "9726856701",
    "firstName": "Jane",
    "lastName": "Smith",
    "effectiveLevel": "LOCATION_ECBN",
    "effectiveValue": "9726856772",
    "quality": "RECOMMENDED"
  },
  "locationMemberInfo": {
    "phoneNumber": "9726856703",
    "firstName": "Group Name",
    "lastName": ".",
    "memberId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS82MmQ3YTY3MS00YmVlLTQ2MDItOGVkOC1jOTFmNjU5NjcxZGI",
    "effectiveLevel": "LOCATION_MEMBER_NUMBER",
    "effectiveValue": "9726856774",
    "quality": "RECOMMENDED",
    "memberType": "PLACE"
  }
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