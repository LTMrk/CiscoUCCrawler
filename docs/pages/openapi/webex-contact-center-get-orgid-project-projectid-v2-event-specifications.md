---
doc_id: webex-contact-center-get-orgid-project-projectid-v2-event-specifications
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /{orgId}/project/{projectId}/v2/event-specifications
operation_id: listEventSpecifications
tags: Events
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.146819+00:00
---

# GET /{orgId}/project/{projectId}/v2/event-specifications

**API:** Webex Contact Center
**Área:** Events
**operationId:** `listEventSpecifications`

## Resumen
List Event Specifications

## Descripción
List the event types available for use in `event_flows[]`. Each entry describes the event name, payload schema, and any contextual metadata bound when the event fires.

Scope: `cjp:config_read`

## Parámetros
- `orgId` [path] (string) (**requerido**): Organization ID.
- `projectId` [path] (string) (**requerido**): Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.

## Ejemplo de invocación
```bash
curl -X GET '/<orgId>/project/<projectId>/v2/event-specifications' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Available event specifications, plus ready-to-paste quick-start snippets.
- `specifications` (array): The available event specifications.
  - `eventSpecificationName` (string): Event specification name. Must be used verbatim as `FlowV2EventFlow.event`.
  - `eventSourceName` (string): Name of the event source the specification belongs to.
  - `eventClassificationName` (string): Name of the event classification the specification belongs to.
- `quick_start` (object): Ready-to-paste start-node and global-error snippets. The backend resolves IDs from the supplied names.

### Ejemplo — respuesta 200
```json
{
  "specifications": [
    {
      "eventSourceName": "WebexContactCenter",
      "eventClassificationName": "VoiceInteractions",
      "eventSpecificationName": "ContactStartWorkflow"
    },
    {
      "eventSourceName": "WebexContactCenter",
      "eventClassificationName": "VoiceInteractions",
      "eventSpecificationName": "GlobalErrorHandling"
    }
  ],
  "quick_start": {
    "description": "Copy snippets directly into flow; backend resolves IDs from names.",
    "voice_flow_start_node": {
      "eventSourceName": "WebexContactCenter",
      "eventClassificationName": "VoiceInteractions",
      "eventSpecificationName": "ContactStartWorkflow"
    },
    "global_error_eventflow": {
      "eventSourceName": "WebexContactCenter",
      "eventClassificationName": "VoiceInteractions",
      "eventSpecificationName": "GlobalErrorHandling"
    }
  }
}
```

## Respuestas de error
- **401**: Unauthorized.
- **403**: Forbidden.
- **404**: Not Found.
- **429**: Too Many Requests.

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs