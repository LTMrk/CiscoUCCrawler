---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-agent-availablecallerids
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/{personId}/agent/availableCallerIds
operation_id: retrieveAgentsListOfAvailableCallerIDs
tags: User Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.766359+00:00
---

# GET /telephony/config/people/{personId}/agent/availableCallerIds

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `retrieveAgentsListOfAvailableCallerIDs`

## Resumen
Retrieve Agent's List of Available Caller IDs

## Descripción
Get the list of call queues and hunt groups available for caller ID use by this person as an agent.

This API requires a full, user, or read-only administrator or location administrator auth token with a scope of `spark-admin:people_read`.

## Parámetros
- `personId` [path] (string) (**requerido**): Unique identifier for the person.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/<personId>/agent/availableCallerIds' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `availableCallerIds` (array) (**requerido**): A list of call queues and hunt groups that the agent belongs to and are available to be selected as the Caller ID for outgoing calls. Call queues and hunt groups which have disabled using the phone number as Caller ID are not returned.
  - `id` (string) (**requerido**): Call queue or hunt group's unique identifier.
  - `type` (string) (**requerido**): * `CALL_QUEUE` - A call queue has been selected for the agent's caller ID.  * `HUNT_GROUP` - A hunt group has been selected for the agent's caller ID. Valores: CALL_QUEUE, HUNT_GROUP.
  - `name` (string) (**requerido**): Call queue or hunt group's name.
  - `phoneNumber` (string): When not null, it is call queue or hunt group's phone number.
  - `extension` (string): When not null, it is call queue or hunt group's extension number.

### Ejemplo — respuesta 200
```json
{
  "availableCallerIds": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUVVFVUUvYmRlNDE4NDAtNmVmYS00YTkzLTk5YmEtNDc5Y2QxYTFjZmI5",
      "type": "CALL_QUEUE",
      "name": "TestCallQueue",
      "extension": "6001"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0hVTlRfR1JPVVAvOTExNmRmZDMtZGQ4ZS00YTk5LTg1MmYtMjFiYmMxOGNkNzcy",
      "type": "HUNT_GROUP",
      "name": "TestHuntGroup",
      "phoneNumber": "+441234200090",
      "extension": "6002"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUVVFVUUvZTY1NjgzOTMtZTQ5MC00OGQ2LTg3OTgtY2IyZmY3YzkwNzg0",
      "type": "CALL_QUEUE",
      "name": "TestCallQueueSecond",
      "phoneNumber": "+441234200091",
      "extension": "6003"
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