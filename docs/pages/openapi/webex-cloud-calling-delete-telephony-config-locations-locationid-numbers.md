---
doc_id: webex-cloud-calling-delete-telephony-config-locations-locationid-numbers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: DELETE
path: /telephony/config/locations/{locationId}/numbers
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.631879+00:00
---

# DELETE /telephony/config/locations/{locationId}/numbers

**API:** Webex Cloud Calling
**Área:** Numbers
**operationId:** `Remove phone numbers from a location`

## Resumen
Remove Phone Numbers from a Location

## Descripción
Remove the specified set of phone numbers from a location for an organization.

Phone numbers must follow the E.164 format.

Removing a mobile number may require more time depending on mobile carrier capabilities.

Removing a phone number from a location requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

A location's main number cannot be removed.

<br/>

<div><Callout type="warning">This API is only supported for non-integrated PSTN connection types of Local Gateway (LGW) and Non-integrated CPP. It should never be used for locations with integrated PSTN connection types like Cisco Calling Plans or Integrated CCP because backend data issues may occur.</Callout></div>

## Parámetros
- `locationId` [path] (string) **(requerido)**: `LocationId` to which numbers should be added.
- `orgId` [query] (string): Organization of the Route Group.

## Cuerpo de la petición (application/json)
- `phoneNumbers` (array) **(requerido)**: List of phone numbers that need to be deleted. The maximum limit is 5.

### Ejemplo de petición
```json
{
  "phoneNumbers": [
    "+12145557861",
    "+12145551321"
  ]
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
