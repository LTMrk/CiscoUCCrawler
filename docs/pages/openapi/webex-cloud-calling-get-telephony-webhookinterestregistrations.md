---
doc_id: webex-cloud-calling-get-telephony-webhookinterestregistrations
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/webhookInterestRegistrations
operation_id: getWebhookInterestRegistration
tags: Webhook Interest Registrations
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.370490+00:00
---

# GET /telephony/webhookInterestRegistrations

**API:** Webex Cloud Calling
**Área:** Webhook Interest Registrations
**operationId:** `getWebhookInterestRegistration`

## Resumen
Get Webhook Interest Registration

## Descripción
Returns the webhook interest registration associated with the authenticated user and the client derived from the access token, including the list of interests and the date/time at which the registration expires. The client identifier is not supplied by the caller.

Registrations are managed for a specific user and client, but registered interests apply to all applicable webhooks in the organization.

This API is reserved for administrators and requires the `spark-admin:calls_read` scope.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/webhookInterestRegistrations' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `interests` (array) (**requerido**): The collection of webhook interests associated with the registration. Each interest is either resource-based or actor-based. At least one interest is always present in a successful response.
  - `resource` (string): Resource-based interest. Set exactly one of `resource` or `actor` per interest entry.  - `Hook Status` - Enables webhook events for the `telephony_hookstatus` resource. - `Agent` - Enables webhook events for the `telephony_agent` resource. - `Services` - Enables webhook events for the `telephony_services` resource. - `Agent Monitoring` - Enables webhook events for the `telephony_agentMonitoring` resource. - `Queue` - Enables webhook events for the `telephony_queue` resource. - `Queue Monitoring` - Enables webhook events for the `telephony_queueMonitoring` resource. Valores: Hook Status, Agent, Services, Agent Monitoring, Queue, Queue Monitoring.
  - `actor` (string): Actor-based interest. Set exactly one of `resource` or `actor` per interest entry.  - `Workspaces` - Enables telephony webhook events associated with workspace actors. - `Virtual Lines` - Enables telephony webhook events associated with virtual line actors. Valores: Workspaces, Virtual Lines.
- `expiresAt` (string/date-time) (**requerido**): The date/time at which the registration expires.

### Ejemplo — respuesta 200
```json
{
  "interests": [
    {
      "resource": "Agent"
    },
    {
      "actor": "Workspaces"
    }
  ],
  "expiresAt": "2026-08-01T00:00:00.000Z"
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