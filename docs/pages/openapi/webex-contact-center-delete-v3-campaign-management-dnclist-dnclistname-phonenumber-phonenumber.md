---
doc_id: webex-contact-center-delete-v3-campaign-management-dnclist-dnclistname-phonenumber-phonenumber
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: DELETE
path: /v3/campaign-management/dncList/{dncListName}/phoneNumber/{phoneNumber}
operation_id: removePhoneNumberFromDncList
tags: DNC Management
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.218016+00:00
---

# DELETE /v3/campaign-management/dncList/{dncListName}/phoneNumber/{phoneNumber}

**API:** Webex Contact Center
**Área:** DNC Management
**operationId:** `removePhoneNumberFromDncList`

## Resumen
Remove Phone Number from DNC List

## Descripción
Removes a phone number from the specified Do Not Contact (DNC) list. This operation allows administrators to remove numbers that should no longer be blocked from receiving calls.

**Note:** Phone numbers must be URL-encoded and in E.164 format (e.g., +1234567890 for +1234567890). If the number doesn't exist in the list, a 404 error will be returned.

## Parámetros
- `dncListName` [path] (string) (**requerido**): The name of the DNC list to remove the phone number from. List names are case-sensitive and must be URL-encoded if they contain special characters.
- `phoneNumber` [path] (string) (**requerido**): The phone number to remove from the DNC list. Must be URL-encoded and in E.164 format (e.g., %2B1234567890 for +1234567890).

## Ejemplo de invocación
```bash
curl -X DELETE '/v3/campaign-management/dncList/<dncListName>/phoneNumber/<phoneNumber>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**204**: Phone number successfully removed from the DNC list. No content is returned.

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
  Ejemplo:
```json
{
  "code": 1001,
  "message": "Invalid pageSize. Allowed range is 1 to 100.",
  "trackingId": "GTWY_e6763c9a-71b2-4515-ad5b-89260f7f594b"
}
```
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
  Ejemplo:
```json
{
  "code": 401,
  "message": "Invalid or expired access token.",
  "trackingId": "GTWY_e6763c9a-71b2-4515-ad5b-89260f7f591"
}
```
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed. User lacks required permissions to manage DNC lists.
  Ejemplo:
```json
{
  "code": 403,
  "message": "Feature is not enabled for this organization.",
  "trackingId": "GTWY_e6763c9a-71b2-4515-ad5b-89260f7f592"
}
```
- **404**: Not Found: The specified DNC list does not exist, the phone number is not found in the list, or the user does not have access to it.
  Ejemplo:
```json
{
  "code": 1001,
  "message": "Phone number +1234567890 not found in DNC list 'corporate-dnc-list'",
  "trackingId": "WXC-12345-67893"
}
```
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
  Ejemplo:
```json
{
  "code": 429,
  "message": "Too many requests. Rate limit exceeded.",
  "trackingId": "GTWY_e6763c9a-71b2-4515-ad5b-89260f7f595"
}
```
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
  Ejemplo:
```json
{
  "code": 1006,
  "message": "An unexpected error occurred while processing your request.",
  "trackingId": "GTWY_e6763c9a-71b2-4515-ad5b-89260f7f596"
}
```
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
  Ejemplo:
```json
{
  "code": 502,
  "message": "The server received an invalid response from an upstream server.",
  "trackingId": "GTWY_e6763c9a-71b2-4515-ad5b-89260f7f597"
}
```
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
  Ejemplo:
```json
{
  "code": 503,
  "message": "Service is temporarily unavailable. Please try again later.",
  "trackingId": "GTWY_e6763c9a-71b2-4515-ad5b-89260f7f598"
}
```
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.
  Ejemplo:
```json
{
  "code": 504,
  "message": "The server did not receive a timely response from an upstream server.",
  "trackingId": "GTWY_e6763c9a-71b2-4515-ad5b-89260f7f599"
}
```

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs