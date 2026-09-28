---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-user-template-settings-ht-ce81ee4fbf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cupi-api-user-template-settings.html
retrieved_at: 2026-08-17T03:49:19.582312+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API for User Template Settings

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API for User Template Settings

# Cisco Unity Connection Provisioning Interface (CUPI) API for User Template Settings

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Basic User Template
                        	 Information

### About User
                           	 Templates

This page contains information on how to use the API to create, list,
                                 		  modify, and delete user templates. When you create user accounts, you base each
                                 		  account on a user template. Creating new user accounts on a template minimizes
                                 		  the number of settings that must be modified on individual user accounts,
                                 		  making the job of creating user accounts easier.

Cisco Unity Connection comes with predefined user templates too, which you can modify but not delete. For more information
                                 on default user template, see Default User Template section.

### Listing and
                           	 Viewing User Templates

#### Generic Examples
                              	 to List User Templates

Example 1

The following is an example of the GET request that lists all the User
                                    		  Templates:

```
https://<connection_server>/vmrest/usertemplates
```

The following is an example of the response from the above *GET*
                                    		  request and the actual response will depend upon the information given by you:

```
<UserTemplates total="1">
<UserTemplate>
 <URI>/vmrest/usertemplates/7553408b-3415-43db-aa82-3b2dc78062d1</URI>
 <ObjectId>7553408b-3415-43db-aa82-3b2dc78062d1</ObjectId>
 <UseDefaultLanguage>true</UseDefaultLanguage>
 <UseDefaultTimeZone>true</UseDefaultTimeZone>
 <Alias>voicemailusertemplate</Alias>
 <DisplayName>Voice Mail User Template</DisplayName>
 <TimeZone>190</TimeZone>
 <CreationTime>2012-06-25T06:07:31Z</CreationTime>
 <CosObjectId>7be9b3f3-1200-403f-984a-04c07b7c5a7b</CosObjectId>
 <CosURI>/vmrest/coses/7be9b3f3-1200-403f-984a-04c07b7c5a7b</CosURI>
 <Language>1033</Language>
 <LocationObjectId>6d4ff2e5-3f26-4a19-b2fa-beca79b4c5e9</LocationObjectId>
 <LocationURI>
 /vmrest/locations/connectionlocations/6d4ff2e5-3f26-4a19-b2fa- beca79b4c5e9
 </LocationURI>
 <AddressMode>0</AddressMode>
 <ClockMode>0</ClockMode>
 <ConversationTui>SubMenu</ConversationTui>
 <GreetByName>true</GreetByName>
 <ListInDirectory>true</ListInDirectory>
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
 <MediaSwitchObjectId>
 1fb12b1c-cf14-4634-b73d- 9b9c58ecdf68
 </MediaSwitchObjectId>
 <PhoneSystemURI>
 /vmrest/phonesystems/1fb12b1c-cf14-4634-b73d-9b9c58ecdf68
 </PhoneSystemURI>
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
 <ExitCallActionObjectId>
 a365e3c0-d8ed-4874-9810-cedb074dfe33
 </ExitCallActionObjectId>
 <CallAnswerTimeout>4</CallAnswerTimeout>
 <CallHandlerObjectId>f700f378-9656-45ea-94ff-c0462592999e</CallHandlerObjectId>
 <CallhandlerURI>
 /vmrest/callhandlerprimarytemplates/f700f378-9656-45ea-94ff-c0462592999e 
 </CallhandlerURI>
 <DisplayNameRule>1</DisplayNameRule>
 <DoesntExpire>false</DoesntExpire>
 <CantChange>false</CantChange>
 <MailboxStoreObjectId>cfc43112-601b-4764-ba92-b0220e9d7f23</MailboxStoreObjectId>
 <SavedMessageStackOrder>1234567</SavedMessageStackOrder>
 <NewMessageStackOrder>1234567</NewMessageStackOrder>
 <InboxAutoResolveMessageRecipients>true</InboxAutoResolveMessageRecipients>
 <PcaAddressBookRowsPerPage>5</PcaAddressBookRowsPerPage>
 <ReadOnly>false</ReadOnly>
 <EnableTts>true</EnableTts>
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
 <SearchByExtensionSearchSpaceObjectId>
 25e2e004-c194-4593-9961-bdcaf5dd7189
 </SearchByExtensionSearchSpaceObjectId>
 <SearchByExtensionSearchSpaceURI>
 /vmrest/searchspaces/25e2e004-c194-4593-9961-bdcaf5dd7189
 </SearchByExtensionSearchSpaceURI>
 <SearchByNameSearchSpaceObjectId>
 25e2e004-c194-4593-9961-bdcaf5dd7189
 </SearchByNameSearchSpaceObjectId>
 <SearchByNameSearchSpaceURI>
 /vmrest/searchspaces/25e2e004-c194-4593-9961-bdcaf5dd7189
 </SearchByNameSearchSpaceURI>
 <PartitionObjectId>12101df7-ecd2-4a48-b5b9-9a96b5f85a25</PartitionObjectId>
 <PartitionURI>
 /vmrest/partitions/12101df7-ecd2-4a48-b5b9-9a96b5f85a25
 </PartitionURI>
 <UseDynamicNameSearchWeight>false</UseDynamicNameSearchWeight>
 <LdapType>0</LdapType>
 <EnableMessageBookmark>false</EnableMessageBookmark>
 <SayTotalDraftMsg>false</SayTotalDraftMsg>
 <EnableSaveDraft>false</EnableSaveDraft>
 <RetainUrgentMessageFlag>false</RetainUrgentMessageFlag>
 <SayMessageLength>false</SayMessageLength>
 <CreateSmtpProxyFromCorp>false</CreateSmtpProxyFromCorp>
 <AutoAdvanceMsgs>false</AutoAdvanceMsgs>
 <SaySenderAfter>false</SaySenderAfter>
 <SaySenderExtensionAfter>false</SaySenderExtensionAfter>
 <SayMsgNumberAfter>false</SayMsgNumberAfter>
 <SayAniAfter>false</SayAniAfter>
 <SayMessageLengthAfter>false</SayMessageLengthAfter>
 <UserTemplateRolesURI>
 /vmrest/usertemplates/7553408b-3415-43db-aa82-3b2dc78062d1/usertemplateroles
 </UserTemplateRolesURI>
 <UserTemplateNotificationDevicesURI>
 /vmrest/usertemplates/7553408b-3415-43db-aa823b2dc78062d1/usertemplatenotificationdevices
 </UserTemplateNotificationDevicesURI>
 <UserTemplateWebPasswordURI>
 /vmrest/usertemplates/7553408b-3415-43db-aa82-3b2dc78062d1/credential/password
 </UserTemplateWebPasswordURI>
 <UserTemplateVoicePinURI>
 /vmrest/usertemplates/7553408b-3415-43db-aa82-3b2dc78062d1/credential/pin
 </UserTemplateVoicePinURI>
 <UserTemplateMessageActionURI>
 /vmrest/usertemplates/7553408b-3415-43db-aa82-3b2dc78062d1/usertemplatemessageactions
 </UserTemplateMessageActionURI>
</UserTemplate>
```

```
Response Code: 200
```

Example 2

The following is an example of the GET request that lists the User
                                    		  Template as represented by <objectId>:

```
https://<connection_server>/vmrest/usertemplates/<objectId>
```

The following is an example of the response from the above *GET*
                                    		  request and the actual response will depend upon the information given by you:

```
<UserTemplate>
 <URI>
 /vmrest/usertemplates/c8af2544-2bc9-44fa-b713-e80f306cf781
 </URI>
 <ObjectId>
 c8af2544-2bc9-44fa-b713-e80f306cf781
 </ObjectId>
 <UseDefaultLanguage>true</UseDefaultLanguage>
 <UseDefaultTimeZone>true</UseDefaultTimeZone>
 <Alias>NewCiscoTemplate2</Alias>
 <City/>
 <State/>
 <Country>US</Country>
 <PostalCode/>
 <Department/>
 <Manager/>
 <Building/>
 <Address/>
 <DisplayName>testmonica</DisplayName>
 <BillingId/>
 <TimeZone>190</TimeZone>
 <CreationTime>2012-06-26 05:02:22.05</CreationTime>
 <CosObjectId>7be9b3f3-1200-403f-984a-04c07b7c5a7b</CosObjectId>
 <CosURI>/vmrest/coses/7be9b3f3-1200-403f-984a-04c07b7c5a7b</CosURI>
 <Language>1033</Language>
 <LocationObjectId>
 6d4ff2e5-3f26-4a19-b2fa-beca79b4c5e9
 </LocationObjectId>
 <LocationURI>
 /vmrest/locations/connectionlocations/6d4ff2e5-3f26-4a19-b2fa-beca79b4c5e9
 </LocationURI>
 <AddressMode>0</AddressMode>
 <ClockMode>0</ClockMode>
 <ConversationTui>SubMenu</ConversationTui>
 <GreetByName>true</GreetByName>
 <ListInDirectory>true</ListInDirectory>
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
 <MediaSwitchObjectId>
 1fb12b1c-cf14-4634-b73d-9b9c58ecdf68
 </MediaSwitchObjectId>
 <PhoneSystemURI>
 /vmrest/phonesystems/1fb12b1c-cf14-4634-b73d-9b9c58ecdf68
 </PhoneSystemURI>
 <Undeletable>false</Undeletable>
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
 <ExitCallActionObjectId>
 27cbb3a8-f040-4ee9-9686-620c43e3d725
 </ExitCallActionObjectId>
 <CallAnswerTimeout>4</CallAnswerTimeout>
 <CallHandlerObjectId>
 9a5ac35a-0df8-4ebb-8e19-77f936dfd263
 </CallHandlerObjectId>
 <CallhandlerURI>
 /vmrest/callhandlerprimarytemplates/9a5ac35a-0df8-4ebb-8e19-77f936dfd263
 </CallhandlerURI>
 <DisplayNameRule>1</DisplayNameRule>
 <DoesntExpire>false</DoesntExpire>
 <CantChange>false</CantChange>
 <MailboxStoreObjectId>
 cfc43112-601b-4764-ba92-b0220e9d7f23
 </MailboxStoreObjectId>
 <SavedMessageStackOrder>1234567</SavedMessageStackOrder>
 <NewMessageStackOrder>1234567</NewMessageStackOrder>
 <MessageLocatorSortOrder>1</MessageLocatorSortOrder>
 <SavedMessageSortOrder>2</SavedMessageSortOrder>
 <NewMessageSortOrder>1</NewMessageSortOrder>
 <MessageTypeMenu>false</MessageTypeMenu>
 <EnablePersonalRules>true</EnablePersonalRules>
 <RecordUnknownCallerName>true</RecordUnknownCallerName>
 <RingPrimaryPhoneFirst>false</RingPrimaryPhoneFirst>
 <PromptSpeed>100</PromptSpeed>
 <ExitAction>2</ExitAction>
 <ExitTargetConversation>PHTransfer</ExitTargetConversation>
 <ExitTargetHandlerObjectId>
 7ae69f21-1c99-4cc1-96c3-a1bbe11fd4ca
 </ExitTargetHandlerObjectId>
 <RepeatMenu>1</RepeatMenu>
 <FirstDigitTimeout>5000</FirstDigitTimeout>
 <InterdigitDelay>3000</InterdigitDelay>
 <PromptVolume>50</PromptVolume>
 <AddressAfterRecord>false</AddressAfterRecord>
 <ConfirmDeleteMessage>false</ConfirmDeleteMessage>
 <ConfirmDeleteDeletedMessage>false</ConfirmDeleteDeletedMessage>
 <ConfirmDeleteMultipleMessages>true</ConfirmDeleteMultipleMessages>
 <IsClockMode24Hour>false</IsClockMode24Hour>
 <RouteNDRToSender>true</RouteNDRToSender>
 <NotificationType>0</NotificationType>
 <SendReadReceipts>0</SendReadReceipts>
 <ReceiveQuota>-1</ReceiveQuota>
 <SendQuota>-1</SendQuota>
 <WarningQuota>-1</WarningQuota>
 <IsSetForVmEnrollment>true</IsSetForVmEnrollment>
 <VoiceNameRequired>false</VoiceNameRequired>
 <SendBroadcastMsg>true</SendBroadcastMsg>
 <UpdateBroadcastMsg>false</UpdateBroadcastMsg>
 <ConversationVui>VuiStart</ConversationVui>
 <SpeechCompleteTimeout>0</SpeechCompleteTimeout>
 <SpeechIncompleteTimeout>750</SpeechIncompleteTimeout>
 <UseVui>false</UseVui>
 <SkipPasswordForKnownDevice>false</SkipPasswordForKnownDevice>
 <JumpToMessagesOnLogin>true</JumpToMessagesOnLogin>
 <EnableMessageLocator>false</EnableMessageLocator>
 <MessageAgingPolicyObjectId>
 2e02eca6-270b-4b7f-a153-f03ea74d403d
 </MessageAgingPolicyObjectId>
 <MessageAgingPolicyURI>
 /vmrest/messageagingpolicies/2e02eca6-270b-4b7f-a153-f03ea74d403d
 </MessageAgingPolicyURI>
 <AssistantRowsPerPage>5</AssistantRowsPerPage>
 <InboxMessagesPerPage>20</InboxMessagesPerPage>
 <InboxAutoRefresh>15</InboxAutoRefresh>
 <InboxAutoResolveMessageRecipients>true</InboxAutoResolveMessageRecipients>
 <PcaAddressBookRowsPerPage>5</PcaAddressBookRowsPerPage>
 <ReadOnly>false</ReadOnly>
 <EnableTts>true</EnableTts>
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
 <SearchByExtensionSearchSpaceObjectId>
 25e2e004-c194-4593-9961-bdcaf5dd7189
 </SearchByExtensionSearchSpaceObjectId>
 <SearchByExtensionSearchSpaceURI>
 /vmrest/searchspaces/25e2e004-c194-4593-9961-bdcaf5dd7189
 </SearchByExtensionSearchSpaceURI>
 <SearchByNameSearchSpaceObjectId>
 25e2e004-c194-4593-9961-bdcaf5dd7189
 </SearchByNameSearchSpaceObjectId>
 <SearchByNameSearchSpaceURI>
 /vmrest/searchspaces/25e2e004-c194-4593-9961-bdcaf5dd7189
 </SearchByNameSearchSpaceURI>
 <PartitionObjectId>
 12101df7-ecd2-4a48-b5b9-9a96b5f85a25
 </PartitionObjectId>
 <PartitionURI>
 /vmrest/partitions/12101df7-ecd2-4a48-b5b9-9a96b5f85a25 
 </PartitionURI>
 <UseDynamicNameSearchWeight>false</UseDynamicNameSearchWeight>
 <LdapType>0</LdapType>
 <EnableMessageBookmark>false</EnableMessageBookmark>
 <SayTotalDraftMsg>false</SayTotalDraftMsg>
 <EnableSaveDraft>false</EnableSaveDraft>
 <RetainUrgentMessageFlag>false</RetainUrgentMessageFlag>
 <SayMessageLength>false</SayMessageLength>
 <CreateSmtpProxyFromCorp>false</CreateSmtpProxyFromCorp>
 <AutoAdvanceMsgs>false</AutoAdvanceMsgs>
 <SaySenderAfter>false</SaySenderAfter>
 <SaySenderExtensionAfter>false</SaySenderExtensionAfter>
 <SayMsgNumberAfter>false</SayMsgNumberAfter>
 <SayAniAfter>false</SayAniAfter>
 <SayMessageLengthAfter>false</SayMessageLengthAfter>
 <UserTemplateRolesURI>
 /vmrest/usertemplates/c8af2544-2bc9-44fa-b713-e80f306cf781/usertemplateroles
 </UserTemplateRolesURI>
 <UserTemplateNotificationDevicesURI>
 /vmrest/usertemplates/c8af2544-2bc9-44fa-b713-e80f306cf781/usertemplatenotificationdevices
 </UserTemplateNotificationDevicesURI>
 <UserTemplateWebPasswordURI>
 /vmrest/usertemplates/c8af2544-2bc9-44fa-b713-e80f306cf781/credential/password
 </UserTemplateWebPasswordURI>
 <UserTemplateVoicePinURI>
 /vmrest/usertemplates/c8af2544-2bc9-44fa-b713-e80f306cf781/credential/pin
 </UserTemplateVoicePinURI>
 <UserTemplateMessageActionURI>
 /vmrest/usertemplates/c8af2544-2bc9-44fa-b713-e80f306cf781/usertemplatemessageactions
 </UserTemplateMessageActionURI>
</UserTemplate>
```

```
Response Code: 200
```

JSON Examples to List User Templates

Example 1

The following is an example of the GET request that lists all the User
                                    		  Templates:

```
https://<connection_server>/vmrest/usertemplates/
```

The following is an example of the response from the above *GET*
                                    		  request and the actual response will depend upon the information given by you:

