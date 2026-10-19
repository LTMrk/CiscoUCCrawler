---
doc_id: webex-contact-center-post-v1-monitor
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/monitor
operation_id: createMonitoringRequest
tags: Call Monitoring
deprecated: true
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-10-19T09:48:26.422445+00:00
---

# POST /v1/monitor

> **ENDPOINT DEPRECADO.** No usar en integraciones nuevas.

**API:** Webex Contact Center
**Área:** Call Monitoring
**operationId:** `createMonitoringRequest`

## Resumen
Create Monitoring Request

## Descripción
Creates a monitoring request for an ongoing call or the next successful inbound or outbound call. Requires the 'cloud-contact-center:pod_conv' scope and either the 'cjp.supervisor' role with a supervisor profile or, when Licensed Administrator access is enabled, the 'cjp.admin' or 'id_full_admin' role together with the 'cjp.premium_agent' role and an administrator profile. When Licensed Administrator access is enabled, contact-center access and supervisor capabilities must also be enabled. The applicable Call Monitoring profile permissions and resource access are required. When Continuous Scheduled Monitoring is enabled, ad hoc and continuous requests are rejected; use POST /v2/monitor/{taskId} for mid-call monitoring.

## Cuerpo de la petición (application/json)
- `id` (string) (**requerido**): The id represents the unique request id with which the Monitoring Request will be created, maximum length 36 characters.
- `monitorType` (string) (**requerido**): It represents the type of the monitoring request. Only allowed type is ```midcall```
- `taskId` (string/UUID): The unique ID representing the task that needs to be monitored. Mandatory for ```midcall``` type.
- `queueIds` (array): If the call is routed to an agent and the agent is assigned to a queue, the queueId can be entered here to initiate a successful call monitoring request for that particular queue, maximum length of each queue is 36 characters and maximum number of queueIds 250.
- `teams` (array): If the call is routed to an agent and the agent is assigned to a team, the teamId can be entered here to initiate a successful monitoring request for that particular team, maximum length of each team is 36 characters and maximum number of teams 100.
- `sites` (array): If the call is routed to an agent and the agent is assigned to a site, the siteId can be entered here to initiate a successful monitoring request for that particular site, maximum length of each site is 36 characters and the maximum number of sites 20.
- `agents` (array): Enter the agentId to monitor a particular agent to whom the call is being assigned, maximum length of each agent is 36 characters and the maximum number of agents is 500.
- `trackingId` (string/UUID): An unique id to keep a track of events occurring during the call
- `invisibleMode` (boolean): This allows the supervisor to obfuscate their details from Team Performance Widget panel. Set ```true``` inorder to activate this mode

## Ejemplo de invocación
```bash
curl -X POST '/v1/monitor' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"id": "<id>", "monitorType": "<monitorType>"}'
```

## Respuestas correctas
**202**: The create request was accepted for processing

## Respuestas de error
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **412**: Precondition Failed
- **500**: Internal Server Error
- **503**: Service Unavailable

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs