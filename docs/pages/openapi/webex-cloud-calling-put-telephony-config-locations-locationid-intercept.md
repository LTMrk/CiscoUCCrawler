---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-intercept
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/intercept
operation_id: Put Location Intercept
tags: Location Call Settings: Call Handling
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.729990+00:00
---

# PUT /telephony/config/locations/{locationId}/intercept

**API:** Webex Cloud Calling
**Área:** Location Call Settings: Call Handling
**operationId:** `Put Location Intercept`

## Resumen
Put Location Intercept

## Descripción
Modifies the intercept location details for a customer location.

Intercept incoming or outgoing calls for users in your organization. If this is enabled, calls are either routed to a designated number the user chooses, or to the user's voicemail.

Modifying the intercept location details requires a full, user administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Modifies the intercept details for this location.
- `orgId` [query] (string): Modifies the intercept location details for a customer location.

## Cuerpo de la petición (application/json)
- `enabled` (boolean) (**requerido**): Enable/disable location intercept. Enable this feature to override any location's Call Intercept settings that a person configures.
- `incoming` (object): Inbound call details.
  - `type` (string): Select inbound call options.  * `INTERCEPT_ALL` - Set to `INTERCEPT_ALL` to intercept all inbound calls.  * `ALLOW_ALL` - Set to `ALLOW_ALL` to allow all inbound calls. Valores: INTERCEPT_ALL, ALLOW_ALL.
  - `voicemailEnabled` (boolean): Set to `true` to route voice mail.
  - `announcements` (object): Announcements details.
    - `greeting` (string): Greeting type for location intercept.  * `DEFAULT` - Set to `DEFAULT` to play default greeting.  * `CUSTOM` - Set to `CUSTOM` to play custom greeting. Valores: DEFAULT, CUSTOM.
    - `fileName` (string): If set to `CUSTOM` for greeting, filename of previously uploaded file.
    - `newNumber` (object): Details for new number.
      - `enabled` (boolean): Set to `true` to play new number announcement.
      - `destination` (string): If enabled, set destination phone number.
    - `zeroTransfer` (object): Transfer number details.
      - `enabled` (boolean): Set to `true` to transfer to phone number.
      - `destination` (string): Transfer phone number to be called when '0' is dialed.
- `outgoing` (object): Outbound Call details
  - `type` (string): Outbound call options.  * `INTERCEPT_ALL` - Set to `INTERCEPT_ALL` to intercept all outbound calls.  * `ALLOW_LOCAL_ONLY` - Set to `ALLOW_LOCAL_ONLY` to allow local outbound calls. Valores: INTERCEPT_ALL, ALLOW_LOCAL_ONLY.
  - `transferEnabled` (boolean): If `true`, allows transfer and forwarding for the call type.
  - `destination` (string): If enabled, set valid outgoing destination phone number.

### Ejemplo — petición
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

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>/intercept' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"enabled": true}'
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