---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-availablepreferredanswerendpoints
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/settings/availablePreferredAnswerEndpoints
operation_id: getListAvailablePreferredAnswerEndpoints
tags: Call Settings For Me
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.174522+00:00
---

# GET /telephony/config/people/me/settings/availablePreferredAnswerEndpoints

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `getListAvailablePreferredAnswerEndpoints`
**Autenticación:** bearer-key

## Resumen
Get List Available Preferred Answer Endpoints

## Descripción
Get the person's preferred answer endpoint and the list of endpoints available for selection. The list of endpoints is empty if the person has no endpoints assigned which support the preferred answer endpoint functionality.

 A Webex Calling user may be associated with multiple endpoints such as Webex App (desktop or mobile), Cisco desk IP phone, Webex Calling-supported analog devices or third-party endpoints. Preferred answering endpoints allow users to specify which of these devices should be prioritized for answering calls, particularly when a person's extension (or a virtual line assigned to them) rings on multiple devices. This helps ensure that calls are answered on the most convenient or appropriate device for the person.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/settings/availablePreferredAnswerEndpoints' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `endpoints` (array) (**requerido**): Array of endpoints available to the person.
  - `id` (string) (**requerido**): Unique identifier for the endpoint.
  - `type` (string) (**requerido**): * `DEVICE` - The endpoint is a device.  * `APPLICATION` - The endpoint is a application. Valores: DEVICE, APPLICATION.
  - `name` (string) (**requerido**): The `name` field in the response is calculated using device tag. Admins have the ability to set tags for devices. If a `name=<value>` tag is set, for example “name=home phone“, then the `<value>` is included in the `name` field of the API response. In this example “home phone”.

### Ejemplo — respuesta 200
```json
{
  "endpoints": [
    {
      "id": "Y2lzY29z...",
      "type": "DEVICE",
      "name": "Cisco 8865 (Phone in reception area)",
      "isPreferredAnswerEndpoint": false
    },
    {
      "id": "Y2lzY29b...",
      "type": "APPLICATION",
      "name": "Webex Desktop Application",
      "isPreferredAnswerEndpoint": true
    }
  ]
}
```

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