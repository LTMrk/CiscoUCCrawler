---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-srsv-guide-b-14cucsrsvx-b-14cucsrsvx-chapter-0111-html-93a5181ef9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/srsv/guide/b_14cucsrsvx/b_14cucsrsvx_chapter_0111.html
retrieved_at: 2026-08-16T18:35:44.877011+00:00
---

Complete Reference Guide for Cisco Unity Connection Survivable Remote Site Voicemail (SRSV)

# Complete Reference Guide for Cisco Unity Connection Survivable Remote Site Voicemail (SRSV)

Updated: March 31, 2021

Chapter: Cisco Unity Connection Surviable Remote Site VoiceMail APIs

## Chapter: Cisco Unity Connection Surviable Remote Site VoiceMail APIs

# Cisco Unity Connection Surviable Remote Site VoiceMail APIs

## Listing the Branches

The following is an example of the *GET* request that lists the branches associated with the Cisco Unity Connection server:

GET https://<connection-server>/vmrest/branches

The following is an example of response from the above *GET* request but the actual result depends on the information provided
                              by you:

Response Code: 200

```
<Branches total="2">
 <Branch>
  <URI>/vmrest/branches/1e0ed69d-028d-4156-9d68-f14a90438448</URI>
  <ObjectId>1e0ed69d-028d-4156-9d68-f14a90438448</ObjectId>
  <IsAlive>true</IsAlive>
  <IsDisabled>false</IsDisabled>
  <OperatorObjectId>159bb671-cbba-4964-b06b-871f990e1de8</OperatorObjectId>
  <Port>443</Port>
  <ProvisionState>0</ProvisionState>
  <ServerAddress>mysrsv.cisco.com</ServerAddress>
  <SyncGreetings>false</SyncGreetings>
  <SyncVoiceName>false</SyncVoiceName>
  <UserName>admin</UserName>
  <VmUploadState>0</VmUploadState>
  <DisplayName>Branch1</DisplayName>
  <PartitionObjectId>d6ac04c5-fb36-4e21-9e60-d15e0f9c6971</PartitionObjectId>
  <PartitionURI>/vmrest/partitions/d6ac04c5-fb36-4e21-9e60-d15e0f9c6971</PartitionURI>
  <SmtpDomain>mysrsv.cisco.com</SmtpDomain>
  </Branch>
  <Branch>
  <URI>/vmrest/branches/c3816faf-8dc6-48f3-9c6a-b8e93bba1c42</URI>
  <ObjectId>c3816faf-8dc6-48f3-9c6a-b8e93bba1c42</ObjectId>
  <IsAlive>true</IsAlive>
  <IsDisabled>false</IsDisabled>
  <OperatorObjectId>159bb671-cbba-4964-b06b-871f990e1de8</OperatorObjectId>
  <Port>443</Port>
  <ProvisionState>0</ProvisionState>
  <ServerAddress>mysrsv1.cisco.com</ServerAddress>
  <SyncGreetings>false</SyncGreetings>
  <SyncVoiceName>false</SyncVoiceName>
  <UserName>admin</UserName>
  <VmUploadState>0</VmUploadState>
  <DisplayName>Branch2</DisplayName>
  <PartitionObjectId>765cd618-0cff-43a4-b781-efdba282dba4</PartitionObjectId>
  <PartitionURI>/vmrest/partitions/765cd618-0cff-43a4-b781-efdba282dba4</PartitionURI>
  <SmtpDomain>mysrsv1.cisco.com</SmtpDomain>
  </Branch>
 </Branches>
```

The following chart lists the data fields:

Field Name

Read/Write

Possible Values

Description

ObjectId

Read/Write

objectid

The object id of the branch at central Unity Connection server.

IsAlive

Read

true/false

Connectivity status between the central Unity Connection server and the branch server.

IsDisabled

Read/Write

true/false

Disabled status of branch on the central Unity Connection server.

OperatorObjectId

Read/Write

objectid

The object id of the user who is assigned as the operator user for the branch on the central Unity Connection server.

Port

Read/Write

Port number

PAT port number for the branch server.

ProvisionState

Read/Write

0 – Idle,

1 – Scheduled,

2 – In-progress

Current provisioning status of branch on the central Unity Connection server.

ServerAddress

Read/Write

FQDN, IP Address

The address of the branch server.

SyncGreetings

Read/Write

true/false

Option to enable/disable syncing of greetings for users.

SyncVoiceName

Read/Write

true/false

Option to enable/disable syncing of voice names for users.

UserName

Read/Write

