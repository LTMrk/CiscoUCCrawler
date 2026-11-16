---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-autoattendants-autoattendantid-callforwarding
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/autoAttendants/{autoAttendantId}/callForwarding
operation_id: updateAutoAttendantCallForwardingSettings
tags: Features:  Auto Attendant
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:50.664904+00:00
---

# PUT /telephony/config/locations/{locationId}/autoAttendants/{autoAttendantId}/callForwarding

**API:** Webex Cloud Calling
**Área:** Features:  Auto Attendant
**operationId:** `updateAutoAttendantCallForwardingSettings`

## Resumen
Update Call Forwarding Settings for an Auto Attendant

## Descripción
Update Call Forwarding settings for the designated Auto Attendant.

The call forwarding feature allows you to direct all incoming calls based on specific criteria that you define.
Below are the available options for configuring your call forwarding:
1. Always forward calls to a designated number.
2. Forward calls to a designated number based on certain criteria.
3. Forward calls using different modes.

Updating call forwarding settings for an auto attendant requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location in which this auto attendant exists.
- `autoAttendantId` [path] (string) (**requerido**): Update call forwarding settings for this auto attendant.
- `orgId` [query] (string): Update auto attendant forwarding settings from this organization.

## Cuerpo de la petición (application/json)
- `callForwarding` (object) (**requerido**): Settings related to `Always`, `Busy`, and `No Answer` call forwarding.

### Ejemplo — petición
```json
{
  "callForwarding": {
    "always": {
      "enabled": false,
      "destination": "+19705550006",
      "ringReminderEnabled": false,
      "sendToVoicemailEnabled": false
    },
    "selective": {
      "enabled": true,
      "destination": "+19705550006",
      "ringReminderEnabled": false,
      "sendToVoicemailEnabled": false
    },
    "rules": [
      {
        "id": "Y2lzY29zcGFyazovL3VzL0NBTExfRk9SV0FSRElOR19TRUxFQ1RJVkVfUlVMRS9WR1Z6ZENCU2RXeGw",
        "enabled": false
      }
    ],
    "operatingModes": {
      "enabled": true,
      "modes": [
        {
          "normalOperationEnabled": true,
          "id": "Y2lzY29zcGFyazovL3VzL09QRVJBVElOR19NT0RFL2JiOTc1OTcxLTBjZWYtNDdhNi05Yzc5LTliZWFjY2IwYjg4Mg",
          "forwardTo": {
            "selection": "FORWARD_TO_SPECIFIED_NUMBER",
            "destination": "00000",
            "destinationVoicemailEnabled": false
          }
        }
      ]
    }
  }
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>/autoAttendants/<autoAttendantId>/callForwarding' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"callForwarding": "<callForwarding>"}'
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