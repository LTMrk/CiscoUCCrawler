---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-call-handler-html-6d0fd8fb06
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m-call-handler.html
retrieved_at: 2026-08-17T03:49:33.292976+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Call Handler

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Call Handler

# Cisco Unity Connection Provisioning Interface (CUPI) API -- Call Handler

## Cisco Unity Connection Provisioning Interface (CUPI) API -- Call Handler APIs

### Call Handler APIs

Call handlers answer calls, greet callers with recorded prompts, provide callers with information and options, route calls,
                              and take messages. They are a basic component of Cisco Unity Connection. Your plan for call handlers can be simple, using
                              only the predefined call handlers, or you can create up to 40,000 new call handlers. You may want to use call handlers in
                              the following ways:

As an automated attendant---A call handler can be used in place of a human operator to answer and direct calls by playing
                              greetings and responding to key presses. The automated attendant can provide a menu of options. For example, "For Sales, press
                              1; for Service, press 2; for our business hours, press 3".

To offer prerecorded audio text---A call handler can be used to provide information that customers request frequently. For
                              example, "Our normal business hours are Monday through Friday, 8 a.m. to 5 p.m.", or to play a pre-recorded message that all
                              callers hear before they can interact with the system.

As a message recipient---A call handler can be used to take messages for the organization. For example, "All of our customer
                              service representatives are busy. Please state your name, phone number, and account number, and we will return your call as
                              soon as possible.".

To transfer calls---A call handler can be used to route callers to a user. For example, after hours, you could transfer calls
                              that come to a technical support call handler directly to the mobile phone of the person who is on call, or to another call
                              handler.

Administrator can use this API to create/update/delete/fetch the call handler. You can update various attributes of call handler
                              using this API.

#### Listing the Call Handlers

The following is an example of the GET request that fetch the list of call handlers:

```
GET https://<connection-server>/vmrest/handlers/callhandlers
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                    by you:

```
<Callhandlers total="2">
  <Callhandler>
    <URI>/vmrest/handlers/callhandlers/fc922cfc-6583-471b-b8ab-9971e02418f3</URI>
    <CreationTime>2013-01-02T15:42:48Z</CreationTime>
    <Language>1033</Language>
    <Undeletable>true</Undeletable>
    <VoiceName>9d168d20-303d-4019-b381-cd430e478540.wav</VoiceName>
    <VoiceFileURI>/vmrest/voicefiles/99cbec60-ef57-41a5-a0bd-
  5d1b79e6b7f7</VoiceFileURI>
    <VoiceNameURI>/vmrest/handlers/callhandlers/fc922cfc-6583-471b-b8ab-
  9971e02418f3/voicename</VoiceNameURI>
    <LocationObjectId>fa15de52-b98d-4de9-a868-ed02f957e38f</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/fa15de52-b98d-4de9-a868-
  ed02f957e38f</LocationURI>
    <EditMsg>true</EditMsg>
    <IsPrimary>false</IsPrimary>
    <OneKeyDelay>1500</OneKeyDelay>
    <ScheduleSetObjectId>2eee2b88-8e45-4b77-8b4c-f52aaa1e39e4</ScheduleSetObjectId>
    <ScheduleSetURI>/vmrest/schedulesets/2eee2b88-8e45-4b77-8b4c-
  f52aaa1e39e4</ScheduleSetURI>
    <SendUrgentMsg>0</SendUrgentMsg>
    <MaxMsgLen>300</MaxMsgLen>
    <IsTemplate>false</IsTemplate>
    <ObjectId>fc922cfc-6583-471b-b8ab-9971e02418f3</ObjectId>
    <TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
    <RecipientDistributionListObjectId>e93ca9db-8659-4e07-bee6-
  7af3f5c1a1db</RecipientDistributionListObjectId>
    <RecipientDistributionListURI>/vmrest/distributionlists/e93ca9db-8659-4e07-bee6-
  7af3f5c1a1db</RecipientDistributionListURI>
    <DisplayName>Opening Greeting</DisplayName>
    <AfterMessageAction>2</AfterMessageAction>
    <AfterMessageTargetConversation>PHGreeting</AfterMessageTargetConversation>
    <AfterMessageTargetHandlerObjectId>2f4b7240-f56a-4644-b22a-
  b1a346a5a9b2</AfterMessageTargetHandlerObjectId>
    <TimeZone>190</TimeZone>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <UseDefaultTimeZone>true</UseDefaultTimeZone>
    <MediaSwitchObjectId>2dcf1e57-80d6-43d3-b245-3693fe78397d</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/2dcf1e57-80d6-43d3-b245-
  3693fe78397d</PhoneSystemURI>
    <UseCallLanguage>true</UseCallLanguage>
    <SendSecureMsg>false</SendSecureMsg>
    <EnablePrependDigits>false</EnablePrependDigits>
    <DispatchDelivery>false</DispatchDelivery>
    <CallSearchSpaceObjectId>1736fdd9-b6f9-4a92-ad25-
  17d5b8228700</CallSearchSpaceObjectId>
    <CallSearchSpaceURI>/vmrest/searchspaces/1736fdd9-b6f9-4a92-ad25-
  17d5b8228700</CallSearchSpaceURI>
    <InheritSearchSpaceFromCall>true</InheritSearchSpaceFromCall>
    <PartitionObjectId>0017febb-15bf-4454-9a5c-3b26e19aa14a</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/0017febb-15bf-4454-9a5c-3b26e19aa14a</PartitionURI>
    <PlayPostGreetingRecording>0</PlayPostGreetingRecording>
    <SendPrivateMsg>0</SendPrivateMsg>
    <PlayAfterMessage>1</PlayAfterMessage>
    <GreetingsURI>/vmrest/handlers/callhandlers/fc922cfc-6583-471b-b8ab-
  9971e02418f3/greetings</GreetingsURI>
    <TransferOptionsURI>/vmrest/handlers/callhandlers/fc922cfc-6583-471b-b8ab-
  9971e02418f3/transferoptions</TransferOptionsURI>
    <MenuEntriesURI>/vmrest/handlers/callhandlers/fc922cfc-6583-471b-b8ab-
  9971e02418f3/menuentries</MenuEntriesURI>
    <CallHandlerOwnerURI>/vmrest/handlers/callhandlers/fc922cfc-6583-471b-b8ab-
  9971e02418f3/callhandlerowners</CallHandlerOwnerURI>
  </Callhandler>
  <Callhandler>
    <URI>/vmrest/handlers/callhandlers/2f4b7240-f56a-4644-b22a-b1a346a5a9b2</URI>
    <CreationTime>2013-01-02T15:42:49Z</CreationTime>
    <Language>1033</Language>
    <Undeletable>true</Undeletable>
    <VoiceName>a797edef-e693-400f-bb7c-8fe889c3d758.wav</VoiceName>
    <VoiceFileURI>/vmrest/voicefiles/9a1a20ca-acb3-4ddc-9cde-
  0d10a2921427</VoiceFileURI>
    <VoiceNameURI>/vmrest/handlers/callhandlers/2f4b7240-f56a-4644-b22a-
  b1a346a5a9b2/voicename</VoiceNameURI>
    <LocationObjectId>fa15de52-b98d-4de9-a868-ed02f957e38f</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/fa15de52-b98d-4de9-a868-
  ed02f957e38f</LocationURI>
    <EditMsg>true</EditMsg>
    <IsPrimary>false</IsPrimary>
    <OneKeyDelay>1500</OneKeyDelay>
    <ScheduleSetObjectId>1cd28472-ced0-44ce-a8f7-cd7692ce7594</ScheduleSetObjectId>
    <ScheduleSetURI>/vmrest/schedulesets/1cd28472-ced0-44ce-a8f7-
  cd7692ce7594</ScheduleSetURI>
    <SendUrgentMsg>0</SendUrgentMsg>
    <MaxMsgLen>300</MaxMsgLen>
    <IsTemplate>false</IsTemplate>
    <ObjectId>2f4b7240-f56a-4644-b22a-b1a346a5a9b2</ObjectId>
    <RecipientDistributionListObjectId>e93ca9db-8659-4e07-bee6-
  7af3f5c1a1db</RecipientDistributionListObjectId>
    <RecipientDistributionListURI>/vmrest/distributionlists/e93ca9db-8659-4e07-bee6-
  7af3f5c1a1db</RecipientDistributionListURI>
    <DisplayName>Goodbye</DisplayName>
    <AfterMessageAction>1</AfterMessageAction>
    <TimeZone>190</TimeZone>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <UseDefaultTimeZone>true</UseDefaultTimeZone>
    <MediaSwitchObjectId>2dcf1e57-80d6-43d3-b245-
  3693fe78397d</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/2dcf1e57-80d6-43d3-b245-
  3693fe78397d</PhoneSystemURI>
    <UseCallLanguage>true</UseCallLanguage>
    <SendSecureMsg>false</SendSecureMsg>
    <EnablePrependDigits>false</EnablePrependDigits>
    <DispatchDelivery>false</DispatchDelivery>
    <CallSearchSpaceObjectId>1736fdd9-b6f9-4a92-ad25-
  17d5b8228700</CallSearchSpaceObjectId>
    <CallSearchSpaceURI>/vmrest/searchspaces/1736fdd9-b6f9-4a92-ad25-
  17d5b8228700</CallSearchSpaceURI>
    <InheritSearchSpaceFromCall>true</InheritSearchSpaceFromCall>
    <PartitionObjectId>0017febb-15bf-4454-9a5c-3b26e19aa14a</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/0017febb-15bf-4454-9a5c-3b26e19aa14a</PartitionURI>
    <PlayPostGreetingRecording>0</PlayPostGreetingRecording>
    <SendPrivateMsg>0</SendPrivateMsg>
    <PlayAfterMessage>1</PlayAfterMessage>
    <GreetingsURI>/vmrest/handlers/callhandlers/2f4b7240-f56a-4644-b22a-
  b1a346a5a9b2/greetings</GreetingsURI>
    <TransferOptionsURI>/vmrest/handlers/callhandlers/2f4b7240-f56a-4644-b22a-
  b1a346a5a9b2/transferoptions</TransferOptionsURI>
    <MenuEntriesURI>/vmrest/handlers/callhandlers/2f4b7240-f56a-4644-b22a-
  b1a346a5a9b2/menuentries</MenuEntriesURI>
    <CallHandlerOwnerURI>/vmrest/handlers/callhandlers/2f4b7240-f56a-4644-b22a-
  b1a346a5a9b2/callhandlerowners</CallHandlerOwnerURI>
  </Callhandler>
</Callhandlers>
```

```
Response Code: 200
```

JSON Example

To list of the call handlers, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/handlers/callhandlers
Accept: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                    by you:

```
{
  "@total": "2",
  "Callhandler": [
  {
    "URI": "/vmrest/handlers/callhandlers/6702cce8-853f-4cbd-8579-35c595213898",
    "CreationTime": "2013-02-14T05:05:43Z",
    "Language": "1033",
    "Undeletable": "true",
    "VoiceName": "43145be7-0101-4ba1-9448-76834baa153f.wav",
    "VoiceFileURI": "/vmrest/voicefiles/2374c796-b006-4b29-a35e-8b0b1d576e50",
    "VoiceNameURI": "/vmrest/handlers/callhandlers/6702cce8-853f-4cbd-8579-
  35c595213898/voicename",
    "LocationObjectId": "bbf3e6ed-0278-479c-9a6e-2da8756eeb6f",
    "LocationURI": "/vmrest/locations/connectionlocations/bbf3e6ed-0278-479c-9a6e-
  2da8756eeb6f",
    "EditMsg": "true",
    "IsPrimary": "false",
    "OneKeyDelay": "1500",
    "ScheduleSetObjectId": "96e43ab7-b6c1-49b1-ba27-008b8f8870e4",
    "ScheduleSetURI": "/vmrest/schedulesets/96e43ab7-b6c1-49b1-ba27-008b8f8870e4",
    "SendUrgentMsg": "0",
    "MaxMsgLen": "300",
    "IsTemplate": "false",
    "ObjectId": "6702cce8-853f-4cbd-8579-35c595213898",
    "TenantObjectId": "fe6541fb-b42c-44f2-8404-ded14cbf7438",
    "RecipientDistributionListObjectId": "24865f76-fa95-412d-bc56-a48ef9e1531a",
    "RecipientDistributionListURI": "/vmrest/distributionlists/24865f76-fa95-412d-bc56-
  a48ef9e1531a",
    "DisplayName": "Opening Greeting",
    "AfterMessageAction": "2",
    "AfterMessageTargetConversation": "PHGreeting",
    "AfterMessageTargetHandlerObjectId": "8c400830-7e92-4908-9ca6-a4b123f1bd19",
    "TimeZone": "190",
    "UseDefaultLanguage": "true",
    "UseDefaultTimeZone": "true",
    "MediaSwitchObjectId": "a984674b-98d1-442e-83a9-2dcc0824af9e",
    "PhoneSystemURI": "/vmrest/phonesystems/a984674b-98d1-442e-83a9-2dcc0824af9e",
    "UseCallLanguage": "true",
    "SendSecureMsg": "false",
    "EnablePrependDigits": "false",
    "DispatchDelivery": "false",
    "CallSearchSpaceObjectId": "5a07d332-6fc5-4a3f-baba-3cb4ea630280",
    "CallSearchSpaceURI": "/vmrest/searchspaces/5a07d332-6fc5-4a3f-baba-
  3cb4ea630280",
    "InheritSearchSpaceFromCall": "true",
    "PartitionObjectId": "d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b",
    "PartitionURI": "/vmrest/partitions/d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b",
    "PlayPostGreetingRecording": "0",
    "SendPrivateMsg": "0",
    "PlayAfterMessage": "1",
    "GreetingsURI": "/vmrest/handlers/callhandlers/6702cce8-853f-4cbd-8579-
  35c595213898/greetings",
    "TransferOptionsURI": "/vmrest/handlers/callhandlers/6702cce8-853f-4cbd-8579-
  35c595213898/transferoptions",
    "MenuEntriesURI": "/vmrest/handlers/callhandlers/6702cce8-853f-4cbd-8579-
  35c595213898/menuentries",
    "CallHandlerOwnerURI": "/vmrest/handlers/callhandlers/6702cce8-853f-4cbd-8579-
  35c595213898/callhandlerowners"
  }
  {
    "URI": "/vmrest/handlers/callhandlers/426e4f1c-0cf1-43dc-a52b-63db2c0704c5",
    "CreationTime": "2013-02-14T05:05:44Z",
    "Language": "1033",
    "Undeletable": "true",
    "VoiceName": "389d2d11-f74c-4df1-9766-098800b8fe74.wav",
    "VoiceFileURI": "/vmrest/voicefiles/c8cd8b94-8d2f-47d6-841e-ca1d3a02bdc2",
    "VoiceNameURI": "/vmrest/handlers/callhandlers/426e4f1c-0cf1-43dc-a52b-
    63db2c0704c5/voicename",
    "LocationObjectId": "bbf3e6ed-0278-479c-9a6e-2da8756eeb6f",
    "LocationURI": "/vmrest/locations/connectionlocations/bbf3e6ed-0278-479c-9a6e-
    2da8756eeb6f",
    "EditMsg": "true",
    "IsPrimary": "false",
    "OneKeyDelay": "1500",
    "ScheduleSetObjectId": "96e43ab7-b6c1-49b1-ba27-008b8f8870e4",
    "ScheduleSetURI": "/vmrest/schedulesets/96e43ab7-b6c1-49b1-ba27-008b8f8870e4",
    "SendUrgentMsg": "0",
    "MaxMsgLen": "300",
    "IsTemplate": "false",
    "ObjectId": "426e4f1c-0cf1-43dc-a52b-63db2c0704c5",
    "RecipientSubscriberObjectId": "053afdf6-78e8-4a54-9384-e6c32c68dacd",
    "RecipientUserURI": "/vmrest/users/053afdf6-78e8-4a54-9384-e6c32c68dacd",
    "DisplayName": "Operator",
    "AfterMessageAction": "2",
    "AfterMessageTargetConversation": "PHGreeting",
    "AfterMessageTargetHandlerObjectId": "8c400830-7e92-4908-9ca6-a4b123f1bd19",
    "DtmfAccessId": "0",
    "TimeZone": "190",
    "UseDefaultLanguage": "true",
    "UseDefaultTimeZone": "true",
    "MediaSwitchObjectId": "a984674b-98d1-442e-83a9-2dcc0824af9e",
    "PhoneSystemURI": "/vmrest/phonesystems/a984674b-98d1-442e-83a9-2dcc0824af9e",
    "UseCallLanguage": "true",
    "SendSecureMsg": "false",
    "EnablePrependDigits": "false",
    "DispatchDelivery": "false",
    "CallSearchSpaceObjectId": "5a07d332-6fc5-4a3f-baba-3cb4ea630280",
    "CallSearchSpaceURI": "/vmrest/searchspaces/5a07d332-6fc5-4a3f-baba-
    3cb4ea630280",
    "InheritSearchSpaceFromCall": "true",
    "PartitionObjectId": "d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b",
    "PartitionURI": "/vmrest/partitions/d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b",
    "PlayPostGreetingRecording": "0",
    "SendPrivateMsg": "0",
    "PlayAfterMessage": "1",
    "GreetingsURI": "/vmrest/handlers/callhandlers/426e4f1c-0cf1-43dc-a52b-
    63db2c0704c5/greetings",
    "TransferOptionsURI": "/vmrest/handlers/callhandlers/426e4f1c-0cf1-43dc-a52b-
    63db2c0704c5/transferoptions",
    "MenuEntriesURI": "/vmrest/handlers/callhandlers/426e4f1c-0cf1-43dc-a52b-
    63db2c0704c5/menuentries",
    "CallHandlerOwnerURI": "/vmrest/handlers/callhandlers/426e4f1c-0cf1-43dc-a52b-
    63db2c0704c5/callhandlerowners"
  }
  ]
}
```

```
Response Code: 200
```

#### Listing Specific Tenant Related Call Handlers by System Administrator

In Cisco Unity Connection 10.5(2) and later, the system administrator can use TenantObjectID to list the specific tenant related
                                    call handlers using the following URI:

```
GET https://<connection-server>/vmrest/handlers/callhandlers?query=(TenantObjectId is <Tenant-ObjectId>)
```

To get the TenantObjectID, use the following URI:

```
GET https://<connection-server>/vmrest/tenants
```

#### Viewing the Specific Call Handler

The following is an example of the GET request that lists the details of specific call handler represented by the provided
                                    value of call handler ID:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                    by you:

```
<Callhandler>
    <URI>/vmrest/handlers/callhandlers/4afc0de6-c52c-42e4-99bb-6359bd518f11</URI>
    <CreationTime>2012-12-14T09:32:50Z</CreationTime>
    <Language>1033</Language>
    <Undeletable>false</Undeletable>
    <VoiceName>a6b5b738-6aa3-467e-a1c9-2061e9f078b2.wav</VoiceName>
    <VoiceFileURI>/vmrest/voicefiles/009caa53-375b-4c84-b287-2d593550b185</VoiceFileURI>
    <VoiceNameURI>/vmrest/handlers/callhandlers/4afc0de6-c52c-42e4-99bb-
  6359bd518f11/voicename</VoiceNameURI>
    <LocationObjectId>36342486-2f03-4dee-9f92-e0324f25e31c</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/36342486-2f03-4dee-9f92-
  e0324f25e31c</LocationURI>
    <EditMsg>true</EditMsg>
    <IsPrimary>false</IsPrimary>
    <OneKeyDelay>1500</OneKeyDelay>
    <ScheduleSetObjectId>fc3d37bd-eb5e-4425-9820-bd913f77683b</ScheduleSetObjectId>
    <ScheduleSetURI>/vmrest/schedulesets/fc3d37bd-eb5e-4425-9820-
  bd913f77683b</ScheduleSetURI>
    <SendUrgentMsg>0</SendUrgentMsg>
    <MaxMsgLen>300</MaxMsgLen>
    <IsTemplate>false</IsTemplate>
    <ObjectId>4afc0de6-c52c-42e4-99bb-6359bd518f11</ObjectId>
    <RecipientSubscriberObjectId>0a082dcd-9f31-4897-b819-
  dedff7e67484</RecipientSubscriberObjectId>
    <RecipientUserURI>/vmrest/users/0a082dcd-9f31-4897-b819-
  dedff7e67484</RecipientUserURI>
    <DisplayName>test</DisplayName>
    <AfterMessageAction>2</AfterMessageAction>
    <AfterMessageTargetConversation>SystemTransfer</AfterMessageTargetConversation>
    <DtmfAccessId>2345</DtmfAccessId>
    <TimeZone>190</TimeZone>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <UseDefaultTimeZone>true</UseDefaultTimeZone>
    <MediaSwitchObjectId>7a04d1f8-e71f-431b-a86c-1bb84da153e6</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/7a04d1f8-e71f-431b-a86c-
  1bb84da153e6</PhoneSystemURI>
    <UseCallLanguage>false</UseCallLanguage>
    <SendSecureMsg>true</SendSecureMsg>
    <EnablePrependDigits>false</EnablePrependDigits>
    <DispatchDelivery>false</DispatchDelivery>
    <CallSearchSpaceObjectId>d4885446-a1f9-4e4c-810f-168bcc8489af</CallSearchSpaceObjectId>
    <CallSearchSpaceURI>/vmrest/searchspaces/d4885446-a1f9-4e4c-810f-
  168bcc8489af</CallSearchSpaceURI>
    <InheritSearchSpaceFromCall>true</InheritSearchSpaceFromCall>
    <PartitionObjectId>a7108db5-c354-4b71-a72f-2c945291bda2</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/a7108db5-c354-4b71-a72f-2c945291bda2</PartitionURI>
    <PlayPostGreetingRecording>2</PlayPostGreetingRecording>
    <PostGreetingRecordingObjectId>1b13cab3-8ae8-4b39-a9e8-
  51464dc5216d</PostGreetingRecordingObjectId>
    <SendPrivateMsg>2</SendPrivateMsg>
    <PlayAfterMessage>1</PlayAfterMessage>
    <GreetingsURI>/vmrest/handlers/callhandlers/4afc0de6-c52c-42e4-99bb-
  6359bd518f11/greetings</GreetingsURI>
    <TransferOptionsURI>/vmrest/handlers/callhandlers/4afc0de6-c52c-42e4-99bb-
  6359bd518f11/transferoptions</TransferOptionsURI>
    <MenuEntriesURI>/vmrest/handlers/callhandlers/4afc0de6-c52c-42e4-99bb-
  6359bd518f11/menuentries</MenuEntriesURI>
    <CallHandlerOwnerURI>/vmrest/handlers/callhandlers/4afc0de6-c52c-42e4-99bb-
  6359bd518f11/callhandlerowners</CallHandlerOwnerURI>
  </Callhandler>
