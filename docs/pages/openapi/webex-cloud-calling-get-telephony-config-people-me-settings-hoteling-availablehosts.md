---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-hoteling-availablehosts
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/settings/hoteling/availableHosts
operation_id: getAvailableHotelingHosts
tags: Call Settings For Me Phase 5
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.982482+00:00
---

# GET /telephony/config/people/me/settings/hoteling/availableHosts

**API:** Webex Cloud Calling
**Área:** Call Settings For Me Phase 5
**operationId:** `getAvailableHotelingHosts`

## Resumen
Get Available Hoteling Hosts

## Descripción
Retrieve a list of available hoteling hosts that a person can associate with as a guest. Returns hosts that have hoteling enabled on their devices and are available for guest associations. The list can be filtered by name or phone number and supports pagination.

Hoteling is a feature of Webex Calling that enables flexible workspace solutions by allowing users to log into shared devices.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Parámetros
- `max` [query] (integer): Limit the maximum number of hosts in the response. Default is 100. Por defecto: 2000.
- `start` [query] (integer): Start index for pagination. Default is 0. Por defecto: 0.
- `name` [query] (string): Filter hosts by name (first name or last name). Partial match is supported.
- `phoneNumber` [query] (string): Filter hosts by phone number. Partial match is supported.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/settings/hoteling/availableHosts' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `hosts` (array) (**requerido**): List of available hoteling hosts.
  - `hostId` (string) (**requerido**): Unique identifier for the person or workspace.
  - `firstName` (string) (**requerido**): First name of the hoteling host.
  - `lastName` (string) (**requerido**): Last name of the hoteling host.
  - `phoneNumber` (string) (**requerido**): Phone number of the hoteling host.
  - `extension` (string) (**requerido**): Extension of the hoteling host.
  - `allowedAssociationDuration` (integer) (**requerido**): Maximum allowed association duration in hours for this host.

### Ejemplo — respuesta 200
```json
{
  "hosts": [
    {
      "hostId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hYmNkZWYxMi0zNDU2LTc4OTAtYWJjZC1lZjEyMzQ1Njc4OTA",
      "firstName": "John",
      "lastName": "Doe",
      "phoneNumber": "+14085551234",
      "extension": "1234",
      "allowedAssociationDuration": 24
    },
    {
      "hostId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85ODc2NTQzMi0xMjM0LTU2NzgtOTBhYi1jZGVmMTIzNDU2Nzg",
      "firstName": "Jane",
      "lastName": "Smith",
      "phoneNumber": "+14085555678",
      "extension": "5678",
      "allowedAssociationDuration": 12
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