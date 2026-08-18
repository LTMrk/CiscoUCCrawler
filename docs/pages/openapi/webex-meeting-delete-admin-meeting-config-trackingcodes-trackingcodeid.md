---
doc_id: webex-meeting-delete-admin-meeting-config-trackingcodes-trackingcodeid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: DELETE
path: /admin/meeting/config/trackingCodes/{trackingCodeId}
operation_id: Delete a Tracking Code
tags: Tracking Codes
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.492588+00:00
---

# DELETE /admin/meeting/config/trackingCodes/{trackingCodeId}

**API:** Webex Meetings
**Área:** Tracking Codes
**operationId:** `Delete a Tracking Code`

## Resumen
Delete a Tracking Code

## Descripción
Deletes a tracking code by an admin user.

* The `siteUrl` is required. The operation deletes a tracking code for the specified site. All of a user's available Webex sites can be retrieved by the [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

* Admins can switch any Control Hub managed site from using classic tracking codes to mapped tracking codes in Control Hub, this is a one-time irreversible operation. Once the tracking codes are mapped to custom or user profile attributes, they cannot delete tracking codes when the mapping process is in progress or the mapping process is completed.

## Parámetros
- `trackingCodeId` [path] (string) (**requerido**): Unique identifier for the tracking code to be deleted.
- `siteUrl` [query] (string) (**requerido**): URL of the Webex site from which the API deletes the tracking code. All available Webex sites and preferred sites of a user can be retrieved by the [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

## Ejemplo de invocación
```bash
curl -X DELETE '/admin/meeting/config/trackingCodes/<trackingCodeId>?siteUrl=<siteUrl>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**204**: No Content

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found
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
The Webex Meetings APIs enable developers to schedule, manage, and retrieve information about Webex meetings, webinars, and events. They provide endpoints for meeting creation, participant management, recordings, transcripts, in-meeting features such as chat and closed captions, and post-meeting analytics. Common use cases include integrating meeting scheduling into calendar apps, automating follow-ups with recordings and transcripts, embedding meeting controls in custom portals, and extracting insights for compliance or productivity analysis. The APIs support both real-time and asynchronous w...

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs