---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-user-phone-menu-api-html-5b86075d57
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cupi-api-user-phone-menu-api.html
retrieved_at: 2026-08-17T03:48:17.370672+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Phone Menu API

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Phone Menu API

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- User Phone Menu API

Links to Other API pages: Cisco_Unity_Connection_APIs

## Phone Menu
                        	 API

### Listing Phone Menu
                           	 Fields

All the parameters of Phone Menu
                                 		  are present at the URI:

```
GET https://<connection-server>/vmrest/users/<user-objectid>
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<User>
  <URI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1</URI>
  <ObjectId>4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1</ObjectId>
  <UseDefaultLanguage>true</UseDefaultLanguage>
  <Alias>undeliverablemessagesmailbox</Alias>
  <DisplayName>Undeliverable Messages</DisplayName>
  <TimeZone>190</TimeZone>
  <CreationTime>2013-03-05T10:54:38Z</CreationTime>
  <IsTemplate>false</IsTemplate>
  <CosObjectId>610c9c71-32be-4465-b61a-523f24a9d828</CosObjectId>
  <CosURI>/vmrest/coses/610c9c71-32be-4465-b61a-523f24a9d828</CosURI>
  <Language>1033</Language>
  <LocationObjectId>42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationObjectId>
  <LocationURI>/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationURI>
  <AddressMode>0</AddressMode>
  <ClockMode>0</ClockMode>
  <ConversationTui>SubMenu</ConversationTui>
  <GreetByName>true</GreetByName>
  <ListInDirectory>false</ListInDirectory>
  <IsVmEnrolled>true</IsVmEnrolled>
  <SayCopiedNames>true</SayCopiedNames>
  <SayDistributionList>true</SayDistributionList>
  <SayMsgNumber>true</SayMsgNumber>
  <SaySender>true</SaySender>
  <SayTimestampAfter>true</SayTimestampAfter>
  <SayTimestampBefore>false</SayTimestampBefore>
  <SayTotalNew>false</SayTotalNew>
  <SayTotalNewEmail>false</SayTotalNewEmail>
  <SayTotalNewFax>false</SayTotalNewFax>
  <SayTotalNewVoice>true</SayTotalNewVoice>
  <SayTotalReceipts>false</SayTotalReceipts>
  <SayTotalSaved>true</SayTotalSaved>
  <Speed>100</Speed>
  <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
  <PhoneSystemURI>/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150</PhoneSystemURI>
  <Undeletable>true</Undeletable>
  <UseBriefPrompts>false</UseBriefPrompts>
  <Volume>50</Volume>
  <EnAltGreetDontRingPhone>false</EnAltGreetDontRingPhone>
  <EnAltGreetPreventSkip>false</EnAltGreetPreventSkip>
  <EnAltGreetPreventMsg>false</EnAltGreetPreventMsg>
  <EncryptPrivateMessages>false</EncryptPrivateMessages>
  <DeletedMessageSortOrder>2</DeletedMessageSortOrder>
  <SayAltGreetWarning>false</SayAltGreetWarning>
  <SaySenderExtension>false</SaySenderExtension>
  <SayAni>false</SayAni>
  <CallAnswerTimeout>4</CallAnswerTimeout>
  <CallHandlerObjectId>13a3c5fc-f706-4bd0-aeeb-32dad2c4a29b</CallHandlerObjectId>
  <CallhandlerURI>/vmrest/handlers/callhandlers/13a3c5fc-f706-4bd0-aeeb-32dad2c4a29b</CallhandlerURI>
  <MessageTypeMenu>false</MessageTypeMenu>
  <NewMessageSortOrder>1</NewMessageSortOrder>
  <SavedMessageSortOrder>2</SavedMessageSortOrder>
  <MessageLocatorSortOrder>1</MessageLocatorSortOrder>
  <NewMessageStackOrder>1234567</NewMessageStackOrder>
  <SavedMessageStackOrder>1234567</SavedMessageStackOrder>
  <EnablePersonalRules>true</EnablePersonalRules>
  <RecordUnknownCallerName>true</RecordUnknownCallerName>
  <RingPrimaryPhoneFirst>false</RingPrimaryPhoneFirst>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>PHGreeting</ExitTargetConversation>
  <PromptSpeed>100</PromptSpeed>
  <ExitTargetHandlerObjectId>939d4d12-cec8-4fee-ae47-fbf0cf20c33e</ExitTargetHandlerObjectId>
  <RepeatMenu>1</RepeatMenu>
  <FirstDigitTimeout>5000</FirstDigitTimeout>
  <InterdigitDelay>3000</InterdigitDelay>
  <PromptVolume>50</PromptVolume>
  <ExitCallActionObjectId>d6507973-3041-4798-ac83-c6c691cb9187</ExitCallActionObjectId>
  <AddressAfterRecord>false</AddressAfterRecord>
  <DtmfAccessId>99999</DtmfAccessId>
  <ConfirmDeleteMessage>false</ConfirmDeleteMessage>
  <ConfirmDeleteDeletedMessage>false</ConfirmDeleteDeletedMessage>
  <ConfirmDeleteMultipleMessages>true</ConfirmDeleteMultipleMessages>
  <IsClockMode24Hour>false</IsClockMode24Hour>
  <SynchScheduleObjectId>821f40e6-3a97-412c-ae7f-6c7ade9a754b</SynchScheduleObjectId>
  <SynchScheduleURI>/vmrest/schedules/821f40e6-3a97-412c-ae7f-6c7ade9a754b</SynchScheduleURI>
  <RouteNDRToSender>true</RouteNDRToSender>
  <IsSetForVmEnrollment>true</IsSetForVmEnrollment>
  <VoiceNameRequired>false</VoiceNameRequired>
  <SendBroadcastMsg>false</SendBroadcastMsg>
  <UpdateBroadcastMsg>false</UpdateBroadcastMsg>
  <ConversationVui>VuiStart</ConversationVui>
  <ConversationName>SubMenu</ConversationName>
  <SpeechCompleteTimeout>0</SpeechCompleteTimeout>
  <SpeechIncompleteTimeout>750</SpeechIncompleteTimeout>
  <UseVui>false</UseVui>
  <SkipPasswordForKnownDevice>false</SkipPasswordForKnownDevice>
  <JumpToMessagesOnLogin>false</JumpToMessagesOnLogin>
  <UseDefaultTimeZone>true</UseDefaultTimeZone>
  <EnableMessageLocator>false</EnableMessageLocator>
  <AssistantRowsPerPage>5</AssistantRowsPerPage>
  <InboxMessagesPerPage>20</InboxMessagesPerPage>
  <InboxAutoRefresh>15</InboxAutoRefresh>
  <InboxAutoResolveMessageRecipients>true</InboxAutoResolveMessageRecipients>
  <PcaAddressBookRowsPerPage>5</PcaAddressBookRowsPerPage>
  <ReadOnly>false</ReadOnly>
  <EnableTts>true</EnableTts>
  <SmtpAddress>undeliverablemessagesmailbox@ucbu-aricent-vm463.cisco.com</SmtpAddress>
  <ConfirmationConfidenceThreshold>60</ConfirmationConfidenceThreshold>
  <AnnounceUpcomingMeetings>60</AnnounceUpcomingMeetings>
  <SpeechConfidenceThreshold>40</SpeechConfidenceThreshold>
  <SpeechSpeedVsAccuracy>50</SpeechSpeedVsAccuracy>
  <SpeechSensitivity>50</SpeechSensitivity>
  <EnableVisualMessageLocator>false</EnableVisualMessageLocator>
  <ContinuousAddMode>false</ContinuousAddMode>
  <NameConfirmation>false</NameConfirmation>
  <CommandDigitTimeout>1500</CommandDigitTimeout>
  <SaveMessageOnHangup>false</SaveMessageOnHangup>
  <SendMessageOnHangup>1</SendMessageOnHangup>
  <SkipForwardTime>5000</SkipForwardTime>
  <SkipReverseTime>5000</SkipReverseTime>
  <UseShortPollForCache>false</UseShortPollForCache>
  <SearchByExtensionSearchSpaceObjectId>877942bf-6600-4b7a-809d-159199cfc2ec</SearchByExtensionSearchSpaceObjectId>
  <SearchByExtensionSearchSpaceURI>/vmrest/searchspaces/877942bf-6600-4b7a-809d-159199cfc2ec</SearchByExtensionSearchSpaceURI>
  <SearchByNameSearchSpaceObjectId>877942bf-6600-4b7a-809d-159199cfc2ec</SearchByNameSearchSpaceObjectId>
  <SearchByNameSearchSpaceURI>/vmrest/searchspaces/877942bf-6600-4b7a-809d-159199cfc2ec</SearchByNameSearchSpaceURI>
  <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId>
  <PartitionURI>/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionURI>
  <UseDynamicNameSearchWeight>false</UseDynamicNameSearchWeight>
  <LdapType>0</LdapType>
  <CreateSmtpProxyFromCorp>false</CreateSmtpProxyFromCorp>
  <MwisURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/mwis</MwisURI>
  <NotificationDevicesURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/notificationdevices</NotificationDevicesURI>
  <MessageHandlersURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/messagehandlers</MessageHandlersURI>
  <ExternalServiceAccountsURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-                       d48e7e9b73c1/externalserviceaccounts</ExternalServiceAccountsURI>
  <AlternateExtensionsURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/alternateextensions</AlternateExtensionsURI>
  <PrivateListsURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/privatelists</PrivateListsURI>
  <UserWebPasswordURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/credential/password</UserWebPasswordURI>
  <UserVoicePinURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/credential/pin</UserVoicePinURI>
  <SmtpProxyAddressesURI>/vmrest/smtpproxyaddresses?query=(ObjectGlobalUserObjectId%20is%204d5df6e3-a036-4f16-8f1e-d48e7e9b73c1)
  </SmtpProxyAddressesURI>
  <AlternateNamesURI>/vmrest/alternatenames?query=(GlobalUserObjectId%20is%204d5df6e3-a036-4f16-8f1e-d48e7e9b73c1)    </AlternateNamesURI>
</User>
```

```
Response Code: 200
```

### Updating Phone
                           	 menu fields

To update the attributes of Phone
                                 		  Menu, the following steps can be followed:

```
PUT https://<connection-server>/vmrest/users/<user-objectid>
```

```
<User>
  <UseBriefPrompts>true</UseBriefPrompts>
  <PromptVolume>100</PromptVolume>
  <PromptSpeed>100</PromptSpeed>
  <IsClockMode24Hour>false</IsClockMode24Hour>
  <ConversationTui>SubMenu</ConversationTui>
  <MessageLocatorSortOrder>1</MessageLocatorSortOrder>
  <JumpToMessagesOnLogin>false</JumpToMessagesOnLogin>
</User>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Updating
                           	 Conversation fields

Example 1: Edit call actions

```
<User>
  <ExitAction>1</ExitAction>
</User>
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

Example 2: Edit call handler

```
<User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>PHTransfer</ExitTargetConversation>
  <ExitTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</ExitTargetHandlerObjectId>
</User>
```

The following URI can be used to view call handler template object ID:

```
GET https://<connection-server>/vmrest/handlers/callhandlers
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

Example 3: Interview handler

```
<User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>PHInterview</ExitTargetConversation>
  <ExitTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</ExitTargetHandlerObjectId>
</User>
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

Example 4: Directory handler

The following is an example of the GET request that shows the
                                 		  directory handler template object ID:

```
GET https://<connection-server>/vmrest/handlers/directoryhandlers
```

```
<User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>AD</ExitTargetConversation>
  <ExitTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</ExitTargetHandlerObjectId> 
</User>
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

Example 5: Conversation

Request Body: for broadcast message administrator

```
<User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>BroadcastMessageAdministrator</ExitTargetConversation>
</UserTemplate>
```

The following is the response from the *PUT* request for broadcast
                                 		  message administrator and the actual response will depend upon the information
                                 		  given by you:

```
Response Code: 204
```

Request Body: for caller system transfer

```
<User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>SystemTransfer</ExitTargetConversation>
</User>
```

The following is the response from the *PUT* request for caller system
                                 		  transfer and the actual response will depend upon the information given by you:

```
Response Code: 204
```

Request Body: for greeting administrator

```
<User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>GreetingAdministrator</ExitTargetConversation>
</User>
```

The following is the response from the *PUT* request for greeting
                                 		  administrator and the actual response will depend upon the information given by
                                 		  you:

```
Response Code: 204
```

Request Body: for sign in

```
<UserTemplate>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>SubSignIn</ExitTargetConversation>
</UserTemplate>
```

The following is the response from the *PUT* request for sign in and
                                 		  the actual response will depend upon the information given by you:

```
Response Code: 204
```

Request Body: for user system transfer

```
<User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>SubSysTransfer</ExitTargetConversation>
</User>
```

The following is the response from the *PUT* request for user system
                                 		  transfer and the actual response will depend upon the information given by you:

```
Response Code: 204
```

Example 6: Users with Mailbox

```
<User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>PHTransfer</ExitTargetConversation> 
  <ExitTargetHandlerObjectId>71cb381b-fd16-4ba8-8a1d-e71684e57b0e</ExitTargetHandlerObjectId>
</User>
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example To set exit action, do the following:

```
PUT https://<connection-server>/vmrest/users/<userobjectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
{
  "ExitAction":"2",
  "ExitTargetConversation":"SubSysTransfer"
}
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

### Explanation of
                           	 Data Fields

Possible values:

- true: Brief

- false: Full

Possible values:

- 25: Low

- 50: Medium

- 100: High

Default Value: 50

Possible values:

- 50: Slow

- 100: Normal

- 150: Fast

- 200: Fastest

Default Value: 100

Possible values: • true: 24-Hour Clock (00:00 - 23:59) •
                                                						false: 12-Hour Clock (12:00 AM - 11:59 PM) EnableMessageLocator Boolean
                                                						Read/Write A flag indicating whether the message locator feature is enabled for
                                                						the subscriber. Possible Values: • false: Message locator feature is disabled
                                                						for subscriber • true: Message locator feature is enabled for subscriber
                                                						Default Value: false RepeatMenu Integer Read/Write The number of times to
                                                						repeat a menu in touchtone conversation. The range can vary from 0 to 250.
                                                						Default value: 1 ConversationTui String Read/Write The name of the conversation
                                                						the subscriber uses to set up, send, and retrieve messages. Possible values:

- SubMenu: Classic
                                                      						  Conversation

- SubMenu_Alternate_Custom: Custom
                                                      						  keypad mapping1

- SubMenu_Alternate_Custom1: Custom
                                                      						  keypad mapping1

- SubMenu_AlternateN: Alternate Keypad
                                                      						  Mapping(N)

- SubMenu_AlternateS: Alternate Keypad
                                                      						  Mapping(S)

- SubMenu_AlternateX: Alternate Keypad
                                                      						  Mapping (X)

- SubMenuOpt1:
                                                      						  Optional conversation1

- SubMenu_AlternateI: Standard
                                                      						  Conversation

Possible values:

- 1: Last In,
                                                      						  First Out

- 2: First In,
                                                      						  First Out

Default Value: 1

Default value: 5000

Default Value: 3000

Default value: 1500

Possible Values:

- false: Do not
                                                      						  play the name.

- true: Play the
                                                      						  recorded voice name.

Default Value: true

- true- Notify the
                                                      						  subscriber when they login if their alternate greeting is turned on

- false: Do not
                                                      						  notify the subscriber that their alternate greeting is turned on

Default Value: false

Possible values:

- false:
                                                      						  Subscriber conversation does not jump directly to first message in the message
                                                      						  stack after subscriber sign-in.

- true: Subscriber
                                                      						  conversation jumps directly to the first message in the message stack after
                                                      						  subscriber sign-in.

Default Value: true

Possible values: 0-8 Default Value: 0

| GET https://<connection-server>/vmrest/users/<user-objectid> |
|---|

| <User>
  <URI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1</URI>
  <ObjectId>4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1</ObjectId>
  <UseDefaultLanguage>true</UseDefaultLanguage>
  <Alias>undeliverablemessagesmailbox</Alias>
  <DisplayName>Undeliverable Messages</DisplayName>
  <TimeZone>190</TimeZone>
  <CreationTime>2013-03-05T10:54:38Z</CreationTime>
  <IsTemplate>false</IsTemplate>
  <CosObjectId>610c9c71-32be-4465-b61a-523f24a9d828</CosObjectId>
  <CosURI>/vmrest/coses/610c9c71-32be-4465-b61a-523f24a9d828</CosURI>
  <Language>1033</Language>
  <LocationObjectId>42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationObjectId>
  <LocationURI>/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationURI>
  <AddressMode>0</AddressMode>
  <ClockMode>0</ClockMode>
  <ConversationTui>SubMenu</ConversationTui>
  <GreetByName>true</GreetByName>
  <ListInDirectory>false</ListInDirectory>
  <IsVmEnrolled>true</IsVmEnrolled>
  <SayCopiedNames>true</SayCopiedNames>
  <SayDistributionList>true</SayDistributionList>
  <SayMsgNumber>true</SayMsgNumber>
  <SaySender>true</SaySender>
  <SayTimestampAfter>true</SayTimestampAfter>
  <SayTimestampBefore>false</SayTimestampBefore>
  <SayTotalNew>false</SayTotalNew>
  <SayTotalNewEmail>false</SayTotalNewEmail>
  <SayTotalNewFax>false</SayTotalNewFax>
  <SayTotalNewVoice>true</SayTotalNewVoice>
  <SayTotalReceipts>false</SayTotalReceipts>
  <SayTotalSaved>true</SayTotalSaved>
  <Speed>100</Speed>
  <MediaSwitchObjectId>ec1e2636-fc14-44fc-8cda-d6c1a3d61150</MediaSwitchObjectId>
  <PhoneSystemURI>/vmrest/phonesystems/ec1e2636-fc14-44fc-8cda-d6c1a3d61150</PhoneSystemURI>
  <Undeletable>true</Undeletable>
  <UseBriefPrompts>false</UseBriefPrompts>
  <Volume>50</Volume>
  <EnAltGreetDontRingPhone>false</EnAltGreetDontRingPhone>
  <EnAltGreetPreventSkip>false</EnAltGreetPreventSkip>
  <EnAltGreetPreventMsg>false</EnAltGreetPreventMsg>
  <EncryptPrivateMessages>false</EncryptPrivateMessages>
  <DeletedMessageSortOrder>2</DeletedMessageSortOrder>
  <SayAltGreetWarning>false</SayAltGreetWarning>
  <SaySenderExtension>false</SaySenderExtension>
  <SayAni>false</SayAni>
  <CallAnswerTimeout>4</CallAnswerTimeout>
  <CallHandlerObjectId>13a3c5fc-f706-4bd0-aeeb-32dad2c4a29b</CallHandlerObjectId>
  <CallhandlerURI>/vmrest/handlers/callhandlers/13a3c5fc-f706-4bd0-aeeb-32dad2c4a29b</CallhandlerURI>
  <MessageTypeMenu>false</MessageTypeMenu>
  <NewMessageSortOrder>1</NewMessageSortOrder>
  <SavedMessageSortOrder>2</SavedMessageSortOrder>
  <MessageLocatorSortOrder>1</MessageLocatorSortOrder>
  <NewMessageStackOrder>1234567</NewMessageStackOrder>
  <SavedMessageStackOrder>1234567</SavedMessageStackOrder>
  <EnablePersonalRules>true</EnablePersonalRules>
  <RecordUnknownCallerName>true</RecordUnknownCallerName>
  <RingPrimaryPhoneFirst>false</RingPrimaryPhoneFirst>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>PHGreeting</ExitTargetConversation>
  <PromptSpeed>100</PromptSpeed>
  <ExitTargetHandlerObjectId>939d4d12-cec8-4fee-ae47-fbf0cf20c33e</ExitTargetHandlerObjectId>
  <RepeatMenu>1</RepeatMenu>
  <FirstDigitTimeout>5000</FirstDigitTimeout>
  <InterdigitDelay>3000</InterdigitDelay>
  <PromptVolume>50</PromptVolume>
  <ExitCallActionObjectId>d6507973-3041-4798-ac83-c6c691cb9187</ExitCallActionObjectId>
  <AddressAfterRecord>false</AddressAfterRecord>
  <DtmfAccessId>99999</DtmfAccessId>
  <ConfirmDeleteMessage>false</ConfirmDeleteMessage>
  <ConfirmDeleteDeletedMessage>false</ConfirmDeleteDeletedMessage>
  <ConfirmDeleteMultipleMessages>true</ConfirmDeleteMultipleMessages>
  <IsClockMode24Hour>false</IsClockMode24Hour>
  <SynchScheduleObjectId>821f40e6-3a97-412c-ae7f-6c7ade9a754b</SynchScheduleObjectId>
  <SynchScheduleURI>/vmrest/schedules/821f40e6-3a97-412c-ae7f-6c7ade9a754b</SynchScheduleURI>
  <RouteNDRToSender>true</RouteNDRToSender>
  <IsSetForVmEnrollment>true</IsSetForVmEnrollment>
  <VoiceNameRequired>false</VoiceNameRequired>
  <SendBroadcastMsg>false</SendBroadcastMsg>
  <UpdateBroadcastMsg>false</UpdateBroadcastMsg>
  <ConversationVui>VuiStart</ConversationVui>
  <ConversationName>SubMenu</ConversationName>
  <SpeechCompleteTimeout>0</SpeechCompleteTimeout>
  <SpeechIncompleteTimeout>750</SpeechIncompleteTimeout>
  <UseVui>false</UseVui>
  <SkipPasswordForKnownDevice>false</SkipPasswordForKnownDevice>
  <JumpToMessagesOnLogin>false</JumpToMessagesOnLogin>
  <UseDefaultTimeZone>true</UseDefaultTimeZone>
  <EnableMessageLocator>false</EnableMessageLocator>
  <AssistantRowsPerPage>5</AssistantRowsPerPage>
  <InboxMessagesPerPage>20</InboxMessagesPerPage>
  <InboxAutoRefresh>15</InboxAutoRefresh>
  <InboxAutoResolveMessageRecipients>true</InboxAutoResolveMessageRecipients>
  <PcaAddressBookRowsPerPage>5</PcaAddressBookRowsPerPage>
  <ReadOnly>false</ReadOnly>
  <EnableTts>true</EnableTts>
  <SmtpAddress>undeliverablemessagesmailbox@ucbu-aricent-vm463.cisco.com</SmtpAddress>
  <ConfirmationConfidenceThreshold>60</ConfirmationConfidenceThreshold>
  <AnnounceUpcomingMeetings>60</AnnounceUpcomingMeetings>
  <SpeechConfidenceThreshold>40</SpeechConfidenceThreshold>
  <SpeechSpeedVsAccuracy>50</SpeechSpeedVsAccuracy>
  <SpeechSensitivity>50</SpeechSensitivity>
  <EnableVisualMessageLocator>false</EnableVisualMessageLocator>
  <ContinuousAddMode>false</ContinuousAddMode>
  <NameConfirmation>false</NameConfirmation>
  <CommandDigitTimeout>1500</CommandDigitTimeout>
  <SaveMessageOnHangup>false</SaveMessageOnHangup>
  <SendMessageOnHangup>1</SendMessageOnHangup>
  <SkipForwardTime>5000</SkipForwardTime>
  <SkipReverseTime>5000</SkipReverseTime>
  <UseShortPollForCache>false</UseShortPollForCache>
  <SearchByExtensionSearchSpaceObjectId>877942bf-6600-4b7a-809d-159199cfc2ec</SearchByExtensionSearchSpaceObjectId>
  <SearchByExtensionSearchSpaceURI>/vmrest/searchspaces/877942bf-6600-4b7a-809d-159199cfc2ec</SearchByExtensionSearchSpaceURI>
  <SearchByNameSearchSpaceObjectId>877942bf-6600-4b7a-809d-159199cfc2ec</SearchByNameSearchSpaceObjectId>
  <SearchByNameSearchSpaceURI>/vmrest/searchspaces/877942bf-6600-4b7a-809d-159199cfc2ec</SearchByNameSearchSpaceURI>
  <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId>
  <PartitionURI>/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionURI>
  <UseDynamicNameSearchWeight>false</UseDynamicNameSearchWeight>
  <LdapType>0</LdapType>
  <CreateSmtpProxyFromCorp>false</CreateSmtpProxyFromCorp>
  <MwisURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/mwis</MwisURI>
  <NotificationDevicesURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/notificationdevices</NotificationDevicesURI>
  <MessageHandlersURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/messagehandlers</MessageHandlersURI>
  <ExternalServiceAccountsURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-                       d48e7e9b73c1/externalserviceaccounts</ExternalServiceAccountsURI>
  <AlternateExtensionsURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/alternateextensions</AlternateExtensionsURI>
  <PrivateListsURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/privatelists</PrivateListsURI>
  <UserWebPasswordURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/credential/password</UserWebPasswordURI>
  <UserVoicePinURI>/vmrest/users/4d5df6e3-a036-4f16-8f1e-d48e7e9b73c1/credential/pin</UserVoicePinURI>
  <SmtpProxyAddressesURI>/vmrest/smtpproxyaddresses?query=(ObjectGlobalUserObjectId%20is%204d5df6e3-a036-4f16-8f1e-d48e7e9b73c1)
  </SmtpProxyAddressesURI>
  <AlternateNamesURI>/vmrest/alternatenames?query=(GlobalUserObjectId%20is%204d5df6e3-a036-4f16-8f1e-d48e7e9b73c1)    </AlternateNamesURI>
</User> |
|---|

| Response Code: 200 |
|---|

| PUT https://<connection-server>/vmrest/users/<user-objectid> |
|---|

| <User>
  <UseBriefPrompts>true</UseBriefPrompts>
  <PromptVolume>100</PromptVolume>
  <PromptSpeed>100</PromptSpeed>
  <IsClockMode24Hour>false</IsClockMode24Hour>
  <ConversationTui>SubMenu</ConversationTui>
  <MessageLocatorSortOrder>1</MessageLocatorSortOrder>
  <JumpToMessagesOnLogin>false</JumpToMessagesOnLogin>
</User> |
|---|

| Response Code: 204 |
|---|

| <User>
  <ExitAction>1</ExitAction>
</User> |
|---|

| Response Code: 204 |
|---|

| <User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>PHTransfer</ExitTargetConversation>
  <ExitTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</ExitTargetHandlerObjectId>
</User> |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers |
|---|

| Response Code: 204 |
|---|

| <User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>PHInterview</ExitTargetConversation>
  <ExitTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</ExitTargetHandlerObjectId>
</User> |
|---|

| GET https://<connection-server>/vmrest/handlers/interviewhandlers |
|---|

| Response Code: 204 |
|---|

| GET https://<connection-server>/vmrest/handlers/directoryhandlers |
|---|

| <User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>AD</ExitTargetConversation>
  <ExitTargetHandlerObjectId>c1fc1029-55f4-40dc-a553-40b75664ed8a</ExitTargetHandlerObjectId> 
</User> |
|---|

| Response Code: 204 |
|---|

| <User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>BroadcastMessageAdministrator</ExitTargetConversation>
</UserTemplate> |
|---|

| Response Code: 204 |
|---|

| <User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>SystemTransfer</ExitTargetConversation>
</User> |
|---|

| Response Code: 204 |
|---|

| <User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>GreetingAdministrator</ExitTargetConversation>
</User> |
|---|

| Response Code: 204 |
|---|

| <UserTemplate>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>SubSignIn</ExitTargetConversation>
</UserTemplate> |
|---|

| Response Code: 204 |
|---|

| <User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>SubSysTransfer</ExitTargetConversation>
</User> |
|---|

| Response Code: 204 |
|---|

| <User>
  <ExitAction>2</ExitAction>
  <ExitTargetConversation>PHTransfer</ExitTargetConversation> 
  <ExitTargetHandlerObjectId>71cb381b-fd16-4ba8-8a1d-e71684e57b0e</ExitTargetHandlerObjectId>
</User> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/users/<userobjectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive |
|---|

| {
  "ExitAction":"2",
  "ExitTargetConversation":"SubSysTransfer"
} |
|---|

| Response Code: 204 |
|---|

| Field Name | Data Type | Operation | Description |
|---|---|---|---|
| UseBriefPrompts | Boolean | Read/Write | A flag indicating whether the subscriber
                                             					 hears brief or full phone menus when accessing Cisco Unity Connection over the
                                             					 phone. Possible values: true: Brief false: Full |
| PromptVolume | Integer | Read/Write | The volume level for playback of system
                                             					 prompts. The range can vary from 0 to 100. Possible values: 25: Low 50: Medium 100: High Default Value: 50 |
| PromptSpeed | Integer | Read/Write | The audio speed Cisco Unity Connection uses
                                             					 to play back prompts to the subscriber. Possible values: 50: Slow 100: Normal 150: Fast 200: Fastest Default Value: 100 |
| IsClockMode24Hour | Boolean | Read/Write | The time format used for the message
                                             					 timestamps that the subscriber hears when they listen to their messages over
                                             					 the phone. Possible values: • true: 24-Hour Clock (00:00 - 23:59) •
                                                						false: 12-Hour Clock (12:00 AM - 11:59 PM) EnableMessageLocator Boolean
                                                						Read/Write A flag indicating whether the message locator feature is enabled for
                                                						the subscriber. Possible Values: • false: Message locator feature is disabled
                                                						for subscriber • true: Message locator feature is enabled for subscriber
                                                						Default Value: false RepeatMenu Integer Read/Write The number of times to
                                                						repeat a menu in touchtone conversation. The range can vary from 0 to 250.
                                                						Default value: 1 ConversationTui String Read/Write The name of the conversation
                                                						the subscriber uses to set up, send, and retrieve messages. Possible values: SubMenu: Classic
                                                      						  Conversation SubMenu_Alternate_Custom: Custom
                                                      						  keypad mapping1 SubMenu_Alternate_Custom1: Custom
                                                      						  keypad mapping1 SubMenu_AlternateN: Alternate Keypad
                                                      						  Mapping(N) SubMenu_AlternateS: Alternate Keypad
                                                      						  Mapping(S) SubMenu_AlternateX: Alternate Keypad
                                                      						  Mapping (X) SubMenuOpt1:
                                                      						  Optional conversation1 SubMenu_AlternateI: Standard
                                                      						  Conversation |
| MessageLocatorSortOrder | Integer | Read/Write | The order in which system will sort
                                             					 messages when the "Message Locator" feature is enabled. Possible values: 1: Last In,
                                                      						  First Out 2: First In,
                                                      						  First Out Default Value: 1 |
| FirstDigitTimeout | Integer | Read/Write | The amount of time to wait (in
                                             					 milliseconds) for first digit when collecting touchtone. The range can vary
                                             					 from 500 to 10000. Default value: 5000 |
| InterdigitDelay | Integer | Read/Write | The amount of time to wait (in
                                             					 milliseconds) for input between touch tones when collecting digits in touchtone
                                             					 conversation. The range can vary from 1000 to 10000. Default Value: 3000 |
| CommandDigitTimeout | Integer | Read/Write | The amount of time (in milliseconds)
                                             					 between digits on a multiple digit menu command entry (i.e. different than the
                                             					 inter digit timeout that is used for strings of digits such as extensions and
                                             					 transfer strings). The range can vary from 250 to 5000. Default value: 1500 |
| GreetByName | Boolean | Read/Write | A flag indicating whether the subscriber
                                             					 hears his/her name when they log into their mailbox over the phone. Possible Values: false: Do not
                                                      						  play the name. true: Play the
                                                      						  recorded voice name. Default Value: true |
| SayAltGreetWarning | Boolean | Read/Write | A flag indicating whether Cisco Unity
                                             					 Connection notifies the subscriber when they login via the phone (plays
                                             					 conversation) or CPCA (displays a warning banner) if their alternate greeting
                                             					 is turned on. true- Notify the
                                                      						  subscriber when they login if their alternate greeting is turned on false: Do not
                                                      						  notify the subscriber that their alternate greeting is turned on Default Value: false |
| JumpToMessagesOnLogin | Boolean | Read/Write | A flag indicating whether the subscriber
                                             					 conversation jumps directly to the first message in the message stack after
                                             					 subscriber sign-in. Possible values: false:
                                                      						  Subscriber conversation does not jump directly to first message in the message
                                                      						  stack after subscriber sign-in. true: Subscriber
                                                      						  conversation jumps directly to the first message in the message stack after
                                                      						  subscriber sign-in. Default Value: true |
| ExitCallActionObjectId | String(36) | Read Only | The unique identifier of the CallAction
                                             					 object that is taken when a caller exits the subscriber conversation by
                                             					 pressing the * key or timing out. |
| ExitAction | Integer | Read/Write | The type of call action to take, e.g.,
                                             					 hang-up, goto another object, etc. Possible values: 0-8 Default Value: 0 |
| ExitTargetConversation | String(64) | Read/Write | The name of the conversation to which the
                                             					 caller is routed. |
| ExitTargetHandlerObjectId | String(36) | Read Only | The unique identifier of the specific
                                             					 object to send along to the target conversation. |