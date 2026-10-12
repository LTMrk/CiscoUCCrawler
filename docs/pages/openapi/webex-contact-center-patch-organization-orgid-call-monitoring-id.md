---
doc_id: webex-contact-center-patch-organization-orgid-call-monitoring-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PATCH
path: /organization/{orgid}/call-monitoring/{id}
operation_id: patchConfigCallMonitoring
tags: Call Monitoring Request
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-10-12T11:51:20.906178+00:00
---

# PATCH /organization/{orgid}/call-monitoring/{id}

**API:** Webex Contact Center
**Área:** Call Monitoring Request
**operationId:** `patchConfigCallMonitoring`

## Resumen
Partially update Call Monitoring by ID

## Descripción
Partially update Call Monitoring by ID in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) (**requerido**): Resource ID of the Call Monitoring.

## Cuerpo de la petición (application/json)
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): Name of the call monitoring schedule Long. max: 80.
- `timezone` (string) (**requerido**): (Optional) The time zone that you provision for your enterprise.
- `recurrence` (boolean) (**requerido**): Indicates if this is a recurring schedule
- `daysOfWeek` (array): Days of the week when the schedule is active
- `teams` (array) (**requerido**): List of teams for this schedule
  - `id` (string): Entity ID
  - `name` (string): Entity name
- `agentsAccessType` (string): Access type for agents - ALL or SPECIFIC
- `agents` (array): List of agents for this schedule when agentsAccessType is SPECIFIC
  - `id` (string): Agent/User ID
  - `userDetails` (object): User details containing name and email
    - `firstName` (string): First name of the user
    - `lastName` (string): Last name of the user
    - `email` (string): Email of the user
- `contactServiceQueues` (array) (**requerido**): List of contact service queues
  - `id` (string): Entity ID
  - `name` (string): Entity name
- `startTimestamp` (integer/int64) (**requerido**): Start timestamp of the schedule in epoch milliseconds (UTC)
- `endTimestamp` (integer/int64) (**requerido**): End timestamp of the schedule in epoch milliseconds (UTC)
- `userId` (string) (**requerido**): User ID of the supervisor who created/owns this schedule
- `userDetails` (object): User details containing name and email
  - `firstName` (string): First name of the user
  - `lastName` (string): Last name of the user
  - `email` (string): Email of the user
- `paused` (boolean) (**requerido**): Indicates if the schedule is paused
- `filtersCount` (object): Count of specific agents, teams, and contact service queues
  - `specificAgents` (integer/int32): Count of specific agents
  - `specificCsqs` (integer/int32): Count of specific contact service queues
  - `specificTeams` (integer/int32): Count of specific teams
- `createdTime` (integer/int64): This is the created time of the entity.
- `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

### Ejemplo — petición
```json
{
  "recurrence": true
}
```

## Ejemplo de invocación
```bash
curl -X PATCH '/organization/<orgid>/call-monitoring/<id>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"contactServiceQueues": [], "endTimestamp": 0, "name": "<name>", "paused": true, "recurrence": true, "startTimestamp": 0}'
```

## Respuestas correctas
**200**: OK
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): Name of the call monitoring schedule Long. max: 80.
- `timezone` (string) (**requerido**): (Optional) The time zone that you provision for your enterprise.
- `recurrence` (boolean) (**requerido**): Indicates if this is a recurring schedule
- `daysOfWeek` (array): Days of the week when the schedule is active
- `teams` (array) (**requerido**): List of teams for this schedule
  - `id` (string): Entity ID
  - `name` (string): Entity name
- `agentsAccessType` (string): Access type for agents - ALL or SPECIFIC
- `agents` (array): List of agents for this schedule when agentsAccessType is SPECIFIC
  - `id` (string): Agent/User ID
  - `userDetails` (object): User details containing name and email
    - `firstName` (string): First name of the user
    - `lastName` (string): Last name of the user
    - `email` (string): Email of the user
- `contactServiceQueues` (array) (**requerido**): List of contact service queues
  - `id` (string): Entity ID
  - `name` (string): Entity name
- `startTimestamp` (integer/int64) (**requerido**): Start timestamp of the schedule in epoch milliseconds (UTC)
- `endTimestamp` (integer/int64) (**requerido**): End timestamp of the schedule in epoch milliseconds (UTC)
- `userId` (string) (**requerido**): User ID of the supervisor who created/owns this schedule
- `userDetails` (object): User details containing name and email
  - `firstName` (string): First name of the user
  - `lastName` (string): Last name of the user
  - `email` (string): Email of the user
- `paused` (boolean) (**requerido**): Indicates if the schedule is paused
- `filtersCount` (object): Count of specific agents, teams, and contact service queues
  - `specificAgents` (integer/int32): Count of specific agents
  - `specificCsqs` (integer/int32): Count of specific contact service queues
  - `specificTeams` (integer/int32): Count of specific teams
- `createdTime` (integer/int64): This is the created time of the entity.
- `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

## Respuestas de error
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "400",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "400",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **401**: Unauthorized Operation
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "401",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "401",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **403**: Operation is forbidden
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "403",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "403",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **404**: Resource not found or URI is invalid
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "404",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "404",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "429",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "429",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **500**: An Unexpected Error Occurred
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "500",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "500",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs