---
doc_id: webex-cloud-calling-get-telephony-config-queues-agents-availableagents
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/queues/agents/availableAgents
operation_id: getCallQueueAvailableAgents
tags: Features:  Call Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.266769+00:00
---

# GET /telephony/config/queues/agents/availableAgents

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `getCallQueueAvailableAgents`

## Resumen
Get Call Queue Available Agents

## Descripción
List all available users, workspaces, or virtual lines that can be assigned as call queue agents.

Available agents are users (excluding users with Webex Calling Standard license), workspaces, or virtual lines that can be assigned to a call queue. 
Calls from the call queue are routed to assigned agents based on configuration. 
An agent can be assigned to one or more call queues and can be managed by supervisors.

Retrieving this list requires a full, read-only or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [query] (string) (**requerido**): The location ID of the call queue. Temporary mandatory query parameter, used for performance reasons only and not a filter.
- `orgId` [query] (string): List available agents for this organization.
- `max` [query] (number): Limit the number of objects returned to this maximum count.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `name` [query] (string): Search based on name (user first and last name combination).
- `phoneNumber` [query] (string): Search based on number or extension.
- `order` [query] (string): Order the available agents according to the designated fields. Up to three comma-separated sort order fields may be specified. Available sort fields are: `userId`, `fname`, `firstname`, `lname`, `lastname`, `dn`, and `extension`. Sort order can be added together with each field using a hyphen, `-`. Available sort orders are: `asc`, and `desc`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/queues/agents/availableAgents?locationId=<locationId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `agents` (array) (**requerido**): Array of available agents.
  - `id` (string) (**requerido**): ID of a person, workspace or virtual line.
  - `lastName` (string): Last name of a person, workspace or virtual line.
  - `firstName` (string): First name of a person, workspace or virtual line.
  - `displayName` (string): Display name of a person, workspace or virtual line.
  - `type` (string) (**requerido**): Type of the person, workspace or virtual line.  * `PEOPLE` - Object is a user.  * `PLACE` - Object is a place.  * `VIRTUAL_LINE` - Object is a virtual line. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
  - `email` (string) (**requerido**): Email of a person, workspace or virtual line.
  - `hasCxEssentials` (boolean) (**requerido**): Person has the CX Essentials license.
  - `phoneNumbers` (array): List of phone numbers of a person, workspace or virtual line.
    - `external` (string): Phone number of a person, workspace or virtual line.
    - `extension` (string): Extension of a person, workspace or virtual line.

### Ejemplo — respuesta 200
```json
{
  "agents": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80NDVkMzMzMC1mNjE3LTExZWItOWQyZS01NzViODE3ZGE1NmE",
      "lastName": "Brown",
      "firstName": "John",
      "displayName": "John Brown",
      "type": "PEOPLE",
      "email": "john.brown@example.com",
      "hasCxEssentials": false,
      "phoneNumbers": [
        {
          "external": "+19075552859",
          "extension": "8080"
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