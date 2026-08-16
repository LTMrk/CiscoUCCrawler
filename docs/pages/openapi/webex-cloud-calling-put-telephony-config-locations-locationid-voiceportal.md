---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-voiceportal
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/locations/{locationId}/voicePortal
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.629261+00:00
---

# PUT /telephony/config/locations/{locationId}/voicePortal

**API:** Webex Cloud Calling
**Área:** Location Call Settings:  Voicemail
**operationId:** `Update VoicePortal`

## Resumen
Update VoicePortal

## Descripción
Update Voice portal information for the location.

Voice portals provide an interactive voice response (IVR)
system so administrators can manage auto attendant anouncements.

Updating voice portal information for an organization and/or rules requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Location to which the voice portal belongs.
- `orgId` [query] (string): Update voicemail rules for this organization.

## Cuerpo de la petición (application/json)
- `name` (string): Voice Portal Name.
- `languageCode` (string): Language code for voicemail group audio announcement.
- `extension` (string): Extension of incoming call.
- `phoneNumber` (string): Phone Number of incoming call.
- `firstName` (string): Caller ID First Name. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `lastName` (string): Caller ID Last Name. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `passcode` (object): Voice Portal Admin Passcode.
  - `newPasscode` (string): New passcode.
  - `confirmPasscode` (string): Confirm new passcode.
- `directLineCallerIdName` (object): Settings for the direct line caller ID name to be shown for this workspace.
  - `selection` (string): * `DISPLAY_NAME` - When this option is selected, `displayName` is to be shown for this workspace.  * `CUSTOM_NAME` - When this option is selected, `customName` is to be shown for this workspace. Valores: CUSTOM_NAME, DISPLAY_NAME.
  - `customName` (string): Sets or clears the custom direct line caller ID name.  To clear the `customName`, the attribute must be set to null or empty string. Required if `selection` is set to `CUSTOM_NAME`.
- `dialByName` (string): Sets or clears the name to be used for dial by name functions. To clear the `dialByName`, the attribute must be set to null or empty string. Characters of `%`,  `+`, `\`, `"` and Unicode characters are not allowed.

### Ejemplo de petición
```json
{
  "name": "Voice Portal Name",
  "languageCode": "en_us",
  "extension": 5678,
  "firstName": "John",
  "lastName": "Brown",
  "passcode": {
    "newPasscode": "135668",
    "confirmPasscode": "135668"
  },
  "directLineCallerIdName": {
    "selection": "CUSTOM_NAME",
    "customName": "Hakim Smith"
  },
  "dialByName": "Hakim Smith"
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
