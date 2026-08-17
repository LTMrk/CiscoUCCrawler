---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-alternat-extension-html-7d4057235d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m-cupi-api-alternat-extension.html
retrieved_at: 2026-08-17T03:47:40.207691+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- Alternate Extension

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- Alternate Extension

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- Alternate Extension

Links to Other API pages: Cisco_Unity_Connection_APIs

## Alternate
                        	 Extensions API

### Listing the Basic
                           	 Settings of Alternate Extension

```
GET https://<connection-server>/vmrest/users/<user-objectid>/alternateextensions
```

The following is the response from the above *GET* request and the
                              		actual response will depend upon the information given by you:

```
<AlternateExtensions total="1">
  <AlternateExtension>
  <URI>/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/alternateextensions/f0cfbf52-a6b2-466c-b7e6-eb05d6cce705</URI>
  <IdIndex>0</IdIndex>
  <DtmfAccessId>99934</DtmfAccessId>
  <LocationObjectId>42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationObjectId>
  <LocationURI>/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-8ddce4f430ff</LocationURI>
  <ObjectId>f0cfbf52-a6b2-466c-b7e6-eb05d6cce705</ObjectId>
  <PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId>
  <PartitionURI>/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionURI>
  <AlternateExtensionAdvancedURI>/vmrest/alternateextensionadvanceds/42266e69-5e5e-42fe-924e-e94b2c9e06b3</AlternateExtensionAdvancedURI>
  </AlternateExtension>
</AlternateExtensions>
```

```
Response Code: 200
```

JSON Example

```
GET https://<connection-server>/vmrest/users/<user-objectid>/alternateextensions/<alternateextension_objectid>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                              		actual response will depend upon the information given by you:

```
{
  "URI": "/vmrest/users/9375d893-c8eb-437b-90bf-7de4b1d0c3e8/alternateextensions/f0cfbf52-a6b2-466c-b7e6-eb05d6cce705",
  "IdIndex": "0",
  "DtmfAccessId": "99934",
  "LocationObjectId": "42a9ab40-490d-4819-9bfb-8ddce4f430ff",
  "LocationURI": "/vmrest/locations/connectionlocations/42a9ab40-490d-4819-9bfb-8ddce4f430ff",
  "ObjectId": "f0cfbf52-a6b2-466c-b7e6-eb05d6cce705",
  "PartitionObjectId": "da2114bf-cde7-43d8-9709-cd3895a9d41b",
  "PartitionURI": "/vmrest/partitions/da2114bf-cde7-43d8-9709-cd3895a9d41b",
  "AlternateExtensionAdvancedURI": "/vmrest/alternateextensionadvanceds/42266e69-5e5e-42fe-924e-e94b2c9e06b3"
}
```

### Listing the
                           	 Advanced Settings of Alternate Extension

Fetch the Alternate Extension
                                    			 URI from following URI:

```
https://<connection-server>/vmrest/users/<user-objectid>
```

Now fetch the Alternate Extension Advanced URI from a URI:

```
https://<connection-server>/vmrest/users/<user-objectid>/alternateextensions/<alternateextionsion_objectid>
```

Set following as a Request URI:

```
https://<connection-server>/vmrest/alternateextensionadvanceds/<alternateextensionadvanced_objectid>
```

The following is the response from the above *GET* request and the
                                    			 actual response will depend upon the information given by you:

```
<AlternateExtensionAdvanced> 
  <URI>/vmrest/alternateextensionadvanceds/42266e69-5e5e-42fe-924e-e94b2c9e06b3</URI>
  <DeviceDtmfAccessIdObjectId>7c26381e-ee0f-4abf-9083-94a5017abc76</DeviceDtmfAccessIdObjectId>
  <MessageSpeed>100</MessageSpeed>
  <MessageVolume>50</MessageVolume>
  <ObjectId>42266e69-5e5e-42fe-924e-e94b2c9e06b3</ObjectId>
  <PromptSpeed>100</PromptSpeed>
  <PromptVolume>50</PromptVolume>
  <SaveMessageOnHangup>true</SaveMessageOnHangup>
  <SendMessageOnHangup>1</SendMessageOnHangup>
  <SkipPasswordForKnownDevice>true</SkipPasswordForKnownDevice>
  <SubscriberObjectId>bf0e9ca3-db47-472d-aa0c-609a3265ada1</SubscriberObjectId>
  <UserURI>/vmrest/users/bf0e9ca3-db47-472d-aa0c-609a3265ada1</UserURI>