```
{
"@total": "2",
"UserTemplate":   
 {
   "URI": "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d",
   "ObjectId": "885dd0af-bdb1-401f-b4e9-6bd9fc8d594d",
   "UseDefaultLanguage": "true",
   "UseDefaultTimeZone": "true",
   "Alias": "voicemailusertemplate",
   "DisplayName": "Voice Mail User Template",
   "TimeZone": "4",
   "CreationTime": "2012-07-29T14:10:26Z",
   "CosObjectId": "362bf7f9-7cec-4f59-86dd-6c058a9100ef",
   "CosURI": "/vmrest/coses/362bf7f9-7cec-4f59-86dd-6c058a9100ef",
   "Language": "1033",
   "LocationObjectId": "3a403c9c-04c8-496a-ba76-23faaaae5a95",
   "LocationURI": 
   "/vmrest/locations/connectionlocations/3a403c9c-04c8-496a-ba76-23faaaae5a95",
   "AddressMode": "0",
   "ClockMode": "0",
   "ConversationTui": "SubMenu",
   "GreetByName": "true",
   "ListInDirectory": "true",
   "IsVmEnrolled": "true",
   "SayCopiedNames": "true",
   "SayDistributionList": "true",
   "SayMsgNumber": "true",
   "SaySender": "true",
   "SayTimestampAfter": "true",
   "SayTimestampBefore": "false",
   "SayTotalNew": "false",
   "SayTotalNewEmail": "false",
   "SayTotalNewFax": "false",
   "SayTotalNewVoice": "true",
   "SayTotalReceipts": "false",
   "SayTotalSaved": "true",
   "Speed": "100",
   "MediaSwitchObjectId": "0d15753c-e1b4-4865-b00b-999a1ccf56ce",
   "PhoneSystemURI": 
   "/vmrest/phonesystems/0d15753c-e1b4-4865-b00b-999a1ccf56ce",
   "Undeletable": "true",
   "UseBriefPrompts": "false",
   "Volume": "50",
   "EnAltGreetDontRingPhone": "false",
   "EnAltGreetPreventSkip": "false",
   "EnAltGreetPreventMsg": "false",
   "EncryptPrivateMessages": "false",
   "DeletedMessageSortOrder": "2",
   "SayAltGreetWarning": "false",
   "SaySenderExtension": "false",
   "SayAni": "false",
   "ExitCallActionObjectId": "6352cf7d-89f8-4748-bac5-8878889c3d56",
   "CallAnswerTimeout": "4",
   "CallHandlerObjectId": "c9069370-3631-4d36-a53a-1ac4e8d8f444",
   "CallhandlerURI": 
   "/vmrest/callhandlerprimarytemplates/c9069370-3631-4d36-a53a-1ac4e8d8f444",
   "DisplayNameRule": "1",
   "DoesntExpire": "false",
   "CantChange": "false",
   "MailboxStoreObjectId": "6d2eb9ad-3caf-41d2-b3db-4451d95057fe",
   "SavedMessageStackOrder": "1234567",
   "NewMessageStackOrder": "1234567",
   "MessageLocatorSortOrder": "1",
   "SavedMessageSortOrder": "2",
   "NewMessageSortOrder": "1",
   "MessageTypeMenu": "false",
   "EnablePersonalRules": "true",
   "RecordUnknownCallerName": "true",
   "RingPrimaryPhoneFirst": "false",
   "PromptSpeed": "100",
   "ExitAction": "2",
   "ExitTargetConversation": "PHGreeting",
   "ExitTargetHandlerObjectId": "708d5a59-95bb-4804-979b-c56b2f7d719a",
   "RepeatMenu": "1",
   "FirstDigitTimeout": "5000",
   "InterdigitDelay": "3000",
   "PromptVolume": "50",
   "DelayAfterGreeting": "0",
   "AddressAfterRecord": "false",
   "ConfirmDeleteMessage": "false",
   "ConfirmDeleteDeletedMessage": "false",
   "ConfirmDeleteMultipleMessages": "true",
   "IsClockMode24Hour": "false",
   "RouteNDRToSender": "true",
   "NotificationType": "0",
   "SendReadReceipts": "1",
   "ReceiveQuota": "2147483647",
   "SendQuota": "2147483647",
   "WarningQuota": "2147483647",
   "IsSetForVmEnrollment": "true",
   "VoiceNameRequired": "false",
   "SendBroadcastMsg": "false",
   "UpdateBroadcastMsg": "false",
   "ConversationVui": "VuiStart",
   "SpeechCompleteTimeout": "0",
   "SpeechIncompleteTimeout": "750",
   "UseVui": "false",
   "SkipPasswordForKnownDevice": "false",
   "JumpToMessagesOnLogin": "true",
   "EnableMessageLocator": "false",
   "MessageAgingPolicyObjectId": "a4b9216a-9360-4f9b-8937-cc66fba0ebbe",
   "MessageAgingPolicyURI": 
   "/vmrest/messageagingpolicies/a4b9216a-9360-4f9b-8937-cc66fba0ebbe",
   "AssistantRowsPerPage": "5",
   "InboxMessagesPerPage": "20",
   "InboxAutoRefresh": "15",
   "InboxAutoResolveMessageRecipients": "true",
   "PcaAddressBookRowsPerPage": "5",
   "ReadOnly": "false",
   "EnableTts": "true",
   "ConfirmationConfidenceThreshold": "60",
   "AnnounceUpcomingMeetings": "60",
   "SpeechConfidenceThreshold": "40",
   "SpeechSpeedVsAccuracy": "50",
   "SpeechSensitivity": "50",
   "EnableVisualMessageLocator": "false",
   "ContinuousAddMode": "false",
   "NameConfirmation": "false",
   "CommandDigitTimeout": "1500",
   "SaveMessageOnHangup": "false",
   "SendMessageOnHangup": "1",
   "SkipForwardTime": "12345",
   "SkipReverseTime": "54321",
   "UseShortPollForCache": "false",
   "SearchByExtensionSearchSpaceObjectId": 
   "a3933806-a995-443e-8704-498c03377bf7",
   "SearchByExtensionSearchSpaceURI": 
   "/vmrest/searchspaces/a3933806-a995-443e-8704-498c03377bf7",
   "SearchByNameSearchSpaceObjectId": 
   "a3933806-a995-443e-8704-498c03377bf7",
   "SearchByNameSearchSpaceURI": 
   "/vmrest/searchspaces/a3933806-a995-443e-8704-498c03377bf7",
   "PartitionObjectId": "6ac064a3-79d6-4a52-a3d3-f4311be5c28c",
   "PartitionURI": 
   "/vmrest/partitions/6ac064a3-79d6-4a52-a3d3-f4311be5c28c",
   "UseDynamicNameSearchWeight": "false",
   "LdapType": "0",
   "EnableMessageBookmark": "false",
   "SayTotalDraftMsg": "false",
   "EnableSaveDraft": "false",
   "RetainUrgentMessageFlag": "false",
   "SayMessageLength": "false",
   "CreateSmtpProxyFromCorp": "false",
   "AutoAdvanceMsgs": "false",
   "SaySenderAfter": "false",
   "SaySenderExtensionAfter": "false",
   "SayMsgNumberAfter": "true",
   "SayAniAfter": "false",
   "SayMessageLengthAfter": "false",
   "UserTemplateRolesURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/usertemplateroles",
   "UserTemplateNotificationDevicesURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/usertemplatenotificationdevices",
   "TemplateExternalServiceAccountsURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/templateexternalserviceaccounts",
   "UserTemplateWebPasswordURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/credential/password",
   "UserTemplateVoicePinURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/credential/pin",
   "UserTemplateMessageActionURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/usertemplatemessageactions",
   "DefaultUserTemplateURI": "/vmrest/userdefaulttemplates"
  },
  {
   "URI": "/vmrest/usertemplates/7426a16f-e735-4854-9ab6-7463728ea4f7",
   "ObjectId": "7426a16f-e735-4854-9ab6-7463728ea4f7",
   "UseDefaultLanguage": "true",
   "UseDefaultTimeZone": "true",
   "Alias": "AdminTest",
   "DisplayName": "Admin test",
   "TimeZone": "4",
   "CreationTime": "2012-08-28T10:57:12Z",
   "CosObjectId": "362bf7f9-7cec-4f59-86dd-6c058a9100ef",
   "CosURI": "/vmrest/coses/362bf7f9-7cec-4f59-86dd-6c058a9100ef",
   "Language": "1033",
   "LocationObjectId": "3a403c9c-04c8-496a-ba76-23faaaae5a95",
   "LocationURI": 
   "/vmrest/locations/connectionlocations/3a403c9c-04c8-496a-ba76-23faaaae5a95",
   "AddressMode": "0",
   "ClockMode": "0",
   "ConversationTui": "SubMenu",
   "GreetByName": "true",
   "ListInDirectory": "true",
   "IsVmEnrolled": "true",
   "SayCopiedNames": "true",
   "SayDistributionList": "true",
   "SayMsgNumber": "true",
   "SaySender": "true",
   "SayTimestampAfter": "true",
   "SayTimestampBefore": "false",
   "SayTotalNew": "false",
   "SayTotalNewEmail": "false",
   "SayTotalNewFax": "false",
   "SayTotalNewVoice": "true",
   "SayTotalReceipts": "false",
   "SayTotalSaved": "true",
   "Speed": "100",
   "MediaSwitchObjectId": "0d15753c-e1b4-4865-b00b-999a1ccf56ce",
   "PhoneSystemURI": 
   "/vmrest/phonesystems/0d15753c-e1b4-4865-b00b-999a1ccf56ce",
   "Undeletable": "false",
   "UseBriefPrompts": "false",
   "Volume": "50",
   "EnAltGreetDontRingPhone": "false",
   "EnAltGreetPreventSkip": "false",
   "EnAltGreetPreventMsg": "false",
   "EncryptPrivateMessages": "false",
   "DeletedMessageSortOrder": "2",
   "SayAltGreetWarning": "false",
   "SaySenderExtension": "false",
   "SayAni": "false",
   "ExitCallActionObjectId": "38d9d3d2-2f70-4e4c-a3bd-54c8e96df9f6",
   "CallAnswerTimeout": "4",
   "CallHandlerObjectId": "ee01a097-2c78-4f36-9400-c0a6e0159419",
   "CallhandlerURI": 
   "/vmrest/callhandlerprimarytemplates/ee01a097-2c78-4f36-9400-c0a6e0159419",
   "DisplayNameRule": "1",
   "DoesntExpire": "false",
   "CantChange": "false",
   "MailboxStoreObjectId": "6d2eb9ad-3caf-41d2-b3db-4451d95057fe",
   "SavedMessageStackOrder": "1234567",
   "NewMessageStackOrder": "1234567",
   "MessageLocatorSortOrder": "1",
   "SavedMessageSortOrder": "2",
   "NewMessageSortOrder": "1",
   "MessageTypeMenu": "false",
   "EnablePersonalRules": "true",
   "RecordUnknownCallerName": "true",
   "RingPrimaryPhoneFirst": "false",
   "PromptSpeed": "100",
   "ExitAction": "2",
   "ExitTargetConversation": "PHGreeting",
   "ExitTargetHandlerObjectId": "708d5a59-95bb-4804-979b-c56b2f7d719a",
   "RepeatMenu": "1",
   "FirstDigitTimeout": "5000",
   "InterdigitDelay": "3000",
   "PromptVolume": "50",
   "DelayAfterGreeting": "0",
   "AddressAfterRecord": "false",
   "ConfirmDeleteMessage": "false",
   "ConfirmDeleteDeletedMessage": "false",
   "ConfirmDeleteMultipleMessages": "true",
   "IsClockMode24Hour": "false",
   "RouteNDRToSender": "true",
   "NotificationType": "0",
   "SendReadReceipts": "1",
   "ReceiveQuota": "2147483647",
   "SendQuota": "2147483647",
   "WarningQuota": "2147483647",
   "IsSetForVmEnrollment": "true",
   "VoiceNameRequired": "false",
   "SendBroadcastMsg": "false",
   "UpdateBroadcastMsg": "false",
   "ConversationVui": "VuiStart",
   "SpeechCompleteTimeout": "0",
   "SpeechIncompleteTimeout": "750",
   "UseVui": "false",
   "SkipPasswordForKnownDevice": "false",
   "JumpToMessagesOnLogin": "true",
   "EnableMessageLocator": "false",
   "MessageAgingPolicyObjectId": "a4b9216a-9360-4f9b-8937-cc66fba0ebbe",
   "MessageAgingPolicyURI": 
   "/vmrest/messageagingpolicies/a4b9216a-9360-4f9b-8937-cc66fba0ebbe",
   "AssistantRowsPerPage": "5",
   "InboxMessagesPerPage": "20",
   "InboxAutoRefresh": "15",
   "InboxAutoResolveMessageRecipients": "true",
   "PcaAddressBookRowsPerPage": "5",
   "ReadOnly": "false",
   "EnableTts": "true",
   "ConfirmationConfidenceThreshold": "60",
   "AnnounceUpcomingMeetings": "60",
   "SpeechConfidenceThreshold": "40",
   "SpeechSpeedVsAccuracy": "50",
   "SpeechSensitivity": "50",
   "EnableVisualMessageLocator": "false",
   "ContinuousAddMode": "false",
   "NameConfirmation": "false",
   "CommandDigitTimeout": "1500",
   "SaveMessageOnHangup": "false",
   "SendMessageOnHangup": "1",
   "SkipForwardTime": "12345",
   "SkipReverseTime": "54321",
   "UseShortPollForCache": "false",
   "SearchByExtensionSearchSpaceObjectId": 
   "a3933806-a995-443e-8704-498c03377bf7",
   "SearchByExtensionSearchSpaceURI": 
   "/vmrest/searchspaces/a3933806-a995-443e-8704-498c03377bf7",
   "SearchByNameSearchSpaceObjectId": 
   "a3933806-a995-443e-8704-498c03377bf7",
   "SearchByNameSearchSpaceURI": 
   "/vmrest/searchspaces/a3933806-a995-443e-8704-498c03377bf7",
   "PartitionObjectId": 
   "6ac064a3-79d6-4a52-a3d3-f4311be5c28c",
   "PartitionURI": 
   "/vmrest/partitions/6ac064a3-79d6-4a52-a3d3-f4311be5c28c",
   "UseDynamicNameSearchWeight": "false",
   "LdapType": "0",
   "EnableMessageBookmark": "false",
   "SayTotalDraftMsg": "false",
   "EnableSaveDraft": "false",
   "RetainUrgentMessageFlag": "false",
   "SayMessageLength": "false",
   "CreateSmtpProxyFromCorp": "false",
   "AutoAdvanceMsgs": "false",
   "SaySenderAfter": "false",
   "SaySenderExtensionAfter": "false",
   "SayMsgNumberAfter": "true",
   "SayAniAfter": "false",
   "SayMessageLengthAfter": "false",
   "UserTemplateRolesURI": 
   "/vmrest/usertemplates/7426a16f-e735-4854-9ab6-7463728ea4f7/usertemplateroles",
   "UserTemplateNotificationDevicesURI": 
   "/vmrest/usertemplates/7426a16f-e735-4854-9ab6-7463728ea4f7/usertemplatenotificationdevices",
   "TemplateExternalServiceAccountsURI": 
   "/vmrest/usertemplates/7426a16f-e735-4854-9ab6-7463728ea4f7/templateexternalserviceaccounts",
   "UserTemplateWebPasswordURI": 
   "/vmrest/usertemplates/7426a16f-e735-4854-9ab6-7463728ea4f7/credential/password",
   "UserTemplateVoicePinURI": 
   "/vmrest/usertemplates/7426a16f-e735-4854-9ab6-7463728ea4f7/credential/pin",
   "UserTemplateMessageActionURI": 
   "/vmrest/usertemplates/7426a16f-e735-4854-9ab6-7463728ea4f7/usertemplatemessageactions",
   "DefaultUserTemplateURI": "/vmrest/userdefaulttemplates"
  }
  
}
```

```
Response Code: 200
```

Example 2

The following is an example of the GET request that lists the User
                                    		  Template as represented by <objectId>:

```
https://<connection_server>/vmrest/usertemplates/<objectId>
```

The following is an example of the response from the above *GET*
                                    		  request and the actual response will depend upon the information given by you:

```
{
   "URI": "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d",
   "ObjectId": "885dd0af-bdb1-401f-b4e9-6bd9fc8d594d",
   "UseDefaultLanguage": "true",
   "UseDefaultTimeZone": "true",
   "Alias": "voicemailusertemplate",
   "DisplayName": "Voice Mail User Template",
   "TimeZone": "4",
   "CreationTime": "2012-07-29T14:10:26Z",
   "CosObjectId": "362bf7f9-7cec-4f59-86dd-6c058a9100ef",
   "CosURI": "/vmrest/coses/362bf7f9-7cec-4f59-86dd-6c058a9100ef",
   "Language": "1033",
   "LocationObjectId": "3a403c9c-04c8-496a-ba76-23faaaae5a95",
   "LocationURI": 
   "/vmrest/locations/connectionlocations/3a403c9c-04c8-496a-ba76-23faaaae5a95",
   "AddressMode": "0",
   "ClockMode": "0",
   "ConversationTui": "SubMenu",
   "GreetByName": "true",
   "ListInDirectory": "true",
   "IsVmEnrolled": "true",
   "SayCopiedNames": "true",
   "SayDistributionList": "true",
   "SayMsgNumber": "true",
   "SaySender": "true",
   "SayTimestampAfter": "true",
   "SayTimestampBefore": "false",
   "SayTotalNew": "false",
   "SayTotalNewEmail": "false",
   "SayTotalNewFax": "false",
   "SayTotalNewVoice": "true",
   "SayTotalReceipts": "false",
   "SayTotalSaved": "true",
   "Speed": "100",
   "MediaSwitchObjectId": "0d15753c-e1b4-4865-b00b-999a1ccf56ce",
   "PhoneSystemURI": 
   "/vmrest/phonesystems/0d15753c-e1b4-4865-b00b-999a1ccf56ce",
   "Undeletable": "true",
   "UseBriefPrompts": "false",
   "Volume": "50",
   "EnAltGreetDontRingPhone": "false",
   "EnAltGreetPreventSkip": "false",
   "EnAltGreetPreventMsg": "false",
   "EncryptPrivateMessages": "false",
   "DeletedMessageSortOrder": "2",
   "SayAltGreetWarning": "false",
   "SaySenderExtension": "false",
   "SayAni": "false",
   "ExitCallActionObjectId": "6352cf7d-89f8-4748-bac5-8878889c3d56",
   "CallAnswerTimeout": "4",
   "CallHandlerObjectId": "c9069370-3631-4d36-a53a-1ac4e8d8f444",
   "CallhandlerURI": 
   "/vmrest/callhandlerprimarytemplates/c9069370-3631-4d36-a53a-1ac4e8d8f444",
   "DisplayNameRule": "1",
   "DoesntExpire": "false",
   "CantChange": "false",
   "MailboxStoreObjectId": "6d2eb9ad-3caf-41d2-b3db-4451d95057fe",
   "SavedMessageStackOrder": "1234567",
   "NewMessageStackOrder": "1234567",
   "MessageLocatorSortOrder": "1",
   "SavedMessageSortOrder": "2",
   "NewMessageSortOrder": "1",
   "MessageTypeMenu": "false",
   "EnablePersonalRules": "true",
   "RecordUnknownCallerName": "true",
   "RingPrimaryPhoneFirst": "false",
   "PromptSpeed": "100",
   "ExitAction": "2",
   "ExitTargetConversation": "PHGreeting",
   "ExitTargetHandlerObjectId": "708d5a59-95bb-4804-979b-c56b2f7d719a",
   "RepeatMenu": "1",
   "FirstDigitTimeout": "5000",
   "InterdigitDelay": "3000",
   "PromptVolume": "50",
   "AddressAfterRecord": "false",
   "ConfirmDeleteMessage": "false",
   "ConfirmDeleteDeletedMessage": "false",
   "ConfirmDeleteMultipleMessages": "true",
   "IsClockMode24Hour": "false",
   "RouteNDRToSender": "true",
   "NotificationType": "0",
   "SendReadReceipts": "1",
   "ReceiveQuota": "2147483647",
   "SendQuota": "2147483647",
   "WarningQuota": "2147483647",
   "IsSetForVmEnrollment": "true",
   "VoiceNameRequired": "false",
   "SendBroadcastMsg": "false",
   "UpdateBroadcastMsg": "false",
   "ConversationVui": "VuiStart",
   "SpeechCompleteTimeout": "0",
   "SpeechIncompleteTimeout": "750",
   "UseVui": "false",
   "SkipPasswordForKnownDevice": "false",
   "JumpToMessagesOnLogin": "true",
   "EnableMessageLocator": "false",
   "MessageAgingPolicyObjectId": "a4b9216a-9360-4f9b-8937-cc66fba0ebbe",
   "MessageAgingPolicyURI": 
   "/vmrest/messageagingpolicies/a4b9216a-9360-4f9b-8937-cc66fba0ebbe",
   "AssistantRowsPerPage": "5",
   "InboxMessagesPerPage": "20",
   "InboxAutoRefresh": "15",
   "InboxAutoResolveMessageRecipients": "true",
   "PcaAddressBookRowsPerPage": "5",
   "ReadOnly": "false",
   "EnableTts": "true",
   "ConfirmationConfidenceThreshold": "60",
   "AnnounceUpcomingMeetings": "60",
   "SpeechConfidenceThreshold": "40",
   "SpeechSpeedVsAccuracy": "50",
   "SpeechSensitivity": "50",
   "EnableVisualMessageLocator": "false",
   "ContinuousAddMode": "false",
   "NameConfirmation": "false",
   "CommandDigitTimeout": "1500",
   "SaveMessageOnHangup": "false",
   "SendMessageOnHangup": "1",
   "SkipForwardTime": "12345",
   "SkipReverseTime": "54321",
   "UseShortPollForCache": "false",
   "SearchByExtensionSearchSpaceObjectId": 
   "a3933806-a995-443e-8704-498c03377bf7",
   "SearchByExtensionSearchSpaceURI": 
   "/vmrest/searchspaces/a3933806-a995-443e-8704-498c03377bf7",
   "SearchByNameSearchSpaceObjectId": 
   "a3933806-a995-443e-8704-498c03377bf7",
   "SearchByNameSearchSpaceURI": 
   "/vmrest/searchspaces/a3933806-a995-443e-8704-498c03377bf7",
   "PartitionObjectId": 
   "6ac064a3-79d6-4a52-a3d3-f4311be5c28c",
   "PartitionURI": 
   "/vmrest/partitions/6ac064a3-79d6-4a52-a3d3-f4311be5c28c",
   "UseDynamicNameSearchWeight": "false",
   "LdapType": "0",
   "EnableMessageBookmark": "false",
   "SayTotalDraftMsg": "false",
   "EnableSaveDraft": "false",
   "RetainUrgentMessageFlag": "false",
   "SayMessageLength": "false",
   "CreateSmtpProxyFromCorp": "false",
   "AutoAdvanceMsgs": "false",
   "SaySenderAfter": "false",
   "SaySenderExtensionAfter": "false",
   "SayMsgNumberAfter": "true",
   "SayAniAfter": "false",
   "SayMessageLengthAfter": "false",
   "UserTemplateRolesURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/usertemplateroles",
   "UserTemplateNotificationDevicesURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/usertemplatenotificationdevices",
   "TemplateExternalServiceAccountsURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/templateexternalserviceaccounts",
   "UserTemplateWebPasswordURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/credential/password",
   "UserTemplateVoicePinURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/credential/pin",
   "UserTemplateMessageActionURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/usertemplatemessageactions",
   "DefaultUserTemplateURI": "/vmrest/userdefaulttemplates"
}
```

```
Response Code: 200
```

#### Adding User
                              	 Template

Example 1

The following is an example of the POST request that adds the User
                                    		  Templates:

```
https://<connection_server>/vmrest/usertemplates?templateAlias=voicemailusertemplate
```

The following is an example of the response from the above *POST*
                                    		  request and the actual response will depend upon the information given by you:

```
<UserTemplate>
 <DisplayName>DemoUserTemplate</DisplayName>
 <Alias>DemoUserTemplate</Alias>
</UserTemplate>
```

```
Response Code: 201
```

Example 2

The following is a JSON example of the POST request that adds the User
                                    		  Templates:

```
https://<connection_server>/vmrest/usertemplates?templateAlias=voicemailusertemplate
```

The following is an example of the response from the above *POST*
                                    		  request and the actual response will depend upon the information given by you:

```
{
  "Alias": "adminTemplate1",
  "DisplayName": "Admin Voice Mail Template"
   
}
```

```
Response Code: 201
```

#### Modifying a User
                              	 Template

Example 1

The following is an example of the PUT request that modifies the user
                                    		  template as represented by <objectId>:

```
https://<connection_server>/vmrest/usertemplate/<objectId>
```

The following is an example of the response from the above *PUT*
                                    		  request and the actual response will depend upon the information given by you:

```
<UserTemplate>
 <SendBroadcastMsg>true</SendBroadcastMsg>
 <GreetByName>true</GreetByName>
 <ListInDirectory>true</ListInDirectory>
 <IsVmEnrolled>true</IsVmEnrolled>
 <SayCopiedNames>true</SayCopiedNames>
 <SayDistributionList>true</SayDistributionList>
 <SayMsgNumber>true</SayMsgNumber>
</UserTemplate>
```

```
Response Code: 204
```

Example 2

The following is a JSON example of the PUT request that modifies the
                                    		  user template as represented by <objectId>:

```
https://<connection_server>/vmrest/usertemplate/<objectId>
```

The following is an example of the response from the above *PUT*
                                    		  request and the actual response will depend upon the information given by you:

```
{
 "SendBroadcastMsg" : "true",
 "GreetByName" : "true",
 "ListInDirectory" : "true",
 "IsVmEnrolled" : "true"
 "SayCopiedNames" : "true",
 "SayDistributionList" : "true",
 "SayMsgNumber" :"true"
}
```

```
Response Code: 204
```

You can also modify the following for a user template:

- User Template Voicemail PIN

- User Template Transfer Options

- User Template Caller Input

- User Template Greetings

- User Template Notification Devices

- User Template External Services

- User Template External Service Accounts

#### Deleting User
                              	 Templates

The following is an example of
                                    		  the DELETE request that deletes a User Template as represented by
                                    		  <objectId>:

```
https://<connection_server>/vmrest/usertemplates/<objectId>
```

The output for this request returns the successful response code.

```
Response Code: 204
```

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Default User Template

### About Default
                           	 Templates

This section contains information on how to list and modify default User
                              		Templates. Cisco Unity Connection comes with the following predefined user
                              		templates, which you can modify but not delete:

- Voice Mail User Template

- Administrator Template

### Listing Default
                           	 Templates

Example 1

The following is an example of the GET request that lists the default
                                 		  User Templates:

```
https://<connection_server>/vmrest/userdefaulttemplates
```

The following is an example of the response from the above *GET*
                                 		  request and the actual response will depend upon the information given by you:

```
<DefaultUserTemplates total="2">
<DefaultUserTemplate>
 <URI>
  /vmrest/defaultusertemplates/48caecef-6f7a-47aa-91cb-019b761fce69
 </URI>
 <ObjectId>48caecef-6f7a-47aa-91cb-019b761fce69</ObjectId>
 <UseDefaultLanguage>true</UseDefaultLanguage>
 <UseDefaultTimeZone>true</UseDefaultTimeZone>
 <Alias>administratortemplate1</Alias>
 <City/>
 <State/>
 <Country>US</Country>
 <PostalCode/>
 <Department/>
 <Building/>
 <Address/>
 <DisplayName>Administrator Template</DisplayName>
 <BillingId/>
 <TimeZone>190</TimeZone>
 <CreationTime>2012-07-09T07:27:43Z</CreationTime>
 <Language>1033</Language>
 <LocationObjectId>be27976c-6e6e-419f-853d-b3764881dfb0</LocationObjectId>
 <LocationURI>
  /vmrest/locations/connectionlocations/be27976c-6e6e-419f-853d-b3764881dfb0
 </LocationURI>
 <DisplayNameRule>1</DisplayNameRule>
 <DoesntExpire>false</DoesntExpire>
 <CantChange>false</CantChange>
 <RouteNDRToSender>true</RouteNDRToSender>
 <Undeletable>true</Undeletable>
 <ReadOnly>false</ReadOnly>
 <PartitionObjectId>c2ecf6c5-b3c2-45f4-99fc-e065056501d5</PartitionObjectId>
 <PartitionURI>
  /vmrest/partitions/c2ecf6c5-b3c2-45f4-99fc-e065056501d5
 </PartitionURI>
 <LdapType>0</LdapType>
 <CreateSmtpProxyFromCorp>false</CreateSmtpProxyFromCorp>
 <DefaultUserTemplateWebPasswordURI>
 /vmrest/usertemplates/48caecef-6f7a-47aa-91cb-019b761fce69/credential/password
 </DefaultUserTemplateWebPasswordURI>
 <DefaultUserTemplateVoicePinURI>
 /vmrest/usertemplates/48caecef-6f7a-47aa-91cb-019b761fce69/credential/pin
 </DefaultUserTemplateVoicePinURI>
</DefaultUserTemplate>
<DefaultUserTemplate>
 <URI>
 /vmrest/defaultusertemplates/bc0eedd5-0483-4362-a091-5f89d27b7b3c
 </URI>
 <ObjectId>bc0eedd5-0483-4362-a091-5f89d27b7b3c</ObjectId>
 <UseDefaultLanguage>true</UseDefaultLanguage>
 <UseDefaultTimeZone>true</UseDefaultTimeZone>
 <Alias>voicemailusertemplate</Alias>
 <DisplayName>Voice Mail User Template</DisplayName>
 <TimeZone>190</TimeZone>
 <CreationTime>2012-07-09T07:27:44Z</CreationTime>
 <CosObjectId>305a9699-03a8-41d0-9215-0fcd32d600b0</CosObjectId>
 <CosURI>/vmrest/coses/305a9699-03a8-41d0-9215-0fcd32d600b0</CosURI>
 <Language>1033</Language>
 <LocationObjectId>be27976c-6e6e-419f-853d-b3764881dfb0</LocationObjectId>
 <LocationURI>
 /vmrest/locations/connectionlocations/be27976c-6e6e-419f-853d-b3764881dfb0
 </LocationURI>
 <DisplayNameRule>1</DisplayNameRule>
 <DoesntExpire>false</DoesntExpire>
 <CantChange>false</CantChange>
 <MailboxStoreObjectId>15dd71c8-2ba1-4efa-a34e-01613a0d2ef7</MailboxStoreObjectId>
 <RouteNDRToSender>true</RouteNDRToSender>
 <Undeletable>true</Undeletable>
 <ReadOnly>false</ReadOnly>
 <PartitionObjectId>c2ecf6c5-b3c2-45f4-99fc-e065056501d5</PartitionObjectId>
 <PartitionURI>
  /vmrest/partitions/c2ecf6c5-b3c2-45f4-99fc-e065056501d5
 </PartitionURI>
 <LdapType>0</LdapType>
 <CreateSmtpProxyFromCorp>false</CreateSmtpProxyFromCorp>
 <DefaultUserTemplateWebPasswordURI>
  /vmrest/usertemplates/bc0eedd5-0483-4362-a091-5f89d27b7b3c/credential/password
 </DefaultUserTemplateWebPasswordURI>
 <DefaultUserTemplateVoicePinURI>
 /vmrest/usertemplates/bc0eedd5-0483-4362-a091-5f89d27b7b3c/credential/pin
 </DefaultUserTemplateVoicePinURI>
</DefaultUserTemplate>
</DefaultUserTemplates>
```

