---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-numbers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/locations/{locationId}/numbers
operation_id: Add Phone Numbers to a location
tags: Numbers
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.739762+00:00
---

# POST /telephony/config/locations/{locationId}/numbers

**API:** Webex Cloud Calling
**Área:** Numbers
**operationId:** `Add Phone Numbers to a location`

## Resumen
Add Phone Numbers to a Location

## Descripción
Adds a specified set of phone numbers to a location for an organization. Phone numbers must follow the E.164 format.

Each location has a set of phone numbers that can be assigned to people, workspaces, or features. Active phone numbers are in service.

Adding a phone number to a location requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

Phone numbers included in the request that already exist in the location will simply be ignored.

<br/>

<div><Callout type="warning">This API is only supported for adding DID and Toll-free numbers to non-integrated PSTN connection types such as Local Gateway (LGW) and Non-integrated CPP. It should never be used for locations with integrated PSTN connection types like Cisco Calling Plans or Integrated CCP because backend data issues may occur.
</Callout></div>
<div><Callout type="warning">Mobile numbers can be added to any location that has PSTN connection setup. Only 20 mobile numbers can be added per request.
</Callout></div>

## Parámetros
- `locationId` [path] (string) (**requerido**): LocationId to which numbers should be added.
- `orgId` [query] (string): Organization of the Route Group.

## Cuerpo de la petición (application/json)
- `phoneNumbers` (array) (**requerido**): List of phone numbers that need to be added.
- `numberType` (string): * `TOLLFREE` - A toll-free PSTN number.  * `DID` - A normal Direct Inward Dial (DID) PSTN number.  * `MOBILE` - A mobile number. Valores: TOLLFREE, DID, MOBILE.
- `numberUsageType` (string): * `NONE` - Standard/user number usage (default).  * `SERVICE` - The number will be used in high-volume service, for example, Contact Center. Valores: NONE, SERVICE.
- `state` (string): * `ACTIVE` - The number is activated and has calling capability.  * `INACTIVE` - A number is not yet activated and has no calling capability. Valores: ACTIVE, INACTIVE.
- `subscriptionId` (string): The `subscriptionId` to be used for the mobile number order.
- `carrierId` (string/uuid): The `carrierId` to be used for the mobile number order.

### Ejemplo — petición
```json
{
  "phoneNumbers": [
    "+19136748203",
    "+19136748204",
    "+19136748205"
  ],
  "numberType": "TOLLFREE",
  "numberUsageType": "NONE",
  "state": "INACTIVE",
  "carrierId": "123e4567-e89b-12d3-a456-426614174000"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations/<locationId>/numbers' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"phoneNumbers": []}'
```

## Respuestas correctas
**201**: Created

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