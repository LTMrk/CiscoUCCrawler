---
doc_id: webex-cloud-calling-put-telephony-config-people-personid-singlenumberreach-numbers-id
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/people/{personId}/singleNumberReach/numbers/{id}
operation_id: Update Single Number Reach Settings For A Number
tags: Features: Single Number Reach
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.289468+00:00
---

# PUT /telephony/config/people/{personId}/singleNumberReach/numbers/{id}

**API:** Webex Cloud Calling
**Área:** Features: Single Number Reach
**operationId:** `Update Single Number Reach Settings For A Number`

## Resumen
Update Single Number Reach Settings For A Number

## Descripción
Update Single number reach settings for a number.

Single number reach allows you to setup your work calls ring any phone number. This means that your office phone, mobile phone, or any other designated devices can ring at the same time, ensuring you don't miss important calls.

The response returns an ID that can change if the phoneNumber is modified, as the ID contains base64 encoded phone number data.

Updating a single number reach settings for a number requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `personId` [path] (string) (**requerido**): Unique identifier for the person.
- `id` [path] (string) (**requerido**): Unique identifier for single number reach.

## Cuerpo de la petición (application/json)
- `phoneNumber` (string) (**requerido**): Personal phone number used as single Number Reach.
- `enabled` (boolean) (**requerido**): A flag to enable or disable single Number Reach phone number.
- `name` (string) (**requerido**): Name of the single number reach phone number entry.
- `doNotForwardCallsEnabled` (boolean): If enabled, the call forwarding settings of provided phone Number will not be applied.
- `answerConfirmationEnabled` (boolean): If enabled, the call recepient will be prompted to press a key before being connected.

### Ejemplo — petición
```json
{
  "phoneNumber": "+17011558169",
  "enabled": true,
  "name": "myNumber",
  "doNotForwardCallsEnabled": false,
  "answerConfirmationEnabled": false
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/people/<personId>/singleNumberReach/numbers/<id>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"phoneNumber": "<phoneNumber>", "enabled": true, "name": "<name>"}'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): ID of the updated single number reach. Note that this ID can change if the phone number is changed, as the ID contains base64 encoded phone number data.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1NJTkdMRV9OVU1CRVJfUkVBQ0gvS3pFM01ERXhOVFU0TVRZNQ"
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