```
Response code: 200
```

Example 2

The following is an example of the GET request that lists a specified
                                 		  default User Templates:

```
https://<connection_server>/vmrest/userdefaulttemplates/<objectId>
```

The following is an example of the response from the above *GET*
                                 		  request and the actual response will depend upon the information given by you:

```
<DefaultUserTemplate>
 <URI>
  /vmrest/defaultusertemplates/48caecef-6f7a-47aa-91cb-019b761fce69
 </URI>
 <TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
 <UseDefaultLanguage>true</UseDefaultLanguage>
 <UseDefaultTimeZone>true</UseDefaultTimeZone>
 <Alias>administratortemplate1</Alias>
 <City/>
 <State/>
 <Country>US</Country>
 <PostalCode/>
 <Department/>
 <Building/>
 <Address/>
 <DisplayName>Administrator Template</DisplayName>
 <BillingId/>
 <TimeZone>190</TimeZone>
 <CreationTime>2012-07-09T07:27:43Z</CreationTime>
 <Language>1033</Language>
 <LocationObjectId>be27976c-6e6e-419f-853d-b3764881dfb0</LocationObjectId>
 <LocationURI>
  /vmrest/locations/connectionlocations/be27976c-6e6e-419f-853d-b3764881dfb0
 </LocationURI>
 <DisplayNameRule>1</DisplayNameRule>
 <DoesntExpire>false</DoesntExpire>
 <CantChange>false</CantChange>
 <RouteNDRToSender>true</RouteNDRToSender>
 <Undeletable>true</Undeletable>
 <ReadOnly>false</ReadOnly>
 <PartitionObjectId>c2ecf6c5-b3c2-45f4-99fc-e065056501d5</PartitionObjectId>
 <PartitionURI>
  /vmrest/partitions/c2ecf6c5-b3c2-45f4-99fc-e065056501d5
 </PartitionURI>
 <LdapType>0</LdapType>
 <CreateSmtpProxyFromCorp>false</CreateSmtpProxyFromCorp>
 <DefaultUserTemplateWebPasswordURI>
  /vmrest/usertemplates/48caecef-6f7a-47aa-91cb-019b761fce69/credential/password
 </DefaultUserTemplateWebPasswordURI>
 <DefaultUserTemplateVoicePinURI>
  /vmrest/usertemplates/48caecef-6f7a-47aa-91cb-019b761fce69/credential/pin
 </DefaultUserTemplateVoicePinURI>
 </DefaultUserTemplate>
```

```
Response code: 200
```

### Modifying Default
                           	 Templates

The following is an example of
                                 		  the PUT request that modifies the Default User Templates:

```
https://<connection_server>/vmrest/userdefaulttemplates/<objectId>
```

The actual response will depend upon the information given by you.

```
<DefaultUserTemplate>
 <City>San Jose</City>
 <State>CA</State>
 <Country>US</Country>
</DefaultUserTemplate>
```

```
Response code: 204
```

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- User Template VoiceMail PIN

### Changing User
                           	 Template Voicemail PIN

The following is an example of
                                 		  the PUT request that modifies the user template Voicemail PIN represented by
                                 		  <objectId>:

```
https://<connection_server>/vmrest/usertemplates/<objectId>/credential/pin
```

The following is an example of the response from the above *PUT*
                                 		  request and the actual response will depend upon the information given by you:

```
<UserTemplateCredential>
 <Credentials>abcd@1234</Credentials>
</UserTemplateCredential>
```

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- User Template Transfer Options

### About Transfer
                           	 Options

Every user template with a mailbox
                              		has an associated call handler template, and thus transfers options. Transfer
                              		Options are also referred to as Transfer Rules.

### Listing and
                           	 Viewing

The settings on each transfer
                                 		  option can be read by the GET command. Perform the following steps to list the
                                 		  transfer options for a user template:

Step 1

Do the following GET command
                                          			 to list all the user templates:

```
https://<connection_server>/vmrest/usertemplates
```

Step 2

Do the following GET command
                                          			 to list the user template of your choice represented by the
                                          			 <usertemplate-id>:

```
https://<connection_server>/vmrest/usertemplates/<objectId>
```

Step 3

The following URI is the
                                          			 response from the above GET command:

```
https://<connection_server>/vmrest/callhandlerprimarytemplates/<callhandlerprimarytemplates-id>
```

Step 4

The following URI is the reponse from the above GET command:

```
https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>/transferoptions
```

#### What to do next

Every user template and call handler template has three transfer
                                 		  options:

- Standard

- Off Hours

- Alternate

Each transfer option can be accessed through a GET request:

- https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>/transferoptions/Alternate

- https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>/transferoptions/off%20Hours

- https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>/transferoptions/Standard

TimeExpires is the field that determines if a transfer option is
                                 		  enabled or disabled. To enable a transfer option, TimeExpires must be set to a
                                 		  future date, which is the date that the transfer option will expire (be
                                 		  disabled). To disable a transfer option, simply set TimeExpires to a date in
                                 		  the past. Also, if TimeExpires is set to null that means it is enabled
                                 		  indefinitely (however, note that currently CUPI offers no ability to set this
                                 		  field to null). TimeExpires is always treated as GMT. Any required time zone
                                 		  conversion is the responsibility of the client.

Action is the field that determines if the transfer option will
                                 		  transfer calls to an extension or directly to the greetings. The Action field
                                 		  is a custom type. A value of 0 denotes that the call will be sent directly to
                                 		  the greetings. A value of 1 denotes that the call will be transferred to an
                                 		  extension.

Several settings are specific to how the transfer option should
                                 		  transfer the call (assuming that the Action is set to 1):

- TransferType

- Extension

- TransferRings

TransferType determines whether the transfer will be released (a
                                 		  value of 0) or supervised (a value of 1).

Extension indicates the extension that the call will transfer
                                 		  to.

TransferRings is the number of times Connection will ring the
                                 		  extension before it considers the call a ring-no-answer (RNA), and pulls the
                                 		  call back to play the greeting. This value is only used when the TransferType
                                 		  is set to 1 (a supervised transfer).

UsePrimaryExtension is a boolean that is a bit of an oddity.
                                 		  When the value is set to true, the Extension is set to the primary extension of
                                 		  the user. However, note the following caveat when using this field: if
                                 		  UsePrimaryExtension is set to true and the Extension field is set to a value in
                                 		  the same PUT, an error will be thrown. Because setting UsePrimaryExtension to
                                 		  true causes the Extension field to be set to a specific value, you cannot also
                                 		  explicitly set the Extension field in the same PUT; one or the other can occur,
                                 		  but not both. An error will also be thrown if UsePrimaryExtension is set to
                                 		  false and no value is given for the Extension field in the same PUT. In other
                                 		  words, if you set UsePrimaryExtension to false, you must provide a new
                                 		  Extension in the same PUT.

PersonalCallTransfer is a boolean that determines whether
                                 		  personal call transfer rules will be used instead of the basic transfer rules.
                                 		  If PersonalCallTransfer is set to true, then instead of using any of the
                                 		  settings of this transfer rule, the call will be sent to the personal call
                                 		  transfer rules of the user to be acted on. If PersonalCallTransfer is set to
                                 		  false, then the basic transfer rule is used. If you are using personal call
                                 		  transfer rules, set this to true; otherwise, leave it set to false. It's that
                                 		  simple.

### Creating

Note that you cannot use CUPI to
                              		create transfer options.

### Updating

To enable the Alternate transfer
                                 		  option until March 9, 2020, you would use the following PUT request:

```
https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>/transferoptions/Alternate
```

To disable the Alternate transfer option you would do a PUT request
                                 		  with the TimeExpires field set to a date in the past as in this example:

Example 1

```
https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>/transferoptions/Alternate
```

```
<?xml version="1.0" encoding="UTF-8"?>
<TransferOption>
  <TimeExpires>1976-03-09 00:00:00.0</TimeExpires>
</TransferOption>
```

```
Response Code: 204
```

Example 2

```
https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>/transferoptions/Alternate
```

```
<?xml version="1.0" encoding="UTF-8"?>
<TransferOption>
  <TransferHoldingMode>1</TransferHoldingMode>
</TransferOption>
```

```
Response Code: 204
```

### Deleting

Note that you cannot use CUPI to
                                 		  delete transfer options.

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- User Template Caller
                        	 Input

### About Caller
                           	 Input

This page contains information on how to use the API to list and
                                 		  modify Caller Input. Caller input settings define actions that Cisco Unity
                                 		  Connection takes in response to phone keys pressed by callers.

For more information on caller inputs, see Cisco_Unity_Connection_Provisioning_Interface_(CUPI)_API_--_Caller_Input_Keys

### Listing and
                           	 Viewing Caller Input

The following is an example of a
                                 		  GET that lists all caller inputs of all types for the specified user template:

```
https://<connection_server>/vmrest/callhandlerprimarytemplates
```

The following is an example of the response from the above *GET*
                                 		  request and the actual response will depend upon the information given by you:

```
<MenuEntries total="12">
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/*
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>*
 </TouchtoneKey>
 <Locked>true</Locked>
 <Action>2</Action>
 <TargetConversation>SubSignIn</TargetConversation>
 <ObjectId>1d111b26-d50c-44a3-bfcc-0b60f2e3207a
 </ObjectId>
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/#
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>#</TouchtoneKey>
 <Locked>true</Locked>
 <Action>5</Action>
 <ObjectId>3e3d796b-ffd3-4388-a2bf-b2cca2cf0b9c
 </ObjectId>
 </MenuEntry>
 <MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/0
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>0</TouchtoneKey>
 <Locked>false</Locked>
 <Action>2</Action>
 <TargetConversation>PHTransfer</TargetConversation>
 <TargetHandlerObjectId>e4c32c78-42c6-495e-83c5-4a4a17c0cb7f</TargetHandlerObjectId>
 <ObjectId>050b1a62-b237-457d-a027-d2c3289eab20
 </ObjectId>
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/1
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a -1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>1</TouchtoneKey>
 <Locked>false</Locked>
 <Action>0</Action>
 <ObjectId>31a8cba0-8deb-4266-b83b-57a6c1a33ebb
 </ObjectId>
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/2
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>2</TouchtoneKey>
 <Locked>false</Locked>
 <Action>0</Action>
 <ObjectId>f7e0cca3-e864-480b-bcd5-84f290587cbf
 </ObjectId> 
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/3
 </URI><CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>3</TouchtoneKey>
 <Locked>false</Locked>
 <Action>0</Action>
 <ObjectId>910a7722-5cc1-4f98-b6b5-d9ac0c11440f
 </ObjectId>
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/4
 </URI><CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>4</TouchtoneKey>
 <Locked>false</Locked>
 <Action>0</Action>
 <ObjectId>da2588dc-557e-4671-892b-edde2987d4c0
 </ObjectId>
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/5
 </URI><CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>5</TouchtoneKey>
 <Locked>false</Locked>
 <Action>0</Action>
 <ObjectId>15c55592-df99-46d0-9a96-19a6ecff2bd5
 </ObjectId>
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/6
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>6</TouchtoneKey>
 <Locked>false</Locked>
 <Action>0</Action>
 <ObjectId>bdb6a884-269e-4aab-9ff7-997453e69642
 </ObjectId>
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/7
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>7</TouchtoneKey>
 <Locked>false</Locked>
 <Action>2</Action>
 <TargetConversation>PHTransfer</TargetConversation>
 <TargetHandlerObjectId>b659a96c-6949-4d78-a899-93a2407baf28
 </TargetHandlerObjectId>
 <ObjectId>11e69e5d-1223-4727-ad8c-1dbe3f8f8ce5
 </ObjectId>
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/8
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>8</TouchtoneKey>
 <Locked>false</Locked>
 <Action>0</Action>
 <ObjectId>333a6147-cd06-4d71-9def-417cb70c8ebf
 </ObjectId>
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/9
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>9</TouchtoneKey>
 <Locked>false</Locked>
 <Action>0</Action>
 <ObjectId>eb66e91d-2a82-425a-88f5-f2c058c2491e</ObjectId>
</MenuEntry>
</MenuEntries>
```

```
Response Code: 200
```

### Modifying a Caller
                           	 Input

The following is an example of
                                 		  the PUT request that modifies the caller input as represented by
                                 		  <callerinputId>:

```
https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>
```

The following is an example of the response from the above *PUT*
                                 		  request and the actual response will depend upon the information given by you:

```
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/*
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>*
 </TouchtoneKey>
 <Locked>true</Locked>
 <Action>2</Action>
 <TargetConversation>SubSignIn</TargetConversation>
 <ObjectId>1d111b26-d50c-44a3-bfcc-0b60f2e3207a
 </ObjectId>
</MenuEntry>
```

```
Response Code: 204
```

### Explanation of
                           	 Data Fields

The following chart lists all of the data fields available on Caller.

1- HangUp 0-ignore 6-RestartGreeting 8- Route from next calling route 5- Skip Greeting 4- Take message 7- Transfer to Alternate
                                             contact number

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- User Template Greetings

### Listing and
                           	 Viewing

The following GET allows users
                                 		  templates to listen to and modify their personal greeting:

```
https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>/usertemplategreetings
```

The following is an example of the response from the above *GET*
                                 		  request and the actual response will depend upon the information given by you:

```
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?> 
<UserTemplateGreetings total="7">
<UserTemplateGreeting>
  <CallHandlerObjectId>a254488a-7f96-4737-9df4-886e3f4b88af</CallHandlerObjectId> 
  <CallhandlerURI>/vmrest/callhandlerprimarytemplates/a254488a-7f96-4737-9df4-886e3f4b88af</CallhandlerURI> 
  <IgnoreDigits>false</IgnoreDigits> 
  <PlayWhat>1</PlayWhat> 
  <RepromptDelay>20</RepromptDelay> 
  <Reprompts>30</Reprompts> 
  <TimeExpires>2012-10-06 09:25:00.0</TimeExpires> 
  <GreetingType>Alternate</GreetingType> 
  <AfterGreetingAction>2</AfterGreetingAction> 
  <AfterGreetingTargetConversation>PHTransfer</AfterGreetingTargetConversation> 
  <AfterGreetingTargetHandlerObjectId>9e96f34b-22bc-429a-8852-46fbceeff182</AfterGreetingTargetHandlerObjectId> 
  <PlayRecordMessagePrompt>false</PlayRecordMessagePrompt> 
  <EnableTransfer>false</EnableTransfer>
  <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
  <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt> 
  <EnAltGreetDontRingPhone>true</EnAltGreetDontRingPhone> 
  <EnAltGreetPreventSkip>true</EnAltGreetPreventSkip> 
  <EnAltGreetPreventMsg>true</EnAltGreetPreventMsg> 
  <LanguageCode>1033</LanguageCode> 
</UserTemplateGreeting>
<UserTemplateGreeting>
  <CallHandlerObjectId>a254488a-7f96-4737-9df4-886e3f4b88af</CallHandlerObjectId> 
  <CallhandlerURI>/vmrest/callhandlerprimarytemplates/a254488a-7f96-4737-9df4-886e3f4b88af</CallhandlerURI> 
  <IgnoreDigits>false</IgnoreDigits> 
  <PlayWhat>0</PlayWhat> 
  <RepromptDelay>2</RepromptDelay> 
  <Reprompts>0</Reprompts> 
  <TimeExpires>2020-10-06 09:25:00.0</TimeExpires> 
  <GreetingType>Busy</GreetingType> 
  <AfterGreetingAction>4</AfterGreetingAction> 
  <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt> 
  <EnableTransfer>true</EnableTransfer>
  <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
  <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt> 
  <LanguageCode>1033</LanguageCode> 
</UserTemplateGreeting>
<UserTemplateGreeting>
  <CallHandlerObjectId>a254488a-7f96-4737-9df4-886e3f4b88af</CallHandlerObjectId> 
  <CallhandlerURI>/vmrest/callhandlerprimarytemplates/a254488a-7f96-4737-9df4-886e3f4b88af</CallhandlerURI> 
  <IgnoreDigits>false</IgnoreDigits> 
  <PlayWhat>0</PlayWhat> 
  <RepromptDelay>2</RepromptDelay> 
  <Reprompts>0</Reprompts> 
  <GreetingType>Error</GreetingType> 
  <AfterGreetingAction>6</AfterGreetingAction> 
  <AfterGreetingTargetConversation>PHGreeting</AfterGreetingTargetConversation> 
  <AfterGreetingTargetHandlerObjectId>08313019-91db-4aed-8ef3-af13a4a72e22</AfterGreetingTargetHandlerObjectId> 
  <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt> 
  <EnableTransfer>false</EnableTransfer> 
  <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
  <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt>
  <LanguageCode>1033</LanguageCode> 
</UserTemplateGreeting>
<UserTemplateGreeting>
  <CallHandlerObjectId>a254488a-7f96-4737-9df4-886e3f4b88af</CallHandlerObjectId> 
  <CallhandlerURI>/vmrest/callhandlerprimarytemplates/a254488a-7f96-4737-9df4-886e3f4b88af</CallhandlerURI> 
  <IgnoreDigits>false</IgnoreDigits> 
  <PlayWhat>0</PlayWhat> 
  <RepromptDelay>2</RepromptDelay> 
  <Reprompts>0</Reprompts> 
  <TimeExpires>2013-01-01 00:00:00.0</TimeExpires> 
  <GreetingType>Internal</GreetingType> 
  <AfterGreetingAction>4</AfterGreetingAction> 
  <PlayRecordMessagePrompt>false</PlayRecordMessagePrompt> 
  <EnableTransfer>false</EnableTransfer> 
  <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
  <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt>
  <LanguageCode>1033</LanguageCode> 
</UserTemplateGreeting>
<UserTemplateGreeting>
  <CallHandlerObjectId>a254488a-7f96-4737-9df4-886e3f4b88af</CallHandlerObjectId> 
  <CallhandlerURI>/vmrest/callhandlerprimarytemplates/a254488a-7f96-4737-9df4-886e3f4b88af</CallhandlerURI> 
  <IgnoreDigits>false</IgnoreDigits> 
  <PlayWhat>0</PlayWhat> 
  <RepromptDelay>2</RepromptDelay> 
  <Reprompts>0</Reprompts> 
  <TimeExpires>1972-01-01 00:00:00.0</TimeExpires> 
  <GreetingType>Off Hours</GreetingType> 
  <AfterGreetingAction>4</AfterGreetingAction> 
  <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt> 
  <EnableTransfer>false</EnableTransfer> 
  <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
  <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt>
  <LanguageCode>1033</LanguageCode> 
</UserTemplateGreeting>
<UserTemplateGreeting>
  <CallHandlerObjectId>a254488a-7f96-4737-9df4-886e3f4b88af</CallHandlerObjectId> 
  <CallhandlerURI>/vmrest/callhandlerprimarytemplates/a254488a-7f96-4737-9df4-886e3f4b88af</CallhandlerURI> 
  <IgnoreDigits>false</IgnoreDigits> 
  <PlayWhat>0</PlayWhat> 
  <RepromptDelay>2</RepromptDelay> 
  <Reprompts>0</Reprompts> 
  <GreetingType>Standard</GreetingType> 
  <AfterGreetingAction>4</AfterGreetingAction> 
  <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt> 
  <EnableTransfer>false</EnableTransfer> 
  <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
  <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt>
  <LanguageCode>1033</LanguageCode> 
</UserTemplateGreeting>
<UserTemplateGreeting>
  <CallHandlerObjectId>a254488a-7f96-4737-9df4-886e3f4b88af</CallHandlerObjectId> 
  <CallhandlerURI>/vmrest/callhandlerprimarytemplates/a254488a-7f96-4737-9df4-886e3f4b88af</CallhandlerURI> 
  <IgnoreDigits>false</IgnoreDigits> 
  <PlayWhat>0</PlayWhat> 
  <RepromptDelay>2</RepromptDelay> 
  <Reprompts>0</Reprompts> 
  <TimeExpires>1972-01-01 00:00:00.0</TimeExpires> 
  <GreetingType>Holiday</GreetingType> 
  <AfterGreetingAction>4</AfterGreetingAction> 
  <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt> 
  <EnableTransfer>false</EnableTransfer> 
  <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
  <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt>
  <LanguageCode>1033</LanguageCode> 
</UserTemplateGreeting>
</UserTemplateGreetings>
```

```
Response Code: 200
```

The \{greeting type\} can be any one of the following:

- Standard

- Alternate

- Busy

- Closed

- Holiday

- Error

- Internal

Each greeting can be accessed through the following various GET
                                 		  requests:

- https://<connection_server>/vmrest/usertemplate/greetings/Alternate

- https://<connection_server>/vmrest/usertemplate/greetings/Busy

- https://<connection_server>/vmrest/usertemplate/greetings/Error

- https://<connection_server>/vmrest/usertemplate/greetings/Internal

- https://<connection_server>/vmrest/usertemplate/greetings/Off%20Hours

- https://<connection_server>/vmrest/usertemplate/greetings/Standard

- https://<connection_server>/vmrest/usertemplate/greetings/Holiday

### Creating
                           	 Greetings

Note that you cannot use CUPI to
                                 		  create Greetings.

### Modifying
                           	 Greetings

The following is an example of
                                 		  the PUT request that modifies the personal greeting as represented by
                                 		  <greetingtype>:

```
https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>/usertemplategreetings/<Greeting-type
```

The following is an example of the response from the above *PUT*
                                 		  request and the actual response will depend upon the information given by you:

```
<UserTemplateGreeting>
 <EnableTransfer>true</EnableTransfer> 
  <RepromptDelay>454354</RepromptDelay> 
  <Reprompts>30</Reprompts> 
</UserTemplateGreeting>
```

```
Response Code: 204
```

### Deleting
                           	 Greetings

Note that you cannot use CUPI to
                                 		  delete Greetings.

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- User Template Settings
                        	 Notification Devices

### About Notification
                           	 Devices

This page contains information on how to use the API to create, list,
                              		update, and delete Notification Devices.

Cisco Unity Connection supports four different types of Notification
                              		Devices:

- Phone Devices

- Pager Devices

- HTML Devices

- SMTP Devices

The generic Notification Device resource contains the data fields that
                              		are common to most or all of the specialized Device resources, which in turn
                              		may contain additional data fields that are specific to certain Device
                              		resources. A listing of all data fields, including a description of what they
                              		mean and which specialized Device types support them, can be found later in
                              		this document.

In order to create, update, or delete a Notification Device, an API user
                              		must use the appropriate specialized Device resource. In other words, an API
                              		user can retrieve all of a user's Notification Devices, but if they then want
                              		to update a particular Phone Device, they must do the update operation on the
                              		Phone Device resource, not the Notification Device resource. This will be
                              		explained in more detail below.

The Notification Device resource and the four specialized Device
                              		resources contain data fields from the Device objects in the database, plus
                              		some data fields from the Notification Rule object. From an API user's
                              		perspective, this detail may not usually be important, but it is worth
                              		mentioning that the Device resources collapse two database objects into a
                              		single resource. This can be safely done because there is always a one-to-one
                              		mapping in the database of Notification Devices and Notification Rules.

The factory default User Template for Voicemail Users contains five
                              		Notification Devices: three Phone Devices (Home, Work, and Mobile), one Pager
                              		Device, one HTML device, and one SMTP Device. Any of these default Notification
                              		Devices can be modified, and new Devices of any of four specialized types
                              		(phone, pager, HTML, and SMTP) can be created or deleted.

### Listing and
                           	 Viewing Notification Devices

Example 1

The following is an example of a GET that lists all Notification
                                 		  Devices of all types for the specified User Template:

```
https://<connection-server>/vmrest/usertemplates/<objectId>/usertemplatenotificationdevices
```

The following is the response from the above *GET* request. Notice
                                 		  that this list contains a mix of different types of specialized Devices, since
                                 		  the request was for a list of all Notification Devices. The Type field
                                 		  indicates the specialized Device type for each Notification Device (1 = Phone,
                                 		  2 = Pager, 4 = SMTP, 8 = HTML).

```
<UserTemplateNotificationDevices total="7">
<UserTemplateNotificationDevice>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/usertemplatenotificationdevices/22b1e3cc-f13d-4349-8811-a196132781a3</URI>
 <SubscriberObjectId>85a845d3-063d-4641-aa70-8b536282bffb</SubscriberObjectId>
 <UserURI>/vmrest/users/85a845d3-063d-4641-aa70-8b536282bffb</UserURI>
 <ObjectId>22b1e3cc-f13d-4349-8811-a196132781a3</ObjectId>
 <DisplayName>Pager</DisplayName>
 <Active>false</Active>
 <BusyRetryInterval>5</BusyRetryInterval>
 <Type>2</Type>
 <DialDelay>1</DialDelay>
 <MaxBody>512</MaxBody>
 <MaxSubject>64</MaxSubject>
 <RetriesOnBusy>4</RetriesOnBusy>
 <RetriesOnRna>4</RetriesOnRna>
 <RingsToWait>4</RingsToWait>
 <RnaRetryInterval>15</RnaRetryInterval>
 <SendCount>true</SendCount>
 <WaitConnect>true</WaitConnect>
 <MediaSwitchObjectId>24f1171f-27b3-4ad3-a94c-66d1fb2e448b</MediaSwitchObjectId>
 <PhoneSystemURI>/vmrest/phonesystems/24f1171f-27b3-4ad3-a94c-66d1fb2e448b</PhoneSystemURI>
 <TransmitForcedAuthorizationCode>false</TransmitForcedAuthorizationCode>
 <DeviceName>Pager</DeviceName>
 <PromptForId>false</PromptForId>
 <SendCallerId>true</SendCallerId>
 <SendPcaLink>false</SendPcaLink>
 <Undeletable>true</Undeletable>
 <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
 <DetectTransferLoop>false</DetectTransferLoop>
 <SuccessRetryInterval>1</SuccessRetryInterval>
 <RetriesOnSuccess>0</RetriesOnSuccess>
 <EventList>NewVoiceMail</EventList>
 <ScheduleSetObjectId>a884af0a-dd5f-4597-8bc7-31a61e8b612a</ScheduleSetObjectId>
 <InitialDelay>0</InitialDelay>
 <RepeatInterval>0</RepeatInterval>
 <RepeatNotify>false</RepeatNotify>
 </UserTemplateNotificationDevice>
 <UserTemplateNotificationDevice>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/usertemplatenotificationdevices/d2e67ebc-a987-441d-a168-88d1d7dc49c2</URI>
 <SubscriberObjectId>85a845d3-063d-4641-aa70-8b536282bffb</SubscriberObjectId>
 <UserURI>/vmrest/users/85a845d3-063d-4641-aa70-8b536282bffb</UserURI>
 <ObjectId>d2e67ebc-a987-441d-a168-88d1d7dc49c2</ObjectId>
 <DisplayName>PagerDevice</DisplayName>
 <Active>false</Active>
 <BusyRetryInterval>5</BusyRetryInterval>
 <Type>2</Type>
 <DialDelay>1</DialDelay>
 <MaxBody>512</MaxBody>
 <MaxSubject>64</MaxSubject>
 <RetriesOnBusy>4</RetriesOnBusy>
 <RetriesOnRna>4</RetriesOnRna>
 <RingsToWait>4</RingsToWait>
 <RnaRetryInterval>15</RnaRetryInterval>
 <SendCount>true</SendCount>
 <WaitConnect>true</WaitConnect>
 <MediaSwitchObjectId>24f1171f-27b3-4ad3-a94c-66d1fb2e448b</MediaSwitchObjectId>
 <PhoneSystemURI>/vmrest/phonesystems/24f1171f-27b3-4ad3-a94c-66d1fb2e448b</PhoneSystemURI>
 <TransmitForcedAuthorizationCode>false</TransmitForcedAuthorizationCode>
 <DeviceName>Other</DeviceName>
 <PromptForId>false</PromptForId>
 <SendCallerId>true</SendCallerId>
 <SendPcaLink>false</SendPcaLink>
 <Undeletable>false</Undeletable>
 <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
 <DetectTransferLoop>false</DetectTransferLoop>
 <SuccessRetryInterval>1</SuccessRetryInterval>
 <RetriesOnSuccess>0</RetriesOnSuccess>
 <EventList>NewVoiceMail</EventList>
 <ScheduleSetObjectId>a884af0a-dd5f-4597-8bc7-31a61e8b612a</ScheduleSetObjectId>
 <InitialDelay>0</InitialDelay>
 <RepeatInterval>0</RepeatInterval>
 <RepeatNotify>false</RepeatNotify>
 </UserTemplateNotificationDevice>
 <UserTemplateNotificationDevice>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/usertemplatenotificationdevices/53bd701a-7301-49d0-8404-9769b38094cd</URI>
 <SubscriberObjectId>85a845d3-063d-4641-aa70-8b536282bffb</SubscriberObjectId>
 <UserURI>/vmrest/users/85a845d3-063d-4641-aa70-8b536282bffb</UserURI>
 <ObjectId>53bd701a-7301-49d0-8404-9769b38094cd</ObjectId>
 <DisplayName>Work Phone</DisplayName>
 <Active>false</Active>
 <BusyRetryInterval>5</BusyRetryInterval>
 <Conversation>SubNotify</Conversation>
 <Type>1</Type>
 <DialDelay>1</DialDelay>
 <MaxBody>512</MaxBody>
 <MaxSubject>64</MaxSubject>
 <RetriesOnBusy>4</RetriesOnBusy>
 <RetriesOnRna>4</RetriesOnRna>
 <RingsToWait>4</RingsToWait>
 <RnaRetryInterval>15</RnaRetryInterval>
 <SendCount>false</SendCount>
 <WaitConnect>true</WaitConnect>
 <MediaSwitchObjectId>24f1171f-27b3-4ad3-a94c-66d1fb2e448b</MediaSwitchObjectId>
 <PhoneSystemURI>/vmrest/phonesystems/24f1171f-27b3-4ad3-a94c-66d1fb2e448b</PhoneSystemURI>
 <TransmitForcedAuthorizationCode>false</TransmitForcedAuthorizationCode>
 <DeviceName>Work Phone</DeviceName>
 <PromptForId>false</PromptForId>
 <SendCallerId>false</SendCallerId>
 <SendPcaLink>false</SendPcaLink>
 <Undeletable>true</Undeletable>
 <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
 <DetectTransferLoop>false</DetectTransferLoop>
 <SuccessRetryInterval>0</SuccessRetryInterval>
 <RetriesOnSuccess>0</RetriesOnSuccess>
 <EventList>NewVoiceMail</EventList>
 <ScheduleSetObjectId>a884af0a-dd5f-4597-8bc7-31a61e8b612a</ScheduleSetObjectId>
 <InitialDelay>0</InitialDelay>
 <RepeatInterval>0</RepeatInterval>
 <RepeatNotify>false</RepeatNotify>
 </UserTemplateNotificationDevice>
 <UserTemplateNotificationDevice>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/usertemplatenotificationdevices/fa8d720c-7c03-4506-867f-780636b00c13</URI>
 <SubscriberObjectId>85a845d3-063d-4641-aa70-8b536282bffb</SubscriberObjectId>
 <UserURI>/vmrest/users/85a845d3-063d-4641-aa70-8b536282bffb</UserURI>
 <ObjectId>fa8d720c-7c03-4506-867f-780636b00c13</ObjectId>
 <DisplayName>Home Phone</DisplayName>
 <Active>false</Active>
 <BusyRetryInterval>5</BusyRetryInterval>
 <Conversation>SubNotify</Conversation>
 <Type>1</Type>
 <DialDelay>1</DialDelay>
 <MaxBody>512</MaxBody>
 <MaxSubject>64</MaxSubject>
 <RetriesOnBusy>4</RetriesOnBusy>
 <RetriesOnRna>4</RetriesOnRna>
 <RingsToWait>4</RingsToWait>
 <RnaRetryInterval>15</RnaRetryInterval>
 <SendCount>false</SendCount>
 <WaitConnect>true</WaitConnect>
 <MediaSwitchObjectId>24f1171f-27b3-4ad3-a94c-66d1fb2e448b</MediaSwitchObjectId>
 <PhoneSystemURI>/vmrest/phonesystems/24f1171f-27b3-4ad3-a94c-66d1fb2e448b</PhoneSystemURI>
 <TransmitForcedAuthorizationCode>false</TransmitForcedAuthorizationCode>
 <DeviceName>Home Phone</DeviceName>
 <PromptForId>false</PromptForId>
 <SendCallerId>false</SendCallerId>
 <SendPcaLink>false</SendPcaLink>
 <Undeletable>true</Undeletable>
 <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
 <DetectTransferLoop>false</DetectTransferLoop>
 <SuccessRetryInterval>0</SuccessRetryInterval>
 <RetriesOnSuccess>0</RetriesOnSuccess>
 <EventList>NewVoiceMail</EventList>
 <ScheduleSetObjectId>a884af0a-dd5f-4597-8bc7-31a61e8b612a</ScheduleSetObjectId>
 <InitialDelay>0</InitialDelay>
 <RepeatInterval>0</RepeatInterval>
 <RepeatNotify>false</RepeatNotify>
 </UserTemplateNotificationDevice>
 <UserTemplateNotificationDevice>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/usertemplatenotificationdevices/24cd2817-2911-4668-b740-24369c4b0d19</URI>
 <SubscriberObjectId>85a845d3-063d-4641-aa70-8b536282bffb</SubscriberObjectId>
 <UserURI>/vmrest/users/85a845d3-063d-4641-aa70-8b536282bffb</UserURI>
 <ObjectId>24cd2817-2911-4668-b740-24369c4b0d19</ObjectId>
 <DisplayName>Mobile Phone</DisplayName>
 <Active>false</Active>
 <BusyRetryInterval>5</BusyRetryInterval>
 <Conversation>SubNotify</Conversation>
 <Type>1</Type>
 <DialDelay>1</DialDelay>
 <MaxBody>512</MaxBody>
 <MaxSubject>64</MaxSubject>
 <RetriesOnBusy>4</RetriesOnBusy>
 <RetriesOnRna>4</RetriesOnRna>
 <RingsToWait>4</RingsToWait>
 <RnaRetryInterval>15</RnaRetryInterval>
 <SendCount>false</SendCount>
 <WaitConnect>true</WaitConnect>
 <MediaSwitchObjectId>24f1171f-27b3-4ad3-a94c-66d1fb2e448b</MediaSwitchObjectId>
 <PhoneSystemURI>/vmrest/phonesystems/24f1171f-27b3-4ad3-a94c-66d1fb2e448b</PhoneSystemURI>
 <TransmitForcedAuthorizationCode>false</TransmitForcedAuthorizationCode>
 <DeviceName>Mobile Phone</DeviceName>
 <PromptForId>false</PromptForId>
 <SendCallerId>false</SendCallerId>
 <SendPcaLink>false</SendPcaLink>
 <Undeletable>true</Undeletable>
 <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
 <DetectTransferLoop>false</DetectTransferLoop>
 <SuccessRetryInterval>0</SuccessRetryInterval>
 <RetriesOnSuccess>0</RetriesOnSuccess>
 <EventList>NewVoiceMail</EventList>
 <ScheduleSetObjectId>a884af0a-dd5f-4597-8bc7-31a61e8b612a</ScheduleSetObjectId>
 <InitialDelay>0</InitialDelay>
 <RepeatInterval>0</RepeatInterval>
 <RepeatNotify>false</RepeatNotify>
 </UserTemplateNotificationDevice>
 <UserTemplateNotificationDevice>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/usertemplatenotificationdevices/d6871a13-4680-428a-a839-afb6d3b46b6b</URI>
 <SubscriberObjectId>85a845d3-063d-4641-aa70-8b536282bffb</SubscriberObjectId>
 <UserURI>/vmrest/users/85a845d3-063d-4641-aa70-8b536282bffb</UserURI>
 <ObjectId>d6871a13-4680-428a-a839-afb6d3b46b6b</ObjectId>
 <DisplayName>SMTP</DisplayName>
 <Active>false</Active>
 <BusyRetryInterval>0</BusyRetryInterval>
 <Type>4</Type>
 <DialDelay>0</DialDelay>
 <MaxBody>512</MaxBody>
 <MaxSubject>64</MaxSubject>
 <RetriesOnBusy>0</RetriesOnBusy>
 <RetriesOnRna>0</RetriesOnRna>
 <RingsToWait>0</RingsToWait>
 <RnaRetryInterval>0</RnaRetryInterval>
 <SendCount>true</SendCount>
 <WaitConnect>false</WaitConnect>
 <TransmitForcedAuthorizationCode>false</TransmitForcedAuthorizationCode>
 <DeviceName>SMTP</DeviceName>
 <PromptForId>false</PromptForId>
 <SendCallerId>true</SendCallerId>
 <SendPcaLink>false</SendPcaLink>
 <Undeletable>true</Undeletable>
 <DetectTransferLoop>false</DetectTransferLoop>
 <SuccessRetryInterval>0</SuccessRetryInterval>
 <RetriesOnSuccess>0</RetriesOnSuccess>
 <EventList>NewVoiceMail</EventList>
 <ScheduleSetObjectId>a884af0a-dd5f-4597-8bc7-31a61e8b612a</ScheduleSetObjectId>
 <InitialDelay>0</InitialDelay>
 <RepeatInterval>0</RepeatInterval>
 <RepeatNotify>false</RepeatNotify>
</UserTemplateNotificationDevice>
<UserTemplateNotificationDevice>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/usertemplatenotificationdevices/9f2f0ce2-0567-421a-bd89-973ceecb8518</URI>
 <SubscriberObjectId>85a845d3-063d-4641-aa70-8b536282bffb</SubscriberObjectId>
 <UserURI>/vmrest/users/85a845d3-063d-4641-aa70-8b536282bffb</UserURI>
 <ObjectId>9f2f0ce2-0567-421a-bd89-973ceecb8518</ObjectId>
 <DisplayName>HTML</DisplayName>
 <Active>false</Active>
 <BusyRetryInterval>0</BusyRetryInterval>
 <Type>8</Type>
 <DialDelay>0</DialDelay>
 <MaxBody>512</MaxBody>
 <MaxSubject>64</MaxSubject>
 <RetriesOnBusy>0</RetriesOnBusy>
 <RetriesOnRna>0</RetriesOnRna>
 <RingsToWait>0</RingsToWait>
 <RnaRetryInterval>0</RnaRetryInterval>
 <SendCount>false</SendCount>
 <SmtpAddress>aaaa</SmtpAddress>
 <WaitConnect>false</WaitConnect>
 <TransmitForcedAuthorizationCode>false</TransmitForcedAuthorizationCode>
 <DeviceName>HTML</DeviceName>
 <PromptForId>false</PromptForId>
 <SendCallerId>false</SendCallerId>
 <SendPcaLink>false</SendPcaLink>
 <Undeletable>true</Undeletable>
 <DetectTransferLoop>false</DetectTransferLoop>
 <SuccessRetryInterval>0</SuccessRetryInterval>
 <RetriesOnSuccess>0</RetriesOnSuccess>
 <EventList>NewVoiceMail</EventList>
 <ScheduleSetObjectId>a884af0a-dd5f-4597-8bc7-31a61e8b612a</ScheduleSetObjectId>
 <InitialDelay>0</InitialDelay>
 <RepeatInterval>0</RepeatInterval>
 <RepeatNotify>false</RepeatNotify>
</UserTemplateNotificationDevice>
</UserTemplateNotificationDevices>
```

```
Response Code: 200
```

Example 2

The following is an example of a GET that lists a particular
                                 		  Notification Devices for the specified User Template:

```
https://<connection_server>/vmrest/usertemplates/<objectId>/usertemplatenotificationdevices/<objectId>
```

The following is the response from the above *GET* request.

```
<UserTemplateNotificationDevice>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/usertemplatenotificationdevices/9f2f0ce2-0567-421a-bd89-973ceecb8518</URI>
 <SubscriberObjectId>85a845d3-063d-4641-aa70-8b536282bffb</SubscriberObjectId>
 <UserURI>/vmrest/users/85a845d3-063d-4641-aa70-8b536282bffb</UserURI>
 <ObjectId>9f2f0ce2-0567-421a-bd89-973ceecb8518</ObjectId>
 <DisplayName>HTML</DisplayName>
 <Active>false</Active>
 <Type>8</Type>
 <MaxBody>512</MaxBody>
 <MaxSubject>64</MaxSubject>
 <SmtpAddress>aaaa</SmtpAddress>
 <DeviceName>HTML</DeviceName>
 <Undeletable>true</Undeletable>
 <EventList>NewVoiceMail</EventList>
 <ScheduleSetObjectId>a884af0a-dd5f-4597-8bc7-31a61e8b612a</ScheduleSetObjectId>
 <InitialDelay>0</InitialDelay>
 <RepeatInterval>0</RepeatInterval>
 <RepeatNotify>false</RepeatNotify>
</UserTemplateNotificationDevice>

<pre> Response Code: 200
```

### Adding a New
                           	 Notification Device

This section contains information on how to create notification
                                 		  devices:

- Adding Pager Notification
                                       			 Device

- Adding Phone Notification
                                       			 Device

- Adding HTML Notification
                                       			 Device

- Adding SMTP Notification
                                       			 Device

- Adding Pager Notification
                                       			 Device

#### Adding Pager
                              	 Notification Device

The following is an example of
                                    		  the POST request that adds a Pager Notification Device:

```
https://<connection_server>/vmrest/usertemplates/<objectId>/notificationdevices/<objectId>
```

The actual response will depend upon the information given by you.

```
<UserTemplatePagerDevice>
 <DisplayName>pager1</DisplayName>
 <MediaSwitchObjectId>2b6324a2-d66f-4f25-9572-decf88c9a0b7</MediaSwitchObjectId>
 <PhoneNumber>5656</PhoneNumber>
</UserTemplatePagerDevice>
```

```
Response Code: 201
```

#### Adding Phone
                              	 Notification Device

The following is an example of
                                    		  the POST request that adds a Phone Notification Device:

```
https://<connection_server>/vmrest/usertemplates/<objectId>/notificationdevices/<objectId>
```

The actual response will depend upon the information given by you.

```
<UserTemplatePhoneDevice>
 <DisplayName>pager1</DisplayName>
 <MediaSwitchObjectId>2b6324a2-d66f-4f25-9572-decf88c9a0b7</MediaSwitchObjectId>
 <PhoneNumber>5656</PhoneNumber>
</UserTemplatePhoneDevice>
```

```
Response Code: 201
```

#### Adding HTML
                              	 Notification Device

The following is an example of
                                    		  the POST request that adds a HTML Notification Device:

```
https://<connection_server>/vmrest/usertemplates/<objectId>/notificationdevices/<objectId>
```

The actual response will depend upon the information given by you.

```
<UserTemplateHtmlDevice>
 <DisplayName>Html</DisplayName>
 < SmtpAddress> a@cisco.com</SmtpAddress>
 <CallbackNumber>1111</CallbackNumber>
</UserTemplateHtmlDevice>
```

```
Response Code: 201
```

#### Adding SMTP
                              	 Notification Device

The following is an example of
                                    		  the POST request that adds a HTML Notification Device:

```
https://<connection_server>/vmrest/usertemplates/<objectId>/notificationdevices/<objectId>
```

The actual response will depend upon the information given by you.

```
<UserTemplateSmtpDevice>
 <DisplayName>SMTP</DisplayName>
 <SmtpAddress> a@cisco.com</SmtpAddress>
 <PhoneNumber>5656</PhoneNumber>
</UserTemplateSmtpDevice>
```

```
Response Code: 201
```

### Modifying
                           	 Notification Device

The following is an example of
                                 		  the PUT request that modifies a Notification Device as represented by
                                 		  <objectId>:

```
https://<connection_server>/vmrest/usertemplates/<objectId>/usertemplatenotificationdevices/<objectId>
```

The following is an example of the response from the above *PUT*
                                 		  request and the actual response will depend upon the information given by you:

```
<UserTemplatePhoneDevice>
 <Active>false</Active>
 <RepeatInterval>0</RepeatInterval>
 <RepeatNotify>true</RepeatNotify>
 <PhoneNumber>123456</PhoneNumber>
 <AfterDialDigits>11111</AfterDialDigits>
 <DialDelay>0</DialDelay>
 <RingsToWait>100</RingsToWait>
 <RetriesOnBusy>4</RetriesOnBusy>
 <RetriesOnRna>4</RetriesOnRna>
 <BusyRetryInterval>1</BusyRetryInterval>
 <RnaRetryInterval>100</RnaRetryInterval>
 <RetriesOnRna>100</RetriesOnRna>
 <MediaSwitchObjectId>1fb12b1c-cf14-4634-b73d-9b9c58ecdf68</MediaSwitchObjectId>
 <PromptForId>false</PromptForId>
 <EventList>NewUrgentFax,UrgentDispatchMessage</EventList>
</UserTemplatePhoneDevice>
```

```
Response Code: 204
```

### Deleting a New
                           	 Notification Device

The following is an example of
                                 		  the DELETE request that deletes a Notification Device as represented by
                                 		  <notificationdeviceid>:

```
https://<connection_server>/vmrest/usertemplates/<objectId>/usertemplatenotificationdevices/<objectId>
```

The output for this request returns the successful response code.

```
Response Code: 204
```

### Explanation of
                           	 Data Fields

Cisco_Unity_Connection_Provisioning_Interface_(CUPI)_API_-_Notification_Devices#Explanation_of_Data_Fields

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- User Template Settings Video
                        	 Service Account

### Listing the User
                           	 Template Video Service Account

The following is an example of
                                 		  GET request that displays user template settings video service account:

```
GET: https://<server-ip>/vmrest/usertemplates/981d804d-7a81-4171-b33e-8a4b12e0c309/usertemplatevideoserviceaccounts
```

The following is an example of response from the above *GET* request
                                 		  and the actual result will depend upon the information that has been provided
                                 		  by you:

```
200 
OK

<UserTemplateVideoServiceAccounts total="1">
 <UserTemplateVideoServiceAccount>
   <URI>/vmrest/usertemplates/981d804d-7a81-4171-b33e-8a4b12e0c309/usertemplatevideoserviceaccount/88397230-91a7-4248-910d-11e9fd5a8dc3</URI>
   <ConnectorFactoryObjectId>bf9e3b86-4306-4da3-a958-40f9197c99bd</ConnectorFactoryObjectId>
   <IsConnectorMapped>true</IsConnectorMapped>
   <ObjectId>88397230-91a7-4248-910d-11e9fd5a8dc3</ObjectId>
   <UserTemplateObjectId>981d804d-7a81-4171-b33e-8a4b12e0c309</UserTemplateObjectId>
   <UserTemplateURI>/vmrest/usertemplates/981d804d-7a81-4171-b33e-8a4b12e0c309</UserTemplateURI>
   <ConnectorFactoryName>test</ConnectorFactoryName>
   <MediaServerType>0</MediaServerType>
 </UserTemplateVideoServiceAccount>
</UserTemplateVideoServiceAccounts>
```

JSON Example

The following is an example to list a new video service template:

Request URI:

```
GET: https://<connection-ip-address>/vmrest/usertemplates/<TemplateObjectid>/usertemplatevideoserviceaccounts
```

The following is the response from the above *GET* request:

```
200
Ok
{
  "UserTemplateVideoServiceAccounts": {
    "-total": "1",
    "UserTemplateVideoServiceAccount": {
      "URI": "/vmrest/usertemplates/b98c46a4-ceaa-43df-bac6-4bd0620dc904/usertemplatevideoserviceaccounts/56b22a57-ffdc-4056-a5a9-5aa1d0987271",
      "ConnectorFactoryObjectId": "dbd26014-fe57-4d00-bd5a-a1df1bdae6a2",
      "IsConnectorMapped": "true",
      "ObjectId": "56b22a57-ffdc-4056-a5a9-5aa1d0987271",
      "UserTemplateObjectId": "b98c46a4-ceaa-43df-bac6-4bd0620dc904",
      "UserTemplateURI": "/vmrest/usertemplates/b98c46a4-ceaa-43df-bac6-4bd0620dc904",
      "ConnectorFactoryName": "video",
      "MediaServerType": "0"
    }
  }
}
```

### Creating the User
                           	 Template Video Service Account

The following is an example of
                                 		  POST request that can be used to create a new user template video service
                                 		  account:

```
POST: https://<server-ip>/vmrest/usertemplates/<templateobjectid>/usertemplatevideoserviceaccounts
```

Request Body:

```
<UserTemplateVideoServiceAccount>
   <ConnectorFactoryObjectId>bf9e3b86-4306-4da3-a958-40f9197c99bd</ConnectorFactoryObjectId>
   <IsConnectorMapped>true</IsConnectorMapped>
   <ConnectorFactoryName>test</ConnectorFactoryName>
   <MediaServerType>0</MediaServerType>
</UserTemplateVideoServiceAccount>
```

Response Code:

```
201 OK
```

The following is the response from the above POST request and the
                                 		  actual response will depend upon the information given by you:

```
/vmrest/usertemplates/981d804d-7a81-4171-b33e-8a4b12e0c309/usertemplatevideoserviceaccount/88397230-91a7-4248-910d-11e9fd5a8dc3
```

JSON Example

The following is an example to create a video service template:

Request URI:

```
POST:https://<connection-ip-address>/vmrest/usertemplates/<TemplateObjectid>/usertemplatevideoserviceaccounts
Accept: application/json
Content-type: application/json
```

The following is an example of the above POST request:

```
{
             "TemplateVideoService": {  "ConnectorFactoryObjectId": "dbd26014-fe57-4d00-bd5a-  a1df1bdae6a2",
           "ConnectorFactoryName": "myservice"
 }
}
```

The following is the response from the above POST request:

```
/vmrest/usertemplates/<TemplateObjectId>/ usertemplatevideoserviceaccounts /<TemplateObjectid>/
```

### Updating the User
                           	 Template Video Service Account

The following is an example of
                                 		  the PUT request to update the user template video service account:

```
PUT: https://<server-ip>/vmrest/usertemplates/<templateobjectid>/usertemplatevideoserviceaccounts/<objectid>
```

Request Body:

```
<UserTemplateVideoServiceAccount>
 <ConnectorFactoryObjectId>bf9e3b86-4306-4da3-a958-40f9197c99bd</ConnectorFactoryObjectId>
 <IsConnectorMapped>true</IsConnectorMapped>
 <ConnectorFactoryName>test</ConnectorFactoryName>
 <MediaServerType>0</MediaServerType>
</UserTemplateVideoServiceAccount>
```

Response Code:

```
204 OK
```

JSON Example

The following is an example to update a video service template:

Request URI:

```
PUT: https://<connection-ip-address>/vmrest/usertemplates/<TemplateObjectid>/usertemplatevideoserviceaccounts/<ObjectId>
Accept: application/json
Content-type: application/json
```

The following is an example of the PUT request:

```
{
   	    "TemplateVideoService": {
 	    "IsConnectorMapped": "false ",
   	    "ConnectorFactoryName": "myservice",
     	    "MediaServerType": "0"
                  }
               }
```

The following is the response from the above PUT request:

```
204
```

### Deleting the User
                           	 Template Video Service Account

The following is an example of DELETE request that deletes user
                                 		  template settings video service account:

Request URI:

```
Request URI :https://<server-ip>/vmrest/usertemplates/<templateobjectid>/usertemplatevideoserviceaccounts/<objectid>
```

Below is the response code from the above DELETE request:

```
204 OK
```

JSON Example

The following is an example to delete video service template:

Request URI:

```
DELETE: https://<connection-ip-address>/vmrest/usertemplates/<TemplateObjectid>/usertemplatevideoserviceaccounts/<ObjectId>
Accept: application/json
Content-type: application/json
```

The following is the response from the above DELETE request:

```
200
```

### Explanation of
                           	 Data Fields

The following chart lists all of the data fields:

| https://<connection_server>/vmrest/usertemplates |
|---|

| <UserTemplates total="1">
<UserTemplate>
 <URI>/vmrest/usertemplates/7553408b-3415-43db-aa82-3b2dc78062d1</URI>
 <ObjectId>7553408b-3415-43db-aa82-3b2dc78062d1</ObjectId>
 <UseDefaultLanguage>true</UseDefaultLanguage>
 <UseDefaultTimeZone>true</UseDefaultTimeZone>
 <Alias>voicemailusertemplate</Alias>
 <DisplayName>Voice Mail User Template</DisplayName>
 <TimeZone>190</TimeZone>
 <CreationTime>2012-06-25T06:07:31Z</CreationTime>
 <CosObjectId>7be9b3f3-1200-403f-984a-04c07b7c5a7b</CosObjectId>
 <CosURI>/vmrest/coses/7be9b3f3-1200-403f-984a-04c07b7c5a7b</CosURI>
 <Language>1033</Language>
 <LocationObjectId>6d4ff2e5-3f26-4a19-b2fa-beca79b4c5e9</LocationObjectId>
 <LocationURI>
 /vmrest/locations/connectionlocations/6d4ff2e5-3f26-4a19-b2fa- beca79b4c5e9
 </LocationURI>
 <AddressMode>0</AddressMode>
 <ClockMode>0</ClockMode>
 <ConversationTui>SubMenu</ConversationTui>
 <GreetByName>true</GreetByName>
 <ListInDirectory>true</ListInDirectory>
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
 <MediaSwitchObjectId>
 1fb12b1c-cf14-4634-b73d- 9b9c58ecdf68
 </MediaSwitchObjectId>
 <PhoneSystemURI>
 /vmrest/phonesystems/1fb12b1c-cf14-4634-b73d-9b9c58ecdf68
 </PhoneSystemURI>
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
 <ExitCallActionObjectId>
 a365e3c0-d8ed-4874-9810-cedb074dfe33
 </ExitCallActionObjectId>
 <CallAnswerTimeout>4</CallAnswerTimeout>
 <CallHandlerObjectId>f700f378-9656-45ea-94ff-c0462592999e</CallHandlerObjectId>
 <CallhandlerURI>
 /vmrest/callhandlerprimarytemplates/f700f378-9656-45ea-94ff-c0462592999e 
 </CallhandlerURI>
 <DisplayNameRule>1</DisplayNameRule>
 <DoesntExpire>false</DoesntExpire>
 <CantChange>false</CantChange>
 <MailboxStoreObjectId>cfc43112-601b-4764-ba92-b0220e9d7f23</MailboxStoreObjectId>
 <SavedMessageStackOrder>1234567</SavedMessageStackOrder>
 <NewMessageStackOrder>1234567</NewMessageStackOrder>
 <InboxAutoResolveMessageRecipients>true</InboxAutoResolveMessageRecipients>
 <PcaAddressBookRowsPerPage>5</PcaAddressBookRowsPerPage>
 <ReadOnly>false</ReadOnly>
 <EnableTts>true</EnableTts>
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
 <SearchByExtensionSearchSpaceObjectId>
 25e2e004-c194-4593-9961-bdcaf5dd7189
 </SearchByExtensionSearchSpaceObjectId>
 <SearchByExtensionSearchSpaceURI>
 /vmrest/searchspaces/25e2e004-c194-4593-9961-bdcaf5dd7189
 </SearchByExtensionSearchSpaceURI>
 <SearchByNameSearchSpaceObjectId>
 25e2e004-c194-4593-9961-bdcaf5dd7189
 </SearchByNameSearchSpaceObjectId>
 <SearchByNameSearchSpaceURI>
 /vmrest/searchspaces/25e2e004-c194-4593-9961-bdcaf5dd7189
 </SearchByNameSearchSpaceURI>
 <PartitionObjectId>12101df7-ecd2-4a48-b5b9-9a96b5f85a25</PartitionObjectId>
 <PartitionURI>
 /vmrest/partitions/12101df7-ecd2-4a48-b5b9-9a96b5f85a25
 </PartitionURI>
 <UseDynamicNameSearchWeight>false</UseDynamicNameSearchWeight>
 <LdapType>0</LdapType>
 <EnableMessageBookmark>false</EnableMessageBookmark>
 <SayTotalDraftMsg>false</SayTotalDraftMsg>
 <EnableSaveDraft>false</EnableSaveDraft>
 <RetainUrgentMessageFlag>false</RetainUrgentMessageFlag>
 <SayMessageLength>false</SayMessageLength>
 <CreateSmtpProxyFromCorp>false</CreateSmtpProxyFromCorp>
 <AutoAdvanceMsgs>false</AutoAdvanceMsgs>
 <SaySenderAfter>false</SaySenderAfter>
 <SaySenderExtensionAfter>false</SaySenderExtensionAfter>
 <SayMsgNumberAfter>false</SayMsgNumberAfter>
 <SayAniAfter>false</SayAniAfter>
 <SayMessageLengthAfter>false</SayMessageLengthAfter>
 <UserTemplateRolesURI>
 /vmrest/usertemplates/7553408b-3415-43db-aa82-3b2dc78062d1/usertemplateroles
 </UserTemplateRolesURI>
 <UserTemplateNotificationDevicesURI>
 /vmrest/usertemplates/7553408b-3415-43db-aa823b2dc78062d1/usertemplatenotificationdevices
 </UserTemplateNotificationDevicesURI>
 <UserTemplateWebPasswordURI>
 /vmrest/usertemplates/7553408b-3415-43db-aa82-3b2dc78062d1/credential/password
 </UserTemplateWebPasswordURI>
 <UserTemplateVoicePinURI>
 /vmrest/usertemplates/7553408b-3415-43db-aa82-3b2dc78062d1/credential/pin
 </UserTemplateVoicePinURI>
 <UserTemplateMessageActionURI>
 /vmrest/usertemplates/7553408b-3415-43db-aa82-3b2dc78062d1/usertemplatemessageactions
 </UserTemplateMessageActionURI>
</UserTemplate> |
|---|

| Response Code: 200 |
|---|

| https://<connection_server>/vmrest/usertemplates/<objectId> |
|---|

| <UserTemplate>
 <URI>
 /vmrest/usertemplates/c8af2544-2bc9-44fa-b713-e80f306cf781
 </URI>
 <ObjectId>
 c8af2544-2bc9-44fa-b713-e80f306cf781
 </ObjectId>
 <UseDefaultLanguage>true</UseDefaultLanguage>
 <UseDefaultTimeZone>true</UseDefaultTimeZone>
 <Alias>NewCiscoTemplate2</Alias>
 <City/>
 <State/>
 <Country>US</Country>
 <PostalCode/>
 <Department/>
 <Manager/>
 <Building/>
 <Address/>
 <DisplayName>testmonica</DisplayName>
 <BillingId/>
 <TimeZone>190</TimeZone>
 <CreationTime>2012-06-26 05:02:22.05</CreationTime>
 <CosObjectId>7be9b3f3-1200-403f-984a-04c07b7c5a7b</CosObjectId>
 <CosURI>/vmrest/coses/7be9b3f3-1200-403f-984a-04c07b7c5a7b</CosURI>
 <Language>1033</Language>
 <LocationObjectId>
 6d4ff2e5-3f26-4a19-b2fa-beca79b4c5e9
 </LocationObjectId>
 <LocationURI>
 /vmrest/locations/connectionlocations/6d4ff2e5-3f26-4a19-b2fa-beca79b4c5e9
 </LocationURI>
 <AddressMode>0</AddressMode>
 <ClockMode>0</ClockMode>
 <ConversationTui>SubMenu</ConversationTui>
 <GreetByName>true</GreetByName>
 <ListInDirectory>true</ListInDirectory>
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
 <MediaSwitchObjectId>
 1fb12b1c-cf14-4634-b73d-9b9c58ecdf68
 </MediaSwitchObjectId>
 <PhoneSystemURI>
 /vmrest/phonesystems/1fb12b1c-cf14-4634-b73d-9b9c58ecdf68
 </PhoneSystemURI>
 <Undeletable>false</Undeletable>
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
 <ExitCallActionObjectId>
 27cbb3a8-f040-4ee9-9686-620c43e3d725
 </ExitCallActionObjectId>
 <CallAnswerTimeout>4</CallAnswerTimeout>
 <CallHandlerObjectId>
 9a5ac35a-0df8-4ebb-8e19-77f936dfd263
 </CallHandlerObjectId>
 <CallhandlerURI>
 /vmrest/callhandlerprimarytemplates/9a5ac35a-0df8-4ebb-8e19-77f936dfd263
 </CallhandlerURI>
 <DisplayNameRule>1</DisplayNameRule>
 <DoesntExpire>false</DoesntExpire>
 <CantChange>false</CantChange>
 <MailboxStoreObjectId>
 cfc43112-601b-4764-ba92-b0220e9d7f23
 </MailboxStoreObjectId>
 <SavedMessageStackOrder>1234567</SavedMessageStackOrder>
 <NewMessageStackOrder>1234567</NewMessageStackOrder>
 <MessageLocatorSortOrder>1</MessageLocatorSortOrder>
 <SavedMessageSortOrder>2</SavedMessageSortOrder>
 <NewMessageSortOrder>1</NewMessageSortOrder>
 <MessageTypeMenu>false</MessageTypeMenu>
 <EnablePersonalRules>true</EnablePersonalRules>
 <RecordUnknownCallerName>true</RecordUnknownCallerName>
 <RingPrimaryPhoneFirst>false</RingPrimaryPhoneFirst>
 <PromptSpeed>100</PromptSpeed>
 <ExitAction>2</ExitAction>
 <ExitTargetConversation>PHTransfer</ExitTargetConversation>
 <ExitTargetHandlerObjectId>
 7ae69f21-1c99-4cc1-96c3-a1bbe11fd4ca
 </ExitTargetHandlerObjectId>
 <RepeatMenu>1</RepeatMenu>
 <FirstDigitTimeout>5000</FirstDigitTimeout>
 <InterdigitDelay>3000</InterdigitDelay>
 <PromptVolume>50</PromptVolume>
 <AddressAfterRecord>false</AddressAfterRecord>
 <ConfirmDeleteMessage>false</ConfirmDeleteMessage>
 <ConfirmDeleteDeletedMessage>false</ConfirmDeleteDeletedMessage>
 <ConfirmDeleteMultipleMessages>true</ConfirmDeleteMultipleMessages>
 <IsClockMode24Hour>false</IsClockMode24Hour>
 <RouteNDRToSender>true</RouteNDRToSender>
 <NotificationType>0</NotificationType>
 <SendReadReceipts>0</SendReadReceipts>
 <ReceiveQuota>-1</ReceiveQuota>
 <SendQuota>-1</SendQuota>
 <WarningQuota>-1</WarningQuota>
 <IsSetForVmEnrollment>true</IsSetForVmEnrollment>
 <VoiceNameRequired>false</VoiceNameRequired>
 <SendBroadcastMsg>true</SendBroadcastMsg>
 <UpdateBroadcastMsg>false</UpdateBroadcastMsg>
 <ConversationVui>VuiStart</ConversationVui>
 <SpeechCompleteTimeout>0</SpeechCompleteTimeout>
 <SpeechIncompleteTimeout>750</SpeechIncompleteTimeout>
 <UseVui>false</UseVui>
 <SkipPasswordForKnownDevice>false</SkipPasswordForKnownDevice>
 <JumpToMessagesOnLogin>true</JumpToMessagesOnLogin>
 <EnableMessageLocator>false</EnableMessageLocator>
 <MessageAgingPolicyObjectId>
 2e02eca6-270b-4b7f-a153-f03ea74d403d
 </MessageAgingPolicyObjectId>
 <MessageAgingPolicyURI>
 /vmrest/messageagingpolicies/2e02eca6-270b-4b7f-a153-f03ea74d403d
 </MessageAgingPolicyURI>
 <AssistantRowsPerPage>5</AssistantRowsPerPage>
 <InboxMessagesPerPage>20</InboxMessagesPerPage>
 <InboxAutoRefresh>15</InboxAutoRefresh>
 <InboxAutoResolveMessageRecipients>true</InboxAutoResolveMessageRecipients>
 <PcaAddressBookRowsPerPage>5</PcaAddressBookRowsPerPage>
 <ReadOnly>false</ReadOnly>
 <EnableTts>true</EnableTts>
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
 <SearchByExtensionSearchSpaceObjectId>
 25e2e004-c194-4593-9961-bdcaf5dd7189
 </SearchByExtensionSearchSpaceObjectId>
 <SearchByExtensionSearchSpaceURI>
 /vmrest/searchspaces/25e2e004-c194-4593-9961-bdcaf5dd7189
 </SearchByExtensionSearchSpaceURI>
 <SearchByNameSearchSpaceObjectId>
 25e2e004-c194-4593-9961-bdcaf5dd7189
 </SearchByNameSearchSpaceObjectId>
 <SearchByNameSearchSpaceURI>
 /vmrest/searchspaces/25e2e004-c194-4593-9961-bdcaf5dd7189
 </SearchByNameSearchSpaceURI>
 <PartitionObjectId>
 12101df7-ecd2-4a48-b5b9-9a96b5f85a25
 </PartitionObjectId>
 <PartitionURI>
 /vmrest/partitions/12101df7-ecd2-4a48-b5b9-9a96b5f85a25 
 </PartitionURI>
 <UseDynamicNameSearchWeight>false</UseDynamicNameSearchWeight>
 <LdapType>0</LdapType>
 <EnableMessageBookmark>false</EnableMessageBookmark>
 <SayTotalDraftMsg>false</SayTotalDraftMsg>
 <EnableSaveDraft>false</EnableSaveDraft>
 <RetainUrgentMessageFlag>false</RetainUrgentMessageFlag>
 <SayMessageLength>false</SayMessageLength>
 <CreateSmtpProxyFromCorp>false</CreateSmtpProxyFromCorp>
 <AutoAdvanceMsgs>false</AutoAdvanceMsgs>
 <SaySenderAfter>false</SaySenderAfter>
 <SaySenderExtensionAfter>false</SaySenderExtensionAfter>
 <SayMsgNumberAfter>false</SayMsgNumberAfter>
 <SayAniAfter>false</SayAniAfter>
 <SayMessageLengthAfter>false</SayMessageLengthAfter>
 <UserTemplateRolesURI>
 /vmrest/usertemplates/c8af2544-2bc9-44fa-b713-e80f306cf781/usertemplateroles
 </UserTemplateRolesURI>
 <UserTemplateNotificationDevicesURI>
 /vmrest/usertemplates/c8af2544-2bc9-44fa-b713-e80f306cf781/usertemplatenotificationdevices
 </UserTemplateNotificationDevicesURI>
 <UserTemplateWebPasswordURI>
 /vmrest/usertemplates/c8af2544-2bc9-44fa-b713-e80f306cf781/credential/password
 </UserTemplateWebPasswordURI>
 <UserTemplateVoicePinURI>
 /vmrest/usertemplates/c8af2544-2bc9-44fa-b713-e80f306cf781/credential/pin
 </UserTemplateVoicePinURI>
 <UserTemplateMessageActionURI>
 /vmrest/usertemplates/c8af2544-2bc9-44fa-b713-e80f306cf781/usertemplatemessageactions
 </UserTemplateMessageActionURI>
</UserTemplate> |
|---|

| Response Code: 200 |
|---|

| https://<connection_server>/vmrest/usertemplates/ |
|---|

| {
"@total": "2",
"UserTemplate":   
 {
   "URI": "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d",
   "ObjectId": "885dd0af-bdb1-401f-b4e9-6bd9fc8d594d",
   "UseDefaultLanguage": "true",
   "UseDefaultTimeZone": "true",
   "Alias": "voicemailusertemplate",
   "DisplayName": "Voice Mail User Template",
   "TimeZone": "4",
   "CreationTime": "2012-07-29T14:10:26Z",
   "CosObjectId": "362bf7f9-7cec-4f59-86dd-6c058a9100ef",
   "CosURI": "/vmrest/coses/362bf7f9-7cec-4f59-86dd-6c058a9100ef",
   "Language": "1033",
   "LocationObjectId": "3a403c9c-04c8-496a-ba76-23faaaae5a95",
   "LocationURI": 
   "/vmrest/locations/connectionlocations/3a403c9c-04c8-496a-ba76-23faaaae5a95",
   "AddressMode": "0",
   "ClockMode": "0",
   "ConversationTui": "SubMenu",
   "GreetByName": "true",
   "ListInDirectory": "true",
   "IsVmEnrolled": "true",
   "SayCopiedNames": "true",
   "SayDistributionList": "true",
   "SayMsgNumber": "true",
   "SaySender": "true",
   "SayTimestampAfter": "true",
   "SayTimestampBefore": "false",
   "SayTotalNew": "false",
   "SayTotalNewEmail": "false",
   "SayTotalNewFax": "false",
   "SayTotalNewVoice": "true",
   "SayTotalReceipts": "false",
   "SayTotalSaved": "true",
   "Speed": "100",
   "MediaSwitchObjectId": "0d15753c-e1b4-4865-b00b-999a1ccf56ce",
   "PhoneSystemURI": 
   "/vmrest/phonesystems/0d15753c-e1b4-4865-b00b-999a1ccf56ce",
   "Undeletable": "true",
   "UseBriefPrompts": "false",
   "Volume": "50",
   "EnAltGreetDontRingPhone": "false",
   "EnAltGreetPreventSkip": "false",
   "EnAltGreetPreventMsg": "false",
   "EncryptPrivateMessages": "false",
   "DeletedMessageSortOrder": "2",
   "SayAltGreetWarning": "false",
   "SaySenderExtension": "false",
   "SayAni": "false",
   "ExitCallActionObjectId": "6352cf7d-89f8-4748-bac5-8878889c3d56",
   "CallAnswerTimeout": "4",
   "CallHandlerObjectId": "c9069370-3631-4d36-a53a-1ac4e8d8f444",
   "CallhandlerURI": 
   "/vmrest/callhandlerprimarytemplates/c9069370-3631-4d36-a53a-1ac4e8d8f444",
   "DisplayNameRule": "1",
   "DoesntExpire": "false",
   "CantChange": "false",
   "MailboxStoreObjectId": "6d2eb9ad-3caf-41d2-b3db-4451d95057fe",
   "SavedMessageStackOrder": "1234567",
   "NewMessageStackOrder": "1234567",
   "MessageLocatorSortOrder": "1",
   "SavedMessageSortOrder": "2",
   "NewMessageSortOrder": "1",
   "MessageTypeMenu": "false",
   "EnablePersonalRules": "true",
   "RecordUnknownCallerName": "true",
   "RingPrimaryPhoneFirst": "false",
   "PromptSpeed": "100",
   "ExitAction": "2",
   "ExitTargetConversation": "PHGreeting",
   "ExitTargetHandlerObjectId": "708d5a59-95bb-4804-979b-c56b2f7d719a",
   "RepeatMenu": "1",
   "FirstDigitTimeout": "5000",
   "InterdigitDelay": "3000",
   "PromptVolume": "50",
   "DelayAfterGreeting": "0",
   "AddressAfterRecord": "false",
   "ConfirmDeleteMessage": "false",
   "ConfirmDeleteDeletedMessage": "false",
   "ConfirmDeleteMultipleMessages": "true",
   "IsClockMode24Hour": "false",
   "RouteNDRToSender": "true",
   "NotificationType": "0",
   "SendReadReceipts": "1",
   "ReceiveQuota": "2147483647",
   "SendQuota": "2147483647",
   "WarningQuota": "2147483647",
   "IsSetForVmEnrollment": "true",
   "VoiceNameRequired": "false",
   "SendBroadcastMsg": "false",
   "UpdateBroadcastMsg": "false",
   "ConversationVui": "VuiStart",
   "SpeechCompleteTimeout": "0",
   "SpeechIncompleteTimeout": "750",
   "UseVui": "false",
   "SkipPasswordForKnownDevice": "false",
   "JumpToMessagesOnLogin": "true",
   "EnableMessageLocator": "false",
   "MessageAgingPolicyObjectId": "a4b9216a-9360-4f9b-8937-cc66fba0ebbe",
   "MessageAgingPolicyURI": 
   "/vmrest/messageagingpolicies/a4b9216a-9360-4f9b-8937-cc66fba0ebbe",
   "AssistantRowsPerPage": "5",
   "InboxMessagesPerPage": "20",
   "InboxAutoRefresh": "15",
   "InboxAutoResolveMessageRecipients": "true",
   "PcaAddressBookRowsPerPage": "5",
   "ReadOnly": "false",
   "EnableTts": "true",
   "ConfirmationConfidenceThreshold": "60",
   "AnnounceUpcomingMeetings": "60",
   "SpeechConfidenceThreshold": "40",
   "SpeechSpeedVsAccuracy": "50",
   "SpeechSensitivity": "50",
   "EnableVisualMessageLocator": "false",
   "ContinuousAddMode": "false",
   "NameConfirmation": "false",
   "CommandDigitTimeout": "1500",
   "SaveMessageOnHangup": "false",
   "SendMessageOnHangup": "1",
   "SkipForwardTime": "12345",
   "SkipReverseTime": "54321",
   "UseShortPollForCache": "false",
   "SearchByExtensionSearchSpaceObjectId": 
   "a3933806-a995-443e-8704-498c03377bf7",
   "SearchByExtensionSearchSpaceURI": 
   "/vmrest/searchspaces/a3933806-a995-443e-8704-498c03377bf7",
   "SearchByNameSearchSpaceObjectId": 
   "a3933806-a995-443e-8704-498c03377bf7",
   "SearchByNameSearchSpaceURI": 
   "/vmrest/searchspaces/a3933806-a995-443e-8704-498c03377bf7",
   "PartitionObjectId": "6ac064a3-79d6-4a52-a3d3-f4311be5c28c",
   "PartitionURI": 
   "/vmrest/partitions/6ac064a3-79d6-4a52-a3d3-f4311be5c28c",
   "UseDynamicNameSearchWeight": "false",
   "LdapType": "0",
   "EnableMessageBookmark": "false",
   "SayTotalDraftMsg": "false",
   "EnableSaveDraft": "false",
   "RetainUrgentMessageFlag": "false",
   "SayMessageLength": "false",
   "CreateSmtpProxyFromCorp": "false",
   "AutoAdvanceMsgs": "false",
   "SaySenderAfter": "false",
   "SaySenderExtensionAfter": "false",
   "SayMsgNumberAfter": "true",
   "SayAniAfter": "false",
   "SayMessageLengthAfter": "false",
   "UserTemplateRolesURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/usertemplateroles",
   "UserTemplateNotificationDevicesURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/usertemplatenotificationdevices",
   "TemplateExternalServiceAccountsURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/templateexternalserviceaccounts",
   "UserTemplateWebPasswordURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/credential/password",
   "UserTemplateVoicePinURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/credential/pin",
   "UserTemplateMessageActionURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/usertemplatemessageactions",
   "DefaultUserTemplateURI": "/vmrest/userdefaulttemplates"
  },
  {
   "URI": "/vmrest/usertemplates/7426a16f-e735-4854-9ab6-7463728ea4f7",
   "ObjectId": "7426a16f-e735-4854-9ab6-7463728ea4f7",
   "UseDefaultLanguage": "true",
   "UseDefaultTimeZone": "true",
   "Alias": "AdminTest",
   "DisplayName": "Admin test",
   "TimeZone": "4",
   "CreationTime": "2012-08-28T10:57:12Z",
   "CosObjectId": "362bf7f9-7cec-4f59-86dd-6c058a9100ef",
   "CosURI": "/vmrest/coses/362bf7f9-7cec-4f59-86dd-6c058a9100ef",
   "Language": "1033",
   "LocationObjectId": "3a403c9c-04c8-496a-ba76-23faaaae5a95",
   "LocationURI": 
   "/vmrest/locations/connectionlocations/3a403c9c-04c8-496a-ba76-23faaaae5a95",
   "AddressMode": "0",
   "ClockMode": "0",
   "ConversationTui": "SubMenu",
   "GreetByName": "true",
   "ListInDirectory": "true",
   "IsVmEnrolled": "true",
   "SayCopiedNames": "true",
   "SayDistributionList": "true",
   "SayMsgNumber": "true",
   "SaySender": "true",
   "SayTimestampAfter": "true",
   "SayTimestampBefore": "false",
   "SayTotalNew": "false",
   "SayTotalNewEmail": "false",
   "SayTotalNewFax": "false",
   "SayTotalNewVoice": "true",
   "SayTotalReceipts": "false",
   "SayTotalSaved": "true",
   "Speed": "100",
   "MediaSwitchObjectId": "0d15753c-e1b4-4865-b00b-999a1ccf56ce",
   "PhoneSystemURI": 
   "/vmrest/phonesystems/0d15753c-e1b4-4865-b00b-999a1ccf56ce",
   "Undeletable": "false",
   "UseBriefPrompts": "false",
   "Volume": "50",
   "EnAltGreetDontRingPhone": "false",
   "EnAltGreetPreventSkip": "false",
   "EnAltGreetPreventMsg": "false",
   "EncryptPrivateMessages": "false",
   "DeletedMessageSortOrder": "2",
   "SayAltGreetWarning": "false",
   "SaySenderExtension": "false",
   "SayAni": "false",
   "ExitCallActionObjectId": "38d9d3d2-2f70-4e4c-a3bd-54c8e96df9f6",
   "CallAnswerTimeout": "4",
   "CallHandlerObjectId": "ee01a097-2c78-4f36-9400-c0a6e0159419",
   "CallhandlerURI": 
   "/vmrest/callhandlerprimarytemplates/ee01a097-2c78-4f36-9400-c0a6e0159419",
   "DisplayNameRule": "1",
   "DoesntExpire": "false",
   "CantChange": "false",
   "MailboxStoreObjectId": "6d2eb9ad-3caf-41d2-b3db-4451d95057fe",
   "SavedMessageStackOrder": "1234567",
   "NewMessageStackOrder": "1234567",
   "MessageLocatorSortOrder": "1",
   "SavedMessageSortOrder": "2",
   "NewMessageSortOrder": "1",
   "MessageTypeMenu": "false",
   "EnablePersonalRules": "true",
   "RecordUnknownCallerName": "true",
   "RingPrimaryPhoneFirst": "false",
   "PromptSpeed": "100",
   "ExitAction": "2",
   "ExitTargetConversation": "PHGreeting",
   "ExitTargetHandlerObjectId": "708d5a59-95bb-4804-979b-c56b2f7d719a",
   "RepeatMenu": "1",
   "FirstDigitTimeout": "5000",
   "InterdigitDelay": "3000",
   "PromptVolume": "50",
   "DelayAfterGreeting": "0",
   "AddressAfterRecord": "false",
   "ConfirmDeleteMessage": "false",
   "ConfirmDeleteDeletedMessage": "false",
   "ConfirmDeleteMultipleMessages": "true",
   "IsClockMode24Hour": "false",
   "RouteNDRToSender": "true",
   "NotificationType": "0",
   "SendReadReceipts": "1",
   "ReceiveQuota": "2147483647",
   "SendQuota": "2147483647",
   "WarningQuota": "2147483647",
   "IsSetForVmEnrollment": "true",
   "VoiceNameRequired": "false",
   "SendBroadcastMsg": "false",
   "UpdateBroadcastMsg": "false",
   "ConversationVui": "VuiStart",
   "SpeechCompleteTimeout": "0",
   "SpeechIncompleteTimeout": "750",
   "UseVui": "false",
   "SkipPasswordForKnownDevice": "false",
   "JumpToMessagesOnLogin": "true",
   "EnableMessageLocator": "false",
   "MessageAgingPolicyObjectId": "a4b9216a-9360-4f9b-8937-cc66fba0ebbe",
   "MessageAgingPolicyURI": 
   "/vmrest/messageagingpolicies/a4b9216a-9360-4f9b-8937-cc66fba0ebbe",
   "AssistantRowsPerPage": "5",
   "InboxMessagesPerPage": "20",
   "InboxAutoRefresh": "15",
   "InboxAutoResolveMessageRecipients": "true",
   "PcaAddressBookRowsPerPage": "5",
   "ReadOnly": "false",
   "EnableTts": "true",
   "ConfirmationConfidenceThreshold": "60",
   "AnnounceUpcomingMeetings": "60",
   "SpeechConfidenceThreshold": "40",
   "SpeechSpeedVsAccuracy": "50",
   "SpeechSensitivity": "50",
   "EnableVisualMessageLocator": "false",
   "ContinuousAddMode": "false",
   "NameConfirmation": "false",
   "CommandDigitTimeout": "1500",
   "SaveMessageOnHangup": "false",
   "SendMessageOnHangup": "1",
   "SkipForwardTime": "12345",
   "SkipReverseTime": "54321",
   "UseShortPollForCache": "false",
   "SearchByExtensionSearchSpaceObjectId": 
   "a3933806-a995-443e-8704-498c03377bf7",
   "SearchByExtensionSearchSpaceURI": 
   "/vmrest/searchspaces/a3933806-a995-443e-8704-498c03377bf7",
   "SearchByNameSearchSpaceObjectId": 
   "a3933806-a995-443e-8704-498c03377bf7",
   "SearchByNameSearchSpaceURI": 
   "/vmrest/searchspaces/a3933806-a995-443e-8704-498c03377bf7",
   "PartitionObjectId": 
   "6ac064a3-79d6-4a52-a3d3-f4311be5c28c",
   "PartitionURI": 
   "/vmrest/partitions/6ac064a3-79d6-4a52-a3d3-f4311be5c28c",
   "UseDynamicNameSearchWeight": "false",
   "LdapType": "0",
   "EnableMessageBookmark": "false",
   "SayTotalDraftMsg": "false",
   "EnableSaveDraft": "false",
   "RetainUrgentMessageFlag": "false",
   "SayMessageLength": "false",
   "CreateSmtpProxyFromCorp": "false",
   "AutoAdvanceMsgs": "false",
   "SaySenderAfter": "false",
   "SaySenderExtensionAfter": "false",
   "SayMsgNumberAfter": "true",
   "SayAniAfter": "false",
   "SayMessageLengthAfter": "false",
   "UserTemplateRolesURI": 
   "/vmrest/usertemplates/7426a16f-e735-4854-9ab6-7463728ea4f7/usertemplateroles",
   "UserTemplateNotificationDevicesURI": 
   "/vmrest/usertemplates/7426a16f-e735-4854-9ab6-7463728ea4f7/usertemplatenotificationdevices",
   "TemplateExternalServiceAccountsURI": 
   "/vmrest/usertemplates/7426a16f-e735-4854-9ab6-7463728ea4f7/templateexternalserviceaccounts",
   "UserTemplateWebPasswordURI": 
   "/vmrest/usertemplates/7426a16f-e735-4854-9ab6-7463728ea4f7/credential/password",
   "UserTemplateVoicePinURI": 
   "/vmrest/usertemplates/7426a16f-e735-4854-9ab6-7463728ea4f7/credential/pin",
   "UserTemplateMessageActionURI": 
   "/vmrest/usertemplates/7426a16f-e735-4854-9ab6-7463728ea4f7/usertemplatemessageactions",
   "DefaultUserTemplateURI": "/vmrest/userdefaulttemplates"
  }
  
} |
|---|

| Response Code: 200 |
|---|

| https://<connection_server>/vmrest/usertemplates/<objectId> |
|---|

| {
   "URI": "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d",
   "ObjectId": "885dd0af-bdb1-401f-b4e9-6bd9fc8d594d",
   "UseDefaultLanguage": "true",
   "UseDefaultTimeZone": "true",
   "Alias": "voicemailusertemplate",
   "DisplayName": "Voice Mail User Template",
   "TimeZone": "4",
   "CreationTime": "2012-07-29T14:10:26Z",
   "CosObjectId": "362bf7f9-7cec-4f59-86dd-6c058a9100ef",
   "CosURI": "/vmrest/coses/362bf7f9-7cec-4f59-86dd-6c058a9100ef",
   "Language": "1033",
   "LocationObjectId": "3a403c9c-04c8-496a-ba76-23faaaae5a95",
   "LocationURI": 
   "/vmrest/locations/connectionlocations/3a403c9c-04c8-496a-ba76-23faaaae5a95",
   "AddressMode": "0",
   "ClockMode": "0",
   "ConversationTui": "SubMenu",
   "GreetByName": "true",
   "ListInDirectory": "true",
   "IsVmEnrolled": "true",
   "SayCopiedNames": "true",
   "SayDistributionList": "true",
   "SayMsgNumber": "true",
   "SaySender": "true",
   "SayTimestampAfter": "true",
   "SayTimestampBefore": "false",
   "SayTotalNew": "false",
   "SayTotalNewEmail": "false",
   "SayTotalNewFax": "false",
   "SayTotalNewVoice": "true",
   "SayTotalReceipts": "false",
   "SayTotalSaved": "true",
   "Speed": "100",
   "MediaSwitchObjectId": "0d15753c-e1b4-4865-b00b-999a1ccf56ce",
   "PhoneSystemURI": 
   "/vmrest/phonesystems/0d15753c-e1b4-4865-b00b-999a1ccf56ce",
   "Undeletable": "true",
   "UseBriefPrompts": "false",
   "Volume": "50",
   "EnAltGreetDontRingPhone": "false",
   "EnAltGreetPreventSkip": "false",
   "EnAltGreetPreventMsg": "false",
   "EncryptPrivateMessages": "false",
   "DeletedMessageSortOrder": "2",
   "SayAltGreetWarning": "false",
   "SaySenderExtension": "false",
   "SayAni": "false",
   "ExitCallActionObjectId": "6352cf7d-89f8-4748-bac5-8878889c3d56",
   "CallAnswerTimeout": "4",
   "CallHandlerObjectId": "c9069370-3631-4d36-a53a-1ac4e8d8f444",
   "CallhandlerURI": 
   "/vmrest/callhandlerprimarytemplates/c9069370-3631-4d36-a53a-1ac4e8d8f444",
   "DisplayNameRule": "1",
   "DoesntExpire": "false",
   "CantChange": "false",
   "MailboxStoreObjectId": "6d2eb9ad-3caf-41d2-b3db-4451d95057fe",
   "SavedMessageStackOrder": "1234567",
   "NewMessageStackOrder": "1234567",
   "MessageLocatorSortOrder": "1",
   "SavedMessageSortOrder": "2",
   "NewMessageSortOrder": "1",
   "MessageTypeMenu": "false",
   "EnablePersonalRules": "true",
   "RecordUnknownCallerName": "true",
   "RingPrimaryPhoneFirst": "false",
   "PromptSpeed": "100",
   "ExitAction": "2",
   "ExitTargetConversation": "PHGreeting",
   "ExitTargetHandlerObjectId": "708d5a59-95bb-4804-979b-c56b2f7d719a",
   "RepeatMenu": "1",
   "FirstDigitTimeout": "5000",
   "InterdigitDelay": "3000",
   "PromptVolume": "50",
   "AddressAfterRecord": "false",
   "ConfirmDeleteMessage": "false",
   "ConfirmDeleteDeletedMessage": "false",
   "ConfirmDeleteMultipleMessages": "true",
   "IsClockMode24Hour": "false",
   "RouteNDRToSender": "true",
   "NotificationType": "0",
   "SendReadReceipts": "1",
   "ReceiveQuota": "2147483647",
   "SendQuota": "2147483647",
   "WarningQuota": "2147483647",
   "IsSetForVmEnrollment": "true",
   "VoiceNameRequired": "false",
   "SendBroadcastMsg": "false",
   "UpdateBroadcastMsg": "false",
   "ConversationVui": "VuiStart",
   "SpeechCompleteTimeout": "0",
   "SpeechIncompleteTimeout": "750",
   "UseVui": "false",
   "SkipPasswordForKnownDevice": "false",
   "JumpToMessagesOnLogin": "true",
   "EnableMessageLocator": "false",
   "MessageAgingPolicyObjectId": "a4b9216a-9360-4f9b-8937-cc66fba0ebbe",
   "MessageAgingPolicyURI": 
   "/vmrest/messageagingpolicies/a4b9216a-9360-4f9b-8937-cc66fba0ebbe",
   "AssistantRowsPerPage": "5",
   "InboxMessagesPerPage": "20",
   "InboxAutoRefresh": "15",
   "InboxAutoResolveMessageRecipients": "true",
   "PcaAddressBookRowsPerPage": "5",
   "ReadOnly": "false",
   "EnableTts": "true",
   "ConfirmationConfidenceThreshold": "60",
   "AnnounceUpcomingMeetings": "60",
   "SpeechConfidenceThreshold": "40",
   "SpeechSpeedVsAccuracy": "50",
   "SpeechSensitivity": "50",
   "EnableVisualMessageLocator": "false",
   "ContinuousAddMode": "false",
   "NameConfirmation": "false",
   "CommandDigitTimeout": "1500",
   "SaveMessageOnHangup": "false",
   "SendMessageOnHangup": "1",
   "SkipForwardTime": "12345",
   "SkipReverseTime": "54321",
   "UseShortPollForCache": "false",
   "SearchByExtensionSearchSpaceObjectId": 
   "a3933806-a995-443e-8704-498c03377bf7",
   "SearchByExtensionSearchSpaceURI": 
   "/vmrest/searchspaces/a3933806-a995-443e-8704-498c03377bf7",
   "SearchByNameSearchSpaceObjectId": 
   "a3933806-a995-443e-8704-498c03377bf7",
   "SearchByNameSearchSpaceURI": 
   "/vmrest/searchspaces/a3933806-a995-443e-8704-498c03377bf7",
   "PartitionObjectId": 
   "6ac064a3-79d6-4a52-a3d3-f4311be5c28c",
   "PartitionURI": 
   "/vmrest/partitions/6ac064a3-79d6-4a52-a3d3-f4311be5c28c",
   "UseDynamicNameSearchWeight": "false",
   "LdapType": "0",
   "EnableMessageBookmark": "false",
   "SayTotalDraftMsg": "false",
   "EnableSaveDraft": "false",
   "RetainUrgentMessageFlag": "false",
   "SayMessageLength": "false",
   "CreateSmtpProxyFromCorp": "false",
   "AutoAdvanceMsgs": "false",
   "SaySenderAfter": "false",
   "SaySenderExtensionAfter": "false",
   "SayMsgNumberAfter": "true",
   "SayAniAfter": "false",
   "SayMessageLengthAfter": "false",
   "UserTemplateRolesURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/usertemplateroles",
   "UserTemplateNotificationDevicesURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/usertemplatenotificationdevices",
   "TemplateExternalServiceAccountsURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/templateexternalserviceaccounts",
   "UserTemplateWebPasswordURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/credential/password",
   "UserTemplateVoicePinURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/credential/pin",
   "UserTemplateMessageActionURI": 
   "/vmrest/usertemplates/885dd0af-bdb1-401f-b4e9-6bd9fc8d594d/usertemplatemessageactions",
   "DefaultUserTemplateURI": "/vmrest/userdefaulttemplates"
} |
|---|

| Response Code: 200 |
|---|

| https://<connection_server>/vmrest/usertemplates?templateAlias=voicemailusertemplate |
|---|

| <UserTemplate>
 <DisplayName>DemoUserTemplate</DisplayName>
 <Alias>DemoUserTemplate</Alias>
</UserTemplate> |
|---|

| Response Code: 201 |
|---|

| https://<connection_server>/vmrest/usertemplates?templateAlias=voicemailusertemplate |
|---|

| {
  "Alias": "adminTemplate1",
  "DisplayName": "Admin Voice Mail Template"
   
} |
|---|

| Response Code: 201 |
|---|

| https://<connection_server>/vmrest/usertemplate/<objectId> |
|---|

| <UserTemplate>
 <SendBroadcastMsg>true</SendBroadcastMsg>
 <GreetByName>true</GreetByName>
 <ListInDirectory>true</ListInDirectory>
 <IsVmEnrolled>true</IsVmEnrolled>
 <SayCopiedNames>true</SayCopiedNames>
 <SayDistributionList>true</SayDistributionList>
 <SayMsgNumber>true</SayMsgNumber>
</UserTemplate> |
|---|

| Response Code: 204 |
|---|

| https://<connection_server>/vmrest/usertemplate/<objectId> |
|---|

| {
 "SendBroadcastMsg" : "true",
 "GreetByName" : "true",
 "ListInDirectory" : "true",
 "IsVmEnrolled" : "true"
 "SayCopiedNames" : "true",
 "SayDistributionList" : "true",
 "SayMsgNumber" :"true"
} |
|---|

| Response Code: 204 |
|---|

| https://<connection_server>/vmrest/usertemplates/<objectId> |
|---|

| Response Code: 204 |
|---|

| https://<connection_server>/vmrest/userdefaulttemplates |
|---|

| <DefaultUserTemplates total="2">
<DefaultUserTemplate>
 <URI>
  /vmrest/defaultusertemplates/48caecef-6f7a-47aa-91cb-019b761fce69
 </URI>
 <ObjectId>48caecef-6f7a-47aa-91cb-019b761fce69</ObjectId>
 <UseDefaultLanguage>true</UseDefaultLanguage>
 <UseDefaultTimeZone>true</UseDefaultTimeZone>
 <Alias>administratortemplate1</Alias>
 <City/>
 <State/>
 <Country>US</Country>
 <PostalCode/>
 <Department/>
 <Building/>
 <Address/>
 <DisplayName>Administrator Template</DisplayName>
 <BillingId/>
 <TimeZone>190</TimeZone>
 <CreationTime>2012-07-09T07:27:43Z</CreationTime>
 <Language>1033</Language>
 <LocationObjectId>be27976c-6e6e-419f-853d-b3764881dfb0</LocationObjectId>
 <LocationURI>
  /vmrest/locations/connectionlocations/be27976c-6e6e-419f-853d-b3764881dfb0
 </LocationURI>
 <DisplayNameRule>1</DisplayNameRule>
 <DoesntExpire>false</DoesntExpire>
 <CantChange>false</CantChange>
 <RouteNDRToSender>true</RouteNDRToSender>
 <Undeletable>true</Undeletable>
 <ReadOnly>false</ReadOnly>
 <PartitionObjectId>c2ecf6c5-b3c2-45f4-99fc-e065056501d5</PartitionObjectId>
 <PartitionURI>
  /vmrest/partitions/c2ecf6c5-b3c2-45f4-99fc-e065056501d5
 </PartitionURI>
 <LdapType>0</LdapType>
 <CreateSmtpProxyFromCorp>false</CreateSmtpProxyFromCorp>
 <DefaultUserTemplateWebPasswordURI>
 /vmrest/usertemplates/48caecef-6f7a-47aa-91cb-019b761fce69/credential/password
 </DefaultUserTemplateWebPasswordURI>
 <DefaultUserTemplateVoicePinURI>
 /vmrest/usertemplates/48caecef-6f7a-47aa-91cb-019b761fce69/credential/pin
 </DefaultUserTemplateVoicePinURI>
</DefaultUserTemplate>
<DefaultUserTemplate>
 <URI>
 /vmrest/defaultusertemplates/bc0eedd5-0483-4362-a091-5f89d27b7b3c
 </URI>
 <ObjectId>bc0eedd5-0483-4362-a091-5f89d27b7b3c</ObjectId>
 <UseDefaultLanguage>true</UseDefaultLanguage>
 <UseDefaultTimeZone>true</UseDefaultTimeZone>
 <Alias>voicemailusertemplate</Alias>
 <DisplayName>Voice Mail User Template</DisplayName>
 <TimeZone>190</TimeZone>
 <CreationTime>2012-07-09T07:27:44Z</CreationTime>
 <CosObjectId>305a9699-03a8-41d0-9215-0fcd32d600b0</CosObjectId>
 <CosURI>/vmrest/coses/305a9699-03a8-41d0-9215-0fcd32d600b0</CosURI>
 <Language>1033</Language>
 <LocationObjectId>be27976c-6e6e-419f-853d-b3764881dfb0</LocationObjectId>
 <LocationURI>
 /vmrest/locations/connectionlocations/be27976c-6e6e-419f-853d-b3764881dfb0
 </LocationURI>
 <DisplayNameRule>1</DisplayNameRule>
 <DoesntExpire>false</DoesntExpire>
 <CantChange>false</CantChange>
 <MailboxStoreObjectId>15dd71c8-2ba1-4efa-a34e-01613a0d2ef7</MailboxStoreObjectId>
 <RouteNDRToSender>true</RouteNDRToSender>
 <Undeletable>true</Undeletable>
 <ReadOnly>false</ReadOnly>
 <PartitionObjectId>c2ecf6c5-b3c2-45f4-99fc-e065056501d5</PartitionObjectId>
 <PartitionURI>
  /vmrest/partitions/c2ecf6c5-b3c2-45f4-99fc-e065056501d5
 </PartitionURI>
 <LdapType>0</LdapType>
 <CreateSmtpProxyFromCorp>false</CreateSmtpProxyFromCorp>
 <DefaultUserTemplateWebPasswordURI>
  /vmrest/usertemplates/bc0eedd5-0483-4362-a091-5f89d27b7b3c/credential/password
 </DefaultUserTemplateWebPasswordURI>
 <DefaultUserTemplateVoicePinURI>
 /vmrest/usertemplates/bc0eedd5-0483-4362-a091-5f89d27b7b3c/credential/pin
 </DefaultUserTemplateVoicePinURI>
</DefaultUserTemplate>
</DefaultUserTemplates> |
|---|

| Response code: 200 |
|---|

| https://<connection_server>/vmrest/userdefaulttemplates/<objectId> |
|---|

| <DefaultUserTemplate>
 <URI>
  /vmrest/defaultusertemplates/48caecef-6f7a-47aa-91cb-019b761fce69
 </URI>
 <TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
 <UseDefaultLanguage>true</UseDefaultLanguage>
 <UseDefaultTimeZone>true</UseDefaultTimeZone>
 <Alias>administratortemplate1</Alias>
 <City/>
 <State/>
 <Country>US</Country>
 <PostalCode/>
 <Department/>
 <Building/>
 <Address/>
 <DisplayName>Administrator Template</DisplayName>
 <BillingId/>
 <TimeZone>190</TimeZone>
 <CreationTime>2012-07-09T07:27:43Z</CreationTime>
 <Language>1033</Language>
 <LocationObjectId>be27976c-6e6e-419f-853d-b3764881dfb0</LocationObjectId>
 <LocationURI>
  /vmrest/locations/connectionlocations/be27976c-6e6e-419f-853d-b3764881dfb0
 </LocationURI>
 <DisplayNameRule>1</DisplayNameRule>
 <DoesntExpire>false</DoesntExpire>
 <CantChange>false</CantChange>
 <RouteNDRToSender>true</RouteNDRToSender>
 <Undeletable>true</Undeletable>
 <ReadOnly>false</ReadOnly>
 <PartitionObjectId>c2ecf6c5-b3c2-45f4-99fc-e065056501d5</PartitionObjectId>
 <PartitionURI>
  /vmrest/partitions/c2ecf6c5-b3c2-45f4-99fc-e065056501d5
 </PartitionURI>
 <LdapType>0</LdapType>
 <CreateSmtpProxyFromCorp>false</CreateSmtpProxyFromCorp>
 <DefaultUserTemplateWebPasswordURI>
  /vmrest/usertemplates/48caecef-6f7a-47aa-91cb-019b761fce69/credential/password
 </DefaultUserTemplateWebPasswordURI>
 <DefaultUserTemplateVoicePinURI>
  /vmrest/usertemplates/48caecef-6f7a-47aa-91cb-019b761fce69/credential/pin
 </DefaultUserTemplateVoicePinURI>
 </DefaultUserTemplate> |
|---|

| Response code: 200 |
|---|

| https://<connection_server>/vmrest/userdefaulttemplates/<objectId> |
|---|

| <DefaultUserTemplate>
 <City>San Jose</City>
 <State>CA</State>
 <Country>US</Country>
</DefaultUserTemplate> |
|---|

| Response code: 204 |
|---|

| https://<connection_server>/vmrest/usertemplates/<objectId>/credential/pin |
|---|

| <UserTemplateCredential>
 <Credentials>abcd@1234</Credentials>
</UserTemplateCredential> |
|---|

| Step 1 | Do the following GET command
                                          			 to list all the user templates: https://<connection_server>/vmrest/usertemplates | https://<connection_server>/vmrest/usertemplates |
|---|---|---|
| https://<connection_server>/vmrest/usertemplates |
| Step 2 | Do the following GET command
                                          			 to list the user template of your choice represented by the
                                          			 <usertemplate-id>: https://<connection_server>/vmrest/usertemplates/<objectId> | https://<connection_server>/vmrest/usertemplates/<objectId> |
| https://<connection_server>/vmrest/usertemplates/<objectId> |
| Step 3 | The following URI is the
                                          			 response from the above GET command: https://<connection_server>/vmrest/callhandlerprimarytemplates/<callhandlerprimarytemplates-id> | https://<connection_server>/vmrest/callhandlerprimarytemplates/<callhandlerprimarytemplates-id> |
| https://<connection_server>/vmrest/callhandlerprimarytemplates/<callhandlerprimarytemplates-id> |
| Step 4 | The following URI is the reponse from the above GET command: https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>/transferoptions | https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>/transferoptions |
| https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>/transferoptions |

| https://<connection_server>/vmrest/usertemplates |
|---|

| https://<connection_server>/vmrest/usertemplates/<objectId> |
|---|

| https://<connection_server>/vmrest/callhandlerprimarytemplates/<callhandlerprimarytemplates-id> |
|---|

| https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>/transferoptions |
|---|

| https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>/transferoptions/Alternate |
|---|

| https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>/transferoptions/Alternate |
|---|

| <?xml version="1.0" encoding="UTF-8"?>
<TransferOption>
  <TimeExpires>1976-03-09 00:00:00.0</TimeExpires>
</TransferOption> |
|---|

| Response Code: 204 |
|---|

| https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>/transferoptions/Alternate |
|---|

| <?xml version="1.0" encoding="UTF-8"?>
<TransferOption>
  <TransferHoldingMode>1</TransferHoldingMode>
</TransferOption> |
|---|

| Response Code: 204 |
|---|

| https://<connection_server>/vmrest/callhandlerprimarytemplates |
|---|

| <MenuEntries total="12">
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/*
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>*
 </TouchtoneKey>
 <Locked>true</Locked>
 <Action>2</Action>
 <TargetConversation>SubSignIn</TargetConversation>
 <ObjectId>1d111b26-d50c-44a3-bfcc-0b60f2e3207a
 </ObjectId>
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/#
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>#</TouchtoneKey>
 <Locked>true</Locked>
 <Action>5</Action>
 <ObjectId>3e3d796b-ffd3-4388-a2bf-b2cca2cf0b9c
 </ObjectId>
 </MenuEntry>
 <MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/0
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>0</TouchtoneKey>
 <Locked>false</Locked>
 <Action>2</Action>
 <TargetConversation>PHTransfer</TargetConversation>
 <TargetHandlerObjectId>e4c32c78-42c6-495e-83c5-4a4a17c0cb7f</TargetHandlerObjectId>
 <ObjectId>050b1a62-b237-457d-a027-d2c3289eab20
 </ObjectId>
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/1
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a -1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>1</TouchtoneKey>
 <Locked>false</Locked>
 <Action>0</Action>
 <ObjectId>31a8cba0-8deb-4266-b83b-57a6c1a33ebb
 </ObjectId>
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/2
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>2</TouchtoneKey>
 <Locked>false</Locked>
 <Action>0</Action>
 <ObjectId>f7e0cca3-e864-480b-bcd5-84f290587cbf
 </ObjectId> 
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/3
 </URI><CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>3</TouchtoneKey>
 <Locked>false</Locked>
 <Action>0</Action>
 <ObjectId>910a7722-5cc1-4f98-b6b5-d9ac0c11440f
 </ObjectId>
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/4
 </URI><CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>4</TouchtoneKey>
 <Locked>false</Locked>
 <Action>0</Action>
 <ObjectId>da2588dc-557e-4671-892b-edde2987d4c0
 </ObjectId>
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/5
 </URI><CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>5</TouchtoneKey>
 <Locked>false</Locked>
 <Action>0</Action>
 <ObjectId>15c55592-df99-46d0-9a96-19a6ecff2bd5
 </ObjectId>
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/6
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>6</TouchtoneKey>
 <Locked>false</Locked>
 <Action>0</Action>
 <ObjectId>bdb6a884-269e-4aab-9ff7-997453e69642
 </ObjectId>
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/7
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>7</TouchtoneKey>
 <Locked>false</Locked>
 <Action>2</Action>
 <TargetConversation>PHTransfer</TargetConversation>
 <TargetHandlerObjectId>b659a96c-6949-4d78-a899-93a2407baf28
 </TargetHandlerObjectId>
 <ObjectId>11e69e5d-1223-4727-ad8c-1dbe3f8f8ce5
 </ObjectId>
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/8
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>8</TouchtoneKey>
 <Locked>false</Locked>
 <Action>0</Action>
 <ObjectId>333a6147-cd06-4d71-9def-417cb70c8ebf
 </ObjectId>
</MenuEntry>
<MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/9
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>9</TouchtoneKey>
 <Locked>false</Locked>
 <Action>0</Action>
 <ObjectId>eb66e91d-2a82-425a-88f5-f2c058c2491e</ObjectId>
</MenuEntry>
</MenuEntries> |
|---|

| Response Code: 200 |
|---|

| https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId> |
|---|

| <MenuEntry>
 <URI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444/menuentries/*
 </URI>
 <CallHandlerObjectId>c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallHandlerObjectId>
 <CallhandlerURI>/vmrest/handlers/callhandlers/c9069370-3631-4d36-a53a-1ac4e8d8f444
 </CallhandlerURI>
 <TouchtoneKey>*
 </TouchtoneKey>
 <Locked>true</Locked>
 <Action>2</Action>
 <TargetConversation>SubSignIn</TargetConversation>
 <ObjectId>1d111b26-d50c-44a3-bfcc-0b60f2e3207a
 </ObjectId>
</MenuEntry> |
|---|

| Response Code: 204 |
|---|

| Field Name | Writable? | Available Values | Explanation/Comment |
|---|---|---|---|
| ObjectId | Read Only | All | ObjectId of the Device. |
| OneKeyDelay | Read/Write | 0-10000 | Indicate the amount of time that Cisco Unity Connection waits for additional input after callers press a single key that is
                                          not locked. Default: 1500 |
| EnablePrependDigits | Read/Write | true/false | Enable to simulate abbreviated extensions by using prepended digits for call handlers and user mailboxes. Default: false |
| PrependDigits | Read/Write | Data Length[40] | Enter the digits that are prepended to any extension that a caller dials while listening to the greeting of the user. |
| TouchtoneKey | Read/Write | Length(1) | Edit caller input settings. |
| Locked | Read/Write | true/false | Indicates whether Cisco Unity Connection allows additional input (Unlocked) or ignores additional input (Locked). Default:
                                          false |
| Action | Read/Write | 2-Go to an object such as a call handler, directory handler or interview handler. 1- HangUp 0-ignore 6-RestartGreeting 8- Route from next calling route 5- Skip Greeting 4- Take message 7- Transfer to Alternate
                                             contact number | Indicates the action that Cisco Unity Connection takes when a caller presses the key. |

| https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>/usertemplategreetings |
|---|

| <?xml version="1.0" encoding="UTF-8" standalone="yes" ?> 
<UserTemplateGreetings total="7">
<UserTemplateGreeting>
  <CallHandlerObjectId>a254488a-7f96-4737-9df4-886e3f4b88af</CallHandlerObjectId> 
  <CallhandlerURI>/vmrest/callhandlerprimarytemplates/a254488a-7f96-4737-9df4-886e3f4b88af</CallhandlerURI> 
  <IgnoreDigits>false</IgnoreDigits> 
  <PlayWhat>1</PlayWhat> 
  <RepromptDelay>20</RepromptDelay> 
  <Reprompts>30</Reprompts> 
  <TimeExpires>2012-10-06 09:25:00.0</TimeExpires> 
  <GreetingType>Alternate</GreetingType> 
  <AfterGreetingAction>2</AfterGreetingAction> 
  <AfterGreetingTargetConversation>PHTransfer</AfterGreetingTargetConversation> 
  <AfterGreetingTargetHandlerObjectId>9e96f34b-22bc-429a-8852-46fbceeff182</AfterGreetingTargetHandlerObjectId> 
  <PlayRecordMessagePrompt>false</PlayRecordMessagePrompt> 
  <EnableTransfer>false</EnableTransfer>
  <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
  <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt> 
  <EnAltGreetDontRingPhone>true</EnAltGreetDontRingPhone> 
  <EnAltGreetPreventSkip>true</EnAltGreetPreventSkip> 
  <EnAltGreetPreventMsg>true</EnAltGreetPreventMsg> 
  <LanguageCode>1033</LanguageCode> 
</UserTemplateGreeting>
<UserTemplateGreeting>
  <CallHandlerObjectId>a254488a-7f96-4737-9df4-886e3f4b88af</CallHandlerObjectId> 
  <CallhandlerURI>/vmrest/callhandlerprimarytemplates/a254488a-7f96-4737-9df4-886e3f4b88af</CallhandlerURI> 
  <IgnoreDigits>false</IgnoreDigits> 
  <PlayWhat>0</PlayWhat> 
  <RepromptDelay>2</RepromptDelay> 
  <Reprompts>0</Reprompts> 
  <TimeExpires>2020-10-06 09:25:00.0</TimeExpires> 
  <GreetingType>Busy</GreetingType> 
  <AfterGreetingAction>4</AfterGreetingAction> 
  <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt> 
  <EnableTransfer>true</EnableTransfer>
  <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
  <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt> 
  <LanguageCode>1033</LanguageCode> 
</UserTemplateGreeting>
<UserTemplateGreeting>
  <CallHandlerObjectId>a254488a-7f96-4737-9df4-886e3f4b88af</CallHandlerObjectId> 
  <CallhandlerURI>/vmrest/callhandlerprimarytemplates/a254488a-7f96-4737-9df4-886e3f4b88af</CallhandlerURI> 
  <IgnoreDigits>false</IgnoreDigits> 
  <PlayWhat>0</PlayWhat> 
  <RepromptDelay>2</RepromptDelay> 
  <Reprompts>0</Reprompts> 
  <GreetingType>Error</GreetingType> 
  <AfterGreetingAction>6</AfterGreetingAction> 
  <AfterGreetingTargetConversation>PHGreeting</AfterGreetingTargetConversation> 
  <AfterGreetingTargetHandlerObjectId>08313019-91db-4aed-8ef3-af13a4a72e22</AfterGreetingTargetHandlerObjectId> 
  <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt> 
  <EnableTransfer>false</EnableTransfer> 
  <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
  <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt>
  <LanguageCode>1033</LanguageCode> 
</UserTemplateGreeting>
<UserTemplateGreeting>
  <CallHandlerObjectId>a254488a-7f96-4737-9df4-886e3f4b88af</CallHandlerObjectId> 
  <CallhandlerURI>/vmrest/callhandlerprimarytemplates/a254488a-7f96-4737-9df4-886e3f4b88af</CallhandlerURI> 
  <IgnoreDigits>false</IgnoreDigits> 
  <PlayWhat>0</PlayWhat> 
  <RepromptDelay>2</RepromptDelay> 
  <Reprompts>0</Reprompts> 
  <TimeExpires>2013-01-01 00:00:00.0</TimeExpires> 
  <GreetingType>Internal</GreetingType> 
  <AfterGreetingAction>4</AfterGreetingAction> 
  <PlayRecordMessagePrompt>false</PlayRecordMessagePrompt> 
  <EnableTransfer>false</EnableTransfer> 
  <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
  <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt>
  <LanguageCode>1033</LanguageCode> 
</UserTemplateGreeting>
<UserTemplateGreeting>
  <CallHandlerObjectId>a254488a-7f96-4737-9df4-886e3f4b88af</CallHandlerObjectId> 
  <CallhandlerURI>/vmrest/callhandlerprimarytemplates/a254488a-7f96-4737-9df4-886e3f4b88af</CallhandlerURI> 
  <IgnoreDigits>false</IgnoreDigits> 
  <PlayWhat>0</PlayWhat> 
  <RepromptDelay>2</RepromptDelay> 
  <Reprompts>0</Reprompts> 
  <TimeExpires>1972-01-01 00:00:00.0</TimeExpires> 
  <GreetingType>Off Hours</GreetingType> 
  <AfterGreetingAction>4</AfterGreetingAction> 
  <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt> 
  <EnableTransfer>false</EnableTransfer> 
  <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
  <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt>
  <LanguageCode>1033</LanguageCode> 
</UserTemplateGreeting>
<UserTemplateGreeting>
  <CallHandlerObjectId>a254488a-7f96-4737-9df4-886e3f4b88af</CallHandlerObjectId> 
  <CallhandlerURI>/vmrest/callhandlerprimarytemplates/a254488a-7f96-4737-9df4-886e3f4b88af</CallhandlerURI> 
  <IgnoreDigits>false</IgnoreDigits> 
  <PlayWhat>0</PlayWhat> 
  <RepromptDelay>2</RepromptDelay> 
  <Reprompts>0</Reprompts> 
  <GreetingType>Standard</GreetingType> 
  <AfterGreetingAction>4</AfterGreetingAction> 
  <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt> 
  <EnableTransfer>false</EnableTransfer> 
  <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
  <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt>
  <LanguageCode>1033</LanguageCode> 
</UserTemplateGreeting>
<UserTemplateGreeting>
  <CallHandlerObjectId>a254488a-7f96-4737-9df4-886e3f4b88af</CallHandlerObjectId> 
  <CallhandlerURI>/vmrest/callhandlerprimarytemplates/a254488a-7f96-4737-9df4-886e3f4b88af</CallhandlerURI> 
  <IgnoreDigits>false</IgnoreDigits> 
  <PlayWhat>0</PlayWhat> 
  <RepromptDelay>2</RepromptDelay> 
  <Reprompts>0</Reprompts> 
  <TimeExpires>1972-01-01 00:00:00.0</TimeExpires> 
  <GreetingType>Holiday</GreetingType> 
  <AfterGreetingAction>4</AfterGreetingAction> 
  <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt> 
  <EnableTransfer>false</EnableTransfer> 
  <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
  <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt>
  <LanguageCode>1033</LanguageCode> 
</UserTemplateGreeting>
</UserTemplateGreetings> |
|---|

| Response Code: 200 |
|---|

| https://<connection_server>/vmrest/callhandlerprimarytemplates/<objectId>/usertemplategreetings/<Greeting-type |
|---|

| <UserTemplateGreeting>
 <EnableTransfer>true</EnableTransfer> 
  <RepromptDelay>454354</RepromptDelay> 
  <Reprompts>30</Reprompts> 
</UserTemplateGreeting> |
|---|

| Response Code: 204 |
|---|

| https://<connection-server>/vmrest/usertemplates/<objectId>/usertemplatenotificationdevices |
|---|

| <UserTemplateNotificationDevices total="7">
<UserTemplateNotificationDevice>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/usertemplatenotificationdevices/22b1e3cc-f13d-4349-8811-a196132781a3</URI>
 <SubscriberObjectId>85a845d3-063d-4641-aa70-8b536282bffb</SubscriberObjectId>
 <UserURI>/vmrest/users/85a845d3-063d-4641-aa70-8b536282bffb</UserURI>
 <ObjectId>22b1e3cc-f13d-4349-8811-a196132781a3</ObjectId>
 <DisplayName>Pager</DisplayName>
 <Active>false</Active>
 <BusyRetryInterval>5</BusyRetryInterval>
 <Type>2</Type>
 <DialDelay>1</DialDelay>
 <MaxBody>512</MaxBody>
 <MaxSubject>64</MaxSubject>
 <RetriesOnBusy>4</RetriesOnBusy>
 <RetriesOnRna>4</RetriesOnRna>
 <RingsToWait>4</RingsToWait>
 <RnaRetryInterval>15</RnaRetryInterval>
 <SendCount>true</SendCount>
 <WaitConnect>true</WaitConnect>
 <MediaSwitchObjectId>24f1171f-27b3-4ad3-a94c-66d1fb2e448b</MediaSwitchObjectId>
 <PhoneSystemURI>/vmrest/phonesystems/24f1171f-27b3-4ad3-a94c-66d1fb2e448b</PhoneSystemURI>
 <TransmitForcedAuthorizationCode>false</TransmitForcedAuthorizationCode>
 <DeviceName>Pager</DeviceName>
 <PromptForId>false</PromptForId>
 <SendCallerId>true</SendCallerId>
 <SendPcaLink>false</SendPcaLink>
 <Undeletable>true</Undeletable>
 <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
 <DetectTransferLoop>false</DetectTransferLoop>
 <SuccessRetryInterval>1</SuccessRetryInterval>
 <RetriesOnSuccess>0</RetriesOnSuccess>
 <EventList>NewVoiceMail</EventList>
 <ScheduleSetObjectId>a884af0a-dd5f-4597-8bc7-31a61e8b612a</ScheduleSetObjectId>
 <InitialDelay>0</InitialDelay>
 <RepeatInterval>0</RepeatInterval>
 <RepeatNotify>false</RepeatNotify>
 </UserTemplateNotificationDevice>
 <UserTemplateNotificationDevice>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/usertemplatenotificationdevices/d2e67ebc-a987-441d-a168-88d1d7dc49c2</URI>
 <SubscriberObjectId>85a845d3-063d-4641-aa70-8b536282bffb</SubscriberObjectId>
 <UserURI>/vmrest/users/85a845d3-063d-4641-aa70-8b536282bffb</UserURI>
 <ObjectId>d2e67ebc-a987-441d-a168-88d1d7dc49c2</ObjectId>
 <DisplayName>PagerDevice</DisplayName>
 <Active>false</Active>
 <BusyRetryInterval>5</BusyRetryInterval>
 <Type>2</Type>
 <DialDelay>1</DialDelay>
 <MaxBody>512</MaxBody>
 <MaxSubject>64</MaxSubject>
 <RetriesOnBusy>4</RetriesOnBusy>
 <RetriesOnRna>4</RetriesOnRna>
 <RingsToWait>4</RingsToWait>
 <RnaRetryInterval>15</RnaRetryInterval>
 <SendCount>true</SendCount>
 <WaitConnect>true</WaitConnect>
 <MediaSwitchObjectId>24f1171f-27b3-4ad3-a94c-66d1fb2e448b</MediaSwitchObjectId>
 <PhoneSystemURI>/vmrest/phonesystems/24f1171f-27b3-4ad3-a94c-66d1fb2e448b</PhoneSystemURI>
 <TransmitForcedAuthorizationCode>false</TransmitForcedAuthorizationCode>
 <DeviceName>Other</DeviceName>
 <PromptForId>false</PromptForId>
 <SendCallerId>true</SendCallerId>
 <SendPcaLink>false</SendPcaLink>
 <Undeletable>false</Undeletable>
 <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
 <DetectTransferLoop>false</DetectTransferLoop>
 <SuccessRetryInterval>1</SuccessRetryInterval>
 <RetriesOnSuccess>0</RetriesOnSuccess>
 <EventList>NewVoiceMail</EventList>
 <ScheduleSetObjectId>a884af0a-dd5f-4597-8bc7-31a61e8b612a</ScheduleSetObjectId>
 <InitialDelay>0</InitialDelay>
 <RepeatInterval>0</RepeatInterval>
 <RepeatNotify>false</RepeatNotify>
 </UserTemplateNotificationDevice>
 <UserTemplateNotificationDevice>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/usertemplatenotificationdevices/53bd701a-7301-49d0-8404-9769b38094cd</URI>
 <SubscriberObjectId>85a845d3-063d-4641-aa70-8b536282bffb</SubscriberObjectId>
 <UserURI>/vmrest/users/85a845d3-063d-4641-aa70-8b536282bffb</UserURI>
 <ObjectId>53bd701a-7301-49d0-8404-9769b38094cd</ObjectId>
 <DisplayName>Work Phone</DisplayName>
 <Active>false</Active>
 <BusyRetryInterval>5</BusyRetryInterval>
 <Conversation>SubNotify</Conversation>
 <Type>1</Type>
 <DialDelay>1</DialDelay>
 <MaxBody>512</MaxBody>
 <MaxSubject>64</MaxSubject>
 <RetriesOnBusy>4</RetriesOnBusy>
 <RetriesOnRna>4</RetriesOnRna>
 <RingsToWait>4</RingsToWait>
 <RnaRetryInterval>15</RnaRetryInterval>
 <SendCount>false</SendCount>
 <WaitConnect>true</WaitConnect>
 <MediaSwitchObjectId>24f1171f-27b3-4ad3-a94c-66d1fb2e448b</MediaSwitchObjectId>
 <PhoneSystemURI>/vmrest/phonesystems/24f1171f-27b3-4ad3-a94c-66d1fb2e448b</PhoneSystemURI>
 <TransmitForcedAuthorizationCode>false</TransmitForcedAuthorizationCode>
 <DeviceName>Work Phone</DeviceName>
 <PromptForId>false</PromptForId>
 <SendCallerId>false</SendCallerId>
 <SendPcaLink>false</SendPcaLink>
 <Undeletable>true</Undeletable>
 <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
 <DetectTransferLoop>false</DetectTransferLoop>
 <SuccessRetryInterval>0</SuccessRetryInterval>
 <RetriesOnSuccess>0</RetriesOnSuccess>
 <EventList>NewVoiceMail</EventList>
 <ScheduleSetObjectId>a884af0a-dd5f-4597-8bc7-31a61e8b612a</ScheduleSetObjectId>
 <InitialDelay>0</InitialDelay>
 <RepeatInterval>0</RepeatInterval>
 <RepeatNotify>false</RepeatNotify>
 </UserTemplateNotificationDevice>
 <UserTemplateNotificationDevice>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/usertemplatenotificationdevices/fa8d720c-7c03-4506-867f-780636b00c13</URI>
 <SubscriberObjectId>85a845d3-063d-4641-aa70-8b536282bffb</SubscriberObjectId>
 <UserURI>/vmrest/users/85a845d3-063d-4641-aa70-8b536282bffb</UserURI>
 <ObjectId>fa8d720c-7c03-4506-867f-780636b00c13</ObjectId>
 <DisplayName>Home Phone</DisplayName>
 <Active>false</Active>
 <BusyRetryInterval>5</BusyRetryInterval>
 <Conversation>SubNotify</Conversation>
 <Type>1</Type>
 <DialDelay>1</DialDelay>
 <MaxBody>512</MaxBody>
 <MaxSubject>64</MaxSubject>
 <RetriesOnBusy>4</RetriesOnBusy>
 <RetriesOnRna>4</RetriesOnRna>
 <RingsToWait>4</RingsToWait>
 <RnaRetryInterval>15</RnaRetryInterval>
 <SendCount>false</SendCount>
 <WaitConnect>true</WaitConnect>
 <MediaSwitchObjectId>24f1171f-27b3-4ad3-a94c-66d1fb2e448b</MediaSwitchObjectId>
 <PhoneSystemURI>/vmrest/phonesystems/24f1171f-27b3-4ad3-a94c-66d1fb2e448b</PhoneSystemURI>
 <TransmitForcedAuthorizationCode>false</TransmitForcedAuthorizationCode>
 <DeviceName>Home Phone</DeviceName>
 <PromptForId>false</PromptForId>
 <SendCallerId>false</SendCallerId>
 <SendPcaLink>false</SendPcaLink>
 <Undeletable>true</Undeletable>
 <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
 <DetectTransferLoop>false</DetectTransferLoop>
 <SuccessRetryInterval>0</SuccessRetryInterval>
 <RetriesOnSuccess>0</RetriesOnSuccess>
 <EventList>NewVoiceMail</EventList>
 <ScheduleSetObjectId>a884af0a-dd5f-4597-8bc7-31a61e8b612a</ScheduleSetObjectId>
 <InitialDelay>0</InitialDelay>
 <RepeatInterval>0</RepeatInterval>
 <RepeatNotify>false</RepeatNotify>
 </UserTemplateNotificationDevice>
 <UserTemplateNotificationDevice>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/usertemplatenotificationdevices/24cd2817-2911-4668-b740-24369c4b0d19</URI>
 <SubscriberObjectId>85a845d3-063d-4641-aa70-8b536282bffb</SubscriberObjectId>
 <UserURI>/vmrest/users/85a845d3-063d-4641-aa70-8b536282bffb</UserURI>
 <ObjectId>24cd2817-2911-4668-b740-24369c4b0d19</ObjectId>
 <DisplayName>Mobile Phone</DisplayName>
 <Active>false</Active>
 <BusyRetryInterval>5</BusyRetryInterval>
 <Conversation>SubNotify</Conversation>
 <Type>1</Type>
 <DialDelay>1</DialDelay>
 <MaxBody>512</MaxBody>
 <MaxSubject>64</MaxSubject>
 <RetriesOnBusy>4</RetriesOnBusy>
 <RetriesOnRna>4</RetriesOnRna>
 <RingsToWait>4</RingsToWait>
 <RnaRetryInterval>15</RnaRetryInterval>
 <SendCount>false</SendCount>
 <WaitConnect>true</WaitConnect>
 <MediaSwitchObjectId>24f1171f-27b3-4ad3-a94c-66d1fb2e448b</MediaSwitchObjectId>
 <PhoneSystemURI>/vmrest/phonesystems/24f1171f-27b3-4ad3-a94c-66d1fb2e448b</PhoneSystemURI>
 <TransmitForcedAuthorizationCode>false</TransmitForcedAuthorizationCode>
 <DeviceName>Mobile Phone</DeviceName>
 <PromptForId>false</PromptForId>
 <SendCallerId>false</SendCallerId>
 <SendPcaLink>false</SendPcaLink>
 <Undeletable>true</Undeletable>
 <MediaSwitchDisplayName>PhoneSystem</MediaSwitchDisplayName>
 <DetectTransferLoop>false</DetectTransferLoop>
 <SuccessRetryInterval>0</SuccessRetryInterval>
 <RetriesOnSuccess>0</RetriesOnSuccess>
 <EventList>NewVoiceMail</EventList>
 <ScheduleSetObjectId>a884af0a-dd5f-4597-8bc7-31a61e8b612a</ScheduleSetObjectId>
 <InitialDelay>0</InitialDelay>
 <RepeatInterval>0</RepeatInterval>
 <RepeatNotify>false</RepeatNotify>
 </UserTemplateNotificationDevice>
 <UserTemplateNotificationDevice>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/usertemplatenotificationdevices/d6871a13-4680-428a-a839-afb6d3b46b6b</URI>
 <SubscriberObjectId>85a845d3-063d-4641-aa70-8b536282bffb</SubscriberObjectId>
 <UserURI>/vmrest/users/85a845d3-063d-4641-aa70-8b536282bffb</UserURI>
 <ObjectId>d6871a13-4680-428a-a839-afb6d3b46b6b</ObjectId>
 <DisplayName>SMTP</DisplayName>
 <Active>false</Active>
 <BusyRetryInterval>0</BusyRetryInterval>
 <Type>4</Type>
 <DialDelay>0</DialDelay>
 <MaxBody>512</MaxBody>
 <MaxSubject>64</MaxSubject>
 <RetriesOnBusy>0</RetriesOnBusy>
 <RetriesOnRna>0</RetriesOnRna>
 <RingsToWait>0</RingsToWait>
 <RnaRetryInterval>0</RnaRetryInterval>
 <SendCount>true</SendCount>
 <WaitConnect>false</WaitConnect>
 <TransmitForcedAuthorizationCode>false</TransmitForcedAuthorizationCode>
 <DeviceName>SMTP</DeviceName>
 <PromptForId>false</PromptForId>
 <SendCallerId>true</SendCallerId>
 <SendPcaLink>false</SendPcaLink>
 <Undeletable>true</Undeletable>
 <DetectTransferLoop>false</DetectTransferLoop>
 <SuccessRetryInterval>0</SuccessRetryInterval>
 <RetriesOnSuccess>0</RetriesOnSuccess>
 <EventList>NewVoiceMail</EventList>
 <ScheduleSetObjectId>a884af0a-dd5f-4597-8bc7-31a61e8b612a</ScheduleSetObjectId>
 <InitialDelay>0</InitialDelay>
 <RepeatInterval>0</RepeatInterval>
 <RepeatNotify>false</RepeatNotify>
</UserTemplateNotificationDevice>
<UserTemplateNotificationDevice>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/usertemplatenotificationdevices/9f2f0ce2-0567-421a-bd89-973ceecb8518</URI>
 <SubscriberObjectId>85a845d3-063d-4641-aa70-8b536282bffb</SubscriberObjectId>
 <UserURI>/vmrest/users/85a845d3-063d-4641-aa70-8b536282bffb</UserURI>
 <ObjectId>9f2f0ce2-0567-421a-bd89-973ceecb8518</ObjectId>
 <DisplayName>HTML</DisplayName>
 <Active>false</Active>
 <BusyRetryInterval>0</BusyRetryInterval>
 <Type>8</Type>
 <DialDelay>0</DialDelay>
 <MaxBody>512</MaxBody>
 <MaxSubject>64</MaxSubject>
 <RetriesOnBusy>0</RetriesOnBusy>
 <RetriesOnRna>0</RetriesOnRna>
 <RingsToWait>0</RingsToWait>
 <RnaRetryInterval>0</RnaRetryInterval>
 <SendCount>false</SendCount>
 <SmtpAddress>aaaa</SmtpAddress>
 <WaitConnect>false</WaitConnect>
 <TransmitForcedAuthorizationCode>false</TransmitForcedAuthorizationCode>
 <DeviceName>HTML</DeviceName>
 <PromptForId>false</PromptForId>
 <SendCallerId>false</SendCallerId>
 <SendPcaLink>false</SendPcaLink>
 <Undeletable>true</Undeletable>
 <DetectTransferLoop>false</DetectTransferLoop>
 <SuccessRetryInterval>0</SuccessRetryInterval>
 <RetriesOnSuccess>0</RetriesOnSuccess>
 <EventList>NewVoiceMail</EventList>
 <ScheduleSetObjectId>a884af0a-dd5f-4597-8bc7-31a61e8b612a</ScheduleSetObjectId>
 <InitialDelay>0</InitialDelay>
 <RepeatInterval>0</RepeatInterval>
 <RepeatNotify>false</RepeatNotify>
</UserTemplateNotificationDevice>
</UserTemplateNotificationDevices> |
|---|

| Response Code: 200 |
|---|

| https://<connection_server>/vmrest/usertemplates/<objectId>/usertemplatenotificationdevices/<objectId> |
|---|

| <UserTemplateNotificationDevice>
 <URI>/vmrest/usertemplates/85a845d3-063d-4641-aa70-8b536282bffb/usertemplatenotificationdevices/9f2f0ce2-0567-421a-bd89-973ceecb8518</URI>
 <SubscriberObjectId>85a845d3-063d-4641-aa70-8b536282bffb</SubscriberObjectId>
 <UserURI>/vmrest/users/85a845d3-063d-4641-aa70-8b536282bffb</UserURI>
 <ObjectId>9f2f0ce2-0567-421a-bd89-973ceecb8518</ObjectId>
 <DisplayName>HTML</DisplayName>
 <Active>false</Active>
 <Type>8</Type>
 <MaxBody>512</MaxBody>
 <MaxSubject>64</MaxSubject>
 <SmtpAddress>aaaa</SmtpAddress>
 <DeviceName>HTML</DeviceName>
 <Undeletable>true</Undeletable>
 <EventList>NewVoiceMail</EventList>
 <ScheduleSetObjectId>a884af0a-dd5f-4597-8bc7-31a61e8b612a</ScheduleSetObjectId>
 <InitialDelay>0</InitialDelay>
 <RepeatInterval>0</RepeatInterval>
 <RepeatNotify>false</RepeatNotify>
</UserTemplateNotificationDevice>

<pre> Response Code: 200 |
|---|

| https://<connection_server>/vmrest/usertemplates/<objectId>/notificationdevices/<objectId> |
|---|

| <UserTemplatePagerDevice>
 <DisplayName>pager1</DisplayName>
 <MediaSwitchObjectId>2b6324a2-d66f-4f25-9572-decf88c9a0b7</MediaSwitchObjectId>
 <PhoneNumber>5656</PhoneNumber>
</UserTemplatePagerDevice> |
|---|

| Response Code: 201 |
|---|

| https://<connection_server>/vmrest/usertemplates/<objectId>/notificationdevices/<objectId> |
|---|

| <UserTemplatePhoneDevice>
 <DisplayName>pager1</DisplayName>
 <MediaSwitchObjectId>2b6324a2-d66f-4f25-9572-decf88c9a0b7</MediaSwitchObjectId>
 <PhoneNumber>5656</PhoneNumber>
</UserTemplatePhoneDevice> |
|---|

| Response Code: 201 |
|---|

| https://<connection_server>/vmrest/usertemplates/<objectId>/notificationdevices/<objectId> |
|---|

| <UserTemplateHtmlDevice>
 <DisplayName>Html</DisplayName>
 < SmtpAddress> a@cisco.com</SmtpAddress>
 <CallbackNumber>1111</CallbackNumber>
</UserTemplateHtmlDevice> |
|---|

| Response Code: 201 |
|---|

| https://<connection_server>/vmrest/usertemplates/<objectId>/notificationdevices/<objectId> |
|---|

| <UserTemplateSmtpDevice>
 <DisplayName>SMTP</DisplayName>
 <SmtpAddress> a@cisco.com</SmtpAddress>
 <PhoneNumber>5656</PhoneNumber>
</UserTemplateSmtpDevice> |
|---|

| Response Code: 201 |
|---|

| https://<connection_server>/vmrest/usertemplates/<objectId>/usertemplatenotificationdevices/<objectId> |
|---|

| <UserTemplatePhoneDevice>
 <Active>false</Active>
 <RepeatInterval>0</RepeatInterval>
 <RepeatNotify>true</RepeatNotify>
 <PhoneNumber>123456</PhoneNumber>
 <AfterDialDigits>11111</AfterDialDigits>
 <DialDelay>0</DialDelay>
 <RingsToWait>100</RingsToWait>
 <RetriesOnBusy>4</RetriesOnBusy>
 <RetriesOnRna>4</RetriesOnRna>
 <BusyRetryInterval>1</BusyRetryInterval>
 <RnaRetryInterval>100</RnaRetryInterval>
 <RetriesOnRna>100</RetriesOnRna>
 <MediaSwitchObjectId>1fb12b1c-cf14-4634-b73d-9b9c58ecdf68</MediaSwitchObjectId>
 <PromptForId>false</PromptForId>
 <EventList>NewUrgentFax,UrgentDispatchMessage</EventList>
</UserTemplatePhoneDevice> |
|---|

| Response Code: 204 |
|---|

| https://<connection_server>/vmrest/usertemplates/<objectId>/usertemplatenotificationdevices/<objectId> |
|---|

| Response Code: 204 |
|---|

| GET: https://<server-ip>/vmrest/usertemplates/981d804d-7a81-4171-b33e-8a4b12e0c309/usertemplatevideoserviceaccounts |
|---|

| 200 
OK

<UserTemplateVideoServiceAccounts total="1">
 <UserTemplateVideoServiceAccount>
   <URI>/vmrest/usertemplates/981d804d-7a81-4171-b33e-8a4b12e0c309/usertemplatevideoserviceaccount/88397230-91a7-4248-910d-11e9fd5a8dc3</URI>
   <ConnectorFactoryObjectId>bf9e3b86-4306-4da3-a958-40f9197c99bd</ConnectorFactoryObjectId>
   <IsConnectorMapped>true</IsConnectorMapped>
   <ObjectId>88397230-91a7-4248-910d-11e9fd5a8dc3</ObjectId>
   <UserTemplateObjectId>981d804d-7a81-4171-b33e-8a4b12e0c309</UserTemplateObjectId>
   <UserTemplateURI>/vmrest/usertemplates/981d804d-7a81-4171-b33e-8a4b12e0c309</UserTemplateURI>
   <ConnectorFactoryName>test</ConnectorFactoryName>
   <MediaServerType>0</MediaServerType>
 </UserTemplateVideoServiceAccount>
</UserTemplateVideoServiceAccounts> |
|---|

| GET: https://<connection-ip-address>/vmrest/usertemplates/<TemplateObjectid>/usertemplatevideoserviceaccounts |
|---|

| 200
Ok
{
  "UserTemplateVideoServiceAccounts": {
    "-total": "1",
    "UserTemplateVideoServiceAccount": {
      "URI": "/vmrest/usertemplates/b98c46a4-ceaa-43df-bac6-4bd0620dc904/usertemplatevideoserviceaccounts/56b22a57-ffdc-4056-a5a9-5aa1d0987271",
      "ConnectorFactoryObjectId": "dbd26014-fe57-4d00-bd5a-a1df1bdae6a2",
      "IsConnectorMapped": "true",
      "ObjectId": "56b22a57-ffdc-4056-a5a9-5aa1d0987271",
      "UserTemplateObjectId": "b98c46a4-ceaa-43df-bac6-4bd0620dc904",
      "UserTemplateURI": "/vmrest/usertemplates/b98c46a4-ceaa-43df-bac6-4bd0620dc904",
      "ConnectorFactoryName": "video",
      "MediaServerType": "0"
    }
  }
} |
|---|

| POST: https://<server-ip>/vmrest/usertemplates/<templateobjectid>/usertemplatevideoserviceaccounts |
|---|

| <UserTemplateVideoServiceAccount>
   <ConnectorFactoryObjectId>bf9e3b86-4306-4da3-a958-40f9197c99bd</ConnectorFactoryObjectId>
   <IsConnectorMapped>true</IsConnectorMapped>
   <ConnectorFactoryName>test</ConnectorFactoryName>
   <MediaServerType>0</MediaServerType>
</UserTemplateVideoServiceAccount> |
|---|

| 201 OK |
|---|

| /vmrest/usertemplates/981d804d-7a81-4171-b33e-8a4b12e0c309/usertemplatevideoserviceaccount/88397230-91a7-4248-910d-11e9fd5a8dc3 |
|---|

| POST:https://<connection-ip-address>/vmrest/usertemplates/<TemplateObjectid>/usertemplatevideoserviceaccounts
Accept: application/json
Content-type: application/json |
|---|

| {
             "TemplateVideoService": {  "ConnectorFactoryObjectId": "dbd26014-fe57-4d00-bd5a-  a1df1bdae6a2",
           "ConnectorFactoryName": "myservice"
 }
} |
|---|

| /vmrest/usertemplates/<TemplateObjectId>/ usertemplatevideoserviceaccounts /<TemplateObjectid>/ |
|---|

| PUT: https://<server-ip>/vmrest/usertemplates/<templateobjectid>/usertemplatevideoserviceaccounts/<objectid> |
|---|

| <UserTemplateVideoServiceAccount>
 <ConnectorFactoryObjectId>bf9e3b86-4306-4da3-a958-40f9197c99bd</ConnectorFactoryObjectId>
 <IsConnectorMapped>true</IsConnectorMapped>
 <ConnectorFactoryName>test</ConnectorFactoryName>
 <MediaServerType>0</MediaServerType>
</UserTemplateVideoServiceAccount> |
|---|

| 204 OK |
|---|

| PUT: https://<connection-ip-address>/vmrest/usertemplates/<TemplateObjectid>/usertemplatevideoserviceaccounts/<ObjectId>
Accept: application/json
Content-type: application/json |
|---|

| {
   	    "TemplateVideoService": {
 	    "IsConnectorMapped": "false ",
   	    "ConnectorFactoryName": "myservice",
     	    "MediaServerType": "0"
                  }
               } |
|---|

| 204 |
|---|

| Request URI :https://<server-ip>/vmrest/usertemplates/<templateobjectid>/usertemplatevideoserviceaccounts/<objectid> |
|---|

| 204 OK |
|---|

| DELETE: https://<connection-ip-address>/vmrest/usertemplates/<TemplateObjectid>/usertemplatevideoserviceaccounts/<ObjectId>
Accept: application/json
Content-type: application/json |
|---|

| 200 |
|---|

| Parameters | Operation | Data Type | Comment |
|---|---|---|---|
| ConnectorFactoryName | Read | String | Name Of The Video Service |
| MediaServerType | Read | Integer | Media Server Used For Video |
| ConnectorFactoryObjectId | Read | String | Objectid of Video service created |
| TemplateObjectId | Read | String | Objectid of Voice Mail User Template |
| TemplateVideoServicesObjectId | Read | String | Objectid of Video Service Template created |
| IsConnectorMapped | Read, Update | Boolean | Validate if the Video Service Account is
                                             					 connected to the Video service |