---
doc_id: webex-cloud-calling-post-telephony-config-aireceptionists-actions-validatecountry-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/aiReceptionists/actions/validateCountry/invoke
operation_id: validateAiReceptionistCountry
tags: AI Receptionist for Webex Calling, AI Receptionist
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.933851+00:00
---

# POST /telephony/config/aiReceptionists/actions/validateCountry/invoke

**API:** Webex Cloud Calling
**Área:** AI Receptionist for Webex Calling, AI Receptionist
**operationId:** `validateAiReceptionistCountry`

## Resumen
Validate Country for AI Receptionist

## Descripción
Validates if country passed in the request supports AI Receptionist.

AI Receptionist is a Webex Calling feature that uses AI to greet callers and intelligently route calls.

This API requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Optional; target organization ID, otherwise defaults to token's org.

## Cuerpo de la petición (application/json)
- `countryCode` (string) (**requerido**): Two letter country code of the location for which AI Receptionist needs to be validated.
- `locationId` (string): Location associated with the AI Receptionist.

### Ejemplo — petición
```json
{
  "countryCode": "US",
  "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzEyMzQ1"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/aiReceptionists/actions/validateCountry/invoke' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"countryCode": "<countryCode>"}'
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