</AlternateExtensionAdvanced>
```

```
Response Code: 200
```

JSON Example

Step 1: Fetch the Alternate Extension URI from following URI:

```
GET https://<connection-server>/vmrest/users/<user-objectid>
```

Step 2: Now fetch the Alternate Extension Advanced URI from a URI:

```
GET https://<connection-server>/vmrest/users/
<user-objectid>/alternateextensions/<alternateextension_objectid>
```

Step 3: Set following as a Request URI:

```
GET  https://<connection-server>/vmrest/alternateextensionadvanceds/<objectid>
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the
                                       			 actual response will depend upon the information given by you:

```
{  
  "URI": "/vmrest/alternateextensionadvanceds/42266e69-5e5e-42fe-924e-e94b2c9e06b3",
  "DeviceDtmfAccessIdObjectId": "7c26381e-ee0f-4abf-9083-94a5017abc76",  
  "MessageSpeed": "100", 
  "MessageVolume": "50", 
  "ObjectId": "42266e69-5e5e-42fe-924e-e94b2c9e06b3", 
  "PromptSpeed": "100", 
  "PromptVolume": "50",  
  "SaveMessageOnHangup": "true", 
  "SendMessageOnHangup": "1", 
  "SkipPasswordForKnownDevice": "true",  
  "SubscriberObjectId": "bf0e9ca3-db47-472d-aa0c-609a3265ada1", 
  "UserURI": "/vmrest/users/bf0e9ca3-db47-472d-aa0c-609a3265ada1"
}
```

```
Response Code: 200
```

### Create a new
                           	 Alternate Extension

The mandatory fields for creation
                              		of alternate extension are IdIndex, DtmfAccessId, and PartitionObjectId. The
                              		URI for getting partition object ID use:

```
GET https://<connection-server>/vmrest/partitions
```

The following URI is fetched from the response body of URI:

```
GET https://<connection-server>/vmrest/users/<user-objectid>
```

To create a new alternate extension for a user

```
POST https://<connection-server>/vmrest/users/<user-objectid>/alternateextensions
```

```
<AlternateExtension> <IdIndex>2</IdIndex>
<DtmfAccessId>999341</DtmfAccessId>
<PartitionObjectId>da2114bf-cde7-43d8-9709-cd3895a9d41b</PartitionObjectId>
</AlternateExtension>
```

The following is the response from the above *POST* request and the
                              		actual response will depend upon the information given by you:

```
Response Code: 201
/vmrest/users/fa2114bf-cde7-43d8-9709-cd3895a9d41b/alternateextensions/ea2114bf-cde7-43d8-9709-cd3895a9d41b
```

JSON Example

```
POST https://<connection-server>/vmrest/users/<user-objectid>/alternateextensions
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
{
  "IdIndex":"2",
  "DtmfAccessId":"999341",
  "PartitionObjectId":da2114bf-cde7-43d8-9709-cd3895a9d41b"
}
```

The following is the response from the above *POST* request and the
                              		actual response will depend upon the information given by you:

```
Response code: 201
/vmrest/users/fa2114bf-cde7-43d8-9709-cd3895a9d41b/alternateextensions/ea2114bf-cde7-43d8-9709-cd3895a9d41b
```

### Update Basic
                           	 Settings of Alternate Extension

```
PUT https://<connection-server>/vmrest/users/<user-objectid>/alternateextensions/<objectid>
```

```
<AlternateExtension>
  <DtmfAccessId>999345c1</DtmfAccessId>
  <PartitionObjectId>e1c25917-7dbe-4691-8226-246f84edc73b</PartitionObjectId>
</AlternateExtension>
```

The following is the response from the above *PUT* request and the
                              		actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
PUT https://<connection-server>/vmrest/users/<user-objectid>/alternateextensions/<alternateextension_objectid>
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

```
{ 
"DtmfAccessId":"123345" 
}
```

The following is the response from the above *PUT* request and the
                              		actual response will depend upon the information given by you:

```
Response Code: 204
```

### Delete Alternate
                           	 Extension

```
DELETE https://<connection-server>/vmrest/users/<user-objectid>/alternateextensions/<alternateextension_objectid>
```

The following is the response from the above *DELETE* request and the
                              		actual response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

```
DELETE
https://<connection-server>/vmrest/users/<user-objectid>/alternateextensions/<alternateextension_objectid>
Accept: application/json Connection: keep-alive
```

The following is the response from the above *DELETE* request and the
                              		actual response will depend upon the information given by you:

```
Response code: 204
```

### Explanation of
                           	 Data Fields

### Explanation of
                           	 Data Fields: Advance Settings

Data Type

Possible Values can be:

- false: Cisco
                                                   						  Unity Connection will not request confirmation from a subscriber before
                                                   						  proceeding with a deletion of a single new or saved message.

- true: Cisco
                                                   						  Unity Connection will request confirmation from a subscriber before proceeding
                                                   						  with a deletion of a single new or saved message

Possible values:

- 0: Unity
                                                   						  Connection prompts subscribers to press 1 to add more recipients.

- 1: Unity
                                                   						  Connection does not prompt subscribers to press 1 to add more recipients.
                                                   						  Instead, subscribers continue entering recipient names or extensions (as
                                                   						  applicable) until they indicate that they have completed addressing.

- Changing this setting affects the Send and Forward flows
                                             						for all subscribers associated with the Unity Connection server, regardless of
                                             						subscriber conversation style and whether Unity Connection is set up to prompt
                                             						subscribers to record before or after addressing. - By enabling streamlined
                                             						addressing, forwarding messages to single recipients requires that subscribers
                                             						press an extra keystroke as when streamlined addressing is disabled.

Subscribers will not hear message counts, their own name,
                                             						top level menus, etc when this setting is active. Possible Values:

- false:
                                                   						  Subscriber conversation does not jump directly to first message in the message
                                                   						  stack after subscriber sign-in.

- true: Subscriber
                                                   						  conversation jumps directly to the first message in the message stack after
                                                   						  subscriber sign-in.

Possible Values: A value between 0 and 200 is allowed.

- Normal speed,
                                                   						  the speed at which messages are recorded is a value of 100.

- Twice as fast as
                                                   						  normal speed is a value of 200.

- Half as fast as
                                                   						  normal speed is a value of 50.

Possible Values: A value between 0 and 100 is allowed.

- Normal volume,
                                                   						  the volume used to record a message is a value of 50.

- Twice as loud is
                                                   						  a value of 100.

- Half as loud as
                                                   						  normal volume is a value of 25.

Note that the value is only used for message play back, not
                                             						for other parts of the conversation.

Possible Values:

- true

- false

Possible Values: A value between 0 and 200 is allowed.

- Normal speed,
                                                   						  the speed at which messages are recorded is a value of 100.

- Twice as fast as
                                                   						  normal speed is a value of 200.

- Half as fast as
                                                   						  normal speed is a value of 50.

Possible Values: A value between 0 and 100 is allowed.

- Normal volume,
                                                   						  the volume used to record a message is a value of 50.

- Twice as loud is
                                                   						  a value of 100.

- Half as loud as
                                                   						  normal volume is a value of 25.

Note that the value is only used for playback of system
                                             						prompts, not for other parts of the conversation.

Possible Values: 0-250

Possible values:

- true

- false

Possible Values:

- 0: Message is
                                                   						  not sent on hangup unless subscriber explictly issues the command to send the
                                                   						  message via DTMFor voice command.

- 1: Message is
                                                   						  sent on hangup if it has a recording and at least one valid recipient

- 2: Message is
                                                   						  saved as a draft message

Possible Values:

- false:
                                                   						  Subscriber will not be asked for their PIN when calling in from a known device.

- true: Subscriber
                                                   						  will be asked for their PIN when calling in from a known device.

Possible Values: 1000-60000

Possible Values: 300-0000

Possible Values: 0-100

Possible Values:

- false: Speech
                                                   						  recognition conversation is not default conversation for the subscriber.

- true: Speech
                                                   						  recognition conversation is the default conversation for the subscriber.

This is different from the voice-recognition class of
                                             						service which indicates that the subscriber is allowed to use the
                                             						voice-recognition conversation

| Field Name | Data Type | Operation | Description |
|---|---|---|---|
| URI | String | Read Only | URI of Alternate Extension |
| IdIndex | Read/Write | Integer | An index into the alternate extensions for
                                          					 a subscriber. Possible value can be 0-20. Admin-defined alternate extensions
                                          					 utilize the range of 1-10. User-defined alternate extensions utilize the range
                                          					 of 11-20. |
| DtmfAccessId | String(319) | Read/Write | The dialable number. |
| PartitionURI | String | Read Only | URI of partition to which the DtmfAccessId
                                          					 is assigned. |
| PartitionObjectId | String(36) | Read/Write | The unique identifier of the Partition to
                                          					 which the DtmfAccessId is assigned. |
