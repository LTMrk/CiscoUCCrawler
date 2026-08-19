---
doc_id: webex-cloud-calling-get-telephony-config-servicesettings-callerreputationprovider-providers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/serviceSettings/callerReputationProvider/providers
operation_id: getCallerReputationProviderProviders
tags: Caller Reputation Provider
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.188349+00:00
---

# GET /telephony/config/serviceSettings/callerReputationProvider/providers

**API:** Webex Cloud Calling
**Área:** Caller Reputation Provider
**operationId:** `getCallerReputationProviderProviders`

## Resumen
Get Caller Reputation Provider Providers

## Descripción
Retrieves the list of available caller reputation providers and their regions for Webex Calling.

## Parámetros
- `organizationId` [query] (string): Unique identifier for the organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/serviceSettings/callerReputationProvider/providers' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Successful response with list of caller reputation providers.
- `providers` (array): List of caller reputation providers.
  - `id` (string): Unique identifier for the provider.
  - `enabled` (boolean): Indicates if the provider is enabled.
  - `name` (string): Name of the provider.
  - `regions` (array): List of regions for the provider.
    - `id` (string): Unique identifier for the region.
    - `name` (string): Name of the region.
    - `type` (string): Type of the region (e.g., primary, secondary).
    - `visible` (boolean): Indicates if the region is visible.
    - `environmentType` (string): Environment type of the region (e.g., production, staging).

### Ejemplo — respuesta 200
```json
{
  "providers": [
    {
      "id": "provider-123",
      "enabled": true,
      "name": "Acme Reputation Provider",
      "regions": [
        {
          "id": "region-1",
          "name": "US East",
          "type": "primary",
          "visible": true,
          "environmentType": "production"
        }
      ]
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