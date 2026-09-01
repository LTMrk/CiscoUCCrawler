---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-callforwarding-availablenumbers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/{personId}/callForwarding/availableNumbers
operation_id: getPersonCallForwardAvailablePhoneNumbers
tags: User Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.767714+00:00
---

# GET /telephony/config/people/{personId}/callForwarding/availableNumbers

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `getPersonCallForwardAvailablePhoneNumbers`

## Resumen
Get Person Call Forward Available Phone Numbers

## Descripción
List the service and standard PSTN numbers that are available to be assigned as a person's call forward number.
These numbers are associated with the location of the person specified in the request URL, can be active or inactive, and are assigned to an owning entity.

The available numbers APIs help identify candidate numbers and their owning entities to simplify the assignment or association of these numbers to members or features.

Retrieving this list requires a full, read-only or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `personId` [path] (string) (**requerido**): Unique identifier for the person.
- `orgId` [query] (string): List numbers for this organization.
- `max` [query] (number): Limit the number of phone numbers returned to this maximum count. The default is 2000.
- `start` [query] (number): Start at the zero-based offset in the list of matching phone numbers. The default is 0.
- `phoneNumber` [query] (array): Filter phone numbers based on the comma-separated list provided in the `phoneNumber` array.
- `ownerName` [query] (string): Return the list of phone numbers that are owned by the given `ownerName`. Maximum length is 255.
- `extension` [query] (string): Returns the list of PSTN phone numbers with the given `extension`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/<personId>/callForwarding/availableNumbers' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `phoneNumbers` (array) (**requerido**): Array of phone numbers.
  - `phoneNumber` (string): A unique identifier for the PSTN phone number.
  - `extension` (string): Extension for a PSTN phone number.
  - `state` (string) (**requerido**): * `ACTIVE` - Phone number is in the active state.  * `INACTIVE` - Phone number is in the inactive state. Valores: ACTIVE, INACTIVE.
  - `isMainNumber` (boolean) (**requerido**): If `true`, the phone number is used as a location CLID.
  - `tollFreeNumber` (boolean) (**requerido**): If `true`, the phone number is a toll-free number.
  - `telephonyType` (string) (**requerido**): * `PSTN_NUMBER` - The object is a PSTN number. Valores: PSTN_NUMBER.
  - `isServiceNumber` (boolean) (**requerido**): If `true`, the phone number is a service number; otherwise, it is a standard number. Service numbers are high-utilization or high-concurrency PSTN phone numbers that are neither mobile nor toll-free.
  - `owner` (object):
    - `id` (string) (**requerido**): Unique identifier of the owner to which the number is assigned.
    - `type` (string) (**requerido**): * `PLACE` - PSTN phone number's owner is a workspace.  * `PEOPLE` - PSTN phone number's owner is a person.  * `VIRTUAL_LINE` - PSTN phone number's owner is a Virtual Profile.  * `AUTO_ATTENDANT` - PSTN phone number's owner is an auto-attendant.  * `CALL_QUEUE` - PSTN phone number's owner is a call queue.  * `GROUP_PAGING` - PSTN phone number's owner is a group paging.  * `HUNT_GROUP` - PSTN phone number's owner is a hunt group.  * `VOICE_MESSAGING` - PSTN phone number's owner is a voice messaging.  * `OFFICE_ANYWHERE` - PSTN phone number's owner is a Single Number Reach.  * `CONTACT_CENTER_LINK` - PSTN phone number's owner is a Contact Center link.  * `CONTACT_CENTER_ADAPTER` - PSTN phone number's owner is a Contact Center adapter.  * `ROUTE_LIST` - PSTN phone number's owner is a route list.  * `VOICEMAIL_GROUP` - PSTN phone number's owner is a voicemail group.  * `COLLABORATE_BRIDGE` - PSTN phone number's owner is a collaborate bridge. Valores: PLACE, PEOPLE, VIRTUAL_LINE, AUTO_ATTENDANT, CALL_QUEUE, GROUP_PAGING, HUNT_GROUP, VOICE_MESSAGING, OFFICE_ANYWHERE, CONTACT_CENTER_LINK, CONTACT_CENTER_ADAPTER, ROUTE_LIST, VOICEMAIL_GROUP, COLLABORATE_BRIDGE.
    - `firstName` (string): First name of the number's owner. This field will be present only when the owner `type` is `PEOPLE` or `VIRTUAL_LINE`.
    - `lastName` (string): Last name of the number's owner. This field will be present only when the owner `type` is `PEOPLE` or `VIRTUAL_LINE`.
    - `displayName` (string): Display name of the number's owner.

### Ejemplo — respuesta 200
```json
{
  "phoneNumbers": [
    {
      "phoneNumber": "+12056350001",
      "state": "ACTIVE",
      "isMainNumber": false,
      "telephonyType": "PSTN_NUMBER",
      "tollFreeNumber": false,
      "isServiceNumber": false,
      "owner": {
        "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jODhiZGIwNC1jZjU5LTRjMjMtODQ4OC00NTNhOTE3ZDFlMjk",
        "type": "PEOPLE",
        "firstName": "Test",
        "lastName": "Person",
        "displayName": "Test Person"
      }
    },
    {
      "phoneNumber": "+12056350002",
      "extension": "1235",
      "state": "ACTIVE",
      "isMainNumber": true,
      "telephonyType": "PSTN_NUMBER",
      "tollFreeNumber": false,
      "isServiceNumber": true,
      "owner": {
        "id": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMV9pbnQxMy9QTEFDRS9lZjJkMjg3Ny1hYTY0LTRkMjQtYTFjNi02OWExMmNhMWI2YTA=",
        "type": "PLACE",
        "displayName": "TestWorkSpace"
      }
    },
    {
      "phoneNumber": "+12056350003",
      "extension": "1236",
      "state": "INACTIVE",
      "isMainNumber": false,
      "telephonyType": "PSTN_NUMBER",
      "tollFreeNumber": true,
      "isServiceNumber": false,
      "owner": {
        "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUVVFVUUvYm1kMmVIcHNabTgwWVVBMk5EazBNVEk1Tnk1cGJuUXhNQzVpWTJ4a0xuZGxZbVY0TG1OdmJRPT0",
        "type": "CALL_QUEUE",
        "displayName": "Test call queue"
      }
    }
  ]
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