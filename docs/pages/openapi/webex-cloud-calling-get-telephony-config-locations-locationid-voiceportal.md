---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-voiceportal
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/voicePortal
operation_id: Get VoicePortal
tags: Location Call Settings:  Voicemail
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.735464+00:00
---

# GET /telephony/config/locations/{locationId}/voicePortal

**API:** Webex Cloud Calling
**Área:** Location Call Settings:  Voicemail
**operationId:** `Get VoicePortal`

## Resumen
Get VoicePortal

## Descripción
Retrieve Voice portal information for the location.

Voice portals provide an interactive voice response (IVR)
system so administrators can manage auto attendant announcements.

Retrieving voice portal information for an organization requires a full read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location to which the voice portal belongs.
- `orgId` [query] (string): Organization to which the voice portal belongs.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/voicePortal' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string): Voice Portal ID
- `name` (string): Voice Portal Name.
- `language` (string): Language for audio announcements.
- `languageCode` (string): Language code for voicemail group audio announcement.
- `extension` (string): Extension of incoming call.
- `phoneNumber` (string): Phone Number of incoming call.
- `firstName` (string): Caller ID First Name. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `lastName` (string): Caller ID Last Name. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `directLineCallerIdName` (object): Settings for the direct line caller ID name to be shown for this workspace.
  - `selection` (string): * `DISPLAY_NAME` - When this option is selected, `displayName` is to be shown for this workspace.  * `CUSTOM_NAME` - When this option is selected, `customName` is to be shown for this workspace. Valores: CUSTOM_NAME, DISPLAY_NAME.
  - `customName` (string): The custom direct line caller ID name. Required if `selection` is set to `CUSTOM_NAME`.
- `dialByName` (string): The name to be used for dial by name functions.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1ZPSUNFTUFJTF9HUk9VUC8yZmQzZGMwMy0yZWRhLTQ4NmUtODdhYS0xODY1ZDI5YWExZWI",
  "name": "test voicePortal",
  "language": "English",
  "languageCode": "en_us",
  "extension": "0007",
  "phoneNumber": "+1345325235",
  "firstName": "firstName",
  "lastName": "lastName",
  "directLineCallerIdName": {
    "selection": "CUSTOM_NAME",
    "customName": "Hakim Smith"
  },
  "dialByName": "Hakim Smith"
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