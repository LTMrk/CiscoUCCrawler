---
doc_id: webex-contact-center-post-v3-campaign-management-dnclist-dnclistname-phonenumber
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v3/campaign-management/dncList/{dncListName}/phoneNumber
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.974783+00:00
---

# POST /v3/campaign-management/dncList/{dncListName}/phoneNumber

**API:** Webex Contact Center
**Área:** DNC Management
**operationId:** `addPhoneNumberToDncList`

## Resumen
Add Phone Number to DNC List

## Descripción
Adds a phone number to the specified Do Not Contact (DNC) list. This operation helps ensure compliance with applicable rules & regulations by preventing outbound calls to specific numbers.

**Note:** Phone numbers must be in E.164 format (e.g., +1234567890). Duplicate entries will be rejected with a 409 error.

## Parámetros
- `dncListName` [path] (string) **(requerido)**: This is the Name of the DNC list to which you want to add a phone number. List names are case-sensitive and must be URL-encoded if they contain special characters.

## Cuerpo de la petición (application/json)
- `phoneNumber` (string) **(requerido)**: The phone number to add to the DNC list. Must be in E.164 format (e.g., +1234567890).
- `source` (string) **(requerido)**: The source or origin of the DNC entry. This helps track where the request originated from.
- `reason` (string): Optional reason for adding the phone number to the DNC list. This can help with compliance documentation.

## Respuestas
- **201**: Phone number successfully added to the DNC list
  - `phoneNumber` (string): The phone number in the DNC list, in E.164 format.
  - `source` (string): The source or origin of the DNC entry.
  - `addedDate` (string): The date and time when the phone number was added to the DNC list.
  - `addedBy` (string): The user or system that added the phone number to the DNC list.
  - `reason` (string): The reason for adding the phone number to the DNC list, if provided.
  - `lastModified` (string): The date and time when the DNC entry was last modified.
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed. User lacks required permissions to manage DNC lists.
- **404**: Not Found: The specified DNC list does not exist or the user does not have access to it.
- **409**: Conflict: The phone number already exists in the specified DNC list.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
