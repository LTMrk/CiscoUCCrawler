---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-answersettings
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/{personId}/answerSettings
operation_id: getPersonAnswerSettings
tags: User Call Settings (3/3)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-30T18:17:19.912958+00:00
---

# GET /telephony/config/people/{personId}/answerSettings

**API:** Webex Cloud Calling
**Área:** User Call Settings (3/3)
**operationId:** `getPersonAnswerSettings`

## Resumen
Get Answer Settings for a Person

## Descripción
Get the answer settings for a specific person.

Answer settings allow administrators to configure automatic call answering behavior for a person, including preferred answer endpoint and whether auto answer is enabled.

This API requires a full administrator, read-only administrator, delegated full administrator, user administrator, or location administrator auth token with the `spark-admin:telephony_config_read` scope.

## Parámetros
- `personId` [path] (string) (**requerido**): The unique identifier for the person.
- `orgId` [query] (string): Optional target organization identifier. Defaults to token's organization if not provided.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/<personId>/answerSettings' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `preferredAnswerEndpointId` (string): The unique identifier for the preferred answer endpoint. The companion `preferredAnswerEndpointIdType` identifies the encoded resource type as `APPLICATION`, `CALLING_DEVICE`, or `HOTDESKING_GUEST`.
- `preferredAnswerEndpointType` (string): The preferred endpoint's behavior category.   * `WEBEX_APP_DESKTOP` - The Webex desktop application answers the call.  * `PRIMARY_DEVICE` - The person's primary physical device answers the call.  * `NON_PRIMARY_DEVICE` - A physical device other than the person's primary device answers the call.  * `HOTDESK_DEVICE` - The device on which the person is signed in as a hot desking guest answers the call.  * `NONE` - No preferred answer endpoint is selected. Valores: WEBEX_APP_DESKTOP, PRIMARY_DEVICE, NON_PRIMARY_DEVICE, HOTDESK_DEVICE, NONE.
- `preferredAnswerEndpointIdType` (string): The resource type encoded by `preferredAnswerEndpointId`.   * `APPLICATION` - The identifier represents a Webex application.  * `CALLING_DEVICE` - The identifier represents a Webex Calling device.  * `HOTDESKING_GUEST` - The identifier represents a hot desking guest session. Valores: APPLICATION, CALLING_DEVICE, HOTDESKING_GUEST.
- `preferredAnswerEndpointRequired` (boolean) (**requerido**): Indicates whether the person must have a preferred answer endpoint selected in order for a call to be auto-answered.
- `autoAnswerEnabled` (boolean) (**requerido**): Indicates whether auto answer is enabled for the person.
- `isPreferredEndpointClearableByPerson` (boolean) (**requerido**): Indicates whether the person can clear the preferred endpoint setting.

### Ejemplo — respuesta 200
```json
{
  "preferredAnswerEndpointId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMV9pbnQxMy9DQUxMSU5HX0RFVklDRS82NjY2Nzc3Ny04ODg4LTRhOTQtOGZiZC0wMzM2NzhmMDU5ZjM=",
  "preferredAnswerEndpointType": "PRIMARY_DEVICE",
  "preferredAnswerEndpointIdType": "CALLING_DEVICE",
  "preferredAnswerEndpointRequired": true,
  "autoAnswerEnabled": true,
  "isPreferredEndpointClearableByPerson": false
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested does not exist. Also returned when the requested format is not supported by the requested method.
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