---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-agent-callerid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/{personId}/agent/callerId
operation_id: retrieveAgentsCallerIDInformation
tags: User Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.158166+00:00
---

# GET /telephony/config/people/{personId}/agent/callerId

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `retrieveAgentsCallerIDInformation`

## Resumen
Retrieve Agent's Caller ID Information

## Descripción
Retrieve the Agent's Caller ID Information.

Each agent will be able to set their outgoing Caller ID as either the Call Queue's Caller ID, Hunt Group's Caller ID or their own configured Caller ID.

This API requires a full admin or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `personId` [path] (string) (**requerido**): Unique identifier for the person.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/<personId>/agent/callerId' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `selectedCallerId` (object) (**requerido**):
  - `id` (string) (**requerido**): When not null, this is the call queue or hunt group's unique identifier.
  - `type` (string) (**requerido**): * `CALL_QUEUE` - A call queue has been selected for the agent's caller ID.  * `HUNT_GROUP` - A hunt group has been selected for the agent's caller ID. Valores: CALL_QUEUE, HUNT_GROUP.
  - `name` (string) (**requerido**): When not null, indicates the call queue's or hunt group's name.
  - `phoneNumber` (string) (**requerido**): When not null, indicates the call queue's or hunt group's phone number.
  - `extension` (string) (**requerido**): When not null, indicates the call queue's or hunt group's extension number.

### Ejemplo — respuesta 200
```json
{
  "selectedCallerId": {
    "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUVVFVUUvMzc4NzRjOGUtMzRhOS00NzFjLWI1N2QtMzAxNTJkZjlmMjQx",
    "type": "CALL_QUEUE",
    "name": "new ram",
    "phoneNumber": "+81123456890",
    "extension": "09899"
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