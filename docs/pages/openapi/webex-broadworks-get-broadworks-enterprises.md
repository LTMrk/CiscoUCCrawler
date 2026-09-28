---
doc_id: webex-broadworks-get-broadworks-enterprises
source: webex-openapi-specs/public-spec/webex-broadworks.json
api: Webex Broadworks Calling
api_version: 1.0.0
method: GET
path: /broadworks/enterprises
operation_id: List BroadWorks Enterprises
tags: BroadWorks Enterprises
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-27T10:51:18.911022+00:00
---

# GET /broadworks/enterprises

**API:** Webex Broadworks Calling
**Área:** BroadWorks Enterprises
**operationId:** `List BroadWorks Enterprises`

## Resumen
List BroadWorks Enterprises

## Descripción
List the provisioned enterprises for a Service Provider. This API also lets a Service Provider search for their provisioned enterprises on Webex. A search on enterprises can be performed by either a full or partial enterprise identifier.

## Parámetros
- `spEnterpriseId` [query] (string): The Service Provider supplied unique identifier for the subscriber's enterprise.
- `startsWith` [query] (string): The starting string of the enterprise identifiers to match against.
- `max` [query] (number): Limit the number of enterprises returned in the search, up to 1000. Por defecto: 100.

## Ejemplo de invocación
```bash
curl -X GET '/broadworks/enterprises' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string): A unique Cisco identifier for the enterprise.
- `orgId` (string): The Organization ID of the enterprise on Webex.
- `provisioningId` (string): The Provisioning ID associated with the enterprise.
- `spEnterpriseId` (string): The Service Provider supplied unique identifier for the subscriber's enterprise.
- `broadworksDirectorySync` (object): BroadWorks Directory sync
  - `enableDirSync` (boolean): The toggle to enable/disable directory sync.
  - `directorySyncStatus` (object): Directory sync status
    - `lastSyncStartTime` (string): The start date and time of the last sync.
    - `lastSyncEndTime` (string): The end date and time of the last sync.
    - `syncStatus` (string): The sync status of the enterprise.
    - `usersAdded` (number): The number of users added to Common Identity (CI) in this sync.
    - `usersUpdated` (number): The number of users updated in Common Identity (CI) in this sync.
    - `usersDeleted` (number): The number of users deleted from Common Identity (CI) in this sync.
    - `machinesAdded` (number): The number of machines added to Common Identity (CI) in this sync.
    - `machinesUpdated` (number): The number of machines updated in Common Identity (CI) in this sync.
    - `machinesDeleted` (number): The number of machines deleted from Common Identity (CI) in this sync.
    - `totalExternalUsersInCI` (number): The number of total external users that have been added to CI across all syncs.
    - `totalExternalMachinesInCI` (number): The number of total external machines that have been added to Common Identity (CI) across all syncs.
    - `lastSuccessfulSyncTime` (string): The date and time of the last successful sync.
    - `lastSyncTrackingId` (string): Unique tracking identifier.
    - `errors` (array): List of errors that occurred during that last attempt to sync this BroadWorks enterprise. This list captures errors that occurred during *directory sync* of the BroadWorks enterprise, *after* the API has been accepted and 200 OK response returned. Any errors that occur during initial API request validation will be captured directly in error response with appropriate HTTP status code.
      - `errorCode` (number): An error code that identifies the reason for the error
      - `description` (string): A textual representation of the error code.
    - `userContactsAdded` (number): The number of user contacts added to Contact service in this sync.
    - `userContactsUpdated` (number): The number of user contacts updated in Contact service in this sync.
    - `userContactsDeleted` (number): The number of user contacts deleted from Contact service in this sync.
    - `orgContactsAdded` (number): The number of org contacts added to Contact service in this sync.
    - `orgContactsUpdated` (number): The number of org contacts updated in Contact service in this sync.
    - `orgContactsDeleted` (number): The number of org contacts deleted from Contact service in this sync.
    - `totalUserContactsInContactService` (number): The total number of user contacts in Contact service.
    - `totalOrgContactsInContactService` (number): The total number of org contacts in Contact service.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0VOVEVSUFJJU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh",
      "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
      "spEnterpriseId": "Reseller1+acme",
      "provisioningId": "ZjViMzYxODctYzhkZC00NzI3LThiMmYtZjljNDQ3ZjI5MDQ2OjQyODVmNTk0LTViNTEtNDdiZS05Mzk2LTZjMzZlMmFkODNhNQ",
      "broadworksDirectorySync": {
        "enableDirSync": true,
        "directorySyncStatus": {
          "lastSyncStartTime": "2021-04-07T15:26:40.704911Z",
          "lastSyncEndTime": "2021-04-07T15:26:42.695060Z",
          "syncStatus": "COMPLETE",
          "usersAdded": 0,
          "usersUpdated": 0,
          "usersDeleted": 0,
          "machinesAdded": 0,
          "machinesUpdated": 0,
          "machinesDeleted": 0,
          "totalExternalUsersInCI": 2,
          "totalExternalMachinesInCI": 1,
          "lastSyncTrackingId": "WEBEX-DEV-PORTAL_2de9b76f-6ad4-4f28-b8e8-c835885f9e7d_44"
        }
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
The Webex BroadWorks Calling APIs provide access to advanced calling features and user management for BroadWorks-powered Webex Calling deployments. These APIs support provisioning of users and devices, call control, feature management, device inventory, and detailed reporting. Service providers and enterprises can automate onboarding, integrate with OSS/BSS systems, manage user entitlements, and monitor call quality. The APIs are designed for scalable, multi-tenant environments and support seamless integration with existing telephony infrastructure.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs