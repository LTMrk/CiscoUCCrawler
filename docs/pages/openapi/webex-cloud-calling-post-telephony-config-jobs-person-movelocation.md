---
doc_id: webex-cloud-calling-post-telephony-config-jobs-person-movelocation
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/jobs/person/moveLocation
operation_id: validateOrInitiateMoveUsersJob
tags: User Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.332618+00:00
---

# POST /telephony/config/jobs/person/moveLocation

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `validateOrInitiateMoveUsersJob`

## Resumen
Validate or Initiate Move Users Job

## Descripción
This API allows the user to perform one of the following operations:

* Setting the `validate` attribute to `true` validates the user move.

* Setting the `validate` attribute to `false` performs the user move.

<br/>

Notes:

* A maximum of `100` users can be moved at a time.

* Setting the `validate` attribute to `true` only allowed for calling user.

* When a single non calling user is moved, it will be moved synchronously without creating any job.

<br/>

Errors occurring during the initial API request validation are captured directly in the error response, along with the appropriate HTTP status code.

<br/>

Below is a list of possible error `code` values and their associated `message`, which can be found in the `errors` array during initial API request validation, regardless of the `validate` attribute value:

* BATCH-400 - Attribute 'User ID' is required.

* BATCH-400 - Users list should not be empty.

* BATCH-400 - Users should not be empty.

* 1026006 - Attribute 'Validate' is required.

* 1026010 - User is not a valid Calling User.

* 1026011 - Users list should not be empty.

* 1026012 - Users should not be empty.

* 1026013 - The source and the target location cannot be the same.

* 1026014 - Error occurred while processing the move users request.

* 1026015 - Error occurred while moving user number to target location.

* 1026016 - User should have either phone number or extension.

* 1026017 - Phone number is not in e164 format.

* 1026018 - Selected Users list exceeds the maximum limit.

* 1026019 - Duplicate entry for user is not allowed.

* 1026020 - Validate 'true' is supported only for single user.

* 1026021 - Attribute location id is required for Calling user.

* 1026022 - Validate 'true' is supported for calling users only.

* 1026023 - Extension and phone number is supported for calling users only.

* 2150012 - User was not found

<br/>

When the `validate` attribute is set to true, the API identifies and returns the `errors` and `impacts` associated with the user move in the response.

<br/>

Below is a list of possible error `code` values and their associated `message`, which can be found in the `errors` array, when `validate` attribute is set to be true:

* 4003 - `User Not Found`

* 4007 - `User Not Found`

* 4152 - `Location Not Found`

* 5620 - `Location Not Found`

* 4202 - `The extension is not available. It is already assigned to a user : {0}`

* 8264 - `Routing profile is different with new group: {0}`

* 19600 - `User has to be within an enterprise to be moved.`

* 19601 - `User can only be moved to a different group within the same enterprise.`

* 19602 - `Only regular end user can be moved. Service instance virtual user cannot be moved.`

* 19603 - `New group already reaches maximum number of user limits.`

* 19604 - `The {0} number of the user is the same as the calling line ID of the group.`

* 19605 - `User is assigned services not authorized to the new group: {0}.`

* 19606 - `User is in an active hoteling/flexible seating association.`

* 19607 - `User is pilot user of a trunk group.`

* 19608 - `User is using group level device profiles which is used by other users in current group. Following are the device profiles shared with other users: {0}.`

* 19609 - `Following device profiles cannot be moved to the new group because there are already devices with the same name defined in the new group: {0}.`

* 19610 - `The extension of the user is used as transfer to operator number for following Auto Attendent : {0}.`

* 19611 - `Fail to move announcement file from {0} to {1}.`

* 19612 - `Fail to move device management file from {0} to {1}.`

* 19613 - `User is assigned service packs not authorized to the new group: {0}.`

* 25008 - `Missing Mandatory field name: {0}`

* 25110 - `{fieldName} cannot be less than {0} or greater than {1} characters.`

* 25378 - `Target location is same as user's current location.`

