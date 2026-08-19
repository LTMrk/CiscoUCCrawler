---
doc_id: webex-cloud-calling-post-telephony-config-actions-testcallrouting-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/actions/testCallRouting/invoke
operation_id: Test Call Routing
tags: Call Routing
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.945365+00:00
---

# POST /telephony/config/actions/testCallRouting/invoke

**API:** Webex Cloud Calling
**Área:** Call Routing
**operationId:** `Test Call Routing`

## Resumen
Test Call Routing

## Descripción
Validates that an incoming call can be routed.

Dial plans route calls to on-premises destinations by use of trunks or route groups.
They are configured globally for an enterprise and apply to all users, regardless of location.
A dial plan also specifies the routing choice (trunk or route group) for calls that match any of its dial patterns.
Specific dial patterns can be defined as part of your dial plan.

Test call routing requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Organization in which we are validating a call routing.

## Cuerpo de la petición (application/json)
- `originatorId` (string) (**requerido**): This element is used to identify the originating party. It can be a person ID or a trunk ID.
- `originatorType` (string) (**requerido**): * `PEOPLE` - The originator type object is a person.  * `TRUNK` - Connection between Webex Calling and the premises. Valores: PEOPLE, TRUNK.
- `originatorNumber` (string): Only used when `originatorType` is `TRUNK`. The `originatorNumber` can be a phone number or URI.
- `destination` (string) (**requerido**): This element specifies the called party. It can be any dialable string, for example, an ESN number, E.164 number, hosted user DN, extension, extension with location code, URL, or FAC code.
- `includeAppliedServices` (boolean): This element is used to retrieve if any translation pattern, call intercept, permission by type or permission by digit pattern is present for the called party.

### Ejemplo — petición
```json
{
  "originatorId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xMWEzZjk5MC1hNjg5LTQ3N2QtYmU2Yi03MTIwMDI1ZDhhYmI",
  "originatorType": "PEOPLE",
  "destination": "0007",
  "includeAppliedServices": true
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/actions/testCallRouting/invoke' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"originatorId": "<originatorId>", "originatorType": "<originatorType>", "destination": "<destination>"}'
```

## Respuestas correctas
**200**: OK
- `callSourceInfo` (object):
  - `callSourceType` (string) (**requerido**): * `ROUTE_LIST` - Route list is a type of call source.  * `DIAL_PATTERN` - Dial pattern is a type of call source.  * `UNKOWN_EXTENSION` - The call source extension is unknown.  * `UNKOWN_NUMBER` - The call source phone number is unknown. Valores: ROUTE_LIST, DIAL_PATTERN, UNKOWN_EXTENSION, UNKOWN_NUMBER.
  - `routeListName` (string): Name of a route list.  When `originatorType` is `trunk`, `originatorId` is a valid trunk and the trunk belongs to a route group which is assigned to a route list with the name `routeListA` and also `originatorNumber` is a number assigned to `routeListA`, then `routeListA` is returned here. This element is returned when `callSourceType` is `ROUTE_LIST`.
  - `routeListId` (string): Unique identifier for the route list.
  - `dialPlanName` (string): Name of a dial plan. When `originatorType` is `trunk`, `originatorId` is a valid trunk with the name `trunkA`, `trunkA` belongs to a route group which is assigned to a route list with the name `routeListA`, `trunkA` is also assigned to `dialPlanA` as routing choice, `dialPlanA` has `dialPattern` xxxx assigned. If the `originatorNumber` matches the `dialPattern` `xxxx`, `dialPlanA` is returned. This element is returned when `callSourceType` is `DIAL_PATTERN`.
  - `dialPattern` (string): Pattern given to a dial plan. When `originatorType` is `trunk`, `originatorId` is a valid trunk with the name `trunkA`, `trunkA` belongs to a route group which is assigned to a route list with the name `routeListA`, `trunkA` is also assigned to `dialPlanA` as routing choice, `dialPlanA` has `dialPattern` `xxxx` assigned. If the `originatorNumber` matches the `dialPattern` `xxxx`, `dialPattern` `xxxx` is returned. This element is returned when `callSourceType` is `DIAL_PATTERN`.
  - `dialPlanId` (string): Unique identifier for dial plan.
- `destinationType` (string) (**requerido**): * `HOSTED_AGENT` - A destination is a person or workspace with details in the `hostedAgent` field.  * `HOSTED_FEATURE` - Destination is a calling feature like auto-attendant or hunt group with details in the `hostedFeature` field.  * `PBX_USER` - Destination routes into a separate PBX with details in the `pbxUser` field.  * `PSTN_NUMBER` - Destination routes into a PSTN phone number with details in the `pstnNumber` field.  * `VIRTUAL_EXTENSION` - Destination routes into a virtual extension with details in the `virtualExtension` field.  * `VIRTUAL_EXTENSION_RANGE` - Destination routes into a virtual extension range with details in the `virtualExtensionRange` field.  * `ROUTE_LIST` - Destination routes into a route list with details in the `routeList` field.  * `FAC` - Destination routes into a feature access code (FAC) with details in the `featureAccessCode` field.  * `EMERGENCY` - Destination routes into an emergency service like Red Sky, with details in the `emergency` field.  * `REPAIR` - The route is in a repair state with routing choice details in the `repair` field.  * `UNKNOWN_EXTENSION` - Target extension is unknown with routing choice details in the `unknownExtension` field.  * `UNKNOWN_NUMBER` - The target phone number is unknown with routing choice details in the `unknownNumber` field. Valores: HOSTED_AGENT, HOSTED_FEATURE, PBX_USER, PSTN_NUMBER, VIRTUAL_EXTENSION, VIRTUAL_EXTENSION_RANGE, ROUTE_LIST, FAC, EMERGENCY, REPAIR, UNKNOWN_EXTENSION, UNKNOWN_NUMBER.
- `routingAddress` (string) (**requerido**): FAC code if `destinationType` is FAC. The routing address will be returned for all other destination types.
- `outsideAccessCode` (string): Outside access code.
- `isRejected` (boolean) (**requerido**): `true` if the call would be rejected.
- `hostedAgent` (object):
  - `id` (string) (**requerido**): Unique identifier for the person or workspace agent identified as call destination.
  - `type` (string) (**requerido**): * `PEOPLE` - This object is a person.  * `PLACE` - A workspace that is not assigned to a specific person such as for a shared device in a common area. Valores: PEOPLE, PLACE.
  - `firstName` (string) (**requerido**): First name for the hosted agent specified by `id`.
  - `lastName` (string) (**requerido**): Last name for the hosted agent specified by `id`.
  - `locationName` (string) (**requerido**): Name of hosted agent's location.
  - `locationId` (string) (**requerido**): Unique identifier for hosted agent's location.
  - `phoneNumber` (string): Phone number for the hosted agent.
  - `extension` (string): Extension for the hosted agent.
- `hostedFeature` (object):
  - `type` (string) (**requerido**): * `AUTO_ATTENDANT` - The destination is an auto attendant.  * `BROADWORKS_ANYWHERE` - The destination is the Office (Broadworks) Anywhere feature.  * `CALL_QUEUE` - The destination is the Call Queue feature.  * `CONTACT_CENTER_LINK` - The destination is the Contact Center Link feature.  * `GROUP_PAGING` - The destination is the Group Paging feature.  * `HUNT_GROUP` - The destination is the Hunt Group feature.  * `VOICE_MESSAGING` - The destination is the Voice Messaging feature.  * `VOICE_MAIL_GROUP` - The destination is the Voice Mail Group feature. Valores: AUTO_ATTENDANT, BROADWORKS_ANYWHERE, CALL_QUEUE, CONTACT_CENTER_LINK, GROUP_PAGING, HUNT_GROUP, VOICE_MESSAGING, VOICE_MAIL_GROUP.
  - `name` (string) (**requerido**): Name of the service identified as call destination.
  - `id` (string) (**requerido**): Unique identifier of the service identified as call destination.
  - `locationName` (string) (**requerido**): Name of the location with which the service is associated.
  - `locationId` (string) (**requerido**): Unique identifier for the location of the service.
  - `phoneNumber` (string): Phone number of the service.
  - `extension` (string): Extension of the service.
