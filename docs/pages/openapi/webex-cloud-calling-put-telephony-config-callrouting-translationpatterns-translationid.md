---
doc_id: webex-cloud-calling-put-telephony-config-callrouting-translationpatterns-translationid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/callRouting/translationPatterns/{translationId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.558789+00:00
---

# PUT /telephony/config/callRouting/translationPatterns/{translationId}

**API:** Webex Cloud Calling
**Área:** Call Routing
**operationId:** `Modify a specific Translation Pattern for an Organization`

## Resumen
Modify a specific Translation Pattern for an Organization

## Descripción
Modify a translation pattern for a given organization.

A translation pattern lets you manipulate dialed digits before routing a call and applies to outbound calls only. See [this article](https://help.webex.com/en-us/article/nib9o6h/Translation-patterns-for-outbound-calls) for details about the translation pattern syntax.

Requires a full administrator auth token with the `spark-admin:telephony_config_write` scope.

## Parámetros
- `orgId` [query] (string): ID of the organization containing the translation pattern.
- `translationId` [path] (string) **(requerido)**: Modify translation pattern with the matching ID.

## Cuerpo de la petición (application/json)
- `name` (string): Name given to a translation pattern for an organization.
- `matchingPattern` (string): Matching pattern given to a translation pattern for an organization.
- `replacementPattern` (string): Replacement pattern given to a translation pattern for an organization.

### Ejemplo de petición
```json
{
  "name": "CHNHelpDesk",
  "matchingPattern": "+91[2-7]XX21",
  "replacementPattern": "+91352133"
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
