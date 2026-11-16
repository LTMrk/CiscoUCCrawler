---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-huntgroups
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/locations/{locationId}/huntGroups
operation_id: createHuntGroup
tags: Features:  Hunt Group
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:50.708836+00:00
---

# POST /telephony/config/locations/{locationId}/huntGroups

**API:** Webex Cloud Calling
**Área:** Features:  Hunt Group
**operationId:** `createHuntGroup`

## Resumen
Create a Hunt Group

## Descripción
Create new Hunt Groups for the given location.

Hunt groups can route incoming calls to a group of people, workspaces or virtual lines. You can even configure a pattern to route to a whole group.

Creating a hunt group requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Create the hunt group for the given location.
- `orgId` [query] (string): Create the hunt group for this organization.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Unique name for the hunt group.
- `phoneNumber` (string): Primary phone number of the hunt group. Either phone number or extension are required.
- `extension` (string): Primary phone extension of the hunt group. Either phone number or extension are required.
- `languageCode` (string): Language code.
- `firstName` (string): First name to be shown when calls are forwarded out of this hunt group. Defaults to `.`. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `lastName` (string): Last name to be shown when calls are forwarded out of this hunt group. Defaults to the phone number if set, otherwise defaults to call group name. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `timeZone` (string): Time zone for the hunt group.
- `callPolicies` (object) (**requerido**): Policy controlling how calls are routed to agents.
- `agents` (array) (**requerido**): People, workspaces and virtual lines that are eligible to  receive calls.
  - `id` (string) (**requerido**): ID of person, workspace or virtual line.
  - `weight` (string): Weight of person, workspace or virtual line. Only applied when call policy is `WEIGHTED`.
- `enabled` (boolean) (**requerido**): Whether or not the hunt group is enabled.
- `huntGroupCallerIdForOutgoingCallsEnabled` (boolean): Enable the hunt group to be used as the caller ID when the agent places outgoing calls. When set to true the hunt group's caller ID will be used.
- `directLineCallerIdName` (object): Settings for the direct line caller ID name to be shown for this hunt group.
- `dialByName` (string): The name to be used for dial by name functions.  Characters of `%`,  `+`, `\`, `"` and Unicode characters are not allowed.

### Ejemplo — petición
```json
{
  "name": "5714328359",
  "phoneNumber": "+15558675309",
  "extension": "7781",
  "firstName": "Hakim",
  "lastName": "Smith",
  "callPolicies": {
    "policy": "UNIFORM",
    "waitingEnabled": false,
    "groupBusyEnabled": true,
    "allowMembersToControlGroupBusyEnabled": true,
    "noAnswer": {
      "nextAgentEnabled": false,
      "nextAgentRings": 5,
      "forwardEnabled": false,
      "numberOfRings": 0,
      "destinationVoicemailEnabled": false
    },
    "busyRedirect": {
      "enabled": true,
      "destination": "7037344404",
      "destinationVoicemailEnabled": true
    },
    "businessContinuityRedirect": {
      "enabled": true,
      "destination": "7037344405",
      "destinationVoicemailEnabled": false
    }
  },
  "agents": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80YTc2ZmVmNC1mZjlmLTExZWItYWYwZC00M2YwZjY1NTdjYWI"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BMQUNFLzU1YjUyZThhLWZmOWYtMTFlYi05ZjRhLTAzZDY1NzdhYzg1Yg"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfTElORS9kZXRhMXZqeTBsQDY0OTQxMjk3LmludDEwLmJjbGQud2ViZXguY29t"
    }
  ],
  "enabled": true,
  "huntGroupCallerIdForOutgoingCallsEnabled": true,
  "directLineCallerIdName": {
    "selection": "CUSTOM_NAME",
    "customName": "Hakim Smith"
  },
  "dialByName": "Hakim Smith"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations/<locationId>/huntGroups' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "callPolicies": "<callPolicies>", "agents": [], "enabled": true}'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): ID of the newly created hunt group.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0hVTlRfR1JPVVAvYUhaaFpUTjJNRzh5YjBBMk5EazBNVEk1Tnk1cGJuUXhNQzVpWTJ4a0xuZGxZbVY0TG1OdmJRPT0"
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