---
doc_id: webex-messaging-get-hds-organizations-organizationid
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
api_version: 1.0.0
method: GET
path: /hds/organizations/{organizationId}
operation_id: getHDSOrganizationDetails
tags: Hybrid Data Security
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.804199+00:00
---

# GET /hds/organizations/{organizationId}

**API:** Webex Messaging
**Área:** Hybrid Data Security
**operationId:** `getHDSOrganizationDetails`

## Resumen
Get organization details

## Descripción
Retrieve details for an Hybrid Data Security organization, such as the organization name, type of organization.
To obtain the Organization ID needed for this API, use the [Organizations API](</docs/api/v1/organizations/list-organizations>)

## Parámetros
- `organizationId` [path] (string) (**requerido**): Unique ID of the Hybrid Data Security organization.

## Ejemplo de invocación
```bash
curl -X GET '/hds/organizations/<organizationId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Ok
- `orgId` (string): Unique ID of the organization.
- `orgName` (string): Name of the organization.
- `orgType` (string): Type of the organization.
- `orgMode` (string): Mode of the organization.

### Ejemplo — respuesta 200
```json
{
  "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8yYzNjOWY5NS03M2Q5LTQ0NjAtYTY2OC0wNDcxNjJmZjFiYWQ",
  "orgName": "HDS_Demo",
  "orgType": "Single Tenant",
  "orgMode": "Production"
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or could not be processed. An accompanying error message will provide more details.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request was understood, but it has been refused or access is not allowed.
- **404**: Not Found: The requested URI is invalid, or the resource requested (such as a user) does not exist. This response is also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP method that is not supported.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **410**: Gone: The requested resource is no longer available.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type, or with a media type that is not supported.
- **423**: Locked: The requested resource is temporarily unavailable. A Retry-After header may be present to indicate how many seconds you should wait before attempting the request again.
- **428**: Precondition Required: The file(s) cannot be scanned for malware and must be force downloaded.
- **429**: Too Many Requests: Too many requests have been sent in a given period of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, please contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond in time. If your query uses the max parameter, please try reducing its value.

## Contexto de la API
The Webex Messaging APIs offer robust programmatic access to messaging features within Webex, including sending and receiving messages, managing spaces, memberships, attachments, and moderating content. These APIs enable integration with bots, workflow automation, notification systems, and custom messaging solutions to enhance team collaboration and productivity. Use cases include building chatbots, integrating with ticketing or alerting platforms, automating onboarding flows, and creating custom collaboration experiences tailored to business needs.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs