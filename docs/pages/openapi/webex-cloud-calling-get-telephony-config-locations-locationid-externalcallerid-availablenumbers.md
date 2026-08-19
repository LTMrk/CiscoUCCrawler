---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-externalcallerid-availablenumbers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/externalCallerId/availableNumbers
operation_id: Get the List of Phone Numbers Available for External Caller ID
tags: Location Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.115377+00:00
---

# GET /telephony/config/locations/{locationId}/externalCallerId/availableNumbers

**API:** Webex Cloud Calling
**Área:** Location Call Settings
**operationId:** `Get the List of Phone Numbers Available for External Caller ID`

## Resumen
Get the List of Phone Numbers Available for External Caller ID

## Descripción
Get the list of phone numbers available for external caller ID usage by a Webex Calling entity (such as a person, virtual line, or workspace) within the specified location.
Numbers from the specified location are returned and cross location numbers are returned as well where the number's location has the same country, PSTN provider, and zone (only applicable for India locations) as the specified location.
When `personId` is specified, and the person belongs to a cisco PSTN location, has a mobile number assigned as primary DN, and does not have a billing plan, only the assigned mobile number is returned as the available number for caller ID.

The available numbers APIs help identify candidate numbers and their owning entities to simplify the assignment or association of these numbers to members or features.

Retrieving this list requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieve available external caller ID numbers for this location.
- `orgId` [query] (string): List numbers for this organization.
- `max` [query] (number): Limit the number of phone numbers returned to this maximum count. The default is 2000.
- `start` [query] (number): Start at the zero-based offset in the list of matching phone numbers. The default is 0.
- `phoneNumber` [query] (array): Filter phone numbers based on the provided list in the `phoneNumber` array.
- `ownerName` [query] (string): Return the list of phone numbers that are owned by the given `ownerName`. Maximum length is 255.
- `personId` [query] (string): Retrieve available external caller ID numbers for this person. If `personId` is not provided it may result in the unsuccessful assignment of the returned number. This parameter has no effect when workspace or virtual line ID is used.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/externalCallerId/availableNumbers' \
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

### Ejemplo — respuesta 200
```json
{
  "phoneNumbers": [
    {
      "phoneNumber": "+12036390542",
      "state": "ACTIVE",
      "isMainNumber": false,
      "tollFreeNumber": false,
      "isServiceNumber": true,
      "location": {
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzkzMGMzYTNlLTA3Y2EtNDNmOS1iZjE4LTZlZGM2OGE1Y2Y3Yg",
        "name": "Bangalore"
      },
      "owner": {
        "id": "Y2lzY29zcGFyazovL3VzL0hVTlRfR1JPVVAvWkhabFpuQjVhblY2WjBBMk5EazBNVEk1Tnk1cGJuUXhNQzVpWTJ4a0xuZGxZbVY0TG1OdmJRPT0",
        "type": "HUNT_GROUP",
        "displayName": "testingdemo"
      }
    },
    {
      "phoneNumber": "+447975777966",
      "state": "ACTIVE",
      "isMainNumber": false,
      "tollFreeNumber": false,
      "isServiceNumber": false,
      "location": {
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzkzMGMzYTNlLTA3Y2EtNDNmOS1iZjE4LTZlZGM2OGE1Y2Y3Yg",
        "name": "Bangalore"
      },
      "owner": {
        "id": "Y2lzY29zcGFyazovL3VzL0hVTlRfR1JPVVAvWW04MWMyNTVjWFZ6Y1VBMk5EazBNVEk1Tnk1cGJuUXhNQzVpWTJ4a0xuZGxZbVY0TG1OdmJRPT0",
        "type": "HUNT_GROUP",
        "displayName": "CallertestingVeeresh9999te"
      }
    },
    {
      "phoneNumber": "+447975777969",
      "state": "INACTIVE",
      "isMainNumber": true,
      "tollFreeNumber": false,
      "isServiceNumber": false,
      "location": {
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzkzMGMzYTNlLTA3Y2EtNDNmOS1iZjE4LTZlZGM2OGE1Y2Y3Yg",
        "name": "Bangalore"
      },
      "owner": {
        "id": "Y2lzY29zcGFyazovL3VzL1
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