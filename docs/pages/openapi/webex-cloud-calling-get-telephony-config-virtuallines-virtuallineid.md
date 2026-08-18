---
doc_id: webex-cloud-calling-get-telephony-config-virtuallines-virtuallineid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/virtualLines/{virtualLineId}
operation_id: Get Details for a Virtual Line
tags: Virtual Line Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.390163+00:00
---

# GET /telephony/config/virtualLines/{virtualLineId}

**API:** Webex Cloud Calling
**Área:** Virtual Line Call Settings
**operationId:** `Get Details for a Virtual Line`

## Resumen
Get Details for a Virtual Line

## Descripción
Retrieve Virtual Line details.

Virtual line is a capability in Webex Calling that allows administrators to configure multiple lines to Webex Calling users.

Retrieving virtual line details requires a full, user, read-only administrator, or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `virtualLineId` [path] (string) (**requerido**): Retrieve settings for a virtual line with the matching ID.
- `orgId` [query] (string): Retrieve virtual line settings from this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/virtualLines/<virtualLineId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): A unique identifier for the virtual line.
- `firstName` (string): The first name defined for the virtual line. Minimum length is 1. Maximum length is 64.
- `lastName` (string): The last name defined for the virtual line. Minimum length is 1. Maximum length is 64.
- `displayName` (string): The display name defined for the virtual line.
- `directorySearchEnabled` (boolean) (**requerido**): Flag to indicate a directory search.
- `announcementLanguage` (string) (**requerido**): Virtual Line's announcement language.
- `timeZone` (string): Time zone defined for the virtual line.
- `number` (object) (**requerido**): Calling details of virtual line.
  - `external` (string): Phone number of a virtual line.  Either `external` or `extension` is mandatory.
  - `extension` (string): Extension of a virtual line.  Either `external` or `extension` is mandatory.
  - `primary` (boolean) (**requerido**): Number is Primary or Alternative Number.
- `devices` (array): List of devices assigned to a virtual line.
  - `id` (string) (**requerido**): Unique identifier for a device.
  - `description` (array): Comma separated array of tags used to describe device.
  - `model` (string) (**requerido**): Identifier for device model.
  - `mac` (string): MAC address of device.
  - `primaryOwner` (boolean) (**requerido**): Indicates whether the person or the workspace is the owner of the device and points to a primary Line/Port of the device.
  - `type` (string) (**requerido**): * `PRIMARY` - Primary line for the member.  * `SHARED_CALL_APPEARANCE` - Shared line for the member. A shared line allows users to receive and place calls to and from another user's extension, using their own device. Valores: PRIMARY, SHARED_CALL_APPEARANCE.
  - `owner` (object) (**requerido**):
    - `id` (string) (**requerido**): Unique identifier of a person or a workspace.
    - `type` (string) (**requerido**): * `PEOPLE` - Indicates the associated member is a person.  * `PLACE` - Indicates the associated member is a workspace. Valores: PEOPLE, PLACE.
    - `firstName` (string): The first name of the device owner.
    - `lastName` (string): The last name of the device owner.
  - `activationState` (string) (**requerido**): * `ACTIVATING` - Indicates a device is activating.  * `ACTIVATED` - Indicates a device is activated.  * `DEACTIVATED` - Indicates a device is deactivated. Valores: ACTIVATING, ACTIVATED, DEACTIVATED.
- `location` (object) (**requerido**): Location details of virtual line.
  - `id` (string) (**requerido**): ID of location associated with virtual line.
  - `name` (string) (**requerido**): Name of location associated with virtual line.
  - `address` (object) (**requerido**): The address of the virtual line.
    - `address1` (string) (**requerido**): Address 1 of the location.
    - `address2` (string): Address 2 of the location.
    - `city` (string) (**requerido**): City of the location.
    - `state` (string) (**requerido**): State code of the location.
    - `postalCode` (string) (**requerido**): Postal code of the location.
    - `country` (string) (**requerido**): ISO-3166 2-Letter country code of the location.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfTElORS85Y2JmYjYxZi00ZGM0LTQ1NWItYmMzYS00NmI4YmY5YjQzNzk",
  "firstName": "Bob",
  "lastName": "Smith",
  "displayName": "Bob Smith",
  "directorySearchEnabled": "true",
  "announcementLanguage": "French",
  "timeZone": "Africa/Algiers",
  "number": {
    "external": "+15558675309",
    "extension": "5309",
    "primary": true
  },
  "devices": [
    {
      "id": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMl9hL0RFVklDRS9hNmYwYjhkMi01ZjdkLTQzZDItODAyNi0zM2JkNDg3NjYzMTg=",
      "description": [],
      "model": "DMS Cisco 6871",
      "mac": "123451234502",
      "primaryOwner": false,
      "owner": {
        "id": "Y2lzY29zcGFyazovL3VzL0FVVE9fQVRURU5EQU5UL2J6QjJlRGd6Ym1GeU5rQm1iR1Y0TWk1amFYTmpieTVqYjIw",
        "lastName": "Christian",
        "firstName": "Smith",
        "type": "PEOPLE"
      },
      "activationState": "ACTIVATED",
      "type": "PRIMARY"
    }
  ],
  "location": {
    "name": "Main Location Test",
    "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzMxMTYx",
    "address": {
      "address1": "771 Alder Drive",
      "address2": "Cisco Site 5",
      "city": "Milpitas",
      "state": "CA",
      "postalCode": "95035",
      "country": "US"
    }
  }
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