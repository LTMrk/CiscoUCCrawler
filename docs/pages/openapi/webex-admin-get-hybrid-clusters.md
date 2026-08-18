---
doc_id: webex-admin-get-hybrid-clusters
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /hybrid/clusters
operation_id: List Hybrid Clusters
tags: Hybrid Clusters
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.565859+00:00
---

# GET /hybrid/clusters

**API:** Webex Admin
**Área:** Hybrid Clusters
**operationId:** `List Hybrid Clusters`

## Resumen
List Hybrid Clusters

## Descripción
List hybrid clusters for an organization. If no `orgId` is specified, the default is the organization of the authenticated user.

Only an admin auth token with the `spark-admin:hybrid_clusters_read` scope can list clusters.

## Parámetros
- `orgId` [query] (string): List hybrid clusters in this organization. If an organization is not specified, the organization of the caller will be used.

## Ejemplo de invocación
```bash
curl -X GET '/hybrid/clusters' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): An array of hybrid cluster objects.
  - `id` (string): A unique identifier for the cluster.
  - `orgId` (string): The ID of the organization to which this hybrid cluster belongs.
  - `name` (string): The name of the cluster.
  - `resourceGroupId` (string): The ID of the resource group this cluster belongs to.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "Y2lZY76123abbb",
      "orgId": "Y2lzY29zcGFyazovL3",
      "name": "EMEA Oslo 1",
      "resourceGroupId": "Y2lzY29zcGFyazovL3"
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
The Webex Admin APIs provide comprehensive programmatic access to administrative functions for managing Webex organizations, users, licenses, and settings. These APIs enable automation of user provisioning, license assignment, compliance management, and audit event retrieval. Administrators can integrate with enterprise identity systems, enforce security policies, monitor usage, and streamline onboarding/offboarding processes. The APIs support granular control over organizational resources, making them ideal for large-scale deployments and custom admin tooling.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs