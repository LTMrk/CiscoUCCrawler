---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cuc-api-user-message-settings-api--bf44559516
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cuc-api-user-message-settings-api.html
retrieved_at: 2026-08-17T03:48:05.212897+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Message Settings
	 API

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Message Settings
	 API

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- User Message Settings
                     	 API

Links to Other API pages: Cisco_Unity_Connection_APIs

## Message Settings
                        	 API

Administrator can use this API to
                              		  create and update the message settings. All the parameters for message settings
                              		  are present in call handler.

```
GET https://<connection-server>/vmrest/users/<user-objectid>
```

From the above URI get the call handler URI:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
```

Please Find below the combination of values to select language for a
                              		  call handler: URI for timezone:

```
https://<connection-server>/vmrest/timezones.
```

URI for installed Languages:

```
https://<connection-server>/vmrest/installedlanguages.
```

URI to get all language codes supported:

```
https://<connection-server>/vmrest/languagemap.
```

### Listing Message
                           	 Settings

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<Callhandler>
  <URI>/vmrest/handlers/callhandlers/287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842</URI>
  <CreationTime>2013-03-05T11:24:33Z</CreationTime>
  <Language>1033</Language>
  <Undeletable>false</Undeletable>
  <LocationObjectId>42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationObjectId>
  <LocationURI>/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationURI>
  <EditMsg>true</EditMsg>
  <IsPrimary>true</IsPrimary>
  <OneKeyDelay>1500</OneKeyDelay>
  <ScheduleSetObjectId>b8a03d12-d425-4cdb-ba36-88e64bf16432</ScheduleSetObjectId>
  <ScheduleSetURI>/vmrest/schedulesets/b8a03d12-d425-4cdb-ba36-88e64bf16432</ScheduleSetURI>
  <SendUrgentMsg>1</SendUrgentMsg>
  <MaxMsgLen>300</MaxMsgLen>
  <IsTemplate>false</IsTemplate>
  <ObjectId>287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842</ObjectId>
  <RecipientSubscriberObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</RecipientSubscriberObjectId>
  <RecipientUserURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</RecipientUserURI>
  <DisplayName>chhaviiiiiii</DisplayName>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>SubSysTransfer</AfterMessageTargetConversation>
  <TimeZone>190</TimeZone>
  <UseDefaultLanguage>false</UseDefaultLanguage>
  <UseDefaultTimeZone>true</UseDefaultTimeZone>
  <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
  <PhoneSystemURI>/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150</PhoneSystemURI>
  <UseCallLanguage>false</UseCallLanguage>
  <SendSecureMsg>true</SendSecureMsg>
  <EnablePrependDigits>false</EnablePrependDigits>
  <DispatchDelivery>false</DispatchDelivery>
  <CallSearchSpaceObjectId>4398317e-3f78-425c-aad8-22d9f818b3dd</CallSearchSpaceObjectId>
  <CallSearchSpaceURI>/vmrest/searchspaces/4398317e-3f78-425c-aad8-22d9f818b3dd</CallSearchSpaceURI>
  <InheritSearchSpaceFromCall>true</InheritSearchSpaceFromCall>
  <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId>
  <PartitionURI>/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionURI>
  <PlayPostGreetingRecording>0</PlayPostGreetingRecording>
  <PostGreetingRecordingObjectId>cc9de0b0-ddfd-479f-9cc1-b3ee14cba6d0</PostGreetingRecordingObjectId>
  <SendPrivateMsg>1</SendPrivateMsg>
  <PlayAfterMessage>1</PlayAfterMessage>
  <GreetingsURI>/vmrest/handlers/callhandlers/287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842/greetings</GreetingsURI>
  <TransferOptionsURI>/vmrest/handlers/callhandlers/287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842/transferoptions</TransferOptionsURI>
  <MenuEntriesURI>/vmrest/handlers/callhandlers/287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842/menuentries</MenuEntriesURI>
  <CallHandlerOwnerURI>/vmrest/handlers/callhandlers/287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842/callhandlerowners
  </CallHandlerOwnerURI>
</Callhandler>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<CallHandlerObjectId>
Accept: application/json
Connection: keep-alive
Response Code: 200
```

### Updating Message
                           	 Settings

The following is an example of
                                 		  the PUT request that updates message settings:

```
PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
```

```
<Callhandler>
  <EditMsg>true</EditMsg>
  <MaxMsgLen>1000</MaxMsgLen>
  <AfterMessageAction>1</AfterMessageAction>
  <SendUrgentMsg>2</SendUrgentMsg>
  <UseCallLanguage>false</UseCallLanguage>
  <SendSecureMsg>false</SendSecureMsg
  <SendPrivateMsg>1</SendPrivateMsg>
  <PlayAfterMessage>2</PlayAfterMessage>
</Callhandler>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
{
  "AfterMessageAction":"2",
  "AfterMessageTargetConversation":"SystemTransfer"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response code: 204
```

### Updating after
                           	 Message Actions

Example 1: Call Handler

```
PUT
https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
```

```
<Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>PHGreeting</AfterMessageTargetConversation>      
  <AfterMessageTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</AfterMessageTargetHandlerObjectId> 
</Callhandler>
```

The following is an example of the GET request that shows the call
                                 		  handler object ID:

```
GET https://<connection-server>/vmrest/handlers/callhandlers
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

Example 2: Interview Handler

```
<Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</AfterMessageTargetHandlerObjectId>
  <AfterMessageTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</AfterMessageTargetHandlerObjectId>
</Callhandler>
```

The following is an example of the GET request that shows the
                                 		  interview handler template object ID:

```
GET https://<connection-server>/vmrest/handlers/interviewhandlers
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

Example 3: Directory Handler

```
<Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>AD</AfterMessageTargetConversation>
  <AfterMessageTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</AfterMessageTargetHandlerObjectId>  
</Callhandler>
```

The following is an example of the GET request that shows the
                                 		  interview handler template object ID:

```
GET https://<connection-server>/vmrest/handlers/directoryhandlers
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

Example 4: Conversation

Request Body: for broadcast message administrator

```
<Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>BroadcastMessageAdministrator</AfterMessageTargetConversation>
</Callhandler>
```

The following is the response from the *PUT* request for broadcast
                                 		  message administrator and the actual response will depend upon the information
                                 		  given by you:

```
Response Code: 204
```

Request Body: for caller system transfer

```
<Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>SystemTransfer</AfterMessageTargetConversation>
</Callhandler>
```

The following is the response from the *PUT* request for caller system
                                 		  transfer and the actual response will depend upon the information given by you:

```
Response Code: 204
```

Request Body: for greeting administrator

```
<Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>GreetingAdministrator</AfterMessageTargetConversation>
</Callhandler>
```

The following is the response from the *PUT* request for greeting
                                 		  administrator and the actual response will depend upon the information given by
                                 		  you:

```
Response Code: 204
```

For sign in

```
<Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>SubSignIn</AfterMessageTargetConversation>
</Callhandler>
```

The following is the response from the *PUT* request for sign in and
                                 		  the actual response will depend upon the information given by you:

```
Response Code: 204
```

For system transfer:

```
Request Body:
<CallhandlerPrimaryTemplate>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>SubSysTransfer</AfterMessageTargetConversation>
</CallhandlerPrimaryTemplate>
```

The following is the response from the *PUT* request for user system
                                 		  transfer and the actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive
Request Body:
{
  "AfterMessageAction":"2",
  "AfterMessageTargetConversation":"SystemTransfer"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Explanation of
                           	 Data Fields

Default value : 300 Range: 1-3600

Values can be: • false: Callers cannot edit messages • true:
                                                						Callers can edit messages Default value: true

- false: The
                                                      						  language is the default language defined for the call handler template.

- true: The
                                                      						  language is derived from the location to which this call handler template
                                                      						  belongs.

Default value: true

Values can be:

- false: Do not
                                                      						  use the language specified by the system call routing rule to play prompts for
                                                      						  users

- true: Use the
                                                      						  language specified by the system call routing rule to play prompts for users

Default value: false

- 0: Never -
                                                      						  messages left by unidentified calls are never marked urgent.

- 1: Always - all
                                                      						  messages left by unidentified callers are marked urgent.

- 2: Ask - Cisco
                                                      						  Unity Connection asks unidentified callers whether to mark their messages
                                                      						  urgent.

Default Value: 0

Values can be:

- 0: Never - No
                                                      						  messages are marked private.

- 1: Always - All
                                                      						  messages are marked private.

- 2: Ask - Ask the
                                                      						  outside caller if they wish to mark the message as private.

Default Value: 0

Values can be:

- false: Never -
                                                      						  messages left by unidentified calls are never marked secure.

- true: Always -
                                                      						  all messages left by unidentified callers are marked secure.

Default Value: false

Values can be:

- 0: Do not play
                                                      						  recording

- 1: System
                                                      						  default recording

- 2: Play
                                                      						  recording

Default value: 0

- 0: Ignore

- 1: Hang up

- 2: Goto

- 3: Error

- 4: TakeMsg

- 5: SkipGreeting

- 6:
                                                      						  RestartGreeting

- 7:
                                                      						  TransferAltContact

- 8: Route from
                                                      						  next call routing rule.

| GET https://<connection-server>/vmrest/users/<user-objectid> |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId> |
|---|

| https://<connection-server>/vmrest/timezones. |
|---|

| https://<connection-server>/vmrest/installedlanguages. |
|---|

| https://<connection-server>/vmrest/languagemap. |
|---|

|  | UseCallLanguage | UseDefaultLanguage | Language |
|---|---|---|---|
| Use System Default Language | false | true | NULL/LanguageCode |
| Inherit Language from Caller | true | true/false | NULL/LanguageCode |
| Particular Language | false | false | Language Code |

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId> |
|---|

| <Callhandler>
  <URI>/vmrest/handlers/callhandlers/287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842</URI>
  <CreationTime>2013-03-05T11:24:33Z</CreationTime>
  <Language>1033</Language>
  <Undeletable>false</Undeletable>
  <LocationObjectId>42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationObjectId>
  <LocationURI>/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationURI>
  <EditMsg>true</EditMsg>
  <IsPrimary>true</IsPrimary>
  <OneKeyDelay>1500</OneKeyDelay>
  <ScheduleSetObjectId>b8a03d12-d425-4cdb-ba36-88e64bf16432</ScheduleSetObjectId>
  <ScheduleSetURI>/vmrest/schedulesets/b8a03d12-d425-4cdb-ba36-88e64bf16432</ScheduleSetURI>
  <SendUrgentMsg>1</SendUrgentMsg>
  <MaxMsgLen>300</MaxMsgLen>
  <IsTemplate>false</IsTemplate>
  <ObjectId>287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842</ObjectId>
  <RecipientSubscriberObjectId>9375d893-c8eb-437b-90bf-7de4b1d0c3e8</RecipientSubscriberObjectId>
  <RecipientUserURI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8</RecipientUserURI>
  <DisplayName>chhaviiiiiii</DisplayName>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>SubSysTransfer</AfterMessageTargetConversation>
  <TimeZone>190</TimeZone>
  <UseDefaultLanguage>false</UseDefaultLanguage>
  <UseDefaultTimeZone>true</UseDefaultTimeZone>
  <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
  <PhoneSystemURI>/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150</PhoneSystemURI>
  <UseCallLanguage>false</UseCallLanguage>
  <SendSecureMsg>true</SendSecureMsg>
  <EnablePrependDigits>false</EnablePrependDigits>
  <DispatchDelivery>false</DispatchDelivery>
  <CallSearchSpaceObjectId>4398317e-3f78-425c-aad8-22d9f818b3dd</CallSearchSpaceObjectId>
  <CallSearchSpaceURI>/vmrest/searchspaces/4398317e-3f78-425c-aad8-22d9f818b3dd</CallSearchSpaceURI>
  <InheritSearchSpaceFromCall>true</InheritSearchSpaceFromCall>
  <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId>
  <PartitionURI>/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionURI>
  <PlayPostGreetingRecording>0</PlayPostGreetingRecording>
  <PostGreetingRecordingObjectId>cc9de0b0-ddfd-479f-9cc1-b3ee14cba6d0</PostGreetingRecordingObjectId>
  <SendPrivateMsg>1</SendPrivateMsg>
  <PlayAfterMessage>1</PlayAfterMessage>
  <GreetingsURI>/vmrest/handlers/callhandlers/287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842/greetings</GreetingsURI>
  <TransferOptionsURI>/vmrest/handlers/callhandlers/287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842/transferoptions</TransferOptionsURI>
  <MenuEntriesURI>/vmrest/handlers/callhandlers/287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842/menuentries</MenuEntriesURI>
  <CallHandlerOwnerURI>/vmrest/handlers/callhandlers/287cdcc0-9f77-48e0-a7b1-0f9b1a5ac842/callhandlerowners
  </CallHandlerOwnerURI>
</Callhandler> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<CallHandlerObjectId>
Accept: application/json
Connection: keep-alive
Response Code: 200 |
|---|

| PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId> |
|---|

| <Callhandler>
  <EditMsg>true</EditMsg>
  <MaxMsgLen>1000</MaxMsgLen>
  <AfterMessageAction>1</AfterMessageAction>
  <SendUrgentMsg>2</SendUrgentMsg>
  <UseCallLanguage>false</UseCallLanguage>
  <SendSecureMsg>false</SendSecureMsg
  <SendPrivateMsg>1</SendPrivateMsg>
  <PlayAfterMessage>2</PlayAfterMessage>
</Callhandler> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
  "AfterMessageAction":"2",
  "AfterMessageTargetConversation":"SystemTransfer"
} |
|---|

| Response code: 204 |
|---|

| PUT
https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId> |
|---|

| <Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>PHGreeting</AfterMessageTargetConversation>      
  <AfterMessageTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</AfterMessageTargetHandlerObjectId> 
</Callhandler> |
|---|

| Response Code: 204 |
|---|

| <Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</AfterMessageTargetHandlerObjectId>
  <AfterMessageTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</AfterMessageTargetHandlerObjectId>
</Callhandler> |
|---|

| GET https://<connection-server>/vmrest/handlers/interviewhandlers |
|---|

| Response Code: 204 |
|---|

| <Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>AD</AfterMessageTargetConversation>
  <AfterMessageTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</AfterMessageTargetHandlerObjectId>  
</Callhandler> |
|---|

| GET https://<connection-server>/vmrest/handlers/directoryhandlers |
|---|

| Response Code: 204 |
|---|

| <Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>BroadcastMessageAdministrator</AfterMessageTargetConversation>
</Callhandler> |
|---|

| Response Code: 204 |
|---|

| <Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>SystemTransfer</AfterMessageTargetConversation>
</Callhandler> |
|---|

| Response Code: 204 |
|---|

| <Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>GreetingAdministrator</AfterMessageTargetConversation>
</Callhandler> |
|---|

| Response Code: 204 |
|---|

| <Callhandler>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>SubSignIn</AfterMessageTargetConversation>
</Callhandler> |
|---|

| Response Code: 204 |
|---|

| Request Body:
<CallhandlerPrimaryTemplate>
  <AfterMessageAction>2</AfterMessageAction>
  <AfterMessageTargetConversation>SubSysTransfer</AfterMessageTargetConversation>
</CallhandlerPrimaryTemplate> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/callhandlers/<CallhandlerObjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive
Request Body:
{
  "AfterMessageAction":"2",
  "AfterMessageTargetConversation":"SystemTransfer"
} |
|---|

| Response Code: 204 |
|---|

| Parameter | Data Type | Operations | Comments |
|---|---|---|---|
| MaxMsgLen | Integer | Read/Write | The maximum recording length (in seconds)
                                             					 for messages left by unidentified callers. Default value : 300 Range: 1-3600 |
| EditMsg | Boolean | Read/Write | Allows callers to be prompted to listen to,
                                             					 add to, rerecord, or delete their messages. Values can be: • false: Callers cannot edit messages • true:
                                                						Callers can edit messages Default value: true |
| UseDefaultLanguage | Boolean | Read/Write | Values can be: false: The
                                                      						  language is the default language defined for the call handler template. true: The
                                                      						  language is derived from the location to which this call handler template
                                                      						  belongs. Default value: true |
| UseCallLanguage | Boolean | Read/Write | This flag allows that language to be the
                                             					 language used by handlers in the system to play prompts for users. Values can be: false: Do not
                                                      						  use the language specified by the system call routing rule to play prompts for
                                                      						  users true: Use the
                                                      						  language specified by the system call routing rule to play prompts for users Default value: false |
| SendUrgentMsg | Integer | Read/Write | A flag indicating whether an unidentified
                                             					 caller can mark a message as "urgent." Values can be: 0: Never -
                                                      						  messages left by unidentified calls are never marked urgent. 1: Always - all
                                                      						  messages left by unidentified callers are marked urgent. 2: Ask - Cisco
                                                      						  Unity Connection asks unidentified callers whether to mark their messages
                                                      						  urgent. Default Value: 0 |
| SendPrivateMsg | Integer | Read/Write | Determines if an outside caller can mark
                                             					 their message as private. Values can be: 0: Never - No
                                                      						  messages are marked private. 1: Always - All
                                                      						  messages are marked private. 2: Ask - Ask the
                                                      						  outside caller if they wish to mark the message as private. Default Value: 0 |
| SendSecureMsg | Boolean | Read/Write | A flag indicating whether an unidentified
                                             					 caller can mark a message as "secure." Values can be: false: Never -
                                                      						  messages left by unidentified calls are never marked secure. true: Always -
                                                      						  all messages left by unidentified callers are marked secure. Default Value: false |
| PlayAfterMessage | Integer | Read/Write | Indicates whether the Sent Message Prompt
                                             					 Recording referenced by Post Greeting Values can be: 0: Do not play
                                                      						  recording 1: System
                                                      						  default recording 2: Play
                                                      						  recording Default value: 0 |
| AfterMessageAction | Integer | Read/Write | AfterMessageAction can only accept integer
                                             					 with the following values: 0: Ignore 1: Hang up 2: Goto 3: Error 4: TakeMsg 5: SkipGreeting 6:
                                                      						  RestartGreeting 7:
                                                      						  TransferAltContact 8: Route from
                                                      						  next call routing rule. |
| AfterMessageTargetHandlerObjectId | String(36) | Read/Write | The unique identifier of the specific
                                             					 object to send along to the target conversation. |
| AfterMessageTargetConversation | String(64) | Read/Write | The name of the conversation to which the
                                             					 caller is routed. |
| Language | Integer | Read/Write | The Windows Locale ID (LCID) that
                                             					 identifies the language that Cisco Unity Connection plays for system prompts |