* 25379 - `Error Occurred while Fetching User's Current Location Id.`

* 25381 - `Error Occurred while rolling back to Old Location Call recording Settings`

* 25382 - `Error Occurred while Disabling Call Recording for user which is required Before User can be Moved`

* 25383 - `OCI Error while moving user`

* 25384 - `Error Occurred while checking for Possible Call Recording Impact.`

* 25385 - `Error Occurred while getting Call Recording Settings`

* 27559 - `The groupExternalId search criteria contains groups with different calling zone.`

* 27960 - `Parameter isWebexCalling, newPhoneNumber, or newExtension can only be set in Webex Calling deployment mode.`

* 27961 - `Parameter isWebexCalling shall be set if newPhoneNumber or newExtension is set.`

* 27962 - `Work space cannot be moved.`

* 27963 - `Virtual profile user cannot be moved.`

* 27965 - `The user's phone number: {0}, is same as the current group charge number.`

* 27966 - `The phone number, {0}, is not available in the new group.`

* 27967 - `User is configured as the ECBN user for another user in the current group.`

* 27968 - `User is configured as the ECBN user for the current group.`

* 27969 - `User is associated with DECT handset(s): {0}`

* 27970 - `User is using a customer managed device: {0}`

* 27971 - `User is using an ATA device: {0}`

* 27972 - `User is in an active hotdesking association.`

* 27975 - `Need to unassign CLID number from group before moving the number to the new group. Phone number: {0}`

* 27976 - `Local Gateway configuration is different with new group. Phone number: {0}`

* 1026015 - `Error occurred while moving user number to target location`

* 10010000 - `Total numbers exceeded maximum limit allowed`

* 10010001 - `to-location and from-location cannot be same`

* 10010002 - `to-location and from-location should belong to same customer`

* 10010003 - `to-location must have a carrier`

* 10010004 - `from-location must have a carrier`

* 10010005 - `Different Carrier move is not supported for non-Cisco PSTN carriers.`

* 10010006 - `Number move not supported for WEBEX_DIRECT carriers.`

* 10010007 - `Numbers out of sync, missing on CPAPI`

* 10010008 - `from-location not found or pstn connection missing in CPAPI`

* 10010010 - `from-location is in transition`

* 10010009 - `to-location not found or pstn connection missing in CPAPI`

* 10010011 - `to-location is in transition`

* 10010012 - `Numbers don't have a carrier Id`

* 10010013 - `Location less numbers don't have a carrier Id`

* 10010014 - `Different Carrier move is not supported for numbers with different country or region.`

* 10010015 - `Numbers contain mobile and non-mobile types.`

* 10010016 - `To/From location carriers must be same for mobile numbers.`

* 10010017 - `Move request for location less number not supported`

* 10010200 - `Move request for more than one block number is not supported`

* 10010201 - `Cannot move block number as few numbers not from the block starting %s to %s`

* 10010202 - `Cannot move block number as few numbers failed VERIFICATION from the block %s to %s`

* 10010203 - `Cannot move block number as few numbers missing from the block %s to %s`

* 10010204 - `Cannot move number as it is NOT a part of the block %s to %s`

* 10010205 - `Move request for Cisco PSTN block order not supported.`

* 10010299 - `Move order couldn't be created as no valid number to move`

* 10030000 - `Number not found`

* 10030001 - `Number does not belong to from-location`

* 10030002 - `Number is not present in CPAPI`

* 10030003 - `Number assigned to an user or device`

* 10030004 - `Number not in Active status`

* 10030005 - `Number is set as main number of the location`

* 10030006 - `Number has pending order associated with it`

* 10030007 - `Number belongs to a location but a from-location was not set`

* 10030008 - `Numbers from multiple carrier ids are not supported`

* 10030009 - `Location less number belongs to a location. from-location value is set to null or no location id`

* 10030010 - `One or more numbers are not portable.`

* 10030011 - `Mobile number carrier was not set`

* 10030012 - `Number must be assigned for assigned move`

