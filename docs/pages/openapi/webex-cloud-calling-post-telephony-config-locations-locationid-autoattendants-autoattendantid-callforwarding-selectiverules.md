---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-autoattendants-autoattendantid-callforwarding-selectiverules
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/locations/{locationId}/autoAttendants/{autoAttendantId}/callForwarding/selectiveRules
operation_id: createAutoAttendantSelectiveCallForwardingRule
tags: Features:  Auto Attendant
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T14:22:47.294457+00:00
---

# POST /telephony/config/locations/{locationId}/autoAttendants/{autoAttendantId}/callForwarding/selectiveRules

**API:** Webex Cloud Calling
**Área:** Features:  Auto Attendant
**operationId:** `createAutoAttendantSelectiveCallForwardingRule`

## Resumen
Create a Selective Call Forwarding Rule for an Auto Attendant

## Descripción
Create a Selective Call Forwarding Rule for the designated Auto Attendant.

A selective call forwarding rule for an auto attendant allows calls to be forwarded or not forwarded to the designated number, based on the defined criteria.

Note that the list of existing call forward rules is available in the auto attendant's call forwarding settings.

Creating a selective call forwarding rule for an auto attendant requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

**NOTE**: The Call Forwarding Rule ID will change upon modification of the Call Forwarding Rule name.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location in which the auto attendant exists.
- `autoAttendantId` [path] (string) (**requerido**): Create the rule for this auto attendant.
- `orgId` [query] (string): Create the auto attendant rule for this organization.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Unique name for the selective rule in the auto attendant.
- `enabled` (boolean): Reflects if rule is enabled.
- `businessSchedule` (string): Name of the business schedule which determines when this selective call forwarding rule is in effect.
- `businessScheduleLevel` (string): Level of the business schedule named by `businessSchedule`. Defaults to `LOCATION` when omitted. A non-blank `businessSchedule` is required when this field is set.  * `LOCATION` - The schedule is a location schedule.  * `ORGANIZATION` - The schedule is an organization schedule. Valores: LOCATION, ORGANIZATION.
- `holidaySchedule` (string): Name of the holiday schedule which determines when this selective call forwarding rule is in effect.
- `holidayScheduleLevel` (string): Level of the holiday schedule named by `holidaySchedule`. Defaults to `LOCATION` when omitted. A non-blank `holidaySchedule` is required when this field is set.  * `LOCATION` - The schedule is a location schedule.  * `ORGANIZATION` - The schedule is an organization schedule. Valores: LOCATION, ORGANIZATION.
- `forwardTo` (object) (**requerido**): Controls what happens when the rule matches including the destination number for the call forwarding.
- `callsFrom` (object) (**requerido**): Settings related to the rule matching based on incoming caller ID.
- `callsTo` (object): Settings related to the rule matching based on the destination number.

### Ejemplo — petición
```json
{
  "name": "Test Rule",
  "businessSchedule": "AUTOATTENDANT-BUSINESS-HOURS",
  "holidaySchedule": "AUTOATTENDANT-HOLIDAY",
  "callsFrom": {
    "selection": "CUSTOM",
    "customNumbers": {
      "privateNumberEnabled": true,
      "unavailableNumberEnabled": false,
      "numbers": [
        "4554"
      ]
    }
  },
  "callsTo": {
    "numbers": [
      {
        "type": "PRIMARY",
        "phoneNumber": "+19705550026"
      }
    ]
  },
  "forwardTo": {
    "selection": "FORWARD_TO_DEFAULT_NUMBER"
  },
  "enabled": true
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations/<locationId>/autoAttendants/<autoAttendantId>/callForwarding/selectiveRules' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "forwardTo": "<forwardTo>", "callsFrom": "<callsFrom>"}'
```

## Respuestas correctas
**201**: Created
- `id` (string) (**requerido**): ID of the newly created auto attendant call forward selective rule.

### Ejemplo — respuesta 201
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0NBTExfRk9SV0FSRElOR19TRUxFQ1RJVkVfUlVMRS9WR1Z6ZENCU2RXeGw"
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