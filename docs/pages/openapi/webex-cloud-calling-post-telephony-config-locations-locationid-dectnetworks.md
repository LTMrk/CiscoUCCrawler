---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-dectnetworks
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/locations/{locationId}/dectNetworks
operation_id: Create a DECT Network
tags: DECT Devices Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.546498+00:00
---

# POST /telephony/config/locations/{locationId}/dectNetworks

**API:** Webex Cloud Calling
**Área:** DECT Devices Settings
**operationId:** `Create a DECT Network`

## Resumen
Create a DECT Network

## Descripción
Create a multi-cell DECT network for a given location.

DECT networks enable wireless communication for DECT devices within a location, allowing multiple base stations to provide coverage across a larger area.

Creating a DECT network requires a full or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Create a DECT network in this location.
- `orgId` [query] (string): Create a DECT network in this organization.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Name of the DECT network. Min and max length supported for the DECT network name are 1 and 40 respectively.
- `displayName` (string): Add a default name (11 characters max) to display for all handsets. If left blank, the default name will be an indexed number followed by the DECT network name.
- `model` (string) (**requerido**): Select a device model type depending on the number of base stations and handset lines needed in the DECT network.  The corresponding device model display name sometimes called the product name, can also be used to specify the model.  * `DMS Cisco DBS110` - Model name supporting 1 base station and 30 line ports.  * `Cisco DECT 110 Base` - Alternate product/display name which also specifies the model `DMS Cisco DBS110`.  * `DMS Cisco DBS210` - Supports 250 base stations and 1000 line ports.  * `Cisco DECT 210 Base` - Alternate product/display name which also specifies the model `DMS Cisco DBS210`. Valores: DMS Cisco DBS110, Cisco DECT 110 Base, DMS Cisco DBS210, Cisco DECT 210 Base.
- `defaultAccessCodeEnabled` (boolean) (**requerido**): If set to true, need to provide a default access code that will be shared for all users in this network to pair their lines to the next available handset. Otherwise, each user will get a unique 4-digit access code that will be auto-generated. Note: There is currently no public API to retrieve the auto generated access codes for handsets. Use Control Hub instead.
- `defaultAccessCode` (string) (**requerido**): If `defaultAccessCodeEnabled` is set to true, then provide a default access code that needs to be a 4-numeric digit. The access code should be unique to the DECT network for the location.

### Ejemplo — petición
```json
{
  "name": "test-dect",
  "displayName": "test-dect",
  "model": "DMS Cisco DBS210",
  "defaultAccessCodeEnabled": true,
  "defaultAccessCode": "1551"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations/<locationId>/dectNetworks' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "model": "<model>", "defaultAccessCodeEnabled": true, "defaultAccessCode": "<defaultAccessCode>"}'
```

## Respuestas correctas
**201**: Created
- `dectNetworkId` (string) (**requerido**): A unique identifier for the DECT network.

### Ejemplo — respuesta 201
```json
{
  "dectNetworkId": "Y2lzY29zcGFyazovL3VzL0RFQ1RfREVWX05FVC81NmRiMjRkMy03YTdhLTQwYTItOWFjOS1iMjMzMjc3OTIxNzf"
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