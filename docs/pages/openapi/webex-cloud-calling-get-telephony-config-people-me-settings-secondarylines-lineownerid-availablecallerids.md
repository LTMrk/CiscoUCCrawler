---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-secondarylines-lineownerid-availablecallerids
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/settings/secondaryLines/{lineownerId}/availableCallerIds
operation_id: getMySecondaryLinesAvailableCallerIDList
tags: Call Settings For Me
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.956708+00:00
---

# GET /telephony/config/people/me/settings/secondaryLines/{lineownerId}/availableCallerIds

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `getMySecondaryLinesAvailableCallerIDList`

## Resumen
Get My Secondary Line Owner's Available Caller ID List

## Descripción
Get details of available caller IDs for a secondary line of the authenticated user.

Note that an authenticated user can only retrieve information for their configured secondary lines.

Caller ID settings control how a person's information is displayed when making outgoing calls.
The available caller ID list shows the caller IDs that the user can choose from.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Parámetros
- `lineownerId` [path] (string) (**requerido**): Unique identifier for the secondary line owner (applicable only for Virtual Lines).

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/settings/secondaryLines/<lineownerId>/availableCallerIds' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `availableCallerIds` (array) (**requerido**): A List of available caller IDs.
  - `type` (string) (**requerido**): * `DEFAULT_CLID` - Caller ID is the default configured caller ID.  * `ADDITIONAL_CLID` - Caller ID is an additional external caller ID phone number available for the user.  * `CALL_QUEUE` - Caller ID is associated with a call queue.  * `HUNT_GROUP` - Caller ID is associated with a hunt group. Valores: DEFAULT_CLID, ADDITIONAL_CLID, CALL_QUEUE, HUNT_GROUP.
  - `id` (string): Unique identifier of the available caller ID.
  - `name` (string) (**requerido**): Name of the available caller ID.
  - `directNumber` (string): Direct number of the available caller ID.
  - `extension` (string): Extension of the available caller ID.

### Ejemplo — respuesta 200
```json
{
  "availableCallerIds": [
    {
      "type": "HUNT_GROUP",
      "id": "Y2lzY29zcGFyazovL3VzL0hVTlRfR1JPVVAvNmU1NTVjZDAtNjM0MS00MmI4LWEyMWMtZTc1ZjIxNDQ4Mjc5",
      "name": "Hunt Group",
      "directNumber": "+19075552860",
      "extension": "10079"
    }
  ]
}
```
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