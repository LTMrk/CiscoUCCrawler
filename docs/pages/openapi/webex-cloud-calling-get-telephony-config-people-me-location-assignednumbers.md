---
doc_id: webex-cloud-calling-get-telephony-config-people-me-location-assignednumbers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/location/assignedNumbers
operation_id: getAvailableNumbersForMyLocation
tags: Call Settings For Me With UserHub Phase2
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.162948+00:00
---

# GET /telephony/config/people/me/location/assignedNumbers

**API:** Webex Cloud Calling
**Área:** Call Settings For Me With UserHub Phase2
**operationId:** `getAvailableNumbersForMyLocation`

## Resumen
Get Available Numbers for User's Location

## Descripción
Get Available Numbers for User's Location.

Fetch all the numbers available in User's location.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Parámetros
- `max` [query] (number): Limit the maximum number of numbers in the response.
- `start` [query] (number): Specify the offset from the first result that you want to fetch.
- `name` [query] (string): List numbers whose owner name contains this string.
- `phoneNumber` [query] (string): List numbers whose phoneNumber contains this string.
- `extension` [query] (string): List numbers whose extension contains this string.
- `order` [query] (string): Sort the list of numbers based on `lastName`, `dn`, `extension` either asc or desc.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/location/assignedNumbers' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Available numbers retrieved for the authenticated user's location.
- `phoneNumbers` (array): List of assigned phone numbers/extension in user's location.
  - `phoneNumber` (string): The phone number in E.164 format.
  - `extension` (string): The extension.
  - `state` (string): * `ACTIVE` - Phone number is in the active state.  * `INACTIVE` - Phone number is in the inactive state. Valores: ACTIVE, INACTIVE.
  - `phoneNumberType` (string): * `PRIMARY` - A direct phone number. * `ALTERNATE` - An alternate phone number. * `FAX` - A FAX number. Valores: PRIMARY, ALTERNATE, FAX.
  - `tollFreeNumber` (boolean): Indicate if the number is toll free.
  - `owner` (object): The owner details.
    - `type` (string) (**requerido**): * `PLACE` - PSTN phone number's owner is a workspace.  * `PEOPLE` - PSTN phone number's owner is a person.  * `VIRTUAL_LINE` - PSTN phone number's owner is a Virtual Profile.  * `AUTO_ATTENDANT` - PSTN phone number's owner is an auto-attendant.  * `CALL_QUEUE` - PSTN phone number's owner is a call queue.  * `GROUP_PAGING` - PSTN phone number's owner is a group paging.  * `HUNT_GROUP` - PSTN phone number's owner is a hunt group.  * `VOICE_MESSAGING` - PSTN phone number's owner is a voice messaging.  * `OFFICE_ANYWHERE` - PSTN phone number's owner is a Single Number Reach.  * `CONTACT_CENTER_LINK` - PSTN phone number's owner is a Contact Center link.  * `CONTACT_CENTER_ADAPTER` - PSTN phone number's owner is a Contact Center adapter.  * `ROUTE_LIST` - PSTN phone number's owner is a route list.  * `VOICEMAIL_GROUP` - PSTN phone number's owner is a voicemail group.  * `COLLABORATE_BRIDGE` - PSTN phone number's owner is a collaborate bridge. Valores: PLACE, PEOPLE, VIRTUAL_LINE, AUTO_ATTENDANT, CALL_QUEUE, GROUP_PAGING, HUNT_GROUP, VOICE_MESSAGING, OFFICE_ANYWHERE, CONTACT_CENTER_LINK, CONTACT_CENTER_ADAPTER, ROUTE_LIST, VOICEMAIL_GROUP, COLLABORATE_BRIDGE.
    - `firstName` (string): First name of the phone number/extension owner. This field is present only for type `PEOPLE` and `VIRTUAL_LINE`.
    - `lastName` (string): Last name of the phone number/extension owner. This field is present only for type `PEOPLE` and `VIRTUAL_LINE`.
    - `displayName` (string): Display Name of the phone number/extension owner.

### Ejemplo — respuesta 200
```json
{
  "phoneNumbers": [
    {
      "phoneNumber": "+16177817765",
      "extension": "765",
      "state": "ACTIVE",
      "phoneNumberType": "PRIMARY",
      "tollFreeNumber": false,
      "owner": {
        "type": "HUNT_GROUP",
        "displayName": "testingdemoHunt"
      }
    }
  ]
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served.
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