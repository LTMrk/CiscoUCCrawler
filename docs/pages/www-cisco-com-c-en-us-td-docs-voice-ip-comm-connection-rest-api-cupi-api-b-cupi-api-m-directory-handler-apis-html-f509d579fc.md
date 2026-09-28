---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-directory-handler-apis-html-f509d579fc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m-directory-handler-apis.html
retrieved_at: 2026-08-17T03:49:41.493202+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API--Directory Handler APIs

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API--Directory Handler APIs

# Cisco Unity Connection Provisioning Interface (CUPI) API--Directory Handler APIs

## Cisco Unity Connection Provisioning Interface (CUPI) API--Directory Handler APIs

### Directory Handler
                           	 APIs

Directory handlers provide access
                              		to a corporate directory that callers can use to reach Cisco Unity Connection
                              		users with mailboxes. When a caller searches for a username or part of a name,
                              		a directory handler looks up the extension and routes the call to the
                              		appropriate user. Administrator can use this API to create/update/delete/fetch
                              		the directory handler. You can update various attributes of directory handler
                              		using this API.

#### Listing the Directory Handlers

The following is an example of the GET request that fetch the list of directory handlers:

```
GET https://<connection-server>/vmrest/handlers/directoryhandlers
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                    by you:

```
<DirectoryHandlers total="1">
<DirectoryHandler>
<URI>/vmrest/handlers/directoryhandlers/16090424-1c38-4901-a465-3b76ffaf437a</URI>
<CreationTime>2012-12-10T19:24:31Z</CreationTime>
<Language>1033</Language>
<DisplayName>System Directory Handler</DisplayName>
Cisco_Unity_Connection_Provisioning_Interface_(CUPI)_API_--_Directory_Handler_APIs
Contents 1
<Undeletable>true</Undeletable>
<VoiceName>b09bd14d-15ef-4100-b0f7-4ba2f0c15343.wav</VoiceName>
<VoiceFileURI>/vmrest/voicefiles/b09bd14d-15ef-4100-b0f7-
4ba2f0c15343.wav</VoiceFileURI>
<VoiceNameURI>/vmrest/handlers/directoryhandlers/16090424-1c38-4901-a465-
3b76ffaf437a/voicename</VoiceNameURI>
<LocationObjectId>08b0402c-ba81-4f16-bcba-ca7883de0482</LocationObjectId>
<LocationURI>/vmrest/locations/connectionlocations/08b0402c-ba81-4f16-bcbaca7883de0482</
LocationURI>
<EndDialDelay>4</EndDialDelay>
<MaxMatches>8</MaxMatches>
<MenuStyle>true</MenuStyle>
<SayExtension>true</SayExtension>
<SearchByFirstName>false</SearchByFirstName>
<StartDialDelay>5</StartDialDelay>
<Tries>1</Tries>
<UseStarToExit>true</UseStarToExit>
<SearchScope>0</SearchScope>
<SearchScopeObjectId>08b0402c-ba81-4f16-bcba-ca7883de0482</SearchScopeObjectId>
<PlayAllNames>false</PlayAllNames>
<ExitAction>2</ExitAction>
<ExitTargetConversation>PHTransfer</ExitTargetConversation>
<ExitTargetHandlerObjectId>04786933-dd71-45e1-b2fb-
1a5dd99503f6</ExitTargetHandlerObjectId>
<NoInputAction>2</NoInputAction>
<NoInputTargetConversation>PHTransfer</NoInputTargetConversation>
<NoInputTargetHandlerObjectId>f8bac9c4-62a2-4744-a9e6-74ac90fb87fd</NoInputTargetHandlerObjectId>
<NoSelectionAction>2</NoSelectionAction>
<NoSelectionTargetConversation>PHTransfer</NoSelectionTargetConversation>
<NoSelectionTargetHandlerObjectId>f8bac9c4-62a2-4744-a9e6-
74ac90fb87fd</NoSelectionTargetHandlerObjectId>
<ZeroAction>2</ZeroAction>
<ZeroTargetConversation>PHTransfer</ZeroTargetConversation>
<ZeroTargetHandlerObjectId>b6cd5cfd-312c-4eb0-96ea-
57531fa9058d</ZeroTargetHandlerObjectId>
<AutoRoute>false</AutoRoute>
<ObjectId>16090424-1c38-4901-a465-3b76ffaf437a</ObjectId>
<TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
<DtmfAccessId>555</DtmfAccessId>
<ScopeObjectLocationObjectId>08b0402c-ba81-4f16-bcbaca7883de0482</
ScopeObjectLocationObjectId>
<ScopeObjectLocationURI>/vmrest/locations/connectionlocations/08b0402c-ba81-4f16-bcbaca7883de0482</
ScopeObjectLocationURI>
<VoiceEnabled>false</VoiceEnabled>
<UseCallLanguage>true</UseCallLanguage>
<UseDefaultLanguage>true</UseDefaultLanguage>
<PartitionObjectId>ff1c9ff2-6fcc-47e9-a4e0-a220c6e3ae4e</PartitionObjectId>
<PartitionURI>/vmrest/partitions/ff1c9ff2-6fcc-47e9-a4e0-a220c6e3ae4e</PartitionURI>
<SpeechConfidenceThreshold>10</SpeechConfidenceThreshold>
<SayCity>false</SayCity>
<SayDepartment>false</SayDepartment>
</DirectoryHandler>
</DirectoryHandlers>
```

```
Response Code: 200
```

JSON Example

To list of directory handlers, do the following:

```
GET https://<connection-server>/vmrest/handlers/directoryhandlers
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                    by you:

```
"@total": "1",
"DirectoryHandler": [
{
"URI": "/vmrest/handlers/directoryhandlers/36408c02-4b25-4549-b3a4-deafa5945339",
"CreationTime": "2013-02-08T04:59:36Z",
"Language": "1033",
"DisplayName": "System Directory Handler",
"Undeletable": "true",
"VoiceName": "41a5ba0d-5267-40d8-aa2c-dd1f61046f7c.wav",
"VoiceFileURI": "/vmrest/voicefiles/41a5ba0d-5267-40d8-aa2c-dd1f61046f7c.wav",
"VoiceNameURI": "/vmrest/handlers/directoryhandlers/36408c02-4b25-4549-b3a4-
deafa5945339/voicename",
"LocationObjectId": "df46033e-0058-4f7e-b5fc-8346df0ffee1",
"LocationURI": "/vmrest/locations/connectionlocations/df46033e-0058-4f7e-b5fc-
8346df0ffee1",
"EndDialDelay": "4",
"MaxMatches": "8",
"MenuStyle": "true",
"SayExtension": "true",
"SearchByFirstName": "false",
"StartDialDelay": "5",
"Tries": "1",
"UseStarToExit": "true",
"SearchScope": "0",
"SearchScopeObjectId": "df46033e-0058-4f7e-b5fc-8346df0ffee1",
"PlayAllNames": "false",
"ExitAction": "2",
"ExitTargetConversation": "PHTransfer",
"ExitTargetHandlerObjectId": "e6fd6ae4-7bf5-4a46-b994-e9fd13d83c30",
"NoInputAction": "2",
"NoInputTargetConversation": "PHTransfer",
"NoInputTargetHandlerObjectId": "d4d920f6-d7d4-4a3e-8876-21917480867f",
"NoSelectionAction": "2",
"NoSelectionTargetConversation": "PHTransfer",
"NoSelectionTargetHandlerObjectId": "d4d920f6-d7d4-4a3e-8876-21917480867f",
"ZeroAction": "2",
"ZeroTargetConversation": "PHTransfer",
"ZeroTargetHandlerObjectId": "b45f1e23-ce6d-4406-a9b2-48c647094a77",
"AutoRoute": "false",
"ObjectId": "36408c02-4b25-4549-b3a4-deafa5945339",
"TenantObjectId": "fe6541fb-b42c-44f2-8404-ded14cbf7438",
"DtmfAccessId": "555",
"ScopeObjectLocationObjectId": "df46033e-0058-4f7e-b5fc-8346df0ffee1",
"ScopeObjectLocationURI": "/vmrest/locations/connectionlocations/df46033e-0058-
4f7e-b5fc-8346df0ffee1",
"VoiceEnabled": "false",
"UseCallLanguage": "true",
"UseDefaultLanguage": "true",
"PartitionObjectId": "92ef3894-5bf0-430c-a1f1-4ef67925aecf",
"PartitionURI": "/vmrest/partitions/92ef3894-5bf0-430c-a1f1-4ef67925aecf",
"SpeechConfidenceThreshold": "10",
"SayCity": "false",
"SayDepartment": "false",
"UseCustomGreeting": "false",
"ExitConversationURI":
"/vmrest/conversations?query=(cnvdirectoryhandlerexit%20is%201)",
"NoInputConversationURI":
"/vmrest/conversations?query=(cnvdirectoryhandlernoinput%20is%201)",
"NoSelectionConversationURI":
Cisco_Unity_Connection_Provisioning_Interface_(CUPI)_API_--_Directory_Handler_APIs
Listing the Directory Handlers 3
"/vmrest/conversations?query=(cnvdirectoryhandlernoselection%20is%201)",
"ZeroExitConversationURI":
"/vmrest/conversations?query=(cnvdirectoryhandlerzeroexit%20is%201)",
"DirectoryHandlerStreamFileURI":
"/vmrest/handlers/directoryhandlers/36408c02-4b25-4549-b3a4-deafa5945339/directoryhandlerstreamfiles"
}
]
}
```

```
Response Code: 200
```

##### Listing Specific Tenant Related Directory Handlers by System Administrator

In Cisco Unity Connection 10.5(2) and later, the system administrator can use TenantObjectID to list the specific tenant related
                                       directory handlers using the following URI:

```
GET https://<connection-server>/vmrest/handlers/directoryhandlers?query=(TenantObjectId is <Tenant>
```

To get the TenantObjectID, use the following URI:

```
GET https://<connection-server>/vmrest/tenants
```

