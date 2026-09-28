---
doc_id: webex-cloud-calling-post-telephony-conference-members-memberid-silentmonitor
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/conference/members/{memberId}/silentMonitor
operation_id: silentMonitorByMemberId
tags: Conference Controls
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-28T16:31:32.503847+00:00
---

# POST /telephony/conference/members/{memberId}/silentMonitor

**API:** Webex Cloud Calling
**Área:** Conference Controls
**operationId:** `silentMonitorByMemberId`

## Resumen
Silent Monitor by Member ID

## Descripción
Transition the member's conference type to silent monitoring mode. This allows the supervisor to listen to the conference without being heard by the other participants.

## Parámetros
- `memberId` [path] (string) (**requerido**): Unique identifier for the member. Member ID can be one of the following: person, workspace, or virtual line
- `orgId` [query] (string): Id of the organization to which the member belongs. If not provided, the orgId of the Service App is used. If provided, the organization must be the same as or managed by the Service App's organization.

## Ejemplo de invocación
```bash
curl -X POST '/telephony/conference/members/<memberId>/silentMonitor' \
  -H 'Authorization: Bearer <TOKEN>'
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