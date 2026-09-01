---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-monitoring
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/settings/monitoring
operation_id: getMyMonitoringSettings
tags: Call Settings For Me
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.583986+00:00
---

# GET /telephony/config/people/me/settings/monitoring

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `getMyMonitoringSettings`

## Resumen
Get My Monitoring Settings

## Descripción
Retrieves the monitoring settings for the authenticated person, which shows specified people, places, virtual lines or call park extensions that are being monitored.

Monitors the line status which indicates if a person, place or virtual line is on a call and if a call has been parked on that extension.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/settings/monitoring' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `callParkNotificationEnabled` (boolean) (**requerido**): Call park notification is enabled or disabled. Only applies to monitored users, workspaces, and virtual lines. Does not apply to call park extensions.
- `monitoredElements` (array) (**requerido**): Settings of monitored elements which can be person, place, virtual line or call park extension.
  - `callparkextension` (object):
    - `id` (string) (**requerido**): ID of call park extension.
    - `name` (string) (**requerido**): Name of call park extension.
    - `extension` (string) (**requerido**): Extension of call park extension.
    - `routingPrefix` (string): Routing prefix of location.
    - `esn` (string): Routing prefix + extension of a person or workspace.
    - `location` (string) (**requerido**): Name of location for call park extension.
    - `locationId` (string) (**requerido**): ID of location for call park extension.
    - `lineKeyLabel` (string): Customizable line key label for monitored call park extension.
  - `member` (object):
    - `id` (string): The identifier of the monitored person or workspace.
    - `firstName` (string): The first name of the monitored person, place, or virtual line.
    - `lastName` (string): The last name of the monitored person, place, or virtual line.
    - `displayName` (string): The display name of the monitored person, place, or virtual line.
    - `type` (string): The type of the monitored person, place, or virtual line.  * `PEOPLE` - Object is a user.  * `PLACE` - Object is a workspace. Valores: PEOPLE, PLACE.
    - `email` (string): The email address of the monitored person, place, or virtual line.
    - `numbers` (array): The list of phone numbers of the monitored person, place, or virtual line.
      - `external` (string): Phone number of person or workspace. Either `phoneNumber` or `extension` is mandatory.
      - `extension` (string): Extension of person or workspace. Either `phoneNumber` or `extension` is mandatory.
      - `routingPrefix` (string): Routing prefix of location.
      - `esn` (string): Routing prefix + extension of a person or workspace.
      - `primary` (boolean) (**requerido**): Flag to indicate primary phone.
      - `tollFreeNumber` (boolean): Flag to indicate toll free number.
    - `location` (string): The location name where the line is.
    - `locationId` (string): The ID for the location.
    - `lineKeyLabel` (string): Customizable line key label for monitored member.
  - `speedDial` (object):
    - `id` (string): The identifier of the speed dial.
    - `displayName` (string): The display name of the speed dial.
    - `type` (string): The type of the speed dial.  * `PEOPLE` - Object is a user.  * `PLACE` - Object is a workspace.  * `VIRTUAL_LINE` - Object is a virtual line. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
    - `lineKeyLabel` (string): Customizable line key label for speed dial.
    - `phoneNumber` (string): The phone number of the speed dial.
    - `location` (string): The location name where the speed dial is.
    - `locationId` (string): The ID for the location.

### Ejemplo — respuesta 200
```json
{
  "callParkNotificationEnabled": true,
  "monitoredElements": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85M2JjZWQ2Mi1lYWRmLTQ0MGItYThiYi03ZWQ5ZWEwNzExMTg",
      "lastName": "Nelson",
      "firstName": "John",
      "displayName": "John Nelson",
      "type": "PEOPLE",
      "email": "john.nelson@gmail.com",
      "extension": "50003",
      "esn": "50003",
      "locationName": "San Francisco",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzFiNDIzN2U4LWE2MDYtNGM5Ni1iMDZmLTYzMmU5N2FjZmQxNg"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUEFSS19FWFRFTlNJT04vNDk1ZTgxMTEtY2U4My00ZTc5LWJjOTAtODM2OWQxZjY0NTQ2",
      "displayName": "Dallas-Test",
      "type": "CALL_PARK_EXTENSION",
      "extension": "10082",
      "locationName": "San Francisco",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzFiNDIzN2U4LWE2MDYtNGM5Ni1iMDZmLTYzMmU5N2FjZmQxNg"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMV9pbnQxMy9QTEFDRS9mZTg5NmVmMC1iYTk3LTQ3NGYtOTMwZS03ODQxYzUwMjFhNDU=",
      "displayName": "TXS16 ConfRoom1",
      "type": "PLACE",
      "email": "fe896ef0-ba97-474f-930e-7841c5021a45@csg1test.room.wbx2.com",
      "directNumber": "+15594015485",
      "locationName": "San Francisco",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzFiNDIzN2U4LWE2MDYtNGM5Ni1iMDZmLTYzMmU5N2FjZmQxNg"
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