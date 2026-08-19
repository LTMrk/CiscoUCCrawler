---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-queues-queueid-callforwarding-selectiverules
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/locations/{locationId}/queues/{queueId}/callForwarding/selectiveRules
operation_id: createCallQueueSelectiveCallForwardingRule
tags: Features:  Call Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.031052+00:00
---

# POST /telephony/config/locations/{locationId}/queues/{queueId}/callForwarding/selectiveRules

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `createCallQueueSelectiveCallForwardingRule`

## Resumen
Create a Selective Call Forwarding Rule for a Call Queue

## Descripción
Create a Selective Call Forwarding Rule for the designated Call Queue.

A selective call forwarding rule for a call queue allows calls to be forwarded or not forwarded to the designated number, based on the defined criteria.

Note that the list of existing call forward rules is available in the call queue's call forwarding settings.

Creating a selective call forwarding rule for a call queue requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

**NOTE**: The Call Forwarding Rule ID will change upon modification of the Call Forwarding Rule name.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location in which the call queue exists.
- `queueId` [path] (string) (**requerido**): Create the rule for this call queue.
- `orgId` [query] (string): Create the call queue rule for this organization.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Unique name for the selective rule in the hunt group.
- `enabled` (boolean): Reflects if rule is enabled.
- `holidaySchedule` (string): Name of the location's holiday schedule which determines when this selective call forwarding rule is in effect.
- `businessSchedule` (string): Name of the location's business schedule which determines when this selective call forwarding rule is in effect.
- `forwardTo` (object): Controls what happens when the rule matches including the destination number for the call forwarding.
  - `selection` (string) (**requerido**): Controls what happens when the rule matches.  * `FORWARD_TO_DEFAULT_NUMBER` - When the rule matches, forward to the destination for the hunt group.  * `FORWARD_TO_SPECIFIED_NUMBER` - When the rule matches, forward to the destination for this rule.  * `DO_NOT_FORWARD` - When the rule matches, do not forward to another number. Valores: FORWARD_TO_DEFAULT_NUMBER, FORWARD_TO_SPECIFIED_NUMBER, DO_NOT_FORWARD.
  - `phoneNumber` (string): Phone number to forward calls to. Required when selection is `FORWARD_TO_SPECIFIED_NUMBER`.
- `callsFrom` (object) (**requerido**): Settings related to the rule matching based on incoming caller ID.
  - `selection` (string) (**requerido**): If `CUSTOM`, use `customNumbers` to specify which incoming caller ID values cause this rule to match. `ANY` means any incoming call matches assuming the rule is in effect based on the associated schedules.  * `ANY` - Rule matches for calls from any number.  * `CUSTOM` - Rule matches based on the numbers and options in `customNumbers`. Valores: ANY, CUSTOM.
  - `customNumbers` (object) (**requerido**): Custom rules for matching incoming caller ID information.
    - `privateNumberEnabled` (boolean) (**requerido**): Match if caller ID indicates the call is from a private number.
    - `unavailableNumberEnabled` (boolean) (**requerido**): Match if caller ID is unavailable.
    - `numbers` (array): Array of number strings to be matched against incoming caller ID.
- `callsTo` (object) (**requerido**): Settings related to the rule matching based on the destination number.
  - `numbers` (array): Array of numbers to be matched against the calling destination number.
    - `phoneNumber` (string): Only return call queues with matching primary phone number or extension.
    - `extension` (string): Primary phone extension of the call queue.
    - `type` (string) (**requerido**): Type of  * `PRIMARY` - Indicates that the given `phoneNumber` or `extension` associated with this rule's containing object is a primary number or extension.  * `ALTERNATE` - Indicates that the given `phoneNumber` or `extension` associated with this rule's containing object is an alternate number or extension. Valores: PRIMARY, ALTERNATE.

### Ejemplo — petición
```json
{
  "name": "New Selective Rule",
  "holidaySchedule": "HolidayScheduleOne",
  "businessSchedule": "BusinessScheduleTwo",
  "callsFrom": {
    "selection": "CUSTOM",
    "customNumbers": {
      "privateNumberEnabled": true,
      "unavailableNumberEnabled": true,
      "numbers": [
        "2025551212"
      ]
    }
  },
  "callsTo": {
    "numbers": []
  },
  "forwardTo": {
    "selection": "FORWARD_TO_DEFAULT_NUMBER"
  },
  "enabled": true
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations/<locationId>/queues/<queueId>/callForwarding/selectiveRules' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "callsFrom": {}, "callsTo": {}}'
```

## Respuestas correctas
**201**: Created
- `id` (string) (**requerido**): ID of the newly created call queue.

### Ejemplo — respuesta 201
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0hVTlRfR1JPVVAvYUhaaFpUTjJNRzh5YjBBMk5EazBNVEk1Tnk1cGJuUXhNQzVpWTJ4a0xuZGxZbVY0TG1OdmJRPT0"
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