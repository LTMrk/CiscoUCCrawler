---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-huntgroups-huntgroupid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/huntGroups/{huntGroupId}
operation_id: getHuntGroup
tags: Features:  Hunt Group
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:50.709500+00:00
---

# GET /telephony/config/locations/{locationId}/huntGroups/{huntGroupId}

**API:** Webex Cloud Calling
**Área:** Features:  Hunt Group
**operationId:** `getHuntGroup`

## Resumen
Get Details for a Hunt Group

## Descripción
Retrieve Hunt Group details.

Hunt groups can route incoming calls to a group of people, workspaces or virtual lines. You can even configure a pattern to route to a whole group.

Retrieving hunt group details requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieve settings for a hunt group in this location.
- `huntGroupId` [path] (string) (**requerido**): Retrieve the settings for the hunt group with this identifier.
- `orgId` [query] (string): Retrieve the hunt group settings from this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/huntGroups/<huntGroupId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): A unique identifier for the hunt group.
- `name` (string) (**requerido**): Unique name for the hunt group.
- `enabled` (boolean) (**requerido**): Whether or not the hunt group is enabled.
- `phoneNumber` (string): Primary phone number of the hunt group.
- `extension` (string): Extension of the hunt group.
- `distinctiveRing` (boolean) (**requerido**): Whether or not the hunt group has the distinctive ring option enabled.
- `alternateNumbers` (array) (**requerido**): The alternate numbers feature allows you to assign multiple phone numbers or extensions to a hunt group. Each number will reach the same greeting and each menu will function identically to the main number. The alternate numbers option enables you to have up to ten (10) phone numbers ring into the hunt group.
  - `phoneNumber` (string) (**requerido**): Alternate phone number for the hunt group.
  - `ringPattern` (object): Ring pattern for when this alternate number is called. Only available when `distinctiveRing` is enabled for the hunt group.
- `language` (string): Language for hunt group.
- `languageCode` (string): Language code for hunt group.
- `firstName` (string): First name to be shown when calls are forwarded out of this hunt group. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `lastName` (string): Last name to be shown when calls are forwarded out of this hunt group. Defaults to phone number if set, otherwise defaults to call group name. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `timeZone` (string): Time zone for the hunt group.
- `callPolicies` (object) (**requerido**): Policy controlling how calls are routed to agents.
- `agents` (array) (**requerido**): People, workspaces and virtual lines that are eligible to  receive calls.
  - `id` (string) (**requerido**): ID of a person, workspace or virtual line.
  - `firstName` (string): First name of a person, workspace or virtual line.
  - `lastName` (string): Last name of a person, workspace or virtual line.
  - `phoneNumber` (string): Phone number of a person, workspace or virtual line.
  - `extension` (string): Extension of a person, workspace or virtual line.
  - `routingPrefix` (string): Routing prefix of location.
  - `esn` (string): Routing prefix + extension of a person or workspace.
  - `weight` (string): Weight of a person, workspace or virtual line. Only applied when call policy is `WEIGHTED`.
- `huntGroupCallerIdForOutgoingCallsEnabled` (boolean): Whether or not the hunt group can be used as the caller ID when the agent places outgoing calls.
- `directLineCallerIdName` (object): Settings for the direct line caller ID name to be shown for this hunt group.
- `dialByName` (string): The name to be used for dial by name functions.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0hVTlRfR1JPVVAvYUhaaFpUTjJNRzh5YjBBMk5EazBNVEk1Tnk1cGJuUXhNQzVpWTJ4a0xuZGxZbVY0TG1OdmJRPT0",
  "name": "hgnME3",
  "enabled": true,
  "extension": "079999",
  "distinctiveRing": true,
  "alternateNumbers": [],
  "language": "English",
  "languageCode": "en-US",
  "callingFirstName": "FirstName",
  "callingLastName": "hgnME3",
  "timeZone": "America/Los_Angeles",
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
      "systemMaxNumberOfRings": 20,
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
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80YTc2ZmVmNC1mZjlmLTExZWItYWYwZC00M2YwZjY1NTdjYWI",
      "firstName": "John",
      "lastName": "Doe",
      "type": "PEOPLE",
      "phoneNumber": "+15558675310",
      "extension": "7781",
      "routingPrefix": "123",
      "esn": "1237781"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BMQUNFLzg0YjQ1OTIyLWZmOWYtMTFlYi1hNGI4LTMzNjI3YmVkNjdiNQ",
      "firstName": "Alaska Office",
  ... (truncado)
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