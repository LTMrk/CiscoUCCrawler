---
doc_id: webex-cloud-calling-get-workspaces-workspaceid-features-numbers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /workspaces/{workspaceId}/features/numbers
operation_id: List numbers associated with a specific workspace
tags: Workspace Call Settings (1/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.373530+00:00
---

# GET /workspaces/{workspaceId}/features/numbers

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings (1/2)
**operationId:** `List numbers associated with a specific workspace`

## Resumen
List numbers associated with a specific workspace

## Descripción
List the PSTN phone numbers associated with a specific workspace, by ID, within the organization. Also shows the location and organization associated with the workspace.

Retrieving this list requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:workspaces_read`.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): List numbers for this workspace.
- `orgId` [query] (string): Workspace is in this organization. Only admin users of another organization (such as partners) can use this parameter as the default is the same organization as the token used to access the API.

## Ejemplo de invocación
```bash
curl -X GET '/workspaces/<workspaceId>/features/numbers' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `distinctiveRingEnabled` (boolean): Enables a distinctive ring pattern for the person.
- `phoneNumbers` (array) (**requerido**): List of phone numbers that are assigned to a person.
  - `primary` (boolean) (**requerido**): If `true` marks the phone number as primary.
  - `action` (string) (**requerido**): * `ADD` - Add action.  * `DELETE` - Delete action. Valores: ADD, DELETE.
  - `directNumber` (string) (**requerido**): Phone numbers that are assigned.
  - `extension` (string): Extension that is assigned.
  - `ringPattern` (string): * `NORMAL` - Normal incoming ring pattern.  * `LONG_LONG` - Incoming ring pattern of two long rings.  * `SHORT_SHORT_LONG` - Incoming ring pattern of two short rings, followed by a short ring.  * `SHORT_LONG_SHORT` - Incoming ring pattern of a short ring, followed by a long ring, followed by a short ring. Valores: NORMAL, LONG_LONG, SHORT_SHORT_LONG, SHORT_LONG_SHORT.

### Ejemplo — respuesta 200
```json
{
  "distinctiveRingEnabled": true,
  "phoneNumbers": [
    {
      "external": "+12055550001",
      "extension": "12211",
      "routingPrefix": "1234",
      "esn": "123412211",
      "primary": true
    },
    {
      "external": "+12055550002",
      "extension": "122",
      "routingPrefix": "1234",
      "esn": "123412211",
      "primary": false
    }
  ],
  "workspace": {
    "id": "Y2lzY29zcGFyazovL3VzL1BMQUNFLzg0MjkzOGQ1LTkyNzMtNGJjNi1hYTNhLTA1Njc3MmRiMzE2NQ"
  },
  "location": {
    "name": "MainOffice",
    "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2E4Mjg5NzIyLTFiODAtNDFiNy05Njc4LTBlNzdhZThjMTA5OA"
  },
  "organization": {
    "id": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9hNDVkNmNkYS1hZTVhLTQwYzMtYTdhZC01NjUwZmRkZGQ1M2M",
    "name": "Atlas_Test_CALL-1237"
  }
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