String

Username to be used for REST communication between the central Unity Connection and the branch server.

VmUploadState

Read/Write

0 – Idle,

1 – Scheduled,

2 – In-progress

Displays the status of the current voicemail upload status from branch to the central Unity Connection server.

DisplayName

Read/Write

String

Display name of the branch Unity Connection SRSV server on the central Unity Connection server.

PartitionObjectId

Read/Write

ObjectId

Partition object ID associated with the branch on the central Unity Connection server.

SmtpDomain

Read/Write

Domain name

SMTP domain of the branch server.

## Viewing Data for an Individual Branch

The following is an example of the *GET* request that lists the properties of an individual branch associated with the central
                              Unity Connection server:

GET https://<connection-server>/vmrest/branches/<objectid>

The following is an example of response from the above *GET* request but the actual result depends on the information provided
                              by you:

Response Code: 200

```
<Branch>
 <URI>/vmrest/branches/c3816faf-8dc6-48f3-9c6a-b8e93bba1c42</URI>
 <ObjectId>c3816faf-8dc6-48f3-9c6a-b8e93bba1c42</ObjectId>
 <IsAlive>true</IsAlive>
 <IsDisabled>false</IsDisabled>
 <OperatorObjectId>159bb671-cbba-4964-b06b-871f990e1de8</OperatorObjectId>
 <Port>443</Port>
 <ProvisionState>0</ProvisionState>
 <ServerAddress>mysrsv.cisco.com</ServerAddress>
 <SyncGreetings>false</SyncGreetings>
 <SyncVoiceName>false</SyncVoiceName>
 <UserName>admin</UserName>
 <VmUploadState>0</VmUploadState>
 <DisplayName>branch16</DisplayName>
 <PartitionObjectId>765cd618-0cff-43a4-b781-efdba282dba4</PartitionObjectId>
 <PartitionURI>/vmrest/partitions/765cd618-0cff-43a4-b781-efdba282dba4</PartitionURI>
 <SmtpDomain>mysrsv.cisco.com</SmtpDomain>
</Branch>
```

The following chart lists the data fields.

Field Name

Read/Write

Possible Values

Description

URI

Read

URL to access the branch.

Server address of a particular branch.

ObjectId

Read/Write

object ID

The object id of the branch at the central Unity Connection server.

IsAlive

Read/Write

true/false

Connectivity status between the central and branch Unity Connection server.

IsDisabled

Read/Write

true/false

Disabled status of branch on the central Unity Connection server.

OperatorObjectId

Read/Write

Objectid

The object id of the user who is assigned as the operator user for the branch on the central Unity Connection server.

Port

Read/Write

Port number

PAT port number for the branch server.

Provision

Read/Write

State 0 – Idle, 1 – Scheduled, 2 – In-progress

Current provisioning status of branch on the central Unity Connection server.

ServerAddress

Read/Write

FQDN, IP Address

The address of the branch Unity Connection server.

SyncGreetings

Read/Write

true/false

Option to enable/disable syncing of greetings for users.

SyncVoiceName

Read/Write

true/false

Option to enable/disable syncing of voice names for users.

UserName

Read/Write

String

User name of the administrator of a particular branch.

VmUploadState

Read/Write

0 – Idle,

1 – Scheduled,

2 – In-progress

Current voicemail upload status of branch on the central Unity Connection server.

DisplayName

Read/Write

String

Display name of the branch server on the central Unity Connection server.

PartitionObjectId

Read/Write

ObjectId

Partition object ID associated with the branch on the central Unity Connection server.

PartitionURI

Read/Write

URL Partition

URL associated with the branch on the central Unity Connection server.

SmtpDomain

Read/Write

Domain name

SMTP domain of the branch server.

## Creating a Branch

The following is an example of the *POST* request that is used for creating a branch on the central Unity Connection server:

POST https://<connection-server>/vmrest/branches

```
<Branch>
<IsDisabled>false</IsDisabled>
<OperatorObjectId>159bb671-cbba-4964-b06b-871f990e1de8</OperatorObjectId>
<Port>443</Port>
<ServerAddress>mysrsv.cisco.com</ServerAddress>
<SyncGreetings>false</SyncGreetings>
<SyncVoiceName>false</SyncVoiceName>
<UserName>admin</UserName>
<Password>test</Password>
<DisplayName>branch16</DisplayName>
<PartitionObjectId>765cd618-0cff-43a4-b781-efdba282dba4</PartitionObjectId>
<SmtpDomain>mysrsv.cisco.com</SmtpDomain>
</Branch>
```

