---
doc_id: webex-cloud-calling-put-telephony-config-people-me-settings-callpolicies
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/people/me/settings/callPolicies
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.566668+00:00
---

# PUT /telephony/config/people/me/settings/callPolicies

**API:** Webex Cloud Calling
**Área:** Beta Call Settings For Me With Userhub Phase1
**operationId:** `updateMyCallPoliciesSettings`

## Resumen
Modify Call Policies Settings for User

## Descripción
Update call policies settings for the authenticated user.

Call Policies in Webex allow you to manage how your call information is displayed and handled. You can configure privacy settings for your connected line ID on redirected calls and control other call-related preferences.

This API requires a user auth token with a scope of `spark:telephony_config_write`.

## Cuerpo de la petición (application/json)
- `connectedLineIdPrivacyOnRedirectedCalls` (string): * `NO_PRIVACY` - Caller sees the final destination's identity when call is redirected.  * `PRIVACY_FOR_EXTERNAL_CALLS` - Internal callers see the final destination's identity; external callers see the original recipient's identity.  * `PRIVACY_FOR_ALL_CALLS` - All callers see the original recipient's identity when call is redirected. Valores: NO_PRIVACY, PRIVACY_FOR_EXTERNAL_CALLS, PRIVACY_FOR_ALL_CALLS.

### Ejemplo de petición
```json
{
  "connectedLineIdPrivacyOnRedirectedCalls": "NO_PRIVACY"
}
```

## Respuestas
- **204**: Call policies updated successfully for the authenticated user.
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
