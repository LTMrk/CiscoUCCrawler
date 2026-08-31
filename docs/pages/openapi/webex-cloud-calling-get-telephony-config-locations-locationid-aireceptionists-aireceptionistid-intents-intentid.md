---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-aireceptionists-aireceptionistid-intents-intentid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/aiReceptionists/{aiReceptionistId}/intents/{intentId}
operation_id: getAiReceptionistIntent
tags: AI Receptionist for Webex Calling, AI Receptionist
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.123016+00:00
---

# GET /telephony/config/locations/{locationId}/aiReceptionists/{aiReceptionistId}/intents/{intentId}

**API:** Webex Cloud Calling
**Área:** AI Receptionist for Webex Calling, AI Receptionist
**operationId:** `getAiReceptionistIntent`

## Resumen
Get AI Receptionist Intent

## Descripción
Get details of a specific AI Receptionist Intent.

AI Receptionist is a Webex Calling feature that uses AI to greet callers and intelligently route calls. Intents represent call-handling behaviors such as transfers.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location ID.
- `aiReceptionistId` [path] (string) (**requerido**): Unique identifier for the AI Receptionist.
- `intentId` [path] (string) (**requerido**): Unique identifier for a specific AI Receptionist intent within a given location and AI Receptionist instance.
- `orgId` [query] (string): Optional target organization identifier. Defaults to token's organization if not provided.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/aiReceptionists/<aiReceptionistId>/intents/<intentId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Unique identifier for a specific AI Receptionist intent within a given location and AI Receptionist instance.
- `name` (string) (**requerido**): Name of the intent.
- `description` (string) (**requerido**): Description of the intent (Action).
- `transferTo` (object) (**requerido**): Transfer destination details for the intent.
  - `contactType` (string) (**requerido**): Contact type. - PEOPLE - A person in the organization. - RESOURCE_GROUP - A group resource such as a call queue or hunt group. - CONTACT - An organization contact. - PHONE_NUMBER - A raw phone number or extension. Valores: PEOPLE, RESOURCE_GROUP, CONTACT, PHONE_NUMBER.
  - `contactId` (string): Unique identifier for the transfer destination, encoded using the resource type indicated by contactType (PEOPLE, RESOURCE_GROUP, or CONTACT). Not required when contactType is PHONE_NUMBER.
  - `name` (string): Name of the calling service or contact.
  - `phoneNumber` (string): Phone number of calling service or contact.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0lOVEVOVC82OGVhZTIyNDQ3NDZiZDJlMjJiZGY2ODY",
  "name": "Physical Therapy",
  "description": "Connect the caller to knowledgeable representative if they seek assistance with Physical Therapy",
  "transferTo": {
    "contactType": "PEOPLE",
    "contactId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNDFjZDA1MS04MTdmLTRkODEtYTFjZS0wZmQzOWMxZTdiOWY",
    "name": "John Doe",
    "phoneNumber": "+4765241628"
  }
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