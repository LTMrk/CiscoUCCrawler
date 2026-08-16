---
doc_id: webex-cloud-calling-get-telephony-config-emergencycallnotification
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/emergencyCallNotification
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.592124+00:00
---

# GET /telephony/config/emergencyCallNotification

**API:** Webex Cloud Calling
**Área:** Emergency Services Settings
**operationId:** `Get an Organization Emergency Call Notification`

## Resumen
Get an Organization Emergency Call Notification

## Descripción
Get organization emergency call notification.

Emergency Call Notifications can be enabled at the organization level, allowing specified email addresses to receive email notifications when an emergency call is made. To comply with U.S. Public Law 115-127, also known as Kari’s Law, any call that's made from within your organization to emergency services must generate an email notification.

To retrieve organization call notifications requires a full, user or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Retrieve Emergency Call Notification attributes for the organization.

## Respuestas
- **200**: OK
  - `emergencyCallNotificationEnabled` (boolean): When true sends an email to the specified email address when a call is made to emergency services.
  - `allowEmailNotificationAllLocationEnabled` (boolean): Send an emergency call notification email for all locations.
  - `emailAddress` (string): When `emergencyCallNotificationEnabled` is true, the emergency notification email is sent to the specified email address.
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
