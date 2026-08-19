---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-intercept
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/intercept
operation_id: Get Location Intercept
tags: Location Call Settings: Call Handling
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.120388+00:00
---

# GET /telephony/config/locations/{locationId}/intercept

**API:** Webex Cloud Calling
**Área:** Location Call Settings: Call Handling
**operationId:** `Get Location Intercept`

## Resumen
Get Location Intercept

## Descripción
Retrieve intercept location details for a customer location.

Intercept incoming or outgoing calls for persons in your organization. If this is enabled, calls are either routed to a designated number the person chooses, or to the person's voicemail.

Retrieving intercept location details requires a full, user or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieve intercept details for this location.
- `orgId` [query] (string): Retrieve intercept location details for a customer location.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/intercept' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `enabled` (boolean) (**requerido**): Enable/disable location intercept. Enable this feature to override any Location's Call Intercept settings that person configures.
- `incoming` (object): Inbound call details.
  - `type` (string): Select inbound call options.  * `INTERCEPT_ALL` - Intercept all inbound calls.  * `ALLOW_ALL` - Allow all inbound calls. Valores: INTERCEPT_ALL, ALLOW_ALL.
  - `voicemailEnabled` (boolean): Enable/disable to route voice mail.
  - `announcements` (object): Announcements details.
    - `greeting` (string): Greeting type for location intercept.  * `DEFAULT` - Play default greeting.  * `CUSTOM` - Play custom greeting. Valores: DEFAULT, CUSTOM.
    - `fileName` (string): If set to `CUSTOM` for greeting, filename of previously uploaded file.
    - `newNumber` (object): Settings for new number announcement.
      - `enabled` (boolean): Enable/disable to play new number announcement.
      - `destination` (string): Incoming destination phone number to be announced.
    - `zeroTransfer` (object): Transfer number details.
      - `enabled` (boolean): Enable/disable to transfer to phone number.
      - `destination` (string): Transfer phone number to be called when '0' is dialed.
- `outgoing` (object): Outbound Call details
  - `type` (string): Outbound call modes  * `INTERCEPT_ALL` - Intercept all outbound calls.  * `ALLOW_LOCAL_ONLY` - Allow local outbound calls. Valores: INTERCEPT_ALL, ALLOW_LOCAL_ONLY.
  - `transferEnabled` (boolean): If `true`, allows transfer and forwarding for the call type.
  - `destination` (string): If enabled, set outgoing destination phone number.

### Ejemplo — respuesta 200
```json
{
  "enabled": true,
  "incoming": {
    "type": "INTERCEPT_ALL",
    "voicemailEnabled": false,
    "announcements": {
      "greeting": "DEFAULT",
      "fileName": "audiofile.wav",
      "newNumber": {
        "enabled": true,
        "destination": "2147691003"
      },
      "zeroTransfer": {
        "enabled": true,
        "destination": "2147691005"
      }
    }
  },
  "outgoing": {
    "type": "ALLOW_LOCAL_ONLY",
    "transferEnabled": true,
    "destination": "2147691007"
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