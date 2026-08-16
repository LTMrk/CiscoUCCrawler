---
doc_id: webex-broadworks-get-broadworks-enterprises
source: webex-openapi-specs/public-spec/webex-broadworks.json
api: Webex Broadworks Calling
method: GET
path: /broadworks/enterprises
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.284491+00:00
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
- `max` [query] (number): Limit the number of enterprises returned in the search, up to 1000.

## Respuestas
- **200**: OK
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