```

```
Response Code:200
```

JSON Example

To view a specific call handler, do the following:

```
Request URI:
GET https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>
Accept: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                    by you:

```
{
    "URI": "/vmrest/handlers/callhandlers/8c400830-7e92-4908-9ca6-a4b123f1bd19",
    "CreationTime": "2013-02-14T05:05:44Z",
    "Language": "1033",
    "Undeletable": "true",
    "VoiceName": "a05d6040-1494-49eb-94bf-b9019eb79813.wav",
    "VoiceFileURI": "/vmrest/voicefiles/e90706a2-d264-4104-abdf-f8e146799588",
    "VoiceNameURI": "/vmrest/handlers/callhandlers/8c400830-7e92-4908-9ca6-
    a4b123f1bd19/voicename",
    "LocationObjectId": "bbf3e6ed-0278-479c-9a6e-2da8756eeb6f",
    "LocationURI": "/vmrest/locations/connectionlocations/bbf3e6ed-0278-479c-9a6e-
    2da8756eeb6f",
    "EditMsg": "true",
    "IsPrimary": "false",
    "OneKeyDelay": "1500",
    "ScheduleSetObjectId": "74205ca1-1f58-466b-a543-13ad7bd4798e",
    "ScheduleSetURI": "/vmrest/schedulesets/74205ca1-1f58-466b-a543-13ad7bd4798e",
    "SendUrgentMsg": "0",
    "MaxMsgLen": "300",
    "IsTemplate": "false",
    "ObjectId": "8c400830-7e92-4908-9ca6-a4b123f1bd19",
    "RecipientDistributionListObjectId": "24865f76-fa95-412d-bc56-a48ef9e1531a",
    "RecipientDistributionListURI": "/vmrest/distributionlists/24865f76-fa95-412d-bc56-
    a48ef9e1531a",
    "DisplayName": "Goodbye",
    "AfterMessageAction": "1",
    "TimeZone": "190",
    "UseDefaultLanguage": "true",
    "UseDefaultTimeZone": "true",
    "MediaSwitchObjectId": "a984674b-98d1-442e-83a9-2dcc0824af9e",
    "PhoneSystemURI": "/vmrest/phonesystems/a984674b-98d1-442e-83a9-2dcc0824af9e",
    "UseCallLanguage": "true",
    "SendSecureMsg": "false",
    "EnablePrependDigits": "false",
    "DispatchDelivery": "false",
    "CallSearchSpaceObjectId": "5a07d332-6fc5-4a3f-baba-3cb4ea630280",
    "CallSearchSpaceURI": "/vmrest/searchspaces/5a07d332-6fc5-4a3f-baba-3cb4ea630280",
    "InheritSearchSpaceFromCall": "true",
    "PartitionObjectId": "d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b",
    "PartitionURI": "/vmrest/partitions/d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b",
    "PlayPostGreetingRecording": "0",
    "SendPrivateMsg": "0",
    "PlayAfterMessage": "1",
    "GreetingsURI": "/vmrest/handlers/callhandlers/8c400830-7e92-4908-9ca6-
    a4b123f1bd19/greetings",
    "TransferOptionsURI": "/vmrest/handlers/callhandlers/8c400830-7e92-4908-9ca6-
    a4b123f1bd19/transferoptions",
    "MenuEntriesURI": "/vmrest/handlers/callhandlers/8c400830-7e92-4908-9ca6-
    a4b123f1bd19/menuentries",
    "CallHandlerOwnerURI": "/vmrest/handlers/callhandlers/8c400830-7e92-4908-9ca6-
    a4b123f1bd19/callhandlerowners"
}
```

```
Response Code:200
```

#### Creating a Call Handler

The following is an example of the POST request that creates a new call handler:

```
POST https://<connection-server>/vmrest/handlers/callhandlers?templateObjectId=<callHandlerTemplate-ObjectId>
Request Body:
<pre>
<CallHandler>
    <DisplayName>Taxoma_Test</DisplayName>
</CallHandler>
```

The following is the response from the above *POST* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 201
/vmrest/handlers/callhandlers/8c400830-7e92-4908-9ca6-a4b123f1bd19
```

JSON Example

To create a new call handler, do the following:

```
POST https://<connection-server>/vmrest/handlers/callhandlers?templateObjectId=<callHandlerTemplate-ObjectId>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "DisplayName": "Texoma1"
}
```

The following is the response from the above *POST* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 201
/vmrest/handlers/callhandlers/8c400830-7e92-4908-9ca6-a4b123f1bd19
```

#### Delete the Call Handler

The following is an example of the DELETE request that can be used to delete a call handler:

```
DELETE https://<connection-server>/vmrest/callhandlers/<callhandler-objectid>
```

The following is the response from the above *DELETE* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

JSON Example

To delete a call handler, do the following:

```
DELETE https://<connection-server>/vmrest/callhandlers/<callhandler-objectid>
Accept: application/json
Connection: keep_alive
```

The following is the response from the above *DELETE* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

#### Assigning a Schedule Set to a Call Handler

The following is an example of the PUT request that can be used to assign a schedule set to a call handler:

```
PUT https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>
Request Body:
<Callhandler>
    <ScheduleSetObjectId>9dd6c1d5-249e-4715-8953-396ce2f26314</ScheduleSetObjectId>
</Callhandler>
```

```
Response Code: 204
```

JSON Example

To assign a schedule to a call handler, do the following:

```
PUT https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "ScheduleSetObjectId": "74205ca1-1f58-466b-a543-13ad7bd4798e"
}
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

#### Specify Message Recipient for a Call Handler

The following is an example of the PUT request that can be used to specify message recipient for a call handler:

```
PUT https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>
Request Body:
  <Callhandler>
    <RecipientSubscriberObjectId>3c700079-33bb-4897-b1a5-
  23cf19194ecf</RecipientSubscriberObjectId>
  </Callhandler>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

JSON Example

To specify message recipient for a call handler, do the following:

```
PUT https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "RecipientSubscriberObjectId": "571412d0-6330-433d-8a1f-7f7cb102a09f"
}
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

#### Caller Input Keys

http://docwiki.cisco.com/wiki/Cisco_Unity_Connection_Provisioning_Interface_%28CUPI%29_API_--_Caller_Input_Keys

#### Updating Caller Input Keys

http://docwiki.cisco.com/wiki/Cisco_Unity_Connection_Provisioning_Interface_%28CUPI%29_API_--_Updating_Caller_Input_Keys

#### Update the Language of Call Handler

To fetch the language code, use the following URI:

```
GET https://<connection-server>/vmrest/languagemap
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

#### Updating Time Zone of Call Handler

This PUT request can be used to update time zone for a call handler template. It can be set to default or particular time
                                    zone. To know time zones installed on the server, you can use the following URI:

```
GET https://<connection-server>/vmrest/timezones
```

For updating time zone of a call handler, the mandatory fields are:

UseDefaultTimeZone

TimeZone

```
PUT https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>
Request Body:
<Callhandler>
    <UseDefaultTimeZone>false</UseDefaultTimeZone>
    <TimeZone>190</TimeZone>
</Callhandler>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                    by you:

```
Response Code: 204
```

#### Explanation of Data Fields

Parameter

Operations

Data Type

Comments

URI

Read Only

String

Call Handler URI

AfterMessageAction

Read/Write

Integer

Specifies the after message action. Refer to the section Enumeration Type.

AfterMessageTargetConversation

Read/Write

String

The name of the conversation to which the caller is routed. Refer to the section Enumeration Type

AfterMessageTargetHandlerObjectId

Read/Write

String

The Unique Identifier of the call action object that Cisco Unity Connection performs after taking a message.

CallSearchSpaceObjectId

Read/Write

String

The unique identifier of the SearchSpace that is used limit visibility to dialable objects when searching by extension (dial
                                                string).

CallSearchSpaceURI

Read Only

String

URL for search spaces.

CreationTime

Read Only

datetime

Specifies the creation date and time of the call handler. Format: YYYY-MM-DDThh:mm:ssZ . The default value is the current
                                                system date and time.

DispatchDelivery

Read/Write

Boolean

A flag indicating that all messages left for the call handler is for dispatch delivery.

Possible values:

false: specifies no dispatch delivery.

true: specifies dispatch delivery.

Default value: false

DisplayName

Read/Write

String

Name of the call handler.

DtmfAccessId

Read/Write

String

Extension of the call handler.

EditMsg

Read/Write

Boolean

A flag that determines whether the caller can edit messages.

Possible values:

false : Callers cannot edit messages

true : Callers can edit messages

Default value: true.

EnablePrependDigits

Read/Write

Boolean

Specifies if Prepend Digits to Dialed Extensions is enabled.

Possible values:

false:- System will not prepend digits when dialing the transfer extension

true:- System will prepend digits when dialing the transfer extension

Default value: false

InheritSearchSpaceFromCall

Read/Write

Boolean

Specifies if the search space is to be inherited from the call.

Possible values:

true – Inherit from call.

false – Do not inherit from call

Default value: true

IsPrimary

Read Only

Boolean

A flag indicating whether this is a "primary" call handler for a subscriber, or an "application" call handler.

Note:- Each subscriber is associated with a call handler, which is referred to as the "primary call handler" for that subscriber.
                                                An "application call handler" is just a normal call handler. Possible values:

false: Not a primary call handler

true: Primary call handler

Default value: false.

IsTemplate

Read Only

Boolean

A flag indicating whether this CallHandler is a "template" for creating new call handlers. It is used to provide default values
                                                for selected columns when creating new call handlers.

Possible values:

false: Not a template

true: Is a template

Default value: false

Language

Read/Write

Integer

LocationObjectId

Read Only

String

LocationURI

Read Only

String

Specifies the URI of locations

The maximum recording length (in seconds) for messages left by unidentified callers. This value is used when the call handler
                                                is set to an action of "Take Message" (either by an after greeting action in the messagingrule table or via a user input action
                                                in the menuentry table.

This value only gets applied to unidentified callers leaving a message. This value is not used for subscriber-subscriber messaging.
                                                Instead the COS for the calling subscriber determines the maximum recorded message length. The range of this field can vary
                                                from 1-3600. Default value: 300

MaxMsgLen

Read/Write

Integer

Specifies the object Id of the Phone System the call handler belongs to.

MediaSwitchObjectId

Read/Write

String

Specifies the URI of Phone Systems.

PhoneSystemURI

Read Only

String

Specifies an object ID of the call handler.

ObjectId

Read Only

String

The unique identifier of the tenant to which the call handler belongs. This field is reflected in the response only if the
                                                call handler belongs to a particular tenant.

TenantOjectId

Read Only

String

The amount of time (in milliseconds) that Cisco Unity Connection waits for additional input after callers press a single key
                                                that is not locked. If there is no input within this time, Cisco Unity Connection performs the action assigned to the single
                                                key.

When a caller interrupts a greeting with a digit, Cisco Unity Connection will wait this number of milliseconds to see if they
                                                are going to enter more digits. Once this timeout is reached (or the caller terminates the input with a #), Cisco Unity Connection
                                                will do a look-up of the resulting string of numbers for a match with a DTMFAccessID value in the dialing domain. If a match
                                                is found, the call is sent to the matching object. If no match is found, the "Error greeting" for the call handler is invoked.
                                                If a key is "locked" then this value does not apply. Instead action is taken immediately on that key instead of allowing more
                                                digits. A value of 0 disables one key input .The range of this field can vary from 1 to 10000. Default value: 1500

OneKeyDelay

Read/Write

Integer

Specifies the object Id of the partition the Call Handler belongs to.

PartitionObjectId

Read/Write

String

PartitionURI

Read Only

String

Specifies what should be played after the message. Refer to the section Enumeration Type.

PlayAfterMessage

Read/Write

Integer

Specifies an object ID of the recoding.

PlayAfterMessageRecordingObjectId

Read/Write

String

Indicates whether the recording referenced by PostGreetingRecordingObjectId should be played.

Possible values:

0 : No

1 : Always

2 : External

Default value: 0

PlayPostGreetingRecording

Read/Write

Integer

Specifies the object Id of the Post Greeting recording.

PostGreetingRecordingObjectId

Read/Write

String

URI of the Post Greeting Recording

PostGreetingURI

Read Only

String

Specifies the touchtone digits to be prepended to extension when dialing transfer number ( #, 0,1...9,*). Digits, plus, hash
                                                and asterisk only are allowed

PrependDigits

Read/Write

String

Specifies an object ID of the distribution list that is the message recipient.

RecipientDistributionListObjectId

Read/Write

String

Object ID of a User with a mailbox that is the message recipient.

RecipientDistributaionListURI

Read Only

String

Object ID of the schedule set assigned to the Call Handler.

ScheduleSetObjectId

Read/Write

String

Specifies the URI of schedule sets.

ScheduleSetURI

Read/Write

String

Determines if an outside caller can mark their message as private.

Possible values:

0 : Never

1 : Always

2 : Ask

Default value: 0

SendPrivateMsg

Read/Write

Integer

A flag indicating whether an unidentified caller can mark a message as "secure."

Default value: false

SendSecureMsg

Read/Write

Boolean

A flag indicating whether an unidentified caller can mark a message as "urgent."

Possible values:

0 : Never

1 : Always

2 : Ask

Default value: 0(Never)

SendUrgentMsg

Read/Write

Integer

Used when the UseDefaultTimezone is set to false.

To know the Integer Time Zone codes for the Time Zones installed on the server following URI can be used: https://<connection-server>/vmrest/timezones.
                                                Example: 190 is the code for (GMT+05:30) Asia/Kolkata

TimeZone

Read/Write

Integer

A flag indicating whether Cisco Unity Connection will use the language assigned to the call.

Possible Values:

true

false

Default value: true

UseCallLanguage

Read/Write

Boolean

A flag that is dependent on the value of the Language field. If Language is set to Null, UseDefaultLanguage is set to true.
                                                If any language is specified, UseDefaultLanguage is set to false.

Possible Values:

true

false

UseDefaultLanguage

Read/Write

Boolean

A flag indicating whether Cisco Unity Connection will use the system default Time Zone.

Possible Values:

true

false

Default value: false

UseDefaultTimeZone

Read/Write

Boolean

URI of the call handler owner API.

CallHandlerOwnerURI

Read Only

String

The name of the WAV file containing the recorded audio (voice name, greeting, etc.) for the parent object.

It is displayed once a voice-name is recorded.

VoiceName

Read Only

String

It is displayed once a voice-name is recorded.

VoiceFileURI

Read Only

String

Specifies the URI of greetings

GreetingsURI

Read Only

String

Specifies the URI of transfer options.

TransferOptionsURI

Read Only

String

Specifies the URI of menu entries

MenuEntriesURI

Read Only

String

Specifies the URI of menu entries

ViceNameURI

Read Only

String

URI for voice name once it is recorded.

## Cisco Unity Connection Provisioning Interface (CUPI) API -- Call Handler Owner APIs

### Add a Call Handler Owner

The following is an example of the *POST* request that can be used to create a new call handler owner.

Note: The RoleObjectId is no longer required for assigning Call Handler owners.

1. To assign a user as call handler owner

```
POST https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/callhandlerowners
Request Body:
<CallhandlerOwner>
            <UserObjectId>c0430be2-52b8-46d7-8fad-c6aa13781469</UserObjectId>
