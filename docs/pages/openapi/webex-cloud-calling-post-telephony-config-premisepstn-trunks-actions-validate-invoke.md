---
doc_id: webex-cloud-calling-post-telephony-config-premisepstn-trunks-actions-validate-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/premisePstn/trunks/actions/validate/invoke
operation_id: Validate a Trunk
tags: Call Routing
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-15T08:15:48.719912+00:00
---

# POST /telephony/config/premisePstn/trunks/actions/validate/invoke

**API:** Webex Cloud Calling
**Área:** Call Routing
**operationId:** `Validate a Trunk`

## Resumen
Validate a Trunk

## Descripción
Validate Local Gateway trunk settings for the organization before creation.

Local Gateway trunks connect Webex Calling to on-premises PSTN infrastructure, terminating on a local gateway or other supported device. Trunks can be assigned to Route Groups to distribute calls across multiple trunks or to provide redundancy.

This endpoint validates FQDN, domain, peer identity, and trunk type settings prior to trunk creation.

Validating a trunk requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Organization to which the trunk belongs.

## Cuerpo de la petición (application/json)
- `fqdnAddress` (string): FQDN or SRV address of the trunk.
- `fqdnDomain` (string): Domain name of the trunk.
- `fqdnPort` (integer): FQDN port of the trunk.
- `trunkType` (string): * `REGISTERING` - For Cisco CUBE Local Gateway.  * `CERTIFICATE_BASED` - For Cisco Unified Border Element, Oracle ACME Session Border Controller, AudioCodes Session Border Controller, Ribbon Session Border Controller. Valores: REGISTERING, CERTIFICATE_BASED.
- `isRestrictedToDedicatedInstance` (boolean): Flag to indicate if the trunk is restricted to a dedicated instance.
- `peerIdentity` (string): Peer identity for certificate-based trunks. Used for TLS peer verification.

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/premisePstn/trunks/actions/validate/invoke' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**204**: No Content

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
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