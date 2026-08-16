---
doc_id: webex-contact-center-delete-v3-campaign-management-dnclist-dnclistname-phonenumber-phonenumber
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: DELETE
path: /v3/campaign-management/dncList/{dncListName}/phoneNumber/{phoneNumber}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.974959+00:00
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
- `dncListName` [path] (string) **(requerido)**: The name of the DNC list to remove the phone number from. List names are case-sensitive and must be URL-encoded if they contain special characters.
- `phoneNumber` [path] (string) **(requerido)**: The phone number to remove from the DNC list. Must be URL-encoded and in E.164 format (e.g., %2B1234567890 for +1234567890).

## Respuestas
- **204**: Phone number successfully removed from the DNC list. No content is returned.
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed. User lacks required permissions to manage DNC lists.
- **404**: Not Found: The specified DNC list does not exist, the phone number is not found in the list, or the user does not have access to it.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