</CallhandlerOwner>
```

Here, UserObjectId can be fetched from

```
GET https://<connection-server>/vmrest/users
```

2. To assign a distribution list as call handler owner

```
POST https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/callhandlerowners
Request Body:
<CallhandlerOwner>
            <DistributionListObjectId>b6616b6f-c0e0-4462-b64a-654b0f5baa65</DistributionListObjectId>
</CallhandlerOwner>
```

Here, DistributionListObjectId can be fetched from

```
GET https://<connection-server>/vmrest/distributionlists
```

The following is the response from the above *POST* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 201
/vmrest/handlers/callhandlers/c0430be2-52b8-46d7-8fad-c6aa13781469
```

JSON Example

1. To assign a user as a call handler owner, do the following:

```
POST https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/callhandlerowners
Accept: application/json
Content_type: application/json
Connection: keep_alive
```

The following is the response from the above *POST* request and the actual response will depend upon the information given
                                 by you:

```
{
    "UserObjectId": "5aeb75a4-14c2-474d-bec9-90aa731ee4cc",
}
```

```
Response Code: 201
/vmrest/handlers/callhandlers/c0430be2-52b8-46d7-8fad-c6aa13781469
```

2. To assign a distribution list as a call handler owner, do the following:

```
POST https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/callhandlerowners
Accept: application/json
Content_type: application/json
Connection: keep_alive
```

The following is the response from the above *POST* request and the actual response will depend upon the information given
                                 by you:

```
{
    "DistributionListObjectId": "5aeb75a4-14c2-474d-bec9-90aa731ee4cc",
}
```

```
Response Code: 201
/vmrest/handlers/callhandlers/c0430be2-52b8-46d7-8fad-c6aa13781469
```

### View the Call Handler Owners

The following is an example of the Get request that can be used to fetch the call handler owners:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/callhandlerowners
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                 by you:

```
<CallhandlerOwners total="2">
   <CallhandlerOwner>
      <URI>/vmrest/handlers/callhandlers/f3b4cc1f-c2d7-4c67-9f53-7095d4b2a928/callhandlerowners/3aee209f-948b-450a-9d0f-75e2c1d4992f</URI>
      <DistributionListObjectId>b6616b6f-c0e0-4462-b64a-654b0f5baa65</DistributionListObjectId>
      <DistributionListURI>/vmrest/distributionlists/b6616b6f-c0e0-4462-b64a-654b0f5baa65</DistributionListURI>
      <ObjectId>3aee209f-948b-450a-9d0f-75e2c1d4992f</ObjectId>
      <TargetHandlerObjectId>f3b4cc1f-c2d7-4c67-9f53-7095d4b2a928</TargetHandlerObjectId>
   </CallhandlerOwner>
   <CallhandlerOwner>
      <URI>/vmrest/handlers/callhandlers/f3b4cc1f-c2d7-4c67-9f53-7095d4b2a928/callhandlerowners/75587df3-5be4-4e21-83b3-9ec7e4f60874</URI>
      <ObjectId>75587df3-5be4-4e21-83b3-9ec7e4f60874</ObjectId>
      <TargetHandlerObjectId>f3b4cc1f-c2d7-4c67-9f53-7095d4b2a928</TargetHandlerObjectId>
      <UserObjectId>ecdc6d2d-19e5-4adf-ac7d-6e351a5c95c4</UserObjectId>
      <UserURI>/vmrest/users/ecdc6d2d-19e5-4adf-ac7d-6e351a5c95c4</UserURI>
   </CallhandlerOwner>
</CallhandlerOwners>
```

```
Response Code: 200
```

JSON Example

To view the list of call handler owners, do the following:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/callhandlerowners
Accept: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                 by you:

```
{
    "@total": "2",
    "CallhandlerOwner": {
    "URI": "/vmrest/handlers/callhandlers/b2d3d56a-f0c2-4839-98c5-
    48770690244a/callhandlerowners/ac6dda36-798d-4eea-9055-db5a31eb5599",
    "ObjectId": "75587df3-5be4-4e21-83b3-9ec7e4f60874",
    "UserObjectId": "5aeb75a4-14c2-474d-bec9-90aa731ee4cc",
    "UserURI": "/vmrest/users/5aeb75a4-14c2-474d-bec9-90aa731ee4cc",
    "TargetHandlerObjectId": "b2d3d56a-f0c2-4839-98c5-48770690244a"
    }
    "CallhandlerOwner": {
    "URI": "/vmrest/handlers/callhandlers/b2d3d56a-f0c2-4839-98c5-
    48770690244a/callhandlerowners/ac6dda36-798d-4eea-9055-db5a31eb5599",
    "ObjectId": "3aee209f-948b-450a-9d0f-75e2c1d4992f",
    "DistributionListObjectId": "b6616b6f-c0e0-4462-b64a-654b0f5baa65",
    "DistributionListURI": "/vmrest/users/b6616b6f-c0e0-4462-b64a-654b0f5baa65",
    "TargetHandlerObjectId": "b2d3d56a-f0c2-4839-98c5-48770690244a"
    }   
}
```

```
Response Code: 200
```

### View the Details of Specific Call Handler Owner

The following is an example of the Get request that can be used to fetch the specific call handler owner details:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/callhandlerowners/<callHandlerowner-objectid>
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                 by you

1. For a user as a call handler owner:

```
<CallhandlerOwner>
    <URI>/vmrest/handlers/callhandlers/4afc0de6-c52c-42e4-99bb-
  6359bd518f11/callhandlerowners/a6731eca-ba31-4cee-a367-0bd6f45c633f</URI>
    <ObjectId>a6731eca-ba31-4cee-a367-0bd6f45c633f</ObjectId>
    <UserObjectId>eaacd744-6fe1-4085-8b25-10c702fdfd20</UserObjectId>
    <UserURI>/vmrest/users/eaacd744-6fe1-4085-8b25-10c702fdfd20</UserURI>
    <TargetHandlerObjectId>4afc0de6-c52c-42e4-99bb-6359bd518f11</TargetHandlerObjectId>
  </CallhandlerOwner>
```

```
Response Code:200
```

2. For a distribution list as a call handler owner:

```
<CallhandlerOwner>
    <URI>/vmrest/handlers/callhandlers/f3b4cc1f-c2d7-4c67-9f53-
  7095d4b2a928/callhandlerowners/4e35ed6c-6aed-42e4-9723-b859706ac749</URI>
    <DistributionListObjectId>988630fa-313a-4f0c-980f-f6dc78add3ca</DistributionListObjectId>
    <DistributionListURI>/vmrest/distributionlists/988630fa-313a-4f0c-980f-f6dc78add3ca</DistributionListURI>
    <ObjectId>4e35ed6c-6aed-42e4-9723-b859706ac749</ObjectId>
    <TargetHandlerObjectId>f3b4cc1f-c2d7-4c67-9f53-7095d4b2a928</TargetHandlerObjectId>
  </CallhandlerOwner>
```

```
Response Code:200
```

JSON Example

To view a specific call handler owner, do the following:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/callhandlerowners/<callhandlerowner-objectid>
Accept: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                 by you:

1. For a user as a call handler owner:

```
{
    "URI": "/vmrest/handlers/callhandlers/b2d3d56a-f0c2-4839-98c5-
    48770690244a/callhandlerowners/ac6dda36-798d-4eea-9055-db5a31eb5599",
    "ObjectId": "ac6dda36-798d-4eea-9055-db5a31eb5599",
    "UserObjectId": "5aeb75a4-14c2-474d-bec9-90aa731ee4cc",
    "UserURI": "/vmrest/users/5aeb75a4-14c2-474d-bec9-90aa731ee4cc",
    "TargetHandlerObjectId": "b2d3d56a-f0c2-4839-98c5-48770690244a"
}
```

```
Response Code:200
```

2. For a distribution list as a call handler owner:

```
{
    "URI": "/vmrest/handlers/callhandlers/b2d3d56a-f0c2-4839-98c5-
    48770690244a/callhandlerowners/ac6dda36-798d-4eea-9055-db5a31eb5599",
    "ObjectId": "4e35ed6c-6aed-42e4-9723-b859706ac749",
    "DistributionListObjectId": "988630fa-313a-4f0c-980f-f6dc78add3ca",
    "DistributionListURI": "/vmrest/users/988630fa-313a-4f0c-980f-f6dc78add3ca",
    "TargetHandlerObjectId": "b2d3d56a-f0c2-4839-98c5-48770690244a"
}
```

```
Response Code:200
```

### Delete a Call Handler Owner

The following is an example of the DELETE request that can be used to delete a call handler owner:

```
DELETE https://<connection-server>/vmrest/callhandlers/<callhandlerId>/callhandlerowners/<callhandlerowner-objectid>
```

The following is the response from the above *DELETE* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 204
```

JSON Example

To delete a call handler owner, do the following:

```
DELETE https://<connection-server>/vmrest/callhandlers/<callhandler-objectid>/callhandlerowners/<callhandlerowner-objectid>
Accept: application/json
Connection: keep_alive
```

The following is the response from the above *DELETE* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 204
```

### Explanation of Data Fields

Parameter

Operation

Data Type

Comments

ObejectId

Read Only

String

Specifies an object ID to uniquely identify a call handler owner.

UserObjectId

Read/Write

String

Specifies an object ID of the user who owns the call handler.

VmsObjectId

Read Only

String

Specifies an unique identifier of the LocationVMS object.

DistributionListObjectId

Read Write

String

Specifies an object ID of the distribution list who owns the call handler.

TragetHandlerObjectId

Read Only

String

Specifies an object ID of the call handler to which the call handler owner object belongs.

UserURI

Read Only

String

Specifies URI to get details of the user who owns the Call Handler.

DistributionListURI

Read Only

String

Specifies URI to get details of the distribution list who owns the Call Handler Owner

## Cisco Unity Connection Provisioning Interface (CUPI) API -- Call Handler Enumeration Types

### Call Action

### Play After Message
                           	 Recording

### AfterMessageTargetConversation

### Greeting
                           	 Type

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- Call Handler Greetings
                        	 APIs

### Call Handler
                           	 Greetings APIs

Administrator can use this API to
                                 		  fetch the greetings. It can be used to fetch the list of greetings and also a
                                 		  single instance of greetings.

### Listing the
                           	 Greetings

The following is an example of
                                 		  the GET request that fetch the list of greetings:

```
GET https://<connection-server>/vmrest/callhandlertemplates/<callhandler-objectid>/greetings
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<Greetings total="7"><Greeting> 
    <URI>/vmrest/handlers/callhandlers/fa468470-1031-4896-ab11-3736bdee3b00/greetings/Alternate</URI> 
    <CallHandlerObjectId>fa468470-1031-4896-ab11-3736bdee3b00</CallHandlerObjectId> 
    <CallhandlerURI>/vmrest/handlers/callhandlers/fa468470-1031-4896-ab11-3736bdee3b00</CallhandlerURI> 
    <IgnoreDigits>false</IgnoreDigits> 
    <PlayWhat>0</PlayWhat> 
    <RepromptDelay>2</RepromptDelay> 
    <Reprompts>0</Reprompts> 
    <TimeExpires>1972-01-01 05:30:00.0</TimeExpires> 
    <GreetingType>Alternate</GreetingType> 
    <AfterGreetingAction>4</AfterGreetingAction> 
    <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt> 
    <EnableTransfer>false</EnableTransfer>
    <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
    <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt> 
    <GreetingStreamFilesURI>/vmrest/handlers/callhandlers/fa468470-1031-4896-ab11-3736bdee3b00/greetings/Alternate/greetingstreamfiles</GreetingStreamFilesURI> 
    <Enabled>false</Enabled> 
</Greeting>
```

```
Response Code: 200
```

JSON Example

To view the list of greetings, do the following:

```
GET https://<connection-server>/vmrest/callhandler/<callhandler-objectid>/greetings
Accept: appliaction/json
Conenction: keep_alive
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
{ 
   "@total":"7" 
   "Greeting": [
  { 
    "URI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a/greetings/Alternate",
    "CallHandlerObjectId":"a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a",
    "CallhandlerURI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a",
    "IgnoreDigits":"false",
    "PlayWhat":"0",
    "RepromptDelay":"2",
    "Reprompts":"0", 
    "TimeExpires":"1972-01-01 00:00:00.0",
    "GreetingType":"Alternate", 
    "AfterGreetingAction":"4",
    "PlayRecordMessagePrompt":"true" ,
    "EnableTransfer":"false",
    "EnablePersonalVideoRecording":"false",
    "PlayRecordVideoMessagePrompt":"false",
    "Enabled":"false"  
  }, 
  { 
    "URI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a/greetings/Busy", 
    "CallHandlerObjectId":"a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a", 
    "CallhandlerURI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a",   
    "IgnoreDigits":"false", 
    "PlayWhat":"0", 
    "RepromptDelay":"2", 
    "Reprompts":"0", 
    "TimeExpires":"1972-01-01 00:00:00.0", 
    "GreetingType":"Busy", 
    "AfterGreetingAction":"4",
    "PlayRecordMessagePrompt":"true", 
    "EnableTransfer":"false",
    "EnablePersonalVideoRecording":"false",
    "PlayRecordVideoMessagePrompt":"false",
    "Enabled":"false"  
  }, 
] 
}
```

```
Response Code: 200
```

### Viewing the
                           	 Details of Specific Greeting

The following is an example of
                                 		  the GET request that lists the details of specific greeting:

```
GET https://<connection-server>/vmrest/callhandler/<callhandler-
  objectid>/greetings/<Greetingname>
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<Greeting> 
    <URI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-836910ac1a4c/greetings/Alternate</URI> 
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId> 
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-836910ac1a4c</CallhandlerURI> 
    <IgnoreDigits>false</IgnoreDigits> 
    <PlayWhat>0</PlayWhat> 
    <RepromptDelay>2</RepromptDelay> 
    <Reprompts>0</Reprompts> 
    <TimeExpires>1972-01-01 00:00:00.0</TimeExpires> 
    <GreetingType>Alternate</GreetingType> 
    <AfterGreetingAction>4</AfterGreetingAction> 
    <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt> 
    <EnableTransfer>false</EnableTransfer>
    <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
    <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt> 
    <Enabled>false</Enabled>  
</Greeting>
```

```
Response Code: 200
```

JSON Example

To view a specific greeting, do the following:

```
GET https://<connection-server>/vmrest/callhandler/<Callhandler-
objectid>/greetings/<Greetingname>
Accept: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
{ 
    "URI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a/greetings/Alternate", 
    "CallHandlerObjectId":"a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a", 
    "CallhandlerURI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a", 
    "IgnoreDigits":"false", 
    "PlayWhat":"0", 
    "RepromptDelay":"2", 
    "Reprompts":"0", 
    "TimeExpires":"1972-01-01 00:00:00.0", 
    "GreetingType":"Alternate", 
    "AfterGreetingAction":"4", 
    "PlayRecordMessagePrompt":"true" ,
    "EnableTransfer":"false", 
    "EnablePersonalVideoRecording":"false",
    "PlayRecordVideoMessagePrompt":"false",
    "Enabled":"false"  
}
```

```
Response Code: 200
```

### Updating a
                           	 Greeting

The following is an example of
                                 		  the GET request that updates the details of specific greeting:

```
PUT https://<connection-server>/vmrest/callhandler/<callhandler-objectid>/greetings/<Greetingname>
Request Body:
<Greeting>
    <PlayWhat>1</PlayWhat>
    <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt>
</Greeting>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update a particular greeting, do the following:

```
PUT https://<connection-server>/vmrest/callhandler/<Callhandler-objectid>/greetings/<Greetingname>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "PlayWhat":"1",
    "PlayRecordMessagePrompt":"true"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Using the CUTI to record greetings via the Phone

