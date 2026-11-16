---
doc_id: webex-cloud-calling-post-telephony-config-actions-testcallrouting-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/actions/testCallRouting/invoke
operation_id: testCallRouting
tags: Call Routing
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:50.553586+00:00
---

# POST /telephony/config/actions/testCallRouting/invoke

**API:** Webex Cloud Calling
**Área:** Call Routing
**operationId:** `testCallRouting`

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
- `originatorType` (object) (**requerido**): This element is used to identify if the `originatorId` is of type `PEOPLE` or `TRUNK`.
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
- `callSourceInfo` (object): Only returned when `originatorNumber` is specified in the request.
- `destinationType` (object) (**requerido**): Destination type for the call.
- `routingAddress` (string) (**requerido**): FAC code if `destinationType` is FAC. The routing address will be returned for all other destination types.
- `outsideAccessCode` (string): Outside access code.
- `isRejected` (boolean) (**requerido**): `true` if the call would be rejected.
- `hostedAgent` (object): Returned when `destinationType` is `HOSTED_AGENT`.
- `hostedFeature` (object): Returned when `destinationType` is `HOSTED_FEATURE`.
- `pbxUser` (object): Returned when `destinationType` is `PBX_USER`.
- `pstnNumber` (object): Returned when `destinationType` is `PSTN_NUMBER`.
- `virtualExtension` (object): Returned when `destinationType` is `VIRTUAL_EXTENSION`.
- `virtualExtensionRange` (object): Returned when `destinationType` is `VIRTUAL_EXTENSION_RANGE`.
- `routeList` (object): Returned when `destinationType` is `ROUTE_LIST`.
- `featureAccessCode` (object): Returned when `destinationType` is `FAC`.
- `emergency` (object): Returned when `destinationType` is `EMERGENCY`.
- `repair` (object): Returned when `destinationType` is `REPAIR`.
- `unknownExtension` (object): Returned when `destinationType` is `UNKNOWN_EXTENSION`.
- `unknownNumber` (object): Returned when `destinationType` is `UNKNOWN_NUMBER`.
- `appliedServices` (array): Returned if any origin is configured with intercept details, outgoing permissions by type, or translation pattern.
  - `translationPattern` (object): Returns the details of the Translation Pattern if applied.
  - `interceptDetails` (object): Returns the details of call intercept if applied.
  - `outgoingCallingPlanPermissionsByType` (object): Returns the details of permissions by type configuration if applied under OCP.
  - `outgoingCallingPlanPermissionsByDigitPattern` (object): Returns the details of the digit pattern configuration if applied under OCP.

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