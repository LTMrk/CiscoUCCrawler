---
doc_id: webex-broadworks-post-broadworks-workspaces
source: webex-openapi-specs/public-spec/webex-broadworks.json
api: Webex Broadworks Calling
method: POST
path: /broadworks/workspaces
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.285964+00:00
---

# POST /broadworks/workspaces

**API:** Webex Broadworks Calling
**Área:** BroadWorks Workspaces
**operationId:** `provisionBroadWorksWorkspace`

## Resumen
Provision a BroadWorks Workspace

## Descripción
Provision a new BroadWorks workspace for Cisco Webex services.

This API allows a Service Provider to provision a workspace for an existing customer.

## Cuerpo de la petición (application/json)
- `provisioningId` (string) **(requerido)**: Provisioning ID that defines how this workspace is to be provisioned for Cisco Webex Services. Each Customer Template will have their own unique Provisioning ID. This ID will be displayed under the chosen Customer Template on Cisco Webex Control Hub.
- `userId` (string) **(requerido)**: The user ID of the workspace on BroadWorks.
- `spEnterpriseId` (string) **(requerido)**: The Service Provider supplied unique identifier for the workspace's enterprise.
- `displayName` (string) **(requerido)**: The display name of the workspace.
- `primaryPhoneNumber` (string): The primary phone number configured against the workspace on BroadWorks.
- `extension` (string): The extension number configured against the workspace on BroadWorks.

### Ejemplo de petición
```json
{
  "provisioningId": "ZjViMzYxODctYzhkZC00NzI3LThiMmYtZjljNDQ3ZjI5MDQ2OjQyODVmNTk0LTViNTEtNDdiZS05Mzk2LTZjMzZlMmFkODNhNQ",
  "userId": "95547321@sp.com",
  "spEnterpriseId": "Reseller1+acme",
  "displayName": "Conference Room",
  "primaryPhoneNumber": "+1-240-555-1212",
  "extension": "51212"
}
```

## Respuestas
- **200**: OK
  - `provisioningId` (string): Provisioning ID that defines how this workspace is to be provisioned for Cisco Webex Services. Each Customer Template will have their own unique Provisioning ID. This ID will be displayed under the chosen Customer Template on Cisco Webex Control Hub.
  - `userId` (string): The user ID of the workspace on BroadWorks.
  - `spEnterpriseId` (string): The Service Provider supplied unique identifier for the workspace's enterprise.
  - `displayName` (string): The display name of the workspace.
  - `primaryPhoneNumber` (string): The primary phone number configured against the workspace on BroadWorks.
  - `extension` (string): The extension number configured against the workspace on BroadWorks.
  - `id` (string): A unique Cisco identifier for the workspace.
  - `created` (string): The date and time the workspace was provisioned.
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
