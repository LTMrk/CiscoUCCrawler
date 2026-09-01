---
doc_id: webex-cloud-calling-get-telephony-calls-history
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/calls/history
operation_id: listcallhistory
tags: Call Controls, External Voicemail
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.560767+00:00
---

# GET /telephony/calls/history

**API:** Webex Cloud Calling
**Área:** Call Controls, External Voicemail
**operationId:** `listcallhistory`

## Resumen
List Call History

## Descripción
Get the list of call history records for the user. A maximum of 20 call history records per type (`placed`, `missed`, `received`) are returned.

## Parámetros
- `type` [query] (string): The type of call history records to retrieve. If not specified, then all call history records are retrieved. Valores: placed, missed, received.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/calls/history' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array) (**requerido**):
  - `type` (object) (**requerido**): The type of call history record.
  - `name` (string): The name of the called/calling party. Only present when the name is available and privacy is not enabled.
  - `number` (string): The number of the called/calling party. Only present when the number is available and privacy is not enabled. The number can be digits or a URI. Some examples for number include: `1234`, `2223334444`, `+12223334444`, `*73`, `user@company.domain`
  - `privacyEnabled` (boolean) (**requerido**): Indicates whether privacy is enabled for the name and number.
  - `time` (string) (**requerido**): The date and time the call history record was created. For a placed call history record, this is when the call was placed. For a missed call history record, this is when the call was disconnected. For a received call history record, this is when the call was answered.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "type": "placed",
      "name": "John Smith",
      "number": "+12225554444",
      "privacyEnabled": false,
      "time": "2016-04-21T17:00:00.000Z"
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