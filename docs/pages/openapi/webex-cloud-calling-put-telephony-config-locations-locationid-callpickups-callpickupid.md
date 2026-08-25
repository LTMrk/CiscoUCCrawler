---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-callpickups-callpickupid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/callPickups/{callPickupId}
operation_id: Update a Call Pickup
tags: Features:  Call Pickup
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.470033+00:00
---

# PUT /telephony/config/locations/{locationId}/callPickups/{callPickupId}

**API:** Webex Cloud Calling
**Área:** Features:  Call Pickup
**operationId:** `Update a Call Pickup`

## Resumen
Update a Call Pickup

## Descripción
Update the designated Call Pickup.

Call Pickup enables a user (agent) to answer any ringing line within their pickup group.

Updating a call pickup requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

**NOTE**: The Call Pickup ID will change upon modification of the Call Pickup name.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location in which this call pickup exists.
- `callPickupId` [path] (string) (**requerido**): Update settings for a call pickup with the matching ID.
- `orgId` [query] (string): Update call pickup settings from this organization.

## Cuerpo de la petición (application/json)
- `name` (string): Unique name for the call pickup. The maximum length is 80.
- `notificationType` (string): Type of the notification when an incoming call is unanswered. The call pickup group notifies all of its members. Default: NONE.  * `NONE` - Notification is not sent to any member of the call pickup group.  * `AUDIO_ONLY` - When the notificationDelayTimerSeconds number of seconds has elapsed, play an audio notification for each call pickup group member.  * `VISUAL_ONLY` - When the notificationDelayTimerSeconds number of seconds has elapsed, provide a visual notification to every call pickup group member.  * `AUDIO_AND_VISUAL` - When the `notificationDelayTimerSeconds` number of seconds has elapsed, provide an audio and visual notification to every call pickup group member. Valores: NONE, AUDIO_ONLY, VISUAL_ONLY, AUDIO_AND_VISUAL.
- `notificationDelayTimerSeconds` (number): After the number of seconds given by the `notificationDelayTimerSeconds` has elapsed, notify every member of the call pickup group when an incoming call goes unanswered. The `notificationType` field specifies the notification method. Default: 6.
- `agents` (array): An array of people, workspace, and virtual lines IDs, that are added to call pickup.

### Ejemplo — petición
```json
{
  "name": "South Alaska-Group",
  "notificationType": "AUDIO_ONLY",
  "notificationDelayTimerSeconds": 20,
  "agents": [
    "Y2lzY29zcGFyazovL3VzL1BFT1BMRS82YTUwMDk1YS1mZjlmLTExZWItODA2NS04ZjhkOWIxNmIzOTQ",
    "Y2lzY29zcGFyazovL3VzL1BMQUNFLzg0YjQ1OTIyLWZmOWYtMTFlYi1hNGI4LTMzNjI3YmVkNjdiNQ",
    "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfTElORS85ODFlNTQ0Yy0xOGI0LTQ2MzItYmFkZi1iYWMwZjFkOGJkYWY="
  ]
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>/callPickups/<callPickupId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): ID of the target call pickup.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUElDS1VQL1kyRnNiRkJwWTJ0MWNEST0"
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