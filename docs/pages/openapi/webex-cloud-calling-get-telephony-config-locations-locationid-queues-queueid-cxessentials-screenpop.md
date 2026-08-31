---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-queues-queueid-cxessentials-screenpop
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/queues/{queueId}/cxEssentials/screenPop
operation_id: Read Screen Pop Configuration
tags: Features: Customer Assist
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.278536+00:00
---

# GET /telephony/config/locations/{locationId}/queues/{queueId}/cxEssentials/screenPop

**API:** Webex Cloud Calling
**Área:** Features: Customer Assist
**operationId:** `Read Screen Pop Configuration`

## Resumen
Read Screen Pop Configuration

## Descripción
Returns the screen pop configuration for a call queue in a location.

Screen pop lets agents view customer-related info in a pop-up window.

Retrieving the screen pop configuration requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): The location ID where the call queue resides.
- `queueId` [path] (string) (**requerido**): The call queue ID for which screen pop configuration is modified.
- `orgId` [query] (string): The organization ID of the customer or partner's organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/queues/<queueId>/cxEssentials/screenPop' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `enabled` (boolean): Enable/disable screen pop.
- `screenPopUrl` (string): The screen pop URL that integrates Webex calls with other business apps like CRM, ticketing tools, and order entry systems.
- `desktopLabel` (string): A label for the screen pop configuration.
- `queryParams` (object):
  - `example_param_1` (string): An example key-value pair that will be sent to the agent.
  - `example_param_2` (string): Another example key-value pair that will be sent to the agent.
  - `example_param_3` (string): Another example key-value pair that will be sent to the agent.

### Ejemplo — respuesta 200
```json
{
  "enabled": true,
  "screenPopUrl": "http://localhost:8086/screenpop",
  "desktopLabel": "example screen pop",
  "queryParams": {
    "example-param": "example-value"
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