---
doc_id: webex-cloud-calling-get-telephony-config-premisepstn-trunks-trunktypes
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/premisePstn/trunks/trunkTypes
operation_id: Read the List of Trunk Types
tags: Call Routing
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.168749+00:00
---

# GET /telephony/config/premisePstn/trunks/trunkTypes

**API:** Webex Cloud Calling
**Área:** Call Routing
**operationId:** `Read the List of Trunk Types`

## Resumen
Read the List of Trunk Types

## Descripción
List all Trunk Types with Device Types for the organization.

A Trunk is a connection between Webex Calling and the premises, which terminates on the premises with a local gateway or other supported device.
The trunk can be assigned to a Route Group which is a group of trunks that allow Webex Calling to distribute calls over multiple trunks or to provide redundancy. Trunk Types are Registering or Certificate Based and are configured in Call Manager.

Retrieving trunk types requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Organization to which the trunk types belong.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/premisePstn/trunks/trunkTypes' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `trunkTypes` (array) (**requerido**): Trunk type with device types.
  - `trunkType` (string) (**requerido**): * `REGISTERING` - For Cisco CUBE Local Gateway.  * `CERTIFICATE_BASED` - For Cisco Unified Border Element, Oracle ACME Session Border Controller, AudioCodes Session Border Controller, Ribbon Session Border Controller. Valores: REGISTERING, CERTIFICATE_BASED.
  - `deviceTypes` (array) (**requerido**): Device types for trunk configuration.

### Ejemplo — respuesta 200
```json
{
  "trunkTypes": [
    {
      "trunkType": "REGISTERING",
      "deviceTypes": [
        {
          "deviceType": "Cisco Unified Border Element",
          "minConcurrentCalls": 250,
          "maxConcurrentCalls": 1000
        }
      ]
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