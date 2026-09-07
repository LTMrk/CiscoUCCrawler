---
doc_id: webex-cloud-calling-get-telephony-config-cxessentials-agents-availableagents
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/cxEssentials/agents/availableAgents
operation_id: getAvailableAgents
tags: Features: Customer Assist
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-07T10:28:37.852974+00:00
---

# GET /telephony/config/cxEssentials/agents/availableAgents

**API:** Webex Cloud Calling
**Área:** Features: Customer Assist
**operationId:** `getAvailableAgents`

## Resumen
Get Available Agents

## Descripción
List eligible people who can be assigned as Customer Assist agents.

Returns people with a Webex Calling Professional license across all locations visible to the caller's authorization. Workspaces and virtual lines are not included.

Calls from call queues are routed to assigned agents based on configuration. An agent can be assigned to one or more call queues and can be managed by supervisors.

Retrieving this list requires a full, read-only or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [query] (string) (**requerido**): The location ID of the call queue. Temporary mandatory query parameter, used for performance reasons only and not a filter.
- `orgId` [query] (string): List available agents for this organization. If omitted, uses the organization associated with the OAuth token.
- `hasCxEssentials` [query] (boolean): Filter agents by Customer Assist license status. When `true`, returns only agents with Customer Assist license. When `false`, returns only agents with Customer Experience Basic license. When omitted, returns all eligible agents regardless of license type.
- `max` [query] (integer): Limit the number of objects returned to this maximum count. Por defecto: 2000.
- `start` [query] (integer): Start at the zero-based offset in the list of matching objects. Por defecto: 0.
- `name` [query] (array): Filter agents by name. Supports partial matching. Multiple values can be provided to search for agents matching any of the specified names.
- `phoneNumbers` [query] (array): Filter agents by phone number. Supports partial matching. Multiple values can be provided to search for agents matching any of the specified phone numbers.
- `order` [query] (string): Sort order for the results. Supported fields are `firstName`, `lastName`, `displayName`, and `extension`. Use `asc` or `desc` suffix to specify direction (e.g., `lastName asc`). Default is `lastName asc`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/cxEssentials/agents/availableAgents?locationId=<locationId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `agents` (array) (**requerido**): Array of available agents.
  - `id` (string) (**requerido**): ID of a person.
  - `lastName` (string): Last name of a person.
  - `firstName` (string): First name of a person.
  - `displayName` (string): Display name of a person.
  - `type` (string) (**requerido**): Type of the person.  * `PEOPLE` - Object is a user. Valores: PEOPLE.
  - `email` (string) (**requerido**): Email of a person.
  - `hasCxEssentials` (boolean) (**requerido**): Person has the CX Essentials license.
  - `phoneNumbers` (array): List of phone numbers of a person.
    - `external` (string): Phone number of a person.
    - `extension` (string): Extension of a person.

### Ejemplo — respuesta 200
```json
{
  "agents": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80YzFjOWE2YS1jYjZiLTRjYjItOWJkYi02YjkyZTA1ZTI4ZmY",
      "lastName": "Smith",
      "firstName": "John",
      "displayName": "John Smith",
      "type": "PEOPLE",
      "email": "john.smith@example.com",
      "hasCxEssentials": true,
      "phoneNumbers": [
        {
          "external": "+12165553518",
          "extension": "5024"
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