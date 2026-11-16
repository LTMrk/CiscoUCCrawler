---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-huntgroups-huntgroupid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/huntGroups/{huntGroupId}
operation_id: updateHuntGroup
tags: Features:  Hunt Group
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:50.709840+00:00
---

# PUT /telephony/config/locations/{locationId}/huntGroups/{huntGroupId}

**API:** Webex Cloud Calling
**Área:** Features:  Hunt Group
**operationId:** `updateHuntGroup`

## Resumen
Update a Hunt Group

## Descripción
Update the designated Hunt Group.

Hunt groups can route incoming calls to a group of people, workspaces or virtual lines. You can even configure a pattern to route to a whole group.

Updating a hunt group requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Update the hunt group for this location.
- `huntGroupId` [path] (string) (**requerido**): Update settings for the hunt group with the matching ID.
- `orgId` [query] (string): Update hunt group settings from this organization.

## Cuerpo de la petición (application/json)
- `enabled` (boolean): Whether or not the hunt group is enabled.
- `name` (string): Unique name for the hunt group.
- `phoneNumber` (string): Primary phone number of the hunt group.
- `extension` (string): Primary phone extension of the hunt group.
- `distinctiveRing` (boolean): Whether or not the hunt group has the distinctive ring option enabled.
- `alternateNumbers` (array): The alternate numbers feature allows you to assign multiple phone numbers or extensions to a hunt group. Each number will reach the same greeting and each menu will function identically to the main number. The alternate numbers option enables you to have up to ten (10) phone numbers ring into the hunt group.
  - `phoneNumber` (string) (**requerido**): Alternate phone number for the hunt group.
  - `ringPattern` (object): Ring pattern for when this alternate number is called. Only available when `distinctiveRing` is enabled for the hunt group.
- `languageCode` (string): Language code.
- `firstName` (string): First name to be shown when calls are forwarded out of this hunt group. Defaults to `.`. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `lastName` (string): Last name to be shown when calls are forwarded out of this hunt group. Defaults to the phone number if set, otherwise defaults to call group name. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `timeZone` (string): Time zone for the hunt group.
- `callPolicies` (object): Policy controlling how calls are routed to agents.
- `agents` (array): People, workspaces and virtual lines that are eligible to  receive calls.
  - `id` (string) (**requerido**): ID of person, workspace or virtual line.
  - `weight` (string): Weight of person, workspace or virtual line. Only applied when call policy is `WEIGHTED`.
- `huntGroupCallerIdForOutgoingCallsEnabled` (boolean): Enable the hunt group to be used as the caller ID when the agent places outgoing calls. When set to true the hunt group's caller ID will be used.
- `directLineCallerIdName` (object): Settings for the direct line caller ID name to be shown for this hunt group.
- `dialByName` (string): Sets or clears the name to be used for dial by name functions. To clear the `dialByName`, the attribute must be set to null or empty string. Characters of `%`,  `+`, `\`, `"` and Unicode characters are not allowed.

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
      "destinationVoicemailEnabled": false
    },
    "businessContinuityRedirect": {
      "enabled": true,
      "destination": "7037344405",
      "destinationVoicemailEnabled": false
    }
  },
  "agents": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS82YTUwMDk1YS1mZjlmLTExZWItODA2NS04ZjhkOWIxNmIzOTQ"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BMQUNFLzg0YjQ1OTIyLWZmOWYtMTFlYi1hNGI4LTMzNjI3YmVkNjdiNQ"
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
curl -X PUT '/telephony/config/locations/<locationId>/huntGroups/<huntGroupId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**204**: No Content

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