The following example demonstrates how to achieve this task.

Record the greeting using CUTI, the details are available at Using CUTI for Basic Call Operations .

The record operation in Step-1 returns XML/JSON output containing the details of the recorded file. Example output:

```
<CallControl>
 <op>RECORD</op>
 <resourceType>STREAM</resourceType>
 <resourceId>01a78559-07ec-4898-beb6-444a4ae9c569.wav</resourceId>
 <lastResult>0</lastResult>
 <speed>100</speed>
 <volume>100</volume>
 <startPosition>0</startPosition>
</CallControl>
```

Send the following PUT request with the body of request containing above XML/JSON output.

```
Request :
PUT https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-id>/greetings/Alternate/greetingstreamfiles/<language-code>/audio
Request Body :
<CallControl>
<op>RECORD</op>
<resourceType>STREAM</resourceType>
<resourceId>01a78559-07ec-4898-beb6-444a4ae9c569.wav</resourceId>
<lastResult>0</lastResult>
<speed>100</speed>
<volume>100</volume>
<startPosition>0</startPosition>
</CallControl>
```

```
Response Code: 204 No Content
```

The Put request will update the Greetings. The update of a Greetings wave file is similar whether a audio wave file is being
                              used or the audio is a CallControl XML/JSON schema.

### Enabling or
                           	 disabling the Greeting

#### Cisco Unity
                              	 Connection Provisioning Interface (CUPI) API -- Call Handler Greetings
                              	 APIs

#### Disabling the
                              	 Greeting

For this scenario the request
                                    		  body should contain the "Enabled" which should be set to false.

```
PUT https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/greetings/<Greetingname>
```

Request Body:

```
<Greeting>
  <Enabled>false</Enabled>
</Greeting>
```

```
Response Code : 204
```

JSON Example

```
{
  "Enabled":"false"
}
```

```
Response Code : 204
```

### Save Video
                           	 Greetings

Unity Connection allows you to
                                 		  save video greetings using both GET and PUT requests.

Example of GET Request

```
GET http://<connection-server>/vmrest/Callhandlersprimarytemplates/<callhandlerobjectid>/usertemplates/Greetings/<GreetingType>/GreetingStreamFiles/<language>/video
```

The following is the response of the above GET command and the output
                                 		  may vary depending on your inputs.

```
Response: 200
<CallControl>
    <resourceId>aad91d6d-aeca-4a72-8069-b656efb3041f.wav</resourceId>
    <sessionId>570146ed1504cb1</sessionId>
</CallControl
```

JSON Example

```
Request 
GET  vmrest/handlers/callhandlers/30600b21-1a4c-47a3-a078-8078984e5376/greetings/Standard/greetingstreamfiles/1033/video
Accept: application/json
User-Agent: Java/1.6.0_17
Host: <connection-server>
Connection: keep-alive
authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg=
```

```
Response
HTTP/1.1 200
Content-Type: application/json
Date: Fri, 15 Jan 2010 15:14:11 GMT
Server:
{ “resourceId” :” aad91d6d-aeca-4a72-8069-b656efb3041f.wav”, “sessionId” : ”570146ed1504cb1”}
```

Example of PUT Request

```
PUT http://<connection-server>/vmrest/Callhandlersprimarytemplates/<callhandlerobjectid>/usertemplates/Greetings/<GreetingType>/GreetingStreamFiles/<language>/video
```

```
<CallControl>
     <resourceId>aad91d6d-aeca-4a72-8069-b656efb3041f.wav</resourceId>
     <sessionId>570146ed1504cb1</sessionId>
</CallControl>
```

```
Response: 204 OK
```

JSON Example

```
Request 
PUT  vmrest/handlers/callhandlers/30600b21-1a4c-47a3-a078-8078984e5376/greetings/Standard/greetingstreamfiles/1033/video
Content-Type: application/json
Accept: application/json
Host: <connection-server>
Connection: keep-alive
authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==

{ “resourceId” :” aad91d6d-aeca-4a72-8069-b656efb3041f.wav”, “sessionId” : ”570146ed1504cb1”}
```

```
Response :
HTTP/1.1 204
Content-Type: application/json
Date: Fri, 15 Jan 2010 15:14:11 GMT
Server:
```

### Explanation of
                           	 Data Fields

This column overrides all the Menu Entry settings when this
                                                						greeting is active. This has the same effect as setting all the menu entry keys
                                                						for this handler to "locked". It is a shorthand way of locking callers into the
                                                						greeting so they cannot get out until it completes. Values can be:

- false: Caller
                                                      						  input enabled during greeting

- true: Caller
                                                      						  input ignored during greeting

Default Value: false

Default Value: 0 For more information, refer to the
                                                						Enumeration Type section.

Values can be:

- 0: Do wait
                                                      						  without receiving caller input and do not replay greeting.

- 1 or greater:
                                                      						  Wait this number of seconds without receiving any input from the caller before
                                                      						  playing the greeting again.

Default Value: 2

This column is typically used when an audio text application
                                                						is expecting input from a caller. The range of this field can vary from 0 to
                                                						100. Values can be:

- 0: Do not
                                                      						  re-prompt - Cisco Unity Connection will play the greeting once and then the
                                                      						  after-greeting action is taken.

- 1 or greater:
                                                      						  Number of times to re-prompt.

The "RepromptDelay" value determines how many seconds to
                                                						wait in between replays. Default Value: 0

The values that are allowed are:

- Hangup

- Goto

- Restart greeting

- Route from next
                                                      						  call routing rule

- Take message

- Custom Type:
                                                      						  Call Action

For more information, refer to the Enumeration Type section.

The "Enhanced Alternate Greeting" feature uses this column
                                                						to specify how long the subscriber wants their alternate greeting enabled. The
                                                						standard greeting rule should never be disabled. The field is not displayed
                                                						when the Greeting field is enabled with no end date and end time.

Values:

- true - Play
                                                      						  Record Message prompt is enabled.

- false - Play
                                                      						  Record prompt is disabled.

Default Value: true

Values:

- true: Allows
                                                      						  transfer

- false: Does not
                                                      						  allow

Default Value: false

A flag indicating whether the personal video recording of
                                                						the user will be used.

Values:

- true : Personal
                                                      						  Video Recording is enabled.

- false : Personal
                                                      						  Video Recording is not enabled.

Default value : false

Values:

- true : Callers
                                                      						  will be prompted with a tone before recording their video message.

- false : Callers
                                                      						  will not be prompted with a tone before recording their video message.

Default value : false

This flag is editable only when the flag
                                                						EnablePersonalVideoRecording is set to True.

## Cisco Unity
                        	 Connection Provisioning Interface (CUPI) API -- TransferRulesAPIs

### Listing the
                           	 Transfer Rules

To enable a transfer type and
                                 		  update the rule to transfer call to another extension, set the transfer type to
                                 		  supervise transfer and if the extension is busy, ask callers to hold. In
                                 		  addition, you can also set some call screening options.

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/transferoptions
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
<TransferOptions total="2"> 
  <TransferOption>
    <URI>/vmrest/handlers/callhandlers/166da38f-951b-4c9a-92da-
  87ed7993cfec/transferoptions/Standard</URI>
    <CallHandlerObjectId>166da38f-951b-4c9a-92da-
  87ed7993cfec</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/166da38f-951b-4c9a-92da-
  87ed7993cfec</CallhandlerURI>
    <TransferOptionType>Standard</TransferOptionType>
    <Action>0</Action>
    <Extension>0</Extension>
    <RnaAction>1</RnaAction>
    <TransferAnnounce>false</TransferAnnounce>
    <TransferConfirm>false</TransferConfirm>
    <TransferDtDetect>false</TransferDtDetect>
    <TransferHoldingMode>0</TransferHoldingMode>
    <TransferIntroduce>false</TransferIntroduce>
    <TransferRings>4</TransferRings>
    <TransferScreening>false</TransferScreening>
    <TransferType>0</TransferType>
    <MediaSwitchObjectId>cd10d831-28d3-40da-ab13-
  a87431b38682</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/cd10d831-28d3-40da-ab13-
  a87431b38682</PhoneSystemURI>
    <UsePrimaryExtension>false</UsePrimaryExtension>
    <PlayTransferPrompt>true</PlayTransferPrompt>
    <PersonalCallTransfer>false</PersonalCallTransfer>
    <Enabled>true</Enabled>
  </TransferOption>
</TransferOptions>
```

```
Response Code: 200
```

JSON Example

To enable transfer rule, do the following:

```
GET https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/transferoptions
Action: application/json
Connection: keep_alive
```

The following is the response from the above *GET* request and the
                                 		  actual response will depend upon the information given by you:

```
{   
  "@total": "2",  
  "TransferOption":    [           
    {         
    "URI": "/vmrest/handlers/callhandlers/166da38f-951b-4c9a-92da-
    87ed7993cfec/transferoptions/Alternate",         
    "CallHandlerObjectId": "166da38f-951b-4c9a-92da-87ed7993cfec", 
    "CallhandlerURI": "/vmrest/handlers/callhandlers/166da38f-951b-4c9a-92da-
    87ed7993cfec",         
    "TransferOptionType": "Alternate",         
    "Action": "0",         
    "Extension": "0",         
    "RnaAction": "1",         
    "TimeExpires": "1972-01-01 00:00:00.0",         
    "TransferAnnounce": "false",         
    "TransferConfirm": "false",        
    "TransferDtDetect": "false",        
    "TransferHoldingMode": "0",        
    "TransferIntroduce": "false",         
    "TransferRings": "4",         
    "TransferScreening": "false",        
    "TransferType": "0",        
    "MediaSwitchObjectId": "cd10d831-28d3-40da-ab13-a87431b38682",        
    "PhoneSystemURI": "/vmrest/phonesystems/cd10d831-28d3-40da-ab13-
    a87431b38682",         
    "UsePrimaryExtension": "true",        
    "PlayTransferPrompt": "true",         
    "PersonalCallTransfer": "false",         
    "Enabled": "false"      
    },           
    {         
    "URI": "/vmrest/callhandlerprimarytemplates/166da38f-951b-4c9a-92da-
    87ed7993cfec/transferoptions/Off%20Hours",         
    "CallHandlerObjectId": "166da38f-951b-4c9a-92da-87ed7993cfec",         
    "CallhandlerURI": "/vmrest/handlers/callhandlers/166da38f-951b-4c9a-92da-
    87ed7993cfec",         
    "TransferOptionType": "Off Hours",         
    "Action": "0",         
    "Extension": "0",         
    "RnaAction": "1",        
    "TransferAnnounce": "false",         
    "TransferConfirm": "false",         
    "TransferDtDetect": "false",        
    "TransferHoldingMode": "0",         
    "TransferIntroduce": "false",         
    "TransferRings": "4",         
    "TransferScreening": "false",         
    "TransferType": "0",         
    "MediaSwitchObjectId": "cd10d831-28d3-40da-ab13-a87431b38682",         
    "PhoneSystemURI": "/vmrest/phonesystems/cd10d831-28d3-40da-ab13-
    a87431b38682",        
    "UsePrimaryExtension": "true",         
    "PlayTransferPrompt": "true",        
    "PersonalCallTransfer": "false",         
    "Enabled": "true"      
    }          
  }
}
```

```
Response Code: 200
```

### Update a Transfer
                           	 Rule

We can do a PUT Operation to
                                 		  update a transfer rule.

```
Request URI:
PUT https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-
objectid>/transferoptions/Alternate 
Request Body:
<TransferOption>
    <Action>1</Action>
    <Extension>1000</Extension>
    <TimeExpires>2012-12-31 12:00:00.0</TimeExpires>
    <TransferAnnounce>true</TransferAnnounce>
    <TransferConfirm>true</TransferConfirm>
    <TransferIntroduce>true</TransferIntroduce>
    <TransferScreening>true</TransferScreening>
    <TransferType>1</TransferType>
    <Enabled>true</Enabled>
</TransferOption>
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update transfer rule, do the following:

```
PUT https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/transferoptions/Alternate
Action: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "Action": "1",
    "TimeExpires": "2012-12-31 12:00:00.0",
    "TransferAnnounce": "true",
    "TransferConfirm": "true", 
    "TransferIntroduce": "true",
    "TransferRings": "8",
    "TransferScreening": "true",
    "TransferType": "1",
    "Enabled": "true"
}
```

The following is the response from the above *PUT* request and the
                                 		  actual response will depend upon the information given by you:

```
Response Code: 204
```

### Explanation of
                           	 Data Fields

- Alternate - in
                                                      						  effect at all times, overrides standard and off hours.

- Off Hours - off
                                                      						  or closed hours based on specified schedule.

- Standard -
                                                      						  standard hours based on specified schedule.

Default value : 0

Default value: 1

The "Standard" transfer option should never be disabled. For
                                                						primary call handlers associated with the subscribers, the "Alternate" transfer
                                                						option should always be enabled since subscribers have only one transfer option
                                                						used currently.

Possible Values:

- false: Do not
                                                      						  say "Transferring call" when the subscriber answers the phone

- true: Say
                                                      						  "Transferring call" when the subscriber answers the phone

Default Value: false

- Unsupervised
                                                      						  transfer (also referred to as "Release to Switch" transfer) - Cisco Unity
                                                      						  Connection puts the caller on hold, dials the extension, and releases the call
                                                      						  to the phone system. When the line is busy or is not answered, the phone system
                                                      						  (not Cisco Unity Connection) forwards the call to the subscriber or handler
                                                      						  greeting. To use "Unsupervised" transfer, call forwarding must be enabled on
                                                      						  the phone system.

- Supervised
                                                      						  transfer - Cisco Unity Connection acts as a receptionist, handling the
                                                      						  transfer. If the line is busy or the call is not answered, Cisco Unity
                                                      						  Connection (not the phone system) forwards the call to the subscriber or
                                                      						  handler greeting. Supervised transfer can be used regardless if the phone
                                                      						  system forwards calls or not.

Typically, TransferConfirm is used in conjunction with the
                                                						call screening option ("TransferScreening" column) enabled. This combination
                                                						enables the subscriber to hear the name of the caller and then decide if they
                                                						want to take the call or not. Possible values:

- false: Transfer
                                                      						  confirm disabled

- true: Transfer
                                                      						  confirm enabled

Default Value: false

This is usually used for phone systems that do not have
                                                						"positive disconnect" capabilities to avoid sending terminated calls to the
                                                						operator console. Possible Values:

- false: Do not
                                                      						  check for dial tone prior to transferring a call

- true: Check for
                                                      						  dial tone prior to transferring a call

Default value: false.

Refer to the section Enumeration Type. Default Value is 0.

Requires a "TransferType" of supervised (1).This
                                                						functionality is normally used when a single extension number is being shared
                                                						by multiple subscribers or a scenario where the subscriber who is the message
                                                						recipient takes calls for more than one dialed extension. The introduction
                                                						alerts the subscriber who answers that the call is for the call handler.
                                                						Default value: false.

Requires a "TransferType" of supervised (1). The value of
                                                						this column should never be less than 2 for a supervised transfer. Possible
                                                						values: Range 2-20 Default Value: 4

Normally this column is used along with "TransferConfirm" to
                                                						allow the subscriber to screen calls. Possible Values:

- false: Call
                                                      						  screening disabled

- true: Ask and
                                                      						  record caller name

Default value: false.

- Unsupervised
                                                      						  transfer (also referred to as "Release to Switch" transfer) - Cisco Unity
                                                      						  Connection puts the caller on hold, dials the extension, and releases the call
                                                      						  to the phone system. When the line is busy or is not answered, the phone system
                                                      						  (not Cisco Unity Connection) forwards the call to the subscriber or handler
                                                      						  greeting. To use "Unsupervised" transfer, call forwarding must be enabled on
                                                      						  the phone system.

- Supervised
                                                      						  transfer - Cisco Unity Connection acts as a receptionist, handling the
                                                      						  transfer. If the line is busy or the call is not answered, Cisco Unity
                                                      						  Connection (not the phone system) forwards the call to the subscriber or
                                                      						  handler greeting. Supervised transfer can be used regardless if the phone
                                                      						  system forwards calls or not.

Refer to the section Enumeration Type. Default value: 0

Possible value:

- true

- false

Default value: true

Possible values:

- true - Play
                                                      						  Transfer prompt is enabled.

- false - Play
                                                      						  transfer prompt is disabled.

Default Value: true.

Possible Values:-

- false: Personal
                                                      						  Call Transfer Rules are not used.

- true:- Personal
                                                      						  Call Transfer Rules are used.

Default value: false

Possible Values:

- true: enabled

- false: disabled

Default Value: true

