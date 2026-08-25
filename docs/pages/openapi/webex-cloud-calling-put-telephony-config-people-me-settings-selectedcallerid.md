---
doc_id: webex-cloud-calling-put-telephony-config-people-me-settings-selectedcallerid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/people/me/settings/selectedCallerId
operation_id: modifyMySelectedCallerIDSettings
tags: Call Settings For Me
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.352670+00:00
---

# PUT /telephony/config/people/me/settings/selectedCallerId

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `modifyMySelectedCallerIDSettings`

## Resumen
Configure My Selected Caller ID Settings

## Descripción
Update selected caller ID settings associated with the authenticated user.

Caller ID settings control how a person's information is displayed when making outgoing calls.
Selected Caller ID settings allow users to choose which configuration among available caller IDs is selected currently.

This API requires a user auth token with a scope of `spark:telephony_config_write`.

## Cuerpo de la petición (application/json)
- `selected` (object) (**requerido**): Selected caller ID settings.
  - `type` (string) (**requerido**): * `DEFAULT_CLID` - Caller ID is the default configured caller ID.  * `ADDITIONAL_CLID` - Caller ID is an additional external caller ID phone number available for the user.  * `CALL_QUEUE` - Caller ID is associated with a call queue.  * `HUNT_GROUP` - Caller ID is associated with a hunt group. Valores: DEFAULT_CLID, ADDITIONAL_CLID, CALL_QUEUE, HUNT_GROUP.
  - `id` (string): Unique identifier of the selected caller ID (HuntGroup / CallQueue) config. Required only when setting `CALL_QUEUE` or `HUNT_GROUP` caller IDs.
  - `directNumber` (string): Direct number of the selected caller ID. Required only when setting ADDITIONAL_CLID as the selected caller ID.

### Ejemplo — petición
```json
{
  "selected": {
    "type": "HUNT_GROUP",
    "id": "Y2lzY29zcGFyazovL3VzL0hVTlRfR1JPVVAvNmU1NTVjZDAtNjM0MS00MmI4LWEyMWMtZTc1ZjIxNDQ4Mjc1"
  }
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/people/me/settings/selectedCallerId' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"selected": {}}'
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