| LocationObjectId | String(36) | Read/Write | The unique identifier of the Location
                                          					 object to which this location (denormalized) belongs. |
| ObjectId | String(36) | Read Only | The unique identifier of the Extension |
| DisplayName | String(64) | Read/Write | The text name of this DtmfAccessId to be
                                          					 used when displaying entries. |
| AlternateExtensionAdvancedURI | String | Read Only | URI for getting and setting the advanced
                                          					 settings of Alternate Extension |

| Field Name | Data Type | Operation | Description |
|---|---|---|---|
| URI | String | Read Only | URI of Advance setting of Alternate
                                          					 Extension |
| AddressMode | Integer | Read/Write | The default method the subscriber will use
                                          					 to address messages to other subscribers. This can be addressing by ID,
                                          					 addressing by first name then last name, or by last name and then first name.
                                          					 Possible Values can be 0-2. |
| CommandDigitTimeout | Integer | Read/Write | The amount of time (in milliseconds)
                                          					 between digits on a multiple digit menu command entry (i.e. different than the
                                          					 inter digit timeout that is used for strings of digits such as extensions and
                                          					 transfer strings). Possible Values can be 250-5000. |
| ConfirmationConfidenceThreshold | Integer | Read/Write | Voice Recognition Confirmation Confidence
                                          					 Threshold Possible Values can be 0-100. |
| ConfirmDeleteMessage | Boolean | Read/Write | A flag indicating whether Cisco Unity
                                          					 Connection will request confirmation from a subscriber before proceeding with a
                                          					 deletion of a single new or saved message. Possible Values can be: false: Cisco
                                                   						  Unity Connection will not request confirmation from a subscriber before
                                                   						  proceeding with a deletion of a single new or saved message. true: Cisco
                                                   						  Unity Connection will request confirmation from a subscriber before proceeding
                                                   						  with a deletion of a single new or saved message |
| ContinuousAddMode | Boolean | Read/Write | A flag indicating whether when addressing,
                                          					 after entering one recipient name, whether the subscriber is asked to enter
                                          					 another name or assume the subscriber is finished adding names and is ready to
                                          					 move on to recording the message or applying message options. Possible values: 0: Unity
                                                   						  Connection prompts subscribers to press 1 to add more recipients. 1: Unity
                                                   						  Connection does not prompt subscribers to press 1 to add more recipients.
                                                   						  Instead, subscribers continue entering recipient names or extensions (as
                                                   						  applicable) until they indicate that they have completed addressing. - Changing this setting affects the Send and Forward flows
                                             						for all subscribers associated with the Unity Connection server, regardless of
                                             						subscriber conversation style and whether Unity Connection is set up to prompt
                                             						subscribers to record before or after addressing. - By enabling streamlined
                                             						addressing, forwarding messages to single recipients requires that subscribers
                                             						press an extra keystroke as when streamlined addressing is disabled. |
| Device_DtmfAccessIdObjectId | String(36) | Read Only | The device to which this
                                          					 DeviceCustomConvSetting object belongs. The unique identifier of the
                                          					 DtmfAccessId object to which these setting apply. |
| FirstDigitTimeout | Integer | Read/Write | The amount of time to wait (in
                                          					 milliseconds) for first digit when collecting touchtone. Possible Values can be
                                          					 500-10000. |
| InterDigitDelay | Integer | Read/Write | The amount of time to wait (in
                                          					 milliseconds) for input between touch tones when collecting digits in touchtone
                                          					 conversation. Possible Values can be 1000-10000. |
| JumpToMessagesOnLogin | Boolean | Read/Write | A flag indicating whether the subscriber
                                          					 conversation jumps directly to the first message in the message stack after
                                          					 subscriber sign-in. Subscribers will not hear message counts, their own name,
                                             						top level menus, etc when this setting is active. Possible Values: false:
                                                   						  Subscriber conversation does not jump directly to first message in the message
                                                   						  stack after subscriber sign-in. true: Subscriber
                                                   						  conversation jumps directly to the first message in the message stack after
                                                   						  subscriber sign-in. |
| MessageSpeed | Integer | Read/Write | The audio speed Cisco Unity Connection uses
                                          					 to play back messages to the subscriber. Possible Values: A value between 0 and 200 is allowed. Normal speed,
                                                   						  the speed at which messages are recorded is a value of 100. Twice as fast as
                                                   						  normal speed is a value of 200. Half as fast as
                                                   						  normal speed is a value of 50. |
