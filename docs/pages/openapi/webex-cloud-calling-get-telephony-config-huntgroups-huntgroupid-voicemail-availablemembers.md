---
doc_id: webex-cloud-calling-get-telephony-config-huntgroups-huntgroupid-voicemail-availablemembers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/huntGroups/{huntGroupId}/voicemail/availableMembers
operation_id: readAvailableMembersForHuntGroupVoicemail
tags: Features:  Hunt Group
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-09T12:44:28.077642+00:00
---

# GET /telephony/config/huntGroups/{huntGroupId}/voicemail/availableMembers

**API:** Webex Cloud Calling
**Área:** Features:  Hunt Group
**operationId:** `readAvailableMembersForHuntGroupVoicemail`

## Resumen
Read Available Members for a Hunt Group Voicemail

## Descripción
Read Available Members for a Hunt Group Voicemail.

The voicemail feature transfers callers to voicemail based on your settings. You can then retrieve voice messages via Voicemail. Voicemail audio is sent in Waveform Audio File Format, `.wav`, format. Optionally, notifications can be sent via email. These notifications will not include the voicemail files.

Retrieving available members for a hunt group's voicemail requires a full, user, read-only or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `huntGroupId` [path] (string) (**requerido**): Unique identifier for the Hunt Group.
- `orgId` [query] (string): Organization ID. Only required when the admin operates on behalf of a different organization.
- `max` [query] (integer): Specifies the maximum number of records that you want to fetch. Default is 2000, maximum is 2000.
- `start` [query] (integer): Zero-based offset from the first result. For example, start=0 returns the first page of results, start=2000 returns the second page if max is 2000.
- `name` [query] (string): Search (Contains) based on member name.
- `phoneNumber` [query] (string): Search (Contains) based on number.
- `extension` [query] (string): Search (Contains) based on extension.
- `locationId` [query] (string): Unique identifier for the location.
- `includeAgentsOnly` [query] (boolean): When `true`, only return members who are assigned as agents to the hunt group.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/huntGroups/<huntGroupId>/voicemail/availableMembers' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `members` (array) (**requerido**): Array of available members (people / workspaces) for Hunt Group Voicemail. Results are paginated using the `max` and `start` query parameters.
  - `id` (string) (**requerido**): Unique identifier for the member.
  - `firstName` (string): First name of a person or workspace.
  - `lastName` (string): Last name of a person or workspace.
  - `displayName` (string): Display name of a person or workspace.
  - `phoneNumber` (string): Phone Number of a person or workspace.
  - `extension` (string): Extension of a person or workspace.
  - `type` (string) (**requerido**): Type of member.  - `PEOPLE` - Member is a person. - `PLACE` - Member is a workspace. Valores: PEOPLE, PLACE.
  - `hasCxEssentials` (boolean) (**requerido**): Indicates whether the member has the Customer Assist license.
  - `location` (object): Location details of the member.
    - `id` (string) (**requerido**): Unique identifier for the location.
    - `name` (string) (**requerido**): Name of the location.

### Ejemplo — respuesta 200
```json
{
  "members": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xMWEzZjk5MC1hNjg5LTQ3N2QtYmU2Yi03MTIwMDI1ZDhhYmI",
      "firstName": "John",
      "lastName": "Doe",
      "displayName": "John Doe",
      "phoneNumber": "+12345354678",
      "extension": "5453",
      "type": "PEOPLE",
      "hasCxEssentials": true,
      "location": {
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzMxMTYx",
        "name": "Main Office"
      }
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