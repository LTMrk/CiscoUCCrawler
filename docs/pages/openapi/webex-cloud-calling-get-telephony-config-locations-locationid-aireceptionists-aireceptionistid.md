---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-aireceptionists-aireceptionistid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/aiReceptionists/{aiReceptionistId}
operation_id: getAiReceptionist
tags: AI Receptionist for Webex Calling, AI Receptionist
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.552927+00:00
---

# GET /telephony/config/locations/{locationId}/aiReceptionists/{aiReceptionistId}

**API:** Webex Cloud Calling
**Área:** AI Receptionist for Webex Calling, AI Receptionist
**operationId:** `getAiReceptionist`

## Resumen
Get AI Receptionist Details

## Descripción
Get AI Receptionist details.

AI Receptionist is a Webex Calling feature that uses AI to greet callers and intelligently route calls to people or services.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location ID.
- `aiReceptionistId` [path] (string) (**requerido**): Unique identifier for the AI Receptionist.
- `orgId` [query] (string): Optional target organization identifier. Defaults to token's organization if not provided.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/aiReceptionists/<aiReceptionistId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): AI Receptionist ID encoded using the Resource Type.
- `name` (string) (**requerido**): Name of the AI Receptionist. This has to be unique across location
- `enabled` (boolean) (**requerido**): Flag to indicate AI receptionist is enabled or not. When disabled, incoming calls to this AI receptionist will not be answered.
- `phoneNumber` (string): Phone number of the AI Receptionist. Either phoneNumber or extension is mandatory. At least one is required.
- `extension` (string): Extension of the AI Receptionist. Either phoneNumber or extension is mandatory. At least one is required.
- `routingPrefix` (string): Routing prefix of location.
- `esn` (string): Routing prefix + extension of the AI Receptionist. If the location has no routing prefix, this will only be the extension. If the AI Receptionist has no extension, this field will not be present.
- `alternateNumbers` (array): List of alternate phone numbers assigned to the AI Receptionist.
  - `phoneNumber` (string): Alternate phone number. Long. max: 23.
  - `tollFreeNumber` (boolean): Flag to indicate if the number is toll free number
  - `ringPattern` (string): Ring pattern for the alternate number:  - `NORMAL` - Standard ring pattern. - `LONG_LONG` - Two long rings. - `SHORT_SHORT_LONG` - Two short rings followed by one long ring. - `SHORT_LONG_SHORT` - Short, long, short ring pattern. Valores: NORMAL, LONG_LONG, SHORT_SHORT_LONG, SHORT_LONG_SHORT.
- `directLineCallerIdName` (object): Direct line caller ID name configuration
- `dialByName` (string): A dial by name used for AI Receptionist name dialing. Characters of `%`, `+`, `\`, `"` and Unicode characters are not allowed.
- `defaultAction` (object): Default action configuration for the AI Receptionist
- `aiAgent` (object): AI Agent configuration
- `intentCount` (integer) (**requerido**): Number of intents configured for this AI Receptionist

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0FJX1JFQ0VQVElPTklTVC82MDEyNGU1MC03MWNkLTQ2N2QtODkzZS1mMGY5MDc0YWYyYjc",
  "name": "Shine Healthcare Clinic",
  "enabled": true,
  "phoneNumber": "+13504342182",
  "extension": "2182",
  "routingPrefix": "2345",
  "esn": "23452182",
  "alternateNumbers": [
    {
      "phoneNumber": "+12147691003",
      "tollFreeNumber": false,
      "ringPattern": "LONG_LONG"
    }
  ],
  "directLineCallerIdName": {
    "directLineCallerIdNameSelection": "CUSTOM_NAME",
    "customName": "Shine Clinic"
  },
  "dialByName": "Shine Healthcare",
  "defaultAction": {
    "actionType": "PLAY_MESSAGE_AND_DISCONNECT",
    "audioMessageSelection": "CUSTOM",
    "audioFile": {
      "id": "Y2lzY29zcGFyazovL3VzL0FVRElPX0ZJTEUvYTJiM2M0NTYtNzg5MC0xMjM0LTU2NzgtOTBhYmNkZWYxMjM0",
      "fileName": "greeting.wav",
      "mediaFileType": "WAV",
      "level": "ORGANIZATION",
      "isTextToSpeech": false
    }
  },
  "aiAgent": {
    "agentId": "Y2lzY29zcGFyazovL3VzL0FJX0FHRU5ULzY4ZWFlMjI0NDc0NmJkMmUyMmJkZjY4Ng",
    "voice": {
      "aiEngine": "PRO",
      "displayName": "en-US-AvaMultilingualNeural",
      "language": "English",
      "languageCode": "en-US"
    },
    "knowledgeBaseId": "Y2lzY29zcGFyazovL3VzL0tOT1dMRURHRV9CQVNFL2IzYzRkNTY3LTg5MDEtMjM0NS02Nzg5LTAxYmNkZWYyMzQ1Ng",
    "guidelines": {
      "goal": "Assist callers with appointment scheduling",
      "welcomeMessage": "Welcome to Shine Healthcare Clinic",
      "guideline": "Be polite and professional"
    },
  ... (truncado)
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