The mandatory properties are ServerAddress, UserName, Password, DisplayName, PartitionObjectId, and SmtpDomain.

The successful response code returned for this API is 201. The error response code and data depend on the information provided
                              by you:

Response Code: 201

```
/vmrest/branches/c3816faf-8dc6-48f3-9c6a-b8e93bba1c42
```

The following chart lists the data fields:

Field Name

Read/Write

Possible Values

Description

IsDisabled

Read/Write

true/false

Enables or activates the branch.

OperatorObjectId

Read/Write

Object ID of the operator.

The operator or the user that must be used to synchronize the messages received by the branch server.

Port

Read/Write

Port number

A port number that the branch uses to communicate with Cisco Unity Connection.

ServerAddress

Read/Write

FQDN, IP Address

The IP address or the Fully Qualified Domain Name (FQDN) of the branch server.

SyncGreetings

Read/Write

true/false

Synchronize the greetings for the users on the branch server.

SyncVoiceName

Read/Write

true/false

Synchronize the recorded voice name of the user on the branch server.

UserName

Read/Write

String

The user name of the administrator of the branch Unity Connection server.

Password

Read/Write

String

The password of the administrator of the branch server.

DisplayName

Read/Write

String

Display name of the branch server on the central Unity Connection server.

PartitionObjectId

Read/Write

ObjectId

Partition object ID associated with the branch on the central Unity Connection server.

SmtpDomain

Read/Write

Domain name

SMTP domain of the branch server.

## Updating a Branch

The following is an example of the *PUT* request that is used for updating a branch on the central Unity Connection server:

PUT https://<connection-server>/vmrest/branches/c3816faf-8dc6-48f3-9c6a-b8e93bba1c42

```
<Branch>
<IsDisabled>false</IsDisabled>
<OperatorObjectId>159bb671-cbba-4964-b06b-871f990e1de8</OperatorObjectId>
<Port>443</Port>
<ServerAddress>mysrsv.cisco.com</ServerAddress>
<SyncGreetings>false</SyncGreetings>
<SyncVoiceName>false</SyncVoiceName>
<UserName>admin</UserName>
<Password>test</Password>
<DisplayName>branch16</DisplayName>
<PartitionObjectId>765cd618-0cff-43a4-b781-efdba282dba4</PartitionObjectId>
<SmtpDomain>mysrsv.cisco.com</SmtpDomain>
<ProvisionState>1</ProvisionState>
<VmUploadState>0</VmUploadState>
</Branch>
```

This *PUT* request is also used for scheduling a branch for provisioning and voicemail upload. Only the properties mentioned
                              in above XML are writable at the time of modifying a branch. The properties, ProvisionState and VmUploadState, cannot be put
                              in the request XML at the same time as a branch can be scheduled either for provisioning or voicemail upload, at a given point
                              of time. The value of those fields can only be 1.

The successful response code returned for this API is 201. The error response code and data depend on the information provided
                              by you:

Response Code: 201

```
/vmrest/branches/c3816faf-8dc6-48f3-9c6a-b8e93bba1c42
```

The following chart lists the data fields:

Field Name

Read/Write

Possible Values

Description

IsDisabled

Read/Write

true/false

Enables or activates the branch.

OperatorObjectId

Read/Write

Object ID of the operator.

The operator or the user that must be used to synchronize the messages received by the branch server.

Port

Read/Write

Port number

A port number that the branch uses to communicate with Unity Connection.

ServerAddress

Read/Write

FQDN, IP Address

The IP address or the Fully Qualified Domain Name (FQDN) of the branch server.

SyncGreetings

Read/Write

true/false

Synchronize the greetings for the users on the branch.

SyncVoiceName

Read/Write

true/false

Synchronize the recorded voice name of the user on the branch.

UserName

Read/Write

String

The user name of the administrator of the branch server.

Password

Read/Write

String

The password of the administrator of the branch server.

DisplayName

Read/Write

String

Display name of the branch server on the central Unity Connection server.

PartitionObjectId

Read/Write

ObjectId

Partition object ID associated with the branch on the central Unity Connection server.

SmtpDomain

Read/Write

Domain name

Smtp domain of the branch server.

ProvisionState

Read/Write

0 – Idle,

1 – Scheduled,

2 – In-progress

Current provisioning status of branch on central Unity Connection server.

VmUploadState

Read/Write

0 – Idle,

1 – Scheduled,

2 – In-progress

Current voicemail upload status of branch on central Unity Connection server.

## Deleting a Branch

