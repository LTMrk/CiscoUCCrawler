---
doc_id: webex-cloud-calling-get-telephony-config-devices-dects-supporteddevices
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/devices/dects/supportedDevices
operation_id: readTheDectDeviceTypeListDeprecated
tags: Device Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.267052+00:00
---

# GET /telephony/config/devices/dects/supportedDevices

**API:** Webex Cloud Calling
**Área:** Device Call Settings
**operationId:** `readTheDectDeviceTypeListDeprecated`

## Resumen
Read the DECT device type list - Deprecated

## Descripción
<div><Callout type="warning">Not supported for Webex for Government (FedRAMP).</Callout></div>

<div><Callout type="warning">The REST path for this API has changed to [GET /telephony/config/devices/dectNetworks/supportedDevices{?orgId}]. The use of this old REST path is deprecated and will be decommissioned on October 10, 2024. Please start using it for all future projects.</Callout></div>

Get DECT device type list with base stations and line ports supported count. This is a static list.

Retrieving this list requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string):

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/devices/dects/supportedDevices' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `devices` (array) (**requerido**): Contains a list of devices.
  - `model` (string) (**requerido**): Model name of the device.
  - `displayName` (string) (**requerido**): Display name of the device.
  - `numberOfBaseStations` (number): Indicates number of base stations.
  - `numberOfLinePorts` (number): Indicates number of port lines,
  - `numberOfRegistrationsSupported` (number): Indicates number of supported registrations.

### Ejemplo — respuesta 200
```json
{
  "devices": [
    {
      "model": "DMS Cisco DBS110",
      "displayName": "Cisco DECT 110 Base",
      "numberOfBaseStations": 2,
      "numberOfLinePorts": 20,
      "numberOfRegistrationsSupported": 10
    },
    {
      "model": "DMS Cisco DBS210",
      "displayName": "Cisco DECT 210 Base",
      "numberOfBaseStations": 250,
      "numberOfLinePorts": 1000,
      "numberOfRegistrationsSupported": 30
    }
  ]
}
```
- Cabecera `Link`: 

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