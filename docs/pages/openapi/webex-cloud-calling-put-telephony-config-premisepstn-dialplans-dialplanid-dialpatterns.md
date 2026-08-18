---
doc_id: webex-cloud-calling-put-telephony-config-premisepstn-dialplans-dialplanid-dialpatterns
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/premisePstn/dialPlans/{dialPlanId}/dialPatterns
operation_id: Modify Dial Patterns
tags: Call Routing
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.165958+00:00
---

# PUT /telephony/config/premisePstn/dialPlans/{dialPlanId}/dialPatterns

**API:** Webex Cloud Calling
**Área:** Call Routing
**operationId:** `Modify Dial Patterns`

## Resumen
Modify Dial Patterns

## Descripción
Modify dial patterns for the Dial Plan.

Dial plans route calls to on-premises destinations by use of trunks or route groups.
They are configured globally for an enterprise and apply to all users, regardless of location.
A dial plan also specifies the routing choice (trunk or route group) for calls that match any of its dial patterns.
Specific dial patterns can be defined as part of your dial plan.

Modifying a dial pattern requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `dialPlanId` [path] (string) (**requerido**): ID of the dial plan being modified.
- `orgId` [query] (string): Organization to which dial plan belongs.

## Cuerpo de la petición (application/json)
- `dialPatterns` (array): Array of dial patterns to add or delete. Dial Pattern that is not present in the request is not modified.
  - `dialPattern` (string): A unique dial pattern.
  - `action` (string): * `ADD` - Add action, when adding a new dial pattern  * `DELETE` - Delete action, when deleting an existing dial pattern Valores: ADD, DELETE.
- `deleteAllDialPatterns` (boolean): Delete all the dial patterns for a dial plan.

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/premisePstn/dialPlans/<dialPlanId>/dialPatterns' \
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