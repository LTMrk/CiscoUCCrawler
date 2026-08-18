---
doc_id: webex-cloud-calling-get-telephony-config-premisepstn-dialplans-dialplanid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/premisePstn/dialPlans/{dialPlanId}
operation_id: Get a Dial Plan
tags: Call Routing
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.166952+00:00
---

# GET /telephony/config/premisePstn/dialPlans/{dialPlanId}

**API:** Webex Cloud Calling
**Área:** Call Routing
**operationId:** `Get a Dial Plan`

## Resumen
Get a Dial Plan

## Descripción
Get a Dial Plan for the organization.

Dial plans route calls to on-premises destinations by use of trunks or route groups.
They are configured globally for an enterprise and apply to all users, regardless of location.
A dial plan also specifies the routing choice (trunk or route group) for calls that match any of its dial patterns.
Specific dial patterns can be defined as part of your dial plan.

Retrieving a dial plan requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `dialPlanId` [path] (string) (**requerido**): ID of the dial plan.
- `orgId` [query] (string): Organization to which dial plan belongs.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/premisePstn/dialPlans/<dialPlanId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Unique identifier for the dial plan.
- `name` (string) (**requerido**): A unique name for the dial plan.
- `routeId` (string) (**requerido**): ID of route type associated with the dial plan.
- `routeName` (string) (**requerido**): Name of route type associated with the dial plan.
- `routeType` (string) (**requerido**): * `ROUTE_GROUP` - Route group must include at least one trunk with a maximum of 10 trunks per route group.  * `TRUNK` - Connection between Webex Calling and the premises. Valores: ROUTE_GROUP, TRUNK.
- `customer` (object) (**requerido**):
  - `id` (string) (**requerido**): ID of the customer/organization.
  - `name` (string) (**requerido**): Name of the customer/organization.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0RJQUxfUExBTi8wNTlhMjczZS1iYmIwLTExZWMtODQyMi0wMjQyYWMxMjAwMDI",
  "name": "dialPlanName",
  "routeId": "Y2lzY29zcGFyazovL3VzL1JPVVRFX0dST1VQLzA1OWEyNzNlLWJiYjAtMTFlYy04NDIyLTAyNDJhYzEyMDAwMg",
  "routeName": "routeName",
  "routeType": "ROUTE_GROUP",
  "customer": {
    "id": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
    "name": "test_org"
  }
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