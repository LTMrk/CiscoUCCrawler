---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-dectnetworks-dectnetworkid-handsets-handsetid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/dectNetworks/{dectNetworkId}/handsets/{handsetId}
operation_id: Get Specific DECT Network Handset Details
tags: DECT Devices Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.931619+00:00
---

# GET /telephony/config/locations/{locationId}/dectNetworks/{dectNetworkId}/handsets/{handsetId}

**API:** Webex Cloud Calling
**Área:** DECT Devices Settings
**operationId:** `Get Specific DECT Network Handset Details`

## Resumen
Get Specific DECT Network Handset Details

## Descripción
List the specific DECT Network handset details.

A handset can have up to two lines, and a DECT network supports a total of 120 lines across all handsets.
A member on line1 of a DECT handset can be of type PEOPLE or PLACE while a member on line2 of a DECT handset can be of type PEOPLE, PLACE, or VIRTUAL_LINE.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location containing the DECT network.
- `dectNetworkId` [path] (string) (**requerido**): Search handset details in the specified DECT network ID.
- `handsetId` [path] (string) (**requerido**): A unique identifier for the handset.
- `orgId` [query] (string): Organization containing the DECT network.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/dectNetworks/<dectNetworkId>/handsets/<handsetId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Unique identifier of the handset.
- `index` (string) (**requerido**): Index of the handset.
- `customDisplayName` (string): Custom display name for the handset.
- `defaultDisplayName` (string) (**requerido**): Default display name for the handset.
- `baseStationId` (string) (**requerido**): Unique identifier of the associated base station.
- `mac` (string) (**requerido**): MAC Address associated with the handset.
- `accessCode` (string): Access code used to pair handsets to the DECT Network for the first time or if a handset becomes disconnected.
- `lines` (array) (**requerido**): Array of lines associated with the handset. Maximum: 2 lines.
  - `memberId` (string) (**requerido**): ID of the member on line1 of the handset. Members can be PEOPLE or PLACE.
  - `firstName` (string) (**requerido**): Line members's first name.
  - `lastName` (string) (**requerido**): Line members's last name.
  - `external` (string): Line members primary number.
  - `extension` (string): Line members extension.
  - `lastRegistrationTime` (string): Last registration timestamp.
  - `hostIP` (string): Registration host IP address for the line port.
  - `remoteIP` (string): Registration remote IP address for the line port.
  - `location` (object) (**requerido**):
    - `id` (string) (**requerido**): Location identifier associated with the members.
    - `name` (string) (**requerido**): Location name associated with the member.
  - `memberType` (string) (**requerido**): * `PEOPLE` - Indicates the associated member is a person.  * `PLACE` - Indicates the associated member is a workspace. Valores: PEOPLE, PLACE.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0RFQ1RfREVWX0hBTkRTRVQvYjE0MDYyOWUtZTExMy00ODQyLWIxMmMtMDVjODEwYTRjYjIz",
  "index": "1",
  "customDisplayName": "Demo_Handset",
  "defaultDisplayName": "Demo_Handset",
  "baseStationId": "Y2lzY29zcGFyazovL3VzL0RFQ1RfREVWX1NUQVRJT04vYzRhMTQxN2ItZGNiYi00MGMzLWE3YWQtNTY1MGZkZGRkNTNj",
  "mac": "1357D4A1B492",
  "accessCode": "4788",
  "lines": [
    {
      "memberId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jODhiZGIwNC1jZjU5LTRjMjMtODQ4OC00NTNhOTE3ZDFlMjk",
      "firstName": "John",
      "lastName": "Smith",
      "external": "+14088571272",
      "extension": "3459",
      "lastRegistrationTime": "1611229671234",
      "hostIP": "10.0.0.45",
      "remoteIP": "76.102.12.84",
      "location": {
        "id": "Y2lzY29zcGFyazovL3VzL0RFQ1RfREVWX05FVC81NmRiMjRkMy03YTdhLTQwYTItOWFjOS1iMjMzMjc3OTIxTrd",
        "name": "MainOffice"
      },
      "memberType": "PEOPLE"
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