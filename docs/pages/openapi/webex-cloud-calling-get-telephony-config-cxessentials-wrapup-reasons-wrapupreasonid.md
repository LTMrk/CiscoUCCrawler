---
doc_id: webex-cloud-calling-get-telephony-config-cxessentials-wrapup-reasons-wrapupreasonid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/cxEssentials/wrapup/reasons/{wrapupReasonId}
operation_id: Read Wrap Up Reason
tags: Features: Customer Assist
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.488272+00:00
---

# GET /telephony/config/cxEssentials/wrapup/reasons/{wrapupReasonId}

**API:** Webex Cloud Calling
**Área:** Features: Customer Assist
**operationId:** `Read Wrap Up Reason`

## Resumen
Read Wrap Up Reason

## Descripción
Return the wrap-up reason by ID.

Agents handling calls use wrap-up reasons to categorize the outcome after a call ends. The control hub admin can configure these reasons for customers and assign them to queues.
Upon call completion, agents select a wrap-up reason from the queue's assigned list. Each wrap-up reason includes a name and description, and can be set as the default for a queue.
Admins can also configure a timer, which dictates the time agents have to select a reason post-call, with a default of 60 seconds. This timer can be disabled if necessary.

Retrieving the wrap-up reason by ID requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `wrapupReasonId` [path] (string) (**requerido**): Wrap-up reason ID.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/cxEssentials/wrapup/reasons/<wrapupReasonId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `name` (string) (**requerido**): Name of the wrap-up reason.
- `description` (string): Description of the wrap-up reason.
- `defaultWrapupQueuesCount` (number) (**requerido**): Number of queues assigned to the wrap-up reason.
- `queues` (array) (**requerido**): List of queues assigned to the wrap-up reason.
  - `id` (string) (**requerido**): Unique queue identifier.
  - `name` (string) (**requerido**): Name of the queue.
  - `locationName` (string) (**requerido**): Name of the location.
  - `locationId` (string) (**requerido**): Unique location identifier.
  - `phoneNumber` (string) (**requerido**): Phone number of the queue.
  - `extension` (number): Extension of the queue.
  - `defaultWrapupEnabled` (boolean) (**requerido**): Denotes whether the default wrap-up is enabled for the queue.

### Ejemplo — respuesta 200
```json
{
  "name": "Wrap up reason 1",
  "description": "This is a description for wrap-up reason 1",
  "defaultWrapupQueuesCount": 1,
  "queues": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUVVFVUUvOGY1MDI2ZjMtMDZjYi00OTU3LWE0MDQtNDYyM2UzYjJjYzVi",
      "name": "Queue 1",
      "locationName": "Location 1",
      "phoneNumber": "+1234567890",
      "extension": "1234",
      "defaultWrapupEnabled": true
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