* 10050000 - `Failed to update customer reference for phone numbers on carrier`

* 10050001 - `Failed to update customer reference`

* 10050002 - `Order is not of operation type MOVE`

* 10050003 - `CPAPI delete call failed`

* 10050004 - `Not found in database`

* 10050005 - `Error sending notification to WxcBillingService`

* 10050006 - `CPAPI provision number as active call failed with status %s ,reason %s`

* 10050007 - `Failed to update E911 Service`

* 10050008 - `Target location does not have Inbound Toll Free license`

* 10050009 - `Source location or Target location subscription found cancelled or suspended`

* 10050010 - `Moving On Premises or Non Integrated CCP numbers from one location to another is not supported.`

* 10099999 - `{Error Code} - {Error Message}`

<br/>

Below is a list of possible impact `code` values and their associated `message`, which can be found in the `impacts` array, when `validate` attribute is set to be true:

* 19701 - `The identity/device profile the user is using is moved to the new group: {0}.`

* 19702 - `The user level customized incoming digit string setting is removed from the user. User is set to use the new group setting.`

* 19703 - `The user level customized outgoing digit plan setting is removed from the user. User is set to use the new group setting.`

* 19704 - `The user level customized enhanced outgoing calling plan setting is removed from the user. User is set to use the new group setting.`

* 19705 - `User is removed from following group services: {0}.`

* 19706 - `The current group schedule used in any criteria is removed from the service settings.`

* 19707 - `User is removed from the department of the old group.`

* 19708 - `User is changed to use the default communication barring profile of the new group.`

* 19709 - `The communication barring profile of the user is assigned to the new group: {0}.`

* 19710 - `The charge number for the user is removed.`

* 19711 - `The disabled FACs for the user are removed because they are not available in the new group.`

* 19712 - `User is removed from trunk group.`

* 19713 - `The extension of the user is reset to empty due to either the length is out of bounds of the new group, or the extension is already taken in new group.`

* 19714 - `The extension of the following alternate number is reset to empty due to either the length out of bounds of the new group or the extension is already taken in new group: {0}.`

* 19715 - `The collaborate room using current group default collaborate bridge is moved to the default collaborate bridge of the new group.`

* 19716 - `Previously stored voice messages of the user are no longer available. The new voice message will be stored on the mail server of the new group.`

* 19717 - `The primary number, alternate numbers or fax messaging number of the user are assigned to the new group: {0}.`

* 19718 - `Following domains are assigned to the new group: {0}.`

* 19719 - `The NCOS of the user is assigned to the new group: {0}.`

* 19720 - `The office zone of the user is assigned to the new group: {0}.`

* 19721 - `The announcement media files are relocated to the new group directory.`

* 19722 - `User CLID number is set to use the new group CLID number: {0}.`

* 19723 - `New group CLID number is not configured.`

* 19724 - `The group level announcement file(s) are removed from the user's music on hold settings.`

* 25388 - `Target Location Does not Have Vendor Configured. Call Recording for user will be disabled`

* 25389 - `Call Recording Vendor for user will be changed from:{0} to:{1}`

* 25390 - `Dub point of user is moved to new external group`

* 25391 - `Error Occurred while moving Call recording Settings to new location`

* 25392 - `Error Occurred while checking for Possible Call Recording Impact.`

* 25393 - `Sending Billing Notification Failed`

This API requires a full administrator auth token with the scopes `spark-admin:telephony_config_write`, `spark-admin:people_write`, and `identity:groups_rw`.

## Parámetros
- `orgId` [query] (string): Create Move Users job for this organization.