- `pbxUser` (object):
  - `dialPlanName` (string) (**requerido**): Dial plan name that the called string matches.
  - `dialPlanId` (string) (**requerido**): Unique identifier for the dial plan.
  - `dialPattern` (string) (**requerido**): Dial pattern that the called string matches.
  - `trunkName` (string): Name of the trunk.
  - `trunkId` (string): Unique identifier of the trunk.
  - `routeGroupName` (string): Name of the route group.
  - `routeGroupId` (string): Unique identifier of the route group.
  - `trunkLocationName` (string): Location of the trunk; required if `trunkName` is returned.
  - `trunkLocationId` (string): Location ID of the trunk; required if `trunkName` is returned.
- `pstnNumber` (object):
  - `trunkName` (string): Name of the trunk.
  - `trunkId` (string): Unique identifier of the trunk.
  - `routeGroupName` (string): Name of the route group.
  - `routeGroupId` (string): Unique identifier of the route group.
  - `trunkLocationName` (string): Location of the trunk; required if `trunkName` is returned.
  - `trunkLocationId` (string): Location ID of the trunk; required if `trunkName` is returned.
- `virtualExtension` (object):
  - `id` (string) (**requerido**): Unique identifier for the virtual extension.
  - `firstName` (string): First name of the virtual extension.
  - `lastName` (string): Last name of the virtual extension.
  - `displayName` (string) (**requerido**): Full name of the virtual extension.
  - `extension` (string) (**requerido**): Extension that the virtual extension is associated with.
  - `phoneNumber` (string) (**requerido**): Phone number that the virtual extension is associated with.
  - `locationName` (string): Location name if the virtual extension is at the location level, empty if it is at the customer level.
  - `locationId` (string): Location ID if the virtual extension is at the location level, empty if it is at the customer level.
  - `trunkName` (string): Name of the trunk.
  - `trunkId` (string): Unique identifier of the trunk.
  - `routeGroupName` (string): Name of the route group.
  - `routeGroupId` (string): Unique identifier of the route group.
  - `trunkLocationName` (string): Location of the trunk; required if `trunkName` is returned.
  - `trunkLocationId` (string): Location ID of the trunk; required if `trunkName` is returned.

### Ejemplo — respuesta 200
```json
{
  "callSourceInfo": {
    "callSourceType": "DIAL_PATTERN",
    "routeListName": "routeList1",
    "routeListId": "Y2lzY29zcGFyazovL3VzL1JPVVRFX0xJU1QvZDA2YWQ5M2QtY2NkOC00MzI1LTg0YzUtMDA2NThhYTdhMDBj",
    "dialPlanName": "dialPlan1",
    "dialPattern": "*888",
    "dialPlanId": "Y2lzY29zcGFyazovL3VzL0RJQUxfUExBTi8wNTlhMjczZS1iYmIwLTExZWMtODQyMi0wMjQyYWMxMjAwMDI"
  },
  "destinationType": "HOSTED_AGENT",
  "routingAddress": "007",
  "outsideAccessCode": "1234",
  "isRejected": false,
  "hostedAgent": {
    "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mMjU4YjhmZi1lODIxLTQ3MDktYTI2My1mMmI4OWZjN2FlYmQ",
    "type": "PEOPLE",
    "firstName": "firstName",
    "lastName": "lastName",
    "locationName": "locationName",
    "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzVlZmI5MTFhLThmNmUtNGU2Ny1iOTZkLWNkM2VmNmRhNDE2OA",
    "phoneNumber": "9874531287",
    "extension": "111"
  },
  "hostedFeature": {
    "type": "AUTO_ATTENDANT",
    "name": "name1",
    "id": "Y2lzY29zcGFyazovL3VzL0FVVE9fQVRURU5EQU5UL2QyRXdhV2R5TVRCamIwQTJORGswTVRJNU55NXBiblF4TUM1aVkyeGtMbmRsWW1WNExtTnZiUT09",
    "locationName": "locationName1",
    "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzVlZmI5MTFhLThmNmUtNGU2Ny1iOTZkLWNkM2VmNmRhNDE2OA",
    "phoneNumber": "9874531287",
    "extension": "111"
  },
  "pbxUser": {
    "dialPlanName": "dialPlan1",
    "dialPlanId": "Y2lzY29zcGFyazovL3VzL0RJQUxfUExBTi8wNTlhMjczZS1iYmIwLTExZWMtODQyMi0wMjQyYWMxMjAwMDI",
    "dialPattern": "442xxx",
    "trunkName": "trunkName1",
  ... (truncado)
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