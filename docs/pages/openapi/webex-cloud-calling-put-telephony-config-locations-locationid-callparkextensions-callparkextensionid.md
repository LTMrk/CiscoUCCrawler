---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-callparkextensions-callparkextensionid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/locations/{locationId}/callParkExtensions/{callParkExtensionId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.601016+00:00
---

# PUT /telephony/config/locations/{locationId}/callParkExtensions/{callParkExtensionId}

**API:** Webex Cloud Calling
**Área:** Features:  Call Park
**operationId:** `Update a Call Park Extension`

## Resumen
Update a Call Park Extension

## Descripción
Update the designated Call Park Extension.

Call Park Extension enables a call recipient to park a call to an extension, so someone else within the same Organization can retrieve the parked call by dialing that extension. Call Park Extensions can be added as monitored lines by users' Cisco phones, so users can park and retrieve calls by pressing the associated phone line key.

Updating a call park extension requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Location in which this call park extension exists.
- `callParkExtensionId` [path] (string) **(requerido)**: Update a call park extension with the matching ID.
- `orgId` [query] (string): Update a call park extension from this organization.

## Cuerpo de la petición (application/json)
- `name` (string): Name for the call park extension. The maximum length is 30.
- `extension` (string): Unique extension which will be assigned to call park extension. The minimum length is 2, maximum length is 10.

### Ejemplo de petición
```json
{
  "name": "Illinois, Call Park Extension",
  "extension": "407721"
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
