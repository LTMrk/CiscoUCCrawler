---
doc_id: webex-cloud-calling-get-workspaces-workspaceid-capabilities
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /workspaces/{workspaceId}/capabilities
operation_id: getWorkspaceCapabilities
tags: Workspaces
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.396230+00:00
---

# GET /workspaces/{workspaceId}/capabilities

**API:** Webex Cloud Calling
**Área:** Workspaces
**operationId:** `getWorkspaceCapabilities`

## Resumen
Get Workspace Capabilities

## Descripción
Shows the capabilities for a workspace by ID.

Returns a set of capabilities, including whether or not the capability is supported by any device in the workspace, and if the capability is configured (enabled). For example for a specific capability like `occupancyDetection`, the API will return if the capability is supported and/or configured such that occupancy detection data will flow from the workspace (device) to the cloud. Specify the workspace ID in the `workspaceId` parameter in the URI.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): A unique identifier for the workspace.

## Ejemplo de invocación
```bash
curl -X GET '/workspaces/<workspaceId>/capabilities' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `capabilities` (object): The map of workspace capabilities.
  - `occupancyDetection` (object): Support and configured information for a workspace capability.
    - `supported` (boolean): Is the workspace capability supported or not.
    - `configured` (boolean): Is the workspace capability configured or not.
  - `presenceDetection` (object): Support and configured information for a workspace capability.
    - `supported` (boolean): Is the workspace capability supported or not.
    - `configured` (boolean): Is the workspace capability configured or not.
  - `ambientNoise` (object): Support and configured information for a workspace capability.
    - `supported` (boolean): Is the workspace capability supported or not.
    - `configured` (boolean): Is the workspace capability configured or not.
  - `soundLevel` (object): Support and configured information for a workspace capability.
    - `supported` (boolean): Is the workspace capability supported or not.
    - `configured` (boolean): Is the workspace capability configured or not.
  - `temperature` (object): Support and configured information for a workspace capability.
    - `supported` (boolean): Is the workspace capability supported or not.
    - `configured` (boolean): Is the workspace capability configured or not.
  - `airQuality` (object): Support and configured information for a workspace capability.
    - `supported` (boolean): Is the workspace capability supported or not.
    - `configured` (boolean): Is the workspace capability configured or not.
  - `relativeHumidity` (object): Support and configured information for a workspace capability.
    - `supported` (boolean): Is the workspace capability supported or not.
    - `configured` (boolean): Is the workspace capability configured or not.

### Ejemplo — respuesta 200
```json
{
  "capabilities": {
    "occupancyDetection": {
      "supported": true,
      "configured": true
    },
    "presenceDetection": {
      "supported": true,
      "configured": true
    },
    "ambientNoise": {
      "supported": true,
      "configured": true
    },
    "soundLevel": {
      "supported": true,
      "configured": true
    },
    "temperature": {
      "supported": true,
      "configured": true
    },
    "airQuality": {
      "supported": true,
      "configured": true
    },
    "relativeHumidity": {
      "supported": true,
      "configured": true
    }
  }
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