| <Callhandlers total="2">
  <Callhandler>
    <URI>/vmrest/handlers/callhandlers/fc922cfc-6583-471b-b8ab-9971e02418f3</URI>
    <CreationTime>2013-01-02T15:42:48Z</CreationTime>
    <Language>1033</Language>
    <Undeletable>true</Undeletable>
    <VoiceName>9d168d20-303d-4019-b381-cd430e478540.wav</VoiceName>
    <VoiceFileURI>/vmrest/voicefiles/99cbec60-ef57-41a5-a0bd-
  5d1b79e6b7f7</VoiceFileURI>
    <VoiceNameURI>/vmrest/handlers/callhandlers/fc922cfc-6583-471b-b8ab-
  9971e02418f3/voicename</VoiceNameURI>
    <LocationObjectId>fa15de52-b98d-4de9-a868-ed02f957e38f</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/fa15de52-b98d-4de9-a868-
  ed02f957e38f</LocationURI>
    <EditMsg>true</EditMsg>
    <IsPrimary>false</IsPrimary>
    <OneKeyDelay>1500</OneKeyDelay>
    <ScheduleSetObjectId>2eee2b88-8e45-4b77-8b4c-f52aaa1e39e4</ScheduleSetObjectId>
    <ScheduleSetURI>/vmrest/schedulesets/2eee2b88-8e45-4b77-8b4c-
  f52aaa1e39e4</ScheduleSetURI>
    <SendUrgentMsg>0</SendUrgentMsg>
    <MaxMsgLen>300</MaxMsgLen>
    <IsTemplate>false</IsTemplate>
    <ObjectId>fc922cfc-6583-471b-b8ab-9971e02418f3</ObjectId>
    <TenantObjectId>fe6541fb-b42c-44f2-8404-ded14cbf7438</TenantObjectId>
    <RecipientDistributionListObjectId>e93ca9db-8659-4e07-bee6-
  7af3f5c1a1db</RecipientDistributionListObjectId>
    <RecipientDistributionListURI>/vmrest/distributionlists/e93ca9db-8659-4e07-bee6-
  7af3f5c1a1db</RecipientDistributionListURI>
    <DisplayName>Opening Greeting</DisplayName>
    <AfterMessageAction>2</AfterMessageAction>
    <AfterMessageTargetConversation>PHGreeting</AfterMessageTargetConversation>
    <AfterMessageTargetHandlerObjectId>2f4b7240-f56a-4644-b22a-
  b1a346a5a9b2</AfterMessageTargetHandlerObjectId>
    <TimeZone>190</TimeZone>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <UseDefaultTimeZone>true</UseDefaultTimeZone>
    <MediaSwitchObjectId>2dcf1e57-80d6-43d3-b245-3693fe78397d</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/2dcf1e57-80d6-43d3-b245-
  3693fe78397d</PhoneSystemURI>
    <UseCallLanguage>true</UseCallLanguage>
    <SendSecureMsg>false</SendSecureMsg>
    <EnablePrependDigits>false</EnablePrependDigits>
    <DispatchDelivery>false</DispatchDelivery>
    <CallSearchSpaceObjectId>1736fdd9-b6f9-4a92-ad25-
  17d5b8228700</CallSearchSpaceObjectId>
    <CallSearchSpaceURI>/vmrest/searchspaces/1736fdd9-b6f9-4a92-ad25-
  17d5b8228700</CallSearchSpaceURI>
    <InheritSearchSpaceFromCall>true</InheritSearchSpaceFromCall>
    <PartitionObjectId>0017febb-15bf-4454-9a5c-3b26e19aa14a</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/0017febb-15bf-4454-9a5c-3b26e19aa14a</PartitionURI>
    <PlayPostGreetingRecording>0</PlayPostGreetingRecording>
    <SendPrivateMsg>0</SendPrivateMsg>
    <PlayAfterMessage>1</PlayAfterMessage>
    <GreetingsURI>/vmrest/handlers/callhandlers/fc922cfc-6583-471b-b8ab-
  9971e02418f3/greetings</GreetingsURI>
    <TransferOptionsURI>/vmrest/handlers/callhandlers/fc922cfc-6583-471b-b8ab-
  9971e02418f3/transferoptions</TransferOptionsURI>
    <MenuEntriesURI>/vmrest/handlers/callhandlers/fc922cfc-6583-471b-b8ab-
  9971e02418f3/menuentries</MenuEntriesURI>
    <CallHandlerOwnerURI>/vmrest/handlers/callhandlers/fc922cfc-6583-471b-b8ab-
  9971e02418f3/callhandlerowners</CallHandlerOwnerURI>
  </Callhandler>
  <Callhandler>
    <URI>/vmrest/handlers/callhandlers/2f4b7240-f56a-4644-b22a-b1a346a5a9b2</URI>
    <CreationTime>2013-01-02T15:42:49Z</CreationTime>
    <Language>1033</Language>
    <Undeletable>true</Undeletable>
    <VoiceName>a797edef-e693-400f-bb7c-8fe889c3d758.wav</VoiceName>
    <VoiceFileURI>/vmrest/voicefiles/9a1a20ca-acb3-4ddc-9cde-
  0d10a2921427</VoiceFileURI>
    <VoiceNameURI>/vmrest/handlers/callhandlers/2f4b7240-f56a-4644-b22a-
  b1a346a5a9b2/voicename</VoiceNameURI>
    <LocationObjectId>fa15de52-b98d-4de9-a868-ed02f957e38f</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/fa15de52-b98d-4de9-a868-
  ed02f957e38f</LocationURI>
    <EditMsg>true</EditMsg>
    <IsPrimary>false</IsPrimary>
    <OneKeyDelay>1500</OneKeyDelay>
    <ScheduleSetObjectId>1cd28472-ced0-44ce-a8f7-cd7692ce7594</ScheduleSetObjectId>
    <ScheduleSetURI>/vmrest/schedulesets/1cd28472-ced0-44ce-a8f7-
  cd7692ce7594</ScheduleSetURI>
    <SendUrgentMsg>0</SendUrgentMsg>
    <MaxMsgLen>300</MaxMsgLen>
    <IsTemplate>false</IsTemplate>
    <ObjectId>2f4b7240-f56a-4644-b22a-b1a346a5a9b2</ObjectId>
    <RecipientDistributionListObjectId>e93ca9db-8659-4e07-bee6-
  7af3f5c1a1db</RecipientDistributionListObjectId>
    <RecipientDistributionListURI>/vmrest/distributionlists/e93ca9db-8659-4e07-bee6-
  7af3f5c1a1db</RecipientDistributionListURI>
    <DisplayName>Goodbye</DisplayName>
    <AfterMessageAction>1</AfterMessageAction>
    <TimeZone>190</TimeZone>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <UseDefaultTimeZone>true</UseDefaultTimeZone>
    <MediaSwitchObjectId>2dcf1e57-80d6-43d3-b245-
  3693fe78397d</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/2dcf1e57-80d6-43d3-b245-
  3693fe78397d</PhoneSystemURI>
    <UseCallLanguage>true</UseCallLanguage>
    <SendSecureMsg>false</SendSecureMsg>
    <EnablePrependDigits>false</EnablePrependDigits>
    <DispatchDelivery>false</DispatchDelivery>
    <CallSearchSpaceObjectId>1736fdd9-b6f9-4a92-ad25-
  17d5b8228700</CallSearchSpaceObjectId>
    <CallSearchSpaceURI>/vmrest/searchspaces/1736fdd9-b6f9-4a92-ad25-
  17d5b8228700</CallSearchSpaceURI>
    <InheritSearchSpaceFromCall>true</InheritSearchSpaceFromCall>
    <PartitionObjectId>0017febb-15bf-4454-9a5c-3b26e19aa14a</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/0017febb-15bf-4454-9a5c-3b26e19aa14a</PartitionURI>
    <PlayPostGreetingRecording>0</PlayPostGreetingRecording>
    <SendPrivateMsg>0</SendPrivateMsg>
    <PlayAfterMessage>1</PlayAfterMessage>
    <GreetingsURI>/vmrest/handlers/callhandlers/2f4b7240-f56a-4644-b22a-
  b1a346a5a9b2/greetings</GreetingsURI>
    <TransferOptionsURI>/vmrest/handlers/callhandlers/2f4b7240-f56a-4644-b22a-
  b1a346a5a9b2/transferoptions</TransferOptionsURI>
    <MenuEntriesURI>/vmrest/handlers/callhandlers/2f4b7240-f56a-4644-b22a-
  b1a346a5a9b2/menuentries</MenuEntriesURI>
    <CallHandlerOwnerURI>/vmrest/handlers/callhandlers/2f4b7240-f56a-4644-b22a-
  b1a346a5a9b2/callhandlerowners</CallHandlerOwnerURI>
  </Callhandler>
</Callhandlers> |
|---|

| Response Code: 200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/handlers/callhandlers
Accept: application/json
Connection: keep_alive |
|---|

| {
  "@total": "2",
  "Callhandler": [
  {
    "URI": "/vmrest/handlers/callhandlers/6702cce8-853f-4cbd-8579-35c595213898",
    "CreationTime": "2013-02-14T05:05:43Z",
    "Language": "1033",
    "Undeletable": "true",
    "VoiceName": "43145be7-0101-4ba1-9448-76834baa153f.wav",
    "VoiceFileURI": "/vmrest/voicefiles/2374c796-b006-4b29-a35e-8b0b1d576e50",
    "VoiceNameURI": "/vmrest/handlers/callhandlers/6702cce8-853f-4cbd-8579-
  35c595213898/voicename",
    "LocationObjectId": "bbf3e6ed-0278-479c-9a6e-2da8756eeb6f",
    "LocationURI": "/vmrest/locations/connectionlocations/bbf3e6ed-0278-479c-9a6e-
  2da8756eeb6f",
    "EditMsg": "true",
    "IsPrimary": "false",
    "OneKeyDelay": "1500",
    "ScheduleSetObjectId": "96e43ab7-b6c1-49b1-ba27-008b8f8870e4",
    "ScheduleSetURI": "/vmrest/schedulesets/96e43ab7-b6c1-49b1-ba27-008b8f8870e4",
    "SendUrgentMsg": "0",
    "MaxMsgLen": "300",
    "IsTemplate": "false",
    "ObjectId": "6702cce8-853f-4cbd-8579-35c595213898",
    "TenantObjectId": "fe6541fb-b42c-44f2-8404-ded14cbf7438",
    "RecipientDistributionListObjectId": "24865f76-fa95-412d-bc56-a48ef9e1531a",
    "RecipientDistributionListURI": "/vmrest/distributionlists/24865f76-fa95-412d-bc56-
  a48ef9e1531a",
    "DisplayName": "Opening Greeting",
    "AfterMessageAction": "2",
    "AfterMessageTargetConversation": "PHGreeting",
    "AfterMessageTargetHandlerObjectId": "8c400830-7e92-4908-9ca6-a4b123f1bd19",
    "TimeZone": "190",
    "UseDefaultLanguage": "true",
    "UseDefaultTimeZone": "true",
    "MediaSwitchObjectId": "a984674b-98d1-442e-83a9-2dcc0824af9e",
    "PhoneSystemURI": "/vmrest/phonesystems/a984674b-98d1-442e-83a9-2dcc0824af9e",
    "UseCallLanguage": "true",
    "SendSecureMsg": "false",
    "EnablePrependDigits": "false",
    "DispatchDelivery": "false",
    "CallSearchSpaceObjectId": "5a07d332-6fc5-4a3f-baba-3cb4ea630280",
    "CallSearchSpaceURI": "/vmrest/searchspaces/5a07d332-6fc5-4a3f-baba-
  3cb4ea630280",
    "InheritSearchSpaceFromCall": "true",
    "PartitionObjectId": "d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b",
    "PartitionURI": "/vmrest/partitions/d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b",
    "PlayPostGreetingRecording": "0",
    "SendPrivateMsg": "0",
    "PlayAfterMessage": "1",
    "GreetingsURI": "/vmrest/handlers/callhandlers/6702cce8-853f-4cbd-8579-
  35c595213898/greetings",
    "TransferOptionsURI": "/vmrest/handlers/callhandlers/6702cce8-853f-4cbd-8579-
  35c595213898/transferoptions",
    "MenuEntriesURI": "/vmrest/handlers/callhandlers/6702cce8-853f-4cbd-8579-
  35c595213898/menuentries",
    "CallHandlerOwnerURI": "/vmrest/handlers/callhandlers/6702cce8-853f-4cbd-8579-
  35c595213898/callhandlerowners"
  }
  {
    "URI": "/vmrest/handlers/callhandlers/426e4f1c-0cf1-43dc-a52b-63db2c0704c5",
    "CreationTime": "2013-02-14T05:05:44Z",
    "Language": "1033",
    "Undeletable": "true",
    "VoiceName": "389d2d11-f74c-4df1-9766-098800b8fe74.wav",
    "VoiceFileURI": "/vmrest/voicefiles/c8cd8b94-8d2f-47d6-841e-ca1d3a02bdc2",
    "VoiceNameURI": "/vmrest/handlers/callhandlers/426e4f1c-0cf1-43dc-a52b-
    63db2c0704c5/voicename",
    "LocationObjectId": "bbf3e6ed-0278-479c-9a6e-2da8756eeb6f",
    "LocationURI": "/vmrest/locations/connectionlocations/bbf3e6ed-0278-479c-9a6e-
    2da8756eeb6f",
    "EditMsg": "true",
    "IsPrimary": "false",
    "OneKeyDelay": "1500",
    "ScheduleSetObjectId": "96e43ab7-b6c1-49b1-ba27-008b8f8870e4",
    "ScheduleSetURI": "/vmrest/schedulesets/96e43ab7-b6c1-49b1-ba27-008b8f8870e4",
    "SendUrgentMsg": "0",
    "MaxMsgLen": "300",
    "IsTemplate": "false",
    "ObjectId": "426e4f1c-0cf1-43dc-a52b-63db2c0704c5",
    "RecipientSubscriberObjectId": "053afdf6-78e8-4a54-9384-e6c32c68dacd",
    "RecipientUserURI": "/vmrest/users/053afdf6-78e8-4a54-9384-e6c32c68dacd",
    "DisplayName": "Operator",
    "AfterMessageAction": "2",
    "AfterMessageTargetConversation": "PHGreeting",
    "AfterMessageTargetHandlerObjectId": "8c400830-7e92-4908-9ca6-a4b123f1bd19",
    "DtmfAccessId": "0",
    "TimeZone": "190",
    "UseDefaultLanguage": "true",
    "UseDefaultTimeZone": "true",
    "MediaSwitchObjectId": "a984674b-98d1-442e-83a9-2dcc0824af9e",
    "PhoneSystemURI": "/vmrest/phonesystems/a984674b-98d1-442e-83a9-2dcc0824af9e",
    "UseCallLanguage": "true",
    "SendSecureMsg": "false",
    "EnablePrependDigits": "false",
    "DispatchDelivery": "false",
    "CallSearchSpaceObjectId": "5a07d332-6fc5-4a3f-baba-3cb4ea630280",
    "CallSearchSpaceURI": "/vmrest/searchspaces/5a07d332-6fc5-4a3f-baba-
    3cb4ea630280",
    "InheritSearchSpaceFromCall": "true",
    "PartitionObjectId": "d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b",
    "PartitionURI": "/vmrest/partitions/d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b",
    "PlayPostGreetingRecording": "0",
    "SendPrivateMsg": "0",
    "PlayAfterMessage": "1",
    "GreetingsURI": "/vmrest/handlers/callhandlers/426e4f1c-0cf1-43dc-a52b-
    63db2c0704c5/greetings",
    "TransferOptionsURI": "/vmrest/handlers/callhandlers/426e4f1c-0cf1-43dc-a52b-
    63db2c0704c5/transferoptions",
    "MenuEntriesURI": "/vmrest/handlers/callhandlers/426e4f1c-0cf1-43dc-a52b-
    63db2c0704c5/menuentries",
    "CallHandlerOwnerURI": "/vmrest/handlers/callhandlers/426e4f1c-0cf1-43dc-a52b-
    63db2c0704c5/callhandlerowners"
  }
  ]
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers?query=(TenantObjectId is <Tenant-ObjectId>) |
|---|

| GET https://<connection-server>/vmrest/tenants |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid> |
|---|

| <Callhandler>
    <URI>/vmrest/handlers/callhandlers/4afc0de6-c52c-42e4-99bb-6359bd518f11</URI>
    <CreationTime>2012-12-14T09:32:50Z</CreationTime>
    <Language>1033</Language>
    <Undeletable>false</Undeletable>
    <VoiceName>a6b5b738-6aa3-467e-a1c9-2061e9f078b2.wav</VoiceName>
    <VoiceFileURI>/vmrest/voicefiles/009caa53-375b-4c84-b287-2d593550b185</VoiceFileURI>
    <VoiceNameURI>/vmrest/handlers/callhandlers/4afc0de6-c52c-42e4-99bb-
  6359bd518f11/voicename</VoiceNameURI>
    <LocationObjectId>36342486-2f03-4dee-9f92-e0324f25e31c</LocationObjectId>
    <LocationURI>/vmrest/locations/connectionlocations/36342486-2f03-4dee-9f92-
  e0324f25e31c</LocationURI>
    <EditMsg>true</EditMsg>
    <IsPrimary>false</IsPrimary>
    <OneKeyDelay>1500</OneKeyDelay>
    <ScheduleSetObjectId>fc3d37bd-eb5e-4425-9820-bd913f77683b</ScheduleSetObjectId>
    <ScheduleSetURI>/vmrest/schedulesets/fc3d37bd-eb5e-4425-9820-
  bd913f77683b</ScheduleSetURI>
    <SendUrgentMsg>0</SendUrgentMsg>
    <MaxMsgLen>300</MaxMsgLen>
    <IsTemplate>false</IsTemplate>
    <ObjectId>4afc0de6-c52c-42e4-99bb-6359bd518f11</ObjectId>
    <RecipientSubscriberObjectId>0a082dcd-9f31-4897-b819-
  dedff7e67484</RecipientSubscriberObjectId>
    <RecipientUserURI>/vmrest/users/0a082dcd-9f31-4897-b819-
  dedff7e67484</RecipientUserURI>
    <DisplayName>test</DisplayName>
    <AfterMessageAction>2</AfterMessageAction>
    <AfterMessageTargetConversation>SystemTransfer</AfterMessageTargetConversation>
    <DtmfAccessId>2345</DtmfAccessId>
    <TimeZone>190</TimeZone>
    <UseDefaultLanguage>true</UseDefaultLanguage>
    <UseDefaultTimeZone>true</UseDefaultTimeZone>
    <MediaSwitchObjectId>7a04d1f8-e71f-431b-a86c-1bb84da153e6</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/7a04d1f8-e71f-431b-a86c-
  1bb84da153e6</PhoneSystemURI>
    <UseCallLanguage>false</UseCallLanguage>
    <SendSecureMsg>true</SendSecureMsg>
    <EnablePrependDigits>false</EnablePrependDigits>
    <DispatchDelivery>false</DispatchDelivery>
    <CallSearchSpaceObjectId>d4885446-a1f9-4e4c-810f-168bcc8489af</CallSearchSpaceObjectId>
    <CallSearchSpaceURI>/vmrest/searchspaces/d4885446-a1f9-4e4c-810f-
  168bcc8489af</CallSearchSpaceURI>
    <InheritSearchSpaceFromCall>true</InheritSearchSpaceFromCall>
    <PartitionObjectId>a7108db5-c354-4b71-a72f-2c945291bda2</PartitionObjectId>
    <PartitionURI>/vmrest/partitions/a7108db5-c354-4b71-a72f-2c945291bda2</PartitionURI>
    <PlayPostGreetingRecording>2</PlayPostGreetingRecording>
    <PostGreetingRecordingObjectId>1b13cab3-8ae8-4b39-a9e8-
  51464dc5216d</PostGreetingRecordingObjectId>
    <SendPrivateMsg>2</SendPrivateMsg>
    <PlayAfterMessage>1</PlayAfterMessage>
    <GreetingsURI>/vmrest/handlers/callhandlers/4afc0de6-c52c-42e4-99bb-
  6359bd518f11/greetings</GreetingsURI>
    <TransferOptionsURI>/vmrest/handlers/callhandlers/4afc0de6-c52c-42e4-99bb-
  6359bd518f11/transferoptions</TransferOptionsURI>
    <MenuEntriesURI>/vmrest/handlers/callhandlers/4afc0de6-c52c-42e4-99bb-
  6359bd518f11/menuentries</MenuEntriesURI>
    <CallHandlerOwnerURI>/vmrest/handlers/callhandlers/4afc0de6-c52c-42e4-99bb-
  6359bd518f11/callhandlerowners</CallHandlerOwnerURI>
  </Callhandler> |
|---|

| Response Code:200 |
|---|

| Request URI:
GET https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>
Accept: application/json
Connection: keep_alive |
|---|

| {
    "URI": "/vmrest/handlers/callhandlers/8c400830-7e92-4908-9ca6-a4b123f1bd19",
    "CreationTime": "2013-02-14T05:05:44Z",
    "Language": "1033",
    "Undeletable": "true",
    "VoiceName": "a05d6040-1494-49eb-94bf-b9019eb79813.wav",
    "VoiceFileURI": "/vmrest/voicefiles/e90706a2-d264-4104-abdf-f8e146799588",
    "VoiceNameURI": "/vmrest/handlers/callhandlers/8c400830-7e92-4908-9ca6-
    a4b123f1bd19/voicename",
    "LocationObjectId": "bbf3e6ed-0278-479c-9a6e-2da8756eeb6f",
    "LocationURI": "/vmrest/locations/connectionlocations/bbf3e6ed-0278-479c-9a6e-
    2da8756eeb6f",
    "EditMsg": "true",
    "IsPrimary": "false",
    "OneKeyDelay": "1500",
    "ScheduleSetObjectId": "74205ca1-1f58-466b-a543-13ad7bd4798e",
    "ScheduleSetURI": "/vmrest/schedulesets/74205ca1-1f58-466b-a543-13ad7bd4798e",
    "SendUrgentMsg": "0",
    "MaxMsgLen": "300",
    "IsTemplate": "false",
    "ObjectId": "8c400830-7e92-4908-9ca6-a4b123f1bd19",
    "RecipientDistributionListObjectId": "24865f76-fa95-412d-bc56-a48ef9e1531a",
    "RecipientDistributionListURI": "/vmrest/distributionlists/24865f76-fa95-412d-bc56-
    a48ef9e1531a",
    "DisplayName": "Goodbye",
    "AfterMessageAction": "1",
    "TimeZone": "190",
    "UseDefaultLanguage": "true",
    "UseDefaultTimeZone": "true",
    "MediaSwitchObjectId": "a984674b-98d1-442e-83a9-2dcc0824af9e",
    "PhoneSystemURI": "/vmrest/phonesystems/a984674b-98d1-442e-83a9-2dcc0824af9e",
    "UseCallLanguage": "true",
    "SendSecureMsg": "false",
    "EnablePrependDigits": "false",
    "DispatchDelivery": "false",
    "CallSearchSpaceObjectId": "5a07d332-6fc5-4a3f-baba-3cb4ea630280",
    "CallSearchSpaceURI": "/vmrest/searchspaces/5a07d332-6fc5-4a3f-baba-3cb4ea630280",
    "InheritSearchSpaceFromCall": "true",
    "PartitionObjectId": "d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b",
    "PartitionURI": "/vmrest/partitions/d50e9d0b-656e-416d-b5b7-43c4d2e2fd0b",
    "PlayPostGreetingRecording": "0",
    "SendPrivateMsg": "0",
    "PlayAfterMessage": "1",
    "GreetingsURI": "/vmrest/handlers/callhandlers/8c400830-7e92-4908-9ca6-
    a4b123f1bd19/greetings",
    "TransferOptionsURI": "/vmrest/handlers/callhandlers/8c400830-7e92-4908-9ca6-
    a4b123f1bd19/transferoptions",
    "MenuEntriesURI": "/vmrest/handlers/callhandlers/8c400830-7e92-4908-9ca6-
    a4b123f1bd19/menuentries",
    "CallHandlerOwnerURI": "/vmrest/handlers/callhandlers/8c400830-7e92-4908-9ca6-
    a4b123f1bd19/callhandlerowners"
} |
|---|

| Response Code:200 |
|---|

| POST https://<connection-server>/vmrest/handlers/callhandlers?templateObjectId=<callHandlerTemplate-ObjectId>
Request Body:
<pre>
<CallHandler>
    <DisplayName>Taxoma_Test</DisplayName>
</CallHandler> |
|---|

| Response Code: 201
/vmrest/handlers/callhandlers/8c400830-7e92-4908-9ca6-a4b123f1bd19 |
|---|

| POST https://<connection-server>/vmrest/handlers/callhandlers?templateObjectId=<callHandlerTemplate-ObjectId>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "DisplayName": "Texoma1"
} |
|---|

| Response Code: 201
/vmrest/handlers/callhandlers/8c400830-7e92-4908-9ca6-a4b123f1bd19 |
|---|

| Note | Make sure that while creating a Call Handler, do not provide the recipient object Id in the request body. By default, Call
                                             handler is created with undeliverable messages distribution list as the recipient. You can update the recipient object id
                                             using PUT API. |
|---|---|

| DELETE https://<connection-server>/vmrest/callhandlers/<callhandler-objectid> |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/callhandlers/<callhandler-objectid>
Accept: application/json
Connection: keep_alive |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>
Request Body:
<Callhandler>
    <ScheduleSetObjectId>9dd6c1d5-249e-4715-8953-396ce2f26314</ScheduleSetObjectId>
</Callhandler> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "ScheduleSetObjectId": "74205ca1-1f58-466b-a543-13ad7bd4798e"
} |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>
Request Body:
  <Callhandler>
    <RecipientSubscriberObjectId>3c700079-33bb-4897-b1a5-
  23cf19194ecf</RecipientSubscriberObjectId>
  </Callhandler> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "RecipientSubscriberObjectId": "571412d0-6330-433d-8a1f-7f7cb102a09f"
} |
|---|

| Response Code: 204 |
|---|

| GET https://<connection-server>/vmrest/languagemap |
|---|

| UseCallLanguage | UseDefaultLanguage | Language | Description |
|---|---|---|---|
| false | true | Null/Language Code | This will select the default language. |
| true | true/false | Null/Language Code | This will inherit the language from user. |
| false | false | Language Code | This will select the particular language as per the code. |

| GET https://<connection-server>/vmrest/timezones |
|---|

| PUT https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>
Request Body:
<Callhandler>
    <UseDefaultTimeZone>false</UseDefaultTimeZone>
    <TimeZone>190</TimeZone>
</Callhandler> |
|---|

| Response Code: 204 |
|---|

| Parameter | Operations | Data Type | Comments |
|---|---|---|---|
| URI | Read Only | String | Call Handler URI |
| AfterMessageAction | Read/Write | Integer | Specifies the after message action. Refer to the section Enumeration Type. |
| AfterMessageTargetConversation | Read/Write | String | The name of the conversation to which the caller is routed. Refer to the section Enumeration Type |
| AfterMessageTargetHandlerObjectId | Read/Write | String | The Unique Identifier of the call action object that Cisco Unity Connection performs after taking a message. |
| CallSearchSpaceObjectId | Read/Write | String | The unique identifier of the SearchSpace that is used limit visibility to dialable objects when searching by extension (dial
                                                string). |
| CallSearchSpaceURI | Read Only | String | URL for search spaces. |
| CreationTime | Read Only | datetime | Specifies the creation date and time of the call handler. Format: YYYY-MM-DDThh:mm:ssZ . The default value is the current
                                                system date and time. |
| DispatchDelivery | Read/Write | Boolean | A flag indicating that all messages left for the call handler is for dispatch delivery. Possible values: false: specifies no dispatch delivery. true: specifies dispatch delivery. Default value: false |
| DisplayName | Read/Write | String | Name of the call handler. |
| DtmfAccessId | Read/Write | String | Extension of the call handler. |
| EditMsg | Read/Write | Boolean | A flag that determines whether the caller can edit messages. Possible values: false : Callers cannot edit messages true : Callers can edit messages Default value: true. |
| EnablePrependDigits | Read/Write | Boolean | Specifies if Prepend Digits to Dialed Extensions is enabled. Possible values: false:- System will not prepend digits when dialing the transfer extension true:- System will prepend digits when dialing the transfer extension Default value: false |
| InheritSearchSpaceFromCall | Read/Write | Boolean | Specifies if the search space is to be inherited from the call. Possible values: true – Inherit from call. false – Do not inherit from call Default value: true |
| IsPrimary | Read Only | Boolean | A flag indicating whether this is a "primary" call handler for a subscriber, or an "application" call handler. Note:- Each subscriber is associated with a call handler, which is referred to as the "primary call handler" for that subscriber.
                                                An "application call handler" is just a normal call handler. Possible values: false: Not a primary call handler true: Primary call handler Default value: false. |
| IsTemplate | Read Only | Boolean | A flag indicating whether this CallHandler is a "template" for creating new call handlers. It is used to provide default values
                                                for selected columns when creating new call handlers. Possible values: false: Not a template true: Is a template Default value: false |
