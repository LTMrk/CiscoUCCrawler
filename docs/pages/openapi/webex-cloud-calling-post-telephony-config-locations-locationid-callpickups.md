---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-callpickups
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/config/locations/{locationId}/callPickups
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.601344+00:00
---

# POST /telephony/config/locations/{locationId}/callPickups

**API:** Webex Cloud Calling
**Área:** Features:  Call Pickup
**operationId:** `Create a Call Pickup`

## Resumen
Create a Call Pickup

## Descripción
Create new Call Pickups for the given location.

Call Pickup enables a user (agent) to answer any ringing line within their pickup group.

Creating a call pickup requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

**NOTE**: The Call Pickup ID will change upon modification of the Call Pickup name.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Create the call pickup for this location.
- `orgId` [query] (string): Create the call pickup for this organization.

## Cuerpo de la petición (application/json)
- `name` (string) **(requerido)**: Unique name for the call pickup. The maximum length is 80.
- `notificationType` (string): Type of the notification when an incoming call is unanswered. The call pickup group notifies all of its members. Default: NONE.  * `NONE` - Notification is not sent to any member of the call pickup group.  * `AUDIO_ONLY` - When the notificationDelayTimerSeconds number of seconds has elapsed, play an audio notification for each call pickup group member.  * `VISUAL_ONLY` - When the notificationDelayTimerSeconds number of seconds has elapsed, provide a visual notification to every call pickup group member.  * `AUDIO_AND_VISUAL` - When the `notificationDelayTimerSeconds` number of seconds has elapsed, provide an audio and visual notification to every call pickup group member. Valores: NONE, AUDIO_ONLY, VISUAL_ONLY, AUDIO_AND_VISUAL.
- `notificationDelayTimerSeconds` (number): After the number of seconds given by the `notificationDelayTimerSeconds` has elapsed, notify every member of the call pickup group when an incoming call goes unanswered. The `notificationType` field specifies the notification method. Default: 6.
- `agents` (array): An Array of ID strings of people, workspaces and virtual lines that are added to call pickup.

### Ejemplo de petición
```json
{
  "name": "South Alaska-Group",
  "notificationType": "AUDIO_ONLY",
  "notificationDelayTimerSeconds": 20,
  "agents": [
    "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80YTc2ZmVmNC1mZjlmLTExZWItYWYwZC00M2YwZjY1NTdjYWI",
    "Y2lzY29zcGFyazovL3VzL1BMQUNFLzU1YjUyZThhLWZmOWYtMTFlYi05ZjRhLTAzZDY1NzdhYzg1Yg",
    "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfTElORS85ODFlNTQ0Yy0xOGI0LTQ2MzItYmFkZi1iYWMwZjFkOGJkYWY="
  ]
}
```

## Respuestas
- **201**: Created
  - `id` (string) **(requerido)**: ID of the newly created call pickup.
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
