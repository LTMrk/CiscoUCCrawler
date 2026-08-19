---
doc_id: webex-cloud-calling-put-telephony-config-virtuallines-virtuallineid-intercept
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/virtualLines/{virtualLineId}/intercept
operation_id: Configure Call Intercept Settings for a Virtual Line
tags: Virtual Line Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.180544+00:00
---

# PUT /telephony/config/virtualLines/{virtualLineId}/intercept

**API:** Webex Cloud Calling
**Área:** Virtual Line Call Settings
**operationId:** `Configure Call Intercept Settings for a Virtual Line`

## Resumen
Configure Call Intercept Settings for a Virtual Line

## Descripción
Configures a virtual line's Call Intercept settings.

The intercept feature gracefully takes a virtual line's phone out of service, while providing callers with informative announcements and alternative routing options. Depending on the service configuration, none, some, or all incoming calls to the specified virtual line are intercepted. Also depending on the service configuration, outgoing calls are intercepted or rerouted to another location.

Updating the intercept settings for a virtual line requires a full, user, or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `virtualLineId` [path] (string) (**requerido**): Update settings for a virtual line with the matching ID.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Cuerpo de la petición (application/json)
- `enabled` (boolean): `true` if the intercept feature is enabled.
- `incoming` (object): Settings related to how incoming calls are handled when the intercept feature is enabled.
  - `type` (string): `INTERCEPT_ALL` indicated incoming calls are intercepted.  * `INTERCEPT_ALL` - Incoming calls are routed as the destination and voicemail specify.  * `ALLOW_ALL` - Incoming calls are not intercepted. Valores: INTERCEPT_ALL, ALLOW_ALL.
  - `voicemailEnabled` (boolean): If `true`, the destination will be the virtual line's voicemail.
  - `announcements` (object): Settings related to how incoming calls are handled when the intercept feature is enabled.
    - `greeting` (string): `DEFAULT` indicates that a system default message will be placed when incoming calls are intercepted.  * `CUSTOM` - A custom greeting is played when incoming calls are intercepted.  * `DEFAULT` - A System default greeting is played when incoming calls are intercepted. Valores: CUSTOM, DEFAULT.
    - `newNumber` (object): Information about the new number announcement.
      - `enabled` (boolean): If `true`, the caller will hear this new number when a call is intercepted.
      - `destination` (string): New number caller will hear announced.
    - `zeroTransfer` (object): Information about how call will be handled if zero (0) is pressed.
      - `enabled` (boolean): If `true`, the caller will be transferred to destination of when zero (0) is pressed.
      - `destination` (string): Destination to which caller will be transferred when zero is pressed.
- `outgoing` (object): Settings related to how outgoing calls are handled when the intercept feature is enabled.
  - `type` (string): `INTERCEPT_ALL` indicated all outgoing calls are intercepted.  * `INTERCEPT_ALL` - Outgoing calls are routed as the destination and voicemail specify.  * `ALLOW_LOCAL_ONLY` - Only non-local calls are intercepted. Valores: INTERCEPT_ALL, ALLOW_LOCAL_ONLY.
  - `transferEnabled` (boolean): If `true`, allows transfer and forwarding for the call type.
  - `destination` (string): Number to which the outbound call will be transferred.

### Ejemplo — petición
```json
{
  "enabled": true,
  "incoming": {
    "type": "INTERCEPT_ALL",
    "voicemailEnabled": false,
    "announcements": {
      "greeting": "DEFAULT",
      "fileName": "",
      "newNumber": {
        "enabled": false,
        "destination": ""
      },
      "zeroTransfer": {
        "enabled": false,
        "destination": ""
      }
    }
  },
  "outgoing": {
    "transferEnabled": false,
    "type": "INTERCEPT_ALL",
    "destination": ""
  }
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/virtualLines/<virtualLineId>/intercept' \
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