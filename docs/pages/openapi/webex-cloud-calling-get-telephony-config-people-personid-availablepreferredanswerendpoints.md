---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-availablepreferredanswerendpoints
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/{personId}/availablePreferredAnswerEndpoints
operation_id: getPersonAvailablePreferredAnswerEndpoints
tags: User Call Settings (3/3)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-30T18:17:19.913501+00:00
---

# GET /telephony/config/people/{personId}/availablePreferredAnswerEndpoints

**API:** Webex Cloud Calling
**Área:** User Call Settings (3/3)
**operationId:** `getPersonAvailablePreferredAnswerEndpoints`

## Resumen
Get Available Preferred Answer Endpoints for a Person

## Descripción
Get the list of available preferred answer endpoints for a specific person. This API returns all available endpoints in a single response.

A Webex Calling person may be associated with multiple endpoints such as Webex App (desktop or mobile), Cisco desk IP phone, Webex Calling-supported analog devices, or third-party endpoints. Preferred answering endpoints allow administrators to specify which of these devices should be prioritized for answering calls, particularly when a person's extension (or a virtual line assigned to them) rings on multiple devices. This helps ensure that calls are answered on the most convenient or appropriate device for the person.

This API requires a full administrator, read-only administrator, delegated full administrator, user administrator, or location administrator auth token with the `spark-admin:telephony_config_read` scope.

## Parámetros
- `personId` [path] (string) (**requerido**): The unique identifier for the person.
- `orgId` [query] (string): Optional target organization identifier. Defaults to token's organization if not provided.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/<personId>/availablePreferredAnswerEndpoints' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `endpoints` (array) (**requerido**): Array of endpoints available to the person. All available endpoints are returned in a single response.
  - `id` (string) (**requerido**): Unique identifier for the endpoint. The companion `type` identifies the endpoint category; the opaque identifier represents a `CALLING_DEVICE`, `APPLICATION`, or `HOTDESKING_GUEST` resource.
  - `type` (string) (**requerido**): Endpoint resource type returned by the API.   * `CALLING_DEVICE` - A physical Webex Calling device registered to the person.  * `APPLICATION` - A software application such as Webex App registered to the person.  * `HOTDESKING_GUEST` - A hot desking guest endpoint for the person. Valores: CALLING_DEVICE, APPLICATION, HOTDESKING_GUEST.
  - `name` (string) (**requerido**): Name of the endpoint. For a device endpoint, the name can include the value of a configured `name=<value>` device tag.
  - `isPreferredAnswerEndpoint` (boolean) (**requerido**): Indicates whether this endpoint is currently selected as the preferred answer endpoint.

### Ejemplo — respuesta 200
```json
{
  "endpoints": [
    {
      "id": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMV9pbnQxMy9DQUxMSU5HX0RFVklDRS82NjY2Nzc3Ny04ODg4LTRhOTQtOGZiZC0wMzM2NzhmMDU5ZjM=",
      "type": "CALLING_DEVICE",
      "name": "Cisco 8865",
      "isPreferredAnswerEndpoint": true
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL2UxNjI5MGQ2LWRkZGYtNDBlNy04MTUxLTNlY2UwMjc1N2RhMA",
      "type": "APPLICATION",
      "name": "Webex Desktop Application",
      "isPreferredAnswerEndpoint": false
    }
  ]
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