The following is an example of the Delete request that is used for deleting a branch on the central Unity Connection server:

```
DELETE /vmrest/branches/c3816faf-8dc6-48f3-9c6a-b8e93bba1c42
```

A branch with this API cannot be deleted if the branch is in a In-Progress state either for provisioning or voicemail upload.

The successful response code returned for this API is 201 but the error response code and data depend on the information provided
                           by you:

Response Code: 201

Data: NA

## Assigning a User
                        	 to Branch

The following is an example of the Put request that is used for
                           		assigning a branch to a user by allocating the branch partition to it:

```
PUT /vmrest/users/<userObjectId>
<User>
<PartitionObjectId>partitionObjectIdMappedToBranch</PartitionObjectId>
</User>
```

To fetch the partition information of a branch, you can use the
                           		API to view the details of a branch. See the Viewing Data for an Individual Branch section for more information. The PartitionObjectId element given in the
                           		response XML of this section denotes the partition mapped with the branch.

Response Code: 204

## Removing a User
                        	 from a Branch

The following is an example of the Put request that is used for
                           		removing a user from a branch by modifying its partition to some other
                           		partition that is not mapped to that branch:

```
PUT /vmrest/users/<userObjectId>
<User>
<PartitionObjectId>partitionObjectIdNotMappedToBranch</PartitionObjectId>
</User>
```

You can use the API to view the partition information of a
                           		branch. For more information, see the Viewing Data for an Individual Branch section. The PartitionObjectId element given in the response XML of this
                           		section denotes the partition mapped with the branch.

Response Code: 204

## Listing All Users of a Particular Branch

The following is an example of the Get request that is used to list the users those are part of a particular branch by searching
                              with the partition object ID of the branch:

```
GET /vmrest/users?query=(PartitionObjectId is partitionObjectIdMappedToBranch)
```

Response Code: 200

```
<Users total="10">
<User>
<URI>/vmrest/users/cb13e6a9-7322-45fa-91cd-7a0b1e21b754</URI> <ObjectId>cb13e6a9-7322-45fa-91cd-7a0b1e21b754</ObjectId>
</User>
</Users>
```

Field Name

Read/Write

Possible Values

Description

URI

Read

URL to access the branch.

Server address of a particular branch.

ObjectId

Read/Write

object ID

The object id of the branch at the central Unity Connection server.

## Creating a Call Handler for a Branch

The following is an example of the Put request that is used to create a call handler:

```
POST /vmrest/handlers/callhandlers?templateObjectId=<callhandlerTemplateObjectId>

<Callhandler>
<DisplayName>Test</DisplayName>
</Callhandler>
```

This is an existing API for creating a call handler that can be used at the branch as well.

Response Code: 201

```
/vmrest/handlers/callhandlers/<callhandlerObjectId>
```

| Field Name | Read/Write | Possible Values | Description |
|---|---|---|---|
| ObjectId | Read/Write | objectid | The object id of the branch at central Unity Connection server. |
| IsAlive | Read | true/false | Connectivity status between the central Unity Connection server and the branch server. |
| IsDisabled | Read/Write | true/false | Disabled status of branch on the central Unity Connection server. |
| OperatorObjectId | Read/Write | objectid | The object id of the user who is assigned as the operator user for the branch on the central Unity Connection server. |
| Port | Read/Write | Port number | PAT port number for the branch server. |
| ProvisionState | Read/Write | 0 – Idle, 1 – Scheduled, 2 – In-progress | Current provisioning status of branch on the central Unity Connection server. |
| ServerAddress | Read/Write | FQDN, IP Address | The address of the branch server. |
| SyncGreetings | Read/Write | true/false | Option to enable/disable syncing of greetings for users. |
| SyncVoiceName | Read/Write | true/false | Option to enable/disable syncing of voice names for users. |
| UserName | Read/Write | String | Username to be used for REST communication between the central Unity Connection and the branch server. |
| VmUploadState | Read/Write | 0 – Idle, 1 – Scheduled, 2 – In-progress | Displays the status of the current voicemail upload status from branch to the central Unity Connection server. |
| DisplayName | Read/Write | String | Display name of the branch Unity Connection SRSV server on the central Unity Connection server. |
| PartitionObjectId | Read/Write | ObjectId | Partition object ID associated with the branch on the central Unity Connection server. |
| SmtpDomain | Read/Write | Domain name | SMTP domain of the branch server. |

