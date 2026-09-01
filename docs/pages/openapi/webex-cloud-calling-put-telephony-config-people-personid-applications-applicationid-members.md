---
doc_id: webex-cloud-calling-put-telephony-config-people-personid-applications-applicationid-members
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/people/{personId}/applications/{applicationId}/members
operation_id: modifySharedLineAppearanceMembers
tags: User Call Settings (2/2)
deprecated: true
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.764992+00:00
---

# PUT /telephony/config/people/{personId}/applications/{applicationId}/members

> **ENDPOINT DEPRECADO.** No usar en integraciones nuevas.

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `modifySharedLineAppearanceMembers`

## Resumen
Put Shared-Line Appearance Members

## Descripción
Add or modify primary and secondary users assigned to shared-lines on a Webex Calling Apps Desktop device.

This API requires a full or user administrator or location administrator auth token with the `spark-admin:people_write` scope.

## Parámetros
- `personId` [path] (string) (**requerido**): A unique identifier for the person.
- `applicationId` [path] (string) (**requerido**): A unique identifier for the application.

## Cuerpo de la petición (application/json)
- `members` (array):
  - `id` (string) (**requerido**): Unique identifier for the person or workspace.
  - `port` (number) (**requerido**): Device port number assigned to person or workspace.
  - `t38FaxCompressionEnabled `true`` (boolean): T.38 Fax Compression setting. Valid only for ATA Devices. Overrides user level compression options.
  - `primaryOwner` (string) (**requerido**): If `true` the person or the workspace is the owner of the device. Points to primary line/port of the device.
  - `lineType` (string) (**requerido**): * `PRIMARY` - Primary line for the member.  * `SHARED_CALL_APPEARANCE` - Shared line for the member. A shared line allows users to receive and place calls to and from another user's extension, using their own device. Valores: PRIMARY, SHARED_CALL_APPEARANCE.
  - `lineWeight` (number) (**requerido**): Number of lines that have been configured for the person on the device.
  - `hotlineEnabled` (boolean) (**requerido**): Configure this line to automatically call a predefined number whenever taken off-hook. Once enabled, the line can only make calls to the predefined number set in `hotlineDestination`.
  - `hotlineDestination` (string) (**requerido**): Preconfigured number for the hotline. Required only if `hotlineEnabled` is set to `true`.
  - `allowCallDeclineEnabled` (boolean) (**requerido**): Set how a device behaves when a call is declined. When set to `true`, a call decline request is extended to all the endpoints on the device. When set to `false`, a call decline request is only declined at the current endpoint.
  - `lineLabel` (string): Device line label.

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/people/<personId>/applications/<applicationId>/members' \
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