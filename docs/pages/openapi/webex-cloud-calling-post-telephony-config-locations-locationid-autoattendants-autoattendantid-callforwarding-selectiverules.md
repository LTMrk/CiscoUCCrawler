---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-autoattendants-autoattendantid-callforwarding-selectiverules
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/config/locations/{locationId}/autoAttendants/{autoAttendantId}/callForwarding/selectiveRules
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.598371+00:00
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
- `locationId` [path] (string) **(requerido)**: Location in which the auto attendant exists.
- `autoAttendantId` [path] (string) **(requerido)**: Create the rule for this auto attendant.
- `orgId` [query] (string): Create the auto attendant rule for this organization.

## Cuerpo de la petición (application/json)
- `name` (string) **(requerido)**: Unique name for the selective rule in the auto attendant.
- `enabled` (boolean): Reflects if rule is enabled.
- `businessSchedule` (string): Name of the location's business schedule which determines when this selective call forwarding rule is in effect.
- `holidaySchedule` (string): Name of the location's holiday schedule which determines when this selective call forwarding rule is in effect.
- `forwardTo` (object) **(requerido)**:
  - `phoneNumber` (string): Phone number used if selection is `FORWARD_TO_SPECIFIED_NUMBER`.
  - `selection` (string) **(requerido)**: Controls what happens when the rule matches.  * `FORWARD_TO_DEFAULT_NUMBER` - When the rule matches, forward to the destination for the auto attendant.  * `FORWARD_TO_SPECIFIED_NUMBER` - When the rule matches, forward to the destination for this rule.  * `DO_NOT_FORWARD` - When the rule matches, do not forward to another number. Valores: FORWARD_TO_DEFAULT_NUMBER, FORWARD_TO_SPECIFIED_NUMBER, DO_NOT_FORWARD.
- `callsFrom` (object) **(requerido)**:
  - `selection` (string) **(requerido)**: If `CUSTOM`, use `customNumbers` to specify which incoming caller ID values cause this rule to match. `ANY` means any incoming call matches assuming the rule is in effect based on the associated schedules.  * `ANY` - Rule matches for calls from any number.  * `CUSTOM` - Rule matches based on the numbers and options in customNumbers. Valores: ANY, CUSTOM.
  - `customNumbers` (object):
    - `privateNumberEnabled` (boolean) **(requerido)**: Match if caller ID indicates the call is from a private number.
    - `unavailableNumberEnabled` (boolean) **(requerido)**: Match if callerID is unavailable.
    - `numbers` (array) **(requerido)**: Array of number strings to be matched against incoming caller ID.
- `callsTo` (object):
  - `numbers` (array): Array of numbers to be matched against the calling destination number.
    - `phoneNumber` (string): AutoCalls To phone number. Either phone number or extension should be present as mandatory.
    - `extension` (string): Calls To extension.  Either `phoneNumber` or `extension` is mandatory.
    - `type` (string) **(requerido)**: Calls to type options.  * `PRIMARY` - Indicates that the given `phoneNumber` or `extension` associated with this rule's containing object is a primary number or extension.  * `ALTERNATE` - Indicates that the given `phoneNumber` or `extension` associated with this rule's containing object is an alternate number or extension. Valores: PRIMARY, ALTERNATE.

### Ejemplo de petición
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

## Respuestas
- **201**: Created
  - `id` (string) **(requerido)**: ID of the newly created auto attendant call forward selective rule.
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
