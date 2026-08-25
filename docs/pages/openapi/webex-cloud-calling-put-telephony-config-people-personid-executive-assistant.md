---
doc_id: webex-cloud-calling-put-telephony-config-people-personid-executive-assistant
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/people/{personId}/executive/assistant
operation_id: modifyPersonExecutiveAssistantSettings
tags: User Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.564780+00:00
---

# PUT /telephony/config/people/{personId}/executive/assistant

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `modifyPersonExecutiveAssistantSettings`

## Resumen
Modify Person Executive Assistant Settings

## Descripción
Update executive assistant settings for the specified person when person is configured as executive assistant.

Executive assistants can make, answer, intercept, and route calls appropriately on behalf of their executive.
Assistants can also set the call forwarding destination, and join or leave an executive’s pool.

This API requires a full, user, or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `personId` [path] (string) (**requerido**): A unique identifier for the person.
- `orgId` [query] (string): Organization ID for the person.

## Cuerpo de la petición (application/json)
- `forwardFilteredCallsEnabled` (boolean): If `true`, filtered calls to assistant are forwarded to the `forwardToPhoneNumber`.
- `forwardToPhoneNumber` (string): Phone number to forward the filtered calls to. Mandatory if `forwardFilteredCallsEnabled` is set to true.
- `executives` (array): List of executives.
  - `personId` (string) (**requerido**): Unique identifier of the executive.
  - `optInEnabled` (boolean) (**requerido**): If `true`, the assistant has opted in to handle calls for the executive.

### Ejemplo — petición
```json
{
  "forwardFilteredCallsEnabled": true,
  "forwardToPhoneNumber": "+19075552860",
  "executives": [
    {
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8zZWQzNDg0MS0yZTkwLTQ4OGEtYmVmZi1iNTk0OTA1ODFkNWM",
      "optInEnabled": true
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/people/<personId>/executive/assistant' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**204**: Person executive assistant settings updated successfully.

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