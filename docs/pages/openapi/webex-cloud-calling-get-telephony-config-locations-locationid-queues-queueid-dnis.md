---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-queues-queueid-dnis
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/queues/{queueId}/dnis
operation_id: getListOfDnisForACallQueue
tags: Features:  Call Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.698415+00:00
---

# GET /telephony/config/locations/{locationId}/queues/{queueId}/dnis

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `getListOfDnisForACallQueue`

## Resumen
Get List of DNIS for a Call Queue

## Descripción
Get the list of DNIS (Dialed Number Identification Service) entries for a call queue.

DNIS allows call queues to distinguish between primary and alternate numbers when delivering calls to agents. Each DNIS entry can have its own name, phone number, extension, ring pattern, and custom announcement settings.

The maximum number of DNIS entries per call queue is 100.

Retrieving this list requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): The location ID where the call queue exists.
- `queueId` [path] (string) (**requerido**): The call queue ID.
- `orgId` [query] (string): The organization ID of the customer.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/queues/<queueId>/dnis' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `dnisList` (array) (**requerido**): List of DNIS. Will return empty array when there is no DNIS in the queue. Item order is preserved exactly as returned, sorted by DNIS name (ascending).
  - `id` (string) (**requerido**): Unique identifier for the DNIS.
  - `name` (string) (**requerido**): Name of the DNIS.
  - `phoneNumber` (string): Phone number of the DNIS.
  - `extension` (string): Extension of the DNIS.
  - `routingPrefix` (string): Routing prefix (location dialing code) of the DNIS.
  - `esn` (string): Enterprise Significant Number (ESN) of the DNIS.
  - `ringPattern` (string) (**requerido**): Ring pattern of the DNIS. Valores: NORMAL, LONG_LONG, SHORT_SHORT_LONG, SHORT_LONG_SHORT.
  - `customDnisAnnouncementSettingsEnabled` (boolean) (**requerido**): Use custom announcement settings for the DNIS. Enable custom announcement settings using Modify DNIS API. Modify custom announcement settings using Modify DNIS announcements API.

### Ejemplo — respuesta 200
```json
{
  "dnisList": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0ROSVMvZTQ0NTE5OWEtNzlkYS00NWE1LTkyY2EtNDI1YzRmMzA0ZDk5",
      "name": "Support Line",
      "phoneNumber": "+15551234567",
      "extension": "100",
      "routingPrefix": "8501",
      "esn": "8501100",
      "ringPattern": "NORMAL",
      "customDnisAnnouncementSettingsEnabled": false
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