---
doc_id: webex-cloud-calling-put-telephony-config-callrecording-complianceannouncement
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/callRecording/complianceAnnouncement
operation_id: updateTheOrganizationComplianceAnnouncement
tags: Features: Call Recording
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.272811+00:00
---

# PUT /telephony/config/callRecording/complianceAnnouncement

**API:** Webex Cloud Calling
**Área:** Features: Call Recording
**operationId:** `updateTheOrganizationComplianceAnnouncement`

## Resumen
Update the Organization Compliance Announcement

## Descripción
Update the organization compliance announcement.

The Compliance Announcement feature interacts with the Call Recording feature, specifically with the playback of the start/stop announcement. When the compliance announcement is played to the PSTN party, and the PSTN party is connected to a party with call recording enabled, then the start/stop announcement is inhibited.

Updating the organization compliance announcement requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Update the compliance announcement setting from this organization.

## Cuerpo de la petición (application/json)
- `inboundPSTNCallsEnabled` (boolean): Flag to indicate whether the call recording START/STOP announcement is played to an inbound caller.
- `outboundPSTNCallsEnabled` (boolean): Flag to indicate whether the call recording START/STOP announcement is played to an outbound caller.
- `outboundPSTNCallsDelayEnabled` (boolean): Flag to indicate whether compliance announcement is played after a specified delay in seconds.
- `delayInSeconds` (number): Number of seconds to wait before playing the compliance announcement.
- `useCustomAnnouncementEnabled` (boolean): Flag to indicate whether to use the custom compliance announcement. If true it uses the organization's custom compliance announcement file, and if false default compliance announcement used.
- `audioAnnouncementFileId` (string): Unique identifier for the custom audio announcement file.

### Ejemplo — petición
```json
{
  "inboundPSTNCallsEnabled": false,
  "outboundPSTNCallsEnabled": false,
  "outboundPSTNCallsDelayEnabled": false,
  "delayInSeconds": 10,
  "useCustomAnnouncementEnabled": true,
  "audioAnnouncementFileId": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC82YTcwZWQ4MS1hZGM5LTQ4OWEtODhjOC0zMWI3ODllODQ1ODU"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/callRecording/complianceAnnouncement' \
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