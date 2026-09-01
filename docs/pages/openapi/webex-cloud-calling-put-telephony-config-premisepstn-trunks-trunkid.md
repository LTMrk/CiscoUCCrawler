---
doc_id: webex-cloud-calling-put-telephony-config-premisepstn-trunks-trunkid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/premisePstn/trunks/{trunkId}
operation_id: Modify a Trunk
tags: Call Routing
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.567320+00:00
---

# PUT /telephony/config/premisePstn/trunks/{trunkId}

**API:** Webex Cloud Calling
**Área:** Call Routing
**operationId:** `Modify a Trunk`

## Resumen
Modify a Trunk

## Descripción
Modify a Trunk for the organization.

A Trunk is a connection between Webex Calling and the premises, which terminates on the premises with a local gateway or other supported device.
The trunk can be assigned to a Route Group - a group of trunks that allow Webex Calling to distribute calls over multiple trunks or to provide redundancy.

Modifying a trunk requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `trunkId` [path] (string) (**requerido**): ID of the trunk being modified.
- `orgId` [query] (string): Organization to which trunk belongs.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): A unique name for the dial plan.
- `password` (string) (**requerido**): A password to use on the trunk.
- `dualIdentitySupportEnabled` (boolean): Determines the behavior of the From and PAI headers on outbound calls.
- `maxConcurrentCalls` (number): Max Concurrent call. Required to create a static certificate-based trunk.
- `pChargeInfoSupportPolicy` (string): * `DISABLED` - The P-Charge-Info header support policy is disabled.  * `ASSERTED_IDENTITY` - The P-Charge-Info header is always included in outbound PSTN calls using Webex Calling primary number or location’s main number.  * `CONFIGURABLE_CHARGE_NUMBER` - The P-Charge-Info header is included in outbound PSTN calls using the originating or redirecting Webex Calling entity's location charge number if set, else the entity's primary number if set and not toll-free, else the main number of the entity's location if set and not toll-free. If none of these are set or not toll-free, it uses the same number as the ASSERTED_IDENTITY option. Valores: DISABLED, ASSERTED_IDENTITY, CONFIGURABLE_CHARGE_NUMBER.

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/premisePstn/trunks/<trunkId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "password": "<password>"}'
```

## Respuestas correctas
**204**: No Content

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