## Cuerpo de la petición (application/json)
- `usersList` (array) (**requerido**): Specifies the users to be moved from the source location.
  - `locationId` (string) (**requerido**): Target location for the user moves.
  - `validate` (boolean) (**requerido**): Set to `true` to validate the user move; this option is not supported for multiple users. Set to `false` to perform the user move.
  - `users` (array) (**requerido**): List of users to be moved.
    - `userId` (string) (**requerido**): User ID to be moved.
    - `extension` (string): Extension to be moved. Extension is only supported for calling user. Only one new extension can be moved to the target location for a user. An empty value will remove the configured extension. If not provided, the existing extension will be retained.
    - `phoneNumber` (string): Phone number to be moved. Phone number is only supported for calling user. Only one new phone number belonging to the target location can be assigned to a user. The phone number must follow the E.164 format. An empty value will remove the configured phone number. If not provided, the existing phone number will be moved to the target location.

### Ejemplo — petición
```json
{
  "usersList": [
    {
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzVmMDI3OGZlLWU4OGMtNDMzNy04MGViLWRjY2NiM2VlMDU1MA",
      "validate": false,
      "users": [
        {
          "userId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9teW5hbWUgaXNvcHRpdXMGEyltZXdlYXJlMGEyMGEyNWM1OWE",
          "phoneNumber": "+18632520486"
        },
        {
          "userId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8wNTJhYjliZC1jNmUyLTZlYWUtMWE5YS01ZWZhMGEyNWMxNmE",
          "extension": "28544"
        }
      ]
    },
    {
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzVmMDI3OGZlLWU4OGMtNDkwNS04MGViLWRjY2NiM2VlMTQ0MwFG",
      "validate": false,
      "users": [
        {
          "userId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85YzJhMDUxMC0wOTUwLTQ1MmYtODFmZi05YTVkMjM2OTJkZTY",
          "extension": "29376",
          "phoneNumber": "+18947028597"
        }
      ]
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/jobs/person/moveLocation' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"usersList": []}'
```

## Respuestas correctas
**200**: OK
- `response` (array) (**requerido**): Contains the response for the user moves validation.
  - `userId` (string) (**requerido**): User ID associated with the validation response.
  - `impacts` (array): List of impacts for the user moves.
    - `code` (number) (**requerido**): Error or Impact code.
    - `message` (string) (**requerido**): Message string with more error or impact information.
  - `errors` (array): List of errors for the user moves.
    - `code` (number) (**requerido**): Error or Impact code.
    - `message` (string) (**requerido**): Message string with more error or impact information.