| Field Name | Read/Write | Possible Values | Description |
|---|---|---|---|
| URI | Read | URL to access the branch. | Server address of a particular branch. |
| ObjectId | Read/Write | object ID | The object id of the branch at the central Unity Connection server. |
| IsAlive | Read/Write | true/false | Connectivity status between the central and branch Unity Connection server. |
| IsDisabled | Read/Write | true/false | Disabled status of branch on the central Unity Connection server. |
| OperatorObjectId | Read/Write | Objectid | The object id of the user who is assigned as the operator user for the branch on the central Unity Connection server. |
| Port | Read/Write | Port number | PAT port number for the branch server. |
| Provision | Read/Write | State 0 – Idle, 1 – Scheduled, 2 – In-progress | Current provisioning status of branch on the central Unity Connection server. |
| ServerAddress | Read/Write | FQDN, IP Address | The address of the branch Unity Connection server. |
| SyncGreetings | Read/Write | true/false | Option to enable/disable syncing of greetings for users. |
| SyncVoiceName | Read/Write | true/false | Option to enable/disable syncing of voice names for users. |
| UserName | Read/Write | String | User name of the administrator of a particular branch. |
| VmUploadState | Read/Write | 0 – Idle, 1 – Scheduled, 2 – In-progress | Current voicemail upload status of branch on the central Unity Connection server. |
| DisplayName | Read/Write | String | Display name of the branch server on the central Unity Connection server. |
| PartitionObjectId | Read/Write | ObjectId | Partition object ID associated with the branch on the central Unity Connection server. |
| PartitionURI | Read/Write | URL Partition | URL associated with the branch on the central Unity Connection server. |
| SmtpDomain | Read/Write | Domain name | SMTP domain of the branch server. |

| Field Name | Read/Write | Possible Values | Description |
|---|---|---|---|
| IsDisabled | Read/Write | true/false | Enables or activates the branch. |
| OperatorObjectId | Read/Write | Object ID of the operator. | The operator or the user that must be used to synchronize the messages received by the branch server. |
| Port | Read/Write | Port number | A port number that the branch uses to communicate with Cisco Unity Connection. |
| ServerAddress | Read/Write | FQDN, IP Address | The IP address or the Fully Qualified Domain Name (FQDN) of the branch server. |
| SyncGreetings | Read/Write | true/false | Synchronize the greetings for the users on the branch server. |
| SyncVoiceName | Read/Write | true/false | Synchronize the recorded voice name of the user on the branch server. |
| UserName | Read/Write | String | The user name of the administrator of the branch Unity Connection server. |
| Password | Read/Write | String | The password of the administrator of the branch server. |
| DisplayName | Read/Write | String | Display name of the branch server on the central Unity Connection server. |
| PartitionObjectId | Read/Write | ObjectId | Partition object ID associated with the branch on the central Unity Connection server. |
| SmtpDomain | Read/Write | Domain name | SMTP domain of the branch server. |

| Field Name | Read/Write | Possible Values | Description |
|---|---|---|---|
| IsDisabled | Read/Write | true/false | Enables or activates the branch. |
| OperatorObjectId | Read/Write | Object ID of the operator. | The operator or the user that must be used to synchronize the messages received by the branch server. |
| Port | Read/Write | Port number | A port number that the branch uses to communicate with Unity Connection. |
| ServerAddress | Read/Write | FQDN, IP Address | The IP address or the Fully Qualified Domain Name (FQDN) of the branch server. |
| SyncGreetings | Read/Write | true/false | Synchronize the greetings for the users on the branch. |
| SyncVoiceName | Read/Write | true/false | Synchronize the recorded voice name of the user on the branch. |
| UserName | Read/Write | String | The user name of the administrator of the branch server. |
| Password | Read/Write | String | The password of the administrator of the branch server. |
| DisplayName | Read/Write | String | Display name of the branch server on the central Unity Connection server. |
| PartitionObjectId | Read/Write | ObjectId | Partition object ID associated with the branch on the central Unity Connection server. |
| SmtpDomain | Read/Write | Domain name | Smtp domain of the branch server. |
| ProvisionState | Read/Write | 0 – Idle, 1 – Scheduled, 2 – In-progress | Current provisioning status of branch on central Unity Connection server. |
| VmUploadState | Read/Write | 0 – Idle, 1 – Scheduled, 2 – In-progress | Current voicemail upload status of branch on central Unity Connection server. |

| Field Name | Read/Write | Possible Values | Description |
|---|---|---|---|
| URI | Read | URL to access the branch. | Server address of a particular branch. |
| ObjectId | Read/Write | object ID | The object id of the branch at the central Unity Connection server. |