#### Viewing the Specific Directory Handler

The following is an example of the GET request that lists the details of specific directory handler represented by the provided
                                    value of directory handler ID:

```
GET https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                    by you:

```
<DirectoryHandler>
<URI>/vmrest/handlers/directoryhandlers/16090424-1c38-4901-a465-3b76ffaf437a</URI>
<CreationTime>2012-12-10T19:24:31Z</CreationTime>
<Language>1033</Language>
<DisplayName>System Directory Handler</DisplayName>
<Undeletable>true</Undeletable>
<VoiceName>b09bd14d-15ef-4100-b0f7-4ba2f0c15343.wav</VoiceName>
<VoiceFileURI>/vmrest/voicefiles/b09bd14d-15ef-4100-b0f7-4ba2f0c15343.wav</VoiceFileURI>
<VoiceNameURI>/vmrest/handlers/directoryhandlers/16090424-1c38-4901-a465-
3b76ffaf437a/voicename</VoiceNameURI>
<LocationObjectId>08b0402c-ba81-4f16-bcba-ca7883de0482</LocationObjectId>
<LocationURI>/vmrest/locations/connectionlocations/08b0402c-ba81-4f16-bcbaca7883de0482</
LocationURI>
<EndDialDelay>4</EndDialDelay>
<MaxMatches>8</MaxMatches>
<MenuStyle>true</MenuStyle>
<SayExtension>true</SayExtension>
<SearchByFirstName>false</SearchByFirstName>
<StartDialDelay>5</StartDialDelay>
<Tries>1</Tries>
<UseStarToExit>true</UseStarToExit>
<SearchScope>0</SearchScope>
<SearchScopeObjectId>08b0402c-ba81-4f16-bcba-ca7883de0482</SearchScopeObjectId>
<PlayAllNames>false</PlayAllNames>
<ExitAction>2</ExitAction>
<ExitTargetConversation>PHTransfer</ExitTargetConversation>
<ExitTargetHandlerObjectId>04786933-dd71-45e1-b2fb-
1a5dd99503f6</ExitTargetHandlerObjectId>
Cisco_Unity_Connection_Provisioning_Interface_(CUPI)_API_--_Directory_Handler_APIs
Listing Specific Tenant Related Directory Handlers by System Administrator 4
<NoInputAction>2</NoInputAction>
<NoInputTargetConversation>PHTransfer</NoInputTargetConversation>
<NoInputTargetHandlerObjectId>f8bac9c4-62a2-4744-a9e6-74ac90fb87fd</NoInputTargetHandlerObjectId>
<NoSelectionAction>2</NoSelectionAction>
<NoSelectionTargetConversation>PHTransfer</NoSelectionTargetConversation>
<NoSelectionTargetHandlerObjectId>f8bac9c4-62a2-4744-a9e6-
74ac90fb87fd</NoSelectionTargetHandlerObjectId>
<ZeroAction>2</ZeroAction>
<ZeroTargetConversation>PHTransfer</ZeroTargetConversation>
<ZeroTargetHandlerObjectId>b6cd5cfd-312c-4eb0-96ea-
57531fa9058d</ZeroTargetHandlerObjectId>
<AutoRoute>false</AutoRoute>
<ObjectId>16090424-1c38-4901-a465-3b76ffaf437a</ObjectId>
<DtmfAccessId>555</DtmfAccessId>
<ScopeObjectLocationObjectId>08b0402c-ba81-4f16-bcba-ca7883de0482</ScopeObjectLocationObjectId>
<ScopeObjectLocationURI>/vmrest/locations/connectionlocations/08b0402c-ba81-4f16-bcbaca7883de0482</
ScopeObjectLocationURI>
<VoiceEnabled>false</VoiceEnabled>
<UseCallLanguage>true</UseCallLanguage>
<UseDefaultLanguage>true</UseDefaultLanguage>
<PartitionObjectId>ff1c9ff2-6fcc-47e9-a4e0-a220c6e3ae4e</PartitionObjectId>
<PartitionURI>/vmrest/partitions/ff1c9ff2-6fcc-47e9-a4e0-a220c6e3ae4e</PartitionURI>
<SpeechConfidenceThreshold>10</SpeechConfidenceThreshold>
<SayCity>false</SayCity>
<SayDepartment>false</SayDepartment>
</DirectoryHandler>
```

```
Response Code: 200
```

JSON Example

To list details of a particular directory handler, do the following:

```
GET https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                    by you:

```
{
"URI": "/vmrest/handlers/directoryhandlers/36408c02-4b25-4549-b3a4-deafa5945339",
"CreationTime": "2013-02-08T04:59:36Z",
"Language": "1033",
"DisplayName": "System Directory Handler",
"Undeletable": "true",
"VoiceName": "41a5ba0d-5267-40d8-aa2c-dd1f61046f7c.wav",
"VoiceFileURI": "/vmrest/voicefiles/41a5ba0d-5267-40d8-aa2c-dd1f61046f7c.wav",
"VoiceNameURI": "/vmrest/handlers/directoryhandlers/36408c02-4b25-4549-b3a4-
deafa5945339/voicename",
"LocationObjectId": "df46033e-0058-4f7e-b5fc-8346df0ffee1",
"LocationURI": "/vmrest/locations/connectionlocations/df46033e-0058-4f7e-b5fc-
8346df0ffee1",
"EndDialDelay": "4",
"MaxMatches": "8",
"MenuStyle": "true",
"SayExtension": "true",
"SearchByFirstName": "false",
"StartDialDelay": "5",
"Tries": "1",
"UseStarToExit": "true",
"SearchScope": "0",
Cisco_Unity_Connection_Provisioning_Interface_(CUPI)_API_--_Directory_Handler_APIs
Viewing the Specific Directory Handler 5
"SearchScopeObjectId": "df46033e-0058-4f7e-b5fc-8346df0ffee1",
"PlayAllNames": "false",
"ExitAction": "2",
"ExitTargetConversation": "PHTransfer",
"ExitTargetHandlerObjectId": "e6fd6ae4-7bf5-4a46-b994-e9fd13d83c30",
"NoInputAction": "2",
"NoInputTargetConversation": "PHTransfer",
"NoInputTargetHandlerObjectId": "d4d920f6-d7d4-4a3e-8876-21917480867f",
"NoSelectionAction": "2",
"NoSelectionTargetConversation": "PHTransfer",
"NoSelectionTargetHandlerObjectId": "d4d920f6-d7d4-4a3e-8876-21917480867f",
"ZeroAction": "2",
"ZeroTargetConversation": "PHTransfer",
"ZeroTargetHandlerObjectId": "b45f1e23-ce6d-4406-a9b2-48c647094a77",
"AutoRoute": "false",
"ObjectId": "36408c02-4b25-4549-b3a4-deafa5945339",
"DtmfAccessId": "555",
"ScopeObjectLocationObjectId": "df46033e-0058-4f7e-b5fc-8346df0ffee1",
"ScopeObjectLocationURI": "/vmrest/locations/connectionlocations/df46033e-0058-
4f7e-b5fc-8346df0ffee1",
"VoiceEnabled": "false",
"UseCallLanguage": "true",
"UseDefaultLanguage": "true",
"PartitionObjectId": "92ef3894-5bf0-430c-a1f1-4ef67925aecf",
"PartitionURI": "/vmrest/partitions/92ef3894-5bf0-430c-a1f1-4ef67925aecf",
"SpeechConfidenceThreshold": "10",
"SayCity": "false",
"SayDepartment": "false",
"UseCustomGreeting": "false",
"ExitConversationURI":
"/vmrest/conversations?query=(cnvdirectoryhandlerexit%20is%201)",
"NoInputConversationURI":
"/vmrest/conversations?query=(cnvdirectoryhandlernoinput%20is%201)",
"NoSelectionConversationURI":
"/vmrest/conversations?query=(cnvdirectoryhandlernoselection%20is%201)",
"ZeroExitConversationURI": "/vmrest/conversations?query=(cnvdirectoryhandlerzeroexit%20is%201)",
"DirectoryHandlerStreamFileURI":
"/vmrest/handlers/directoryhandlers/36408c02-4b25-4549-b3a4-deafa5945339/directoryhandlerstreamfiles"
}
```

```
Response Code: 200
```

#### Creating a Directory Handler

The following is an example of the POST request that creates a new directory handler:

```
POST https://<connection-server>/vmrest/handlers/directoryhandlers
```

Request Body:

```
<DirectoryHandler>
<DisplayName>Taxoma_Directory Handler</DisplayName>
</DirectoryHandler>
```

The following is the response from the above *POST* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 201
/vmrest/handlers/directoryhandlers/16090424-1c38-4901-a465-3b76ffaf437a
```

JSON Example

To create a new directory handler, do the following:

```
POST https://<connection-server>/vmrest/handlers/directoryhandlers
Accept: application/json
Content-Type: application/json
Connection: keep-alive
```

Request Body:

```
{
"DisplayName": "Texoma123_Directory Handler"
}
```

The following is the response from the above *POST* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 201
/vmrest/handlers/directoryhandlers/16090424-1c38-4901-a465-3b76ffaf437a
```

#### Delete the Directory Handler

This request can be used to delete a directory handler.

```
DELETE https://<connection-server>/vmrest/directory handler/<directoryHandlerObjectId>
```

The following is the response from the above *DELETE* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

JSON Example

To delete the directory handler, do the following:

```
DELETE https://<connection-server>/vmrest/directory handler/<directoryHandlerObjectId>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *DELETE* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

#### Updating the Search Scope of the Directory Handler

The following is an example of the PUT request that can be used to modify the search scope of the directory handler. In the
                                    request body, the search scope value corresponds to the type of search scope and search scope object ID represents the objectid
                                    corresponding to the search scope value. For Example Value for COS as search scope is 5 and search scope object ID should
                                    be COS.

```
PUT https://<connection-server>/vmrest/directory handler /<directoryHandlerObjectId>
```

Request Body:

```
<DirectoryHandler>
<SearchScope>5</SearchScope>
<SearchScopeObjectId>03815b4e-3b88-48b3-918d-91a9d1673880</SearchScopeObjectId>
</DirectoryHandler>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

The table given below lists the possible values of the search scope:

Name

Value

Description

VMS

0

DialingDomain

1

Dialing domain - directory handler search restricted to a dialing domain.

Global

2

Global - directory handler search expanded to the entire Unity organization (global).

Location

3

Location - directory handler search restricted to a Unity location.

DistributionList

4

Distribution list - directory handler search is restricted to a distribution list.

cos

5

COS - directory handler search restricted to a class of service.

SearchSpace

6

SearchSpace - directory handler search restricted to a search space.

Inherit

7

Inherit - directory handler search is restricted to the search space of the call.

Invalid

8

Invalid - directory handler search scope is no longer valid; used by the replicator.

You can set the search scope of a directory handler by defining only search scope and search scope object ID. The search scope
                                    object Id can have these references, COS object Id, location object Id, distribution list, and search space object ID.

Example 1: Update the Search Scope of a Directory Handler to a Class of Service

To update the search scope of a directory handler to a class of service, you must obtain the COS object ID.

```
GET https://<connection-server>/vmrest/coses
```

The following is an example of the PUT request to update the directory handler to COS object ID:

Request URI

```
PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
```

Request Body:

```
<DirectoryHandler>
<SearchScope>5</SearchScope>
<SearchScopeObjectId>03815b4e-3b88-48b3-918d-91a9d1673880</SearchScopeObjectId>
</DirectoryHandler>
```

```
Response Code: 204
```

Example 2: Update the Search Scope of a Directory Handler to Entire Server

To update the search scope of a directory handler to entire server, you must obtain the location of the object id of the connection
                                    server:

```
GET https://<connection-server>/vmrest/locations/connectionlocations
```

The following is an example of the PUT request to update the directory handler to entire server:

Request URI:

```
PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
```

Request Body:

```
<DirectoryHandler>
<SearchScope>0</SearchScope>
<SearchScopeObjectId>08b0402c-ba81-4f16-bcba-ca7883de0482</SearchScopeObjectId>
</DirectoryHandler>
```

```
Response Code: 204
```

Example 3: Update the Search Scope of a Directory Handler to Inherit Search Scope from Call

The following is an example of the PUT request to update the search scope of directory handler to inherit search scope from
                                    call:

Request URI:

```
PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
```

Request Body:

```
<DirectoryHandler>
<SearchScope>7</SearchScope>
</DirectoryHandler>
```

```
Response Code: 204
```

Example 3: Update the Search Scope of a Directory Handler to Inherit Search Scope from Call

The following is an example of the PUT request to update the search scope of directory handler to inherit search scope from
                                    call:

Request URI:

```
PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
```

Request Body:

```
<DirectoryHandler>
<SearchScope>7</SearchScope>
</DirectoryHandler>
```

```
Response Code: 204
```

Example 4: Update the Search Scope of a Directory Handler to a Distribution List

The following is an example of the PUT request to update the search scope of directory handler to a distribution list:

```
PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
```

Request Body:

```
<DirectoryHandler>
<SearchScope>4</SearchScope>
<SearchScopeObjectId>0995fc34-6791-4d9a-b20f-52c8dadd65b5</SearchScopeObjectId>
</DirectoryHandler>
```

```
Response Code: 204
```

Example 5: Update the Search Scope of a Directory Handler to a Search Space

To update the search scope of a directory handler to a search space, you must obtain the object ID of the search scope using
                                    the following URL:

```
GET https://<connection-server>/vmrest/searchspaces
```

The following is an example of the PUT request to update the search scope of directory handler to a search space:

Request URI:

PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>

Request Body:

```
<DirectoryHandler>
<SearchScope>6</SearchScope>
<SearchScopeObjectId>1cdaa964-0514-4364-ad74-e55364efb4b4</SearchScopeObjectId>
</DirectoryHandler>
```

```
Response Code: 204
```

JSON Example

To update the search scope of a directory handler to a search space, do the following:

Request URI:

```
PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
```

Request Body:

```
{
"SearchScope":"6",
"SearchScopeObjectId":"1cdaa964-0514-4364-ad74-e55364efb4b4"
}
```

The following is an example of the PUT request to update the search scope of directory handler to a search space:

```
Response Code: 200
```

#### Updating the Exit Action on a directory handler

You can update the exit action, no input action, no selection action and action when caller presses zero on a directory handler.
                                    To specify the destination when a caller exits the directory handler using the * key/ or #key, the following fields are used
                                    to specify the destination:

ExitAction

ExitTargetConversation

ExitTargetHandlerObjectId

In a scenario where caller does not respond to the name entry prompt, the following fields are used to specify the destination
                                    the fields:

NoInputAction

NoInputTargetConversation

NoInputTargethandlerObjectId

In another scenario where caller does not respond to the name entry prompt the fields, the following fields are used to specify
                                    the destination the fields:

NoSelectionAction

NoSelectionTargetConversation

NoSelectionTargetHandlerObjectId

If callers press the zero key, the following fields are used to specify the destination the fields:

ZeroAction

ZeroTargetConversation

ZeroTargetHandlerObjectId

Call Handlers: /vmrest/handlers/callhandlers

Directory Handlers: /vmrest/handlers/directoryhandlers

InterviewHandler : /vmrest/handlers/interviewhandlers

The following sections give some examples of how to specify different types of destinations by using these fields when caller
                                    exits the directory handler.

Example 1: Call should hang up on exit action.

Request URI

```
PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
```

Request Body

```
<DirectoryHandler>
<ExitAction>1</ExitAction>
</DirectoryHandler>
```

```
Response Code: 204
```

Example 2: Call should be sent to a call handler or a user greeting

Request URI

```
PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
```

Request Body

```
<DirectoryHandler>
<ExitAction>2</ExitAction>
<ExitTargetConversation>PHGreeting</ExitTargetConversation>
<ExitTargetHandlerObjectId>5f8b4a28-8042-4cce-a11c-
0222f106f79f</ExitTargetHandlerObjectId>
</DirectoryHandler>
```

```
Response Code: 204
```

JSON Example

To update the directory handler, do the following:

Request URI

```
PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
```

Request Body

```
{
"ExitAction": "2",
"ExitTargetConversation": "PHGreeting",
"ExitTargetHandlerObjectId": "e6fd6ae4-7bf5-4a46-b994-e9fd13d83c30"
}
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

Example 3: Call should be transferred to a call handler or user

Request URI

```
PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
```

Request Body

```
<DirectoryHandler>
<ExitAction>2</ExitAction>
<ExitTargetConversation>SystemTransfer</ExitTargetConversation>
</DirectoryHandler>
```

```
Response Code: 204
```

The fields for that needs to be sent as input are Exit Action and ExitTargetConversation.

Example 5: Call should be sent to an Interview Handler

Request URI

```
PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
```

Request Body

```
<DirectoryHandler>
<ExitAction>2</ExitAction>
<ExitTargetConversation>PHInterview</ExitTargetConversation>
<ExitTargetHandlerObjectId>1ff9ef5e-1b97-4f3f-a30d-
48aef7733d7f</ExitTargetHandlerObjectId>
</DirectoryHandler>
```

```
Response Code: 204
```

Example 6: Call should be sent to a Directory Handler.

Request URI

```
PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
```

Request Body

```
<DirectoryHandler>
<ExitAction>2</ExitAction>
<ExitTargetConversation>AD</ExitTargetConversation>
<ExitTargetHandlerObjectId>249056ed-5954-493d-9d87-
aec9cedafe25</ExitTargetHandlerObjectId>
</DirectoryHandler>
```

```
Response Code: 204
```

#### Setting Voice Enable to true for a Directory Handler

Voice enabled directory handlers cannot use a class of service or a distribution list as per their search scope.

Only entire server, a specific search space, or Inherit search space from call are allowed.

Request URI

```
PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
```

Request Body

```
<DirectoryHandler>
<VoiceEnabled>true</VoiceEnabled>
</DirectoryHandler>
```

```
Response Code: 204
```

JSON Example

To update the voice enable, do the following:

Request URI

```
PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
{
"VoiceEnabled":"true"
}
```

The following is an example of the PUT request to update the search scope of directory handler to a search space:

```
Response Code: 204
```

If a request is sent to enable the voiceenabled field and set the search scope to a COS or distribution list, the search scope
                                                      is set to entire server.

If the search scope of a directory handler is already a COS or a distribution list and request is sent to set the voiceenabled
                                                      to true, the search scope is set to entire server.

#### Updating the Language of Directory Handler

This request can be used to update a language for a directory handler. It can be used to set a particular language for a directory
                                    handler, set the system default language as the language of directory handler or set the language of directory handler as
                                    inherit from call.

```
URI to get Language code: https://<connection-server>/vmrest/languagemap
URI to Get Language code for installed languages: https://<connection-server>/vmrest/installedlang
```

The below table specify the details of value for each field:

UseCallLanguage

UseDefaultLanguage

Language

Description

false

true

Null/Language Code

This will select the default language.

true

true/false

Null/Language Code

This will inherit the language from user.

false

false

Language Code

This will select the particular language as per the code.

Request URI

```
PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectid>
```

Example 1: Updating the Inherit Language field and not the Language field

Request Body

```
<Directoryhandler>
<UseCallLanguage>true</UseCallLanguage>
<UseDefaultLanguage>false</UseDefaultLanguage>
</Directoryhandler>
```

```
Response Code: 204
```

The Inherit Language field from the call is selected but the UseDefaultLanguage field will not get updated in the database
                                    as the Language field is missing. If the Language field is NULL, the UseDefaultLanguage field is by default set to TRUE.

Example 2: Updating the Inherit Language field and the Language field

Request Body

```
<Directoryhandler>
<UseCallLanguage>true</UseCallLanguage>
<UseDefaultLanguage>false</UseDefaultLanguage>
<Language>1033</Language>
</Directoryhandler>
```

```
Response Code: 204
```

The Inherit Language field from the call is selected but the UseDefaultLanguage field is updated in the database as the Language
                                    field is specified.

JSON Example

To change language, do the following:

Request URI

```
PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
```

Request Body

```
{
"UseCallLanguage":"true",
"UseDefaultLanguage":"false",
"Language":"1033"
}
```

```
Response Code: 204
```

#### Explanation of
                              	 Data Fields

All possible language code values can be fetched using <connection server>/vmrest/languagemap.

Values:

- false: The handler can be deleted by an administrator.

- true: The handler cannot be deleted by an administrator.

Default value: false

Value can be in the range 1-10. Default Value: 4.

Value can be in the range 1-30. Default value: 8.

Note: MenuStyle cannot be set to false for the System Default Directory Handler. Possible values can be:

- true : menu choice

- false : extension list.

Default value: true.

Possible values can be:

- false: Play only subscriber names in menu list.

- true: Play subscriber names and extensions in menu list.

Default value : true

Values:

- false: Search by last name, then first name.

- true: Search by first name, then last name.

Default value: false.

Default value: 5. Value can be in the range 1-10.

Default value : 1. Value can be in the range 0-10.

Values:

- true: Use star ("*") key to exit directory handler.

- false: Use pound/hash ("#") key to exit directory handler.

Default value: true.

Default value: 0( search scope set as entire server). Possible values : Refer to the SearchScope section under the Enumeration
                                                Type as given at the end of the document

Default value: false.

Possible Values: Refer to the section Enumeration Type at the end of the document.

Refer to the section Enumeration Type at the end of the document.

Default Value: 2. Possible Values: Refer to the section Enumeration Type at the end of the document.

Refer to the section Enumeration Type at the end of the document.

Possible Values: Refer to the section Enumeration Type at the end of the document.

Refer to the section Enumeration Type at the end of the document.

Default Value: 2 Possible Values: Refer to the section Enumeration Type at the end of the document.

Refer to the section Enumeration Type at the end of the document.

Default value: false. Values:

- false: Presents a list of matches, even if only one, and prompts the user to verify the match.

- true: Automatically routes a call to the extension assigned to the subscriber on a unique match without prompting the caller
                                                      to verify the match.

Default value: false. Values:

- false: Use touchtones

- true: Use voice commands

Default Value is 10. Range of Value is 0 -100

Default value is false.

Default value is false.

Default value is false.

## Cisco Unity Connection Provisioning Interface (CUPI) API--Directory Handler Greeting APIs

### Directory Handler
                           	 Greeting APIs

Administrator can use this API to create/update/fetch the Directory
                              		Handler Greeting.

There are three ways to upload the Custom Greeting for the Directory
                              		Handler :

1) Upload a .wav file from the desktop.

2) Record a recording using CUTI(Cisco Unity Telephony Interface) and
                              		upload to the Directory Handler.

3) Pass the .wav as an inputStream to the Directory
                              		Handler.Administrator can use this API to create/update/fetch the directory
                              		handler greeting. You can update various attributes of directory handler
                              		greeting using this API.

#### Enable Use of
                              	 Custom Recordings on a Directory Handler

Custom Greetings can be enabled
                                    		  on a directory handler using the directory handler API. A PUT operation has to
                                    		  be performed to set the UseCustomGreetings field to True:

```
PUT https://<connection-server>/vmrest/directoryhandlers/<DirectoryhandlerObjectId>
```

```
<DirectoryHandler>
    <UseCustomGreeting>true<UseCustomGreeting>
</DirectoryHandler>
```

The following is the response from the above *PUT* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To enable use of custom recordings on a directory handler, do the
                                    		  following:

```
PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<DirectoryhandlerObjectId>
Accept: application /json
Content-Type: application/json
Connection: keep-alive
```

```
{
    "UseCustomGreeting": "true"
}
```

The following is an example of the *PUT* request and the actual
                                    		  response will depend upon the information given by you:

```
Response Code: 204
```

#### Listing Directory
                              	 Handler Greeting

The following is an example of
                                    		  the GET request that lists all the custom recordings for a directory handler
                                    		  represented by the provided value of directory handler ID:

```
GET https://<connection-
  server>/vmrest/handlers/directoryhandlers/<DirectoryHandlerObjectId>/directoryhandlerstreamfiles
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
<DirectoryHandlerStreamFiles>
  <DirectoryHandlerStreamFile>
    <DirectoryHandlerObjectId>3a0043ab-933b-45f6-852d-e0a261554da2</DirectoryHandlerObjectId>
    <LanguageCode>1033</LanguageCode>
    <StreamFile>5a0c7347-4064-4e94-a9c8-b12426d38f8a.wav</StreamFile>
  </DirectoryHandlerStreamFile>
</DirectoryHandlerStreamFiles>
```

```
Response Code: 200
```

JSON Example

To list directory handler greeting, do the following:

```
Request URI:
GET https://<connection-
server>/vmrest/handlers/directoryhandlers/<DirectoryHandlerObjectId>/directoryhandlerstreamfiles
Accept: application /json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                    		  actual response will depend upon the information given by you:

```
{
  "DirectoryHandlerStreamFile": 
  {
    "DirectoryHandlerObjectId": "06628a5c-b755-466d-9e39-66e1956c2242",
    "LanguageCode": "1033",
    "StreamFile": "050590b8-fb8f-4e8d-ab17-4e29eab7d412.wav"
  }
}
```

```
Response Code: 200
```

#### Viewing Custom
                              	 Recording for a Particular Language

The following is an example of
                                    		  the GET request that list the custom recording for a particular language from a
                                    		  directory handler:

```
GET https://<connection-
  server>/vmrest/handlers/directoryhandlers/<DirectoryHandlerObjectId>/directoryhandlerstreamfiles
  /1033
```

#### Playing an
                              	 Existing Greeting

The following is an example that
                                    		  will play an existing greeting in the browser:

```
https://<connection-
  server>/vmrest/handlers/directoryhandlers/<DirectoryHandlerObjectId>/directoryhandlerstreamfiles
  /1033/audio
```

#### Add or Update
                              	 Greeting by Uploading File from the Desktop

It is a 3 step process

Step 1: A place-holder for the WAV file must be created with a
                                    		  POST. This is a temporary file place-holder that can be used for up to 30
                                    		  minutes. If it is not assigned to a resource within 30 minutes, the file is
                                    		  assumed to be abandoned and is automatically cleaned.

```
POST https://<connection-server>/vmrest/voicefiles
```

```
Response Code: 201
```

The content is the name of the newly created temporary .wav file.

JSON Example

To create a place-holder for the WAV file, do the following:

```
Request URI:
POST https://<connection-server>/vmrest/voicefiles
Accept: application/json
Content-Type: application/json
Connection: keep-alive
```

```
Response Code: 201
Sample Response: 6d9f3b85-c1df-4af8-89f3-6a975ebfb24c.wav
```

Step 2: Use the temporary file name to PUT the new audio data.
                                    		  The HTTP content type is "audio/wav" and the payload content is the audio data.

NOTE: *Rename the .wav file which is to be uploaded as the
                                    		  greeting to the temporary file name generated as part of the response from
                                    		  step1. For eg : If the file on desktop has name "greeting.wav" and the
                                    		  temporary file name is 6d9f3b85-c1df-4af8-89f3-6a975ebfb24c.wav(got as part of
                                    		  the response of step1), then the file should be renamed to
                                    		  6d9f3b85-c1df-4af8-89f3-6a975ebfb24c.wav before step 2 is performed.

- The length of the greeting
                                          			 can be set under the System Settings > General Configuration settings. Here
                                          			 you can enter the maximum length for system call handler greetings. The range
                                          			 is 1 to 1,200 seconds.

Default setting: 90 seconds. PUT /vmrest/voicefiles/<temporary file
                                    		  name>< /pre>

```
Response Code: 204
```

The content gets accepted and copied into the temporary file.

JSON Example To use the temporary file name, do the following:

```
Request URI:
PUT https://<connection server>/vmrest/voicefiles/<temporary file name>
Content-Type: audio/wav
Connection: keep-alive
```

```
Response Code: 204
```

Step 3: Set the Greeting field of the target resource. Both
                                    		  POST/ PUT can be used for adding a greeting. The PUT request should be used for
                                    		  updating the greeting with a new stream file.

```
POST https://<connection-
  server>/vmrest/handlers/directoryhandlers/<directoryhandlerObjectId>/directoryhandlerstreamfiles
  /1033
Request Body:
<DirectoryHandlerStreamFile>
    <StreamFile>7acbfec8-25a3-4b02-bd23-2b61acc175c9.wav</StreamFile>
</DirectoryHandlerStreamFile >
```

```
Response Code: 201
```

JSON Example

To set the greeting field of the target resource, do the following:

```
Request URI: 
POST https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryhandlerObjectId>/directoryhandlerstreamfiles/1033
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "StreamFile":"050590b8-fb8f-4e8d-ab17-4e29eab7d412.wav"
}
```

The following is the response from the above *POST* request and the
                                    		  actual response will depend upon the information given by you:

```
Response Code: 201
```

Use the following URL in a browser to play the stream file: https://<connection-server>/vmrest/handlers/directoryhandlers/<DirectoryHandlerObjectId>/directoryhandlerstreamfiles/1033/audio

#### Add/Update
                              	 Greeting Recording Used in Telephony Interface

It is a three step process to record a new file then modify the current stream with this new stream.

Step 1: Call Connection In the first step integration between Unity Connection and Call Manager must be setup so that a call can be setup. Refer
                                    to the document at the below link to check how to make the call. http://docwiki.cisco.com/wiki/Cisco_Unity_Connection_Telephony_Interface_(CUTI)_API_--_Using_CUTI_for_Basic_Call_Operations

Step 2: Recording Once the phone is answered, the second step is to record the greeting. Refer to the document below to check how to record
                                    a greeting. http://docwiki.cisco.com/wiki/Cisco_Unity_Connection_Telephony_Interface_(CUTI)_API_--_Using_CUTI_for_Basic_Call_Operations

Step 3: Upload Greeting The response for the step 2 is a Call Control object xml. That xml is to be passed in as the request body for this request.

```
PUT https://<Connection Server>/vmrest/handlers/directoryhandlers/<DirectoryHandlerObjectId>/directoryhandlerstreamfiles/1033/audio
Request Body:
<CallControl>
    <op>RECORD</op>
    <resourceType>STREAM</resourceType>
    <resourceId>67ed783c-203f-454b-a0e6-57b77820c831.wav</resourceId>
    <lastResult>0</lastResult>
    <speed>100</speed>
    <volume>100</volume>
    <startPosition>0</startPosition>
</CallControl>
```

```
Response Code: 204
```

JSON Example

To upload greeting, do the following:

```
PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<DirectoryHandlerObjectId>/directoryhandlerstreamfiles/1033/audio
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "op":"RECORD",
    "resourceType":"STREAM",
    "resourceId":"67ed783c-203f-454b-a0e6-57b77820c831.wav",
    "lastResult":"0",
    "speed":"100",
    "volume":"100",
    "startPosition":"0"
}
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

Use the following URL in browser to play the stream file: https://<connection- server>/vmrest/handlers/directoryhandlers/<DirectoryHandlerObjectId>/directoryhandlerstreamfiles/10
                                    33/audio Update the Greeting using the Input Stream The Directory Handler greeting can also be updated using the Input Stream.
                                    An input stream can be created from the wav file and passed as the request body. The URL for this should be :

```
RequestURI :
https://<connectionserver>/vmrest/handlers/directoryhandlers/<directoryhandlerobjectid>/directoryhan
dlerstreamfiles/1033/audio.
```

The request body should be like this: put.setRequestBody(new FileInputStream(file3)); Here put is the PUT request created,
                                    file3 is the wav file which user want to upload. Also the content type for the request should be passed as "audio/wav". Following
                                    URL can be used to listen to the greeting associated with the directory handler. Paste the URL in the browser and listen to
                                    the uploaded greeting: https://<connectionserver>/vmrest/handlers/directoryhandlers/<directoryhandlerobjectid>/directoryhan
                                    dlerstreamfiles/1033/audio

#### Explanation of
                              	 Data Fields

```
GET https://<connection-server>/vmrest/installedlanguages
```

For more information on the Language Map API, please refer to the following document: http://docwiki.cisco.com/wiki/Cisco_Unity_Connection_Provisioning_Interface_%28CUPI%29_API_--_Language_Map

| <DirectoryHandlers total="1">
<DirectoryHandler>
<URI>/vmrest/handlers/directoryhandlers/16090424-1c38-4901-a465-3b76ffaf437a</URI>
<CreationTime>2012-12-10T19:24:31Z</CreationTime>
<Language>1033</Language>
<DisplayName>System Directory Handler</DisplayName>
Cisco_Unity_Connection_Provisioning_Interface_(CUPI)_API_--_Directory_Handler_APIs
Contents 1
<Undeletable>true</Undeletable>
<VoiceName>b09bd14d-15ef-4100-b0f7-4ba2f0c15343.wav</VoiceName>
<VoiceFileURI>/vmrest/voicefiles/b09bd14d-15ef-4100-b0f7-
4ba2f0c15343.wav</VoiceFileURI>
<VoiceNameURI>/vmrest/handlers/directoryhandlers/16090424-1c38-4901-a465-
3b76ffaf437a/voicename</VoiceNameURI>
<LocationObjectId>08b0402c-ba81-4f16-bcba-ca7883de0482</LocationObjectId>
<LocationURI>/vmrest/locations/connectionlocations/08b0402c-ba81-4f16-bcbaca7883de0482</
LocationURI>
<EndDialDelay>4</EndDialDelay>
<MaxMatches>8</MaxMatches>
<MenuStyle>true</MenuStyle>
<SayExtension>true</SayExtension>
<SearchByFirstName>false</SearchByFirstName>
<StartDialDelay>5</StartDialDelay>
<Tries>1</Tries>
<UseStarToExit>true</UseStarToExit>
<SearchScope>0</SearchScope>
<SearchScopeObjectId>08b0402c-ba81-4f16-bcba-ca7883de0482</SearchScopeObjectId>
<PlayAllNames>false</PlayAllNames>
<ExitAction>2</ExitAction>
<ExitTargetConversation>PHTransfer</ExitTargetConversation>
<ExitTargetHandlerObjectId>04786933-dd71-45e1-b2fb-
1a5dd99503f6</ExitTargetHandlerObjectId>
<NoInputAction>2</NoInputAction>
<NoInputTargetConversation>PHTransfer</NoInputTargetConversation>
<NoInputTargetHandlerObjectId>f8bac9c4-62a2-4744-a9e6-74ac90fb87fd</NoInputTargetHandlerObjectId>
<NoSelectionAction>2</NoSelectionAction>
<NoSelectionTargetConversation>PHTransfer</NoSelectionTargetConversation>
<NoSelectionTargetHandlerObjectId>f8bac9c4-62a2-4744-a9e6-
74ac90fb87fd</NoSelectionTargetHandlerObjectId>
<ZeroAction>2</ZeroAction>
<ZeroTargetConversation>PHTransfer</ZeroTargetConversation>
<ZeroTargetHandlerObjectId>b6cd5cfd-312c-4eb0-96ea-
57531fa9058d</ZeroTargetHandlerObjectId>
<AutoRoute>false</AutoRoute>
<ObjectId>16090424-1c38-4901-a465-3b76ffaf437a</ObjectId>
<TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
<DtmfAccessId>555</DtmfAccessId>
<ScopeObjectLocationObjectId>08b0402c-ba81-4f16-bcbaca7883de0482</
ScopeObjectLocationObjectId>
<ScopeObjectLocationURI>/vmrest/locations/connectionlocations/08b0402c-ba81-4f16-bcbaca7883de0482</
ScopeObjectLocationURI>
<VoiceEnabled>false</VoiceEnabled>
<UseCallLanguage>true</UseCallLanguage>
<UseDefaultLanguage>true</UseDefaultLanguage>
<PartitionObjectId>ff1c9ff2-6fcc-47e9-a4e0-a220c6e3ae4e</PartitionObjectId>
<PartitionURI>/vmrest/partitions/ff1c9ff2-6fcc-47e9-a4e0-a220c6e3ae4e</PartitionURI>
<SpeechConfidenceThreshold>10</SpeechConfidenceThreshold>
<SayCity>false</SayCity>
<SayDepartment>false</SayDepartment>
</DirectoryHandler>
</DirectoryHandlers> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/handlers/directoryhandlers
Accept: application/json
Connection: keep-alive |
|---|

| "@total": "1",
"DirectoryHandler": [
{
"URI": "/vmrest/handlers/directoryhandlers/36408c02-4b25-4549-b3a4-deafa5945339",
"CreationTime": "2013-02-08T04:59:36Z",
"Language": "1033",
"DisplayName": "System Directory Handler",
"Undeletable": "true",
"VoiceName": "41a5ba0d-5267-40d8-aa2c-dd1f61046f7c.wav",
"VoiceFileURI": "/vmrest/voicefiles/41a5ba0d-5267-40d8-aa2c-dd1f61046f7c.wav",
"VoiceNameURI": "/vmrest/handlers/directoryhandlers/36408c02-4b25-4549-b3a4-
deafa5945339/voicename",
"LocationObjectId": "df46033e-0058-4f7e-b5fc-8346df0ffee1",
"LocationURI": "/vmrest/locations/connectionlocations/df46033e-0058-4f7e-b5fc-
8346df0ffee1",
"EndDialDelay": "4",
"MaxMatches": "8",
"MenuStyle": "true",
"SayExtension": "true",
"SearchByFirstName": "false",
"StartDialDelay": "5",
"Tries": "1",
"UseStarToExit": "true",
"SearchScope": "0",
"SearchScopeObjectId": "df46033e-0058-4f7e-b5fc-8346df0ffee1",
"PlayAllNames": "false",
"ExitAction": "2",
"ExitTargetConversation": "PHTransfer",
"ExitTargetHandlerObjectId": "e6fd6ae4-7bf5-4a46-b994-e9fd13d83c30",
"NoInputAction": "2",
"NoInputTargetConversation": "PHTransfer",
"NoInputTargetHandlerObjectId": "d4d920f6-d7d4-4a3e-8876-21917480867f",
"NoSelectionAction": "2",
"NoSelectionTargetConversation": "PHTransfer",
"NoSelectionTargetHandlerObjectId": "d4d920f6-d7d4-4a3e-8876-21917480867f",
"ZeroAction": "2",
"ZeroTargetConversation": "PHTransfer",
"ZeroTargetHandlerObjectId": "b45f1e23-ce6d-4406-a9b2-48c647094a77",
"AutoRoute": "false",
"ObjectId": "36408c02-4b25-4549-b3a4-deafa5945339",
"TenantObjectId": "fe6541fb-b42c-44f2-8404-ded14cbf7438",
"DtmfAccessId": "555",
"ScopeObjectLocationObjectId": "df46033e-0058-4f7e-b5fc-8346df0ffee1",
"ScopeObjectLocationURI": "/vmrest/locations/connectionlocations/df46033e-0058-
4f7e-b5fc-8346df0ffee1",
"VoiceEnabled": "false",
"UseCallLanguage": "true",
"UseDefaultLanguage": "true",
"PartitionObjectId": "92ef3894-5bf0-430c-a1f1-4ef67925aecf",
"PartitionURI": "/vmrest/partitions/92ef3894-5bf0-430c-a1f1-4ef67925aecf",
"SpeechConfidenceThreshold": "10",
"SayCity": "false",
"SayDepartment": "false",
"UseCustomGreeting": "false",
"ExitConversationURI":
"/vmrest/conversations?query=(cnvdirectoryhandlerexit%20is%201)",
"NoInputConversationURI":
"/vmrest/conversations?query=(cnvdirectoryhandlernoinput%20is%201)",
"NoSelectionConversationURI":
Cisco_Unity_Connection_Provisioning_Interface_(CUPI)_API_--_Directory_Handler_APIs
Listing the Directory Handlers 3
"/vmrest/conversations?query=(cnvdirectoryhandlernoselection%20is%201)",
"ZeroExitConversationURI":
"/vmrest/conversations?query=(cnvdirectoryhandlerzeroexit%20is%201)",
"DirectoryHandlerStreamFileURI":
"/vmrest/handlers/directoryhandlers/36408c02-4b25-4549-b3a4-deafa5945339/directoryhandlerstreamfiles"
}
]
} |
|---|

| Response Code: 200 |
|---|

| <DirectoryHandler>
<URI>/vmrest/handlers/directoryhandlers/16090424-1c38-4901-a465-3b76ffaf437a</URI>
<CreationTime>2012-12-10T19:24:31Z</CreationTime>
<Language>1033</Language>
<DisplayName>System Directory Handler</DisplayName>
<Undeletable>true</Undeletable>
<VoiceName>b09bd14d-15ef-4100-b0f7-4ba2f0c15343.wav</VoiceName>
<VoiceFileURI>/vmrest/voicefiles/b09bd14d-15ef-4100-b0f7-4ba2f0c15343.wav</VoiceFileURI>
<VoiceNameURI>/vmrest/handlers/directoryhandlers/16090424-1c38-4901-a465-
3b76ffaf437a/voicename</VoiceNameURI>
<LocationObjectId>08b0402c-ba81-4f16-bcba-ca7883de0482</LocationObjectId>
<LocationURI>/vmrest/locations/connectionlocations/08b0402c-ba81-4f16-bcbaca7883de0482</
LocationURI>
<EndDialDelay>4</EndDialDelay>
<MaxMatches>8</MaxMatches>
<MenuStyle>true</MenuStyle>
<SayExtension>true</SayExtension>
<SearchByFirstName>false</SearchByFirstName>
<StartDialDelay>5</StartDialDelay>
<Tries>1</Tries>
<UseStarToExit>true</UseStarToExit>
<SearchScope>0</SearchScope>
<SearchScopeObjectId>08b0402c-ba81-4f16-bcba-ca7883de0482</SearchScopeObjectId>
<PlayAllNames>false</PlayAllNames>
<ExitAction>2</ExitAction>
<ExitTargetConversation>PHTransfer</ExitTargetConversation>
<ExitTargetHandlerObjectId>04786933-dd71-45e1-b2fb-
1a5dd99503f6</ExitTargetHandlerObjectId>
Cisco_Unity_Connection_Provisioning_Interface_(CUPI)_API_--_Directory_Handler_APIs
Listing Specific Tenant Related Directory Handlers by System Administrator 4
<NoInputAction>2</NoInputAction>
<NoInputTargetConversation>PHTransfer</NoInputTargetConversation>
<NoInputTargetHandlerObjectId>f8bac9c4-62a2-4744-a9e6-74ac90fb87fd</NoInputTargetHandlerObjectId>
<NoSelectionAction>2</NoSelectionAction>
<NoSelectionTargetConversation>PHTransfer</NoSelectionTargetConversation>
<NoSelectionTargetHandlerObjectId>f8bac9c4-62a2-4744-a9e6-
74ac90fb87fd</NoSelectionTargetHandlerObjectId>
<ZeroAction>2</ZeroAction>
<ZeroTargetConversation>PHTransfer</ZeroTargetConversation>
<ZeroTargetHandlerObjectId>b6cd5cfd-312c-4eb0-96ea-
57531fa9058d</ZeroTargetHandlerObjectId>
<AutoRoute>false</AutoRoute>
<ObjectId>16090424-1c38-4901-a465-3b76ffaf437a</ObjectId>
<DtmfAccessId>555</DtmfAccessId>
<ScopeObjectLocationObjectId>08b0402c-ba81-4f16-bcba-ca7883de0482</ScopeObjectLocationObjectId>
<ScopeObjectLocationURI>/vmrest/locations/connectionlocations/08b0402c-ba81-4f16-bcbaca7883de0482</
ScopeObjectLocationURI>
<VoiceEnabled>false</VoiceEnabled>
<UseCallLanguage>true</UseCallLanguage>
<UseDefaultLanguage>true</UseDefaultLanguage>
<PartitionObjectId>ff1c9ff2-6fcc-47e9-a4e0-a220c6e3ae4e</PartitionObjectId>
<PartitionURI>/vmrest/partitions/ff1c9ff2-6fcc-47e9-a4e0-a220c6e3ae4e</PartitionURI>
<SpeechConfidenceThreshold>10</SpeechConfidenceThreshold>
<SayCity>false</SayCity>
<SayDepartment>false</SayDepartment>
</DirectoryHandler> |
|---|

| GET https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
Accept: application/json
Connection: keep-alive |
|---|

| {
"URI": "/vmrest/handlers/directoryhandlers/36408c02-4b25-4549-b3a4-deafa5945339",
"CreationTime": "2013-02-08T04:59:36Z",
"Language": "1033",
"DisplayName": "System Directory Handler",
"Undeletable": "true",
"VoiceName": "41a5ba0d-5267-40d8-aa2c-dd1f61046f7c.wav",
"VoiceFileURI": "/vmrest/voicefiles/41a5ba0d-5267-40d8-aa2c-dd1f61046f7c.wav",
"VoiceNameURI": "/vmrest/handlers/directoryhandlers/36408c02-4b25-4549-b3a4-
deafa5945339/voicename",
"LocationObjectId": "df46033e-0058-4f7e-b5fc-8346df0ffee1",
"LocationURI": "/vmrest/locations/connectionlocations/df46033e-0058-4f7e-b5fc-
8346df0ffee1",
"EndDialDelay": "4",
"MaxMatches": "8",
"MenuStyle": "true",
"SayExtension": "true",
"SearchByFirstName": "false",
"StartDialDelay": "5",
"Tries": "1",
"UseStarToExit": "true",
"SearchScope": "0",
Cisco_Unity_Connection_Provisioning_Interface_(CUPI)_API_--_Directory_Handler_APIs
Viewing the Specific Directory Handler 5
"SearchScopeObjectId": "df46033e-0058-4f7e-b5fc-8346df0ffee1",
"PlayAllNames": "false",
"ExitAction": "2",
"ExitTargetConversation": "PHTransfer",
"ExitTargetHandlerObjectId": "e6fd6ae4-7bf5-4a46-b994-e9fd13d83c30",
"NoInputAction": "2",
"NoInputTargetConversation": "PHTransfer",
"NoInputTargetHandlerObjectId": "d4d920f6-d7d4-4a3e-8876-21917480867f",
"NoSelectionAction": "2",
"NoSelectionTargetConversation": "PHTransfer",
"NoSelectionTargetHandlerObjectId": "d4d920f6-d7d4-4a3e-8876-21917480867f",
"ZeroAction": "2",
"ZeroTargetConversation": "PHTransfer",
"ZeroTargetHandlerObjectId": "b45f1e23-ce6d-4406-a9b2-48c647094a77",
"AutoRoute": "false",
"ObjectId": "36408c02-4b25-4549-b3a4-deafa5945339",
"DtmfAccessId": "555",
"ScopeObjectLocationObjectId": "df46033e-0058-4f7e-b5fc-8346df0ffee1",
"ScopeObjectLocationURI": "/vmrest/locations/connectionlocations/df46033e-0058-
4f7e-b5fc-8346df0ffee1",
"VoiceEnabled": "false",
"UseCallLanguage": "true",
"UseDefaultLanguage": "true",
"PartitionObjectId": "92ef3894-5bf0-430c-a1f1-4ef67925aecf",
"PartitionURI": "/vmrest/partitions/92ef3894-5bf0-430c-a1f1-4ef67925aecf",
"SpeechConfidenceThreshold": "10",
"SayCity": "false",
"SayDepartment": "false",
"UseCustomGreeting": "false",
"ExitConversationURI":
"/vmrest/conversations?query=(cnvdirectoryhandlerexit%20is%201)",
"NoInputConversationURI":
"/vmrest/conversations?query=(cnvdirectoryhandlernoinput%20is%201)",
"NoSelectionConversationURI":
"/vmrest/conversations?query=(cnvdirectoryhandlernoselection%20is%201)",
"ZeroExitConversationURI": "/vmrest/conversations?query=(cnvdirectoryhandlerzeroexit%20is%201)",
"DirectoryHandlerStreamFileURI":
"/vmrest/handlers/directoryhandlers/36408c02-4b25-4549-b3a4-deafa5945339/directoryhandlerstreamfiles"
} |
|---|

| <DirectoryHandler>
<DisplayName>Taxoma_Directory Handler</DisplayName>
</DirectoryHandler> |
|---|

| Response Code: 201
/vmrest/handlers/directoryhandlers/16090424-1c38-4901-a465-3b76ffaf437a |
|---|

| POST https://<connection-server>/vmrest/handlers/directoryhandlers
Accept: application/json
Content-Type: application/json
Connection: keep-alive |
|---|

| {
"DisplayName": "Texoma123_Directory Handler"
} |
|---|

| Response Code: 201
/vmrest/handlers/directoryhandlers/16090424-1c38-4901-a465-3b76ffaf437a |
|---|

| DELETE https://<connection-server>/vmrest/directory handler/<directoryHandlerObjectId> |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/directory handler/<directoryHandlerObjectId>
Accept: application/json
Connection: keep-alive |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/directory handler /<directoryHandlerObjectId> |
|---|

| <DirectoryHandler>
<SearchScope>5</SearchScope>
<SearchScopeObjectId>03815b4e-3b88-48b3-918d-91a9d1673880</SearchScopeObjectId>
</DirectoryHandler> |
|---|

| Response Code: 204 |
|---|

| Name | Value | Description |
|---|---|---|
| VMS | 0 | VMS - directory handler search restricted to the local VMS. |
| DialingDomain | 1 | Dialing domain - directory handler search restricted to a dialing domain. |
| Global | 2 | Global - directory handler search expanded to the entire Unity organization (global). |
| Location | 3 | Location - directory handler search restricted to a Unity location. |
| DistributionList | 4 | Distribution list - directory handler search is restricted to a distribution list. |
| cos | 5 | COS - directory handler search restricted to a class of service. |
| SearchSpace | 6 | SearchSpace - directory handler search restricted to a search space. |
| Inherit | 7 | Inherit - directory handler search is restricted to the search space of the call. |
| Invalid | 8 | Invalid - directory handler search scope is no longer valid; used by the replicator. |

| <DirectoryHandler>
<SearchScope>5</SearchScope>
<SearchScopeObjectId>03815b4e-3b88-48b3-918d-91a9d1673880</SearchScopeObjectId>
</DirectoryHandler> |
|---|

| Response Code: 204 |
|---|

| GET https://<connection-server>/vmrest/locations/connectionlocations |
|---|

| <DirectoryHandler>
<SearchScope>0</SearchScope>
<SearchScopeObjectId>08b0402c-ba81-4f16-bcba-ca7883de0482</SearchScopeObjectId>
</DirectoryHandler> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId> |
|---|

| <DirectoryHandler>
<SearchScope>7</SearchScope>
</DirectoryHandler> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId> |
|---|

| <DirectoryHandler>
<SearchScope>7</SearchScope>
</DirectoryHandler> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId> |
|---|

| <DirectoryHandler>
<SearchScope>4</SearchScope>
<SearchScopeObjectId>0995fc34-6791-4d9a-b20f-52c8dadd65b5</SearchScopeObjectId>
</DirectoryHandler> |
|---|

| Response Code: 204 |
|---|

| GET https://<connection-server>/vmrest/searchspaces |
|---|

| PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId> |
|---|

| <DirectoryHandler>
<SearchScope>6</SearchScope>
<SearchScopeObjectId>1cdaa964-0514-4364-ad74-e55364efb4b4</SearchScopeObjectId>
</DirectoryHandler> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
Accept: application/json
Content-Type: application/json
Connection: keep-alive |
|---|

| {
"SearchScope":"6",
"SearchScopeObjectId":"1cdaa964-0514-4364-ad74-e55364efb4b4"
} |
|---|

| Response Code: 200 |
|---|

| PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId> |
|---|

| <DirectoryHandler>
<ExitAction>1</ExitAction>
</DirectoryHandler> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId> |
|---|

| <DirectoryHandler>
<ExitAction>2</ExitAction>
<ExitTargetConversation>PHGreeting</ExitTargetConversation>
<ExitTargetHandlerObjectId>5f8b4a28-8042-4cce-a11c-
0222f106f79f</ExitTargetHandlerObjectId>
</DirectoryHandler> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
Accept: application/json
Content-Type: application/json
Connection: keep-alive |
|---|

| {
"ExitAction": "2",
"ExitTargetConversation": "PHGreeting",
"ExitTargetHandlerObjectId": "e6fd6ae4-7bf5-4a46-b994-e9fd13d83c30"
} |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId> |
|---|

| <DirectoryHandler>
<ExitAction>2</ExitAction>
<ExitTargetConversation>SystemTransfer</ExitTargetConversation>
</DirectoryHandler> |
|---|

| Response Code: 204 |
|---|

| Note | The fields for that needs to be sent as input are Exit Action and ExitTargetConversation. |
|---|---|

| PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId> |
|---|

| <DirectoryHandler>
<ExitAction>2</ExitAction>
<ExitTargetConversation>PHInterview</ExitTargetConversation>
<ExitTargetHandlerObjectId>1ff9ef5e-1b97-4f3f-a30d-
48aef7733d7f</ExitTargetHandlerObjectId>
</DirectoryHandler> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId> |
|---|

| <DirectoryHandler>
<ExitAction>2</ExitAction>
<ExitTargetConversation>AD</ExitTargetConversation>
<ExitTargetHandlerObjectId>249056ed-5954-493d-9d87-
aec9cedafe25</ExitTargetHandlerObjectId>
</DirectoryHandler> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId> |
|---|

| <DirectoryHandler>
<VoiceEnabled>true</VoiceEnabled>
</DirectoryHandler> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
Accept: application/json
Content-Type: application/json
Connection: keep-alive
{
"VoiceEnabled":"true"
} |
|---|

| Response Code: 204 |
|---|

| Note | If a request is sent to enable the voiceenabled field and set the search scope to a COS or distribution list, the search scope
                                                      is set to entire server. If the search scope of a directory handler is already a COS or a distribution list and request is sent to set the voiceenabled
                                                      to true, the search scope is set to entire server. |
|---|---|

| URI to get Language code: https://<connection-server>/vmrest/languagemap
URI to Get Language code for installed languages: https://<connection-server>/vmrest/installedlang |
|---|

| UseCallLanguage | UseDefaultLanguage | Language | Description |
|---|---|---|---|
| false | true | Null/Language Code | This will select the default language. |
| true | true/false | Null/Language Code | This will inherit the language from user. |
| false | false | Language Code | This will select the particular language as per the code. |

| PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectid> |
|---|

| <Directoryhandler>
<UseCallLanguage>true</UseCallLanguage>
<UseDefaultLanguage>false</UseDefaultLanguage>
</Directoryhandler> |
|---|

| Response Code: 204 |
|---|

| <Directoryhandler>
<UseCallLanguage>true</UseCallLanguage>
<UseDefaultLanguage>false</UseDefaultLanguage>
<Language>1033</Language>
</Directoryhandler> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryHandlerObjectId>
Accept: application/json
Content-Type: application/json
Connection: keep-alive |
|---|

| {
"UseCallLanguage":"true",
"UseDefaultLanguage":"false",
"Language":"1033"
} |
|---|

| Response Code: 204 |
|---|

| Parameter | Operations | Data Type | Comments |
|---|---|---|---|
| Language | Read/Write | Integer | Specifies the language code. All possible language code values can be fetched using <connection server>/vmrest/languagemap. |
| Display Name | Read/Write | String(64) | The display name of Directory Handler |
| Undeletable | Read/Write | Boolean | Shows whether the Directory Handler can be deleted or not. Values: false: The handler can be deleted by an administrator. true: The handler cannot be deleted by an administrator. Default value: false |
| VoiceName | Read/Write | String(40) | Specifies the .wav file which is the recorded name. |
| VoiceFileURI | Read Only | String | Specifies the URI of the voice file. |
| VoiceNameURI | Read Only | String | Specifies the URI of voice names. |
| LocationObjectId | Read Only | String(36) | The unique identifier of the location object to which this handler belongs. Location, e.g. "Seattle Office." |
| LocationURI | Read Only | String | Specifies the URI of location. |
| EndDialDelay | Read/Write | Integer | The amount of time (in seconds) that Cisco Unity Connection waits after caller input before performing the action indicated
                                             by the input. Value can be in the range 1-10. Default Value: 4. |
| MaxMatches | Read/Write | Integer | The number of matches that if exceeded, will result in Cisco Unity Connection prompting the caller to dial more letters. Value can be in the range 1-30. Default value: 8. |
| MenuStyle | Read/Write | Boolean | A flag indicating how Cisco Unity Connection presents directory matches to callers - either in "menu choice" or "extension
                                             list" format. Note: MenuStyle cannot be set to false for the System Default Directory Handler. Possible values can be: true : menu choice false : extension list. Default value: true. |
| SayExtension | Read/Write | Boolean | A flag indicating whether Cisco Unity Connection provides a menu of subscriber names including extensions, or just subscriber
                                             names. Possible values can be: false: Play only subscriber names in menu list. true: Play subscriber names and extensions in menu list. Default value : true |
| SearchByFirstName | Read/Write | Boolean | A flag indicating whether a directory handler searches for subscribers by using first name first, or last name first. Values: false: Search by last name, then first name. true: Search by first name, then last name. Default value: false. |
| StartDialDelay | Read/Write | Integer | The amount of time (in seconds) that Cisco Unity Connection waits for the caller to start dialing. Default value: 5. Value can be in the range 1-10. |
| Tries | Read/Write | Integer | The number of times Cisco Unity Connection will reprompt the caller for input, e.g. dial name. Default value : 1. Value can be in the range 0-10. |
| UseStarToExit | Read/Write | Boolean | A flag indicating the key on the phone to use for "exit the directory." Values: true: Use star ("*") key to exit directory handler. false: Use pound/hash ("#") key to exit directory handler. Default value: true. |
| SearchScope | Read/Write | Integer | The scope of the directory that Cisco Unity Connection will search. Default value: 0( search scope set as entire server). Possible values : Refer to the SearchScope section under the Enumeration
                                                Type as given at the end of the document |
| SearchScopeObjectId | Read/Write | String(36) | ObjectId of the Search Scope type set. For example : For Class of Service it will be Class Of Service Object ID. |
| ScopeObjectCosObjectId | Read Only | String(36) | Represents a Class of Service(COS) .Only users with this COS will be included in the directory handler. |
| ScopeObjectDistributionListObjectId | Read Only | String(36) | Represents a Distribution List. Only users who are members of this distribution list will be included in the directory handler. |
| ScopeObjectLocationObjectId | Read Only | String(36) | Represents a Cisco Unity Connection Location .Only those users assigned to this location will be included in the directory
                                             handler. |
| ScopeObjectSearchSpaceObjectId | Read Only | String(36) | Represents a Search Space .The unique identifier of the search space which can act as filter for the directory handler. |
| PlayAllNames | Read/Write | Boolean | A flag indicating whether Cisco Unity Connection plays the names of subscribers in the directory for caller selection, rather
                                             than requiring the caller to search by spelled name. Default value: false. |
| ExitAction | Read/Write | Integer | Specifies the exit action. Default Value is 2. Possible Values: Refer to the section Enumeration Type at the end of the document. |
| ExitTargetConversation | Read/Write | String(64) | Specifies the conversation to go to upon exit. Default value is "PHTransfer". Possible Values: Refer to the section Enumeration Type at the end of the document. |
| ExitTargetHandlerObjectId | Read/Write | String(36) | The Unique Identifier of the call action object that Cisco Unity Connection performs if the caller exits the directory handler. |
| NoInputAction | Read/Write | Integer | Specifies the action to be performed if there is no caller Input. Default Value: 2. Possible Values: Refer to the section Enumeration Type at the end of the document. |
| NoInputTargetConversation | Read/Write | String(64) | Specifies the conversation to go when caller gives no Input. Default value is "PHTransfer". Refer to the section Enumeration Type at the end of the document. |
| NoInputTargetHandlerObjectId | Read/Write | String(36) | The unique identifier of the CallAction object that Cisco Unity Connection performs (or the destination to which calls are
                                             sent) if the caller does not enter a name or by not responding to prompts. |
| NoSelectionAction | Read/Write | Integer | Specifies the action to be performed when caller does not select anything. Default Value: 2. Possible Values: Refer to the section Enumeration Type at the end of the document. |
| NoSelectionTargetConversation | Read/Write | String(64) | Specifies the conversation to go when caller does not select anything.Default value is "PHTransfer" . Refer to the section Enumeration Type at the end of the document. |
| NoSelectionTargetHandlerObjectId | Read/Write | String(36) | The unique identifier of the CallAction object that Cisco Unity Connection performs (or the destination to which the caller
                                             is sent to) if the caller makes no selection from a list of matches. |
| ZeroAction | Read/Write | Integer | Specifies the action to be performed for caller input '0'. Default Value: 2 Possible Values: Refer to the section Enumeration Type at the end of the document. |
| ZeroTargetConversation | Read/Write | String(64) | Specifies the conversation when caller presses 0. Default value is "PHTransfer". Refer to the section Enumeration Type at the end of the document. |
| ZeroTargetHandlerObjectId | Read/Write | String(36) | The unique identifier of the CallAction object that Cisco Unity Connection performs if caller presses zero ("0") key during
                                             menu style list of names. |
| AutoRoute | Read/Write | Boolean | Represents how the call should be routed once the matches are found in the Directory. Default value: false. Values: false: Presents a list of matches, even if only one, and prompts the user to verify the match. true: Automatically routes a call to the extension assigned to the subscriber on a unique match without prompting the caller
                                                      to verify the match. |
| ObjectId | Read Only | String(36) | Object Id of the directory handler |
| TenantObjectId | Read Only | String(36) | The unique identifier of the tenant to which the directory handler belongs. This field is reflected in the response only if
                                             the directory handler belongs to a particular tenant. |
| DtmfAccessId | Read/Write | String(40) | Extension of the Directory handler |
| VoiceEnabled | Read/Write | Boolean | A flag indicating whether the directory handler will use voice based addressing rather than touchtones. Default value: false. Values: false: Use touchtones true: Use voice commands |
| UseCallLanguage | Read/Write | Boolean | Specifies if the language as inherited from the call is to be used. Default value is true. |
| UseDefaultLanguage | Read/Write | Boolean | Specifies if the system default language has to be used. Default value is true. |
| PartitionObjectId | Read/Write | String(36) | Object Id of the partition the directory handler belongs to |
| PartitionURI | Read Only | String | URI of partitions |
| SpeechConfidenceThreshold | Read/Write | Integer | When the engine matches a spoken phrase, it associates a confidence level with that conclusion. This parameter determines
                                             what confidence level should be considered a successful match. Default Value is 10. Range of Value is 0 -100 |
| SayCity | Read/Write | Boolean | A flag indicating if the user's city is voiced when a match is voiced. Default value is false. |
| SayDepartment | Read/Write | Boolean | A flag indicating if the user's department is voiced when a match is voiced. Default value is false. |
| UseCustomGreeting | Read/Write | Boolean | Indicates whether to use the directory handler's custom greeting or the system prompt. Default value is false. |
| CreationTime | Read Only | DateTime | Specifies the creation time of the directory handlers. |
| ExitConversationURI | Read Only | String | Specifies the URI to fetch the conversation values which can be used as the ExitConversation |
| NoInputConversationURI | Read Only | String | Specifies the URI to fetch the conversation values which can be used as the NoInputConversation. |
| NoSelectionConversationURI | Read Only | String | Specifies the URI to fetch the conversation values which can be used as the NoSelectionConversation. |
| ZeroExitConversationURI | Read Only | String | Specifies the URI to fetch the conversation values which can be used as the ZeroExitConversation |
| DirectoryHandlerStreamFileURI | Read Only | String | Specifies the URI for the Directory Handler Stream files which are used as the greeting for the Directory Handler. |

| PUT https://<connection-server>/vmrest/directoryhandlers/<DirectoryhandlerObjectId> |
|---|

| <DirectoryHandler>
    <UseCustomGreeting>true<UseCustomGreeting>
</DirectoryHandler> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<DirectoryhandlerObjectId>
Accept: application /json
Content-Type: application/json
Connection: keep-alive |
|---|

| {
    "UseCustomGreeting": "true"
} |
|---|

| Response Code: 204 |
|---|

| GET https://<connection-
  server>/vmrest/handlers/directoryhandlers/<DirectoryHandlerObjectId>/directoryhandlerstreamfiles |
|---|

| <DirectoryHandlerStreamFiles>
  <DirectoryHandlerStreamFile>
    <DirectoryHandlerObjectId>3a0043ab-933b-45f6-852d-e0a261554da2</DirectoryHandlerObjectId>
    <LanguageCode>1033</LanguageCode>
    <StreamFile>5a0c7347-4064-4e94-a9c8-b12426d38f8a.wav</StreamFile>
  </DirectoryHandlerStreamFile>
</DirectoryHandlerStreamFiles> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-
server>/vmrest/handlers/directoryhandlers/<DirectoryHandlerObjectId>/directoryhandlerstreamfiles
Accept: application /json
Connection: keep-alive |
|---|

| {
  "DirectoryHandlerStreamFile": 
  {
    "DirectoryHandlerObjectId": "06628a5c-b755-466d-9e39-66e1956c2242",
    "LanguageCode": "1033",
    "StreamFile": "050590b8-fb8f-4e8d-ab17-4e29eab7d412.wav"
  }
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-
  server>/vmrest/handlers/directoryhandlers/<DirectoryHandlerObjectId>/directoryhandlerstreamfiles
  /1033 |
|---|

| https://<connection-
  server>/vmrest/handlers/directoryhandlers/<DirectoryHandlerObjectId>/directoryhandlerstreamfiles
  /1033/audio |
|---|

| POST https://<connection-server>/vmrest/voicefiles |
|---|

| Response Code: 201 |
|---|

| Request URI:
POST https://<connection-server>/vmrest/voicefiles
Accept: application/json
Content-Type: application/json
Connection: keep-alive |
|---|

| Response Code: 201
Sample Response: 6d9f3b85-c1df-4af8-89f3-6a975ebfb24c.wav |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT https://<connection server>/vmrest/voicefiles/<temporary file name>
Content-Type: audio/wav
Connection: keep-alive |
|---|

| Response Code: 204 |
|---|

| POST https://<connection-
  server>/vmrest/handlers/directoryhandlers/<directoryhandlerObjectId>/directoryhandlerstreamfiles
  /1033
Request Body:
<DirectoryHandlerStreamFile>
    <StreamFile>7acbfec8-25a3-4b02-bd23-2b61acc175c9.wav</StreamFile>
</DirectoryHandlerStreamFile > |
|---|

| Response Code: 201 |
|---|

| Request URI: 
POST https://<connection-server>/vmrest/handlers/directoryhandlers/<directoryhandlerObjectId>/directoryhandlerstreamfiles/1033
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "StreamFile":"050590b8-fb8f-4e8d-ab17-4e29eab7d412.wav"
} |
|---|

| Response Code: 201 |
|---|

| PUT https://<Connection Server>/vmrest/handlers/directoryhandlers/<DirectoryHandlerObjectId>/directoryhandlerstreamfiles/1033/audio
Request Body:
<CallControl>
    <op>RECORD</op>
    <resourceType>STREAM</resourceType>
    <resourceId>67ed783c-203f-454b-a0e6-57b77820c831.wav</resourceId>
    <lastResult>0</lastResult>
    <speed>100</speed>
    <volume>100</volume>
    <startPosition>0</startPosition>
</CallControl> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/directoryhandlers/<DirectoryHandlerObjectId>/directoryhandlerstreamfiles/1033/audio
Accept: application/json
Content-Type: application/json
Connection: keep-alive
Request Body:
{
    "op":"RECORD",
    "resourceType":"STREAM",
    "resourceId":"67ed783c-203f-454b-a0e6-57b77820c831.wav",
    "lastResult":"0",
    "speed":"100",
    "volume":"100",
    "startPosition":"0"
} |
|---|

| Response Code: 204 |
|---|

| RequestURI :
https://<connectionserver>/vmrest/handlers/directoryhandlers/<directoryhandlerobjectid>/directoryhan
dlerstreamfiles/1033/audio. |
|---|

| Parameter | Operations | Data Type | Comments |
|---|---|---|---|
| DirectoryHandlerObjectId | Read Only | String (36) | Object ID of the custom recording. |
| LanguageCode | Read/Write | Integer | Specifies the enumeration type. |
| StreamFile | Read/Write | String (40) | Contains the .wav file that has been sent. |

| Note | To fetch the languages installed on a Unity Connection server,
                                                			 use the following URL: |
|---|---|

| GET https://<connection-server>/vmrest/installedlanguages |
|---|