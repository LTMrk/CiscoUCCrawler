---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-numbers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/numbers
operation_id: Manage Number State in a location
tags: Numbers
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.739950+00:00
---

# PUT /telephony/config/locations/{locationId}/numbers

**API:** Webex Cloud Calling
**Área:** Numbers
**operationId:** `Manage Number State in a location`

## Resumen
Manage Number State in a Location

## Descripción
Activate or deactivate the specified set of phone numbers in a location for an organization.

Each location has a set of phone numbers that can be assigned to people, workspaces, or features. Phone numbers must follow the E.164 format.

Active phone numbers are in service. A mobile number is activated when assigned to a user. This API will not activate or deactivate mobile numbers.

Managing phone number state in a location requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

<br/>

<div><Callout type="warning">This API is only supported for non-integrated PSTN connection types of Local Gateway (LGW) and Non-integrated CCP.</Callout></div>

## Parámetros
- `locationId` [path] (string) (**requerido**): `LocationId` to which numbers should be added.
- `orgId` [query] (string): Organization of the Route Group.

## Cuerpo de la petición (application/json)
- `phoneNumbers` (array) (**requerido**): List of phone numbers whose activation state will be modified according to the specified action.
- `action` (string): Specifies the action to execute on the provided phone numbers. If no action is specified, the default is set to ACTIVATE. For DEACTIVATE action here are few limitations: 1) a maximum of 500 phone numbers can be processed, 2) the numbers must be unassigned, 3) the numbers cannot serve as ECBN (Emergency Callback Number), 4) the numbers must not be mobile numbers, and 5) this action is only applicable to non-integrated PSTN connection types, specifically Local Gateway (LGW) and Non-integrated CCP Valores: ACTIVATE, DEACTIVATE.

### Ejemplo — petición
```json
{
  "phoneNumbers": [
    "+12145557861",
    "+12145551321"
  ],
  "action": "DEACTIVATE"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>/numbers' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"phoneNumbers": []}'
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