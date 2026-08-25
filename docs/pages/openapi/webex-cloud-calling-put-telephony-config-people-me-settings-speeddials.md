---
doc_id: webex-cloud-calling-put-telephony-config-people-me-settings-speeddials
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/people/me/settings/speedDials
operation_id: modifySpeedDials
tags: Call Settings For Me
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.386324+00:00
---

# PUT /telephony/config/people/me/settings/speedDials

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `modifySpeedDials`

## Resumen
Modify Speed Dials

## Descripción
Modify the Speed Dials settings for the authenticated user. This is a replacement list for speed dials.

Speed Dials allow Webex Calling users to quickly dial frequently contacted people, places, or virtual lines by assigning them to dedicated keys on their desk phones or soft clients.

This API requires a user auth token with a scope of `spark:telephony_config_write`.

## Cuerpo de la petición (application/json)
- `speedDials` (array) (**requerido**): List of speed dial entries to be configured for the person. This is a replacement list.
  - `id` (string): The identifier of the person (PEOPLE), place (PLACE), or virtual line (VIRTUAL_LINE) to add as a speed dial. Use this field when adding a speed dial for an existing member in the organization. Either `id` or `phoneNumber` must be provided.
  - `phoneNumber` (string): The phone number to add as a speed dial. Use this field when adding a speed dial for an external contact or custom number. Either `id` or `phoneNumber` must be provided. Long. max: 31.
  - `lineKeyLabel` (string): This is a custom label configured for the speed dial on the device. Long. max: 63.

### Ejemplo — petición
```json
{
  "speedDials": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85M2JjZWQ2Mi1lYWRmLTQ0MGItYThiYi03ZWQ5ZWEwNzExMTg",
      "lineKeyLabel": "Manager"
    },
    {
      "phoneNumber": "+15594015482",
      "lineKeyLabel": "Support"
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/people/me/settings/speedDials' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"speedDials": []}'
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