### Ejemplo — respuesta 200
```json
{
  "response": [
    {
      "userId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85YzJhMDUxMC0wOTUwLTQ1MmYtODFmZi05YTVkMjM2OTJkZTY",
      "impacts": [
        {
          "code": 19701,
          "message": "[Informational 19701] The identity/device profile the user is using is moved to the new group: GBKAXBRMJUXF, GNXX95CLTQ0V, HD_92dbc8b6-30d1-419f-9386-3340da658f9c, G4O4NVP7MZI5, GQGWO5BDMPLP."
        },
        {
          "code": 19722,
          "message": "[Informational 19722] User CLID number is set to use the new group CLID number: null."
        },
        {
          "code": 19723,
          "message": "[Informational 19723] New group CLID number is not configured."
        }
      ],
      "errors": [
        {
          "code": 4202,
          "message": "[Error 4202] The extension is not available. It is already assigned to a user: 7593. "
        }
      ]
    }
  ]
}
```
**201**: Created
- `response` (object) (**requerido**):
  - `name` (string) (**requerido**): Job name.
  - `id` (string) (**requerido**): Unique identifier of the job.
  - `trackingId` (string) (**requerido**): Unique identifier to track the flow of HTTP requests.
  - `sourceUserId` (string) (**requerido**): Unique identifier of the user who ran the job.
  - `sourceCustomerId` (string) (**requerido**): Unique identifier of the customer who ran the job.
  - `targetCustomerId` (string) (**requerido**): Unique identifier of the customer for whom the job was run.
  - `instanceId` (number) (**requerido**): Unique identifier of the job instance.
  - `jobExecutionStatus` (array): Most recent step's execution status, including statuses of all steps in the job execution.
    - `id` (number) (**requerido**): Unique identifier for each instance of the job.
    - `startTime` (string) (**requerido**): Start date and time of the job in UTC format.
    - `lastUpdated` (string): Last update date and time of the job in UTC format after a step execution completion.
    - `statusMessage` (string) (**requerido**): Status for the overall steps that are part of the job.  * `STARTING` - Job has started.  * `STARTED` - Job is in progress.  * `COMPLETED` - Job has completed.  * `FAILED` - Job has failed.  * `UNKNOWN` - Job status is unknown.  * `ABANDONED` - Job has been abandoned (manually stopped). Valores: STARTING, STARTED, COMPLETED, FAILED, UNKNOWN, ABANDONED.
    - `exitCode` (string): Overall result of the job.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed.  * `FAILED` - Job has failed.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors.  * `COMPLETED_WITH_PENDING_ORDERS` - Job has completed with pending number orders. Valores: UNKNOWN, COMPLETED, FAILED, COMPLETED_WITH_ERRORS, COMPLETED_WITH_PENDING_ORDERS.
    - `createdTime` (string) (**requerido**): Creation date and time of the job in UTC format.
    - `timeElapsed` (string): Time elapsed in seconds since the job execution started.
  - `latestExecutionStatus` (string) (**requerido**): Most recent status of the job at the time of invocation.  * `STARTING` - Job has started.  * `STARTED` - Job is in progress.  * `COMPLETED` - Job has completed.  * `FAILED` - Job has failed.  * `UNKNOWN` - Job status is unknown.  * `ABANDONED` - Job has been abandoned (manually stopped). Valores: STARTING, STARTED, COMPLETED, FAILED, UNKNOWN, ABANDONED.
  - `latestExecutionExitCode` (string): Most recent exit code of the job at the time of invocation.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors.  * `COMPLETED_WITH_PENDING_ORDERS` - Job has completed with pending number orders. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS, COMPLETED_WITH_PENDING_ORDERS.
  - `counts` (object) (**requerido**):
    - `totalMoves` (number) (**requerido**): Total number of user moves requested.
    - `moved` (number) (**requerido**): Total number of user moves completed successfully.
    - `failed` (number) (**requerido**): Total number of user moves that were completed with failures.
    - `pending` (number) (**requerido**): Total number of user moves that were pending with number orders.
    - `skipped` (number) (**requerido**): Total number of user moves that were skipped.

### Ejemplo — respuesta 201
```json
{
  "response": {
    "name": "moveusers",
    "id": "Y2lzY29zcGFyazovL3VzL0pPQl9JRC9mZjBlN2Q2Ni05MDRlLTRkZGItYjJlNS05ZGM0ODk0ZDY5OTk",
    "trackingId": "ROUTER_ebb52b5b-d060-4164-9757-48b383423d73",
    "sourceUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85YzJhMDUxMC0wOTUwLTQ1MmYtODFmZi05YTVkMjM2OTJkZTY",
    "sourceCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8wMjEyNGVlZi04YWY3LTQ4OWMtODA1Yi0zNjNjYzY0MDE4OTM",
    "targetCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8wMjEyNGVlZi04YWY3LTQ4OWMtODA1Yi0zNjNjYzY0MDE4OTM",
    "instanceId": 10,
    "jobExecutionStatus": [
      {
        "id": 10,
        "startTime": "2023-06-08T12:05:11.798Z",
        "lastUpdated": "2023-06-08T12:05:11.798Z",
        "statusMessage": "STARTED",
        "exitCode": "UNKNOWN",
        "createdTime": "2023-06-08T12:05:11.752Z",
        "timeElapsed": "PT0S"
      }
    ],
    "latestExecutionStatus": "STARTED",
    "latestExecutionExitCode": "UNKNOWN",
    "counts": {
      "totalMoves": 0,
      "moved": 0,
      "failed": 0,
      "pending": 0,
      "skipped": 0,
      "inProgress": 0,
      "notStarted": 0
    }
  }
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
  Ejemplo:
```json
{
  "error": [
    {
      "code": 1026016,
      "message": "User should have either phone number or extension."
    }
  ]
}
```
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