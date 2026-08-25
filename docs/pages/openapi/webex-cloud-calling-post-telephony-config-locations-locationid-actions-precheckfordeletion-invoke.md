---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-actions-precheckfordeletion-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/locations/{locationId}/actions/precheckForDeletion/invoke
operation_id: Safe Delete Check Before Disabling Calling Location
tags: Location Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.513745+00:00
---

# POST /telephony/config/locations/{locationId}/actions/precheckForDeletion/invoke

**API:** Webex Cloud Calling
**Área:** Location Call Settings
**operationId:** `Safe Delete Check Before Disabling Calling Location`

## Resumen
Safe Delete Check Before Disabling a Location for Webex Calling

## Descripción
Performs a safe delete check operation to identify any issues that would prevent the calling location from being disabled. This API helps identify resources that need to be addressed before a calling location can be successfully disabled.

This API requires a full administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Unique identifier for the location to be checked.
- `orgId` [query] (string): Organization ID for which the safe delete check operation is being performed.

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations/<locationId>/actions/precheckForDeletion/invoke' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `locationDeleteStatus` (object):
- `blocking` (object): Factors that completely block disabling a calling location.
  - `lastLocation` (boolean): Indicates if this is the last calling location in the organization.
  - `trunksInUseCount` (integer): Number of trunks in use at this location.
  - `usersInUseCount` (integer): Number of users in use at this location.
  - `workspacesInUseCount` (integer): Number of workspaces in use at this location.
  - `virtualLineInUseCount` (integer): Number of virtual lines in use at this location.
  - `numbersOrderPending` (boolean): Indicates if there are pending number orders for this location.
- `nonBlocking` (object): Non blocking reasons for disabling a calling location that do not prevent the operation from proceeding
  - `numbersPresent` (boolean): Indicates if there are phone numbers at this location.
- `blockingUnlessForced` (object): Reasons that block disabling a calling location
  - `nonUserEntitiesInUse` (boolean): Indicates if there are non-user entities in use at this location that would block disabling unless force is applied.
  - `trunksCount` (integer): Total number of trunks at this location.

### Ejemplo — respuesta 200
```json
{
  "locationDeleteStatus": "FORCE_REQUIRED",
  "blocking": {
    "lastLocation": false,
    "trunksInUseCount": 0,
    "usersInUseCount": 0,
    "workspacesInUseCount": 0,
    "virtualLineInUseCount": 0,
    "numbersOrderPending": false
  },
  "nonBlocking": {
    "numbersPresent": true
  },
  "blockingUnlessForced": {
    "nonUserEntitiesInUse": true,
    "trunksCount": 2
  }
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs