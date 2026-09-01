---
doc_id: webex-cloud-calling-put-telephony-config-premisepstn-routelists-routelistid-numbers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/premisePstn/routeLists/{routeListId}/numbers
operation_id: Modify Numbers for Route List
tags: Call Routing
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.570624+00:00
---

# PUT /telephony/config/premisePstn/routeLists/{routeListId}/numbers

**API:** Webex Cloud Calling
**Área:** Call Routing
**operationId:** `Modify Numbers for Route List`

## Resumen
Modify Numbers for Route List

## Descripción
Modify numbers for a specific Route List of a Customer.

A Route List is a list of numbers that can be reached via a Route Group. It can be used to provide cloud PSTN connectivity to Webex Calling Dedicated Instance.

Retrieving a Route List requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `routeListId` [path] (string) (**requerido**): ID of the Route List.
- `orgId` [query] (string): Organization to which the Route List belongs.

## Cuerpo de la petición (application/json)
- `numbers` (array): Array of the numbers to be deleted/added.
  - `number` (string) (**requerido**): Number to be deleted/added.
  - `action` (string) (**requerido**): * `ADD` - Add a phone number to the Route List.  * `DELETE` - Delete a phone number from the Route List. Valores: ADD, DELETE.
- `deleteAllNumbers` (boolean): If present, the numbers array is ignored and all numbers in the route list are deleted.

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/premisePstn/routeLists/<routeListId>/numbers' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- `numberStatus` (array): Array of number statuses.
  - `phoneNumber` (string) (**requerido**): Phone Number whose status is being reported.
  - `numberStatus` (string) (**requerido**):  Valores: INVALID, DUPLICATE, DUPLICATE_IN_LIST, UNAVAILABLE.
  - `message` (string) (**requerido**): Message of the number add status.

### Ejemplo — respuesta 200
```json
{
  "numberStatus": [
    {
      "phoneNumber": "+2147891122",
      "numberStatus": "DUPLICATE",
      "message": "Invalid Number"
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