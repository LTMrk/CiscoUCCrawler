---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-dectnetworks-dectnetworkid-handsets-bulk
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/locations/{locationId}/dectNetworks/{dectNetworkId}/handsets/bulk
operation_id: Add a List of Handsets to a DECT Network
tags: DECT Devices Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.323863+00:00
---

# POST /telephony/config/locations/{locationId}/dectNetworks/{dectNetworkId}/handsets/bulk

**API:** Webex Cloud Calling
**Área:** DECT Devices Settings
**operationId:** `Add a List of Handsets to a DECT Network`

## Resumen
Add a List of Handsets to a DECT Network

## Descripción
Add a list of up to 50 handsets to a DECT network in a location.

A DECT network acts as a container that can support up to 1,000 lines across all handsets, with each handset capable of handling up to two lines. Once the network is created, you can add bases, handsets, and assign users or lines as needed.

Adding a list of handsets to a DECT network requires a full or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

<div><Callout type="warning">Adding a DECT handset to a person with a Webex Calling Standard license will disable Webex Calling across their Webex mobile, tablet, desktop, and browser applications.

</Callout></div>

<div><Callout type="warning">Adding or removing handsets to the DECT network in less than 90 seconds may result in base station not having the latest configuration until the base station is rebooted.</Callout></div>

## Parámetros
- `locationId` [path] (string) (**requerido**): Add handsets in this location.
- `dectNetworkId` [path] (string) (**requerido**): A unique identifier for the DECT network.
- `orgId` [query] (string): Add handsets in this organization.

## Cuerpo de la petición (application/json)
- `items` (array) (**requerido**): List of handsets that are to be added to the DECT network.
  - `line1MemberId` (string) (**requerido**): ID of the member on line1 of the handset. Members can be PEOPLE or PLACE.
  - `line2MemberId` (string): ID of the member on line2 of the handset. Members can be PEOPLE, PLACE, or VIRTUAL_LINE.
  - `customDisplayName` (string) (**requerido**): Custom display name on the handset. Min and max length supported for the custom display name is 1 and 16 respectively.

### Ejemplo — petición
```json
{
  "items": [
    {
      "line1MemberId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jODhiZGIwNC1jZjU5LTRjMjMtODQ4OC00NTNhOTE3ZDFlMjk",
      "line2MemberId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jMjExMWFhZi1kNTFlLTRkNTMtODlhNS00NTcwNzQ1NGYyYWY",
      "customDisplayName": "handsetName1"
    },
    {
      "line1MemberId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85YzNlZDRmYi05MzJiLTQyOTYtODMxNC1iZWY1ZmRlNGRmYjM",
      "customDisplayName": "handsetName2"
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations/<locationId>/dectNetworks/<dectNetworkId>/handsets/bulk' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"items": []}'
```

## Respuestas correctas
**201**: Created
- `items` (array) (**requerido**): List of added handsets.
  - `customDisplayName` (string) (**requerido**): The custom display name on the handset.
  - `result` (object) (**requerido**): The result of the add handset request.
    - `status` (number) (**requerido**): The status of the add handset request.

### Ejemplo — respuesta 201
```json
{
  "items": [
    {
      "customDisplayName": "handsetName1",
      "result": {
        "status": 200
      }
    },
    {
      "customDisplayName": "handsetName2",
      "result": {
        "status": 200
      }
    }
  ]
}
```
**206**: Partial Content
- `items` (array) (**requerido**): List of added handsets.
  - `customDisplayName` (string) (**requerido**): The custom display name on the handset.
  - `result` (object) (**requerido**): The result of the add handset request.
    - `status` (number) (**requerido**): The status of the add handset request. 200 indicates the handset was added successfully.
    - `error` (object): The error message if the add handset request failed.
      - `message` (string) (**requerido**): The error message.
      - `errorCode` (number) (**requerido**): The error code.

### Ejemplo — respuesta 206
```json
{
  "items": [
    {
      "customDisplayName": "handsetName1",
      "result": {
        "status": 200
      }
    },
    {
      "customDisplayName": "handsetName2",
      "result": {
        "status": 400,
        "error": {
          "message": "[Error 4516] Cannot assign user to device: {0} with line/Port: {1}",
          "errorCode": 4516
        }
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