---
doc_id: webex-cloud-calling-post-telephony-config-premisepstn-trunks
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/premisePstn/trunks
operation_id: Create a Trunk
tags: Call Routing
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.342753+00:00
---

# POST /telephony/config/premisePstn/trunks

**API:** Webex Cloud Calling
**Área:** Call Routing
**operationId:** `Create a Trunk`

## Resumen
Create a Trunk

## Descripción
Create a Trunk for the organization.

A Trunk is a connection between Webex Calling and the premises, which terminates on the premises with a local gateway or other supported device.
The trunk can be assigned to a Route Group which is a group of trunks that allow Webex Calling to distribute calls over multiple trunks or to provide redundancy.

Creating a trunk requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Organization to which the trunk belongs.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): A unique name for the trunk.
- `locationId` (string) (**requerido**): ID of location associated with the trunk.
- `password` (string) (**requerido**): A password to use on the trunk.
- `dualIdentitySupportEnabled` (boolean): Dual Identity Support setting impacts the handling of the From header and P-Asserted-Identity header when sending an initial SIP `INVITE` to the trunk for an outbound call.
- `trunkType` (string) (**requerido**): * `REGISTERING` - For Cisco CUBE Local Gateway.  * `CERTIFICATE_BASED` - For Cisco Unified Border Element, Oracle ACME Session Border Controller, AudioCodes Session Border Controller, Ribbon Session Border Controller. Valores: REGISTERING, CERTIFICATE_BASED.
- `deviceType` (string): Device type assosiated with trunk.
- `address` (string): FQDN or SRV address. Required to create a static certificate-based trunk.
- `domain` (string): Domain name. Required to create a static certificate based trunk.
- `port` (number): FQDN port. Required to create a static certificate-based trunk.
- `maxConcurrentCalls` (number): Max Concurrent call. Required to create a static certificate based trunk.
- `pChargeInfoSupportPolicy` (string): * `DISABLED` - The P-Charge-Info header support policy is disabled.  * `ASSERTED_IDENTITY` - The P-Charge-Info header is always included in outbound PSTN calls using Webex Calling primary number or location’s main number.  * `CONFIGURABLE_CHARGE_NUMBER` - The P-Charge-Info header is included in outbound PSTN calls using the originating or redirecting Webex Calling entity's location charge number if set, else the entity's primary number if set and not toll-free, else the main number of the entity's location if set and not toll-free. If none of these are set or not toll-free, it uses the same number as the ASSERTED_IDENTITY option. Valores: DISABLED, ASSERTED_IDENTITY, CONFIGURABLE_CHARGE_NUMBER.

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/premisePstn/trunks' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "locationId": "<locationId>", "password": "<password>", "trunkType": "<trunkType>"}'
```

## Respuestas correctas
**201**: Created
- `id` (string) (**requerido**): ID of the newly created trunk.

### Ejemplo — respuesta 201
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1JPVVRFX0dST1VQLzA1OWEyNzNlLWJiYjAtMTFlYy04NDIyLTAyNDJhYzEyMDAwMg"
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