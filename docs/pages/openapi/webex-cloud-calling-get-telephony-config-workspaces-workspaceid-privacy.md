---
doc_id: webex-cloud-calling-get-telephony-config-workspaces-workspaceid-privacy
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/workspaces/{workspaceId}/privacy
operation_id: Retrieve Privacy Settings for a Workspace
tags: Workspace Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.199043+00:00
---

# GET /telephony/config/workspaces/{workspaceId}/privacy

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings (2/2)
**operationId:** `Retrieve Privacy Settings for a Workspace`

## Resumen
Retrieve Privacy Settings for a Workspace

## Descripción
Retrieve Privacy Settings for a Workspace.

The privacy feature enables the Workspaces line to be monitored by others and determine if they can be reached by Auto Attendant services.

This API requires a full, read-only or location administrator auth token with a scope of `spark-admin:workspaces_read` scope to read workspace settings.

**NOTE**: This API is only available for professional licensed workspaces.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Unique identifier for the workspace.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/workspaces/<workspaceId>/privacy' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `aaExtensionDialingEnabled` (boolean): When `true` auto attendant extension dialing is enabled.
- `aaNamingDialingEnabled` (boolean): When `true` auto attendant dialing by first or last name is enabled.
- `enablePhoneStatusDirectoryPrivacy` (boolean): When `true` phone status directory privacy is enabled.
- `enablePhoneStatusPickupBargeInPrivacy` (boolean): When `true` privacy is enforced for call pickup and barge-in. Only members specified by `monitoringAgents` can pickup or barge-in on the call.
- `monitoringAgents` (array): List of people that are being monitored.
  - `id` (string): Unique identifier of the person.
  - `lastName` (string): Last name of the person.
  - `firstName` (string): First name of the person.
  - `displayName` (string): Display name of the person.
  - `type` (string): * `PEOPLE` - Person or list of people.  * `PLACE` - Workspace that is not assigned to a specific person such as for a shared device in a common area.  * `VIRTUAL_LINE` - Virtual line or list of virtual lines. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
  - `email` (string): Email address of the person.
  - `numbers` (array): List of phone numbers of the person.
    - `external` (string): External phone number of the person.
    - `extension` (string): Extension number of the person.
    - `routingPrefix` (string): Routing prefix of location.
    - `esn` (string): Routing prefix + extension of a person or workspace.
    - `primary` (boolean): If `true`, specifies whether the phone number is primary number.

### Ejemplo — respuesta 200
```json
{
  "aaExtensionDialingEnabled": true,
  "aaNamingDialingEnabled": true,
  "enablePhoneStatusDirectoryPrivacy": true,
  "enablePhoneStatusPickupBargeInPrivacy": true,
  "monitoringAgents": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS82MWU3MDlkNy1hM2IxLTQ2MDctOTBiOC04NmE5MDgxYWFkNmE",
      "lastName": "Little",
      "firstName": "Alice",
      "displayName": "Alice Little",
      "type": "PEOPLE",
      "email": "alice@example.com",
      "numbers": [
        {
          "external": "+19845551088",
          "extension": "1088",
          "routingPrefix": "1234",
          "esn": "12341088",
          "primary": true
        }
      ]
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jMGMxYmFlNi1iMDU4LTRkYzItYmMyZC01NDYwOTFlOTkwOTk",
      "lastName": "Doe",
      "firstName": "John",
      "displayName": "John Doe",
      "type": "PEOPLE",
      "email": "johnDoe@gmail.com",
      "numbers": [
        {
          "extension": "25789",
          "esn": "25789",
          "primary": true
        }
      ]
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