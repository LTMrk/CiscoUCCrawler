---
doc_id: webex-cloud-calling-get-telephony-config-numbers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/numbers
operation_id: Get Phone Numbers for an Organization with Given Criteria
tags: Numbers
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.131565+00:00
---

# GET /telephony/config/numbers

**API:** Webex Cloud Calling
**Área:** Numbers
**operationId:** `Get Phone Numbers for an Organization with Given Criteria`

## Resumen
Get Phone Numbers for an Organization with Given Criteria

## Descripción
List all the phone numbers for the given organization along with the status and owner (if any).

Numbers can be standard, service, or mobile. Both standard and service numbers are PSTN numbers.
Service numbers are considered high-utilization or high-concurrency phone numbers and can be assigned to features like auto-attendants, call queues, and hunt groups.
Phone numbers can be linked to a specific location, be active or inactive, and be assigned or unassigned.
The owner of a number is the person, workspace, or feature to which the number is assigned.
Only a person can own a mobile number.

Retrieving this list requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): List numbers for this organization.
- `locationId` [query] (string): Return the list of phone numbers for this location within the given organization. The maximum length is 36.
- `max` [query] (integer): Limit the number of phone numbers returned to this maximum count. The default is 2000.
- `start` [query] (integer): Start at the zero-based offset in the list of matching phone numbers. The default is 0.
- `phoneNumber` [query] (string): Search for this `phoneNumber`.
- `available` [query] (boolean): Search among the available phone numbers. This parameter cannot be used along with `ownerType` parameter when set to `true`.
- `order` [query] (string): Sort the list of phone numbers based on the following:`lastName`,`dn`,`extension`. Sorted by number and extension in ascending order.
- `ownerName` [query] (string): Return the list of phone numbers that are owned by the given `ownerName`. Maximum length is 255.
- `ownerId` [query] (string): Returns only the matched number/extension entries assigned to the feature with the specified UUID or `broadsoftId`.
- `ownerType` [query] (string): Returns the list of phone numbers of the given `ownerType`. Possible input values: Valores: PEOPLE, PLACE, AUTO_ATTENDANT, CALL_QUEUE, PAGING_GROUP, HUNT_GROUP, VOICE_MESSAGING, BROADWORKS_ANYWHERE, CONTACT_CENTER_LINK, ROUTE_LIST, VOICEMAIL_GROUP, VIRTUAL_LINE.
- `extension` [query] (string): Returns the list of phone numbers with the given extension.
- `numberType` [query] (string): Returns the filtered list of phone numbers that contain a given type of number. `available` or `state` query parameters cannot be used when `numberType=EXTENSION`. Possible input values: Valores: NUMBER, EXTENSION.
- `phoneNumberType` [query] (string): Returns the filtered list of phone numbers of the given `phoneNumberType`. Response excludes any extensions without numbers. Possible input values: Valores: PRIMARY, ALTERNATE, FAX, DNIS, Default.
- `state` [query] (string): Returns the list of phone numbers with the matching state. Response excludes any extensions without numbers. Possible input values: Valores: ACTIVE, INACTIVE, Default.
- `details` [query] (boolean): Returns the overall count of the phone numbers along with other details for a given organization.
- `tollFreeNumbers` [query] (boolean): Returns the list of toll-free phone numbers.
- `restrictedNonGeoNumbers` [query] (boolean): Returns the list of restricted non-geographical numbers.
- `includedTelephonyTypes` [query] (string): Returns the list of phone numbers that are of given `includedTelephonyTypes`. By default, if this query parameter is not provided, it will list both PSTN and Mobile Numbers. Possible input values are PSTN_NUMBER or MOBILE_NUMBER.
- `serviceNumber` [query] (boolean): Returns the list of service phone numbers.
- `reservedNumber` [query] (boolean): Filters reserved phone numbers. When set to `true`, returns only reserved phone numbers. When set to `false`, returns only non-reserved phone numbers. When omitted, no reserved-number filter is applied. Reserved numbers cannot be assigned to people, features, or services. This parameter cannot be used along with the `available` filter, whether `available` is set to `true` for available numbers or `false` for assigned numbers; using both returns a `400` error. This parameter also cannot be used along with the `assigned` filter; using both returns a `400` error.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/numbers' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `phoneNumbers` (array) (**requerido**): Array of phone numbers.
  - `phoneNumber` (string): A unique identifier for the phone number.
  - `extension` (string): Extension for a phone number.
  - `routingPrefix` (string): Routing prefix of location.
  - `esn` (string): Routing prefix + extension of a person or workspace.
  - `state` (string) (**requerido**): Phone number's state.
  - `phoneNumberType` (string) (**requerido**): Returns the filtered list of phone numbers of the given `phoneNumberType`. Response excludes any extensions without numbers. Possible input values:  * `PRIMARY` - Filter the results to include only primary phone numbers.  * `ALTERNATE` - Filter the results to include only alternate phone numbers.  * `FAX` - Filter the results to include only FAX phone numbers.  * `DNIS` - Filter the results to include only Dialed Number Identification Service (DNIS) phone numbers.  * `Default` - Filter the results to include all numbers. Valores: PRIMARY, ALTERNATE, FAX, DNIS, Default.
  - `mainNumber` (boolean) (**requerido**): If `true`, the phone number is used as location CLID.
  - `includedTelephonyTypes` (string) (**requerido**): * `PSTN_NUMBER` - The object is a PSTN number. Valores: PSTN_NUMBER.
  - `mobileNetwork` (string): Mobile Network for the number if the number is MOBILE_NUMBER.
  - `routingProfile` (string): Routing Profile for the number if the number is MOBILE_NUMBER.
  - `tollFreeNumber` (boolean) (**requerido**): If `true`, the phone number is a toll-free number.
  - `isServiceNumber` (boolean) (**requerido**): If `true`, the phone number is a service number; otherwise, it is a standard number.
  - `isReservedNumber` (boolean) (**requerido**): Flag to indicate if the number is a reserved number. Reserved numbers cannot be assigned to people, features, or services.
  - `location` (object):
    - `id` (string) (**requerido**): ID of location in which phone number exists.
    - `name` (string) (**requerido**): Name of the location for phone number.
  - `owner` (object):
    - `id` (string): ID of the owner to which phone number is assigned.
    - `type` (string): * `PLACE` - PSTN phone number's owner is a workspace.  * `PEOPLE` - PSTN phone number's owner is a person.  * `VIRTUAL_LINE` - PSTN phone number's owner is a Virtual Profile.  * `AUTO_ATTENDANT` - PSTN phone number's owner is an auto-attendant.  * `CALL_QUEUE` - PSTN phone number's owner is a call queue.  * `GROUP_PAGING` - PSTN phone number's owner is a group paging.  * `HUNT_GROUP` - PSTN phone number's owner is a hunt group.  * `VOICE_MESSAGING` - PSTN phone number's owner is a voice messaging.  * `OFFICE_ANYWHERE` - PSTN phone number's owner is a Single Number Reach.  * `CONTACT_CENTER_LINK` - PSTN phone number's owner is a Contact Center link.  * `CONTACT_CENTER_ADAPTER` - PSTN phone number's owner is a Contact Center adapter.  * `ROUTE_LIST` - PSTN phone number's owner is a route list.  * `VOICEMAIL_GROUP` - PSTN phone number's owner is a voicemail group.  * `COLLABORATE_BRIDGE` - PSTN phone number's owner is a collaborate bridge. Valores: PLACE, PEOPLE, VIRTUAL_LINE, AUTO_ATTENDANT, CALL_QUEUE, GROUP_PAGING, HUNT_GROUP, VOICE_MESSAGING, OFFICE_ANYWHERE, CONTACT_CENTER_LINK, CONTACT_CENTER_ADAPTER, ROUTE_LIST, VOICEMAIL_GROUP, COLLABORATE_BRIDGE.
    - `firstName` (string): First name of the phone number's owner.
    - `lastName` (string): Last name of the phone number's owner.
- `count` (object):
  - `assigned` (integer): Count of phone numbers that are in the assigned state.
  - `unAssigned` (integer): Count of phone numbers which are in the un-assigned state.
  - `inActive` (integer): Count of phone numbers which are inactive.
  - `extensionOnly` (integer): Count of extensions only without phone number.
  - `tollFreeNumbers` (integer): Count of the toll free numbers.
  - `total` (integer): Total phone numbers and extensions available.
  - `mobileNumber` (integer): Count of phone numbers of type `MOBILE_NUMBER` only without `PSTN_NUMBER` and extension.
  - `serviceNumber` (integer): Count of phone numbers with `includedTelephonyTypes` as `PSTN_NUMBER` and `isServiceNumber` value as `true`.
  - `reservedNumber` (integer): Count of reserved phone numbers.

### Ejemplo — respuesta 200
```json
{
  "count": {
    "assigned": 33,
    "unAssigned": 114,
    "inActive": 12,
    "extensionOnly": 692,
    "tollFreeNumbers": 1,
    "total": 839,
    "mobileNumber": 6,
    "serviceNumber": 1,
    "reservedNumber": 1
  },
  "phoneNumbers": [
    {
      "phoneNumber": "+12056350001",
      "extension": "11",
      "routingPrefix": "1234",
      "esn": "123411",
      "state": "ACTIVE",
      "phoneNumberType": "FAX",
      "mainNumber": false,
      "includedTelephonyTypes": "MOBILE_NUMBER",
      "mobileNetwork": "mobileNetwork",
      "routingProfile": "AttRtPf",
      "tollFreeNumber": false,
      "isServiceNumber": false,
      "location": {
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2E4Mjg5NzIyLTFiODAtNDFiNy05Njc4LTBlNzdhZThjMTA5OA",
        "name": "Banglore"
      },
      "owner": {
        "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jODhiZGIwNC1jZjU5LTRjMjMtODQ4OC00NTNhOTE3ZDFlMjk",
        "type": "PEOPLE",
        "firstName": "sadiqhussain96",
        "lastName": "sadiqhussain96"
      },
      "isReservedNumber": false
    },
    {
      "phoneNumber": "",
      "state": "ACTIVE",
      "phoneNumberType": "ALTERNATE",
      "extension": "568",
      "routingPrefix": "1234",
      "esn": "1234568",
      "mainNumber": false,
      "includedTelephonyTypes": "PSTN_NUMBER",
      "tollFreeNumber": false,
      "isServiceNumber": false,
      "location": {
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2M2MDliOGE1LTAxNmQtNDAwNy1hN2E0LTJhMThiZmZjY2FmNg",
        "na
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