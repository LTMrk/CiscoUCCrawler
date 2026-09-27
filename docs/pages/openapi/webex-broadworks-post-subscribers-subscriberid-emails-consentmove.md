---
doc_id: webex-broadworks-post-subscribers-subscriberid-emails-consentmove
source: webex-openapi-specs/public-spec/webex-broadworks.json
api: Webex Broadworks Calling
api_version: 1.0.0
method: POST
path: /subscribers/{subscriberId}/emails/consentMove
operation_id: Send Consent User Move Email to Pending Broadworks Subscribers
tags: BroadWorks Subscribers
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-27T10:51:18.914081+00:00
---

# POST /subscribers/{subscriberId}/emails/consentMove

**API:** Webex Broadworks Calling
**Área:** BroadWorks Subscribers
**operationId:** `Send Consent User Move Email to Pending Broadworks Subscribers`

## Resumen
Send Consent User Move Email to Pending Broadworks Subscribers

## Descripción
Allows a Service Provider to send the user consent move email to a subscriber who is currently in `pending_user_migration` state.

## Parámetros
- `subscriberId` [path] (string) (**requerido**): A unique identifier for the subscriber in question.

## Ejemplo de invocación
```bash
curl -X POST '/subscribers/<subscriberId>/emails/consentMove' \
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
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

## Contexto de la API
The Webex BroadWorks Calling APIs provide access to advanced calling features and user management for BroadWorks-powered Webex Calling deployments. These APIs support provisioning of users and devices, call control, feature management, device inventory, and detailed reporting. Service providers and enterprises can automate onboarding, integrate with OSS/BSS systems, manage user entitlements, and monitor call quality. The APIs are designed for scalable, multi-tenant environments and support seamless integration with existing telephony infrastructure.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs