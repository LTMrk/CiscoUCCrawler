---
doc_id: webex-cloud-calling-delete-telephony-config-virtuallines-virtuallineid-outgoingpermission-digitpatterns-digitpatternid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: DELETE
path: /telephony/config/virtualLines/{virtualLineId}/outgoingPermission/digitPatterns/{digitPatternId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.659683+00:00
---

# DELETE /telephony/config/virtualLines/{virtualLineId}/outgoingPermission/digitPatterns/{digitPatternId}

**API:** Webex Cloud Calling
**Área:** Virtual Line Call Settings
**operationId:** `Delete a Digit Pattern for a Virtual Profile`

## Resumen
Delete a Digit Pattern for a Virtual Profile

## Descripción
Delete a digit pattern for a virtual profile.

Digit patterns are used to bypass permissions.

Deleting the digit pattern requires a full, user, or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `virtualLineId` [path] (string) **(requerido)**: Unique identifier for the virtual line.
- `digitPatternId` [path] (string) **(requerido)**: Unique identifier for the digit pattern.
- `orgId` [query] (string): ID of the organization in which the virtual line resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

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
