---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-callparks-callparkid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/callParks/{callParkId}
operation_id: Get Details for a Call Park
tags: Features:  Call Park
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.024107+00:00
---

# GET /telephony/config/locations/{locationId}/callParks/{callParkId}

**API:** Webex Cloud Calling
**Área:** Features:  Call Park
**operationId:** `Get Details for a Call Park`

## Resumen
Get Details for a Call Park

## Descripción
Retrieve Call Park details.

Call Park allows call recipients to place a call on hold so that it can be retrieved from another device.

Retrieving call park details requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

**NOTE**: The Call Park ID will change upon modification of the Call Park name.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieve settings for a call park in this location.
- `callParkId` [path] (string) (**requerido**): Retrieve settings for a call park with the matching ID.
- `orgId` [query] (string): Retrieve call park settings from this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/callParks/<callParkId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): A unique identifier for the call park.
- `name` (string) (**requerido**): Unique name for the call park. The maximum length is 80.
- `recall` (object) (**requerido**):
  - `huntGroupId` (string): Alternate user which is a hunt group ID for call park recall alternate destination.
  - `huntGroupName` (string): Unique name for the hunt group.
  - `option` (string) (**requerido**): Call park recall options.  * `ALERT_PARKING_USER_ONLY` - Alert parking user only.  * `ALERT_PARKING_USER_FIRST_THEN_HUNT_GROUP` - Alert parking user first, then hunt group.  * `ALERT_HUNT_GROUP_ONLY` - Alert hunt group only. Valores: ALERT_PARKING_USER_ONLY, ALERT_PARKING_USER_FIRST_THEN_HUNT_GROUP, ALERT_HUNT_GROUP_ONLY.
- `agents` (array): People, workspaces and virtual lines that are eligible to receive calls.
  - `id` (string) (**requerido**): ID of a person, workspace or virtual line.
  - `firstName` (string): First name of a person, workspace or virtual line.
  - `lastName` (string): Last name of a person, workspace or virtual line.
  - `displayName` (string): Display name of a person, workspace or virtual line.
  - `type` (string) (**requerido**): Type of the person, workspace or virtual line.  * `PEOPLE` - Indicates that this object is a user.  * `PLACE` - Indicates that this object is a place.  * `VIRTUAL_LINE` - Indicates that this object is a virtual line. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
  - `email` (string) (**requerido**): Email of a person or workspace.
  - `numbers` (array): List of phone numbers of a person, workspace or virtual line.
    - `external` (string): Phone number of a person, workspace or virtual line.
    - `extension` (string): Extension of a person, workspace or virtual line.
- `parkOnAgentsEnabled` (boolean) (**requerido**): Whether or not the calls will be parked on agents as a destination.
- `callParkExtensions` (array): Array of call park extensions assigned to a call park.
  - `id` (string) (**requerido**): Unique identifier for the call park extension.
  - `extension` (string) (**requerido**): The extension for the call park.
  - `name` (string) (**requerido**): A unique name for the call park extension.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUEFSSy9kR1ZqYUc1cFkyRnNJSE4xY0hCdmNuUWdMU0JwYm5OMWNtRnVZMlVnTFNCamRYTjBiMjFsY2lBeA==",
  "name": "technical support - insurance - customer 1",
  "recall": {
    "huntGroupId": "Y2lzY29zcGFyazovL3VzL0hVTlRfR1JPVVAvZEdWamFHNXBZMkZzTFhOMWNIQnZjblF0TlRVMU9EWTNOVE13T1VCbmJXRnBiQzVqYjIwPQ",
    "huntGroupName": "Technical Support Group - 5558675309",
    "option": "ALERT_PARKING_USER_FIRST_THEN_HUNT_GROUP"
  },
  "agents": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80NDVkMzMzMC1mNjE3LTExZWItOWQyZS01NzViODE3ZGE2NmE",
      "firstName": "John",
      "lastName": "Brown",
      "displayName": "John Brown",
      "type": "PEOPLE",
      "email": "john.brown@example.com",
      "numbers": [
        {
          "external": "+19075552859",
          "extension": "8080",
          "routingPrefix": "1234",
          "esn": "12348080",
          "primary": "true"
        }
      ]
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS83MGY2MzYzMC1mZjlmLTExZWItODU5YS0xZjhiYjRjNzc1MWQ",
      "firstName": "John",
      "lastName": "Smith",
      "displayName": "John Smith",
      "type": "PEOPLE",
      "email": "john.smith@example.com",
      "numbers": [
        {
          "external": "+19075553859",
          "extension": "8081",
          "routingPrefix": "1234",
          "esn": "12348081",
          "primary": "true"
        }
      ]
    }
  ],
  "parkOnAgentsEnabled": false,
  "callParkExtensions": [
    {
      "id": "Y3lzY29zcGFyazovL
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