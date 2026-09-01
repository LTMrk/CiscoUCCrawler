---
doc_id: webex-cloud-calling-put-people-personid-features-callingbehavior
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /people/{personId}/features/callingBehavior
operation_id: Configure Calling Behavior for a person
tags: User Call Settings (1/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.752251+00:00
---

# PUT /people/{personId}/features/callingBehavior

**API:** Webex Cloud Calling
**Área:** User Call Settings (1/2)
**operationId:** `Configure Calling Behavior for a person`

## Resumen
Configure a person's Calling Behavior

## Descripción
Modifies the calling behavior settings for the person which includes calling behavior and UC Manager Profile ID.

Webex Calling Behavior controls which Webex telephony application and which UC Manager Profile is to be used for a person.

An organization has an organization-wide default Calling Behavior that may be overridden for individual persons.

UC Manager Profiles are applicable if your organization uses Jabber in Team Messaging mode or Calling in Webex (Unified CM).

The UC Manager Profile also has an organization-wide default and may be overridden for individual persons.

This API requires a full or user administrator auth token with the `spark-admin:people_write` scope.

## Parámetros
- `personId` [path] (string) (**requerido**): Unique identifier for the person.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Cuerpo de la petición (application/json)
- `behaviorType` (string): The new Calling Behavior setting for the person (case-insensitive). If `null`, the effective Calling Behavior will be the Organization's current default.  * `NATIVE_WEBEX_TEAMS_CALLING` - Calling in Webex or Hybrid Calling.  * `CALL_WITH_APP_REGISTERED_FOR_CISCOTEL` - Cisco Jabber app  * `CALL_WITH_APP_REGISTERED_FOR_TEL` - Third-Party app  * `CALL_WITH_APP_REGISTERED_FOR_WEBEXCALLTEL` - Webex Calling app  * `NATIVE_SIP_CALL_TO_UCM` - Calling in Webex (Unified CM) Valores: NATIVE_WEBEX_TEAMS_CALLING, CALL_WITH_APP_REGISTERED_FOR_CISCOTEL, CALL_WITH_APP_REGISTERED_FOR_TEL, CALL_WITH_APP_REGISTERED_FOR_WEBEXCALLTEL, NATIVE_SIP_CALL_TO_UCM.
- `profileId` (string): The UC Manager Profile ID. Specifying null results in the organizational default being applied. In addition, when `behaviorType` is set to `CALL_WITH_APP_REGISTERED_FOR_CISCOTEL`, then the profile ID value will be cleared irrespective of any value being passed.

### Ejemplo — petición
```json
{
  "behaviorType": "NATIVE_WEBEX_TEAMS_CALLING",
  "profileId": "Y2lzY29zcGFyazovL3VzL0NBTExJTkdfUFJPRklMRS9iMzdmMmZiYS0yZTdjLTExZWItYTM2OC1kYmU0Yjc2NzFmZTk"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/people/<personId>/features/callingBehavior' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**204**: No Content

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