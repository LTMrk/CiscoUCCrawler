---
doc_id: webex-cloud-calling-put-telephony-config-virtuallines-virtuallineid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/virtualLines/{virtualLineId}
operation_id: Update a Virtual Line
tags: Virtual Line Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.355944+00:00
---

# PUT /telephony/config/virtualLines/{virtualLineId}

**API:** Webex Cloud Calling
**Área:** Virtual Line Call Settings
**operationId:** `Update a Virtual Line`

## Resumen
Update a Virtual Line

## Descripción
Update the designated Virtual Line.

Virtual line is a capability in Webex Calling that allows administrators to configure multiple lines to Webex Calling users.

Updating a virtual line requires a full, user, or location administrator auth token with a scope of `spark-admin:telephony_config_write` and `identity:contacts_rw`.

## Parámetros
- `virtualLineId` [path] (string) (**requerido**): Update settings for a virtual line with the matching ID.
- `orgId` [query] (string): Update virtual line settings from this organization.

## Cuerpo de la petición (application/json)
- `firstName` (string): First name defined for a virtual line. Minimum length is 1. Maximum length is 64.
- `lastName` (string): Last name defined for a virtual line. Minimum length is 1. Maximum length is 64.
- `displayName` (string): Display name defined for a virtual line.
- `phoneNumber` (string): Phone number of a virtual line. Minimum length is 1. Maximum length is 23. Either `phoneNumber` or `extension` is mandatory.
- `extension` (string): Extension of a virtual line. Minimum length is 2. Maximum length is 10. Either `phoneNumber` or `extension` is mandatory.
- `announcementLanguage` (string): Virtual Line's announcement language.
- `callerIdLastName` (string): Last name used in the Calling Line ID and for dial-by-name functions. Minimum length is 1. Maximum length is 64.
- `callerIdFirstName` (string): First name used in the Calling Line ID and for dial-by-name functions. Minimum length is 1. Maximum length is 128.
- `callerIdNumber` (string): Phone number to appear as the CLID for all calls. Minimum length is 1. Maximum length is 23.
- `timeZone` (string): Time zone defined for the virtual line.

### Ejemplo — petición
```json
{
  "firstName": "Bob",
  "lastName": "Smith",
  "displayName": "Bob Smith",
  "phoneNumber": "+15558675309",
  "extension": "5309",
  "announcementLanguage": "French",
  "callerIdFirstName": "Bob",
  "callerIdLastName": "Smith",
  "callerIdNumber": "+15558675309",
  "timeZone": "Africa/Algiers"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/virtualLines/<virtualLineId>' \
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