---
doc_id: webex-cloud-calling-get-telephony-config-people-me
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me
operation_id: getMyOwnDetails
tags: Call Settings For Me
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.957957+00:00
---

# GET /telephony/config/people/me

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `getMyOwnDetails`

## Resumen
Get My Own Details

## Descripción
Get profile details for the authenticated user.

Profile details include the user's name, email, location and calling details.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Unique identifier of the user.
- `lastName` (string) (**requerido**): Last name of the user.
- `firstName` (string) (**requerido**): First name of the user.
- `email` (string) (**requerido**): The email addresses of the person.
- `announcementLanguage` (string) (**requerido**): Language for announcements.
- `locationDialingCode` (string) (**requerido**): Dialing code for the user's location.
- `supportMobility` (boolean) (**requerido**): If `true`, the user supports mobility.
- `emergencyCallBackNumber` (string) (**requerido**): Emergency callback number for the user.
- `phoneNumbers` (array) (**requerido**): List of numbers associated with the user.
  - `directNumber` (string) (**requerido**): Direct number of the user.
  - `enterprise` (string) (**requerido**): Enterprise number of the user. This always combines the location routing prefix with the user's extension, and is only present when both are present. That is, the location has a routing prefix and the user has an extension.
  - `extension` (string) (**requerido**): Extension of the user. This is always the user's extension, only present if the user has an extension.
  - `routingPrefix` (string) (**requerido**): Routing prefix of the user.
  - `esn` (string) (**requerido**): Enterprise Significant Number. This combines the location routing prefix and extension when both are set, and only the extension when the location routing prefix is not set. if the extension is not set, the esn is not present.
  - `primary` (boolean) (**requerido**): Indicates if the number is primary or alternate number.
- `devices` (array) (**requerido**): List of devices associated with the user.
  - `description` (array) (**requerido**): Comma separated array of tags used to describe device.
  - `model` (string) (**requerido**): Identifier for device model.
  - `mac` (string) (**requerido**): MAC address of the device.
  - `primaryOwner` (boolean) (**requerido**): Indicates whether the person or the workspace is the owner of the device, and points to a primary Line/Port of the device.
  - `type` (string) (**requerido**): * `PRIMARY` - Primary line for the user.  * `SHARED_CALL_APPEARANCE` - Shared line for the user. A shared line allows users to receive and place calls to and from another user's extension, using their own device.  * `MOBILITY` - Device is a shared line. Valores: PRIMARY, SHARED_CALL_APPEARANCE, MOBILITY.
  - `owner` (object) (**requerido**): Details of the owner of the device.
    - `lastName` (string) (**requerido**): First name of device owner.
    - `firstName` (string) (**requerido**): Last name of device owner.
    - `type` (string) (**requerido**): * `PEOPLE` - Indicates the associated member is a person.  * `PLACE` - Indicates the associated member is a workspace. Valores: PEOPLE, PLACE.
  - `activationState` (string) (**requerido**): * `ACTIVATING` - Device is activating using an activation code.  * `ACTIVATED` - Device has been activated using an activation code.  * `DEACTIVATED` - Device has not been activated using an activation code. Valores: ACTIVATING, ACTIVATED, DEACTIVATED.
- `location` (object) (**requerido**):
  - `id` (string): The ID of the location.
  - `name` (string): The name of the location.
- `receptionistUrl` (string) (**requerido**): URL for the receptionist console.
- `callingHostUrl` (string) (**requerido**): URL for the calling host.
- `attendantConsoleUrl` (string) (**requerido**): URL for the attendant console.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mYWZiM2JhYi1hN2UxLTQ1ZGUtYmYzZS1kOWUxMzkxYzU0Yjk",
  "lastName": "Doe",
  "firstName": "John",
  "email": "john.doe@gmail.com",
  "announcementLanguage": "English",
  "locationDialingCode": "8327",
  "supportMobility": false,
  "emergencyCallBackNumber": "+16232992720",
  "phoneNumbers": [
    {
      "directNumber": "+441234222304",
      "enterprise": "832731599",
      "extension": "31599",
      "routingPrefix": "8327",
      "esn": "832731599",
      "primary": true
    },
    {
      "directNumber": "+441234200015",
      "enterprise": "832731587",
      "extension": "31587",
      "routingPrefix": "8327",
      "esn": "832731587",
      "primary": false
    }
  ],
  "devices": [
    {
      "description": [],
      "model": "DMS Cisco 8865",
      "mac": "110723241134",
      "primaryOwner": true,
      "type": "PRIMARY",
      "owner": {
        "lastName": "Mac",
        "firstName": "Jone",
        "type": "PEOPLE"
      },
      "activationState": "ACTIVATED"
    }
  ],
  "location": {
    "name": "Brampton",
    "address": {
      "address1": "mclean",
      "address2": "mclean",
      "city": "mclean",
      "state": "GB-BGE",
      "postalCode": "112233",
      "country": "GB"
    }
  },
  "receptionistUrl": "https://cisco.receptionist.cloud",
  "callingHostUrl": "https://var-int.broadcloudpbx.net",
  "attendantConsoleUrl": "https://cisco.receptionist.cloud"
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