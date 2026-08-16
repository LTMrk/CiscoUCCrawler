---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-callparks-settings
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/locations/{locationId}/callParks/settings
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.600617+00:00
---

# PUT /telephony/config/locations/{locationId}/callParks/settings

**API:** Webex Cloud Calling
**Área:** Features:  Call Park
**operationId:** `Update Call Park settings`

## Resumen
Update Call Park settings

## Descripción
Update Call Park settings for the designated location.

Call Park allows call recipients to place a call on hold so that it can be retrieved from another device.

Updating call park settings requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Location for which call park settings will be updated.
- `orgId` [query] (string): Update call park settings from this organization.

## Cuerpo de la petición (application/json)
- `callParkRecall` (object):
  - `huntGroupId` (string): Alternate user which is a hunt group ID for call park recall alternate destination.
  - `option` (string) **(requerido)**: Call park recall options.  * `ALERT_PARKING_USER_ONLY` - Alert parking user only.  * `ALERT_PARKING_USER_FIRST_THEN_HUNT_GROUP` - Alert parking user first, then hunt group.  * `ALERT_HUNT_GROUP_ONLY` - Alert hunt group only. Valores: ALERT_PARKING_USER_ONLY, ALERT_PARKING_USER_FIRST_THEN_HUNT_GROUP, ALERT_HUNT_GROUP_ONLY.
- `callParkSettings` (object):
  - `ringPattern` (string) **(requerido)**: Ring pattern for when this callpark is called.  * `NORMAL` - Normal incoming ring pattern.  * `LONG_LONG` - Incoming ring pattern of two long rings.  * `SHORT_SHORT_LONG` - Incoming ring pattern of two short rings, followed by a short ring.  * `SHORT_LONG_SHORT` - Incoming ring pattern of a short ring, followed by a long ring, followed by a short ring. Valores: NORMAL, LONG_LONG, SHORT_SHORT_LONG, SHORT_LONG_SHORT.
  - `recallTime` (number): Amount of time within 30 and 600 seconds the Call Park will be parked. If the call isn't picked up within the set time, then the call will be recalled based on the Call Park Recall setting.
  - `huntWaitTime` (number): Amount of time within 30 and 600 seconds the Call Park will be parked. If the call isn't picked up, the call will revert back to the hunt group (after the person who parked the call is alerted).

### Ejemplo de petición
```json
{
  "callParkRecall": {
    "huntGroupId": "Y2lzY29zcGFyazovL3VzL0hVTlRfR1JPVVAvZEdWamFHNXBZMkZzTFhOMWNIQnZjblF0TlRVMU9EWTNOVE13T1VCbmJXRnBiQzVqYjIwPQ",
    "huntGroupName": "Technical Support Group - 5558675309",
    "option": "ALERT_HUNT_GROUP_ONLY"
  },
  "callParkSettings": {
    "ringPattern": "NORMAL",
    "recallTime": 45,
    "huntWaitTime": 45
  }
}
```

## Respuestas
- **204**: No Content
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
