---
doc_id: webex-cloud-calling-post-telephony-config-redsky-actions-login-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/redSky/actions/login/invoke
operation_id: Login to a RedSky Admin Account
tags: Emergency Services Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.277792+00:00
---

# POST /telephony/config/redSky/actions/login/invoke

**API:** Webex Cloud Calling
**Área:** Emergency Services Settings
**operationId:** `Login to a RedSky Admin Account`

## Resumen
Login to a RedSky Admin Account

## Descripción
Login to Redsky for an existing account admin user to retrieve the `companyId` and verify the status of `externalTenantEnabled`. The password provided will not be stored.

The enhanced emergency (E911) service for Webex Calling provides an emergency service designed for organizations with a hybrid or nomadic workforce. It provides dynamic location support and a network that routes emergency calls to Public Safety Answering Points (PSAP) around the US, its territories, and Canada.

Logging in requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Login to a RedSky account for the organization.

## Cuerpo de la petición (application/json)
- `email` (string) (**requerido**): Email for the RedSky account.
- `password` (string) (**requerido**): Password for the RedSky account.
- `redSkyOrgId` (string): The RedSky organization ID for the organization which can be found in the RedSky portal.

### Ejemplo — petición
```json
{
  "email": "test@cisco.com",
  "password": "Test@123",
  "redSkyOrgId": "610af8f4-a4ed-4be3-ae6f-efcdcd4895a8"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/redSky/actions/login/invoke' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"email": "<email>", "password": "<password>"}'
```

## Respuestas correctas
**200**: OK
- `accountMatch` (boolean) (**requerido**): `true` if the old `companyId` secret is matched with the new `companyId` secret.
- `externalTenantEnabled` (boolean) (**requerido**): `true` if the RedSky reseller customer is not under a Cisco account.
- `companyId` (string) (**requerido**): The RedSky held token from the secret response.

### Ejemplo — respuesta 200
```json
{
  "accountMatch": true,
  "externalTenantEnabled": true,
  "companyId": "ddd1424c-5b48-433d-9bab-061cdfb84c90"
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