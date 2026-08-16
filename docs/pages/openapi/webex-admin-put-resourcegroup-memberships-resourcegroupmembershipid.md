---
doc_id: webex-admin-put-resourcegroup-memberships-resourcegroupmembershipid
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: PUT
path: /resourceGroup/memberships/{resourceGroupMembershipId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.158695+00:00
---

# PUT /resourceGroup/memberships/{resourceGroupMembershipId}

**API:** Webex Admin
**Área:** Resource Group Memberships
**operationId:** `Update a Resource Group Membership`

## Resumen
Update a Resource Group Membership

## Descripción
Updates a resource group membership, by ID.

Specify the resource group membership ID in the `resourceGroupMembershipId` URI parameter.

Only the `resourceGroupId` can be changed with this action. Resource group memberships with a `status` of "pending" cannot be updated. For more information about resource group memberships, see the [Managing Hybrid Services](/docs/api/guides/managing-hybrid-services-licenses#webex-resource-groups) guide.

## Parámetros
- `resourceGroupMembershipId` [path] (string) **(requerido)**: The unique identifier for the resource group membership.

## Cuerpo de la petición (application/json)
- `resourceGroupId` (string) **(requerido)**: The resource group ID.
- `licenseId` (string) **(requerido)**: The license ID.
- `personId` (string) **(requerido)**: The person ID.
- `personOrgId` (string) **(requerido)**: The organization ID of the person.
- `status` (string) **(requerido)**: The activation status of the resource group membership.  * `pending` - activation pending  * `activated` - activated  * `error` - error present Valores: pending, activated, error.

### Ejemplo de petición
```json
{
  "resourceGroupId": "Y2lzY29zcGFyazovL3VzL1JFU09VUkNFX0dST1VQL2RlZmF1bHQ",
  "licenseId": "Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvMWNjYmJjMTctZDYxNi00ZDc0LTg2NGItYjFmM2IwNzAxZmJhOk1TXzAzMDRjMDkzLTFjM2MtNDRlMC1iYjBhLWU1ZDE2NDM2NmQ1OQ",
  "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
  "personOrgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
  "status": "activated"
}
```

## Respuestas
- **200**: OK
  - `id` (string): A unique identifier for the resource group membership.
  - `resourceGroupId` (string): The resource group ID.
  - `licenseId` (string): The license ID.
  - `personId` (string): The person ID.
  - `personOrgId` (string): The organization ID of the person.
  - `status` (string): The activation status of the resource group membership.  * `pending` - activation pending  * `activated` - activated  * `error` - error present Valores: pending, activated, error.
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