| Language | Read/Write | Integer | The Windows Locale ID (LCID) which identifies the language that Cisco Unity Connection plays the handler system prompts. |
| LocationObjectId | Read Only | String | The unique identifier of the Location object to which this handler belongs |
| LocationURI | Read Only | String | Specifies the URI of locations The maximum recording length (in seconds) for messages left by unidentified callers. This value is used when the call handler
                                                is set to an action of "Take Message" (either by an after greeting action in the messagingrule table or via a user input action
                                                in the menuentry table. This value only gets applied to unidentified callers leaving a message. This value is not used for subscriber-subscriber messaging.
                                                Instead the COS for the calling subscriber determines the maximum recorded message length. The range of this field can vary
                                                from 1-3600. Default value: 300 |
| MaxMsgLen | Read/Write | Integer | Specifies the object Id of the Phone System the call handler belongs to. |
| MediaSwitchObjectId | Read/Write | String | Specifies the URI of Phone Systems. |
| PhoneSystemURI | Read Only | String | Specifies an object ID of the call handler. |
| ObjectId | Read Only | String | The unique identifier of the tenant to which the call handler belongs. This field is reflected in the response only if the
                                                call handler belongs to a particular tenant. |
| TenantOjectId | Read Only | String | The amount of time (in milliseconds) that Cisco Unity Connection waits for additional input after callers press a single key
                                                that is not locked. If there is no input within this time, Cisco Unity Connection performs the action assigned to the single
                                                key. When a caller interrupts a greeting with a digit, Cisco Unity Connection will wait this number of milliseconds to see if they
                                                are going to enter more digits. Once this timeout is reached (or the caller terminates the input with a #), Cisco Unity Connection
                                                will do a look-up of the resulting string of numbers for a match with a DTMFAccessID value in the dialing domain. If a match
                                                is found, the call is sent to the matching object. If no match is found, the "Error greeting" for the call handler is invoked.
                                                If a key is "locked" then this value does not apply. Instead action is taken immediately on that key instead of allowing more
                                                digits. A value of 0 disables one key input .The range of this field can vary from 1 to 10000. Default value: 1500 |
| OneKeyDelay | Read/Write | Integer | Specifies the object Id of the partition the Call Handler belongs to. |
| PartitionObjectId | Read/Write | String | Specifies the URI of partitions. |
| PartitionURI | Read Only | String | Specifies what should be played after the message. Refer to the section Enumeration Type. |
| PlayAfterMessage | Read/Write | Integer | Specifies an object ID of the recoding. |
| PlayAfterMessageRecordingObjectId | Read/Write | String | Indicates whether the recording referenced by PostGreetingRecordingObjectId should be played. Possible values: 0 : No 1 : Always 2 : External Default value: 0 |
| PlayPostGreetingRecording | Read/Write | Integer | Specifies the object Id of the Post Greeting recording. |
| PostGreetingRecordingObjectId | Read/Write | String | URI of the Post Greeting Recording |
| PostGreetingURI | Read Only | String | Specifies the touchtone digits to be prepended to extension when dialing transfer number ( #, 0,1...9,*). Digits, plus, hash
                                                and asterisk only are allowed |
| PrependDigits | Read/Write | String | Specifies an object ID of the distribution list that is the message recipient. |
| RecipientDistributionListObjectId | Read/Write | String | Object ID of a User with a mailbox that is the message recipient. |
| RecipientDistributaionListURI | Read Only | String | Object ID of the schedule set assigned to the Call Handler. |
| ScheduleSetObjectId | Read/Write | String | Specifies the URI of schedule sets. |
| ScheduleSetURI | Read/Write | String | Determines if an outside caller can mark their message as private. Possible values: 0 : Never 1 : Always 2 : Ask Default value: 0 |
| SendPrivateMsg | Read/Write | Integer | A flag indicating whether an unidentified caller can mark a message as "secure." Default value: false |
| SendSecureMsg | Read/Write | Boolean | A flag indicating whether an unidentified caller can mark a message as "urgent." Possible values: 0 : Never 1 : Always 2 : Ask Default value: 0(Never) |
| SendUrgentMsg | Read/Write | Integer | Used when the UseDefaultTimezone is set to false. To know the Integer Time Zone codes for the Time Zones installed on the server following URI can be used: https://<connection-server>/vmrest/timezones.
                                                Example: 190 is the code for (GMT+05:30) Asia/Kolkata |
| TimeZone | Read/Write | Integer | A flag indicating whether Cisco Unity Connection will use the language assigned to the call. Possible Values: true false Default value: true |
| UseCallLanguage | Read/Write | Boolean | A flag that is dependent on the value of the Language field. If Language is set to Null, UseDefaultLanguage is set to true.
                                                If any language is specified, UseDefaultLanguage is set to false. Possible Values: true false |
| UseDefaultLanguage | Read/Write | Boolean | A flag indicating whether Cisco Unity Connection will use the system default Time Zone. Possible Values: true false Default value: false |
| UseDefaultTimeZone | Read/Write | Boolean | URI of the call handler owner API. |
| CallHandlerOwnerURI | Read Only | String | The name of the WAV file containing the recorded audio (voice name, greeting, etc.) for the parent object. It is displayed once a voice-name is recorded. |
| VoiceName | Read Only | String | It is displayed once a voice-name is recorded. |
| VoiceFileURI | Read Only | String | Specifies the URI of greetings |
| GreetingsURI | Read Only | String | Specifies the URI of transfer options. |
| TransferOptionsURI | Read Only | String | Specifies the URI of menu entries |
| MenuEntriesURI | Read Only | String | Specifies the URI of menu entries |
| ViceNameURI | Read Only | String | URI for voice name once it is recorded. |

| POST https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/callhandlerowners
Request Body:
<CallhandlerOwner>
            <UserObjectId>c0430be2-52b8-46d7-8fad-c6aa13781469</UserObjectId>
</CallhandlerOwner> |
|---|

| GET https://<connection-server>/vmrest/users |
|---|

| POST https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/callhandlerowners
Request Body:
<CallhandlerOwner>
            <DistributionListObjectId>b6616b6f-c0e0-4462-b64a-654b0f5baa65</DistributionListObjectId>
</CallhandlerOwner> |
|---|

| GET https://<connection-server>/vmrest/distributionlists |
|---|

| Response Code: 201
/vmrest/handlers/callhandlers/c0430be2-52b8-46d7-8fad-c6aa13781469 |
|---|

| POST https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/callhandlerowners
Accept: application/json
Content_type: application/json
Connection: keep_alive |
|---|

| {
    "UserObjectId": "5aeb75a4-14c2-474d-bec9-90aa731ee4cc",
} |
|---|

| Response Code: 201
/vmrest/handlers/callhandlers/c0430be2-52b8-46d7-8fad-c6aa13781469 |
|---|

| POST https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/callhandlerowners
Accept: application/json
Content_type: application/json
Connection: keep_alive |
|---|

| {
    "DistributionListObjectId": "5aeb75a4-14c2-474d-bec9-90aa731ee4cc",
} |
|---|

| Response Code: 201
/vmrest/handlers/callhandlers/c0430be2-52b8-46d7-8fad-c6aa13781469 |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/callhandlerowners |
|---|

| <CallhandlerOwners total="2">
   <CallhandlerOwner>
      <URI>/vmrest/handlers/callhandlers/f3b4cc1f-c2d7-4c67-9f53-7095d4b2a928/callhandlerowners/3aee209f-948b-450a-9d0f-75e2c1d4992f</URI>
      <DistributionListObjectId>b6616b6f-c0e0-4462-b64a-654b0f5baa65</DistributionListObjectId>
      <DistributionListURI>/vmrest/distributionlists/b6616b6f-c0e0-4462-b64a-654b0f5baa65</DistributionListURI>
      <ObjectId>3aee209f-948b-450a-9d0f-75e2c1d4992f</ObjectId>
      <TargetHandlerObjectId>f3b4cc1f-c2d7-4c67-9f53-7095d4b2a928</TargetHandlerObjectId>
   </CallhandlerOwner>
   <CallhandlerOwner>
      <URI>/vmrest/handlers/callhandlers/f3b4cc1f-c2d7-4c67-9f53-7095d4b2a928/callhandlerowners/75587df3-5be4-4e21-83b3-9ec7e4f60874</URI>
      <ObjectId>75587df3-5be4-4e21-83b3-9ec7e4f60874</ObjectId>
      <TargetHandlerObjectId>f3b4cc1f-c2d7-4c67-9f53-7095d4b2a928</TargetHandlerObjectId>
      <UserObjectId>ecdc6d2d-19e5-4adf-ac7d-6e351a5c95c4</UserObjectId>
      <UserURI>/vmrest/users/ecdc6d2d-19e5-4adf-ac7d-6e351a5c95c4</UserURI>
   </CallhandlerOwner>
</CallhandlerOwners> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/callhandlerowners
Accept: application/json
Connection: keep_alive |
|---|

| {
    "@total": "2",
    "CallhandlerOwner": {
    "URI": "/vmrest/handlers/callhandlers/b2d3d56a-f0c2-4839-98c5-
    48770690244a/callhandlerowners/ac6dda36-798d-4eea-9055-db5a31eb5599",
    "ObjectId": "75587df3-5be4-4e21-83b3-9ec7e4f60874",
    "UserObjectId": "5aeb75a4-14c2-474d-bec9-90aa731ee4cc",
    "UserURI": "/vmrest/users/5aeb75a4-14c2-474d-bec9-90aa731ee4cc",
    "TargetHandlerObjectId": "b2d3d56a-f0c2-4839-98c5-48770690244a"
    }
    "CallhandlerOwner": {
    "URI": "/vmrest/handlers/callhandlers/b2d3d56a-f0c2-4839-98c5-
    48770690244a/callhandlerowners/ac6dda36-798d-4eea-9055-db5a31eb5599",
    "ObjectId": "3aee209f-948b-450a-9d0f-75e2c1d4992f",
    "DistributionListObjectId": "b6616b6f-c0e0-4462-b64a-654b0f5baa65",
    "DistributionListURI": "/vmrest/users/b6616b6f-c0e0-4462-b64a-654b0f5baa65",
    "TargetHandlerObjectId": "b2d3d56a-f0c2-4839-98c5-48770690244a"
    }   
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/callhandlerowners/<callHandlerowner-objectid> |
|---|

| <CallhandlerOwner>
    <URI>/vmrest/handlers/callhandlers/4afc0de6-c52c-42e4-99bb-
  6359bd518f11/callhandlerowners/a6731eca-ba31-4cee-a367-0bd6f45c633f</URI>
    <ObjectId>a6731eca-ba31-4cee-a367-0bd6f45c633f</ObjectId>
    <UserObjectId>eaacd744-6fe1-4085-8b25-10c702fdfd20</UserObjectId>
    <UserURI>/vmrest/users/eaacd744-6fe1-4085-8b25-10c702fdfd20</UserURI>
    <TargetHandlerObjectId>4afc0de6-c52c-42e4-99bb-6359bd518f11</TargetHandlerObjectId>
  </CallhandlerOwner> |
|---|

| Response Code:200 |
|---|

| <CallhandlerOwner>
    <URI>/vmrest/handlers/callhandlers/f3b4cc1f-c2d7-4c67-9f53-
  7095d4b2a928/callhandlerowners/4e35ed6c-6aed-42e4-9723-b859706ac749</URI>
    <DistributionListObjectId>988630fa-313a-4f0c-980f-f6dc78add3ca</DistributionListObjectId>
    <DistributionListURI>/vmrest/distributionlists/988630fa-313a-4f0c-980f-f6dc78add3ca</DistributionListURI>
    <ObjectId>4e35ed6c-6aed-42e4-9723-b859706ac749</ObjectId>
    <TargetHandlerObjectId>f3b4cc1f-c2d7-4c67-9f53-7095d4b2a928</TargetHandlerObjectId>
  </CallhandlerOwner> |
|---|

| Response Code:200 |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/callhandlerowners/<callhandlerowner-objectid>
Accept: application/json
Connection: keep_alive |
|---|

| {
    "URI": "/vmrest/handlers/callhandlers/b2d3d56a-f0c2-4839-98c5-
    48770690244a/callhandlerowners/ac6dda36-798d-4eea-9055-db5a31eb5599",
    "ObjectId": "ac6dda36-798d-4eea-9055-db5a31eb5599",
    "UserObjectId": "5aeb75a4-14c2-474d-bec9-90aa731ee4cc",
    "UserURI": "/vmrest/users/5aeb75a4-14c2-474d-bec9-90aa731ee4cc",
    "TargetHandlerObjectId": "b2d3d56a-f0c2-4839-98c5-48770690244a"
} |
|---|

| Response Code:200 |
|---|

| {
    "URI": "/vmrest/handlers/callhandlers/b2d3d56a-f0c2-4839-98c5-
    48770690244a/callhandlerowners/ac6dda36-798d-4eea-9055-db5a31eb5599",
    "ObjectId": "4e35ed6c-6aed-42e4-9723-b859706ac749",
    "DistributionListObjectId": "988630fa-313a-4f0c-980f-f6dc78add3ca",
    "DistributionListURI": "/vmrest/users/988630fa-313a-4f0c-980f-f6dc78add3ca",
    "TargetHandlerObjectId": "b2d3d56a-f0c2-4839-98c5-48770690244a"
} |
|---|

| Response Code:200 |
|---|

| DELETE https://<connection-server>/vmrest/callhandlers/<callhandlerId>/callhandlerowners/<callhandlerowner-objectid> |
|---|

| Response Code: 204 |
|---|

| DELETE https://<connection-server>/vmrest/callhandlers/<callhandler-objectid>/callhandlerowners/<callhandlerowner-objectid>
Accept: application/json
Connection: keep_alive |
|---|

| Response Code: 204 |
|---|

| Parameter | Operation | Data Type | Comments |
|---|---|---|---|
| ObejectId | Read Only | String | Specifies an object ID to uniquely identify a call handler owner. |
| UserObjectId | Read/Write | String | Specifies an object ID of the user who owns the call handler. |
| VmsObjectId | Read Only | String | Specifies an unique identifier of the LocationVMS object. |
| DistributionListObjectId | Read Write | String | Specifies an object ID of the distribution list who owns the call handler. |
| TragetHandlerObjectId | Read Only | String | Specifies an object ID of the call handler to which the call handler owner object belongs. |
| UserURI | Read Only | String | Specifies URI to get details of the user who owns the Call Handler. |
| DistributionListURI | Read Only | String | Specifies URI to get details of the distribution list who owns the Call Handler Owner |

| Name | Value | Description |
|---|---|---|
| Ignore | 0 | No action taken |
| Hangup | 1 | The call is immediately terminated. |
| Goto | 2 | Go to an object such as a call handler, directory handler or interview handler. |
| Error | 3 | Play the error greeting. |
| TakeMsg | 4 | Take a message. |
| SkipGreeting | 5 | Skip greeting. |
| RestartGreeting | 6 | Restart greeting on current handler |
| TransferAltContact | 7 | Transfer to alternate contact number. |
| RouteFromNextRule | 8 | Route from Next call routing rule. |

| Name | Value | Description |
|---|---|---|
| No | 0 | Don't play the recording |
| Always | 1 | Play system default |
| External | 2 | Play recording |

| Name | Description |
|---|---|
| AD | Directory conversation |
| PHTransfer | Transfer to a user or call handler |
| PHGreeting | Play greeting of a user or call handler |
| PHInterview | Interview Conversation |
| Attempt Forward | Forwards the call to the user's greeting if the forwarding number matches a user |
| Attempt SignIn | Sends the call to a user's sign-in if the calling number matches a user |
| BroadcastMessageAdministrator | Sends the call to a conversation for sending broadcast messages |
| SystemTransfer | Sends the call to a conversation allowing the caller to transfer to a number they specify (assuming the restriction table
                                          allows it). |
| CheckedOutGuest | Sends the call to a conversation for checked-out hotel guests. |
| GreetingsAdministrator | Sends the call to a conversation allowing changing greetings by phone. |
| ReverseTrapConv | Connects to Visual Voicemail. |
| SubSignIn | Sends the call to the sign-in conversation, which prompts the user to enter their ID. |
| ConvUtilsLiveRecord | Sends the call to the live-record pilot number configured on Call Manager. |
| SubSysTransfer | Sends the call to a conversation allowing the caller to transfer to a number they specify (assuming the restriction table
                                          allows it). However, requires user sign-in first, so unknown callers cannot use it. |

| Greeting | Description |
|---|---|
| Alternate | Can be used for a variety of special situations, such as vacations, leave of absence, or a holiday. An alternate greeting
                                          overrides all other greetings. |
| Busy | Plays when the extension is busy. A busy greeting overrides the standard, off hours, and internal greetings. |
| Error | Plays when a caller attempts to dial an extension that does not exist on the system during a greeting. |
| Internal | Plays to internal callers only. An internal greeting overrides the standard and off hours greetings. |
| Off Hours | Plays during the closed (nonbusiness) hours defined for the active schedule. An off hours greeting overrides the standard
                                          greeting, and thus limits the standard greeting to the open hours defined for the active schedule. |
| Standard | Plays at all times unless overridden by another greeting. You cannot disable the standard greeting. |
| Holiday | Plays when holiday schedule is encountered unless overridden by an alternate greeting. |

| GET https://<connection-server>/vmrest/callhandlertemplates/<callhandler-objectid>/greetings |
|---|

| <Greetings total="7"><Greeting> 
    <URI>/vmrest/handlers/callhandlers/fa468470-1031-4896-ab11-3736bdee3b00/greetings/Alternate</URI> 
    <CallHandlerObjectId>fa468470-1031-4896-ab11-3736bdee3b00</CallHandlerObjectId> 
    <CallhandlerURI>/vmrest/handlers/callhandlers/fa468470-1031-4896-ab11-3736bdee3b00</CallhandlerURI> 
    <IgnoreDigits>false</IgnoreDigits> 
    <PlayWhat>0</PlayWhat> 
    <RepromptDelay>2</RepromptDelay> 
    <Reprompts>0</Reprompts> 
    <TimeExpires>1972-01-01 05:30:00.0</TimeExpires> 
    <GreetingType>Alternate</GreetingType> 
    <AfterGreetingAction>4</AfterGreetingAction> 
    <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt> 
    <EnableTransfer>false</EnableTransfer>
    <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
    <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt> 
    <GreetingStreamFilesURI>/vmrest/handlers/callhandlers/fa468470-1031-4896-ab11-3736bdee3b00/greetings/Alternate/greetingstreamfiles</GreetingStreamFilesURI> 
    <Enabled>false</Enabled> 
</Greeting> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/callhandler/<callhandler-objectid>/greetings
Accept: appliaction/json
Conenction: keep_alive |
|---|

| { 
   "@total":"7" 
   "Greeting": [
  { 
    "URI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a/greetings/Alternate",
    "CallHandlerObjectId":"a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a",
    "CallhandlerURI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a",
    "IgnoreDigits":"false",
    "PlayWhat":"0",
    "RepromptDelay":"2",
    "Reprompts":"0", 
    "TimeExpires":"1972-01-01 00:00:00.0",
    "GreetingType":"Alternate", 
    "AfterGreetingAction":"4",
    "PlayRecordMessagePrompt":"true" ,
    "EnableTransfer":"false",
    "EnablePersonalVideoRecording":"false",
    "PlayRecordVideoMessagePrompt":"false",
    "Enabled":"false"  
  }, 
  { 
    "URI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a/greetings/Busy", 
    "CallHandlerObjectId":"a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a", 
    "CallhandlerURI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a",   
    "IgnoreDigits":"false", 
    "PlayWhat":"0", 
    "RepromptDelay":"2", 
    "Reprompts":"0", 
    "TimeExpires":"1972-01-01 00:00:00.0", 
    "GreetingType":"Busy", 
    "AfterGreetingAction":"4",
    "PlayRecordMessagePrompt":"true", 
    "EnableTransfer":"false",
    "EnablePersonalVideoRecording":"false",
    "PlayRecordVideoMessagePrompt":"false",
    "Enabled":"false"  
  }, 
] 
} |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/callhandler/<callhandler-
  objectid>/greetings/<Greetingname> |
|---|

| <Greeting> 
    <URI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-836910ac1a4c/greetings/Alternate</URI> 
    <CallHandlerObjectId>5f6e1043-5edf-4646-90ac-836910ac1a4c</CallHandlerObjectId> 
    <CallhandlerURI>/vmrest/handlers/callhandlers/5f6e1043-5edf-4646-90ac-836910ac1a4c</CallhandlerURI> 
    <IgnoreDigits>false</IgnoreDigits> 
    <PlayWhat>0</PlayWhat> 
    <RepromptDelay>2</RepromptDelay> 
    <Reprompts>0</Reprompts> 
    <TimeExpires>1972-01-01 00:00:00.0</TimeExpires> 
    <GreetingType>Alternate</GreetingType> 
    <AfterGreetingAction>4</AfterGreetingAction> 
    <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt> 
    <EnableTransfer>false</EnableTransfer>
    <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
    <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt> 
    <Enabled>false</Enabled>  
</Greeting> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/callhandler/<Callhandler-
objectid>/greetings/<Greetingname>
Accept: application/json
Connection: keep_alive |
|---|

| { 
    "URI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a/greetings/Alternate", 
    "CallHandlerObjectId":"a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a", 
    "CallhandlerURI":"/vmrest/handlers/callhandlers/a2f8fb8f-68ee-4a17-90a0-bff0308b5b1a", 
    "IgnoreDigits":"false", 
    "PlayWhat":"0", 
    "RepromptDelay":"2", 
    "Reprompts":"0", 
    "TimeExpires":"1972-01-01 00:00:00.0", 
    "GreetingType":"Alternate", 
    "AfterGreetingAction":"4", 
    "PlayRecordMessagePrompt":"true" ,
    "EnableTransfer":"false", 
    "EnablePersonalVideoRecording":"false",
    "PlayRecordVideoMessagePrompt":"false",
    "Enabled":"false"  
} |
|---|

| Response Code: 200 |
|---|

| PUT https://<connection-server>/vmrest/callhandler/<callhandler-objectid>/greetings/<Greetingname>
Request Body:
<Greeting>
    <PlayWhat>1</PlayWhat>
    <PlayRecordMessagePrompt>true</PlayRecordMessagePrompt>
</Greeting> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/callhandler/<Callhandler-objectid>/greetings/<Greetingname>
Accept: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "PlayWhat":"1",
    "PlayRecordMessagePrompt":"true"
} |
|---|

| Response Code: 204 |
|---|

| Note | Greetings are disabled or enabled using the combination of fields
                                          		  "Enabled" and "TimeExpires". |
|---|---|

| PUT https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/greetings/<Greetingname> |
|---|

| <Greeting>
  <Enabled>false</Enabled>
</Greeting> |
|---|

| Response Code : 204 |
|---|

| {
  "Enabled":"false"
} |
|---|

| Response Code : 204 |
|---|

| GET http://<connection-server>/vmrest/Callhandlersprimarytemplates/<callhandlerobjectid>/usertemplates/Greetings/<GreetingType>/GreetingStreamFiles/<language>/video |
|---|

| Response: 200
<CallControl>
    <resourceId>aad91d6d-aeca-4a72-8069-b656efb3041f.wav</resourceId>
    <sessionId>570146ed1504cb1</sessionId>
</CallControl |
|---|

| Request 
GET  vmrest/handlers/callhandlers/30600b21-1a4c-47a3-a078-8078984e5376/greetings/Standard/greetingstreamfiles/1033/video
Accept: application/json
User-Agent: Java/1.6.0_17
Host: <connection-server>
Connection: keep-alive
authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg= |
|---|

| Response
HTTP/1.1 200
Content-Type: application/json
Date: Fri, 15 Jan 2010 15:14:11 GMT
Server:
{ “resourceId” :” aad91d6d-aeca-4a72-8069-b656efb3041f.wav”, “sessionId” : ”570146ed1504cb1”} |
|---|

| PUT http://<connection-server>/vmrest/Callhandlersprimarytemplates/<callhandlerobjectid>/usertemplates/Greetings/<GreetingType>/GreetingStreamFiles/<language>/video |
|---|

| <CallControl>
     <resourceId>aad91d6d-aeca-4a72-8069-b656efb3041f.wav</resourceId>
     <sessionId>570146ed1504cb1</sessionId>
</CallControl> |
|---|

| Response: 204 OK |
|---|

| Request 
PUT  vmrest/handlers/callhandlers/30600b21-1a4c-47a3-a078-8078984e5376/greetings/Standard/greetingstreamfiles/1033/video
Content-Type: application/json
Accept: application/json
Host: <connection-server>
Connection: keep-alive
authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==

{ “resourceId” :” aad91d6d-aeca-4a72-8069-b656efb3041f.wav”, “sessionId” : ”570146ed1504cb1”} |
|---|

| Response :
HTTP/1.1 204
Content-Type: application/json
Date: Fri, 15 Jan 2010 15:14:11 GMT
Server: |
|---|

| Parameter | Operations | Data Type | Comments |
|---|---|---|---|
| URI | Read Only | String | URI of greetings |
| CallHandlerObjectId | Read Only | String (36) | The unique identifier of the call handler
                                             					 object to which this greeting rule belongs. |
| TemplateCallHandlerURI | Read/Write | String | URI of the call handler. |
| IgnoreDigits | Read/Write | Boolean | A flag indicating whether Cisco Unity
                                             					 Connection takes action in response to touchtone keys pressed by callers during
                                             					 the greeting. This column overrides all the Menu Entry settings when this
                                                						greeting is active. This has the same effect as setting all the menu entry keys
                                                						for this handler to "locked". It is a shorthand way of locking callers into the
                                                						greeting so they cannot get out until it completes. Values can be: false: Caller
                                                      						  input enabled during greeting true: Caller
                                                      						  input ignored during greeting Default Value: false |
| PlayWhat | Read/Write | Integer | Specifies if the system default greeting,
                                             					 personal recording, or nothing should be played. Default Value: 0 For more information, refer to the
                                                						Enumeration Type section. |
| RepromptDelay | Read/Write | Integer | The amount of time (in seconds) that Cisco
                                             					 Unity Connection waits without receiving any input from a caller before Cisco
                                             					 Unity Connection prompts the caller again. The range of this field can vary
                                             					 from 0 to 100. Values can be: 0: Do wait
                                                      						  without receiving caller input and do not replay greeting. 1 or greater:
                                                      						  Wait this number of seconds without receiving any input from the caller before
                                                      						  playing the greeting again. Default Value: 2 |
| Reprompts | Read/Write | Integer | The number of times to reprompt a caller.
                                             					 After the number of times indicated here, Cisco Unity Connection performs the
                                             					 after-greeting action. This column is typically used when an audio text application
                                                						is expecting input from a caller. The range of this field can vary from 0 to
                                                						100. Values can be: 0: Do not
                                                      						  re-prompt - Cisco Unity Connection will play the greeting once and then the
                                                      						  after-greeting action is taken. 1 or greater:
                                                      						  Number of times to re-prompt. The "RepromptDelay" value determines how many seconds to
                                                						wait in between replays. Default Value: 0 |
| GreetingType | Read Only | String | Specifies the greeting type. There are 7
                                             					 greeting types available. |
| AfterGreetingAction | Read/Write | Integer | The type of call action to take, e.g.,
                                             					 hang-up, goto another object, etc. The values that are allowed are: Hangup Goto Restart greeting Route from next
                                                      						  call routing rule Take message Custom Type:
                                                      						  Call Action |
| AfterGreetingTargetConversation | Read/Write | String | Specifies the conversation to go to after
                                             					 the greeting is played. For more information, refer to the Enumeration Type section. |
| AfterGreetingTargetHandlerObjectId | Read/Write | String (36) | The unique identifier of the call action
                                             					 object that Cisco Unity Connection performs after the greeting is played. |
| TimeExpires | Read/Write | Datetime | The date and time when the greeting rule
                                             					 expires. The greeting rule is considered not expired (enabled), if the value is
                                             					 NULL or a future date. The greeting rule is considered expired (disabled), the
                                             					 value is in the past. The "Enhanced Alternate Greeting" feature uses this column
                                                						to specify how long the subscriber wants their alternate greeting enabled. The
                                                						standard greeting rule should never be disabled. The field is not displayed
                                                						when the Greeting field is enabled with no end date and end time. |
| PlayRecordMessagePrompt | Read/Write | Boolean | A flag indicating whether the "Record your
                                             					 message at the tone…" prompt prior to recording a message. Values: true - Play
                                                      						  Record Message prompt is enabled. false - Play
                                                      						  Record prompt is disabled. Default Value: true |
| EnableTransfer | Read/Write | Boolean | A flag indicating when an extension is
                                             					 dialed at the greeting and the extension is not available whether to transfer
                                             					 to another extension. Values: true: Allows
                                                      						  transfer false: Does not
                                                      						  allow Default Value: false |
| EnablePersonalVideoRecording | Read/Write | Boolean | A flag indicating whether the personal video recording of
                                                						the user will be used. Values: true : Personal
                                                      						  Video Recording is enabled. false : Personal
                                                      						  Video Recording is not enabled. Default value : false |
| PlayRecordVideoMessagePrompt | Read/Write | Boolean | A flag indicating whether Cisco Unity
                                             					 Connection will prompt callers to wait for a tone before recording their video
                                             					 message. Values: true : Callers
                                                      						  will be prompted with a tone before recording their video message. false : Callers
                                                      						  will not be prompted with a tone before recording their video message. Default value : false This flag is editable only when the flag
                                                						EnablePersonalVideoRecording is set to True. |
| Enabled | Read/Write | Boolean | A flag indicating that the Greeting is
                                             					 enabled or disabled |

| GET https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/transferoptions |
|---|

| <TransferOptions total="2"> 
  <TransferOption>
    <URI>/vmrest/handlers/callhandlers/166da38f-951b-4c9a-92da-
  87ed7993cfec/transferoptions/Standard</URI>
    <CallHandlerObjectId>166da38f-951b-4c9a-92da-
  87ed7993cfec</CallHandlerObjectId>
    <CallhandlerURI>/vmrest/handlers/callhandlers/166da38f-951b-4c9a-92da-
  87ed7993cfec</CallhandlerURI>
    <TransferOptionType>Standard</TransferOptionType>
    <Action>0</Action>
    <Extension>0</Extension>
    <RnaAction>1</RnaAction>
    <TransferAnnounce>false</TransferAnnounce>
    <TransferConfirm>false</TransferConfirm>
    <TransferDtDetect>false</TransferDtDetect>
    <TransferHoldingMode>0</TransferHoldingMode>
    <TransferIntroduce>false</TransferIntroduce>
    <TransferRings>4</TransferRings>
    <TransferScreening>false</TransferScreening>
    <TransferType>0</TransferType>
    <MediaSwitchObjectId>cd10d831-28d3-40da-ab13-
  a87431b38682</MediaSwitchObjectId>
    <PhoneSystemURI>/vmrest/phonesystems/cd10d831-28d3-40da-ab13-
  a87431b38682</PhoneSystemURI>
    <UsePrimaryExtension>false</UsePrimaryExtension>
    <PlayTransferPrompt>true</PlayTransferPrompt>
    <PersonalCallTransfer>false</PersonalCallTransfer>
    <Enabled>true</Enabled>
  </TransferOption>
</TransferOptions> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/transferoptions
Action: application/json
Connection: keep_alive |
|---|

| {   
  "@total": "2",  
  "TransferOption":    [           
    {         
    "URI": "/vmrest/handlers/callhandlers/166da38f-951b-4c9a-92da-
    87ed7993cfec/transferoptions/Alternate",         
    "CallHandlerObjectId": "166da38f-951b-4c9a-92da-87ed7993cfec", 
    "CallhandlerURI": "/vmrest/handlers/callhandlers/166da38f-951b-4c9a-92da-
    87ed7993cfec",         
    "TransferOptionType": "Alternate",         
    "Action": "0",         
    "Extension": "0",         
    "RnaAction": "1",         
    "TimeExpires": "1972-01-01 00:00:00.0",         
    "TransferAnnounce": "false",         
    "TransferConfirm": "false",        
    "TransferDtDetect": "false",        
    "TransferHoldingMode": "0",        
    "TransferIntroduce": "false",         
    "TransferRings": "4",         
    "TransferScreening": "false",        
    "TransferType": "0",        
    "MediaSwitchObjectId": "cd10d831-28d3-40da-ab13-a87431b38682",        
    "PhoneSystemURI": "/vmrest/phonesystems/cd10d831-28d3-40da-ab13-
    a87431b38682",         
    "UsePrimaryExtension": "true",        
    "PlayTransferPrompt": "true",         
    "PersonalCallTransfer": "false",         
    "Enabled": "false"      
    },           
    {         
    "URI": "/vmrest/callhandlerprimarytemplates/166da38f-951b-4c9a-92da-
    87ed7993cfec/transferoptions/Off%20Hours",         
    "CallHandlerObjectId": "166da38f-951b-4c9a-92da-87ed7993cfec",         
    "CallhandlerURI": "/vmrest/handlers/callhandlers/166da38f-951b-4c9a-92da-
    87ed7993cfec",         
    "TransferOptionType": "Off Hours",         
    "Action": "0",         
    "Extension": "0",         
    "RnaAction": "1",        
    "TransferAnnounce": "false",         
    "TransferConfirm": "false",         
    "TransferDtDetect": "false",        
    "TransferHoldingMode": "0",         
    "TransferIntroduce": "false",         
    "TransferRings": "4",         
    "TransferScreening": "false",         
    "TransferType": "0",         
    "MediaSwitchObjectId": "cd10d831-28d3-40da-ab13-a87431b38682",         
    "PhoneSystemURI": "/vmrest/phonesystems/cd10d831-28d3-40da-ab13-
    a87431b38682",        
    "UsePrimaryExtension": "true",         
    "PlayTransferPrompt": "true",        
    "PersonalCallTransfer": "false",         
    "Enabled": "true"      
    }          
  }
} |
|---|

| Response Code: 200 |
|---|

| Request URI:
PUT https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-
objectid>/transferoptions/Alternate 
Request Body:
<TransferOption>
    <Action>1</Action>
    <Extension>1000</Extension>
    <TimeExpires>2012-12-31 12:00:00.0</TimeExpires>
    <TransferAnnounce>true</TransferAnnounce>
    <TransferConfirm>true</TransferConfirm>
    <TransferIntroduce>true</TransferIntroduce>
    <TransferScreening>true</TransferScreening>
    <TransferType>1</TransferType>
    <Enabled>true</Enabled>
</TransferOption> |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/handlers/callhandlers/<callhandler-objectid>/transferoptions/Alternate
Action: application/json
Content_type: application/json
Connection: keep_alive
Request Body:
{
    "Action": "1",
    "TimeExpires": "2012-12-31 12:00:00.0",
    "TransferAnnounce": "true",
    "TransferConfirm": "true", 
    "TransferIntroduce": "true",
    "TransferRings": "8",
    "TransferScreening": "true",
    "TransferType": "1",
    "Enabled": "true"
} |
|---|

| Response Code: 204 |
|---|

| Parameter | Operations | Data Type | Comments |
|---|---|---|---|
| URI | Read Only | String | Specifies URI of the call handler transfer
                                             					 options. |
| CallHandlerObjectId | Read Only | String (36) | Specifies the call handler object ID. |
| CallHandlerURI | Read Only | String | SpecifiesURI of the call handler being
                                             					 referenced. |
| TransferOptionType | Read Only | String | Specifies the transfer option type. There
                                             					 are 3 transfer option types available:- Alternate - in
                                                      						  effect at all times, overrides standard and off hours. Off Hours - off
                                                      						  or closed hours based on specified schedule. Standard -
                                                      						  standard hours based on specified schedule. |
| Action | Read/Write | Integer | Specifies the Transfer rule action. Refer
                                             					 to the section Enumeration Type Default value : 0 |
| RnaAction | Read/Write | Integer | Action to take on Ring-No-Answer (RNA)
                                             					 condition. Refer to the section Enumeration Type. Default value: 1 |
| TimeExpires | Read/Write | DateTime | Rather than using a simple on and off
                                             					 scheme for enabling transfer options and greetings, Cisco Unity Connection
                                             					 employs a date scheme. If the value is NULL or a date in the future then the
                                             					 transfer option is considered enabled. If the date is sometime in the past,
                                             					 then the transfer option is considered disabled. The "Standard" transfer option should never be disabled. For
                                                						primary call handlers associated with the subscribers, the "Alternate" transfer
                                                						option should always be enabled since subscribers have only one transfer option
                                                						used currently. |
| TransferAnnounce | Read/Write | Boolean | A flag indicating whether Cisco Unity
                                             					 Connection plays "transferring call" when the subscriber answers the phone.
                                             					 This requires a TransferType column value = "Supervised" (1) Possible Values: false: Do not
                                                      						  say "Transferring call" when the subscriber answers the phone true: Say
                                                      						  "Transferring call" when the subscriber answers the phone Default Value: false |
| TransferConfirm | Read/Write | Boolean | The type of call transfer Unity Connection
                                             					 will perform - supervised or unsupervised (also referred to as "Release to
                                             					 Switch" transfer). This requires a "TransferType" of supervised (1). Unsupervised
                                                      						  transfer (also referred to as "Release to Switch" transfer) - Cisco Unity
                                                      						  Connection puts the caller on hold, dials the extension, and releases the call
                                                      						  to the phone system. When the line is busy or is not answered, the phone system
                                                      						  (not Cisco Unity Connection) forwards the call to the subscriber or handler
                                                      						  greeting. To use "Unsupervised" transfer, call forwarding must be enabled on
                                                      						  the phone system. Supervised
                                                      						  transfer - Cisco Unity Connection acts as a receptionist, handling the
                                                      						  transfer. If the line is busy or the call is not answered, Cisco Unity
                                                      						  Connection (not the phone system) forwards the call to the subscriber or
                                                      						  handler greeting. Supervised transfer can be used regardless if the phone
                                                      						  system forwards calls or not. Typically, TransferConfirm is used in conjunction with the
                                                						call screening option ("TransferScreening" column) enabled. This combination
                                                						enables the subscriber to hear the name of the caller and then decide if they
                                                						want to take the call or not. Possible values: false: Transfer
                                                      						  confirm disabled true: Transfer
                                                      						  confirm enabled Default Value: false |
| TransferDtDetect | Read/Write | Boolean | A flag indicating whether Cisco Unity
                                             					 Connection will check for dial tone before attempting to transfer the call.
                                             					 This requires a "TransferType" of supervised (1). This is usually used for phone systems that do not have
                                                						"positive disconnect" capabilities to avoid sending terminated calls to the
                                                						operator console. Possible Values: false: Do not
                                                      						  check for dial tone prior to transferring a call true: Check for
                                                      						  dial tone prior to transferring a call Default value: false. |
| TransferHoldingMode | Read/Write | Integer | The action Cisco Unity Connection will take
                                             					 when the extension is busy. This requires a TransferType column value =
                                             					 "Supervised" (1). Refer to the section Enumeration Type. Default Value is 0. |
| TransferIntroduce | Read/Write | Boolean | A flag indicating whether Cisco Unity
                                             					 Connection will say "call for <recorded name of the call handler>" when
                                             					 the subscriber answers the phone. Requires a "TransferType" of supervised (1).This
                                                						functionality is normally used when a single extension number is being shared
                                                						by multiple subscribers or a scenario where the subscriber who is the message
                                                						recipient takes calls for more than one dialed extension. The introduction
                                                						alerts the subscriber who answers that the call is for the call handler.
                                                						Default value: false. |
| TransferRings | Read/Write | Integer | The number of times the extension rings
                                             					 before Cisco Unity Connection considers it a "ring no answer" and plays the
                                             					 subscriber or handler greeting. Requires a "TransferType" of supervised (1). The value of
                                                						this column should never be less than 2 for a supervised transfer. Possible
                                                						values: Range 2-20 Default Value: 4 |
| TransferScreening | Read/Write | Boolean | A flag indicating whether Cisco Unity
                                             					 Connection will prompt callers to say their names. When the phone is answered,
                                             					 the subscriber hears "Call from..." before Cisco Unity Connection transfers the
                                             					 call.Requires a "TransferType" of supervised (1). Normally this column is used along with "TransferConfirm" to
                                                						allow the subscriber to screen calls. Possible Values: false: Call
                                                      						  screening disabled true: Ask and
                                                      						  record caller name Default value: false. |
| TransferType | Read Only | String | The type of call transfer Cisco Unity
                                             					 Connection will perform - supervised or unsupervised (also referred to as
                                             					 "Release to Switch" transfer). Unsupervised
                                                      						  transfer (also referred to as "Release to Switch" transfer) - Cisco Unity
                                                      						  Connection puts the caller on hold, dials the extension, and releases the call
                                                      						  to the phone system. When the line is busy or is not answered, the phone system
                                                      						  (not Cisco Unity Connection) forwards the call to the subscriber or handler
                                                      						  greeting. To use "Unsupervised" transfer, call forwarding must be enabled on
                                                      						  the phone system. Supervised
                                                      						  transfer - Cisco Unity Connection acts as a receptionist, handling the
                                                      						  transfer. If the line is busy or the call is not answered, Cisco Unity
                                                      						  Connection (not the phone system) forwards the call to the subscriber or
                                                      						  handler greeting. Supervised transfer can be used regardless if the phone
                                                      						  system forwards calls or not. Refer to the section Enumeration Type. Default value: 0 |
| MediaSwitchObjectId | Read Only | String (36) | The unique identifier of the MediaSwitch
                                             					 object that Cisco Unity Connection uses for transferring the call to the
                                             					 subscriber phone. |
| PhoneSystemURI | Read Only | String | Specifies the URI of the Phone Systems. |
| UsePrimaryExtension | Read/Write | Boolean | If extension is null this field will be set
                                             					 to true to indicate that we are using primary extension instead of DtmfAccessId
                                             					 for the owning handler or the subscriber. Possible value: true false Default value: true |
| Extension | Read/Write | String (40) | If an administrator using Cisco Unity
                                             					 Connection Administration chooses to transfer to the extension of a subscriber
                                             					 or call handler, Cisco Unity Connection will automatically enter the
                                             					 DtmfAccessId value pulled from the DtmfAccessId table for the call handler into
                                             					 this column.Can take values:Digits, hash, comma, asterisk, plus are allowed. |
| PlayTransferprompt | Read/Write | Boolean | A flag indicating whether the "Wait while I
                                             					 transfer your call" prompt should be played prior to transferring a call. Possible values: true - Play
                                                      						  Transfer prompt is enabled. false - Play
                                                      						  transfer prompt is disabled. Default Value: true. |
| PersonalCallTransfer | Read/Write | Boolean | A flag indicating whether or not Personal
                                             					 Call Transfer Rules are used for the specific Transfer Option. Possible Values:- false: Personal
                                                      						  Call Transfer Rules are not used. true:- Personal
                                                      						  Call Transfer Rules are used. Default value: false |
| Enabled | Read/Write | Boolean | Indicate whether the transfer option is
                                             					 enabled or not. To enable rule till particular end date, TimeExpires should
                                             					 also be specified. Whereas, to enable transfer rule with no end date, the
                                             					 TimeExpires field should be empty. Possible Values: true: enabled false: disabled Default Value: true |

| Note | The transfer rules are enabled with no end date by default. |
|---|---|