| MessageVolume | Integer | Read/Write | The audio volume expressed as a percentage
                                          					 that Cisco Unity Connection uses to play back message. Possible Values: A value between 0 and 100 is allowed. Normal volume,
                                                   						  the volume used to record a message is a value of 50. Twice as loud is
                                                   						  a value of 100. Half as loud as
                                                   						  normal volume is a value of 25. Note that the value is only used for message play back, not
                                             						for other parts of the conversation. |
| NameConfirmation | Boolean | Read/Write | Indicates whether the voice name of the
                                          					 subscriber or distribution list added to an address list when a subscriber
                                          					 addresses a message to other subscribers is played. Possible Values: true false |
| ObjectId | String(36) | Read Only | A globally unique, system-generated
                                          					 identifier for an object. |
| PromptSpeed | Integer | Read/Write | The audio speed Cisco Unity Connection uses
                                          					 to play back prompts to the subscriber. Possible Values: A value between 0 and 200 is allowed. Normal speed,
                                                   						  the speed at which messages are recorded is a value of 100. Twice as fast as
                                                   						  normal speed is a value of 200. Half as fast as
                                                   						  normal speed is a value of 50. |
| PromptVolume | Integer | Read/Write | The volume level for playback of system
                                          					 prompts. Possible Values: A value between 0 and 100 is allowed. Normal volume,
                                                   						  the volume used to record a message is a value of 50. Twice as loud is
                                                   						  a value of 100. Half as loud as
                                                   						  normal volume is a value of 25. Note that the value is only used for playback of system
                                             						prompts, not for other parts of the conversation. |
| RepeatMenu | Integer | Read/Write | The number of times to repeat a menu in
                                          					 touchtone. Possible Values: 0-250 |
| SaveMessageOnHangup | Boolean | Read/Write | A flag indicating when hanging up while
                                          					 listening to a new message, whether the message is marked new again or is
                                          					 marked read. Possible values: true false |
| SendMessageOnHangup | Integer | Read/Write | Indicates when hanging up while addressing
                                          					 a message that has a recording and at least one recipient, whether the message
                                          					 is discarded, saved or the message is sent. Possible Values: 0: Message is
                                                   						  not sent on hangup unless subscriber explictly issues the command to send the
                                                   						  message via DTMFor voice command. 1: Message is
                                                   						  sent on hangup if it has a recording and at least one valid recipient 2: Message is
                                                   						  saved as a draft message |
| SkipForwardTime | Integer | Read/Write | Indicates the amount of time (in
                                          					 milliseconds) to jump forward when skipping ahead in a voice or TTS message
                                          					 using either DTMF or voice commands while reviewing messages.Possible Values:
                                          					 1000-60000 |
| SkipPasswordForKnownDevice | Boolean | Read/Write | A flag indicating whether the subscriber
                                          					 will be asked for his/her PIN. Possible Values: false:
                                                   						  Subscriber will not be asked for their PIN when calling in from a known device. true: Subscriber
                                                   						  will be asked for their PIN when calling in from a known device. |
| SkipReverseTime | Integer | Read/Write | Indicates the amount of time (in
                                          					 milliseconds) to jump backward when skipping in reverse in a voice or TTS
                                          					 message using either DTMF or voice commands while reviewing messages. Possible Values: 1000-60000 |
| SpeechIncompleteTimeout | Integer | Read/Write | Specifies the required length of silence
                                          					 (in milliseconds) from when the speech prior to the silence matches an active
                                          					 grammar, but where it is possible to speak further and still match the grammar.
                                          					 By contrast, the SpeechCompleteTimeout property is used when the speech prior
                                          					 to the silence matches an active grammar and no further words can be spoken. Possible Values: 300-0000 |
| UserURI | String | Read Only | URI of the subscriber to which alternate
                                          					 extension belongs |
| SpeechSensitivity | Integer | Read/Write | A variable level of sound sensitivity that
                                          					 enables the speech engine to filter out background noise and not mistake it for
                                          					 speech. A higher value means higher sensitivity. Possible Values: 0-100 |
| SubscriberObjectId | String(36) | Read Only | Object id of Subscriber to which the
                                          					 Alternate Extension Belongs. |
| UseVui | Boolean | Read/Write | A flag indicating whether the speech
                                          					 recognition conversation is the default conversation for the subscriber. Possible Values: false: Speech
                                                   						  recognition conversation is not default conversation for the subscriber. true: Speech
                                                   						  recognition conversation is the default conversation for the subscriber. This is different from the voice-recognition class of
                                             						service which indicates that the subscriber is allowed to use the
                                             						voice-recognition conversation |